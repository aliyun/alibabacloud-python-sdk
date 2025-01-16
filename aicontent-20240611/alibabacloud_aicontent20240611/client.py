# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aicontent20240611 import models as ai_content_20240611_models
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
        self._endpoint = self.get_endpoint('aicontent', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def a_iteacher_expansion_practice_task_generate_with_options(
        self,
        request: ai_content_20240611_models.AITeacherExpansionPracticeTaskGenerateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.AITeacherExpansionPracticeTaskGenerateResponse:
        """
        @summary 拓展练问答对生成
        
        @param request: AITeacherExpansionPracticeTaskGenerateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AITeacherExpansionPracticeTaskGenerateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.key_sentences):
            body['keySentences'] = request.key_sentences
        if not UtilClient.is_unset(request.key_words):
            body['keyWords'] = request.key_words
        if not UtilClient.is_unset(request.learning_object):
            body['learningObject'] = request.learning_object
        if not UtilClient.is_unset(request.text_content):
            body['textContent'] = request.text_content
        if not UtilClient.is_unset(request.textbook):
            body['textbook'] = request.textbook
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AITeacherExpansionPracticeTaskGenerate',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/expansionPractice/generateTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.AITeacherExpansionPracticeTaskGenerateResponse(),
            self.call_api(params, req, runtime)
        )

    async def a_iteacher_expansion_practice_task_generate_with_options_async(
        self,
        request: ai_content_20240611_models.AITeacherExpansionPracticeTaskGenerateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.AITeacherExpansionPracticeTaskGenerateResponse:
        """
        @summary 拓展练问答对生成
        
        @param request: AITeacherExpansionPracticeTaskGenerateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AITeacherExpansionPracticeTaskGenerateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.key_sentences):
            body['keySentences'] = request.key_sentences
        if not UtilClient.is_unset(request.key_words):
            body['keyWords'] = request.key_words
        if not UtilClient.is_unset(request.learning_object):
            body['learningObject'] = request.learning_object
        if not UtilClient.is_unset(request.text_content):
            body['textContent'] = request.text_content
        if not UtilClient.is_unset(request.textbook):
            body['textbook'] = request.textbook
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AITeacherExpansionPracticeTaskGenerate',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/expansionPractice/generateTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.AITeacherExpansionPracticeTaskGenerateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def a_iteacher_expansion_practice_task_generate(
        self,
        request: ai_content_20240611_models.AITeacherExpansionPracticeTaskGenerateRequest,
    ) -> ai_content_20240611_models.AITeacherExpansionPracticeTaskGenerateResponse:
        """
        @summary 拓展练问答对生成
        
        @param request: AITeacherExpansionPracticeTaskGenerateRequest
        @return: AITeacherExpansionPracticeTaskGenerateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.a_iteacher_expansion_practice_task_generate_with_options(request, headers, runtime)

    async def a_iteacher_expansion_practice_task_generate_async(
        self,
        request: ai_content_20240611_models.AITeacherExpansionPracticeTaskGenerateRequest,
    ) -> ai_content_20240611_models.AITeacherExpansionPracticeTaskGenerateResponse:
        """
        @summary 拓展练问答对生成
        
        @param request: AITeacherExpansionPracticeTaskGenerateRequest
        @return: AITeacherExpansionPracticeTaskGenerateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.a_iteacher_expansion_practice_task_generate_with_options_async(request, headers, runtime)

    def a_iteacher_sync_practice_task_generate_with_options(
        self,
        request: ai_content_20240611_models.AITeacherSyncPracticeTaskGenerateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.AITeacherSyncPracticeTaskGenerateResponse:
        """
        @summary 同步基础练问答对生成
        
        @param request: AITeacherSyncPracticeTaskGenerateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AITeacherSyncPracticeTaskGenerateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.key_sentences):
            body['keySentences'] = request.key_sentences
        if not UtilClient.is_unset(request.key_words):
            body['keyWords'] = request.key_words
        if not UtilClient.is_unset(request.learning_object):
            body['learningObject'] = request.learning_object
        if not UtilClient.is_unset(request.text_content):
            body['textContent'] = request.text_content
        if not UtilClient.is_unset(request.textbook):
            body['textbook'] = request.textbook
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AITeacherSyncPracticeTaskGenerate',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/syncPractice/generateTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.AITeacherSyncPracticeTaskGenerateResponse(),
            self.call_api(params, req, runtime)
        )

    async def a_iteacher_sync_practice_task_generate_with_options_async(
        self,
        request: ai_content_20240611_models.AITeacherSyncPracticeTaskGenerateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.AITeacherSyncPracticeTaskGenerateResponse:
        """
        @summary 同步基础练问答对生成
        
        @param request: AITeacherSyncPracticeTaskGenerateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AITeacherSyncPracticeTaskGenerateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.key_sentences):
            body['keySentences'] = request.key_sentences
        if not UtilClient.is_unset(request.key_words):
            body['keyWords'] = request.key_words
        if not UtilClient.is_unset(request.learning_object):
            body['learningObject'] = request.learning_object
        if not UtilClient.is_unset(request.text_content):
            body['textContent'] = request.text_content
        if not UtilClient.is_unset(request.textbook):
            body['textbook'] = request.textbook
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AITeacherSyncPracticeTaskGenerate',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/syncPractice/generateTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.AITeacherSyncPracticeTaskGenerateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def a_iteacher_sync_practice_task_generate(
        self,
        request: ai_content_20240611_models.AITeacherSyncPracticeTaskGenerateRequest,
    ) -> ai_content_20240611_models.AITeacherSyncPracticeTaskGenerateResponse:
        """
        @summary 同步基础练问答对生成
        
        @param request: AITeacherSyncPracticeTaskGenerateRequest
        @return: AITeacherSyncPracticeTaskGenerateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.a_iteacher_sync_practice_task_generate_with_options(request, headers, runtime)

    async def a_iteacher_sync_practice_task_generate_async(
        self,
        request: ai_content_20240611_models.AITeacherSyncPracticeTaskGenerateRequest,
    ) -> ai_content_20240611_models.AITeacherSyncPracticeTaskGenerateResponse:
        """
        @summary 同步基础练问答对生成
        
        @param request: AITeacherSyncPracticeTaskGenerateRequest
        @return: AITeacherSyncPracticeTaskGenerateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.a_iteacher_sync_practice_task_generate_with_options_async(request, headers, runtime)

    def aliyun_console_open_api_query_aliyun_console_servcie_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AliyunConsoleOpenApiQueryAliyunConsoleServcieList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunconsole/queryAliyunConsoleServcieList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse(),
            self.call_api(params, req, runtime)
        )

    async def aliyun_console_open_api_query_aliyun_console_servcie_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AliyunConsoleOpenApiQueryAliyunConsoleServcieList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunconsole/queryAliyunConsoleServcieList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aliyun_console_open_api_query_aliyun_console_servcie_list(self) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.aliyun_console_open_api_query_aliyun_console_servcie_list_with_options(headers, runtime)

    async def aliyun_console_open_api_query_aliyun_console_servcie_list_async(self) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.aliyun_console_open_api_query_aliyun_console_servcie_list_with_options_async(headers, runtime)

    def aliyun_console_open_api_query_aliyun_console_service_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AliyunConsoleOpenApiQueryAliyunConsoleServiceList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunconsole/queryAliyunConsoleServiceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def aliyun_console_open_api_query_aliyun_console_service_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='AliyunConsoleOpenApiQueryAliyunConsoleServiceList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunconsole/queryAliyunConsoleServiceList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aliyun_console_open_api_query_aliyun_console_service_list(self) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.aliyun_console_open_api_query_aliyun_console_service_list_with_options(headers, runtime)

    async def aliyun_console_open_api_query_aliyun_console_service_list_async(self) -> ai_content_20240611_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse:
        """
        @summary 阿里云控制台/列出阿里云控制台上可使用的服务列表
        
        @return: AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.aliyun_console_open_api_query_aliyun_console_service_list_with_options_async(headers, runtime)

    def execute_aiteacher_expansion_dialogue_with_options(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherExpansionDialogueResponse:
        """
        @summary 进行拓展练对话
        
        @param request: ExecuteAITeacherExpansionDialogueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherExpansionDialogueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.background):
            body['background'] = request.background
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.language_code):
            body['languageCode'] = request.language_code
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.role_info):
            body['roleInfo'] = request.role_info
        if not UtilClient.is_unset(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherExpansionDialogue',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/expansionPractice/executeExpansionTraining',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherExpansionDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_expansion_dialogue_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherExpansionDialogueResponse:
        """
        @summary 进行拓展练对话
        
        @param request: ExecuteAITeacherExpansionDialogueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherExpansionDialogueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.background):
            body['background'] = request.background
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.language_code):
            body['languageCode'] = request.language_code
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.role_info):
            body['roleInfo'] = request.role_info
        if not UtilClient.is_unset(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherExpansionDialogue',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/expansionPractice/executeExpansionTraining',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherExpansionDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_expansion_dialogue(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherExpansionDialogueResponse:
        """
        @summary 进行拓展练对话
        
        @param request: ExecuteAITeacherExpansionDialogueRequest
        @return: ExecuteAITeacherExpansionDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_expansion_dialogue_with_options(request, headers, runtime)

    async def execute_aiteacher_expansion_dialogue_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherExpansionDialogueResponse:
        """
        @summary 进行拓展练对话
        
        @param request: ExecuteAITeacherExpansionDialogueRequest
        @return: ExecuteAITeacherExpansionDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_expansion_dialogue_with_options_async(request, headers, runtime)

    def execute_aiteacher_expansion_dialogue_refine_with_options(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRefineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRefineResponse:
        """
        @summary 拓展练根据上下文进行润色
        
        @param request: ExecuteAITeacherExpansionDialogueRefineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherExpansionDialogueRefineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.background):
            body['background'] = request.background
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.language_code):
            body['languageCode'] = request.language_code
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.role_info):
            body['roleInfo'] = request.role_info
        if not UtilClient.is_unset(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherExpansionDialogueRefine',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/expansionPractice/refineByContext',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRefineResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_expansion_dialogue_refine_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRefineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRefineResponse:
        """
        @summary 拓展练根据上下文进行润色
        
        @param request: ExecuteAITeacherExpansionDialogueRefineRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherExpansionDialogueRefineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.background):
            body['background'] = request.background
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.language_code):
            body['languageCode'] = request.language_code
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.role_info):
            body['roleInfo'] = request.role_info
        if not UtilClient.is_unset(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherExpansionDialogueRefine',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/expansionPractice/refineByContext',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRefineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_expansion_dialogue_refine(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRefineRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRefineResponse:
        """
        @summary 拓展练根据上下文进行润色
        
        @param request: ExecuteAITeacherExpansionDialogueRefineRequest
        @return: ExecuteAITeacherExpansionDialogueRefineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_expansion_dialogue_refine_with_options(request, headers, runtime)

    async def execute_aiteacher_expansion_dialogue_refine_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRefineRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherExpansionDialogueRefineResponse:
        """
        @summary 拓展练根据上下文进行润色
        
        @param request: ExecuteAITeacherExpansionDialogueRefineRequest
        @return: ExecuteAITeacherExpansionDialogueRefineResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_expansion_dialogue_refine_with_options_async(request, headers, runtime)

    def execute_aiteacher_expansion_dialogue_translate_with_options(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherExpansionDialogueTranslateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherExpansionDialogueTranslateResponse:
        """
        @summary 拓展练语境翻译
        
        @param request: ExecuteAITeacherExpansionDialogueTranslateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherExpansionDialogueTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.background):
            body['background'] = request.background
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.role_info):
            body['roleInfo'] = request.role_info
        if not UtilClient.is_unset(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherExpansionDialogueTranslate',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/expansionPractice/translate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherExpansionDialogueTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_expansion_dialogue_translate_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherExpansionDialogueTranslateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherExpansionDialogueTranslateResponse:
        """
        @summary 拓展练语境翻译
        
        @param request: ExecuteAITeacherExpansionDialogueTranslateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherExpansionDialogueTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.background):
            body['background'] = request.background
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.role_info):
            body['roleInfo'] = request.role_info
        if not UtilClient.is_unset(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherExpansionDialogueTranslate',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/expansionPractice/translate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherExpansionDialogueTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_expansion_dialogue_translate(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherExpansionDialogueTranslateRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherExpansionDialogueTranslateResponse:
        """
        @summary 拓展练语境翻译
        
        @param request: ExecuteAITeacherExpansionDialogueTranslateRequest
        @return: ExecuteAITeacherExpansionDialogueTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_expansion_dialogue_translate_with_options(request, headers, runtime)

    async def execute_aiteacher_expansion_dialogue_translate_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherExpansionDialogueTranslateRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherExpansionDialogueTranslateResponse:
        """
        @summary 拓展练语境翻译
        
        @param request: ExecuteAITeacherExpansionDialogueTranslateRequest
        @return: ExecuteAITeacherExpansionDialogueTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_expansion_dialogue_translate_with_options_async(request, headers, runtime)

    def execute_aiteacher_grammar_check_with_options(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherGrammarCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherGrammarCheckResponse:
        """
        @summary 语法检测
        
        @param request: ExecuteAITeacherGrammarCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherGrammarCheckResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherGrammarCheck',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/common/grammarChecking',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherGrammarCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_grammar_check_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherGrammarCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherGrammarCheckResponse:
        """
        @summary 语法检测
        
        @param request: ExecuteAITeacherGrammarCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherGrammarCheckResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherGrammarCheck',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/common/grammarChecking',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherGrammarCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_grammar_check(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherGrammarCheckRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherGrammarCheckResponse:
        """
        @summary 语法检测
        
        @param request: ExecuteAITeacherGrammarCheckRequest
        @return: ExecuteAITeacherGrammarCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_grammar_check_with_options(request, headers, runtime)

    async def execute_aiteacher_grammar_check_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherGrammarCheckRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherGrammarCheckResponse:
        """
        @summary 语法检测
        
        @param request: ExecuteAITeacherGrammarCheckRequest
        @return: ExecuteAITeacherGrammarCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_grammar_check_with_options_async(request, headers, runtime)

    def execute_aiteacher_sync_dialogue_with_options(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherSyncDialogueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherSyncDialogueResponse:
        """
        @summary 进行同步练对话
        
        @param request: ExecuteAITeacherSyncDialogueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherSyncDialogueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.language_code):
            body['languageCode'] = request.language_code
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherSyncDialogue',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/syncPractice/executeSyncTraining',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherSyncDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_sync_dialogue_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherSyncDialogueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherSyncDialogueResponse:
        """
        @summary 进行同步练对话
        
        @param request: ExecuteAITeacherSyncDialogueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherSyncDialogueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.language_code):
            body['languageCode'] = request.language_code
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherSyncDialogue',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/syncPractice/executeSyncTraining',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherSyncDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_sync_dialogue(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherSyncDialogueRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherSyncDialogueResponse:
        """
        @summary 进行同步练对话
        
        @param request: ExecuteAITeacherSyncDialogueRequest
        @return: ExecuteAITeacherSyncDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_sync_dialogue_with_options(request, headers, runtime)

    async def execute_aiteacher_sync_dialogue_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherSyncDialogueRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherSyncDialogueResponse:
        """
        @summary 进行同步练对话
        
        @param request: ExecuteAITeacherSyncDialogueRequest
        @return: ExecuteAITeacherSyncDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_sync_dialogue_with_options_async(request, headers, runtime)

    def execute_aiteacher_sync_dialogue_translate_with_options(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherSyncDialogueTranslateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherSyncDialogueTranslateResponse:
        """
        @summary 同步练语境翻译
        
        @param request: ExecuteAITeacherSyncDialogueTranslateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherSyncDialogueTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherSyncDialogueTranslate',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/syncPractice/translate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherSyncDialogueTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_sync_dialogue_translate_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherSyncDialogueTranslateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherSyncDialogueTranslateResponse:
        """
        @summary 同步练语境翻译
        
        @param request: ExecuteAITeacherSyncDialogueTranslateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherSyncDialogueTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherSyncDialogueTranslate',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/syncPractice/translate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherSyncDialogueTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_sync_dialogue_translate(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherSyncDialogueTranslateRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherSyncDialogueTranslateResponse:
        """
        @summary 同步练语境翻译
        
        @param request: ExecuteAITeacherSyncDialogueTranslateRequest
        @return: ExecuteAITeacherSyncDialogueTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_sync_dialogue_translate_with_options(request, headers, runtime)

    async def execute_aiteacher_sync_dialogue_translate_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherSyncDialogueTranslateRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherSyncDialogueTranslateResponse:
        """
        @summary 同步练语境翻译
        
        @param request: ExecuteAITeacherSyncDialogueTranslateRequest
        @return: ExecuteAITeacherSyncDialogueTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_sync_dialogue_translate_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_dialogue_with_options(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantDialogueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantDialogueResponse:
        """
        @summary 进行AI对话
        
        @param request: ExecuteTextbookAssistantDialogueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantDialogueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        if not UtilClient.is_unset(request.user_message):
            body['userMessage'] = request.user_message
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantDialogue',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/ExecuteDialogue',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_dialogue_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantDialogueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantDialogueResponse:
        """
        @summary 进行AI对话
        
        @param request: ExecuteTextbookAssistantDialogueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantDialogueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        if not UtilClient.is_unset(request.user_message):
            body['userMessage'] = request.user_message
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantDialogue',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/ExecuteDialogue',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_dialogue(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantDialogueRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantDialogueResponse:
        """
        @summary 进行AI对话
        
        @param request: ExecuteTextbookAssistantDialogueRequest
        @return: ExecuteTextbookAssistantDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_dialogue_with_options(request, headers, runtime)

    async def execute_textbook_assistant_dialogue_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantDialogueRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantDialogueResponse:
        """
        @summary 进行AI对话
        
        @param request: ExecuteTextbookAssistantDialogueRequest
        @return: ExecuteTextbookAssistantDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_dialogue_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_difficulty_with_options(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantDifficultyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantDifficultyResponse:
        """
        @summary 调整难度
        
        @param request: ExecuteTextbookAssistantDifficultyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantDifficultyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.assistant):
            body['assistant'] = request.assistant
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantDifficulty',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/ExecuteDifficulty',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantDifficultyResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_difficulty_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantDifficultyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantDifficultyResponse:
        """
        @summary 调整难度
        
        @param request: ExecuteTextbookAssistantDifficultyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantDifficultyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action):
            body['action'] = request.action
        if not UtilClient.is_unset(request.assistant):
            body['assistant'] = request.assistant
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantDifficulty',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/ExecuteDifficulty',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantDifficultyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_difficulty(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantDifficultyRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantDifficultyResponse:
        """
        @summary 调整难度
        
        @param request: ExecuteTextbookAssistantDifficultyRequest
        @return: ExecuteTextbookAssistantDifficultyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_difficulty_with_options(request, headers, runtime)

    async def execute_textbook_assistant_difficulty_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantDifficultyRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantDifficultyResponse:
        """
        @summary 调整难度
        
        @param request: ExecuteTextbookAssistantDifficultyRequest
        @return: ExecuteTextbookAssistantDifficultyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_difficulty_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_grammar_check_with_options(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantGrammarCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantGrammarCheckResponse:
        """
        @summary 语法检测
        
        @param request: ExecuteTextbookAssistantGrammarCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantGrammarCheckResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        if not UtilClient.is_unset(request.user):
            body['user'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantGrammarCheck',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/ExecuteGrammarCheck',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantGrammarCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_grammar_check_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantGrammarCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantGrammarCheckResponse:
        """
        @summary 语法检测
        
        @param request: ExecuteTextbookAssistantGrammarCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantGrammarCheckResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        if not UtilClient.is_unset(request.user):
            body['user'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantGrammarCheck',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/ExecuteGrammarCheck',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantGrammarCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_grammar_check(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantGrammarCheckRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantGrammarCheckResponse:
        """
        @summary 语法检测
        
        @param request: ExecuteTextbookAssistantGrammarCheckRequest
        @return: ExecuteTextbookAssistantGrammarCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_grammar_check_with_options(request, headers, runtime)

    async def execute_textbook_assistant_grammar_check_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantGrammarCheckRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantGrammarCheckResponse:
        """
        @summary 语法检测
        
        @param request: ExecuteTextbookAssistantGrammarCheckRequest
        @return: ExecuteTextbookAssistantGrammarCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_grammar_check_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_refine_by_context_with_options(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantRefineByContextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantRefineByContextResponse:
        """
        @summary 句子润色
        
        @param request: ExecuteTextbookAssistantRefineByContextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantRefineByContextResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        if not UtilClient.is_unset(request.user):
            body['user'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantRefineByContext',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/RefineByContext',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantRefineByContextResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_refine_by_context_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantRefineByContextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantRefineByContextResponse:
        """
        @summary 句子润色
        
        @param request: ExecuteTextbookAssistantRefineByContextRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantRefineByContextResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        if not UtilClient.is_unset(request.user):
            body['user'] = request.user
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantRefineByContext',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/RefineByContext',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantRefineByContextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_refine_by_context(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantRefineByContextRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantRefineByContextResponse:
        """
        @summary 句子润色
        
        @param request: ExecuteTextbookAssistantRefineByContextRequest
        @return: ExecuteTextbookAssistantRefineByContextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_refine_by_context_with_options(request, headers, runtime)

    async def execute_textbook_assistant_refine_by_context_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantRefineByContextRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantRefineByContextResponse:
        """
        @summary 句子润色
        
        @param request: ExecuteTextbookAssistantRefineByContextRequest
        @return: ExecuteTextbookAssistantRefineByContextResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_refine_by_context_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_retry_conversation_with_options(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantRetryConversationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantRetryConversationResponse:
        """
        @summary 对话重试
        
        @param request: ExecuteTextbookAssistantRetryConversationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantRetryConversationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assistant):
            body['assistant'] = request.assistant
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantRetryConversation',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/RetryConversation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantRetryConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_retry_conversation_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantRetryConversationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantRetryConversationResponse:
        """
        @summary 对话重试
        
        @param request: ExecuteTextbookAssistantRetryConversationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantRetryConversationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assistant):
            body['assistant'] = request.assistant
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantRetryConversation',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/RetryConversation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantRetryConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_retry_conversation(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantRetryConversationRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantRetryConversationResponse:
        """
        @summary 对话重试
        
        @param request: ExecuteTextbookAssistantRetryConversationRequest
        @return: ExecuteTextbookAssistantRetryConversationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_retry_conversation_with_options(request, headers, runtime)

    async def execute_textbook_assistant_retry_conversation_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantRetryConversationRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantRetryConversationResponse:
        """
        @summary 对话重试
        
        @param request: ExecuteTextbookAssistantRetryConversationRequest
        @return: ExecuteTextbookAssistantRetryConversationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_retry_conversation_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_start_conversation_with_options(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantStartConversationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantStartConversationResponse:
        """
        @summary 开启自由对话
        
        @param request: ExecuteTextbookAssistantStartConversationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantStartConversationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.article_id):
            body['articleId'] = request.article_id
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantStartConversation',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/StartConversation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantStartConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_start_conversation_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantStartConversationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantStartConversationResponse:
        """
        @summary 开启自由对话
        
        @param request: ExecuteTextbookAssistantStartConversationRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantStartConversationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.article_id):
            body['articleId'] = request.article_id
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantStartConversation',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/StartConversation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantStartConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_start_conversation(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantStartConversationRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantStartConversationResponse:
        """
        @summary 开启自由对话
        
        @param request: ExecuteTextbookAssistantStartConversationRequest
        @return: ExecuteTextbookAssistantStartConversationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_start_conversation_with_options(request, headers, runtime)

    async def execute_textbook_assistant_start_conversation_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantStartConversationRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantStartConversationResponse:
        """
        @summary 开启自由对话
        
        @param request: ExecuteTextbookAssistantStartConversationRequest
        @return: ExecuteTextbookAssistantStartConversationResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_start_conversation_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_suggestion_with_options(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantSuggestionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantSuggestionResponse:
        """
        @summary 获取鉴权参数
        
        @param request: ExecuteTextbookAssistantSuggestionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantSuggestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assistant):
            body['assistant'] = request.assistant
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantSuggestion',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/Suggestion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantSuggestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_suggestion_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantSuggestionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantSuggestionResponse:
        """
        @summary 获取鉴权参数
        
        @param request: ExecuteTextbookAssistantSuggestionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantSuggestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assistant):
            body['assistant'] = request.assistant
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantSuggestion',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/Suggestion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantSuggestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_suggestion(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantSuggestionRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantSuggestionResponse:
        """
        @summary 获取鉴权参数
        
        @param request: ExecuteTextbookAssistantSuggestionRequest
        @return: ExecuteTextbookAssistantSuggestionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_suggestion_with_options(request, headers, runtime)

    async def execute_textbook_assistant_suggestion_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantSuggestionRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantSuggestionResponse:
        """
        @summary 获取鉴权参数
        
        @param request: ExecuteTextbookAssistantSuggestionRequest
        @return: ExecuteTextbookAssistantSuggestionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_suggestion_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_translate_with_options(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantTranslateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantTranslateResponse:
        """
        @summary 翻译消息内容
        
        @param request: ExecuteTextbookAssistantTranslateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assistant):
            body['assistant'] = request.assistant
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantTranslate',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/ExecuteTranslate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_translate_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantTranslateRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantTranslateResponse:
        """
        @summary 翻译消息内容
        
        @param request: ExecuteTextbookAssistantTranslateRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantTranslateResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assistant):
            body['assistant'] = request.assistant
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTextbookAssistantTranslate',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/ExecuteTranslate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_translate(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantTranslateRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantTranslateResponse:
        """
        @summary 翻译消息内容
        
        @param request: ExecuteTextbookAssistantTranslateRequest
        @return: ExecuteTextbookAssistantTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_translate_with_options(request, headers, runtime)

    async def execute_textbook_assistant_translate_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantTranslateRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantTranslateResponse:
        """
        @summary 翻译消息内容
        
        @param request: ExecuteTextbookAssistantTranslateRequest
        @return: ExecuteTextbookAssistantTranslateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_translate_with_options_async(request, headers, runtime)

    def get_aiteacher_expansion_dialogue_suggestion_with_options(
        self,
        request: ai_content_20240611_models.GetAITeacherExpansionDialogueSuggestionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.GetAITeacherExpansionDialogueSuggestionResponse:
        """
        @summary 拓展练小助手
        
        @param request: GetAITeacherExpansionDialogueSuggestionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAITeacherExpansionDialogueSuggestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.background):
            body['background'] = request.background
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.language_code):
            body['languageCode'] = request.language_code
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.role_info):
            body['roleInfo'] = request.role_info
        if not UtilClient.is_unset(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAITeacherExpansionDialogueSuggestion',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/expansionPractice/suggestion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.GetAITeacherExpansionDialogueSuggestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aiteacher_expansion_dialogue_suggestion_with_options_async(
        self,
        request: ai_content_20240611_models.GetAITeacherExpansionDialogueSuggestionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.GetAITeacherExpansionDialogueSuggestionResponse:
        """
        @summary 拓展练小助手
        
        @param request: GetAITeacherExpansionDialogueSuggestionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAITeacherExpansionDialogueSuggestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.background):
            body['background'] = request.background
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.language_code):
            body['languageCode'] = request.language_code
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.role_info):
            body['roleInfo'] = request.role_info
        if not UtilClient.is_unset(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not UtilClient.is_unset(request.topic):
            body['topic'] = request.topic
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAITeacherExpansionDialogueSuggestion',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/expansionPractice/suggestion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.GetAITeacherExpansionDialogueSuggestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aiteacher_expansion_dialogue_suggestion(
        self,
        request: ai_content_20240611_models.GetAITeacherExpansionDialogueSuggestionRequest,
    ) -> ai_content_20240611_models.GetAITeacherExpansionDialogueSuggestionResponse:
        """
        @summary 拓展练小助手
        
        @param request: GetAITeacherExpansionDialogueSuggestionRequest
        @return: GetAITeacherExpansionDialogueSuggestionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_aiteacher_expansion_dialogue_suggestion_with_options(request, headers, runtime)

    async def get_aiteacher_expansion_dialogue_suggestion_async(
        self,
        request: ai_content_20240611_models.GetAITeacherExpansionDialogueSuggestionRequest,
    ) -> ai_content_20240611_models.GetAITeacherExpansionDialogueSuggestionResponse:
        """
        @summary 拓展练小助手
        
        @param request: GetAITeacherExpansionDialogueSuggestionRequest
        @return: GetAITeacherExpansionDialogueSuggestionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_aiteacher_expansion_dialogue_suggestion_with_options_async(request, headers, runtime)

    def get_aiteacher_sync_dialogue_suggestion_with_options(
        self,
        request: ai_content_20240611_models.GetAITeacherSyncDialogueSuggestionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.GetAITeacherSyncDialogueSuggestionResponse:
        """
        @summary 同步练小助手
        
        @param request: GetAITeacherSyncDialogueSuggestionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAITeacherSyncDialogueSuggestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.language_code):
            body['languageCode'] = request.language_code
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAITeacherSyncDialogueSuggestion',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/syncPractice/suggestion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.GetAITeacherSyncDialogueSuggestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aiteacher_sync_dialogue_suggestion_with_options_async(
        self,
        request: ai_content_20240611_models.GetAITeacherSyncDialogueSuggestionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.GetAITeacherSyncDialogueSuggestionResponse:
        """
        @summary 同步练小助手
        
        @param request: GetAITeacherSyncDialogueSuggestionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAITeacherSyncDialogueSuggestionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not UtilClient.is_unset(request.language_code):
            body['languageCode'] = request.language_code
        if not UtilClient.is_unset(request.records):
            body['records'] = request.records
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAITeacherSyncDialogueSuggestion',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aiteacher/syncPractice/suggestion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.GetAITeacherSyncDialogueSuggestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aiteacher_sync_dialogue_suggestion(
        self,
        request: ai_content_20240611_models.GetAITeacherSyncDialogueSuggestionRequest,
    ) -> ai_content_20240611_models.GetAITeacherSyncDialogueSuggestionResponse:
        """
        @summary 同步练小助手
        
        @param request: GetAITeacherSyncDialogueSuggestionRequest
        @return: GetAITeacherSyncDialogueSuggestionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_aiteacher_sync_dialogue_suggestion_with_options(request, headers, runtime)

    async def get_aiteacher_sync_dialogue_suggestion_async(
        self,
        request: ai_content_20240611_models.GetAITeacherSyncDialogueSuggestionRequest,
    ) -> ai_content_20240611_models.GetAITeacherSyncDialogueSuggestionResponse:
        """
        @summary 同步练小助手
        
        @param request: GetAITeacherSyncDialogueSuggestionRequest
        @return: GetAITeacherSyncDialogueSuggestionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_aiteacher_sync_dialogue_suggestion_with_options_async(request, headers, runtime)

    def get_textbook_assistant_token_with_options(
        self,
        request: ai_content_20240611_models.GetTextbookAssistantTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.GetTextbookAssistantTokenResponse:
        """
        @summary 获取请求鉴权参数
        
        @param request: GetTextbookAssistantTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextbookAssistantTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['deviceId'] = request.device_id
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTextbookAssistantToken',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/GetToken',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.GetTextbookAssistantTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_textbook_assistant_token_with_options_async(
        self,
        request: ai_content_20240611_models.GetTextbookAssistantTokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.GetTextbookAssistantTokenResponse:
        """
        @summary 获取请求鉴权参数
        
        @param request: GetTextbookAssistantTokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextbookAssistantTokenResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['deviceId'] = request.device_id
        if not UtilClient.is_unset(request.model):
            body['model'] = request.model
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTextbookAssistantToken',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/GetToken',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.GetTextbookAssistantTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_textbook_assistant_token(
        self,
        request: ai_content_20240611_models.GetTextbookAssistantTokenRequest,
    ) -> ai_content_20240611_models.GetTextbookAssistantTokenResponse:
        """
        @summary 获取请求鉴权参数
        
        @param request: GetTextbookAssistantTokenRequest
        @return: GetTextbookAssistantTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_textbook_assistant_token_with_options(request, headers, runtime)

    async def get_textbook_assistant_token_async(
        self,
        request: ai_content_20240611_models.GetTextbookAssistantTokenRequest,
    ) -> ai_content_20240611_models.GetTextbookAssistantTokenResponse:
        """
        @summary 获取请求鉴权参数
        
        @param request: GetTextbookAssistantTokenRequest
        @return: GetTextbookAssistantTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_textbook_assistant_token_with_options_async(request, headers, runtime)

    def list_textbook_assistant_articles_with_options(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantArticlesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ListTextbookAssistantArticlesResponse:
        """
        @summary 获取文章列表
        
        @param request: ListTextbookAssistantArticlesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextbookAssistantArticlesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.directory_id):
            body['directoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTextbookAssistantArticles',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/ListArticles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ListTextbookAssistantArticlesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_textbook_assistant_articles_with_options_async(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantArticlesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ListTextbookAssistantArticlesResponse:
        """
        @summary 获取文章列表
        
        @param request: ListTextbookAssistantArticlesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextbookAssistantArticlesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.directory_id):
            body['directoryId'] = request.directory_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTextbookAssistantArticles',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/ListArticles',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ListTextbookAssistantArticlesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_textbook_assistant_articles(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantArticlesRequest,
    ) -> ai_content_20240611_models.ListTextbookAssistantArticlesResponse:
        """
        @summary 获取文章列表
        
        @param request: ListTextbookAssistantArticlesRequest
        @return: ListTextbookAssistantArticlesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_textbook_assistant_articles_with_options(request, headers, runtime)

    async def list_textbook_assistant_articles_async(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantArticlesRequest,
    ) -> ai_content_20240611_models.ListTextbookAssistantArticlesResponse:
        """
        @summary 获取文章列表
        
        @param request: ListTextbookAssistantArticlesRequest
        @return: ListTextbookAssistantArticlesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_textbook_assistant_articles_with_options_async(request, headers, runtime)

    def list_textbook_assistant_book_directories_with_options(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantBookDirectoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ListTextbookAssistantBookDirectoriesResponse:
        """
        @summary 获取书本下的目录信息
        
        @param request: ListTextbookAssistantBookDirectoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextbookAssistantBookDirectoriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.book_id):
            body['bookId'] = request.book_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTextbookAssistantBookDirectories',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/ListBookDirectories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ListTextbookAssistantBookDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_textbook_assistant_book_directories_with_options_async(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantBookDirectoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ListTextbookAssistantBookDirectoriesResponse:
        """
        @summary 获取书本下的目录信息
        
        @param request: ListTextbookAssistantBookDirectoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextbookAssistantBookDirectoriesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.book_id):
            body['bookId'] = request.book_id
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTextbookAssistantBookDirectories',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/ListBookDirectories',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ListTextbookAssistantBookDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_textbook_assistant_book_directories(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantBookDirectoriesRequest,
    ) -> ai_content_20240611_models.ListTextbookAssistantBookDirectoriesResponse:
        """
        @summary 获取书本下的目录信息
        
        @param request: ListTextbookAssistantBookDirectoriesRequest
        @return: ListTextbookAssistantBookDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_textbook_assistant_book_directories_with_options(request, headers, runtime)

    async def list_textbook_assistant_book_directories_async(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantBookDirectoriesRequest,
    ) -> ai_content_20240611_models.ListTextbookAssistantBookDirectoriesResponse:
        """
        @summary 获取书本下的目录信息
        
        @param request: ListTextbookAssistantBookDirectoriesRequest
        @return: ListTextbookAssistantBookDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_textbook_assistant_book_directories_with_options_async(request, headers, runtime)

    def list_textbook_assistant_books_with_options(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantBooksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ListTextbookAssistantBooksResponse:
        """
        @summary 获取包含年级下的书本列表
        
        @param request: ListTextbookAssistantBooksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextbookAssistantBooksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.book_id):
            body['bookId'] = request.book_id
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.volume):
            body['volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTextbookAssistantBooks',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/ListBooks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ListTextbookAssistantBooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_textbook_assistant_books_with_options_async(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantBooksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ListTextbookAssistantBooksResponse:
        """
        @summary 获取包含年级下的书本列表
        
        @param request: ListTextbookAssistantBooksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextbookAssistantBooksResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.book_id):
            body['bookId'] = request.book_id
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.max_results):
            body['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.page):
            body['page'] = request.page
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        if not UtilClient.is_unset(request.volume):
            body['volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTextbookAssistantBooks',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/ListBooks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ListTextbookAssistantBooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_textbook_assistant_books(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantBooksRequest,
    ) -> ai_content_20240611_models.ListTextbookAssistantBooksResponse:
        """
        @summary 获取包含年级下的书本列表
        
        @param request: ListTextbookAssistantBooksRequest
        @return: ListTextbookAssistantBooksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_textbook_assistant_books_with_options(request, headers, runtime)

    async def list_textbook_assistant_books_async(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantBooksRequest,
    ) -> ai_content_20240611_models.ListTextbookAssistantBooksResponse:
        """
        @summary 获取包含年级下的书本列表
        
        @param request: ListTextbookAssistantBooksRequest
        @return: ListTextbookAssistantBooksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_textbook_assistant_books_with_options_async(request, headers, runtime)

    def list_textbook_assistant_grade_volumes_with_options(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantGradeVolumesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ListTextbookAssistantGradeVolumesResponse:
        """
        @summary 获取有资源的年级信息
        
        @param request: ListTextbookAssistantGradeVolumesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextbookAssistantGradeVolumesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTextbookAssistantGradeVolumes',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/ListGradeVolumes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ListTextbookAssistantGradeVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_textbook_assistant_grade_volumes_with_options_async(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantGradeVolumesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ListTextbookAssistantGradeVolumesResponse:
        """
        @summary 获取有资源的年级信息
        
        @param request: ListTextbookAssistantGradeVolumesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextbookAssistantGradeVolumesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTextbookAssistantGradeVolumes',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/ListGradeVolumes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ListTextbookAssistantGradeVolumesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_textbook_assistant_grade_volumes(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantGradeVolumesRequest,
    ) -> ai_content_20240611_models.ListTextbookAssistantGradeVolumesResponse:
        """
        @summary 获取有资源的年级信息
        
        @param request: ListTextbookAssistantGradeVolumesRequest
        @return: ListTextbookAssistantGradeVolumesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_textbook_assistant_grade_volumes_with_options(request, headers, runtime)

    async def list_textbook_assistant_grade_volumes_async(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantGradeVolumesRequest,
    ) -> ai_content_20240611_models.ListTextbookAssistantGradeVolumesResponse:
        """
        @summary 获取有资源的年级信息
        
        @param request: ListTextbookAssistantGradeVolumesRequest
        @return: ListTextbookAssistantGradeVolumesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_textbook_assistant_grade_volumes_with_options_async(request, headers, runtime)

    def personalized_text_to_image_add_inference_job_with_options(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个预训练模型创建图片推理任务
        
        @param request: PersonalizedTextToImageAddInferenceJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PersonalizedTextToImageAddInferenceJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_number):
            body['imageNumber'] = request.image_number
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.seed):
            body['seed'] = request.seed
        if not UtilClient.is_unset(request.strength):
            body['strength'] = request.strength
        if not UtilClient.is_unset(request.train_steps):
            body['trainSteps'] = request.train_steps
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PersonalizedTextToImageAddInferenceJob',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/addPreModelInferenceJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalized_text_to_image_add_inference_job_with_options_async(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个预训练模型创建图片推理任务
        
        @param request: PersonalizedTextToImageAddInferenceJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PersonalizedTextToImageAddInferenceJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_number):
            body['imageNumber'] = request.image_number
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.seed):
            body['seed'] = request.seed
        if not UtilClient.is_unset(request.strength):
            body['strength'] = request.strength
        if not UtilClient.is_unset(request.train_steps):
            body['trainSteps'] = request.train_steps
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PersonalizedTextToImageAddInferenceJob',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/addPreModelInferenceJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalized_text_to_image_add_inference_job(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobRequest,
    ) -> ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个预训练模型创建图片推理任务
        
        @param request: PersonalizedTextToImageAddInferenceJobRequest
        @return: PersonalizedTextToImageAddInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalized_text_to_image_add_inference_job_with_options(request, headers, runtime)

    async def personalized_text_to_image_add_inference_job_async(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobRequest,
    ) -> ai_content_20240611_models.PersonalizedTextToImageAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个预训练模型创建图片推理任务
        
        @param request: PersonalizedTextToImageAddInferenceJobRequest
        @return: PersonalizedTextToImageAddInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalized_text_to_image_add_inference_job_with_options_async(request, headers, runtime)

    def personalized_text_to_image_query_image_asset_with_options(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetResponse:
        """
        @summary 个性化文生图/通过唯一的图片编号获取图片内容
        
        @param request: PersonalizedTextToImageQueryImageAssetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PersonalizedTextToImageQueryImageAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encode_format):
            query['encodeFormat'] = request.encode_format
        if not UtilClient.is_unset(request.image_id):
            query['imageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PersonalizedTextToImageQueryImageAsset',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryImageAssetFromImageId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='any'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalized_text_to_image_query_image_asset_with_options_async(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetResponse:
        """
        @summary 个性化文生图/通过唯一的图片编号获取图片内容
        
        @param request: PersonalizedTextToImageQueryImageAssetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PersonalizedTextToImageQueryImageAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encode_format):
            query['encodeFormat'] = request.encode_format
        if not UtilClient.is_unset(request.image_id):
            query['imageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PersonalizedTextToImageQueryImageAsset',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryImageAssetFromImageId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='any'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalized_text_to_image_query_image_asset(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetRequest,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetResponse:
        """
        @summary 个性化文生图/通过唯一的图片编号获取图片内容
        
        @param request: PersonalizedTextToImageQueryImageAssetRequest
        @return: PersonalizedTextToImageQueryImageAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalized_text_to_image_query_image_asset_with_options(request, headers, runtime)

    async def personalized_text_to_image_query_image_asset_async(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetRequest,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryImageAssetResponse:
        """
        @summary 个性化文生图/通过唯一的图片编号获取图片内容
        
        @param request: PersonalizedTextToImageQueryImageAssetRequest
        @return: PersonalizedTextToImageQueryImageAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalized_text_to_image_query_image_asset_with_options_async(request, headers, runtime)

    def personalized_text_to_image_query_pre_model_inference_job_info_with_options(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询预制模型推理任务的状态
        
        @param request: PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.inference_job_id):
            query['inferenceJobId'] = request.inference_job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PersonalizedTextToImageQueryPreModelInferenceJobInfo',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryPreModelInferenceJobInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalized_text_to_image_query_pre_model_inference_job_info_with_options_async(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询预制模型推理任务的状态
        
        @param request: PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.inference_job_id):
            query['inferenceJobId'] = request.inference_job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PersonalizedTextToImageQueryPreModelInferenceJobInfo',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryPreModelInferenceJobInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalized_text_to_image_query_pre_model_inference_job_info(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询预制模型推理任务的状态
        
        @param request: PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest
        @return: PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalized_text_to_image_query_pre_model_inference_job_info_with_options(request, headers, runtime)

    async def personalized_text_to_image_query_pre_model_inference_job_info_async(
        self,
        request: ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest,
    ) -> ai_content_20240611_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询预制模型推理任务的状态
        
        @param request: PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest
        @return: PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalized_text_to_image_query_pre_model_inference_job_info_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_add_inference_job_with_options(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个模型创建图片推理任务
        
        @param request: Personalizedtxt2imgAddInferenceJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgAddInferenceJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_number):
            body['imageNumber'] = request.image_number
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.seed):
            body['seed'] = request.seed
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgAddInferenceJob',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/addInferenceJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_add_inference_job_with_options_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个模型创建图片推理任务
        
        @param request: Personalizedtxt2imgAddInferenceJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgAddInferenceJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_number):
            body['imageNumber'] = request.image_number
        if not UtilClient.is_unset(request.model_id):
            body['modelId'] = request.model_id
        if not UtilClient.is_unset(request.prompt):
            body['prompt'] = request.prompt
        if not UtilClient.is_unset(request.seed):
            body['seed'] = request.seed
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgAddInferenceJob',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/addInferenceJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_add_inference_job(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个模型创建图片推理任务
        
        @param request: Personalizedtxt2imgAddInferenceJobRequest
        @return: Personalizedtxt2imgAddInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_add_inference_job_with_options(request, headers, runtime)

    async def personalizedtxt_2img_add_inference_job_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddInferenceJobResponse:
        """
        @summary 个性化文生图/基于一个模型创建图片推理任务
        
        @param request: Personalizedtxt2imgAddInferenceJobRequest
        @return: Personalizedtxt2imgAddInferenceJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_add_inference_job_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_add_model_train_job_with_options(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobResponse:
        """
        @summary 个性化文生图/创建一个模型训练任务
        
        @param request: Personalizedtxt2imgAddModelTrainJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgAddModelTrainJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.object_type):
            body['objectType'] = request.object_type
        if not UtilClient.is_unset(request.train_steps):
            body['trainSteps'] = request.train_steps
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgAddModelTrainJob',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/addModelTrainJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_add_model_train_job_with_options_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobResponse:
        """
        @summary 个性化文生图/创建一个模型训练任务
        
        @param request: Personalizedtxt2imgAddModelTrainJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgAddModelTrainJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['imageUrl'] = request.image_url
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.object_type):
            body['objectType'] = request.object_type
        if not UtilClient.is_unset(request.train_steps):
            body['trainSteps'] = request.train_steps
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgAddModelTrainJob',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/addModelTrainJob',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_add_model_train_job(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobResponse:
        """
        @summary 个性化文生图/创建一个模型训练任务
        
        @param request: Personalizedtxt2imgAddModelTrainJobRequest
        @return: Personalizedtxt2imgAddModelTrainJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_add_model_train_job_with_options(request, headers, runtime)

    async def personalizedtxt_2img_add_model_train_job_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgAddModelTrainJobResponse:
        """
        @summary 个性化文生图/创建一个模型训练任务
        
        @param request: Personalizedtxt2imgAddModelTrainJobRequest
        @return: Personalizedtxt2imgAddModelTrainJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_add_model_train_job_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_query_image_asset_with_options(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetResponse:
        """
        @summary 个性化文生图/图片二进制内容获取
        
        @param request: Personalizedtxt2imgQueryImageAssetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryImageAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encode_format):
            query['encodeFormat'] = request.encode_format
        if not UtilClient.is_unset(request.image_id):
            query['imageId'] = request.image_id
        if not UtilClient.is_unset(request.model_id):
            query['modelId'] = request.model_id
        if not UtilClient.is_unset(request.prompt_id):
            query['promptId'] = request.prompt_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryImageAsset',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryImageAsset',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='any'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_query_image_asset_with_options_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetResponse:
        """
        @summary 个性化文生图/图片二进制内容获取
        
        @param request: Personalizedtxt2imgQueryImageAssetRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryImageAssetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encode_format):
            query['encodeFormat'] = request.encode_format
        if not UtilClient.is_unset(request.image_id):
            query['imageId'] = request.image_id
        if not UtilClient.is_unset(request.model_id):
            query['modelId'] = request.model_id
        if not UtilClient.is_unset(request.prompt_id):
            query['promptId'] = request.prompt_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryImageAsset',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryImageAsset',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='any'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_query_image_asset(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetResponse:
        """
        @summary 个性化文生图/图片二进制内容获取
        
        @param request: Personalizedtxt2imgQueryImageAssetRequest
        @return: Personalizedtxt2imgQueryImageAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_query_image_asset_with_options(request, headers, runtime)

    async def personalizedtxt_2img_query_image_asset_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryImageAssetResponse:
        """
        @summary 个性化文生图/图片二进制内容获取
        
        @param request: Personalizedtxt2imgQueryImageAssetRequest
        @return: Personalizedtxt2imgQueryImageAssetResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_query_image_asset_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_query_inference_job_info_with_options(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询模型推理任务的状态和结果信息
        
        @param request: Personalizedtxt2imgQueryInferenceJobInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryInferenceJobInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.inference_job_id):
            query['inferenceJobId'] = request.inference_job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryInferenceJobInfo',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryInferenceJobInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_query_inference_job_info_with_options_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询模型推理任务的状态和结果信息
        
        @param request: Personalizedtxt2imgQueryInferenceJobInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryInferenceJobInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.inference_job_id):
            query['inferenceJobId'] = request.inference_job_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryInferenceJobInfo',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryInferenceJobInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_query_inference_job_info(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询模型推理任务的状态和结果信息
        
        @param request: Personalizedtxt2imgQueryInferenceJobInfoRequest
        @return: Personalizedtxt2imgQueryInferenceJobInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_query_inference_job_info_with_options(request, headers, runtime)

    async def personalizedtxt_2img_query_inference_job_info_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryInferenceJobInfoResponse:
        """
        @summary 个性化文生图/查询模型推理任务的状态和结果信息
        
        @param request: Personalizedtxt2imgQueryInferenceJobInfoRequest
        @return: Personalizedtxt2imgQueryInferenceJobInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_query_inference_job_info_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_query_model_train_job_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainJobListResponse:
        """
        @summary 个性化文生图/查询模型训练任务列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryModelTrainJobListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryModelTrainJobList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryModelTrainJobList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_query_model_train_job_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainJobListResponse:
        """
        @summary 个性化文生图/查询模型训练任务列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryModelTrainJobListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryModelTrainJobList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryModelTrainJobList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_query_model_train_job_list(self) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainJobListResponse:
        """
        @summary 个性化文生图/查询模型训练任务列表
        
        @return: Personalizedtxt2imgQueryModelTrainJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_query_model_train_job_list_with_options(headers, runtime)

    async def personalizedtxt_2img_query_model_train_job_list_async(self) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainJobListResponse:
        """
        @summary 个性化文生图/查询模型训练任务列表
        
        @return: Personalizedtxt2imgQueryModelTrainJobListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_query_model_train_job_list_with_options_async(headers, runtime)

    def personalizedtxt_2img_query_model_train_status_with_options(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusResponse:
        """
        @summary 个性化文生图/模型训练状态查询
        
        @param request: Personalizedtxt2imgQueryModelTrainStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryModelTrainStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_id):
            query['modelId'] = request.model_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryModelTrainStatus',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryModelTrainStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_query_model_train_status_with_options_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusResponse:
        """
        @summary 个性化文生图/模型训练状态查询
        
        @param request: Personalizedtxt2imgQueryModelTrainStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: Personalizedtxt2imgQueryModelTrainStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_id):
            query['modelId'] = request.model_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Personalizedtxt2imgQueryModelTrainStatus',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/personalizedtxt2img/queryModelTrainStatus',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_query_model_train_status(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusResponse:
        """
        @summary 个性化文生图/模型训练状态查询
        
        @param request: Personalizedtxt2imgQueryModelTrainStatusRequest
        @return: Personalizedtxt2imgQueryModelTrainStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_query_model_train_status_with_options(request, headers, runtime)

    async def personalizedtxt_2img_query_model_train_status_async(
        self,
        request: ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusRequest,
    ) -> ai_content_20240611_models.Personalizedtxt2imgQueryModelTrainStatusResponse:
        """
        @summary 个性化文生图/模型训练状态查询
        
        @param request: Personalizedtxt2imgQueryModelTrainStatusRequest
        @return: Personalizedtxt2imgQueryModelTrainStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_query_model_train_status_with_options_async(request, headers, runtime)
