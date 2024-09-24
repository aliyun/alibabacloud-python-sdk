# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_contactcenterai20240603 import models as contact_center_ai20240603_models
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
        self._endpoint = self.get_endpoint('contactcenterai', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def analyze_conversation_with_options(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.AnalyzeConversationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.AnalyzeConversationResponse:
        """
        @summary 根据类型调用大模型
        
        @param request: AnalyzeConversationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnalyzeConversationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_tags):
            body['categoryTags'] = request.category_tags
        if not UtilClient.is_unset(request.dialogue):
            body['dialogue'] = request.dialogue
        if not UtilClient.is_unset(request.examples):
            body['examples'] = request.examples
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.model_code):
            body['modelCode'] = request.model_code
        if not UtilClient.is_unset(request.result_types):
            body['resultTypes'] = request.result_types
        if not UtilClient.is_unset(request.scene_name):
            body['sceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.user_profiles):
            body['userProfiles'] = request.user_profiles
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AnalyzeConversation',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/ccai/app/{OpenApiUtilClient.get_encode_param(app_id)}/analyze_conversation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.AnalyzeConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def analyze_conversation_with_options_async(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.AnalyzeConversationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.AnalyzeConversationResponse:
        """
        @summary 根据类型调用大模型
        
        @param request: AnalyzeConversationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AnalyzeConversationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category_tags):
            body['categoryTags'] = request.category_tags
        if not UtilClient.is_unset(request.dialogue):
            body['dialogue'] = request.dialogue
        if not UtilClient.is_unset(request.examples):
            body['examples'] = request.examples
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.model_code):
            body['modelCode'] = request.model_code
        if not UtilClient.is_unset(request.result_types):
            body['resultTypes'] = request.result_types
        if not UtilClient.is_unset(request.scene_name):
            body['sceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not UtilClient.is_unset(request.stream):
            body['stream'] = request.stream
        if not UtilClient.is_unset(request.user_profiles):
            body['userProfiles'] = request.user_profiles
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AnalyzeConversation',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/ccai/app/{OpenApiUtilClient.get_encode_param(app_id)}/analyze_conversation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.AnalyzeConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def analyze_conversation(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.AnalyzeConversationRequest,
    ) -> contact_center_ai20240603_models.AnalyzeConversationResponse:
        """
        @summary 根据类型调用大模型
        
        @param request: AnalyzeConversationRequest
        @return: AnalyzeConversationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.analyze_conversation_with_options(workspace_id, app_id, request, headers, runtime)

    async def analyze_conversation_async(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.AnalyzeConversationRequest,
    ) -> contact_center_ai20240603_models.AnalyzeConversationResponse:
        """
        @summary 根据类型调用大模型
        
        @param request: AnalyzeConversationRequest
        @return: AnalyzeConversationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.analyze_conversation_with_options_async(workspace_id, app_id, request, headers, runtime)

    def create_conversation_analysis_task_with_options(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.CreateConversationAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.CreateConversationAnalysisTaskResponse:
        """
        @summary 创建语音文件调用llm任务
        
        @param request: CreateConversationAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConversationAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.client_channel):
            body['clientChannel'] = request.client_channel
        if not UtilClient.is_unset(request.examples):
            body['examples'] = request.examples
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.model_code):
            body['modelCode'] = request.model_code
        if not UtilClient.is_unset(request.result_types):
            body['resultTypes'] = request.result_types
        if not UtilClient.is_unset(request.scene_name):
            body['sceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_channel):
            body['serviceChannel'] = request.service_channel
        if not UtilClient.is_unset(request.service_channel_keywords):
            body['serviceChannelKeywords'] = request.service_channel_keywords
        if not UtilClient.is_unset(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not UtilClient.is_unset(request.template_ids):
            body['templateIds'] = request.template_ids
        if not UtilClient.is_unset(request.voice_file_url):
            body['voiceFileUrl'] = request.voice_file_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConversationAnalysisTask',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/ccai/app/{OpenApiUtilClient.get_encode_param(app_id)}/createConversationAnalysisTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.CreateConversationAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_conversation_analysis_task_with_options_async(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.CreateConversationAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.CreateConversationAnalysisTaskResponse:
        """
        @summary 创建语音文件调用llm任务
        
        @param request: CreateConversationAnalysisTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateConversationAnalysisTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_split):
            body['autoSplit'] = request.auto_split
        if not UtilClient.is_unset(request.client_channel):
            body['clientChannel'] = request.client_channel
        if not UtilClient.is_unset(request.examples):
            body['examples'] = request.examples
        if not UtilClient.is_unset(request.fields):
            body['fields'] = request.fields
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.model_code):
            body['modelCode'] = request.model_code
        if not UtilClient.is_unset(request.result_types):
            body['resultTypes'] = request.result_types
        if not UtilClient.is_unset(request.scene_name):
            body['sceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_channel):
            body['serviceChannel'] = request.service_channel
        if not UtilClient.is_unset(request.service_channel_keywords):
            body['serviceChannelKeywords'] = request.service_channel_keywords
        if not UtilClient.is_unset(request.service_inspection):
            body['serviceInspection'] = request.service_inspection
        if not UtilClient.is_unset(request.template_ids):
            body['templateIds'] = request.template_ids
        if not UtilClient.is_unset(request.voice_file_url):
            body['voiceFileUrl'] = request.voice_file_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateConversationAnalysisTask',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/ccai/app/{OpenApiUtilClient.get_encode_param(app_id)}/createConversationAnalysisTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.CreateConversationAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_conversation_analysis_task(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.CreateConversationAnalysisTaskRequest,
    ) -> contact_center_ai20240603_models.CreateConversationAnalysisTaskResponse:
        """
        @summary 创建语音文件调用llm任务
        
        @param request: CreateConversationAnalysisTaskRequest
        @return: CreateConversationAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_conversation_analysis_task_with_options(workspace_id, app_id, request, headers, runtime)

    async def create_conversation_analysis_task_async(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.CreateConversationAnalysisTaskRequest,
    ) -> contact_center_ai20240603_models.CreateConversationAnalysisTaskResponse:
        """
        @summary 创建语音文件调用llm任务
        
        @param request: CreateConversationAnalysisTaskRequest
        @return: CreateConversationAnalysisTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_conversation_analysis_task_with_options_async(workspace_id, app_id, request, headers, runtime)

    def get_task_result_with_options(
        self,
        request: contact_center_ai20240603_models.GetTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.GetTaskResultResponse:
        """
        @summary 语音文件调用大模型获取结果
        
        @param request: GetTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResultResponse
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
            action='GetTaskResult',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/ccai/app/getTaskResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.GetTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_result_with_options_async(
        self,
        request: contact_center_ai20240603_models.GetTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.GetTaskResultResponse:
        """
        @summary 语音文件调用大模型获取结果
        
        @param request: GetTaskResultRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResultResponse
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
            action='GetTaskResult',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/ccai/app/getTaskResult',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.GetTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task_result(
        self,
        request: contact_center_ai20240603_models.GetTaskResultRequest,
    ) -> contact_center_ai20240603_models.GetTaskResultResponse:
        """
        @summary 语音文件调用大模型获取结果
        
        @param request: GetTaskResultRequest
        @return: GetTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_result_with_options(request, headers, runtime)

    async def get_task_result_async(
        self,
        request: contact_center_ai20240603_models.GetTaskResultRequest,
    ) -> contact_center_ai20240603_models.GetTaskResultResponse:
        """
        @summary 语音文件调用大模型获取结果
        
        @param request: GetTaskResultRequest
        @return: GetTaskResultResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_result_with_options_async(request, headers, runtime)

    def run_completion_with_options(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.RunCompletionResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCompletionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dialogue):
            body['Dialogue'] = request.dialogue
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.model_code):
            body['ModelCode'] = request.model_code
        if not UtilClient.is_unset(request.service_inspection):
            body['ServiceInspection'] = request.service_inspection
        if not UtilClient.is_unset(request.stream):
            body['Stream'] = request.stream
        if not UtilClient.is_unset(request.template_ids):
            body['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCompletion',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/ccai/app/{OpenApiUtilClient.get_encode_param(app_id)}/completion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.RunCompletionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_completion_with_options_async(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.RunCompletionResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCompletionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dialogue):
            body['Dialogue'] = request.dialogue
        if not UtilClient.is_unset(request.fields):
            body['Fields'] = request.fields
        if not UtilClient.is_unset(request.model_code):
            body['ModelCode'] = request.model_code
        if not UtilClient.is_unset(request.service_inspection):
            body['ServiceInspection'] = request.service_inspection
        if not UtilClient.is_unset(request.stream):
            body['Stream'] = request.stream
        if not UtilClient.is_unset(request.template_ids):
            body['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCompletion',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/ccai/app/{OpenApiUtilClient.get_encode_param(app_id)}/completion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.RunCompletionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_completion(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionRequest,
    ) -> contact_center_ai20240603_models.RunCompletionResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionRequest
        @return: RunCompletionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_completion_with_options(workspace_id, app_id, request, headers, runtime)

    async def run_completion_async(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionRequest,
    ) -> contact_center_ai20240603_models.RunCompletionResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionRequest
        @return: RunCompletionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_completion_with_options_async(workspace_id, app_id, request, headers, runtime)

    def run_completion_message_with_options(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.RunCompletionMessageResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCompletionMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.messages):
            body['Messages'] = request.messages
        if not UtilClient.is_unset(request.model_code):
            body['ModelCode'] = request.model_code
        if not UtilClient.is_unset(request.stream):
            body['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCompletionMessage',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/ccai/app/{OpenApiUtilClient.get_encode_param(app_id)}/completion_message',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.RunCompletionMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_completion_message_with_options_async(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> contact_center_ai20240603_models.RunCompletionMessageResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCompletionMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.messages):
            body['Messages'] = request.messages
        if not UtilClient.is_unset(request.model_code):
            body['ModelCode'] = request.model_code
        if not UtilClient.is_unset(request.stream):
            body['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCompletionMessage',
            version='2024-06-03',
            protocol='HTTPS',
            pathname=f'/{OpenApiUtilClient.get_encode_param(workspace_id)}/ccai/app/{OpenApiUtilClient.get_encode_param(app_id)}/completion_message',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            contact_center_ai20240603_models.RunCompletionMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_completion_message(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionMessageRequest,
    ) -> contact_center_ai20240603_models.RunCompletionMessageResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionMessageRequest
        @return: RunCompletionMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_completion_message_with_options(workspace_id, app_id, request, headers, runtime)

    async def run_completion_message_async(
        self,
        workspace_id: str,
        app_id: str,
        request: contact_center_ai20240603_models.RunCompletionMessageRequest,
    ) -> contact_center_ai20240603_models.RunCompletionMessageResponse:
        """
        @summary CCAI服务面API
        
        @param request: RunCompletionMessageRequest
        @return: RunCompletionMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_completion_message_with_options_async(workspace_id, app_id, request, headers, runtime)
