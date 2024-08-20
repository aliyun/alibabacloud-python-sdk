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
        if not UtilClient.is_unset(request.use_scene):
            query['useScene'] = request.use_scene
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
        if not UtilClient.is_unset(request.use_scene):
            query['useScene'] = request.use_scene
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
