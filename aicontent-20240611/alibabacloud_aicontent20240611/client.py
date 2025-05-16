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
            pathname=f'/api/v1/aliyunConsole/queryAliyunConsoleServiceList',
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
            pathname=f'/api/v1/aliyunConsole/queryAliyunConsoleServiceList',
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

    def count_oral_evaluation_statistics_calls_with_options(
        self,
        request: ai_content_20240611_models.CountOralEvaluationStatisticsCallsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.CountOralEvaluationStatisticsCallsResponse:
        """
        @summary 智能批改/口语评测/统计/调用量
        
        @param request: CountOralEvaluationStatisticsCallsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CountOralEvaluationStatisticsCallsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CountOralEvaluationStatisticsCalls',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/countOralEvaluationStatisticsCalls',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.CountOralEvaluationStatisticsCallsResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_oral_evaluation_statistics_calls_with_options_async(
        self,
        request: ai_content_20240611_models.CountOralEvaluationStatisticsCallsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.CountOralEvaluationStatisticsCallsResponse:
        """
        @summary 智能批改/口语评测/统计/调用量
        
        @param request: CountOralEvaluationStatisticsCallsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CountOralEvaluationStatisticsCallsResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CountOralEvaluationStatisticsCalls',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/countOralEvaluationStatisticsCalls',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.CountOralEvaluationStatisticsCallsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_oral_evaluation_statistics_calls(
        self,
        request: ai_content_20240611_models.CountOralEvaluationStatisticsCallsRequest,
    ) -> ai_content_20240611_models.CountOralEvaluationStatisticsCallsResponse:
        """
        @summary 智能批改/口语评测/统计/调用量
        
        @param request: CountOralEvaluationStatisticsCallsRequest
        @return: CountOralEvaluationStatisticsCallsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.count_oral_evaluation_statistics_calls_with_options(request, headers, runtime)

    async def count_oral_evaluation_statistics_calls_async(
        self,
        request: ai_content_20240611_models.CountOralEvaluationStatisticsCallsRequest,
    ) -> ai_content_20240611_models.CountOralEvaluationStatisticsCallsResponse:
        """
        @summary 智能批改/口语评测/统计/调用量
        
        @param request: CountOralEvaluationStatisticsCallsRequest
        @return: CountOralEvaluationStatisticsCallsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.count_oral_evaluation_statistics_calls_with_options_async(request, headers, runtime)

    def count_oral_evaluation_statistics_concurrent_with_options(
        self,
        request: ai_content_20240611_models.CountOralEvaluationStatisticsConcurrentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.CountOralEvaluationStatisticsConcurrentResponse:
        """
        @summary 智能批改/口语评测/统计/并发数
        
        @param request: CountOralEvaluationStatisticsConcurrentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CountOralEvaluationStatisticsConcurrentResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CountOralEvaluationStatisticsConcurrent',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/countOralEvaluationStatisticsConcurrent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.CountOralEvaluationStatisticsConcurrentResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_oral_evaluation_statistics_concurrent_with_options_async(
        self,
        request: ai_content_20240611_models.CountOralEvaluationStatisticsConcurrentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.CountOralEvaluationStatisticsConcurrentResponse:
        """
        @summary 智能批改/口语评测/统计/并发数
        
        @param request: CountOralEvaluationStatisticsConcurrentRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CountOralEvaluationStatisticsConcurrentResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CountOralEvaluationStatisticsConcurrent',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/countOralEvaluationStatisticsConcurrent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.CountOralEvaluationStatisticsConcurrentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_oral_evaluation_statistics_concurrent(
        self,
        request: ai_content_20240611_models.CountOralEvaluationStatisticsConcurrentRequest,
    ) -> ai_content_20240611_models.CountOralEvaluationStatisticsConcurrentResponse:
        """
        @summary 智能批改/口语评测/统计/并发数
        
        @param request: CountOralEvaluationStatisticsConcurrentRequest
        @return: CountOralEvaluationStatisticsConcurrentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.count_oral_evaluation_statistics_concurrent_with_options(request, headers, runtime)

    async def count_oral_evaluation_statistics_concurrent_async(
        self,
        request: ai_content_20240611_models.CountOralEvaluationStatisticsConcurrentRequest,
    ) -> ai_content_20240611_models.CountOralEvaluationStatisticsConcurrentResponse:
        """
        @summary 智能批改/口语评测/统计/并发数
        
        @param request: CountOralEvaluationStatisticsConcurrentRequest
        @return: CountOralEvaluationStatisticsConcurrentResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.count_oral_evaluation_statistics_concurrent_with_options_async(request, headers, runtime)

    def count_oral_evaluation_statistics_error_with_options(
        self,
        request: ai_content_20240611_models.CountOralEvaluationStatisticsErrorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.CountOralEvaluationStatisticsErrorResponse:
        """
        @summary 智能批改/口语评测/统计/调用错误
        
        @param request: CountOralEvaluationStatisticsErrorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CountOralEvaluationStatisticsErrorResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CountOralEvaluationStatisticsError',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/countOralEvaluationStatisticsError',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.CountOralEvaluationStatisticsErrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_oral_evaluation_statistics_error_with_options_async(
        self,
        request: ai_content_20240611_models.CountOralEvaluationStatisticsErrorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.CountOralEvaluationStatisticsErrorResponse:
        """
        @summary 智能批改/口语评测/统计/调用错误
        
        @param request: CountOralEvaluationStatisticsErrorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CountOralEvaluationStatisticsErrorResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CountOralEvaluationStatisticsError',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/countOralEvaluationStatisticsError',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.CountOralEvaluationStatisticsErrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_oral_evaluation_statistics_error(
        self,
        request: ai_content_20240611_models.CountOralEvaluationStatisticsErrorRequest,
    ) -> ai_content_20240611_models.CountOralEvaluationStatisticsErrorResponse:
        """
        @summary 智能批改/口语评测/统计/调用错误
        
        @param request: CountOralEvaluationStatisticsErrorRequest
        @return: CountOralEvaluationStatisticsErrorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.count_oral_evaluation_statistics_error_with_options(request, headers, runtime)

    async def count_oral_evaluation_statistics_error_async(
        self,
        request: ai_content_20240611_models.CountOralEvaluationStatisticsErrorRequest,
    ) -> ai_content_20240611_models.CountOralEvaluationStatisticsErrorResponse:
        """
        @summary 智能批改/口语评测/统计/调用错误
        
        @param request: CountOralEvaluationStatisticsErrorRequest
        @return: CountOralEvaluationStatisticsErrorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.count_oral_evaluation_statistics_error_with_options_async(request, headers, runtime)

    def create_access_warrant_with_options(
        self,
        request: ai_content_20240611_models.CreateAccessWarrantRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.CreateAccessWarrantResponse:
        """
        @summary 阿里云控制台/授权凭证创建
        
        @param request: CreateAccessWarrantRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessWarrantResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.request_sign):
            body['requestSign'] = request.request_sign
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.user_client_ip):
            body['userClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.warrant_available):
            body['warrantAvailable'] = request.warrant_available
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAccessWarrant',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/createAccessWarrant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.CreateAccessWarrantResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_warrant_with_options_async(
        self,
        request: ai_content_20240611_models.CreateAccessWarrantRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.CreateAccessWarrantResponse:
        """
        @summary 阿里云控制台/授权凭证创建
        
        @param request: CreateAccessWarrantRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessWarrantResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['appId'] = request.app_id
        if not UtilClient.is_unset(request.request_sign):
            body['requestSign'] = request.request_sign
        if not UtilClient.is_unset(request.timestamp):
            body['timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.user_client_ip):
            body['userClientIp'] = request.user_client_ip
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.warrant_available):
            body['warrantAvailable'] = request.warrant_available
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAccessWarrant',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/createAccessWarrant',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.CreateAccessWarrantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_warrant(
        self,
        request: ai_content_20240611_models.CreateAccessWarrantRequest,
    ) -> ai_content_20240611_models.CreateAccessWarrantResponse:
        """
        @summary 阿里云控制台/授权凭证创建
        
        @param request: CreateAccessWarrantRequest
        @return: CreateAccessWarrantResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_access_warrant_with_options(request, headers, runtime)

    async def create_access_warrant_async(
        self,
        request: ai_content_20240611_models.CreateAccessWarrantRequest,
    ) -> ai_content_20240611_models.CreateAccessWarrantResponse:
        """
        @summary 阿里云控制台/授权凭证创建
        
        @param request: CreateAccessWarrantRequest
        @return: CreateAccessWarrantResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_access_warrant_with_options_async(request, headers, runtime)

    def create_project_with_options(
        self,
        request: ai_content_20240611_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.CreateProjectResponse:
        """
        @summary 阿里云控制台/创建项目
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.project_type):
            body['projectType'] = request.project_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/createProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: ai_content_20240611_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.CreateProjectResponse:
        """
        @summary 阿里云控制台/创建项目
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        if not UtilClient.is_unset(request.project_type):
            body['projectType'] = request.project_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/createProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: ai_content_20240611_models.CreateProjectRequest,
    ) -> ai_content_20240611_models.CreateProjectResponse:
        """
        @summary 阿里云控制台/创建项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: ai_content_20240611_models.CreateProjectRequest,
    ) -> ai_content_20240611_models.CreateProjectResponse:
        """
        @summary 阿里云控制台/创建项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def execute_aiteacher_chinese_composition_tutoring_workflow_run_with_options(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse:
        """
        @summary 中文作文辅导
        
        @param request: ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.essay_outline):
            body['essayOutline'] = request.essay_outline
        if not UtilClient.is_unset(request.essay_requirements):
            body['essayRequirements'] = request.essay_requirements
        if not UtilClient.is_unset(request.essay_topic):
            body['essayTopic'] = request.essay_topic
        if not UtilClient.is_unset(request.essay_type):
            body['essayType'] = request.essay_type
        if not UtilClient.is_unset(request.essay_word_count):
            body['essayWordCount'] = request.essay_word_count
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.response_mode):
            body['responseMode'] = request.response_mode
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherChineseCompositionTutoringWorkflowRun',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/pop/api/v1/intelligentAgent/chineseCompositionTutoring/workflowRun',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_chinese_composition_tutoring_workflow_run_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse:
        """
        @summary 中文作文辅导
        
        @param request: ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.essay_outline):
            body['essayOutline'] = request.essay_outline
        if not UtilClient.is_unset(request.essay_requirements):
            body['essayRequirements'] = request.essay_requirements
        if not UtilClient.is_unset(request.essay_topic):
            body['essayTopic'] = request.essay_topic
        if not UtilClient.is_unset(request.essay_type):
            body['essayType'] = request.essay_type
        if not UtilClient.is_unset(request.essay_word_count):
            body['essayWordCount'] = request.essay_word_count
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.response_mode):
            body['responseMode'] = request.response_mode
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherChineseCompositionTutoringWorkflowRun',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/pop/api/v1/intelligentAgent/chineseCompositionTutoring/workflowRun',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_chinese_composition_tutoring_workflow_run(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse:
        """
        @summary 中文作文辅导
        
        @param request: ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest
        @return: ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_chinese_composition_tutoring_workflow_run_with_options(request, headers, runtime)

    async def execute_aiteacher_chinese_composition_tutoring_workflow_run_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse:
        """
        @summary 中文作文辅导
        
        @param request: ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest
        @return: ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_chinese_composition_tutoring_workflow_run_with_options_async(request, headers, runtime)

    def execute_aiteacher_english_composition_tutoring_workflow_run_with_options(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse:
        """
        @summary 英语作文辅导
        
        @param request: ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.essay_outline):
            body['essayOutline'] = request.essay_outline
        if not UtilClient.is_unset(request.essay_requirements):
            body['essayRequirements'] = request.essay_requirements
        if not UtilClient.is_unset(request.essay_topic):
            body['essayTopic'] = request.essay_topic
        if not UtilClient.is_unset(request.essay_type):
            body['essayType'] = request.essay_type
        if not UtilClient.is_unset(request.essay_word_count):
            body['essayWordCount'] = request.essay_word_count
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.response_mode):
            body['responseMode'] = request.response_mode
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherEnglishCompositionTutoringWorkflowRun',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/pop/api/v1/intelligentAgent/englishCompositionTutoring/workflowRun',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_english_composition_tutoring_workflow_run_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse:
        """
        @summary 英语作文辅导
        
        @param request: ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.essay_outline):
            body['essayOutline'] = request.essay_outline
        if not UtilClient.is_unset(request.essay_requirements):
            body['essayRequirements'] = request.essay_requirements
        if not UtilClient.is_unset(request.essay_topic):
            body['essayTopic'] = request.essay_topic
        if not UtilClient.is_unset(request.essay_type):
            body['essayType'] = request.essay_type
        if not UtilClient.is_unset(request.essay_word_count):
            body['essayWordCount'] = request.essay_word_count
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.response_mode):
            body['responseMode'] = request.response_mode
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherEnglishCompositionTutoringWorkflowRun',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/pop/api/v1/intelligentAgent/englishCompositionTutoring/workflowRun',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_english_composition_tutoring_workflow_run(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse:
        """
        @summary 英语作文辅导
        
        @param request: ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest
        @return: ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_english_composition_tutoring_workflow_run_with_options(request, headers, runtime)

    async def execute_aiteacher_english_composition_tutoring_workflow_run_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse:
        """
        @summary 英语作文辅导
        
        @param request: ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest
        @return: ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_english_composition_tutoring_workflow_run_with_options_async(request, headers, runtime)

    def execute_aiteacher_english_paraphrase_chat_message_with_options(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherEnglishParaphraseChatMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse:
        """
        @summary 英文释义
        
        @param request: ExecuteAITeacherEnglishParaphraseChatMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherEnglishParaphraseChatMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.question_id):
            body['questionId'] = request.question_id
        if not UtilClient.is_unset(request.question_info):
            body['questionInfo'] = request.question_info
        if not UtilClient.is_unset(request.response_mode):
            body['responseMode'] = request.response_mode
        if not UtilClient.is_unset(request.user_answer):
            body['userAnswer'] = request.user_answer
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherEnglishParaphraseChatMessage',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/pop/api/v1/intelligentAgent/englishParaphrase/chatMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_english_paraphrase_chat_message_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherEnglishParaphraseChatMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse:
        """
        @summary 英文释义
        
        @param request: ExecuteAITeacherEnglishParaphraseChatMessageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteAITeacherEnglishParaphraseChatMessageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.grade):
            body['grade'] = request.grade
        if not UtilClient.is_unset(request.question_id):
            body['questionId'] = request.question_id
        if not UtilClient.is_unset(request.question_info):
            body['questionInfo'] = request.question_info
        if not UtilClient.is_unset(request.response_mode):
            body['responseMode'] = request.response_mode
        if not UtilClient.is_unset(request.user_answer):
            body['userAnswer'] = request.user_answer
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteAITeacherEnglishParaphraseChatMessage',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/pop/api/v1/intelligentAgent/englishParaphrase/chatMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_english_paraphrase_chat_message(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherEnglishParaphraseChatMessageRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse:
        """
        @summary 英文释义
        
        @param request: ExecuteAITeacherEnglishParaphraseChatMessageRequest
        @return: ExecuteAITeacherEnglishParaphraseChatMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_english_paraphrase_chat_message_with_options(request, headers, runtime)

    async def execute_aiteacher_english_paraphrase_chat_message_async(
        self,
        request: ai_content_20240611_models.ExecuteAITeacherEnglishParaphraseChatMessageRequest,
    ) -> ai_content_20240611_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse:
        """
        @summary 英文释义
        
        @param request: ExecuteAITeacherEnglishParaphraseChatMessageRequest
        @return: ExecuteAITeacherEnglishParaphraseChatMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_english_paraphrase_chat_message_with_options_async(request, headers, runtime)

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

    def execute_hundred_thousand_whys_dialogue_with_options(
        self,
        request: ai_content_20240611_models.ExecuteHundredThousandWhysDialogueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteHundredThousandWhysDialogueResponse:
        """
        @summary 十万个为什么对话接入
        
        @param request: ExecuteHundredThousandWhysDialogueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteHundredThousandWhysDialogueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.age_group):
            body['ageGroup'] = request.age_group
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.device_id):
            body['deviceId'] = request.device_id
        if not UtilClient.is_unset(request.mac_address):
            body['macAddress'] = request.mac_address
        if not UtilClient.is_unset(request.messages):
            body['messages'] = request.messages
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteHundredThousandWhysDialogue',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/pop/api/v1/intelligentAgent/tenWWhys/executeDialogue',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteHundredThousandWhysDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_hundred_thousand_whys_dialogue_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteHundredThousandWhysDialogueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteHundredThousandWhysDialogueResponse:
        """
        @summary 十万个为什么对话接入
        
        @param request: ExecuteHundredThousandWhysDialogueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteHundredThousandWhysDialogueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.age_group):
            body['ageGroup'] = request.age_group
        if not UtilClient.is_unset(request.chat_id):
            body['chatId'] = request.chat_id
        if not UtilClient.is_unset(request.device_id):
            body['deviceId'] = request.device_id
        if not UtilClient.is_unset(request.mac_address):
            body['macAddress'] = request.mac_address
        if not UtilClient.is_unset(request.messages):
            body['messages'] = request.messages
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteHundredThousandWhysDialogue',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/pop/api/v1/intelligentAgent/tenWWhys/executeDialogue',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteHundredThousandWhysDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_hundred_thousand_whys_dialogue(
        self,
        request: ai_content_20240611_models.ExecuteHundredThousandWhysDialogueRequest,
    ) -> ai_content_20240611_models.ExecuteHundredThousandWhysDialogueResponse:
        """
        @summary 十万个为什么对话接入
        
        @param request: ExecuteHundredThousandWhysDialogueRequest
        @return: ExecuteHundredThousandWhysDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_hundred_thousand_whys_dialogue_with_options(request, headers, runtime)

    async def execute_hundred_thousand_whys_dialogue_async(
        self,
        request: ai_content_20240611_models.ExecuteHundredThousandWhysDialogueRequest,
    ) -> ai_content_20240611_models.ExecuteHundredThousandWhysDialogueResponse:
        """
        @summary 十万个为什么对话接入
        
        @param request: ExecuteHundredThousandWhysDialogueRequest
        @return: ExecuteHundredThousandWhysDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_hundred_thousand_whys_dialogue_with_options_async(request, headers, runtime)

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

    def execute_textbook_assistant_sse_dialogue_with_options(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantSseDialogueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantSseDialogueResponse:
        """
        @summary 进行对话-流式输出
        
        @param request: ExecuteTextbookAssistantSseDialogueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantSseDialogueResponse
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
            action='ExecuteTextbookAssistantSseDialogue',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/ExecuteSseDialogue',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantSseDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_sse_dialogue_with_options_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantSseDialogueRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantSseDialogueResponse:
        """
        @summary 进行对话-流式输出
        
        @param request: ExecuteTextbookAssistantSseDialogueRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTextbookAssistantSseDialogueResponse
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
            action='ExecuteTextbookAssistantSseDialogue',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/dialogue/ExecuteSseDialogue',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ExecuteTextbookAssistantSseDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_sse_dialogue(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantSseDialogueRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantSseDialogueResponse:
        """
        @summary 进行对话-流式输出
        
        @param request: ExecuteTextbookAssistantSseDialogueRequest
        @return: ExecuteTextbookAssistantSseDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_sse_dialogue_with_options(request, headers, runtime)

    async def execute_textbook_assistant_sse_dialogue_async(
        self,
        request: ai_content_20240611_models.ExecuteTextbookAssistantSseDialogueRequest,
    ) -> ai_content_20240611_models.ExecuteTextbookAssistantSseDialogueResponse:
        """
        @summary 进行对话-流式输出
        
        @param request: ExecuteTextbookAssistantSseDialogueRequest
        @return: ExecuteTextbookAssistantSseDialogueResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_sse_dialogue_with_options_async(request, headers, runtime)

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

    def list_textbook_assistant_article_details_with_options(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantArticleDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ListTextbookAssistantArticleDetailsResponse:
        """
        @summary 批量获取文章详情
        
        @param request: ListTextbookAssistantArticleDetailsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextbookAssistantArticleDetailsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.article_id_list):
            body['articleIdList'] = request.article_id_list
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTextbookAssistantArticleDetails',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/ListArticleDetails',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ListTextbookAssistantArticleDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_textbook_assistant_article_details_with_options_async(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantArticleDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ListTextbookAssistantArticleDetailsResponse:
        """
        @summary 批量获取文章详情
        
        @param request: ListTextbookAssistantArticleDetailsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextbookAssistantArticleDetailsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.article_id_list):
            body['articleIdList'] = request.article_id_list
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTextbookAssistantArticleDetails',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/ListArticleDetails',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ListTextbookAssistantArticleDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_textbook_assistant_article_details(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantArticleDetailsRequest,
    ) -> ai_content_20240611_models.ListTextbookAssistantArticleDetailsResponse:
        """
        @summary 批量获取文章详情
        
        @param request: ListTextbookAssistantArticleDetailsRequest
        @return: ListTextbookAssistantArticleDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_textbook_assistant_article_details_with_options(request, headers, runtime)

    async def list_textbook_assistant_article_details_async(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantArticleDetailsRequest,
    ) -> ai_content_20240611_models.ListTextbookAssistantArticleDetailsResponse:
        """
        @summary 批量获取文章详情
        
        @param request: ListTextbookAssistantArticleDetailsRequest
        @return: ListTextbookAssistantArticleDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_textbook_assistant_article_details_with_options_async(request, headers, runtime)

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

    def list_textbook_assistant_scene_details_with_options(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantSceneDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ListTextbookAssistantSceneDetailsResponse:
        """
        @summary 获取文章内容详情
        
        @param request: ListTextbookAssistantSceneDetailsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextbookAssistantSceneDetailsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.scene_id_list):
            body['sceneIdList'] = request.scene_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTextbookAssistantSceneDetails',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/ListSceneDetails',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ListTextbookAssistantSceneDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_textbook_assistant_scene_details_with_options_async(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantSceneDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.ListTextbookAssistantSceneDetailsResponse:
        """
        @summary 获取文章内容详情
        
        @param request: ListTextbookAssistantSceneDetailsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTextbookAssistantSceneDetailsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auth_token):
            body['authToken'] = request.auth_token
        if not UtilClient.is_unset(request.scene_id_list):
            body['sceneIdList'] = request.scene_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTextbookAssistantSceneDetails',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/textbookAssistant/teachingResource/ListSceneDetails',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.ListTextbookAssistantSceneDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_textbook_assistant_scene_details(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantSceneDetailsRequest,
    ) -> ai_content_20240611_models.ListTextbookAssistantSceneDetailsResponse:
        """
        @summary 获取文章内容详情
        
        @param request: ListTextbookAssistantSceneDetailsRequest
        @return: ListTextbookAssistantSceneDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_textbook_assistant_scene_details_with_options(request, headers, runtime)

    async def list_textbook_assistant_scene_details_async(
        self,
        request: ai_content_20240611_models.ListTextbookAssistantSceneDetailsRequest,
    ) -> ai_content_20240611_models.ListTextbookAssistantSceneDetailsResponse:
        """
        @summary 获取文章内容详情
        
        @param request: ListTextbookAssistantSceneDetailsRequest
        @return: ListTextbookAssistantSceneDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_textbook_assistant_scene_details_with_options_async(request, headers, runtime)

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

    def query_application_access_id_with_options(
        self,
        request: ai_content_20240611_models.QueryApplicationAccessIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.QueryApplicationAccessIdResponse:
        """
        @summary 阿里云控制台/获取应用访问识别码(appkey)信息
        
        @param request: QueryApplicationAccessIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryApplicationAccessIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_access_id):
            query['applicationAccessId'] = request.application_access_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryApplicationAccessId',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/queryApplicationAccessId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.QueryApplicationAccessIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_application_access_id_with_options_async(
        self,
        request: ai_content_20240611_models.QueryApplicationAccessIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.QueryApplicationAccessIdResponse:
        """
        @summary 阿里云控制台/获取应用访问识别码(appkey)信息
        
        @param request: QueryApplicationAccessIdRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryApplicationAccessIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_access_id):
            query['applicationAccessId'] = request.application_access_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryApplicationAccessId',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/queryApplicationAccessId',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.QueryApplicationAccessIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_application_access_id(
        self,
        request: ai_content_20240611_models.QueryApplicationAccessIdRequest,
    ) -> ai_content_20240611_models.QueryApplicationAccessIdResponse:
        """
        @summary 阿里云控制台/获取应用访问识别码(appkey)信息
        
        @param request: QueryApplicationAccessIdRequest
        @return: QueryApplicationAccessIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_application_access_id_with_options(request, headers, runtime)

    async def query_application_access_id_async(
        self,
        request: ai_content_20240611_models.QueryApplicationAccessIdRequest,
    ) -> ai_content_20240611_models.QueryApplicationAccessIdResponse:
        """
        @summary 阿里云控制台/获取应用访问识别码(appkey)信息
        
        @param request: QueryApplicationAccessIdRequest
        @return: QueryApplicationAccessIdResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_application_access_id_with_options_async(request, headers, runtime)

    def query_project_with_options(
        self,
        request: ai_content_20240611_models.QueryProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.QueryProjectResponse:
        """
        @summary 阿里云控制台/获取项目列表
        
        @param request: QueryProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryProjectResponse
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
            action='QueryProject',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/queryProject',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.QueryProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_project_with_options_async(
        self,
        request: ai_content_20240611_models.QueryProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.QueryProjectResponse:
        """
        @summary 阿里云控制台/获取项目列表
        
        @param request: QueryProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryProjectResponse
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
            action='QueryProject',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/queryProject',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.QueryProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_project(
        self,
        request: ai_content_20240611_models.QueryProjectRequest,
    ) -> ai_content_20240611_models.QueryProjectResponse:
        """
        @summary 阿里云控制台/获取项目列表
        
        @param request: QueryProjectRequest
        @return: QueryProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_project_with_options(request, headers, runtime)

    async def query_project_async(
        self,
        request: ai_content_20240611_models.QueryProjectRequest,
    ) -> ai_content_20240611_models.QueryProjectResponse:
        """
        @summary 阿里云控制台/获取项目列表
        
        @param request: QueryProjectRequest
        @return: QueryProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_project_with_options_async(request, headers, runtime)

    def query_project_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.QueryProjectListResponse:
        """
        @summary 阿里云控制台/获取项目列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryProjectListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QueryProjectList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/queryProjectList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.QueryProjectListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_project_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.QueryProjectListResponse:
        """
        @summary 阿里云控制台/获取项目列表
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryProjectListResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QueryProjectList',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/queryProjectList',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.QueryProjectListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_project_list(self) -> ai_content_20240611_models.QueryProjectListResponse:
        """
        @summary 阿里云控制台/获取项目列表
        
        @return: QueryProjectListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_project_list_with_options(headers, runtime)

    async def query_project_list_async(self) -> ai_content_20240611_models.QueryProjectListResponse:
        """
        @summary 阿里云控制台/获取项目列表
        
        @return: QueryProjectListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_project_list_with_options_async(headers, runtime)

    def query_purchased_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.QueryPurchasedServiceResponse:
        """
        @summary 阿里云控制台/已经购买过的服务项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPurchasedServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QueryPurchasedService',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/queryPurchasedService',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.QueryPurchasedServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_purchased_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.QueryPurchasedServiceResponse:
        """
        @summary 阿里云控制台/已经购买过的服务项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPurchasedServiceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='QueryPurchasedService',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/queryPurchasedService',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.QueryPurchasedServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_purchased_service(self) -> ai_content_20240611_models.QueryPurchasedServiceResponse:
        """
        @summary 阿里云控制台/已经购买过的服务项目
        
        @return: QueryPurchasedServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_purchased_service_with_options(headers, runtime)

    async def query_purchased_service_async(self) -> ai_content_20240611_models.QueryPurchasedServiceResponse:
        """
        @summary 阿里云控制台/已经购买过的服务项目
        
        @return: QueryPurchasedServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_purchased_service_with_options_async(headers, runtime)

    def update_project_with_options(
        self,
        request: ai_content_20240611_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.UpdateProjectResponse:
        """
        @summary 阿里云控制台/更新项目信息
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/updateProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        request: ai_content_20240611_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ai_content_20240611_models.UpdateProjectResponse:
        """
        @summary 阿里云控制台/更新项目信息
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.project_name):
            body['projectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='20240611',
            protocol='HTTPS',
            pathname=f'/api/v1/aliyunConsole/updateProject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ai_content_20240611_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        request: ai_content_20240611_models.UpdateProjectRequest,
    ) -> ai_content_20240611_models.UpdateProjectResponse:
        """
        @summary 阿里云控制台/更新项目信息
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(request, headers, runtime)

    async def update_project_async(
        self,
        request: ai_content_20240611_models.UpdateProjectRequest,
    ) -> ai_content_20240611_models.UpdateProjectResponse:
        """
        @summary 阿里云控制台/更新项目信息
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_with_options_async(request, headers, runtime)
