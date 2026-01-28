# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_intelligentcreation20240313 import models as main_models
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

    def add_text_feedback_with_options(
        self,
        request: main_models.AddTextFeedbackRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddTextFeedbackResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.quality):
            body['quality'] = request.quality
        if not DaraCore.is_null(request.text_id):
            body['textId'] = request.text_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddTextFeedback',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/addTextFeedback',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTextFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_text_feedback_with_options_async(
        self,
        request: main_models.AddTextFeedbackRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddTextFeedbackResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.quality):
            body['quality'] = request.quality
        if not DaraCore.is_null(request.text_id):
            body['textId'] = request.text_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddTextFeedback',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/addTextFeedback',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTextFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_text_feedback(
        self,
        request: main_models.AddTextFeedbackRequest,
    ) -> main_models.AddTextFeedbackResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_text_feedback_with_options(request, headers, runtime)

    async def add_text_feedback_async(
        self,
        request: main_models.AddTextFeedbackRequest,
    ) -> main_models.AddTextFeedbackResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_text_feedback_with_options_async(request, headers, runtime)

    def batch_add_document_with_options(
        self,
        knowledge_base_id: str,
        request: main_models.BatchAddDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchAddDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.add_document_infos):
            body['addDocumentInfos'] = request.add_document_infos
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchAddDocument',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/knowledge-base/{DaraURL.percent_encode(knowledge_base_id)}/documents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAddDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_document_with_options_async(
        self,
        knowledge_base_id: str,
        request: main_models.BatchAddDocumentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchAddDocumentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.add_document_infos):
            body['addDocumentInfos'] = request.add_document_infos
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchAddDocument',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/knowledge-base/{DaraURL.percent_encode(knowledge_base_id)}/documents',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchAddDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_document(
        self,
        knowledge_base_id: str,
        request: main_models.BatchAddDocumentRequest,
    ) -> main_models.BatchAddDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_add_document_with_options(knowledge_base_id, request, headers, runtime)

    async def batch_add_document_async(
        self,
        knowledge_base_id: str,
        request: main_models.BatchAddDocumentRequest,
    ) -> main_models.BatchAddDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_add_document_with_options_async(knowledge_base_id, request, headers, runtime)

    def batch_create_aicoach_task_with_options(
        self,
        request: main_models.BatchCreateAICoachTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchCreateAICoachTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.script_record_id):
            body['scriptRecordId'] = request.script_record_id
        if not DaraCore.is_null(request.student_ids):
            body['studentIds'] = request.student_ids
        if not DaraCore.is_null(request.student_list):
            body['studentList'] = request.student_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchCreateAICoachTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/batchCreateTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCreateAICoachTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_aicoach_task_with_options_async(
        self,
        request: main_models.BatchCreateAICoachTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchCreateAICoachTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.script_record_id):
            body['scriptRecordId'] = request.script_record_id
        if not DaraCore.is_null(request.student_ids):
            body['studentIds'] = request.student_ids
        if not DaraCore.is_null(request.student_list):
            body['studentList'] = request.student_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchCreateAICoachTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/batchCreateTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCreateAICoachTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_aicoach_task(
        self,
        request: main_models.BatchCreateAICoachTaskRequest,
    ) -> main_models.BatchCreateAICoachTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_create_aicoach_task_with_options(request, headers, runtime)

    async def batch_create_aicoach_task_async(
        self,
        request: main_models.BatchCreateAICoachTaskRequest,
    ) -> main_models.BatchCreateAICoachTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_create_aicoach_task_with_options_async(request, headers, runtime)

    def batch_delete_practice_task_with_options(
        self,
        tmp_req: main_models.BatchDeletePracticeTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeletePracticeTaskResponse:
        tmp_req.validate()
        request = main_models.BatchDeletePracticeTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'taskIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.idempotent_id):
            query['idempotentId'] = request.idempotent_id
        if not DaraCore.is_null(request.task_ids_shrink):
            query['taskIds'] = request.task_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeletePracticeTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/batchDeletePracticeTask',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeletePracticeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_practice_task_with_options_async(
        self,
        tmp_req: main_models.BatchDeletePracticeTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeletePracticeTaskResponse:
        tmp_req.validate()
        request = main_models.BatchDeletePracticeTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'taskIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.idempotent_id):
            query['idempotentId'] = request.idempotent_id
        if not DaraCore.is_null(request.task_ids_shrink):
            query['taskIds'] = request.task_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeletePracticeTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/batchDeletePracticeTask',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeletePracticeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_practice_task(
        self,
        request: main_models.BatchDeletePracticeTaskRequest,
    ) -> main_models.BatchDeletePracticeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_delete_practice_task_with_options(request, headers, runtime)

    async def batch_delete_practice_task_async(
        self,
        request: main_models.BatchDeletePracticeTaskRequest,
    ) -> main_models.BatchDeletePracticeTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_delete_practice_task_with_options_async(request, headers, runtime)

    def batch_get_project_task_with_options(
        self,
        tmp_req: main_models.BatchGetProjectTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetProjectTaskResponse:
        tmp_req.validate()
        request = main_models.BatchGetProjectTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_id_list):
            request.task_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_id_list, 'taskIdList', 'simple')
        query = {}
        if not DaraCore.is_null(request.task_id_list_shrink):
            query['taskIdList'] = request.task_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetProjectTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/project/batchGetProjectTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetProjectTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_project_task_with_options_async(
        self,
        tmp_req: main_models.BatchGetProjectTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetProjectTaskResponse:
        tmp_req.validate()
        request = main_models.BatchGetProjectTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_id_list):
            request.task_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_id_list, 'taskIdList', 'simple')
        query = {}
        if not DaraCore.is_null(request.task_id_list_shrink):
            query['taskIdList'] = request.task_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetProjectTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/project/batchGetProjectTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetProjectTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_project_task(
        self,
        request: main_models.BatchGetProjectTaskRequest,
    ) -> main_models.BatchGetProjectTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_get_project_task_with_options(request, headers, runtime)

    async def batch_get_project_task_async(
        self,
        request: main_models.BatchGetProjectTaskRequest,
    ) -> main_models.BatchGetProjectTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_get_project_task_with_options_async(request, headers, runtime)

    def batch_get_train_task_with_options(
        self,
        tmp_req: main_models.BatchGetTrainTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetTrainTaskResponse:
        tmp_req.validate()
        request = main_models.BatchGetTrainTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_id_list):
            request.task_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_id_list, 'taskIdList', 'simple')
        query = {}
        if not DaraCore.is_null(request.aliyun_main_id):
            query['aliyunMainId'] = request.aliyun_main_id
        if not DaraCore.is_null(request.task_id_list_shrink):
            query['taskIdList'] = request.task_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetTrainTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/train/task/batchGetTrainTaskInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetTrainTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_train_task_with_options_async(
        self,
        tmp_req: main_models.BatchGetTrainTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetTrainTaskResponse:
        tmp_req.validate()
        request = main_models.BatchGetTrainTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_id_list):
            request.task_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_id_list, 'taskIdList', 'simple')
        query = {}
        if not DaraCore.is_null(request.aliyun_main_id):
            query['aliyunMainId'] = request.aliyun_main_id
        if not DaraCore.is_null(request.task_id_list_shrink):
            query['taskIdList'] = request.task_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetTrainTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/train/task/batchGetTrainTaskInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetTrainTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_train_task(
        self,
        request: main_models.BatchGetTrainTaskRequest,
    ) -> main_models.BatchGetTrainTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_get_train_task_with_options(request, headers, runtime)

    async def batch_get_train_task_async(
        self,
        request: main_models.BatchGetTrainTaskRequest,
    ) -> main_models.BatchGetTrainTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_get_train_task_with_options_async(request, headers, runtime)

    def batch_get_video_clip_task_with_options(
        self,
        tmp_req: main_models.BatchGetVideoClipTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetVideoClipTaskResponse:
        tmp_req.validate()
        request = main_models.BatchGetVideoClipTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_id_list):
            request.task_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_id_list, 'taskIdList', 'simple')
        query = {}
        if not DaraCore.is_null(request.task_id_list_shrink):
            query['taskIdList'] = request.task_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetVideoClipTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/video/clip/batchGetVideoClipTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetVideoClipTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_video_clip_task_with_options_async(
        self,
        tmp_req: main_models.BatchGetVideoClipTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetVideoClipTaskResponse:
        tmp_req.validate()
        request = main_models.BatchGetVideoClipTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_id_list):
            request.task_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_id_list, 'taskIdList', 'simple')
        query = {}
        if not DaraCore.is_null(request.task_id_list_shrink):
            query['taskIdList'] = request.task_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetVideoClipTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/video/clip/batchGetVideoClipTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetVideoClipTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_video_clip_task(
        self,
        request: main_models.BatchGetVideoClipTaskRequest,
    ) -> main_models.BatchGetVideoClipTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_get_video_clip_task_with_options(request, headers, runtime)

    async def batch_get_video_clip_task_async(
        self,
        request: main_models.BatchGetVideoClipTaskRequest,
    ) -> main_models.BatchGetVideoClipTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_get_video_clip_task_with_options_async(request, headers, runtime)

    def batch_query_individuation_text_with_options(
        self,
        tmp_req: main_models.BatchQueryIndividuationTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchQueryIndividuationTextResponse:
        tmp_req.validate()
        request = main_models.BatchQueryIndividuationTextShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.text_id_list):
            request.text_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.text_id_list, 'textIdList', 'simple')
        query = {}
        if not DaraCore.is_null(request.text_id_list_shrink):
            query['textIdList'] = request.text_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQueryIndividuationText',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/individuationText/batchQueryText',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQueryIndividuationTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_query_individuation_text_with_options_async(
        self,
        tmp_req: main_models.BatchQueryIndividuationTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchQueryIndividuationTextResponse:
        tmp_req.validate()
        request = main_models.BatchQueryIndividuationTextShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.text_id_list):
            request.text_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.text_id_list, 'textIdList', 'simple')
        query = {}
        if not DaraCore.is_null(request.text_id_list_shrink):
            query['textIdList'] = request.text_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchQueryIndividuationText',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/individuationText/batchQueryText',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchQueryIndividuationTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_query_individuation_text(
        self,
        request: main_models.BatchQueryIndividuationTextRequest,
    ) -> main_models.BatchQueryIndividuationTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_query_individuation_text_with_options(request, headers, runtime)

    async def batch_query_individuation_text_async(
        self,
        request: main_models.BatchQueryIndividuationTextRequest,
    ) -> main_models.BatchQueryIndividuationTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_query_individuation_text_with_options_async(request, headers, runtime)

    def build_aicoach_script_record_with_options(
        self,
        request: main_models.BuildAICoachScriptRecordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BuildAICoachScriptRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.script_json_url):
            body['scriptJsonUrl'] = request.script_json_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BuildAICoachScriptRecord',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/buildScriptRecord',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BuildAICoachScriptRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def build_aicoach_script_record_with_options_async(
        self,
        request: main_models.BuildAICoachScriptRecordRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BuildAICoachScriptRecordResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.script_json_url):
            body['scriptJsonUrl'] = request.script_json_url
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BuildAICoachScriptRecord',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/buildScriptRecord',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BuildAICoachScriptRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def build_aicoach_script_record(
        self,
        request: main_models.BuildAICoachScriptRecordRequest,
    ) -> main_models.BuildAICoachScriptRecordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.build_aicoach_script_record_with_options(request, headers, runtime)

    async def build_aicoach_script_record_async(
        self,
        request: main_models.BuildAICoachScriptRecordRequest,
    ) -> main_models.BuildAICoachScriptRecordResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.build_aicoach_script_record_with_options_async(request, headers, runtime)

    def check_session_with_options(
        self,
        request: main_models.CheckSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckSession',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/checkSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_session_with_options_async(
        self,
        request: main_models.CheckSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckSession',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/checkSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_session(
        self,
        request: main_models.CheckSessionRequest,
    ) -> main_models.CheckSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_session_with_options(request, headers, runtime)

    async def check_session_async(
        self,
        request: main_models.CheckSessionRequest,
    ) -> main_models.CheckSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_session_with_options_async(request, headers, runtime)

    def close_aicoach_task_session_with_options(
        self,
        request: main_models.CloseAICoachTaskSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloseAICoachTaskSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.uid):
            body['uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloseAICoachTaskSession',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/closeSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseAICoachTaskSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_aicoach_task_session_with_options_async(
        self,
        request: main_models.CloseAICoachTaskSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CloseAICoachTaskSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.uid):
            body['uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloseAICoachTaskSession',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/closeSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseAICoachTaskSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_aicoach_task_session(
        self,
        request: main_models.CloseAICoachTaskSessionRequest,
    ) -> main_models.CloseAICoachTaskSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.close_aicoach_task_session_with_options(request, headers, runtime)

    async def close_aicoach_task_session_async(
        self,
        request: main_models.CloseAICoachTaskSessionRequest,
    ) -> main_models.CloseAICoachTaskSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.close_aicoach_task_session_with_options_async(request, headers, runtime)

    def count_text_with_options(
        self,
        request: main_models.CountTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CountTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.generation_source):
            query['generationSource'] = request.generation_source
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.publish_status):
            query['publishStatus'] = request.publish_status
        if not DaraCore.is_null(request.style):
            query['style'] = request.style
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CountText',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/countText',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CountTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_text_with_options_async(
        self,
        request: main_models.CountTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CountTextResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.generation_source):
            query['generationSource'] = request.generation_source
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.publish_status):
            query['publishStatus'] = request.publish_status
        if not DaraCore.is_null(request.style):
            query['style'] = request.style
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CountText',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/countText',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CountTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_text(
        self,
        request: main_models.CountTextRequest,
    ) -> main_models.CountTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.count_text_with_options(request, headers, runtime)

    async def count_text_async(
        self,
        request: main_models.CountTextRequest,
    ) -> main_models.CountTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.count_text_with_options_async(request, headers, runtime)

    def create_aicoach_task_with_options(
        self,
        request: main_models.CreateAICoachTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAICoachTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.script_record_id):
            body['scriptRecordId'] = request.script_record_id
        if not DaraCore.is_null(request.student_audio_url):
            body['studentAudioUrl'] = request.student_audio_url
        if not DaraCore.is_null(request.student_id):
            body['studentId'] = request.student_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAICoachTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/createTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAICoachTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aicoach_task_with_options_async(
        self,
        request: main_models.CreateAICoachTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAICoachTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.script_record_id):
            body['scriptRecordId'] = request.script_record_id
        if not DaraCore.is_null(request.student_audio_url):
            body['studentAudioUrl'] = request.student_audio_url
        if not DaraCore.is_null(request.student_id):
            body['studentId'] = request.student_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAICoachTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/createTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAICoachTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aicoach_task(
        self,
        request: main_models.CreateAICoachTaskRequest,
    ) -> main_models.CreateAICoachTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_aicoach_task_with_options(request, headers, runtime)

    async def create_aicoach_task_async(
        self,
        request: main_models.CreateAICoachTaskRequest,
    ) -> main_models.CreateAICoachTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_aicoach_task_with_options_async(request, headers, runtime)

    def create_aicoach_task_session_with_options(
        self,
        request: main_models.CreateAICoachTaskSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAICoachTaskSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.uid):
            body['uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAICoachTaskSession',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/startSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAICoachTaskSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aicoach_task_session_with_options_async(
        self,
        request: main_models.CreateAICoachTaskSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAICoachTaskSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        if not DaraCore.is_null(request.uid):
            body['uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAICoachTaskSession',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/startSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAICoachTaskSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aicoach_task_session(
        self,
        request: main_models.CreateAICoachTaskSessionRequest,
    ) -> main_models.CreateAICoachTaskSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_aicoach_task_session_with_options(request, headers, runtime)

    async def create_aicoach_task_session_async(
        self,
        request: main_models.CreateAICoachTaskSessionRequest,
    ) -> main_models.CreateAICoachTaskSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_aicoach_task_session_with_options_async(request, headers, runtime)

    def create_agent_with_options(
        self,
        request: main_models.CreateAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_icon_url):
            body['agentIconUrl'] = request.agent_icon_url
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.agent_scene):
            body['agentScene'] = request.agent_scene
        if not DaraCore.is_null(request.character_age_stage):
            body['characterAgeStage'] = request.character_age_stage
        if not DaraCore.is_null(request.character_gender):
            body['characterGender'] = request.character_gender
        if not DaraCore.is_null(request.character_name):
            body['characterName'] = request.character_name
        if not DaraCore.is_null(request.extra_description):
            body['extraDescription'] = request.extra_description
        if not DaraCore.is_null(request.industry):
            body['industry'] = request.industry
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgent',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/agent/createAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_agent_with_options_async(
        self,
        request: main_models.CreateAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_icon_url):
            body['agentIconUrl'] = request.agent_icon_url
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.agent_scene):
            body['agentScene'] = request.agent_scene
        if not DaraCore.is_null(request.character_age_stage):
            body['characterAgeStage'] = request.character_age_stage
        if not DaraCore.is_null(request.character_gender):
            body['characterGender'] = request.character_gender
        if not DaraCore.is_null(request.character_name):
            body['characterName'] = request.character_name
        if not DaraCore.is_null(request.extra_description):
            body['extraDescription'] = request.extra_description
        if not DaraCore.is_null(request.industry):
            body['industry'] = request.industry
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgent',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/agent/createAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_agent(
        self,
        request: main_models.CreateAgentRequest,
    ) -> main_models.CreateAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_agent_with_options(request, headers, runtime)

    async def create_agent_async(
        self,
        request: main_models.CreateAgentRequest,
    ) -> main_models.CreateAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_agent_with_options_async(request, headers, runtime)

    def create_anchor_with_options(
        self,
        request: main_models.CreateAnchorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnchorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.anchor_category):
            body['anchorCategory'] = request.anchor_category
        if not DaraCore.is_null(request.anchor_material_name):
            body['anchorMaterialName'] = request.anchor_material_name
        if not DaraCore.is_null(request.cover_url):
            body['coverUrl'] = request.cover_url
        if not DaraCore.is_null(request.digital_human_type):
            body['digitalHumanType'] = request.digital_human_type
        if not DaraCore.is_null(request.gender):
            body['gender'] = request.gender
        if not DaraCore.is_null(request.use_scene):
            body['useScene'] = request.use_scene
        if not DaraCore.is_null(request.video_oss_key):
            body['videoOssKey'] = request.video_oss_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnchor',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/anchorOpen/createAnchor',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnchorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_anchor_with_options_async(
        self,
        request: main_models.CreateAnchorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnchorResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.anchor_category):
            body['anchorCategory'] = request.anchor_category
        if not DaraCore.is_null(request.anchor_material_name):
            body['anchorMaterialName'] = request.anchor_material_name
        if not DaraCore.is_null(request.cover_url):
            body['coverUrl'] = request.cover_url
        if not DaraCore.is_null(request.digital_human_type):
            body['digitalHumanType'] = request.digital_human_type
        if not DaraCore.is_null(request.gender):
            body['gender'] = request.gender
        if not DaraCore.is_null(request.use_scene):
            body['useScene'] = request.use_scene
        if not DaraCore.is_null(request.video_oss_key):
            body['videoOssKey'] = request.video_oss_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnchor',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/anchorOpen/createAnchor',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnchorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_anchor(
        self,
        request: main_models.CreateAnchorRequest,
    ) -> main_models.CreateAnchorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_anchor_with_options(request, headers, runtime)

    async def create_anchor_async(
        self,
        request: main_models.CreateAnchorRequest,
    ) -> main_models.CreateAnchorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_anchor_with_options_async(request, headers, runtime)

    def create_illustration_task_with_options(
        self,
        text_id: str,
        request: main_models.CreateIllustrationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIllustrationTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIllustrationTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/texts/{DaraURL.percent_encode(text_id)}/illustrationTasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIllustrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_illustration_task_with_options_async(
        self,
        text_id: str,
        request: main_models.CreateIllustrationTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIllustrationTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIllustrationTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/texts/{DaraURL.percent_encode(text_id)}/illustrationTasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIllustrationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_illustration_task(
        self,
        text_id: str,
        request: main_models.CreateIllustrationTaskRequest,
    ) -> main_models.CreateIllustrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_illustration_task_with_options(text_id, request, headers, runtime)

    async def create_illustration_task_async(
        self,
        text_id: str,
        request: main_models.CreateIllustrationTaskRequest,
    ) -> main_models.CreateIllustrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_illustration_task_with_options_async(text_id, request, headers, runtime)

    def create_individuation_project_with_options(
        self,
        request: main_models.CreateIndividuationProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIndividuationProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_info):
            body['projectInfo'] = request.project_info
        if not DaraCore.is_null(request.project_name):
            body['projectName'] = request.project_name
        if not DaraCore.is_null(request.purpose):
            body['purpose'] = request.purpose
        if not DaraCore.is_null(request.scene_id):
            body['sceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIndividuationProject',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/individuationText/createProject',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIndividuationProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_individuation_project_with_options_async(
        self,
        request: main_models.CreateIndividuationProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIndividuationProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_info):
            body['projectInfo'] = request.project_info
        if not DaraCore.is_null(request.project_name):
            body['projectName'] = request.project_name
        if not DaraCore.is_null(request.purpose):
            body['purpose'] = request.purpose
        if not DaraCore.is_null(request.scene_id):
            body['sceneId'] = request.scene_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIndividuationProject',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/individuationText/createProject',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIndividuationProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_individuation_project(
        self,
        request: main_models.CreateIndividuationProjectRequest,
    ) -> main_models.CreateIndividuationProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_individuation_project_with_options(request, headers, runtime)

    async def create_individuation_project_async(
        self,
        request: main_models.CreateIndividuationProjectRequest,
    ) -> main_models.CreateIndividuationProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_individuation_project_with_options_async(request, headers, runtime)

    def create_individuation_text_task_with_options(
        self,
        request: main_models.CreateIndividuationTextTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIndividuationTextTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.crowd_pack):
            body['crowdPack'] = request.crowd_pack
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIndividuationTextTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/individuationText/createTextTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIndividuationTextTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_individuation_text_task_with_options_async(
        self,
        request: main_models.CreateIndividuationTextTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateIndividuationTextTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.crowd_pack):
            body['crowdPack'] = request.crowd_pack
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.task_name):
            body['taskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIndividuationTextTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/individuationText/createTextTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIndividuationTextTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_individuation_text_task(
        self,
        request: main_models.CreateIndividuationTextTaskRequest,
    ) -> main_models.CreateIndividuationTextTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_individuation_text_task_with_options(request, headers, runtime)

    async def create_individuation_text_task_async(
        self,
        request: main_models.CreateIndividuationTextTaskRequest,
    ) -> main_models.CreateIndividuationTextTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_individuation_text_task_with_options_async(request, headers, runtime)

    def create_product_image_with_options(
        self,
        request: main_models.CreateProductImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.background_description):
            body['backgroundDescription'] = request.background_description
        if not DaraCore.is_null(request.background_priority):
            body['backgroundPriority'] = request.background_priority
        if not DaraCore.is_null(request.background_url):
            body['backgroundUrl'] = request.background_url
        if not DaraCore.is_null(request.highlight_text):
            body['highlightText'] = request.highlight_text
        if not DaraCore.is_null(request.image_count):
            body['imageCount'] = request.image_count
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.sub_title):
            body['subTitle'] = request.sub_title
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProductImage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/images/products',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProductImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_image_with_options_async(
        self,
        request: main_models.CreateProductImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductImageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.background_description):
            body['backgroundDescription'] = request.background_description
        if not DaraCore.is_null(request.background_priority):
            body['backgroundPriority'] = request.background_priority
        if not DaraCore.is_null(request.background_url):
            body['backgroundUrl'] = request.background_url
        if not DaraCore.is_null(request.highlight_text):
            body['highlightText'] = request.highlight_text
        if not DaraCore.is_null(request.image_count):
            body['imageCount'] = request.image_count
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.sub_title):
            body['subTitle'] = request.sub_title
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProductImage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/images/products',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProductImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product_image(
        self,
        request: main_models.CreateProductImageRequest,
    ) -> main_models.CreateProductImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_product_image_with_options(request, headers, runtime)

    async def create_product_image_async(
        self,
        request: main_models.CreateProductImageRequest,
    ) -> main_models.CreateProductImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_product_image_with_options_async(request, headers, runtime)

    def create_realistic_portrait_with_options(
        self,
        request: main_models.CreateRealisticPortraitRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRealisticPortraitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ages):
            body['ages'] = request.ages
        if not DaraCore.is_null(request.cloth):
            body['cloth'] = request.cloth
        if not DaraCore.is_null(request.color):
            body['color'] = request.color
        if not DaraCore.is_null(request.custom):
            body['custom'] = request.custom
        if not DaraCore.is_null(request.face):
            body['face'] = request.face
        if not DaraCore.is_null(request.figure):
            body['figure'] = request.figure
        if not DaraCore.is_null(request.gender):
            body['gender'] = request.gender
        if not DaraCore.is_null(request.hair_color):
            body['hairColor'] = request.hair_color
        if not DaraCore.is_null(request.hairstyle):
            body['hairstyle'] = request.hairstyle
        if not DaraCore.is_null(request.height):
            body['height'] = request.height
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.numbers):
            body['numbers'] = request.numbers
        if not DaraCore.is_null(request.ratio):
            body['ratio'] = request.ratio
        if not DaraCore.is_null(request.width):
            body['width'] = request.width
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRealisticPortrait',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/images/portrait/realistic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRealisticPortraitResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_realistic_portrait_with_options_async(
        self,
        request: main_models.CreateRealisticPortraitRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRealisticPortraitResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.ages):
            body['ages'] = request.ages
        if not DaraCore.is_null(request.cloth):
            body['cloth'] = request.cloth
        if not DaraCore.is_null(request.color):
            body['color'] = request.color
        if not DaraCore.is_null(request.custom):
            body['custom'] = request.custom
        if not DaraCore.is_null(request.face):
            body['face'] = request.face
        if not DaraCore.is_null(request.figure):
            body['figure'] = request.figure
        if not DaraCore.is_null(request.gender):
            body['gender'] = request.gender
        if not DaraCore.is_null(request.hair_color):
            body['hairColor'] = request.hair_color
        if not DaraCore.is_null(request.hairstyle):
            body['hairstyle'] = request.hairstyle
        if not DaraCore.is_null(request.height):
            body['height'] = request.height
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.numbers):
            body['numbers'] = request.numbers
        if not DaraCore.is_null(request.ratio):
            body['ratio'] = request.ratio
        if not DaraCore.is_null(request.width):
            body['width'] = request.width
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRealisticPortrait',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/images/portrait/realistic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRealisticPortraitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_realistic_portrait(
        self,
        request: main_models.CreateRealisticPortraitRequest,
    ) -> main_models.CreateRealisticPortraitResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_realistic_portrait_with_options(request, headers, runtime)

    async def create_realistic_portrait_async(
        self,
        request: main_models.CreateRealisticPortraitRequest,
    ) -> main_models.CreateRealisticPortraitResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_realistic_portrait_with_options_async(request, headers, runtime)

    def create_text_task_with_options(
        self,
        request: main_models.CreateTextTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTextTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTextTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/textTasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTextTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_text_task_with_options_async(
        self,
        request: main_models.CreateTextTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTextTaskResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTextTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/textTasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTextTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_text_task(
        self,
        request: main_models.CreateTextTaskRequest,
    ) -> main_models.CreateTextTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_text_task_with_options(request, headers, runtime)

    async def create_text_task_async(
        self,
        request: main_models.CreateTextTaskRequest,
    ) -> main_models.CreateTextTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_text_task_with_options_async(request, headers, runtime)

    def create_train_task_with_options(
        self,
        request: main_models.CreateTrainTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrainTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aliyun_main_id):
            body['aliyunMainId'] = request.aliyun_main_id
        if not DaraCore.is_null(request.res_spec_type):
            body['resSpecType'] = request.res_spec_type
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        if not DaraCore.is_null(request.use_scene):
            body['useScene'] = request.use_scene
        if not DaraCore.is_null(request.voice_gender):
            body['voiceGender'] = request.voice_gender
        if not DaraCore.is_null(request.voice_language):
            body['voiceLanguage'] = request.voice_language
        if not DaraCore.is_null(request.voice_name):
            body['voiceName'] = request.voice_name
        if not DaraCore.is_null(request.voice_path):
            body['voicePath'] = request.voice_path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrainTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/train/task/createTrainTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrainTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_train_task_with_options_async(
        self,
        request: main_models.CreateTrainTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTrainTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aliyun_main_id):
            body['aliyunMainId'] = request.aliyun_main_id
        if not DaraCore.is_null(request.res_spec_type):
            body['resSpecType'] = request.res_spec_type
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        if not DaraCore.is_null(request.use_scene):
            body['useScene'] = request.use_scene
        if not DaraCore.is_null(request.voice_gender):
            body['voiceGender'] = request.voice_gender
        if not DaraCore.is_null(request.voice_language):
            body['voiceLanguage'] = request.voice_language
        if not DaraCore.is_null(request.voice_name):
            body['voiceName'] = request.voice_name
        if not DaraCore.is_null(request.voice_path):
            body['voicePath'] = request.voice_path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrainTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/train/task/createTrainTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTrainTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_train_task(
        self,
        request: main_models.CreateTrainTaskRequest,
    ) -> main_models.CreateTrainTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_train_task_with_options(request, headers, runtime)

    async def create_train_task_async(
        self,
        request: main_models.CreateTrainTaskRequest,
    ) -> main_models.CreateTrainTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_train_task_with_options_async(request, headers, runtime)

    def create_video_clip_task_with_options(
        self,
        request: main_models.CreateVideoClipTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoClipTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aliyun_main_id):
            body['aliyunMainId'] = request.aliyun_main_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.oss_keys):
            body['ossKeys'] = request.oss_keys
        if not DaraCore.is_null(request.requirement):
            body['requirement'] = request.requirement
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoClipTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/video/clip/createVideoClipTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoClipTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_clip_task_with_options_async(
        self,
        request: main_models.CreateVideoClipTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoClipTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.aliyun_main_id):
            body['aliyunMainId'] = request.aliyun_main_id
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.oss_keys):
            body['ossKeys'] = request.oss_keys
        if not DaraCore.is_null(request.requirement):
            body['requirement'] = request.requirement
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoClipTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/video/clip/createVideoClipTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoClipTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_clip_task(
        self,
        request: main_models.CreateVideoClipTaskRequest,
    ) -> main_models.CreateVideoClipTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_video_clip_task_with_options(request, headers, runtime)

    async def create_video_clip_task_async(
        self,
        request: main_models.CreateVideoClipTaskRequest,
    ) -> main_models.CreateVideoClipTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_video_clip_task_with_options_async(request, headers, runtime)

    def delete_aicoach_script_with_options(
        self,
        request: main_models.DeleteAICoachScriptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAICoachScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.script_id):
            body['scriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAICoachScript',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/deleteAICoachScript',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAICoachScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_aicoach_script_with_options_async(
        self,
        request: main_models.DeleteAICoachScriptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAICoachScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.script_id):
            body['scriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAICoachScript',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/deleteAICoachScript',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAICoachScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_aicoach_script(
        self,
        request: main_models.DeleteAICoachScriptRequest,
    ) -> main_models.DeleteAICoachScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_aicoach_script_with_options(request, headers, runtime)

    async def delete_aicoach_script_async(
        self,
        request: main_models.DeleteAICoachScriptRequest,
    ) -> main_models.DeleteAICoachScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_aicoach_script_with_options_async(request, headers, runtime)

    def delete_agent_with_options(
        self,
        request: main_models.DeleteAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgent',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/agent/deleteAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_agent_with_options_async(
        self,
        request: main_models.DeleteAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAgent',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/agent/deleteAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_agent(
        self,
        request: main_models.DeleteAgentRequest,
    ) -> main_models.DeleteAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_agent_with_options(request, headers, runtime)

    async def delete_agent_async(
        self,
        request: main_models.DeleteAgentRequest,
    ) -> main_models.DeleteAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_agent_with_options_async(request, headers, runtime)

    def delete_individuation_project_with_options(
        self,
        request: main_models.DeleteIndividuationProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndividuationProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndividuationProject',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/individuationText/deleteProject',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIndividuationProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_individuation_project_with_options_async(
        self,
        request: main_models.DeleteIndividuationProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndividuationProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndividuationProject',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/individuationText/deleteProject',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIndividuationProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_individuation_project(
        self,
        request: main_models.DeleteIndividuationProjectRequest,
    ) -> main_models.DeleteIndividuationProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_individuation_project_with_options(request, headers, runtime)

    async def delete_individuation_project_async(
        self,
        request: main_models.DeleteIndividuationProjectRequest,
    ) -> main_models.DeleteIndividuationProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_individuation_project_with_options_async(request, headers, runtime)

    def delete_individuation_text_with_options(
        self,
        request: main_models.DeleteIndividuationTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndividuationTextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.text_id_list):
            body['textIdList'] = request.text_id_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndividuationText',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/individuationText/deleteText',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIndividuationTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_individuation_text_with_options_async(
        self,
        request: main_models.DeleteIndividuationTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIndividuationTextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.text_id_list):
            body['textIdList'] = request.text_id_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIndividuationText',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/individuationText/deleteText',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIndividuationTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_individuation_text(
        self,
        request: main_models.DeleteIndividuationTextRequest,
    ) -> main_models.DeleteIndividuationTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_individuation_text_with_options(request, headers, runtime)

    async def delete_individuation_text_async(
        self,
        request: main_models.DeleteIndividuationTextRequest,
    ) -> main_models.DeleteIndividuationTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_individuation_text_with_options_async(request, headers, runtime)

    def describe_document_with_options(
        self,
        knowledge_base_id: str,
        document_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocumentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeDocument',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/knowledge-base/{DaraURL.percent_encode(knowledge_base_id)}/documents/{DaraURL.percent_encode(document_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocumentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_document_with_options_async(
        self,
        knowledge_base_id: str,
        document_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDocumentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeDocument',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/knowledge-base/{DaraURL.percent_encode(knowledge_base_id)}/documents/{DaraURL.percent_encode(document_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDocumentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_document(
        self,
        knowledge_base_id: str,
        document_id: str,
    ) -> main_models.DescribeDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_document_with_options(knowledge_base_id, document_id, headers, runtime)

    async def describe_document_async(
        self,
        knowledge_base_id: str,
        document_id: str,
    ) -> main_models.DescribeDocumentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_document_with_options_async(knowledge_base_id, document_id, headers, runtime)

    def finish_aicoach_task_session_with_options(
        self,
        request: main_models.FinishAICoachTaskSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FinishAICoachTaskSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.uid):
            body['uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FinishAICoachTaskSession',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/finishSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FinishAICoachTaskSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def finish_aicoach_task_session_with_options_async(
        self,
        request: main_models.FinishAICoachTaskSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FinishAICoachTaskSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.uid):
            body['uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FinishAICoachTaskSession',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/finishSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FinishAICoachTaskSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def finish_aicoach_task_session(
        self,
        request: main_models.FinishAICoachTaskSessionRequest,
    ) -> main_models.FinishAICoachTaskSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.finish_aicoach_task_session_with_options(request, headers, runtime)

    async def finish_aicoach_task_session_async(
        self,
        request: main_models.FinishAICoachTaskSessionRequest,
    ) -> main_models.FinishAICoachTaskSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.finish_aicoach_task_session_with_options_async(request, headers, runtime)

    def get_aicoach_assessment_point_with_options(
        self,
        request: main_models.GetAICoachAssessmentPointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAICoachAssessmentPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.point_id):
            query['pointId'] = request.point_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAICoachAssessmentPoint',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/getAssessmentPoint',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAICoachAssessmentPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aicoach_assessment_point_with_options_async(
        self,
        request: main_models.GetAICoachAssessmentPointRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAICoachAssessmentPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.point_id):
            query['pointId'] = request.point_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAICoachAssessmentPoint',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/getAssessmentPoint',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAICoachAssessmentPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aicoach_assessment_point(
        self,
        request: main_models.GetAICoachAssessmentPointRequest,
    ) -> main_models.GetAICoachAssessmentPointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_aicoach_assessment_point_with_options(request, headers, runtime)

    async def get_aicoach_assessment_point_async(
        self,
        request: main_models.GetAICoachAssessmentPointRequest,
    ) -> main_models.GetAICoachAssessmentPointResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_aicoach_assessment_point_with_options_async(request, headers, runtime)

    def get_aicoach_cheat_detection_with_options(
        self,
        request: main_models.GetAICoachCheatDetectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAICoachCheatDetectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAICoachCheatDetection',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/getCheatDetection',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAICoachCheatDetectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aicoach_cheat_detection_with_options_async(
        self,
        request: main_models.GetAICoachCheatDetectionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAICoachCheatDetectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAICoachCheatDetection',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/getCheatDetection',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAICoachCheatDetectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aicoach_cheat_detection(
        self,
        request: main_models.GetAICoachCheatDetectionRequest,
    ) -> main_models.GetAICoachCheatDetectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_aicoach_cheat_detection_with_options(request, headers, runtime)

    async def get_aicoach_cheat_detection_async(
        self,
        request: main_models.GetAICoachCheatDetectionRequest,
    ) -> main_models.GetAICoachCheatDetectionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_aicoach_cheat_detection_with_options_async(request, headers, runtime)

    def get_aicoach_script_with_options(
        self,
        request: main_models.GetAICoachScriptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAICoachScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.script_record_id):
            query['scriptRecordId'] = request.script_record_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAICoachScript',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/getScript',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAICoachScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aicoach_script_with_options_async(
        self,
        request: main_models.GetAICoachScriptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAICoachScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.script_record_id):
            query['scriptRecordId'] = request.script_record_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAICoachScript',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/getScript',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAICoachScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aicoach_script(
        self,
        request: main_models.GetAICoachScriptRequest,
    ) -> main_models.GetAICoachScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_aicoach_script_with_options(request, headers, runtime)

    async def get_aicoach_script_async(
        self,
        request: main_models.GetAICoachScriptRequest,
    ) -> main_models.GetAICoachScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_aicoach_script_with_options_async(request, headers, runtime)

    def get_aicoach_task_session_history_with_options(
        self,
        request: main_models.GetAICoachTaskSessionHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAICoachTaskSessionHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.uid):
            query['uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAICoachTaskSessionHistory',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/querySessionHistory',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAICoachTaskSessionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aicoach_task_session_history_with_options_async(
        self,
        request: main_models.GetAICoachTaskSessionHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAICoachTaskSessionHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.uid):
            query['uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAICoachTaskSessionHistory',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/querySessionHistory',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAICoachTaskSessionHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aicoach_task_session_history(
        self,
        request: main_models.GetAICoachTaskSessionHistoryRequest,
    ) -> main_models.GetAICoachTaskSessionHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_aicoach_task_session_history_with_options(request, headers, runtime)

    async def get_aicoach_task_session_history_async(
        self,
        request: main_models.GetAICoachTaskSessionHistoryRequest,
    ) -> main_models.GetAICoachTaskSessionHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_aicoach_task_session_history_with_options_async(request, headers, runtime)

    def get_aicoach_task_session_report_with_options(
        self,
        request: main_models.GetAICoachTaskSessionReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAICoachTaskSessionReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.uid):
            query['uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAICoachTaskSessionReport',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/queryTaskSessionReport',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAICoachTaskSessionReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aicoach_task_session_report_with_options_async(
        self,
        request: main_models.GetAICoachTaskSessionReportRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAICoachTaskSessionReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.uid):
            query['uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAICoachTaskSessionReport',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/queryTaskSessionReport',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAICoachTaskSessionReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aicoach_task_session_report(
        self,
        request: main_models.GetAICoachTaskSessionReportRequest,
    ) -> main_models.GetAICoachTaskSessionReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_aicoach_task_session_report_with_options(request, headers, runtime)

    async def get_aicoach_task_session_report_async(
        self,
        request: main_models.GetAICoachTaskSessionReportRequest,
    ) -> main_models.GetAICoachTaskSessionReportResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_aicoach_task_session_report_with_options_async(request, headers, runtime)

    def get_aicoach_task_session_resource_usage_with_options(
        self,
        request: main_models.GetAICoachTaskSessionResourceUsageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAICoachTaskSessionResourceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAICoachTaskSessionResourceUsage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/getSessionResourceUsage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAICoachTaskSessionResourceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aicoach_task_session_resource_usage_with_options_async(
        self,
        request: main_models.GetAICoachTaskSessionResourceUsageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAICoachTaskSessionResourceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAICoachTaskSessionResourceUsage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/getSessionResourceUsage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAICoachTaskSessionResourceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aicoach_task_session_resource_usage(
        self,
        request: main_models.GetAICoachTaskSessionResourceUsageRequest,
    ) -> main_models.GetAICoachTaskSessionResourceUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_aicoach_task_session_resource_usage_with_options(request, headers, runtime)

    async def get_aicoach_task_session_resource_usage_async(
        self,
        request: main_models.GetAICoachTaskSessionResourceUsageRequest,
    ) -> main_models.GetAICoachTaskSessionResourceUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_aicoach_task_session_resource_usage_with_options_async(request, headers, runtime)

    def get_illustration_with_options(
        self,
        text_id: str,
        illustration_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIllustrationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIllustration',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/texts/{DaraURL.percent_encode(text_id)}/illustrations/{DaraURL.percent_encode(illustration_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIllustrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_illustration_with_options_async(
        self,
        text_id: str,
        illustration_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIllustrationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIllustration',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/texts/{DaraURL.percent_encode(text_id)}/illustrations/{DaraURL.percent_encode(illustration_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIllustrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_illustration(
        self,
        text_id: str,
        illustration_id: str,
    ) -> main_models.GetIllustrationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_illustration_with_options(text_id, illustration_id, headers, runtime)

    async def get_illustration_async(
        self,
        text_id: str,
        illustration_id: str,
    ) -> main_models.GetIllustrationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_illustration_with_options_async(text_id, illustration_id, headers, runtime)

    def get_illustration_task_with_options(
        self,
        text_id: str,
        illustration_task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIllustrationTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIllustrationTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/texts/{DaraURL.percent_encode(text_id)}/illustrationTasks/{DaraURL.percent_encode(illustration_task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIllustrationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_illustration_task_with_options_async(
        self,
        text_id: str,
        illustration_task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIllustrationTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIllustrationTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/texts/{DaraURL.percent_encode(text_id)}/illustrationTasks/{DaraURL.percent_encode(illustration_task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIllustrationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_illustration_task(
        self,
        text_id: str,
        illustration_task_id: str,
    ) -> main_models.GetIllustrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_illustration_task_with_options(text_id, illustration_task_id, headers, runtime)

    async def get_illustration_task_async(
        self,
        text_id: str,
        illustration_task_id: str,
    ) -> main_models.GetIllustrationTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_illustration_task_with_options_async(text_id, illustration_task_id, headers, runtime)

    def get_oss_upload_token_with_options(
        self,
        request: main_models.GetOssUploadTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOssUploadTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            query['fileType'] = request.file_type
        if not DaraCore.is_null(request.upload_type):
            query['uploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssUploadToken',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/uploadToken',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssUploadTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_upload_token_with_options_async(
        self,
        request: main_models.GetOssUploadTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOssUploadTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['fileName'] = request.file_name
        if not DaraCore.is_null(request.file_type):
            query['fileType'] = request.file_type
        if not DaraCore.is_null(request.upload_type):
            query['uploadType'] = request.upload_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssUploadToken',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/uploadToken',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssUploadTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_upload_token(
        self,
        request: main_models.GetOssUploadTokenRequest,
    ) -> main_models.GetOssUploadTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_oss_upload_token_with_options(request, headers, runtime)

    async def get_oss_upload_token_async(
        self,
        request: main_models.GetOssUploadTokenRequest,
    ) -> main_models.GetOssUploadTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_oss_upload_token_with_options_async(request, headers, runtime)

    def get_project_task_with_options(
        self,
        request: main_models.GetProjectTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/project/getProjectTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_task_with_options_async(
        self,
        request: main_models.GetProjectTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProjectTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/project/getProjectTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project_task(
        self,
        request: main_models.GetProjectTaskRequest,
    ) -> main_models.GetProjectTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_project_task_with_options(request, headers, runtime)

    async def get_project_task_async(
        self,
        request: main_models.GetProjectTaskRequest,
    ) -> main_models.GetProjectTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_project_task_with_options_async(request, headers, runtime)

    def get_text_with_options(
        self,
        text_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetText',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/texts/{DaraURL.percent_encode(text_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_text_with_options_async(
        self,
        text_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetText',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/texts/{DaraURL.percent_encode(text_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_text(
        self,
        text_id: str,
    ) -> main_models.GetTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_text_with_options(text_id, headers, runtime)

    async def get_text_async(
        self,
        text_id: str,
    ) -> main_models.GetTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_text_with_options_async(text_id, headers, runtime)

    def get_text_task_with_options(
        self,
        text_task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTextTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/textTasks/{DaraURL.percent_encode(text_task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_text_task_with_options_async(
        self,
        text_task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTextTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/textTasks/{DaraURL.percent_encode(text_task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_text_task(
        self,
        text_task_id: str,
    ) -> main_models.GetTextTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_text_task_with_options(text_task_id, headers, runtime)

    async def get_text_task_async(
        self,
        text_task_id: str,
    ) -> main_models.GetTextTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_text_task_with_options_async(text_task_id, headers, runtime)

    def get_text_template_with_options(
        self,
        request: main_models.GetTextTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTextTemplate',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/texts/commands/getTextTemplate',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_text_template_with_options_async(
        self,
        request: main_models.GetTextTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTextTemplate',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/texts/commands/getTextTemplate',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_text_template(
        self,
        request: main_models.GetTextTemplateRequest,
    ) -> main_models.GetTextTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_text_template_with_options(request, headers, runtime)

    async def get_text_template_async(
        self,
        request: main_models.GetTextTemplateRequest,
    ) -> main_models.GetTextTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_text_template_with_options_async(request, headers, runtime)

    def interact_text_with_sse(
        self,
        request: main_models.InteractTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.InteractTextResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InteractText',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/stream/interactText',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.InteractTextResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def interact_text_with_sse_async(
        self,
        request: main_models.InteractTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.InteractTextResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InteractText',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/stream/interactText',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.InteractTextResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def interact_text_with_options(
        self,
        request: main_models.InteractTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InteractTextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InteractText',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/stream/interactText',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InteractTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def interact_text_with_options_async(
        self,
        request: main_models.InteractTextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InteractTextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'InteractText',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/stream/interactText',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InteractTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def interact_text(
        self,
        request: main_models.InteractTextRequest,
    ) -> main_models.InteractTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.interact_text_with_options(request, headers, runtime)

    async def interact_text_async(
        self,
        request: main_models.InteractTextRequest,
    ) -> main_models.InteractTextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.interact_text_with_options_async(request, headers, runtime)

    def list_aicoach_script_page_with_options(
        self,
        request: main_models.ListAICoachScriptPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAICoachScriptPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAICoachScriptPage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/pageScript',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAICoachScriptPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aicoach_script_page_with_options_async(
        self,
        request: main_models.ListAICoachScriptPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAICoachScriptPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAICoachScriptPage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/pageScript',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAICoachScriptPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aicoach_script_page(
        self,
        request: main_models.ListAICoachScriptPageRequest,
    ) -> main_models.ListAICoachScriptPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_aicoach_script_page_with_options(request, headers, runtime)

    async def list_aicoach_script_page_async(
        self,
        request: main_models.ListAICoachScriptPageRequest,
    ) -> main_models.ListAICoachScriptPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_aicoach_script_page_with_options_async(request, headers, runtime)

    def list_aicoach_task_page_with_options(
        self,
        request: main_models.ListAICoachTaskPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAICoachTaskPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.student_id):
            query['studentId'] = request.student_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAICoachTaskPage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/listTaskPage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAICoachTaskPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aicoach_task_page_with_options_async(
        self,
        request: main_models.ListAICoachTaskPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAICoachTaskPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.student_id):
            query['studentId'] = request.student_id
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAICoachTaskPage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/listTaskPage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAICoachTaskPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aicoach_task_page(
        self,
        request: main_models.ListAICoachTaskPageRequest,
    ) -> main_models.ListAICoachTaskPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_aicoach_task_page_with_options(request, headers, runtime)

    async def list_aicoach_task_page_async(
        self,
        request: main_models.ListAICoachTaskPageRequest,
    ) -> main_models.ListAICoachTaskPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_aicoach_task_page_with_options_async(request, headers, runtime)

    def list_agents_with_options(
        self,
        request: main_models.ListAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_scene):
            query['agentScene'] = request.agent_scene
        if not DaraCore.is_null(request.owner):
            query['owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgents',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/agent/listAgents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_agents_with_options_async(
        self,
        request: main_models.ListAgentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAgentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_id):
            query['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_scene):
            query['agentScene'] = request.agent_scene
        if not DaraCore.is_null(request.owner):
            query['owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAgents',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/agent/listAgents',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAgentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_agents(
        self,
        request: main_models.ListAgentsRequest,
    ) -> main_models.ListAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_agents_with_options(request, headers, runtime)

    async def list_agents_async(
        self,
        request: main_models.ListAgentsRequest,
    ) -> main_models.ListAgentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_agents_with_options_async(request, headers, runtime)

    def list_anchor_with_options(
        self,
        request: main_models.ListAnchorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAnchorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.anchor_category):
            query['anchorCategory'] = request.anchor_category
        if not DaraCore.is_null(request.anchor_id):
            query['anchorId'] = request.anchor_id
        if not DaraCore.is_null(request.anchor_type):
            query['anchorType'] = request.anchor_type
        if not DaraCore.is_null(request.cover_rate):
            query['coverRate'] = request.cover_rate
        if not DaraCore.is_null(request.digital_human_type):
            query['digitalHumanType'] = request.digital_human_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.res_spec_type):
            query['resSpecType'] = request.res_spec_type
        if not DaraCore.is_null(request.use_scene):
            query['useScene'] = request.use_scene
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnchor',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/anchorOpen/listAnchor',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnchorResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_anchor_with_options_async(
        self,
        request: main_models.ListAnchorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAnchorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.anchor_category):
            query['anchorCategory'] = request.anchor_category
        if not DaraCore.is_null(request.anchor_id):
            query['anchorId'] = request.anchor_id
        if not DaraCore.is_null(request.anchor_type):
            query['anchorType'] = request.anchor_type
        if not DaraCore.is_null(request.cover_rate):
            query['coverRate'] = request.cover_rate
        if not DaraCore.is_null(request.digital_human_type):
            query['digitalHumanType'] = request.digital_human_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.res_spec_type):
            query['resSpecType'] = request.res_spec_type
        if not DaraCore.is_null(request.use_scene):
            query['useScene'] = request.use_scene
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnchor',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/anchorOpen/listAnchor',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnchorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_anchor(
        self,
        request: main_models.ListAnchorRequest,
    ) -> main_models.ListAnchorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_anchor_with_options(request, headers, runtime)

    async def list_anchor_async(
        self,
        request: main_models.ListAnchorRequest,
    ) -> main_models.ListAnchorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_anchor_with_options_async(request, headers, runtime)

    def list_avatar_project_with_options(
        self,
        tmp_req: main_models.ListAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAvatarProjectResponse:
        tmp_req.validate()
        request = main_models.ListAvatarProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.project_id_list):
            request.project_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.project_id_list, 'projectIdList', 'simple')
        query = {}
        if not DaraCore.is_null(request.project_id_list_shrink):
            query['projectIdList'] = request.project_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvatarProject',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/listAvatarProject',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_avatar_project_with_options_async(
        self,
        tmp_req: main_models.ListAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAvatarProjectResponse:
        tmp_req.validate()
        request = main_models.ListAvatarProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.project_id_list):
            request.project_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.project_id_list, 'projectIdList', 'simple')
        query = {}
        if not DaraCore.is_null(request.project_id_list_shrink):
            query['projectIdList'] = request.project_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAvatarProject',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/listAvatarProject',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAvatarProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_avatar_project(
        self,
        request: main_models.ListAvatarProjectRequest,
    ) -> main_models.ListAvatarProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_avatar_project_with_options(request, headers, runtime)

    async def list_avatar_project_async(
        self,
        request: main_models.ListAvatarProjectRequest,
    ) -> main_models.ListAvatarProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_avatar_project_with_options_async(request, headers, runtime)

    def list_knowledge_base_with_options(
        self,
        request: main_models.ListKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.knowledge_base_id):
            query['knowledgeBaseId'] = request.knowledge_base_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBase',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/knowledge-base',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_knowledge_base_with_options_async(
        self,
        request: main_models.ListKnowledgeBaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListKnowledgeBaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.knowledge_base_id):
            query['knowledgeBaseId'] = request.knowledge_base_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKnowledgeBase',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/knowledge-base',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKnowledgeBaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_knowledge_base(
        self,
        request: main_models.ListKnowledgeBaseRequest,
    ) -> main_models.ListKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_knowledge_base_with_options(request, headers, runtime)

    async def list_knowledge_base_async(
        self,
        request: main_models.ListKnowledgeBaseRequest,
    ) -> main_models.ListKnowledgeBaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_knowledge_base_with_options_async(request, headers, runtime)

    def list_text_themes_with_options(
        self,
        request: main_models.ListTextThemesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextThemesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTextThemes',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/textThemes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextThemesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_text_themes_with_options_async(
        self,
        request: main_models.ListTextThemesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextThemesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTextThemes',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/textThemes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextThemesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_text_themes(
        self,
        request: main_models.ListTextThemesRequest,
    ) -> main_models.ListTextThemesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_text_themes_with_options(request, headers, runtime)

    async def list_text_themes_async(
        self,
        request: main_models.ListTextThemesRequest,
    ) -> main_models.ListTextThemesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_text_themes_with_options_async(request, headers, runtime)

    def list_texts_with_options(
        self,
        request: main_models.ListTextsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.generation_source):
            query['generationSource'] = request.generation_source
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.publish_status):
            query['publishStatus'] = request.publish_status
        if not DaraCore.is_null(request.text_style_type):
            query['textStyleType'] = request.text_style_type
        if not DaraCore.is_null(request.text_theme):
            query['textTheme'] = request.text_theme
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTexts',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/texts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_texts_with_options_async(
        self,
        request: main_models.ListTextsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.generation_source):
            query['generationSource'] = request.generation_source
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.publish_status):
            query['publishStatus'] = request.publish_status
        if not DaraCore.is_null(request.text_style_type):
            query['textStyleType'] = request.text_style_type
        if not DaraCore.is_null(request.text_theme):
            query['textTheme'] = request.text_theme
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTexts',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/texts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_texts(
        self,
        request: main_models.ListTextsRequest,
    ) -> main_models.ListTextsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_texts_with_options(request, headers, runtime)

    async def list_texts_async(
        self,
        request: main_models.ListTextsRequest,
    ) -> main_models.ListTextsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_texts_with_options_async(request, headers, runtime)

    def list_voice_models_with_options(
        self,
        request: main_models.ListVoiceModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVoiceModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.res_spec_type):
            query['resSpecType'] = request.res_spec_type
        if not DaraCore.is_null(request.use_scene):
            query['useScene'] = request.use_scene
        if not DaraCore.is_null(request.voice_language):
            query['voiceLanguage'] = request.voice_language
        if not DaraCore.is_null(request.voice_type):
            query['voiceType'] = request.voice_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVoiceModels',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/voiceOpen/listVoiceModels',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVoiceModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_voice_models_with_options_async(
        self,
        request: main_models.ListVoiceModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListVoiceModelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.res_spec_type):
            query['resSpecType'] = request.res_spec_type
        if not DaraCore.is_null(request.use_scene):
            query['useScene'] = request.use_scene
        if not DaraCore.is_null(request.voice_language):
            query['voiceLanguage'] = request.voice_language
        if not DaraCore.is_null(request.voice_type):
            query['voiceType'] = request.voice_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListVoiceModels',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/voiceOpen/listVoiceModels',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVoiceModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_voice_models(
        self,
        request: main_models.ListVoiceModelsRequest,
    ) -> main_models.ListVoiceModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_voice_models_with_options(request, headers, runtime)

    async def list_voice_models_async(
        self,
        request: main_models.ListVoiceModelsRequest,
    ) -> main_models.ListVoiceModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_voice_models_with_options_async(request, headers, runtime)

    def offline_aicoach_script_with_options(
        self,
        request: main_models.OfflineAICoachScriptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OfflineAICoachScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.script_id):
            body['scriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineAICoachScript',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/offlineAICoachScript',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineAICoachScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_aicoach_script_with_options_async(
        self,
        request: main_models.OfflineAICoachScriptRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OfflineAICoachScriptResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.script_id):
            body['scriptId'] = request.script_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OfflineAICoachScript',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/aicoach/offlineAICoachScript',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineAICoachScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_aicoach_script(
        self,
        request: main_models.OfflineAICoachScriptRequest,
    ) -> main_models.OfflineAICoachScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.offline_aicoach_script_with_options(request, headers, runtime)

    async def offline_aicoach_script_async(
        self,
        request: main_models.OfflineAICoachScriptRequest,
    ) -> main_models.OfflineAICoachScriptResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.offline_aicoach_script_with_options_async(request, headers, runtime)

    def operate_avatar_project_with_options(
        self,
        request: main_models.OperateAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OperateAvatarProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.operate_type):
            body['operateType'] = request.operate_type
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.res_channel_number):
            body['resChannelNumber'] = request.res_channel_number
        if not DaraCore.is_null(request.res_type):
            body['resType'] = request.res_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateAvatarProject',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/operateProjectAvatar',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_avatar_project_with_options_async(
        self,
        request: main_models.OperateAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OperateAvatarProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.operate_type):
            body['operateType'] = request.operate_type
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.res_channel_number):
            body['resChannelNumber'] = request.res_channel_number
        if not DaraCore.is_null(request.res_type):
            body['resType'] = request.res_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OperateAvatarProject',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/operateProjectAvatar',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateAvatarProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_avatar_project(
        self,
        request: main_models.OperateAvatarProjectRequest,
    ) -> main_models.OperateAvatarProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.operate_avatar_project_with_options(request, headers, runtime)

    async def operate_avatar_project_async(
        self,
        request: main_models.OperateAvatarProjectRequest,
    ) -> main_models.OperateAvatarProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.operate_avatar_project_with_options_async(request, headers, runtime)

    def query_avatar_project_with_options(
        self,
        request: main_models.QueryAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvatarProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['projectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAvatarProject',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/queryAvatarProject',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_avatar_project_with_options_async(
        self,
        request: main_models.QueryAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvatarProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['projectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAvatarProject',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/queryAvatarProject',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvatarProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_avatar_project(
        self,
        request: main_models.QueryAvatarProjectRequest,
    ) -> main_models.QueryAvatarProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_avatar_project_with_options(request, headers, runtime)

    async def query_avatar_project_async(
        self,
        request: main_models.QueryAvatarProjectRequest,
    ) -> main_models.QueryAvatarProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_avatar_project_with_options_async(request, headers, runtime)

    def query_avatar_resource_with_options(
        self,
        request: main_models.QueryAvatarResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvatarResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.idempotent_id):
            query['idempotentId'] = request.idempotent_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAvatarResource',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/queryResource',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvatarResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_avatar_resource_with_options_async(
        self,
        request: main_models.QueryAvatarResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvatarResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.idempotent_id):
            query['idempotentId'] = request.idempotent_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAvatarResource',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/queryResource',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvatarResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_avatar_resource(
        self,
        request: main_models.QueryAvatarResourceRequest,
    ) -> main_models.QueryAvatarResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_avatar_resource_with_options(request, headers, runtime)

    async def query_avatar_resource_async(
        self,
        request: main_models.QueryAvatarResourceRequest,
    ) -> main_models.QueryAvatarResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_avatar_resource_with_options_async(request, headers, runtime)

    def query_image_to_video_task_with_options(
        self,
        request: main_models.QueryImageToVideoTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryImageToVideoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryImageToVideoTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/video/imageToVideo/task',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryImageToVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_image_to_video_task_with_options_async(
        self,
        request: main_models.QueryImageToVideoTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryImageToVideoTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryImageToVideoTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/video/imageToVideo/task',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryImageToVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_image_to_video_task(
        self,
        request: main_models.QueryImageToVideoTaskRequest,
    ) -> main_models.QueryImageToVideoTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_image_to_video_task_with_options(request, headers, runtime)

    async def query_image_to_video_task_async(
        self,
        request: main_models.QueryImageToVideoTaskRequest,
    ) -> main_models.QueryImageToVideoTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_image_to_video_task_with_options_async(request, headers, runtime)

    def query_individuation_text_task_with_options(
        self,
        request: main_models.QueryIndividuationTextTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryIndividuationTextTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryIndividuationTextTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/individuationText/queryTextTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryIndividuationTextTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_individuation_text_task_with_options_async(
        self,
        request: main_models.QueryIndividuationTextTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryIndividuationTextTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryIndividuationTextTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/individuationText/queryTextTask',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryIndividuationTextTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_individuation_text_task(
        self,
        request: main_models.QueryIndividuationTextTaskRequest,
    ) -> main_models.QueryIndividuationTextTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_individuation_text_task_with_options(request, headers, runtime)

    async def query_individuation_text_task_async(
        self,
        request: main_models.QueryIndividuationTextTaskRequest,
    ) -> main_models.QueryIndividuationTextTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_individuation_text_task_with_options_async(request, headers, runtime)

    def query_session_info_with_options(
        self,
        tmp_req: main_models.QuerySessionInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QuerySessionInfoResponse:
        tmp_req.validate()
        request = main_models.QuerySessionInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'statusList', 'simple')
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['pageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['projectId'] = request.project_id
        if not DaraCore.is_null(request.status_list_shrink):
            query['statusList'] = request.status_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySessionInfo',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/querySessionInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySessionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_session_info_with_options_async(
        self,
        tmp_req: main_models.QuerySessionInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QuerySessionInfoResponse:
        tmp_req.validate()
        request = main_models.QuerySessionInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.status_list):
            request.status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.status_list, 'statusList', 'simple')
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['pageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['projectId'] = request.project_id
        if not DaraCore.is_null(request.status_list_shrink):
            query['statusList'] = request.status_list_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySessionInfo',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/querySessionInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySessionInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_session_info(
        self,
        request: main_models.QuerySessionInfoRequest,
    ) -> main_models.QuerySessionInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_session_info_with_options(request, headers, runtime)

    async def query_session_info_async(
        self,
        request: main_models.QuerySessionInfoRequest,
    ) -> main_models.QuerySessionInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_session_info_with_options_async(request, headers, runtime)

    def query_text_stream_with_sse(
        self,
        text_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.QueryTextStreamResponse, None, None]:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'QueryTextStream',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/stream/queryTextStream/{DaraURL.percent_encode(text_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.QueryTextStreamResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def query_text_stream_with_sse_async(
        self,
        text_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.QueryTextStreamResponse, None, None]:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'QueryTextStream',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/stream/queryTextStream/{DaraURL.percent_encode(text_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.QueryTextStreamResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def query_text_stream_with_options(
        self,
        text_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryTextStreamResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'QueryTextStream',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/stream/queryTextStream/{DaraURL.percent_encode(text_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTextStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_text_stream_with_options_async(
        self,
        text_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryTextStreamResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'QueryTextStream',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/stream/queryTextStream/{DaraURL.percent_encode(text_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTextStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_text_stream(
        self,
        text_id: str,
    ) -> main_models.QueryTextStreamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_text_stream_with_options(text_id, headers, runtime)

    async def query_text_stream_async(
        self,
        text_id: str,
    ) -> main_models.QueryTextStreamResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_text_stream_with_options_async(text_id, headers, runtime)

    def release_agent_with_options(
        self,
        request: main_models.ReleaseAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseAgent',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/agent/releaseAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_agent_with_options_async(
        self,
        request: main_models.ReleaseAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseAgent',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/agent/releaseAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_agent(
        self,
        request: main_models.ReleaseAgentRequest,
    ) -> main_models.ReleaseAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.release_agent_with_options(request, headers, runtime)

    async def release_agent_async(
        self,
        request: main_models.ReleaseAgentRequest,
    ) -> main_models.ReleaseAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.release_agent_with_options_async(request, headers, runtime)

    def save_avatar_project_with_options(
        self,
        request: main_models.SaveAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SaveAvatarProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.bit_rate):
            body['bitRate'] = request.bit_rate
        if not DaraCore.is_null(request.frame_rate):
            body['frameRate'] = request.frame_rate
        if not DaraCore.is_null(request.frames):
            body['frames'] = request.frames
        if not DaraCore.is_null(request.operate_type):
            body['operateType'] = request.operate_type
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.project_name):
            body['projectName'] = request.project_name
        if not DaraCore.is_null(request.res_spec_type):
            body['resSpecType'] = request.res_spec_type
        if not DaraCore.is_null(request.resolution):
            body['resolution'] = request.resolution
        if not DaraCore.is_null(request.scale_type):
            body['scaleType'] = request.scale_type
        if not DaraCore.is_null(request.script_model_tag):
            body['scriptModelTag'] = request.script_model_tag
        if not DaraCore.is_null(request.synchronized_display):
            body['synchronizedDisplay'] = request.synchronized_display
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveAvatarProject',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/saveAvatarProject',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAvatarProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_avatar_project_with_options_async(
        self,
        request: main_models.SaveAvatarProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SaveAvatarProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.bit_rate):
            body['bitRate'] = request.bit_rate
        if not DaraCore.is_null(request.frame_rate):
            body['frameRate'] = request.frame_rate
        if not DaraCore.is_null(request.frames):
            body['frames'] = request.frames
        if not DaraCore.is_null(request.operate_type):
            body['operateType'] = request.operate_type
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.project_name):
            body['projectName'] = request.project_name
        if not DaraCore.is_null(request.res_spec_type):
            body['resSpecType'] = request.res_spec_type
        if not DaraCore.is_null(request.resolution):
            body['resolution'] = request.resolution
        if not DaraCore.is_null(request.scale_type):
            body['scaleType'] = request.scale_type
        if not DaraCore.is_null(request.script_model_tag):
            body['scriptModelTag'] = request.script_model_tag
        if not DaraCore.is_null(request.synchronized_display):
            body['synchronizedDisplay'] = request.synchronized_display
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SaveAvatarProject',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/saveAvatarProject',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveAvatarProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_avatar_project(
        self,
        request: main_models.SaveAvatarProjectRequest,
    ) -> main_models.SaveAvatarProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.save_avatar_project_with_options(request, headers, runtime)

    async def save_avatar_project_async(
        self,
        request: main_models.SaveAvatarProjectRequest,
    ) -> main_models.SaveAvatarProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.save_avatar_project_with_options_async(request, headers, runtime)

    def select_image_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectImageTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'SelectImageTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/images/portrait/select/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectImageTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def select_image_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectImageTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'SelectImageTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/images/portrait/select/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectImageTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def select_image_task(
        self,
        task_id: str,
    ) -> main_models.SelectImageTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.select_image_task_with_options(task_id, headers, runtime)

    async def select_image_task_async(
        self,
        task_id: str,
    ) -> main_models.SelectImageTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.select_image_task_with_options_async(task_id, headers, runtime)

    def select_resource_with_options(
        self,
        request: main_models.SelectResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.idempotent_id):
            query['idempotentId'] = request.idempotent_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SelectResource',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/project/commands/overview',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def select_resource_with_options_async(
        self,
        request: main_models.SelectResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.idempotent_id):
            query['idempotentId'] = request.idempotent_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SelectResource',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/project/commands/overview',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def select_resource(
        self,
        request: main_models.SelectResourceRequest,
    ) -> main_models.SelectResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.select_resource_with_options(request, headers, runtime)

    async def select_resource_async(
        self,
        request: main_models.SelectResourceRequest,
    ) -> main_models.SelectResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.select_resource_with_options_async(request, headers, runtime)

    def send_sdk_message_with_options(
        self,
        request: main_models.SendSdkMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendSdkMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.header):
            body['header'] = request.header
        if not DaraCore.is_null(request.module_name):
            body['moduleName'] = request.module_name
        if not DaraCore.is_null(request.operation_name):
            body['operationName'] = request.operation_name
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendSdkMessage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/sdk/sendMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendSdkMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_sdk_message_with_options_async(
        self,
        request: main_models.SendSdkMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendSdkMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.header):
            body['header'] = request.header
        if not DaraCore.is_null(request.module_name):
            body['moduleName'] = request.module_name
        if not DaraCore.is_null(request.operation_name):
            body['operationName'] = request.operation_name
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendSdkMessage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/sdk/sendMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendSdkMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_sdk_message(
        self,
        request: main_models.SendSdkMessageRequest,
    ) -> main_models.SendSdkMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_sdk_message_with_options(request, headers, runtime)

    async def send_sdk_message_async(
        self,
        request: main_models.SendSdkMessageRequest,
    ) -> main_models.SendSdkMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_sdk_message_with_options_async(request, headers, runtime)

    def send_sdk_stream_message_with_sse(
        self,
        request: main_models.SendSdkStreamMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.SendSdkStreamMessageResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.header):
            body['header'] = request.header
        if not DaraCore.is_null(request.module_name):
            body['moduleName'] = request.module_name
        if not DaraCore.is_null(request.operation_name):
            body['operationName'] = request.operation_name
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendSdkStreamMessage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/sdk/stream/sendMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.SendSdkStreamMessageResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def send_sdk_stream_message_with_sse_async(
        self,
        request: main_models.SendSdkStreamMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.SendSdkStreamMessageResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.header):
            body['header'] = request.header
        if not DaraCore.is_null(request.module_name):
            body['moduleName'] = request.module_name
        if not DaraCore.is_null(request.operation_name):
            body['operationName'] = request.operation_name
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendSdkStreamMessage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/sdk/stream/sendMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.SendSdkStreamMessageResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def send_sdk_stream_message_with_options(
        self,
        request: main_models.SendSdkStreamMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendSdkStreamMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.header):
            body['header'] = request.header
        if not DaraCore.is_null(request.module_name):
            body['moduleName'] = request.module_name
        if not DaraCore.is_null(request.operation_name):
            body['operationName'] = request.operation_name
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendSdkStreamMessage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/sdk/stream/sendMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendSdkStreamMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_sdk_stream_message_with_options_async(
        self,
        request: main_models.SendSdkStreamMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendSdkStreamMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.data):
            body['data'] = request.data
        if not DaraCore.is_null(request.header):
            body['header'] = request.header
        if not DaraCore.is_null(request.module_name):
            body['moduleName'] = request.module_name
        if not DaraCore.is_null(request.operation_name):
            body['operationName'] = request.operation_name
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendSdkStreamMessage',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/sdk/stream/sendMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendSdkStreamMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_sdk_stream_message(
        self,
        request: main_models.SendSdkStreamMessageRequest,
    ) -> main_models.SendSdkStreamMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_sdk_stream_message_with_options(request, headers, runtime)

    async def send_sdk_stream_message_async(
        self,
        request: main_models.SendSdkStreamMessageRequest,
    ) -> main_models.SendSdkStreamMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_sdk_stream_message_with_options_async(request, headers, runtime)

    def send_text_msg_with_options(
        self,
        request: main_models.SendTextMsgRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendTextMsgResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendTextMsg',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/sendTextMsg',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendTextMsgResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_text_msg_with_options_async(
        self,
        request: main_models.SendTextMsgRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendTextMsgResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.text):
            body['text'] = request.text
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendTextMsg',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/sendTextMsg',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendTextMsgResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_text_msg(
        self,
        request: main_models.SendTextMsgRequest,
    ) -> main_models.SendTextMsgResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_text_msg_with_options(request, headers, runtime)

    async def send_text_msg_async(
        self,
        request: main_models.SendTextMsgRequest,
    ) -> main_models.SendTextMsgResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_text_msg_with_options_async(request, headers, runtime)

    def start_avatar_session_with_options(
        self,
        request: main_models.StartAvatarSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartAvatarSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel_token):
            body['channelToken'] = request.channel_token
        if not DaraCore.is_null(request.custom_push_url):
            body['customPushUrl'] = request.custom_push_url
        if not DaraCore.is_null(request.custom_user_id):
            body['customUserId'] = request.custom_user_id
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartAvatarSession',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/startAvatarSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAvatarSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_avatar_session_with_options_async(
        self,
        request: main_models.StartAvatarSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StartAvatarSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel_token):
            body['channelToken'] = request.channel_token
        if not DaraCore.is_null(request.custom_push_url):
            body['customPushUrl'] = request.custom_push_url
        if not DaraCore.is_null(request.custom_user_id):
            body['customUserId'] = request.custom_user_id
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.request_id):
            body['requestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StartAvatarSession',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/startAvatarSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAvatarSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_avatar_session(
        self,
        request: main_models.StartAvatarSessionRequest,
    ) -> main_models.StartAvatarSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.start_avatar_session_with_options(request, headers, runtime)

    async def start_avatar_session_async(
        self,
        request: main_models.StartAvatarSessionRequest,
    ) -> main_models.StartAvatarSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.start_avatar_session_with_options_async(request, headers, runtime)

    def stop_avatar_session_with_options(
        self,
        request: main_models.StopAvatarSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopAvatarSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopAvatarSession',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/stopAvatarSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAvatarSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_avatar_session_with_options_async(
        self,
        request: main_models.StopAvatarSessionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopAvatarSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopAvatarSession',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/avatar/project/stopAvatarSession',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAvatarSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_avatar_session(
        self,
        request: main_models.StopAvatarSessionRequest,
    ) -> main_models.StopAvatarSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_avatar_session_with_options(request, headers, runtime)

    async def stop_avatar_session_async(
        self,
        request: main_models.StopAvatarSessionRequest,
    ) -> main_models.StopAvatarSessionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_avatar_session_with_options_async(request, headers, runtime)

    def stop_project_task_with_options(
        self,
        request: main_models.StopProjectTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopProjectTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopProjectTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/project/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopProjectTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_project_task_with_options_async(
        self,
        request: main_models.StopProjectTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopProjectTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopProjectTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/project/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopProjectTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_project_task(
        self,
        request: main_models.StopProjectTaskRequest,
    ) -> main_models.StopProjectTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_project_task_with_options(request, headers, runtime)

    async def stop_project_task_async(
        self,
        request: main_models.StopProjectTaskRequest,
    ) -> main_models.StopProjectTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_project_task_with_options_async(request, headers, runtime)

    def submit_image_to_video_task_with_options(
        self,
        request: main_models.SubmitImageToVideoTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImageToVideoTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.pos_prompt):
            body['posPrompt'] = request.pos_prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImageToVideoTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/video/imageToVideo/task',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitImageToVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_image_to_video_task_with_options_async(
        self,
        request: main_models.SubmitImageToVideoTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitImageToVideoTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.pos_prompt):
            body['posPrompt'] = request.pos_prompt
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitImageToVideoTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/video/imageToVideo/task',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitImageToVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_image_to_video_task(
        self,
        request: main_models.SubmitImageToVideoTaskRequest,
    ) -> main_models.SubmitImageToVideoTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_image_to_video_task_with_options(request, headers, runtime)

    async def submit_image_to_video_task_async(
        self,
        request: main_models.SubmitImageToVideoTaskRequest,
    ) -> main_models.SubmitImageToVideoTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_image_to_video_task_with_options_async(request, headers, runtime)

    def submit_project_task_with_options(
        self,
        request: main_models.SubmitProjectTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitProjectTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.frames):
            body['frames'] = request.frames
        if not DaraCore.is_null(request.scale_type):
            body['scaleType'] = request.scale_type
        if not DaraCore.is_null(request.subtitle_tag):
            body['subtitleTag'] = request.subtitle_tag
        if not DaraCore.is_null(request.transparent_background):
            body['transparentBackground'] = request.transparent_background
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitProjectTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/project/submitProjectTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitProjectTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_project_task_with_options_async(
        self,
        request: main_models.SubmitProjectTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubmitProjectTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.frames):
            body['frames'] = request.frames
        if not DaraCore.is_null(request.scale_type):
            body['scaleType'] = request.scale_type
        if not DaraCore.is_null(request.subtitle_tag):
            body['subtitleTag'] = request.subtitle_tag
        if not DaraCore.is_null(request.transparent_background):
            body['transparentBackground'] = request.transparent_background
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitProjectTask',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/digitalHuman/project/submitProjectTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitProjectTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_project_task(
        self,
        request: main_models.SubmitProjectTaskRequest,
    ) -> main_models.SubmitProjectTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.submit_project_task_with_options(request, headers, runtime)

    async def submit_project_task_async(
        self,
        request: main_models.SubmitProjectTaskRequest,
    ) -> main_models.SubmitProjectTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.submit_project_task_with_options_async(request, headers, runtime)

    def transfer_portrait_style_with_options(
        self,
        request: main_models.TransferPortraitStyleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TransferPortraitStyleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.height):
            body['height'] = request.height
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.numbers):
            body['numbers'] = request.numbers
        if not DaraCore.is_null(request.redraw_amplitude):
            body['redrawAmplitude'] = request.redraw_amplitude
        if not DaraCore.is_null(request.style):
            body['style'] = request.style
        if not DaraCore.is_null(request.width):
            body['width'] = request.width
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TransferPortraitStyle',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/images/portrait/transferPortraitStyle',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferPortraitStyleResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_portrait_style_with_options_async(
        self,
        request: main_models.TransferPortraitStyleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TransferPortraitStyleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.height):
            body['height'] = request.height
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.numbers):
            body['numbers'] = request.numbers
        if not DaraCore.is_null(request.redraw_amplitude):
            body['redrawAmplitude'] = request.redraw_amplitude
        if not DaraCore.is_null(request.style):
            body['style'] = request.style
        if not DaraCore.is_null(request.width):
            body['width'] = request.width
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TransferPortraitStyle',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/images/portrait/transferPortraitStyle',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferPortraitStyleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_portrait_style(
        self,
        request: main_models.TransferPortraitStyleRequest,
    ) -> main_models.TransferPortraitStyleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.transfer_portrait_style_with_options(request, headers, runtime)

    async def transfer_portrait_style_async(
        self,
        request: main_models.TransferPortraitStyleRequest,
    ) -> main_models.TransferPortraitStyleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.transfer_portrait_style_with_options_async(request, headers, runtime)

    def update_agent_with_options(
        self,
        request: main_models.UpdateAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_icon_url):
            body['agentIconUrl'] = request.agent_icon_url
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.character_age_stage):
            body['characterAgeStage'] = request.character_age_stage
        if not DaraCore.is_null(request.character_gender):
            body['characterGender'] = request.character_gender
        if not DaraCore.is_null(request.character_name):
            body['characterName'] = request.character_name
        if not DaraCore.is_null(request.extra_description):
            body['extraDescription'] = request.extra_description
        if not DaraCore.is_null(request.industry):
            body['industry'] = request.industry
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgent',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/agent/updateAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_agent_with_options_async(
        self,
        request: main_models.UpdateAgentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAgentResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.agent_icon_url):
            body['agentIconUrl'] = request.agent_icon_url
        if not DaraCore.is_null(request.agent_id):
            body['agentId'] = request.agent_id
        if not DaraCore.is_null(request.agent_name):
            body['agentName'] = request.agent_name
        if not DaraCore.is_null(request.character_age_stage):
            body['characterAgeStage'] = request.character_age_stage
        if not DaraCore.is_null(request.character_gender):
            body['characterGender'] = request.character_gender
        if not DaraCore.is_null(request.character_name):
            body['characterName'] = request.character_name
        if not DaraCore.is_null(request.extra_description):
            body['extraDescription'] = request.extra_description
        if not DaraCore.is_null(request.industry):
            body['industry'] = request.industry
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAgent',
            version = '2024-03-13',
            protocol = 'HTTPS',
            pathname = f'/yic/yic-console/openService/v1/agent/updateAgent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_agent(
        self,
        request: main_models.UpdateAgentRequest,
    ) -> main_models.UpdateAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_agent_with_options(request, headers, runtime)

    async def update_agent_async(
        self,
        request: main_models.UpdateAgentRequest,
    ) -> main_models.UpdateAgentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_agent_with_options_async(request, headers, runtime)
