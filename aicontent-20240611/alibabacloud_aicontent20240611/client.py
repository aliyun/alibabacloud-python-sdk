# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_aicontent20240611 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def a_iteacher_expansion_practice_task_generate_with_options(
        self,
        request: main_models.AITeacherExpansionPracticeTaskGenerateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AITeacherExpansionPracticeTaskGenerateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.key_sentences):
            body['keySentences'] = request.key_sentences
        if not DaraCore.is_null(request.key_words):
            body['keyWords'] = request.key_words
        if not DaraCore.is_null(request.learning_object):
            body['learningObject'] = request.learning_object
        if not DaraCore.is_null(request.text_content):
            body['textContent'] = request.text_content
        if not DaraCore.is_null(request.textbook):
            body['textbook'] = request.textbook
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AITeacherExpansionPracticeTaskGenerate',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/expansionPractice/generateTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AITeacherExpansionPracticeTaskGenerateResponse(),
            self.call_api(params, req, runtime)
        )

    async def a_iteacher_expansion_practice_task_generate_with_options_async(
        self,
        request: main_models.AITeacherExpansionPracticeTaskGenerateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AITeacherExpansionPracticeTaskGenerateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.key_sentences):
            body['keySentences'] = request.key_sentences
        if not DaraCore.is_null(request.key_words):
            body['keyWords'] = request.key_words
        if not DaraCore.is_null(request.learning_object):
            body['learningObject'] = request.learning_object
        if not DaraCore.is_null(request.text_content):
            body['textContent'] = request.text_content
        if not DaraCore.is_null(request.textbook):
            body['textbook'] = request.textbook
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AITeacherExpansionPracticeTaskGenerate',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/expansionPractice/generateTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AITeacherExpansionPracticeTaskGenerateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def a_iteacher_expansion_practice_task_generate(
        self,
        request: main_models.AITeacherExpansionPracticeTaskGenerateRequest,
    ) -> main_models.AITeacherExpansionPracticeTaskGenerateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.a_iteacher_expansion_practice_task_generate_with_options(request, headers, runtime)

    async def a_iteacher_expansion_practice_task_generate_async(
        self,
        request: main_models.AITeacherExpansionPracticeTaskGenerateRequest,
    ) -> main_models.AITeacherExpansionPracticeTaskGenerateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.a_iteacher_expansion_practice_task_generate_with_options_async(request, headers, runtime)

    def a_iteacher_sync_practice_task_generate_with_options(
        self,
        request: main_models.AITeacherSyncPracticeTaskGenerateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AITeacherSyncPracticeTaskGenerateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.key_sentences):
            body['keySentences'] = request.key_sentences
        if not DaraCore.is_null(request.key_words):
            body['keyWords'] = request.key_words
        if not DaraCore.is_null(request.learning_object):
            body['learningObject'] = request.learning_object
        if not DaraCore.is_null(request.text_content):
            body['textContent'] = request.text_content
        if not DaraCore.is_null(request.textbook):
            body['textbook'] = request.textbook
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AITeacherSyncPracticeTaskGenerate',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/syncPractice/generateTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AITeacherSyncPracticeTaskGenerateResponse(),
            self.call_api(params, req, runtime)
        )

    async def a_iteacher_sync_practice_task_generate_with_options_async(
        self,
        request: main_models.AITeacherSyncPracticeTaskGenerateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AITeacherSyncPracticeTaskGenerateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.key_sentences):
            body['keySentences'] = request.key_sentences
        if not DaraCore.is_null(request.key_words):
            body['keyWords'] = request.key_words
        if not DaraCore.is_null(request.learning_object):
            body['learningObject'] = request.learning_object
        if not DaraCore.is_null(request.text_content):
            body['textContent'] = request.text_content
        if not DaraCore.is_null(request.textbook):
            body['textbook'] = request.textbook
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AITeacherSyncPracticeTaskGenerate',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/syncPractice/generateTask',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AITeacherSyncPracticeTaskGenerateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def a_iteacher_sync_practice_task_generate(
        self,
        request: main_models.AITeacherSyncPracticeTaskGenerateRequest,
    ) -> main_models.AITeacherSyncPracticeTaskGenerateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.a_iteacher_sync_practice_task_generate_with_options(request, headers, runtime)

    async def a_iteacher_sync_practice_task_generate_async(
        self,
        request: main_models.AITeacherSyncPracticeTaskGenerateRequest,
    ) -> main_models.AITeacherSyncPracticeTaskGenerateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.a_iteacher_sync_practice_task_generate_with_options_async(request, headers, runtime)

    def aliyun_console_open_api_query_aliyun_console_servcie_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'AliyunConsoleOpenApiQueryAliyunConsoleServcieList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunconsole/queryAliyunConsoleServcieList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse(),
            self.call_api(params, req, runtime)
        )

    async def aliyun_console_open_api_query_aliyun_console_servcie_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'AliyunConsoleOpenApiQueryAliyunConsoleServcieList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunconsole/queryAliyunConsoleServcieList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aliyun_console_open_api_query_aliyun_console_servcie_list(self) -> main_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.aliyun_console_open_api_query_aliyun_console_servcie_list_with_options(headers, runtime)

    async def aliyun_console_open_api_query_aliyun_console_servcie_list_async(self) -> main_models.AliyunConsoleOpenApiQueryAliyunConsoleServcieListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.aliyun_console_open_api_query_aliyun_console_servcie_list_with_options_async(headers, runtime)

    def aliyun_console_open_api_query_aliyun_console_service_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'AliyunConsoleOpenApiQueryAliyunConsoleServiceList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/queryAliyunConsoleServiceList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def aliyun_console_open_api_query_aliyun_console_service_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'AliyunConsoleOpenApiQueryAliyunConsoleServiceList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/queryAliyunConsoleServiceList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aliyun_console_open_api_query_aliyun_console_service_list(self) -> main_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.aliyun_console_open_api_query_aliyun_console_service_list_with_options(headers, runtime)

    async def aliyun_console_open_api_query_aliyun_console_service_list_async(self) -> main_models.AliyunConsoleOpenApiQueryAliyunConsoleServiceListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.aliyun_console_open_api_query_aliyun_console_service_list_with_options_async(headers, runtime)

    def aliyun_console_open_api_query_paid_resource_with_options(
        self,
        request: main_models.AliyunConsoleOpenApiQueryPaidResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AliyunConsoleOpenApiQueryPaidResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AliyunConsoleOpenApiQueryPaidResource',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/queryPaidResource',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AliyunConsoleOpenApiQueryPaidResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def aliyun_console_open_api_query_paid_resource_with_options_async(
        self,
        request: main_models.AliyunConsoleOpenApiQueryPaidResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AliyunConsoleOpenApiQueryPaidResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AliyunConsoleOpenApiQueryPaidResource',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/queryPaidResource',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AliyunConsoleOpenApiQueryPaidResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def aliyun_console_open_api_query_paid_resource(
        self,
        request: main_models.AliyunConsoleOpenApiQueryPaidResourceRequest,
    ) -> main_models.AliyunConsoleOpenApiQueryPaidResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.aliyun_console_open_api_query_paid_resource_with_options(request, headers, runtime)

    async def aliyun_console_open_api_query_paid_resource_async(
        self,
        request: main_models.AliyunConsoleOpenApiQueryPaidResourceRequest,
    ) -> main_models.AliyunConsoleOpenApiQueryPaidResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.aliyun_console_open_api_query_paid_resource_with_options_async(request, headers, runtime)

    def count_oral_evaluation_statistics_calls_with_options(
        self,
        request: main_models.CountOralEvaluationStatisticsCallsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CountOralEvaluationStatisticsCallsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CountOralEvaluationStatisticsCalls',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/countOralEvaluationStatisticsCalls',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CountOralEvaluationStatisticsCallsResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_oral_evaluation_statistics_calls_with_options_async(
        self,
        request: main_models.CountOralEvaluationStatisticsCallsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CountOralEvaluationStatisticsCallsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CountOralEvaluationStatisticsCalls',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/countOralEvaluationStatisticsCalls',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CountOralEvaluationStatisticsCallsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_oral_evaluation_statistics_calls(
        self,
        request: main_models.CountOralEvaluationStatisticsCallsRequest,
    ) -> main_models.CountOralEvaluationStatisticsCallsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.count_oral_evaluation_statistics_calls_with_options(request, headers, runtime)

    async def count_oral_evaluation_statistics_calls_async(
        self,
        request: main_models.CountOralEvaluationStatisticsCallsRequest,
    ) -> main_models.CountOralEvaluationStatisticsCallsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.count_oral_evaluation_statistics_calls_with_options_async(request, headers, runtime)

    def count_oral_evaluation_statistics_concurrent_with_options(
        self,
        request: main_models.CountOralEvaluationStatisticsConcurrentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CountOralEvaluationStatisticsConcurrentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CountOralEvaluationStatisticsConcurrent',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/countOralEvaluationStatisticsConcurrent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CountOralEvaluationStatisticsConcurrentResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_oral_evaluation_statistics_concurrent_with_options_async(
        self,
        request: main_models.CountOralEvaluationStatisticsConcurrentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CountOralEvaluationStatisticsConcurrentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CountOralEvaluationStatisticsConcurrent',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/countOralEvaluationStatisticsConcurrent',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CountOralEvaluationStatisticsConcurrentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_oral_evaluation_statistics_concurrent(
        self,
        request: main_models.CountOralEvaluationStatisticsConcurrentRequest,
    ) -> main_models.CountOralEvaluationStatisticsConcurrentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.count_oral_evaluation_statistics_concurrent_with_options(request, headers, runtime)

    async def count_oral_evaluation_statistics_concurrent_async(
        self,
        request: main_models.CountOralEvaluationStatisticsConcurrentRequest,
    ) -> main_models.CountOralEvaluationStatisticsConcurrentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.count_oral_evaluation_statistics_concurrent_with_options_async(request, headers, runtime)

    def count_oral_evaluation_statistics_error_with_options(
        self,
        request: main_models.CountOralEvaluationStatisticsErrorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CountOralEvaluationStatisticsErrorResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CountOralEvaluationStatisticsError',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/countOralEvaluationStatisticsError',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CountOralEvaluationStatisticsErrorResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_oral_evaluation_statistics_error_with_options_async(
        self,
        request: main_models.CountOralEvaluationStatisticsErrorRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CountOralEvaluationStatisticsErrorResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CountOralEvaluationStatisticsError',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/countOralEvaluationStatisticsError',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CountOralEvaluationStatisticsErrorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_oral_evaluation_statistics_error(
        self,
        request: main_models.CountOralEvaluationStatisticsErrorRequest,
    ) -> main_models.CountOralEvaluationStatisticsErrorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.count_oral_evaluation_statistics_error_with_options(request, headers, runtime)

    async def count_oral_evaluation_statistics_error_async(
        self,
        request: main_models.CountOralEvaluationStatisticsErrorRequest,
    ) -> main_models.CountOralEvaluationStatisticsErrorResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.count_oral_evaluation_statistics_error_with_options_async(request, headers, runtime)

    def create_access_warrant_with_options(
        self,
        request: main_models.CreateAccessWarrantRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessWarrantResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.request_sign):
            body['requestSign'] = request.request_sign
        if not DaraCore.is_null(request.timestamp):
            body['timestamp'] = request.timestamp
        if not DaraCore.is_null(request.user_client_ip):
            body['userClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        if not DaraCore.is_null(request.warrant_available):
            body['warrantAvailable'] = request.warrant_available
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessWarrant',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/createAccessWarrant',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessWarrantResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_warrant_with_options_async(
        self,
        request: main_models.CreateAccessWarrantRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessWarrantResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.request_sign):
            body['requestSign'] = request.request_sign
        if not DaraCore.is_null(request.timestamp):
            body['timestamp'] = request.timestamp
        if not DaraCore.is_null(request.user_client_ip):
            body['userClientIp'] = request.user_client_ip
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        if not DaraCore.is_null(request.warrant_available):
            body['warrantAvailable'] = request.warrant_available
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessWarrant',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/createAccessWarrant',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessWarrantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_warrant(
        self,
        request: main_models.CreateAccessWarrantRequest,
    ) -> main_models.CreateAccessWarrantResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_access_warrant_with_options(request, headers, runtime)

    async def create_access_warrant_async(
        self,
        request: main_models.CreateAccessWarrantRequest,
    ) -> main_models.CreateAccessWarrantResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_access_warrant_with_options_async(request, headers, runtime)

    def create_project_with_options(
        self,
        request: main_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_name):
            body['projectName'] = request.project_name
        if not DaraCore.is_null(request.project_type):
            body['projectType'] = request.project_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/createProject',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: main_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_name):
            body['projectName'] = request.project_name
        if not DaraCore.is_null(request.project_type):
            body['projectType'] = request.project_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/createProject',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def execute_aiteacher_chinese_composition_tutoring_workflow_run_with_sse(
        self,
        request: main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.essay_outline):
            body['essayOutline'] = request.essay_outline
        if not DaraCore.is_null(request.essay_requirements):
            body['essayRequirements'] = request.essay_requirements
        if not DaraCore.is_null(request.essay_topic):
            body['essayTopic'] = request.essay_topic
        if not DaraCore.is_null(request.essay_type):
            body['essayType'] = request.essay_type
        if not DaraCore.is_null(request.essay_word_count):
            body['essayWordCount'] = request.essay_word_count
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.response_mode):
            body['responseMode'] = request.response_mode
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherChineseCompositionTutoringWorkflowRun',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/intelligentAgent/chineseCompositionTutoring/workflowRun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def execute_aiteacher_chinese_composition_tutoring_workflow_run_with_sse_async(
        self,
        request: main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.essay_outline):
            body['essayOutline'] = request.essay_outline
        if not DaraCore.is_null(request.essay_requirements):
            body['essayRequirements'] = request.essay_requirements
        if not DaraCore.is_null(request.essay_topic):
            body['essayTopic'] = request.essay_topic
        if not DaraCore.is_null(request.essay_type):
            body['essayType'] = request.essay_type
        if not DaraCore.is_null(request.essay_word_count):
            body['essayWordCount'] = request.essay_word_count
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.response_mode):
            body['responseMode'] = request.response_mode
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherChineseCompositionTutoringWorkflowRun',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/intelligentAgent/chineseCompositionTutoring/workflowRun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def execute_aiteacher_chinese_composition_tutoring_workflow_run_with_options(
        self,
        request: main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.essay_outline):
            body['essayOutline'] = request.essay_outline
        if not DaraCore.is_null(request.essay_requirements):
            body['essayRequirements'] = request.essay_requirements
        if not DaraCore.is_null(request.essay_topic):
            body['essayTopic'] = request.essay_topic
        if not DaraCore.is_null(request.essay_type):
            body['essayType'] = request.essay_type
        if not DaraCore.is_null(request.essay_word_count):
            body['essayWordCount'] = request.essay_word_count
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.response_mode):
            body['responseMode'] = request.response_mode
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherChineseCompositionTutoringWorkflowRun',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/intelligentAgent/chineseCompositionTutoring/workflowRun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_chinese_composition_tutoring_workflow_run_with_options_async(
        self,
        request: main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.essay_outline):
            body['essayOutline'] = request.essay_outline
        if not DaraCore.is_null(request.essay_requirements):
            body['essayRequirements'] = request.essay_requirements
        if not DaraCore.is_null(request.essay_topic):
            body['essayTopic'] = request.essay_topic
        if not DaraCore.is_null(request.essay_type):
            body['essayType'] = request.essay_type
        if not DaraCore.is_null(request.essay_word_count):
            body['essayWordCount'] = request.essay_word_count
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.response_mode):
            body['responseMode'] = request.response_mode
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherChineseCompositionTutoringWorkflowRun',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/intelligentAgent/chineseCompositionTutoring/workflowRun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_chinese_composition_tutoring_workflow_run(
        self,
        request: main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest,
    ) -> main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_chinese_composition_tutoring_workflow_run_with_options(request, headers, runtime)

    async def execute_aiteacher_chinese_composition_tutoring_workflow_run_async(
        self,
        request: main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunRequest,
    ) -> main_models.ExecuteAITeacherChineseCompositionTutoringWorkflowRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_chinese_composition_tutoring_workflow_run_with_options_async(request, headers, runtime)

    def execute_aiteacher_english_composition_tutoring_workflow_run_with_sse(
        self,
        request: main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.essay_outline):
            body['essayOutline'] = request.essay_outline
        if not DaraCore.is_null(request.essay_requirements):
            body['essayRequirements'] = request.essay_requirements
        if not DaraCore.is_null(request.essay_topic):
            body['essayTopic'] = request.essay_topic
        if not DaraCore.is_null(request.essay_type):
            body['essayType'] = request.essay_type
        if not DaraCore.is_null(request.essay_word_count):
            body['essayWordCount'] = request.essay_word_count
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.response_mode):
            body['responseMode'] = request.response_mode
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherEnglishCompositionTutoringWorkflowRun',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/intelligentAgent/englishCompositionTutoring/workflowRun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def execute_aiteacher_english_composition_tutoring_workflow_run_with_sse_async(
        self,
        request: main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.essay_outline):
            body['essayOutline'] = request.essay_outline
        if not DaraCore.is_null(request.essay_requirements):
            body['essayRequirements'] = request.essay_requirements
        if not DaraCore.is_null(request.essay_topic):
            body['essayTopic'] = request.essay_topic
        if not DaraCore.is_null(request.essay_type):
            body['essayType'] = request.essay_type
        if not DaraCore.is_null(request.essay_word_count):
            body['essayWordCount'] = request.essay_word_count
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.response_mode):
            body['responseMode'] = request.response_mode
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherEnglishCompositionTutoringWorkflowRun',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/intelligentAgent/englishCompositionTutoring/workflowRun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def execute_aiteacher_english_composition_tutoring_workflow_run_with_options(
        self,
        request: main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.essay_outline):
            body['essayOutline'] = request.essay_outline
        if not DaraCore.is_null(request.essay_requirements):
            body['essayRequirements'] = request.essay_requirements
        if not DaraCore.is_null(request.essay_topic):
            body['essayTopic'] = request.essay_topic
        if not DaraCore.is_null(request.essay_type):
            body['essayType'] = request.essay_type
        if not DaraCore.is_null(request.essay_word_count):
            body['essayWordCount'] = request.essay_word_count
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.response_mode):
            body['responseMode'] = request.response_mode
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherEnglishCompositionTutoringWorkflowRun',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/intelligentAgent/englishCompositionTutoring/workflowRun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_english_composition_tutoring_workflow_run_with_options_async(
        self,
        request: main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.essay_outline):
            body['essayOutline'] = request.essay_outline
        if not DaraCore.is_null(request.essay_requirements):
            body['essayRequirements'] = request.essay_requirements
        if not DaraCore.is_null(request.essay_topic):
            body['essayTopic'] = request.essay_topic
        if not DaraCore.is_null(request.essay_type):
            body['essayType'] = request.essay_type
        if not DaraCore.is_null(request.essay_word_count):
            body['essayWordCount'] = request.essay_word_count
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.response_mode):
            body['responseMode'] = request.response_mode
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherEnglishCompositionTutoringWorkflowRun',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/intelligentAgent/englishCompositionTutoring/workflowRun',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_english_composition_tutoring_workflow_run(
        self,
        request: main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest,
    ) -> main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_english_composition_tutoring_workflow_run_with_options(request, headers, runtime)

    async def execute_aiteacher_english_composition_tutoring_workflow_run_async(
        self,
        request: main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunRequest,
    ) -> main_models.ExecuteAITeacherEnglishCompositionTutoringWorkflowRunResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_english_composition_tutoring_workflow_run_with_options_async(request, headers, runtime)

    def execute_aiteacher_english_paraphrase_chat_message_with_sse(
        self,
        request: main_models.ExecuteAITeacherEnglishParaphraseChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.question_id):
            body['questionId'] = request.question_id
        if not DaraCore.is_null(request.question_info):
            body['questionInfo'] = request.question_info
        if not DaraCore.is_null(request.response_mode):
            body['responseMode'] = request.response_mode
        if not DaraCore.is_null(request.user_answer):
            body['userAnswer'] = request.user_answer
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherEnglishParaphraseChatMessage',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/intelligentAgent/englishParaphrase/chatMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def execute_aiteacher_english_paraphrase_chat_message_with_sse_async(
        self,
        request: main_models.ExecuteAITeacherEnglishParaphraseChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.question_id):
            body['questionId'] = request.question_id
        if not DaraCore.is_null(request.question_info):
            body['questionInfo'] = request.question_info
        if not DaraCore.is_null(request.response_mode):
            body['responseMode'] = request.response_mode
        if not DaraCore.is_null(request.user_answer):
            body['userAnswer'] = request.user_answer
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherEnglishParaphraseChatMessage',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/intelligentAgent/englishParaphrase/chatMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def execute_aiteacher_english_paraphrase_chat_message_with_options(
        self,
        request: main_models.ExecuteAITeacherEnglishParaphraseChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.question_id):
            body['questionId'] = request.question_id
        if not DaraCore.is_null(request.question_info):
            body['questionInfo'] = request.question_info
        if not DaraCore.is_null(request.response_mode):
            body['responseMode'] = request.response_mode
        if not DaraCore.is_null(request.user_answer):
            body['userAnswer'] = request.user_answer
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherEnglishParaphraseChatMessage',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/intelligentAgent/englishParaphrase/chatMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_english_paraphrase_chat_message_with_options_async(
        self,
        request: main_models.ExecuteAITeacherEnglishParaphraseChatMessageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.question_id):
            body['questionId'] = request.question_id
        if not DaraCore.is_null(request.question_info):
            body['questionInfo'] = request.question_info
        if not DaraCore.is_null(request.response_mode):
            body['responseMode'] = request.response_mode
        if not DaraCore.is_null(request.user_answer):
            body['userAnswer'] = request.user_answer
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherEnglishParaphraseChatMessage',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/intelligentAgent/englishParaphrase/chatMessage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_english_paraphrase_chat_message(
        self,
        request: main_models.ExecuteAITeacherEnglishParaphraseChatMessageRequest,
    ) -> main_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_english_paraphrase_chat_message_with_options(request, headers, runtime)

    async def execute_aiteacher_english_paraphrase_chat_message_async(
        self,
        request: main_models.ExecuteAITeacherEnglishParaphraseChatMessageRequest,
    ) -> main_models.ExecuteAITeacherEnglishParaphraseChatMessageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_english_paraphrase_chat_message_with_options_async(request, headers, runtime)

    def execute_aiteacher_expansion_dialogue_with_options(
        self,
        request: main_models.ExecuteAITeacherExpansionDialogueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherExpansionDialogueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.background):
            body['background'] = request.background
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.language_code):
            body['languageCode'] = request.language_code
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.role_info):
            body['roleInfo'] = request.role_info
        if not DaraCore.is_null(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherExpansionDialogue',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/expansionPractice/executeExpansionTraining',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherExpansionDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_expansion_dialogue_with_options_async(
        self,
        request: main_models.ExecuteAITeacherExpansionDialogueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherExpansionDialogueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.background):
            body['background'] = request.background
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.language_code):
            body['languageCode'] = request.language_code
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.role_info):
            body['roleInfo'] = request.role_info
        if not DaraCore.is_null(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherExpansionDialogue',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/expansionPractice/executeExpansionTraining',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherExpansionDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_expansion_dialogue(
        self,
        request: main_models.ExecuteAITeacherExpansionDialogueRequest,
    ) -> main_models.ExecuteAITeacherExpansionDialogueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_expansion_dialogue_with_options(request, headers, runtime)

    async def execute_aiteacher_expansion_dialogue_async(
        self,
        request: main_models.ExecuteAITeacherExpansionDialogueRequest,
    ) -> main_models.ExecuteAITeacherExpansionDialogueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_expansion_dialogue_with_options_async(request, headers, runtime)

    def execute_aiteacher_expansion_dialogue_refine_with_options(
        self,
        request: main_models.ExecuteAITeacherExpansionDialogueRefineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherExpansionDialogueRefineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.background):
            body['background'] = request.background
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.language_code):
            body['languageCode'] = request.language_code
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.role_info):
            body['roleInfo'] = request.role_info
        if not DaraCore.is_null(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherExpansionDialogueRefine',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/expansionPractice/refineByContext',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherExpansionDialogueRefineResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_expansion_dialogue_refine_with_options_async(
        self,
        request: main_models.ExecuteAITeacherExpansionDialogueRefineRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherExpansionDialogueRefineResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.background):
            body['background'] = request.background
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.language_code):
            body['languageCode'] = request.language_code
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.role_info):
            body['roleInfo'] = request.role_info
        if not DaraCore.is_null(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherExpansionDialogueRefine',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/expansionPractice/refineByContext',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherExpansionDialogueRefineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_expansion_dialogue_refine(
        self,
        request: main_models.ExecuteAITeacherExpansionDialogueRefineRequest,
    ) -> main_models.ExecuteAITeacherExpansionDialogueRefineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_expansion_dialogue_refine_with_options(request, headers, runtime)

    async def execute_aiteacher_expansion_dialogue_refine_async(
        self,
        request: main_models.ExecuteAITeacherExpansionDialogueRefineRequest,
    ) -> main_models.ExecuteAITeacherExpansionDialogueRefineResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_expansion_dialogue_refine_with_options_async(request, headers, runtime)

    def execute_aiteacher_expansion_dialogue_translate_with_options(
        self,
        request: main_models.ExecuteAITeacherExpansionDialogueTranslateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherExpansionDialogueTranslateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.background):
            body['background'] = request.background
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.role_info):
            body['roleInfo'] = request.role_info
        if not DaraCore.is_null(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherExpansionDialogueTranslate',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/expansionPractice/translate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherExpansionDialogueTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_expansion_dialogue_translate_with_options_async(
        self,
        request: main_models.ExecuteAITeacherExpansionDialogueTranslateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherExpansionDialogueTranslateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.background):
            body['background'] = request.background
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.role_info):
            body['roleInfo'] = request.role_info
        if not DaraCore.is_null(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherExpansionDialogueTranslate',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/expansionPractice/translate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherExpansionDialogueTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_expansion_dialogue_translate(
        self,
        request: main_models.ExecuteAITeacherExpansionDialogueTranslateRequest,
    ) -> main_models.ExecuteAITeacherExpansionDialogueTranslateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_expansion_dialogue_translate_with_options(request, headers, runtime)

    async def execute_aiteacher_expansion_dialogue_translate_async(
        self,
        request: main_models.ExecuteAITeacherExpansionDialogueTranslateRequest,
    ) -> main_models.ExecuteAITeacherExpansionDialogueTranslateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_expansion_dialogue_translate_with_options_async(request, headers, runtime)

    def execute_aiteacher_grammar_check_with_options(
        self,
        request: main_models.ExecuteAITeacherGrammarCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherGrammarCheckResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherGrammarCheck',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/common/grammarChecking',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherGrammarCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_grammar_check_with_options_async(
        self,
        request: main_models.ExecuteAITeacherGrammarCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherGrammarCheckResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content):
            body['content'] = request.content
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherGrammarCheck',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/common/grammarChecking',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherGrammarCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_grammar_check(
        self,
        request: main_models.ExecuteAITeacherGrammarCheckRequest,
    ) -> main_models.ExecuteAITeacherGrammarCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_grammar_check_with_options(request, headers, runtime)

    async def execute_aiteacher_grammar_check_async(
        self,
        request: main_models.ExecuteAITeacherGrammarCheckRequest,
    ) -> main_models.ExecuteAITeacherGrammarCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_grammar_check_with_options_async(request, headers, runtime)

    def execute_aiteacher_sync_dialogue_with_options(
        self,
        request: main_models.ExecuteAITeacherSyncDialogueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherSyncDialogueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.language_code):
            body['languageCode'] = request.language_code
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherSyncDialogue',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/syncPractice/executeSyncTraining',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherSyncDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_sync_dialogue_with_options_async(
        self,
        request: main_models.ExecuteAITeacherSyncDialogueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherSyncDialogueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.language_code):
            body['languageCode'] = request.language_code
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherSyncDialogue',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/syncPractice/executeSyncTraining',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherSyncDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_sync_dialogue(
        self,
        request: main_models.ExecuteAITeacherSyncDialogueRequest,
    ) -> main_models.ExecuteAITeacherSyncDialogueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_sync_dialogue_with_options(request, headers, runtime)

    async def execute_aiteacher_sync_dialogue_async(
        self,
        request: main_models.ExecuteAITeacherSyncDialogueRequest,
    ) -> main_models.ExecuteAITeacherSyncDialogueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_sync_dialogue_with_options_async(request, headers, runtime)

    def execute_aiteacher_sync_dialogue_translate_with_options(
        self,
        request: main_models.ExecuteAITeacherSyncDialogueTranslateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherSyncDialogueTranslateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherSyncDialogueTranslate',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/syncPractice/translate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherSyncDialogueTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_aiteacher_sync_dialogue_translate_with_options_async(
        self,
        request: main_models.ExecuteAITeacherSyncDialogueTranslateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteAITeacherSyncDialogueTranslateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteAITeacherSyncDialogueTranslate',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/syncPractice/translate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteAITeacherSyncDialogueTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_aiteacher_sync_dialogue_translate(
        self,
        request: main_models.ExecuteAITeacherSyncDialogueTranslateRequest,
    ) -> main_models.ExecuteAITeacherSyncDialogueTranslateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_aiteacher_sync_dialogue_translate_with_options(request, headers, runtime)

    async def execute_aiteacher_sync_dialogue_translate_async(
        self,
        request: main_models.ExecuteAITeacherSyncDialogueTranslateRequest,
    ) -> main_models.ExecuteAITeacherSyncDialogueTranslateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_aiteacher_sync_dialogue_translate_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_dialogue_with_options(
        self,
        request: main_models.ExecuteTextbookAssistantDialogueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantDialogueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        if not DaraCore.is_null(request.user_message):
            body['userMessage'] = request.user_message
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantDialogue',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/ExecuteDialogue',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_dialogue_with_options_async(
        self,
        request: main_models.ExecuteTextbookAssistantDialogueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantDialogueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        if not DaraCore.is_null(request.user_message):
            body['userMessage'] = request.user_message
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantDialogue',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/ExecuteDialogue',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_dialogue(
        self,
        request: main_models.ExecuteTextbookAssistantDialogueRequest,
    ) -> main_models.ExecuteTextbookAssistantDialogueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_dialogue_with_options(request, headers, runtime)

    async def execute_textbook_assistant_dialogue_async(
        self,
        request: main_models.ExecuteTextbookAssistantDialogueRequest,
    ) -> main_models.ExecuteTextbookAssistantDialogueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_dialogue_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_difficulty_with_options(
        self,
        request: main_models.ExecuteTextbookAssistantDifficultyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantDifficultyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.assistant):
            body['assistant'] = request.assistant
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantDifficulty',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/ExecuteDifficulty',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantDifficultyResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_difficulty_with_options_async(
        self,
        request: main_models.ExecuteTextbookAssistantDifficultyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantDifficultyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.assistant):
            body['assistant'] = request.assistant
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantDifficulty',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/ExecuteDifficulty',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantDifficultyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_difficulty(
        self,
        request: main_models.ExecuteTextbookAssistantDifficultyRequest,
    ) -> main_models.ExecuteTextbookAssistantDifficultyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_difficulty_with_options(request, headers, runtime)

    async def execute_textbook_assistant_difficulty_async(
        self,
        request: main_models.ExecuteTextbookAssistantDifficultyRequest,
    ) -> main_models.ExecuteTextbookAssistantDifficultyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_difficulty_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_grammar_check_with_options(
        self,
        request: main_models.ExecuteTextbookAssistantGrammarCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantGrammarCheckResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        if not DaraCore.is_null(request.user):
            body['user'] = request.user
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantGrammarCheck',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/ExecuteGrammarCheck',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantGrammarCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_grammar_check_with_options_async(
        self,
        request: main_models.ExecuteTextbookAssistantGrammarCheckRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantGrammarCheckResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        if not DaraCore.is_null(request.user):
            body['user'] = request.user
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantGrammarCheck',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/ExecuteGrammarCheck',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantGrammarCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_grammar_check(
        self,
        request: main_models.ExecuteTextbookAssistantGrammarCheckRequest,
    ) -> main_models.ExecuteTextbookAssistantGrammarCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_grammar_check_with_options(request, headers, runtime)

    async def execute_textbook_assistant_grammar_check_async(
        self,
        request: main_models.ExecuteTextbookAssistantGrammarCheckRequest,
    ) -> main_models.ExecuteTextbookAssistantGrammarCheckResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_grammar_check_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_refine_by_context_with_options(
        self,
        request: main_models.ExecuteTextbookAssistantRefineByContextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantRefineByContextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        if not DaraCore.is_null(request.user):
            body['user'] = request.user
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantRefineByContext',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/RefineByContext',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantRefineByContextResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_refine_by_context_with_options_async(
        self,
        request: main_models.ExecuteTextbookAssistantRefineByContextRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantRefineByContextResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        if not DaraCore.is_null(request.user):
            body['user'] = request.user
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantRefineByContext',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/RefineByContext',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantRefineByContextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_refine_by_context(
        self,
        request: main_models.ExecuteTextbookAssistantRefineByContextRequest,
    ) -> main_models.ExecuteTextbookAssistantRefineByContextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_refine_by_context_with_options(request, headers, runtime)

    async def execute_textbook_assistant_refine_by_context_async(
        self,
        request: main_models.ExecuteTextbookAssistantRefineByContextRequest,
    ) -> main_models.ExecuteTextbookAssistantRefineByContextResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_refine_by_context_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_retry_conversation_with_options(
        self,
        request: main_models.ExecuteTextbookAssistantRetryConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantRetryConversationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assistant):
            body['assistant'] = request.assistant
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantRetryConversation',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/RetryConversation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantRetryConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_retry_conversation_with_options_async(
        self,
        request: main_models.ExecuteTextbookAssistantRetryConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantRetryConversationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assistant):
            body['assistant'] = request.assistant
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantRetryConversation',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/RetryConversation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantRetryConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_retry_conversation(
        self,
        request: main_models.ExecuteTextbookAssistantRetryConversationRequest,
    ) -> main_models.ExecuteTextbookAssistantRetryConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_retry_conversation_with_options(request, headers, runtime)

    async def execute_textbook_assistant_retry_conversation_async(
        self,
        request: main_models.ExecuteTextbookAssistantRetryConversationRequest,
    ) -> main_models.ExecuteTextbookAssistantRetryConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_retry_conversation_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_sse_dialogue_with_sse(
        self,
        request: main_models.ExecuteTextbookAssistantSseDialogueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ExecuteTextbookAssistantSseDialogueResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        if not DaraCore.is_null(request.user_message):
            body['userMessage'] = request.user_message
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantSseDialogue',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/ExecuteSseDialogue',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ExecuteTextbookAssistantSseDialogueResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def execute_textbook_assistant_sse_dialogue_with_sse_async(
        self,
        request: main_models.ExecuteTextbookAssistantSseDialogueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ExecuteTextbookAssistantSseDialogueResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        if not DaraCore.is_null(request.user_message):
            body['userMessage'] = request.user_message
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantSseDialogue',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/ExecuteSseDialogue',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ExecuteTextbookAssistantSseDialogueResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def execute_textbook_assistant_sse_dialogue_with_options(
        self,
        request: main_models.ExecuteTextbookAssistantSseDialogueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantSseDialogueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        if not DaraCore.is_null(request.user_message):
            body['userMessage'] = request.user_message
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantSseDialogue',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/ExecuteSseDialogue',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantSseDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_sse_dialogue_with_options_async(
        self,
        request: main_models.ExecuteTextbookAssistantSseDialogueRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantSseDialogueResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        if not DaraCore.is_null(request.user_message):
            body['userMessage'] = request.user_message
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantSseDialogue',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/ExecuteSseDialogue',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantSseDialogueResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_sse_dialogue(
        self,
        request: main_models.ExecuteTextbookAssistantSseDialogueRequest,
    ) -> main_models.ExecuteTextbookAssistantSseDialogueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_sse_dialogue_with_options(request, headers, runtime)

    async def execute_textbook_assistant_sse_dialogue_async(
        self,
        request: main_models.ExecuteTextbookAssistantSseDialogueRequest,
    ) -> main_models.ExecuteTextbookAssistantSseDialogueResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_sse_dialogue_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_start_conversation_with_options(
        self,
        request: main_models.ExecuteTextbookAssistantStartConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantStartConversationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.article_id):
            body['articleId'] = request.article_id
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantStartConversation',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/StartConversation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantStartConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_start_conversation_with_options_async(
        self,
        request: main_models.ExecuteTextbookAssistantStartConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantStartConversationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.article_id):
            body['articleId'] = request.article_id
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantStartConversation',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/StartConversation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantStartConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_start_conversation(
        self,
        request: main_models.ExecuteTextbookAssistantStartConversationRequest,
    ) -> main_models.ExecuteTextbookAssistantStartConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_start_conversation_with_options(request, headers, runtime)

    async def execute_textbook_assistant_start_conversation_async(
        self,
        request: main_models.ExecuteTextbookAssistantStartConversationRequest,
    ) -> main_models.ExecuteTextbookAssistantStartConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_start_conversation_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_suggestion_with_options(
        self,
        request: main_models.ExecuteTextbookAssistantSuggestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantSuggestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assistant):
            body['assistant'] = request.assistant
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantSuggestion',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/Suggestion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantSuggestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_suggestion_with_options_async(
        self,
        request: main_models.ExecuteTextbookAssistantSuggestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantSuggestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assistant):
            body['assistant'] = request.assistant
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantSuggestion',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/Suggestion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantSuggestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_suggestion(
        self,
        request: main_models.ExecuteTextbookAssistantSuggestionRequest,
    ) -> main_models.ExecuteTextbookAssistantSuggestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_suggestion_with_options(request, headers, runtime)

    async def execute_textbook_assistant_suggestion_async(
        self,
        request: main_models.ExecuteTextbookAssistantSuggestionRequest,
    ) -> main_models.ExecuteTextbookAssistantSuggestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_suggestion_with_options_async(request, headers, runtime)

    def execute_textbook_assistant_translate_with_options(
        self,
        request: main_models.ExecuteTextbookAssistantTranslateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantTranslateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assistant):
            body['assistant'] = request.assistant
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantTranslate',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/ExecuteTranslate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantTranslateResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_textbook_assistant_translate_with_options_async(
        self,
        request: main_models.ExecuteTextbookAssistantTranslateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTextbookAssistantTranslateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.assistant):
            body['assistant'] = request.assistant
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.chat_id):
            body['chatId'] = request.chat_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTextbookAssistantTranslate',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/dialogue/ExecuteTranslate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTextbookAssistantTranslateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_textbook_assistant_translate(
        self,
        request: main_models.ExecuteTextbookAssistantTranslateRequest,
    ) -> main_models.ExecuteTextbookAssistantTranslateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_textbook_assistant_translate_with_options(request, headers, runtime)

    async def execute_textbook_assistant_translate_async(
        self,
        request: main_models.ExecuteTextbookAssistantTranslateRequest,
    ) -> main_models.ExecuteTextbookAssistantTranslateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_textbook_assistant_translate_with_options_async(request, headers, runtime)

    def get_aiteacher_expansion_dialogue_suggestion_with_options(
        self,
        request: main_models.GetAITeacherExpansionDialogueSuggestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAITeacherExpansionDialogueSuggestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.background):
            body['background'] = request.background
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.language_code):
            body['languageCode'] = request.language_code
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.role_info):
            body['roleInfo'] = request.role_info
        if not DaraCore.is_null(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAITeacherExpansionDialogueSuggestion',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/expansionPractice/suggestion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAITeacherExpansionDialogueSuggestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aiteacher_expansion_dialogue_suggestion_with_options_async(
        self,
        request: main_models.GetAITeacherExpansionDialogueSuggestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAITeacherExpansionDialogueSuggestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.background):
            body['background'] = request.background
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.language_code):
            body['languageCode'] = request.language_code
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.role_info):
            body['roleInfo'] = request.role_info
        if not DaraCore.is_null(request.start_sentence):
            body['startSentence'] = request.start_sentence
        if not DaraCore.is_null(request.topic):
            body['topic'] = request.topic
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAITeacherExpansionDialogueSuggestion',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/expansionPractice/suggestion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAITeacherExpansionDialogueSuggestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aiteacher_expansion_dialogue_suggestion(
        self,
        request: main_models.GetAITeacherExpansionDialogueSuggestionRequest,
    ) -> main_models.GetAITeacherExpansionDialogueSuggestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_aiteacher_expansion_dialogue_suggestion_with_options(request, headers, runtime)

    async def get_aiteacher_expansion_dialogue_suggestion_async(
        self,
        request: main_models.GetAITeacherExpansionDialogueSuggestionRequest,
    ) -> main_models.GetAITeacherExpansionDialogueSuggestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_aiteacher_expansion_dialogue_suggestion_with_options_async(request, headers, runtime)

    def get_aiteacher_sync_dialogue_suggestion_with_options(
        self,
        request: main_models.GetAITeacherSyncDialogueSuggestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAITeacherSyncDialogueSuggestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.language_code):
            body['languageCode'] = request.language_code
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAITeacherSyncDialogueSuggestion',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/syncPractice/suggestion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAITeacherSyncDialogueSuggestionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aiteacher_sync_dialogue_suggestion_with_options_async(
        self,
        request: main_models.GetAITeacherSyncDialogueSuggestionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetAITeacherSyncDialogueSuggestionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dialogue_tasks):
            body['dialogueTasks'] = request.dialogue_tasks
        if not DaraCore.is_null(request.language_code):
            body['languageCode'] = request.language_code
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        if not DaraCore.is_null(request.user_id):
            body['userId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetAITeacherSyncDialogueSuggestion',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aiteacher/syncPractice/suggestion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAITeacherSyncDialogueSuggestionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aiteacher_sync_dialogue_suggestion(
        self,
        request: main_models.GetAITeacherSyncDialogueSuggestionRequest,
    ) -> main_models.GetAITeacherSyncDialogueSuggestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_aiteacher_sync_dialogue_suggestion_with_options(request, headers, runtime)

    async def get_aiteacher_sync_dialogue_suggestion_async(
        self,
        request: main_models.GetAITeacherSyncDialogueSuggestionRequest,
    ) -> main_models.GetAITeacherSyncDialogueSuggestionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_aiteacher_sync_dialogue_suggestion_with_options_async(request, headers, runtime)

    def get_textbook_assistant_token_with_options(
        self,
        request: main_models.GetTextbookAssistantTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextbookAssistantTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.device_id):
            body['deviceId'] = request.device_id
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTextbookAssistantToken',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/GetToken',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextbookAssistantTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_textbook_assistant_token_with_options_async(
        self,
        request: main_models.GetTextbookAssistantTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTextbookAssistantTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.device_id):
            body['deviceId'] = request.device_id
        if not DaraCore.is_null(request.model):
            body['model'] = request.model
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTextbookAssistantToken',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/GetToken',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextbookAssistantTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_textbook_assistant_token(
        self,
        request: main_models.GetTextbookAssistantTokenRequest,
    ) -> main_models.GetTextbookAssistantTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_textbook_assistant_token_with_options(request, headers, runtime)

    async def get_textbook_assistant_token_async(
        self,
        request: main_models.GetTextbookAssistantTokenRequest,
    ) -> main_models.GetTextbookAssistantTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_textbook_assistant_token_with_options_async(request, headers, runtime)

    def list_textbook_assistant_article_details_with_options(
        self,
        request: main_models.ListTextbookAssistantArticleDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextbookAssistantArticleDetailsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.article_id_list):
            body['articleIdList'] = request.article_id_list
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTextbookAssistantArticleDetails',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/ListArticleDetails',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextbookAssistantArticleDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_textbook_assistant_article_details_with_options_async(
        self,
        request: main_models.ListTextbookAssistantArticleDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextbookAssistantArticleDetailsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.article_id_list):
            body['articleIdList'] = request.article_id_list
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTextbookAssistantArticleDetails',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/ListArticleDetails',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextbookAssistantArticleDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_textbook_assistant_article_details(
        self,
        request: main_models.ListTextbookAssistantArticleDetailsRequest,
    ) -> main_models.ListTextbookAssistantArticleDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_textbook_assistant_article_details_with_options(request, headers, runtime)

    async def list_textbook_assistant_article_details_async(
        self,
        request: main_models.ListTextbookAssistantArticleDetailsRequest,
    ) -> main_models.ListTextbookAssistantArticleDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_textbook_assistant_article_details_with_options_async(request, headers, runtime)

    def list_textbook_assistant_articles_with_options(
        self,
        request: main_models.ListTextbookAssistantArticlesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextbookAssistantArticlesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTextbookAssistantArticles',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/ListArticles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextbookAssistantArticlesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_textbook_assistant_articles_with_options_async(
        self,
        request: main_models.ListTextbookAssistantArticlesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextbookAssistantArticlesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.directory_id):
            body['directoryId'] = request.directory_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTextbookAssistantArticles',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/ListArticles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextbookAssistantArticlesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_textbook_assistant_articles(
        self,
        request: main_models.ListTextbookAssistantArticlesRequest,
    ) -> main_models.ListTextbookAssistantArticlesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_textbook_assistant_articles_with_options(request, headers, runtime)

    async def list_textbook_assistant_articles_async(
        self,
        request: main_models.ListTextbookAssistantArticlesRequest,
    ) -> main_models.ListTextbookAssistantArticlesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_textbook_assistant_articles_with_options_async(request, headers, runtime)

    def list_textbook_assistant_book_directories_with_options(
        self,
        request: main_models.ListTextbookAssistantBookDirectoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextbookAssistantBookDirectoriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.book_id):
            body['bookId'] = request.book_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTextbookAssistantBookDirectories',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/ListBookDirectories',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextbookAssistantBookDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_textbook_assistant_book_directories_with_options_async(
        self,
        request: main_models.ListTextbookAssistantBookDirectoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextbookAssistantBookDirectoriesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.book_id):
            body['bookId'] = request.book_id
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTextbookAssistantBookDirectories',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/ListBookDirectories',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextbookAssistantBookDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_textbook_assistant_book_directories(
        self,
        request: main_models.ListTextbookAssistantBookDirectoriesRequest,
    ) -> main_models.ListTextbookAssistantBookDirectoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_textbook_assistant_book_directories_with_options(request, headers, runtime)

    async def list_textbook_assistant_book_directories_async(
        self,
        request: main_models.ListTextbookAssistantBookDirectoriesRequest,
    ) -> main_models.ListTextbookAssistantBookDirectoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_textbook_assistant_book_directories_with_options_async(request, headers, runtime)

    def list_textbook_assistant_books_with_options(
        self,
        request: main_models.ListTextbookAssistantBooksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextbookAssistantBooksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.book_id):
            body['bookId'] = request.book_id
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.max_results):
            body['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        if not DaraCore.is_null(request.volume):
            body['volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTextbookAssistantBooks',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/ListBooks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextbookAssistantBooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_textbook_assistant_books_with_options_async(
        self,
        request: main_models.ListTextbookAssistantBooksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextbookAssistantBooksResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.book_id):
            body['bookId'] = request.book_id
        if not DaraCore.is_null(request.grade):
            body['grade'] = request.grade
        if not DaraCore.is_null(request.max_results):
            body['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page):
            body['page'] = request.page
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        if not DaraCore.is_null(request.volume):
            body['volume'] = request.volume
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTextbookAssistantBooks',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/ListBooks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextbookAssistantBooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_textbook_assistant_books(
        self,
        request: main_models.ListTextbookAssistantBooksRequest,
    ) -> main_models.ListTextbookAssistantBooksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_textbook_assistant_books_with_options(request, headers, runtime)

    async def list_textbook_assistant_books_async(
        self,
        request: main_models.ListTextbookAssistantBooksRequest,
    ) -> main_models.ListTextbookAssistantBooksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_textbook_assistant_books_with_options_async(request, headers, runtime)

    def list_textbook_assistant_grade_volumes_with_options(
        self,
        request: main_models.ListTextbookAssistantGradeVolumesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextbookAssistantGradeVolumesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTextbookAssistantGradeVolumes',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/ListGradeVolumes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextbookAssistantGradeVolumesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_textbook_assistant_grade_volumes_with_options_async(
        self,
        request: main_models.ListTextbookAssistantGradeVolumesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextbookAssistantGradeVolumesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.scenario):
            body['scenario'] = request.scenario
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTextbookAssistantGradeVolumes',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/ListGradeVolumes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextbookAssistantGradeVolumesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_textbook_assistant_grade_volumes(
        self,
        request: main_models.ListTextbookAssistantGradeVolumesRequest,
    ) -> main_models.ListTextbookAssistantGradeVolumesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_textbook_assistant_grade_volumes_with_options(request, headers, runtime)

    async def list_textbook_assistant_grade_volumes_async(
        self,
        request: main_models.ListTextbookAssistantGradeVolumesRequest,
    ) -> main_models.ListTextbookAssistantGradeVolumesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_textbook_assistant_grade_volumes_with_options_async(request, headers, runtime)

    def list_textbook_assistant_scene_details_with_options(
        self,
        request: main_models.ListTextbookAssistantSceneDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextbookAssistantSceneDetailsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.scene_id_list):
            body['sceneIdList'] = request.scene_id_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTextbookAssistantSceneDetails',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/ListSceneDetails',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextbookAssistantSceneDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_textbook_assistant_scene_details_with_options_async(
        self,
        request: main_models.ListTextbookAssistantSceneDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTextbookAssistantSceneDetailsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auth_token):
            body['authToken'] = request.auth_token
        if not DaraCore.is_null(request.scene_id_list):
            body['sceneIdList'] = request.scene_id_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListTextbookAssistantSceneDetails',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/textbookAssistant/teachingResource/ListSceneDetails',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTextbookAssistantSceneDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_textbook_assistant_scene_details(
        self,
        request: main_models.ListTextbookAssistantSceneDetailsRequest,
    ) -> main_models.ListTextbookAssistantSceneDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_textbook_assistant_scene_details_with_options(request, headers, runtime)

    async def list_textbook_assistant_scene_details_async(
        self,
        request: main_models.ListTextbookAssistantSceneDetailsRequest,
    ) -> main_models.ListTextbookAssistantSceneDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_textbook_assistant_scene_details_with_options_async(request, headers, runtime)

    def model_router_billing_cost_tabs_with_options(
        self,
        request: main_models.ModelRouterBillingCostTabsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterBillingCostTabsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterBillingCostTabs',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/cost/tabs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterBillingCostTabsResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_billing_cost_tabs_with_options_async(
        self,
        request: main_models.ModelRouterBillingCostTabsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterBillingCostTabsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterBillingCostTabs',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/cost/tabs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterBillingCostTabsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_billing_cost_tabs(
        self,
        request: main_models.ModelRouterBillingCostTabsRequest,
    ) -> main_models.ModelRouterBillingCostTabsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_billing_cost_tabs_with_options(request, headers, runtime)

    async def model_router_billing_cost_tabs_async(
        self,
        request: main_models.ModelRouterBillingCostTabsRequest,
    ) -> main_models.ModelRouterBillingCostTabsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_billing_cost_tabs_with_options_async(request, headers, runtime)

    def model_router_chat_completions_with_sse(
        self,
        request: main_models.ModelRouterChatCompletionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ModelRouterChatCompletionsResponse, None, None]:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterChatCompletions',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ModelRouterChatCompletionsResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def model_router_chat_completions_with_sse_async(
        self,
        request: main_models.ModelRouterChatCompletionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ModelRouterChatCompletionsResponse, None, None]:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterChatCompletions',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ModelRouterChatCompletionsResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def model_router_chat_completions_with_options(
        self,
        request: main_models.ModelRouterChatCompletionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterChatCompletionsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterChatCompletions',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterChatCompletionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_chat_completions_with_options_async(
        self,
        request: main_models.ModelRouterChatCompletionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterChatCompletionsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = request.body
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterChatCompletions',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/chat/completions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterChatCompletionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_chat_completions(
        self,
        request: main_models.ModelRouterChatCompletionsRequest,
    ) -> main_models.ModelRouterChatCompletionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_chat_completions_with_options(request, headers, runtime)

    async def model_router_chat_completions_async(
        self,
        request: main_models.ModelRouterChatCompletionsRequest,
    ) -> main_models.ModelRouterChatCompletionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_chat_completions_with_options_async(request, headers, runtime)

    def model_router_copy_api_key_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterCopyApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterCopyApiKey',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/apikeys/{DaraURL.percent_encode(id)}/copy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterCopyApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_copy_api_key_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterCopyApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterCopyApiKey',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/apikeys/{DaraURL.percent_encode(id)}/copy',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterCopyApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_copy_api_key(
        self,
        id: str,
    ) -> main_models.ModelRouterCopyApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_copy_api_key_with_options(id, headers, runtime)

    async def model_router_copy_api_key_async(
        self,
        id: str,
    ) -> main_models.ModelRouterCopyApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_copy_api_key_with_options_async(id, headers, runtime)

    def model_router_create_api_key_with_options(
        self,
        request: main_models.ModelRouterCreateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterCreateApiKeyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterCreateApiKey',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/apikeys',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterCreateApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_create_api_key_with_options_async(
        self,
        request: main_models.ModelRouterCreateApiKeyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterCreateApiKeyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_id):
            body['clientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterCreateApiKey',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/apikeys',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterCreateApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_create_api_key(
        self,
        request: main_models.ModelRouterCreateApiKeyRequest,
    ) -> main_models.ModelRouterCreateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_create_api_key_with_options(request, headers, runtime)

    async def model_router_create_api_key_async(
        self,
        request: main_models.ModelRouterCreateApiKeyRequest,
    ) -> main_models.ModelRouterCreateApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_create_api_key_with_options_async(request, headers, runtime)

    def model_router_create_billing_rule_with_options(
        self,
        request: main_models.ModelRouterCreateBillingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterCreateBillingRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.billing_type):
            body['billingType'] = request.billing_type
        if not DaraCore.is_null(request.effective_time):
            body['effectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.expire_time):
            body['expireTime'] = request.expire_time
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.pricing_config):
            body['pricingConfig'] = request.pricing_config
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterCreateBillingRule',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterCreateBillingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_create_billing_rule_with_options_async(
        self,
        request: main_models.ModelRouterCreateBillingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterCreateBillingRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.billing_type):
            body['billingType'] = request.billing_type
        if not DaraCore.is_null(request.effective_time):
            body['effectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.expire_time):
            body['expireTime'] = request.expire_time
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.pricing_config):
            body['pricingConfig'] = request.pricing_config
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterCreateBillingRule',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/rules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterCreateBillingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_create_billing_rule(
        self,
        request: main_models.ModelRouterCreateBillingRuleRequest,
    ) -> main_models.ModelRouterCreateBillingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_create_billing_rule_with_options(request, headers, runtime)

    async def model_router_create_billing_rule_async(
        self,
        request: main_models.ModelRouterCreateBillingRuleRequest,
    ) -> main_models.ModelRouterCreateBillingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_create_billing_rule_with_options_async(request, headers, runtime)

    def model_router_create_client_with_options(
        self,
        request: main_models.ModelRouterCreateClientRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterCreateClientResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.address):
            body['address'] = request.address
        if not DaraCore.is_null(request.allowed_models):
            body['allowedModels'] = request.allowed_models
        if not DaraCore.is_null(request.contact):
            body['contact'] = request.contact
        if not DaraCore.is_null(request.discount):
            body['discount'] = request.discount
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            body['parentId'] = request.parent_id
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterCreateClient',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/clients',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterCreateClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_create_client_with_options_async(
        self,
        request: main_models.ModelRouterCreateClientRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterCreateClientResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.address):
            body['address'] = request.address
        if not DaraCore.is_null(request.allowed_models):
            body['allowedModels'] = request.allowed_models
        if not DaraCore.is_null(request.contact):
            body['contact'] = request.contact
        if not DaraCore.is_null(request.discount):
            body['discount'] = request.discount
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            body['parentId'] = request.parent_id
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterCreateClient',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/clients',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterCreateClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_create_client(
        self,
        request: main_models.ModelRouterCreateClientRequest,
    ) -> main_models.ModelRouterCreateClientResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_create_client_with_options(request, headers, runtime)

    async def model_router_create_client_async(
        self,
        request: main_models.ModelRouterCreateClientRequest,
    ) -> main_models.ModelRouterCreateClientResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_create_client_with_options_async(request, headers, runtime)

    def model_router_create_conversation_with_options(
        self,
        request: main_models.ModelRouterCreateConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterCreateConversationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chat_data):
            body['chatData'] = request.chat_data
        if not DaraCore.is_null(request.model_ids):
            body['modelIds'] = request.model_ids
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterCreateConversation',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/conversations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterCreateConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_create_conversation_with_options_async(
        self,
        request: main_models.ModelRouterCreateConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterCreateConversationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chat_data):
            body['chatData'] = request.chat_data
        if not DaraCore.is_null(request.model_ids):
            body['modelIds'] = request.model_ids
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterCreateConversation',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/conversations',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterCreateConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_create_conversation(
        self,
        request: main_models.ModelRouterCreateConversationRequest,
    ) -> main_models.ModelRouterCreateConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_create_conversation_with_options(request, headers, runtime)

    async def model_router_create_conversation_async(
        self,
        request: main_models.ModelRouterCreateConversationRequest,
    ) -> main_models.ModelRouterCreateConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_create_conversation_with_options_async(request, headers, runtime)

    def model_router_create_model_with_options(
        self,
        request: main_models.ModelRouterCreateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterCreateModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.base_url):
            body['baseUrl'] = request.base_url
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.extensions):
            body['extensions'] = request.extensions
        if not DaraCore.is_null(request.in_out):
            body['inOut'] = request.in_out
        if not DaraCore.is_null(request.max_input_length):
            body['maxInputLength'] = request.max_input_length
        if not DaraCore.is_null(request.max_output_length):
            body['maxOutputLength'] = request.max_output_length
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.model_type):
            body['modelType'] = request.model_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.symbol):
            body['symbol'] = request.symbol
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterCreateModel',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/models',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterCreateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_create_model_with_options_async(
        self,
        request: main_models.ModelRouterCreateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterCreateModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.base_url):
            body['baseUrl'] = request.base_url
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.extensions):
            body['extensions'] = request.extensions
        if not DaraCore.is_null(request.in_out):
            body['inOut'] = request.in_out
        if not DaraCore.is_null(request.max_input_length):
            body['maxInputLength'] = request.max_input_length
        if not DaraCore.is_null(request.max_output_length):
            body['maxOutputLength'] = request.max_output_length
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.model_type):
            body['modelType'] = request.model_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.symbol):
            body['symbol'] = request.symbol
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterCreateModel',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/models',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterCreateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_create_model(
        self,
        request: main_models.ModelRouterCreateModelRequest,
    ) -> main_models.ModelRouterCreateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_create_model_with_options(request, headers, runtime)

    async def model_router_create_model_async(
        self,
        request: main_models.ModelRouterCreateModelRequest,
    ) -> main_models.ModelRouterCreateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_create_model_with_options_async(request, headers, runtime)

    def model_router_delete_api_key_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterDeleteApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterDeleteApiKey',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/apikeys/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterDeleteApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_delete_api_key_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterDeleteApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterDeleteApiKey',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/apikeys/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterDeleteApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_delete_api_key(
        self,
        id: str,
    ) -> main_models.ModelRouterDeleteApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_delete_api_key_with_options(id, headers, runtime)

    async def model_router_delete_api_key_async(
        self,
        id: str,
    ) -> main_models.ModelRouterDeleteApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_delete_api_key_with_options_async(id, headers, runtime)

    def model_router_delete_client_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterDeleteClientResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterDeleteClient',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/clients/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterDeleteClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_delete_client_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterDeleteClientResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterDeleteClient',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/clients/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterDeleteClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_delete_client(
        self,
        id: str,
    ) -> main_models.ModelRouterDeleteClientResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_delete_client_with_options(id, headers, runtime)

    async def model_router_delete_client_async(
        self,
        id: str,
    ) -> main_models.ModelRouterDeleteClientResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_delete_client_with_options_async(id, headers, runtime)

    def model_router_delete_conversation_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterDeleteConversationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterDeleteConversation',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/conversations/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterDeleteConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_delete_conversation_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterDeleteConversationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterDeleteConversation',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/conversations/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterDeleteConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_delete_conversation(
        self,
        id: str,
    ) -> main_models.ModelRouterDeleteConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_delete_conversation_with_options(id, headers, runtime)

    async def model_router_delete_conversation_async(
        self,
        id: str,
    ) -> main_models.ModelRouterDeleteConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_delete_conversation_with_options_async(id, headers, runtime)

    def model_router_delete_model_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterDeleteModelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterDeleteModel',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/models/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterDeleteModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_delete_model_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterDeleteModelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterDeleteModel',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/models/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterDeleteModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_delete_model(
        self,
        id: str,
    ) -> main_models.ModelRouterDeleteModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_delete_model_with_options(id, headers, runtime)

    async def model_router_delete_model_async(
        self,
        id: str,
    ) -> main_models.ModelRouterDeleteModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_delete_model_with_options_async(id, headers, runtime)

    def model_router_query_api_key_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryApiKey',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/apikeys/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryApiKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_api_key_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryApiKeyResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryApiKey',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/apikeys/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryApiKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_api_key(
        self,
        id: str,
    ) -> main_models.ModelRouterQueryApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_api_key_with_options(id, headers, runtime)

    async def model_router_query_api_key_async(
        self,
        id: str,
    ) -> main_models.ModelRouterQueryApiKeyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_api_key_with_options_async(id, headers, runtime)

    def model_router_query_api_key_list_with_options(
        self,
        request: main_models.ModelRouterQueryApiKeyListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryApiKeyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryApiKeyList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/apikeys',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryApiKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_api_key_list_with_options_async(
        self,
        request: main_models.ModelRouterQueryApiKeyListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryApiKeyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryApiKeyList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/apikeys',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryApiKeyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_api_key_list(
        self,
        request: main_models.ModelRouterQueryApiKeyListRequest,
    ) -> main_models.ModelRouterQueryApiKeyListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_api_key_list_with_options(request, headers, runtime)

    async def model_router_query_api_key_list_async(
        self,
        request: main_models.ModelRouterQueryApiKeyListRequest,
    ) -> main_models.ModelRouterQueryApiKeyListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_api_key_list_with_options_async(request, headers, runtime)

    def model_router_query_billing_rule_list_with_options(
        self,
        request: main_models.ModelRouterQueryBillingRuleListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryBillingRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_only):
            query['activeOnly'] = request.active_only
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_code):
            query['modelCode'] = request.model_code
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryBillingRuleList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryBillingRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_billing_rule_list_with_options_async(
        self,
        request: main_models.ModelRouterQueryBillingRuleListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryBillingRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_only):
            query['activeOnly'] = request.active_only
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_code):
            query['modelCode'] = request.model_code
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryBillingRuleList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/rules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryBillingRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_billing_rule_list(
        self,
        request: main_models.ModelRouterQueryBillingRuleListRequest,
    ) -> main_models.ModelRouterQueryBillingRuleListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_billing_rule_list_with_options(request, headers, runtime)

    async def model_router_query_billing_rule_list_async(
        self,
        request: main_models.ModelRouterQueryBillingRuleListRequest,
    ) -> main_models.ModelRouterQueryBillingRuleListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_billing_rule_list_with_options_async(request, headers, runtime)

    def model_router_query_client_discount_logs_with_options(
        self,
        id: str,
        request: main_models.ModelRouterQueryClientDiscountLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryClientDiscountLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryClientDiscountLogs',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/clients/{DaraURL.percent_encode(id)}/discount-logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryClientDiscountLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_client_discount_logs_with_options_async(
        self,
        id: str,
        request: main_models.ModelRouterQueryClientDiscountLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryClientDiscountLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryClientDiscountLogs',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/clients/{DaraURL.percent_encode(id)}/discount-logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryClientDiscountLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_client_discount_logs(
        self,
        id: str,
        request: main_models.ModelRouterQueryClientDiscountLogsRequest,
    ) -> main_models.ModelRouterQueryClientDiscountLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_client_discount_logs_with_options(id, request, headers, runtime)

    async def model_router_query_client_discount_logs_async(
        self,
        id: str,
        request: main_models.ModelRouterQueryClientDiscountLogsRequest,
    ) -> main_models.ModelRouterQueryClientDiscountLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_client_discount_logs_with_options_async(id, request, headers, runtime)

    def model_router_query_client_list_with_options(
        self,
        request: main_models.ModelRouterQueryClientListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryClientListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryClientList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/clients',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryClientListResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_client_list_with_options_async(
        self,
        request: main_models.ModelRouterQueryClientListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryClientListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryClientList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/clients',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryClientListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_client_list(
        self,
        request: main_models.ModelRouterQueryClientListRequest,
    ) -> main_models.ModelRouterQueryClientListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_client_list_with_options(request, headers, runtime)

    async def model_router_query_client_list_async(
        self,
        request: main_models.ModelRouterQueryClientListRequest,
    ) -> main_models.ModelRouterQueryClientListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_client_list_with_options_async(request, headers, runtime)

    def model_router_query_client_tree_with_options(
        self,
        request: main_models.ModelRouterQueryClientTreeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryClientTreeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryClientTree',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/clients/tree',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryClientTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_client_tree_with_options_async(
        self,
        request: main_models.ModelRouterQueryClientTreeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryClientTreeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryClientTree',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/clients/tree',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryClientTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_client_tree(
        self,
        request: main_models.ModelRouterQueryClientTreeRequest,
    ) -> main_models.ModelRouterQueryClientTreeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_client_tree_with_options(request, headers, runtime)

    async def model_router_query_client_tree_async(
        self,
        request: main_models.ModelRouterQueryClientTreeRequest,
    ) -> main_models.ModelRouterQueryClientTreeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_client_tree_with_options_async(request, headers, runtime)

    def model_router_query_conversation_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryConversationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryConversation',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/conversations/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_conversation_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryConversationResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryConversation',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/conversations/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_conversation(
        self,
        id: str,
    ) -> main_models.ModelRouterQueryConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_conversation_with_options(id, headers, runtime)

    async def model_router_query_conversation_async(
        self,
        id: str,
    ) -> main_models.ModelRouterQueryConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_conversation_with_options_async(id, headers, runtime)

    def model_router_query_conversation_list_with_options(
        self,
        request: main_models.ModelRouterQueryConversationListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryConversationListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryConversationList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/conversations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryConversationListResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_conversation_list_with_options_async(
        self,
        request: main_models.ModelRouterQueryConversationListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryConversationListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryConversationList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/conversations',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryConversationListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_conversation_list(
        self,
        request: main_models.ModelRouterQueryConversationListRequest,
    ) -> main_models.ModelRouterQueryConversationListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_conversation_list_with_options(request, headers, runtime)

    async def model_router_query_conversation_list_async(
        self,
        request: main_models.ModelRouterQueryConversationListRequest,
    ) -> main_models.ModelRouterQueryConversationListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_conversation_list_with_options_async(request, headers, runtime)

    def model_router_query_cost_model_detail_with_options(
        self,
        request: main_models.ModelRouterQueryCostModelDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryCostModelDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryCostModelDetail',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/cost/model-detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryCostModelDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_cost_model_detail_with_options_async(
        self,
        request: main_models.ModelRouterQueryCostModelDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryCostModelDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryCostModelDetail',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/cost/model-detail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryCostModelDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_cost_model_detail(
        self,
        request: main_models.ModelRouterQueryCostModelDetailRequest,
    ) -> main_models.ModelRouterQueryCostModelDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_cost_model_detail_with_options(request, headers, runtime)

    async def model_router_query_cost_model_detail_async(
        self,
        request: main_models.ModelRouterQueryCostModelDetailRequest,
    ) -> main_models.ModelRouterQueryCostModelDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_cost_model_detail_with_options_async(request, headers, runtime)

    def model_router_query_cost_model_list_with_options(
        self,
        request: main_models.ModelRouterQueryCostModelListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryCostModelListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.granularity):
            query['granularity'] = request.granularity
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_types):
            query['modelTypes'] = request.model_types
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.search):
            query['search'] = request.search
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryCostModelList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/cost/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryCostModelListResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_cost_model_list_with_options_async(
        self,
        request: main_models.ModelRouterQueryCostModelListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryCostModelListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.granularity):
            query['granularity'] = request.granularity
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_types):
            query['modelTypes'] = request.model_types
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.search):
            query['search'] = request.search
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryCostModelList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/cost/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryCostModelListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_cost_model_list(
        self,
        request: main_models.ModelRouterQueryCostModelListRequest,
    ) -> main_models.ModelRouterQueryCostModelListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_cost_model_list_with_options(request, headers, runtime)

    async def model_router_query_cost_model_list_async(
        self,
        request: main_models.ModelRouterQueryCostModelListRequest,
    ) -> main_models.ModelRouterQueryCostModelListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_cost_model_list_with_options_async(request, headers, runtime)

    def model_router_query_cost_overview_metrics_with_options(
        self,
        request: main_models.ModelRouterQueryCostOverviewMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryCostOverviewMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.granularity):
            query['granularity'] = request.granularity
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_types):
            query['modelTypes'] = request.model_types
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryCostOverviewMetrics',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/cost/overview',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryCostOverviewMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_cost_overview_metrics_with_options_async(
        self,
        request: main_models.ModelRouterQueryCostOverviewMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryCostOverviewMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.granularity):
            query['granularity'] = request.granularity
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_types):
            query['modelTypes'] = request.model_types
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryCostOverviewMetrics',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/cost/overview',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryCostOverviewMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_cost_overview_metrics(
        self,
        request: main_models.ModelRouterQueryCostOverviewMetricsRequest,
    ) -> main_models.ModelRouterQueryCostOverviewMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_cost_overview_metrics_with_options(request, headers, runtime)

    async def model_router_query_cost_overview_metrics_async(
        self,
        request: main_models.ModelRouterQueryCostOverviewMetricsRequest,
    ) -> main_models.ModelRouterQueryCostOverviewMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_cost_overview_metrics_with_options_async(request, headers, runtime)

    def model_router_query_cost_trend_metrics_with_options(
        self,
        request: main_models.ModelRouterQueryCostTrendMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryCostTrendMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.granularity):
            query['granularity'] = request.granularity
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_types):
            query['modelTypes'] = request.model_types
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryCostTrendMetrics',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/cost/trend',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryCostTrendMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_cost_trend_metrics_with_options_async(
        self,
        request: main_models.ModelRouterQueryCostTrendMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryCostTrendMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.granularity):
            query['granularity'] = request.granularity
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_types):
            query['modelTypes'] = request.model_types
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryCostTrendMetrics',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/cost/trend',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryCostTrendMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_cost_trend_metrics(
        self,
        request: main_models.ModelRouterQueryCostTrendMetricsRequest,
    ) -> main_models.ModelRouterQueryCostTrendMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_cost_trend_metrics_with_options(request, headers, runtime)

    async def model_router_query_cost_trend_metrics_async(
        self,
        request: main_models.ModelRouterQueryCostTrendMetricsRequest,
    ) -> main_models.ModelRouterQueryCostTrendMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_cost_trend_metrics_with_options_async(request, headers, runtime)

    def model_router_query_model_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryModelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryModel',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/models/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_model_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryModelResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryModel',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/models/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_model(
        self,
        id: str,
    ) -> main_models.ModelRouterQueryModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_model_with_options(id, headers, runtime)

    async def model_router_query_model_async(
        self,
        id: str,
    ) -> main_models.ModelRouterQueryModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_model_with_options_async(id, headers, runtime)

    def model_router_query_model_list_with_options(
        self,
        request: main_models.ModelRouterQueryModelListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryModelListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryModelList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryModelListResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_model_list_with_options_async(
        self,
        request: main_models.ModelRouterQueryModelListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryModelListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_type):
            query['modelType'] = request.model_type
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryModelList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryModelListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_model_list(
        self,
        request: main_models.ModelRouterQueryModelListRequest,
    ) -> main_models.ModelRouterQueryModelListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_model_list_with_options(request, headers, runtime)

    async def model_router_query_model_list_async(
        self,
        request: main_models.ModelRouterQueryModelListRequest,
    ) -> main_models.ModelRouterQueryModelListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_model_list_with_options_async(request, headers, runtime)

    def model_router_query_nacos_providers_with_options(
        self,
        request: main_models.ModelRouterQueryNacosProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryNacosProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryNacosProviders',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/nacos/providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryNacosProvidersResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_nacos_providers_with_options_async(
        self,
        request: main_models.ModelRouterQueryNacosProvidersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryNacosProvidersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryNacosProviders',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/nacos/providers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryNacosProvidersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_nacos_providers(
        self,
        request: main_models.ModelRouterQueryNacosProvidersRequest,
    ) -> main_models.ModelRouterQueryNacosProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_nacos_providers_with_options(request, headers, runtime)

    async def model_router_query_nacos_providers_async(
        self,
        request: main_models.ModelRouterQueryNacosProvidersRequest,
    ) -> main_models.ModelRouterQueryNacosProvidersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_nacos_providers_with_options_async(request, headers, runtime)

    def model_router_query_nacos_tags_with_options(
        self,
        request: main_models.ModelRouterQueryNacosTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryNacosTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_type):
            query['configType'] = request.config_type
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryNacosTags',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/nacos/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryNacosTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_nacos_tags_with_options_async(
        self,
        request: main_models.ModelRouterQueryNacosTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryNacosTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_type):
            query['configType'] = request.config_type
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryNacosTags',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/nacos/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryNacosTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_nacos_tags(
        self,
        request: main_models.ModelRouterQueryNacosTagsRequest,
    ) -> main_models.ModelRouterQueryNacosTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_nacos_tags_with_options(request, headers, runtime)

    async def model_router_query_nacos_tags_async(
        self,
        request: main_models.ModelRouterQueryNacosTagsRequest,
    ) -> main_models.ModelRouterQueryNacosTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_nacos_tags_with_options_async(request, headers, runtime)

    def model_router_query_observation_charts_with_options(
        self,
        request: main_models.ModelRouterQueryObservationChartsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryObservationChartsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_id):
            query['apiKeyId'] = request.api_key_id
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryObservationCharts',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/observation/charts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryObservationChartsResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_observation_charts_with_options_async(
        self,
        request: main_models.ModelRouterQueryObservationChartsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryObservationChartsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_id):
            query['apiKeyId'] = request.api_key_id
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryObservationCharts',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/observation/charts',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryObservationChartsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_observation_charts(
        self,
        request: main_models.ModelRouterQueryObservationChartsRequest,
    ) -> main_models.ModelRouterQueryObservationChartsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_observation_charts_with_options(request, headers, runtime)

    async def model_router_query_observation_charts_async(
        self,
        request: main_models.ModelRouterQueryObservationChartsRequest,
    ) -> main_models.ModelRouterQueryObservationChartsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_observation_charts_with_options_async(request, headers, runtime)

    def model_router_query_observation_logs_with_options(
        self,
        request: main_models.ModelRouterQueryObservationLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryObservationLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_id):
            query['apiKeyId'] = request.api_key_id
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryObservationLogs',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/observation/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryObservationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_observation_logs_with_options_async(
        self,
        request: main_models.ModelRouterQueryObservationLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryObservationLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_id):
            query['apiKeyId'] = request.api_key_id
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryObservationLogs',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/observation/logs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryObservationLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_observation_logs(
        self,
        request: main_models.ModelRouterQueryObservationLogsRequest,
    ) -> main_models.ModelRouterQueryObservationLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_observation_logs_with_options(request, headers, runtime)

    async def model_router_query_observation_logs_async(
        self,
        request: main_models.ModelRouterQueryObservationLogsRequest,
    ) -> main_models.ModelRouterQueryObservationLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_observation_logs_with_options_async(request, headers, runtime)

    def model_router_query_observation_metrics_with_options(
        self,
        request: main_models.ModelRouterQueryObservationMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryObservationMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_id):
            query['apiKeyId'] = request.api_key_id
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryObservationMetrics',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/observation/metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryObservationMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_query_observation_metrics_with_options_async(
        self,
        request: main_models.ModelRouterQueryObservationMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterQueryObservationMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_key_id):
            query['apiKeyId'] = request.api_key_id
        if not DaraCore.is_null(request.client_id):
            query['clientId'] = request.client_id
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.group_by):
            query['groupBy'] = request.group_by
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        if not DaraCore.is_null(request.need_total_count):
            query['needTotalCount'] = request.need_total_count
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_index):
            query['pageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterQueryObservationMetrics',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/observation/metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterQueryObservationMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_query_observation_metrics(
        self,
        request: main_models.ModelRouterQueryObservationMetricsRequest,
    ) -> main_models.ModelRouterQueryObservationMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_query_observation_metrics_with_options(request, headers, runtime)

    async def model_router_query_observation_metrics_async(
        self,
        request: main_models.ModelRouterQueryObservationMetricsRequest,
    ) -> main_models.ModelRouterQueryObservationMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_query_observation_metrics_with_options_async(request, headers, runtime)

    def model_router_update_billing_rule_with_options(
        self,
        id: str,
        request: main_models.ModelRouterUpdateBillingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterUpdateBillingRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.billing_type):
            body['billingType'] = request.billing_type
        if not DaraCore.is_null(request.effective_time):
            body['effectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.expire_time):
            body['expireTime'] = request.expire_time
        if not DaraCore.is_null(request.pricing_config):
            body['pricingConfig'] = request.pricing_config
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterUpdateBillingRule',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/rules/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterUpdateBillingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_update_billing_rule_with_options_async(
        self,
        id: str,
        request: main_models.ModelRouterUpdateBillingRuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterUpdateBillingRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.billing_type):
            body['billingType'] = request.billing_type
        if not DaraCore.is_null(request.effective_time):
            body['effectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.expire_time):
            body['expireTime'] = request.expire_time
        if not DaraCore.is_null(request.pricing_config):
            body['pricingConfig'] = request.pricing_config
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterUpdateBillingRule',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/billing/rules/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterUpdateBillingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_update_billing_rule(
        self,
        id: str,
        request: main_models.ModelRouterUpdateBillingRuleRequest,
    ) -> main_models.ModelRouterUpdateBillingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_update_billing_rule_with_options(id, request, headers, runtime)

    async def model_router_update_billing_rule_async(
        self,
        id: str,
        request: main_models.ModelRouterUpdateBillingRuleRequest,
    ) -> main_models.ModelRouterUpdateBillingRuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_update_billing_rule_with_options_async(id, request, headers, runtime)

    def model_router_update_client_with_options(
        self,
        id: str,
        request: main_models.ModelRouterUpdateClientRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterUpdateClientResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.address):
            body['address'] = request.address
        if not DaraCore.is_null(request.allowed_models):
            body['allowedModels'] = request.allowed_models
        if not DaraCore.is_null(request.contact):
            body['contact'] = request.contact
        if not DaraCore.is_null(request.discount):
            body['discount'] = request.discount
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterUpdateClient',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/clients/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterUpdateClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_update_client_with_options_async(
        self,
        id: str,
        request: main_models.ModelRouterUpdateClientRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterUpdateClientResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.address):
            body['address'] = request.address
        if not DaraCore.is_null(request.allowed_models):
            body['allowedModels'] = request.allowed_models
        if not DaraCore.is_null(request.contact):
            body['contact'] = request.contact
        if not DaraCore.is_null(request.discount):
            body['discount'] = request.discount
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.remark):
            body['remark'] = request.remark
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterUpdateClient',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/clients/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterUpdateClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_update_client(
        self,
        id: str,
        request: main_models.ModelRouterUpdateClientRequest,
    ) -> main_models.ModelRouterUpdateClientResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_update_client_with_options(id, request, headers, runtime)

    async def model_router_update_client_async(
        self,
        id: str,
        request: main_models.ModelRouterUpdateClientRequest,
    ) -> main_models.ModelRouterUpdateClientResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_update_client_with_options_async(id, request, headers, runtime)

    def model_router_update_conversation_with_options(
        self,
        id: str,
        request: main_models.ModelRouterUpdateConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterUpdateConversationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chat_data):
            body['chatData'] = request.chat_data
        if not DaraCore.is_null(request.message_count):
            body['messageCount'] = request.message_count
        if not DaraCore.is_null(request.model_ids):
            body['modelIds'] = request.model_ids
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterUpdateConversation',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/conversations/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterUpdateConversationResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_update_conversation_with_options_async(
        self,
        id: str,
        request: main_models.ModelRouterUpdateConversationRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterUpdateConversationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.chat_data):
            body['chatData'] = request.chat_data
        if not DaraCore.is_null(request.message_count):
            body['messageCount'] = request.message_count
        if not DaraCore.is_null(request.model_ids):
            body['modelIds'] = request.model_ids
        if not DaraCore.is_null(request.title):
            body['title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterUpdateConversation',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/conversations/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterUpdateConversationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_update_conversation(
        self,
        id: str,
        request: main_models.ModelRouterUpdateConversationRequest,
    ) -> main_models.ModelRouterUpdateConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_update_conversation_with_options(id, request, headers, runtime)

    async def model_router_update_conversation_async(
        self,
        id: str,
        request: main_models.ModelRouterUpdateConversationRequest,
    ) -> main_models.ModelRouterUpdateConversationResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_update_conversation_with_options_async(id, request, headers, runtime)

    def model_router_update_model_with_options(
        self,
        id: str,
        request: main_models.ModelRouterUpdateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterUpdateModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.base_url):
            body['baseUrl'] = request.base_url
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.max_input_length):
            body['maxInputLength'] = request.max_input_length
        if not DaraCore.is_null(request.max_output_length):
            body['maxOutputLength'] = request.max_output_length
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.model_type):
            body['modelType'] = request.model_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.symbol):
            body['symbol'] = request.symbol
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterUpdateModel',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/models/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterUpdateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_router_update_model_with_options_async(
        self,
        id: str,
        request: main_models.ModelRouterUpdateModelRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModelRouterUpdateModelResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.api_key):
            body['apiKey'] = request.api_key
        if not DaraCore.is_null(request.base_url):
            body['baseUrl'] = request.base_url
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.max_input_length):
            body['maxInputLength'] = request.max_input_length
        if not DaraCore.is_null(request.max_output_length):
            body['maxOutputLength'] = request.max_output_length
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.model_type):
            body['modelType'] = request.model_type
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.status):
            body['status'] = request.status
        if not DaraCore.is_null(request.symbol):
            body['symbol'] = request.symbol
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModelRouterUpdateModel',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelRouter/open/models/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModelRouterUpdateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_router_update_model(
        self,
        id: str,
        request: main_models.ModelRouterUpdateModelRequest,
    ) -> main_models.ModelRouterUpdateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.model_router_update_model_with_options(id, request, headers, runtime)

    async def model_router_update_model_async(
        self,
        id: str,
        request: main_models.ModelRouterUpdateModelRequest,
    ) -> main_models.ModelRouterUpdateModelResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.model_router_update_model_with_options_async(id, request, headers, runtime)

    def personalized_text_to_image_add_inference_job_with_options(
        self,
        request: main_models.PersonalizedTextToImageAddInferenceJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PersonalizedTextToImageAddInferenceJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_number):
            body['imageNumber'] = request.image_number
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.seed):
            body['seed'] = request.seed
        if not DaraCore.is_null(request.strength):
            body['strength'] = request.strength
        if not DaraCore.is_null(request.train_steps):
            body['trainSteps'] = request.train_steps
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PersonalizedTextToImageAddInferenceJob',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/addPreModelInferenceJob',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PersonalizedTextToImageAddInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalized_text_to_image_add_inference_job_with_options_async(
        self,
        request: main_models.PersonalizedTextToImageAddInferenceJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PersonalizedTextToImageAddInferenceJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_number):
            body['imageNumber'] = request.image_number
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.seed):
            body['seed'] = request.seed
        if not DaraCore.is_null(request.strength):
            body['strength'] = request.strength
        if not DaraCore.is_null(request.train_steps):
            body['trainSteps'] = request.train_steps
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PersonalizedTextToImageAddInferenceJob',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/addPreModelInferenceJob',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PersonalizedTextToImageAddInferenceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalized_text_to_image_add_inference_job(
        self,
        request: main_models.PersonalizedTextToImageAddInferenceJobRequest,
    ) -> main_models.PersonalizedTextToImageAddInferenceJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.personalized_text_to_image_add_inference_job_with_options(request, headers, runtime)

    async def personalized_text_to_image_add_inference_job_async(
        self,
        request: main_models.PersonalizedTextToImageAddInferenceJobRequest,
    ) -> main_models.PersonalizedTextToImageAddInferenceJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.personalized_text_to_image_add_inference_job_with_options_async(request, headers, runtime)

    def personalized_text_to_image_query_image_asset_with_options(
        self,
        request: main_models.PersonalizedTextToImageQueryImageAssetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PersonalizedTextToImageQueryImageAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encode_format):
            query['encodeFormat'] = request.encode_format
        if not DaraCore.is_null(request.image_id):
            query['imageId'] = request.image_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PersonalizedTextToImageQueryImageAsset',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/queryImageAssetFromImageId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'any'
        )
        return DaraCore.from_map(
            main_models.PersonalizedTextToImageQueryImageAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalized_text_to_image_query_image_asset_with_options_async(
        self,
        request: main_models.PersonalizedTextToImageQueryImageAssetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PersonalizedTextToImageQueryImageAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encode_format):
            query['encodeFormat'] = request.encode_format
        if not DaraCore.is_null(request.image_id):
            query['imageId'] = request.image_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PersonalizedTextToImageQueryImageAsset',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/queryImageAssetFromImageId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'any'
        )
        return DaraCore.from_map(
            main_models.PersonalizedTextToImageQueryImageAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalized_text_to_image_query_image_asset(
        self,
        request: main_models.PersonalizedTextToImageQueryImageAssetRequest,
    ) -> main_models.PersonalizedTextToImageQueryImageAssetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.personalized_text_to_image_query_image_asset_with_options(request, headers, runtime)

    async def personalized_text_to_image_query_image_asset_async(
        self,
        request: main_models.PersonalizedTextToImageQueryImageAssetRequest,
    ) -> main_models.PersonalizedTextToImageQueryImageAssetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.personalized_text_to_image_query_image_asset_with_options_async(request, headers, runtime)

    def personalized_text_to_image_query_pre_model_inference_job_info_with_options(
        self,
        request: main_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inference_job_id):
            query['inferenceJobId'] = request.inference_job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PersonalizedTextToImageQueryPreModelInferenceJobInfo',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/queryPreModelInferenceJobInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalized_text_to_image_query_pre_model_inference_job_info_with_options_async(
        self,
        request: main_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inference_job_id):
            query['inferenceJobId'] = request.inference_job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PersonalizedTextToImageQueryPreModelInferenceJobInfo',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/queryPreModelInferenceJobInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalized_text_to_image_query_pre_model_inference_job_info(
        self,
        request: main_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest,
    ) -> main_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.personalized_text_to_image_query_pre_model_inference_job_info_with_options(request, headers, runtime)

    async def personalized_text_to_image_query_pre_model_inference_job_info_async(
        self,
        request: main_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoRequest,
    ) -> main_models.PersonalizedTextToImageQueryPreModelInferenceJobInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.personalized_text_to_image_query_pre_model_inference_job_info_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_add_inference_job_with_options(
        self,
        request: main_models.Personalizedtxt2imgAddInferenceJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.Personalizedtxt2imgAddInferenceJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_number):
            body['imageNumber'] = request.image_number
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.seed):
            body['seed'] = request.seed
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Personalizedtxt2imgAddInferenceJob',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/addInferenceJob',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Personalizedtxt2imgAddInferenceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_add_inference_job_with_options_async(
        self,
        request: main_models.Personalizedtxt2imgAddInferenceJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.Personalizedtxt2imgAddInferenceJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_number):
            body['imageNumber'] = request.image_number
        if not DaraCore.is_null(request.model_id):
            body['modelId'] = request.model_id
        if not DaraCore.is_null(request.prompt):
            body['prompt'] = request.prompt
        if not DaraCore.is_null(request.seed):
            body['seed'] = request.seed
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Personalizedtxt2imgAddInferenceJob',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/addInferenceJob',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Personalizedtxt2imgAddInferenceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_add_inference_job(
        self,
        request: main_models.Personalizedtxt2imgAddInferenceJobRequest,
    ) -> main_models.Personalizedtxt2imgAddInferenceJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_add_inference_job_with_options(request, headers, runtime)

    async def personalizedtxt_2img_add_inference_job_async(
        self,
        request: main_models.Personalizedtxt2imgAddInferenceJobRequest,
    ) -> main_models.Personalizedtxt2imgAddInferenceJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_add_inference_job_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_add_model_train_job_with_options(
        self,
        request: main_models.Personalizedtxt2imgAddModelTrainJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.Personalizedtxt2imgAddModelTrainJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.object_type):
            body['objectType'] = request.object_type
        if not DaraCore.is_null(request.train_steps):
            body['trainSteps'] = request.train_steps
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Personalizedtxt2imgAddModelTrainJob',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/addModelTrainJob',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Personalizedtxt2imgAddModelTrainJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_add_model_train_job_with_options_async(
        self,
        request: main_models.Personalizedtxt2imgAddModelTrainJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.Personalizedtxt2imgAddModelTrainJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_url):
            body['imageUrl'] = request.image_url
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.object_type):
            body['objectType'] = request.object_type
        if not DaraCore.is_null(request.train_steps):
            body['trainSteps'] = request.train_steps
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Personalizedtxt2imgAddModelTrainJob',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/addModelTrainJob',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Personalizedtxt2imgAddModelTrainJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_add_model_train_job(
        self,
        request: main_models.Personalizedtxt2imgAddModelTrainJobRequest,
    ) -> main_models.Personalizedtxt2imgAddModelTrainJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_add_model_train_job_with_options(request, headers, runtime)

    async def personalizedtxt_2img_add_model_train_job_async(
        self,
        request: main_models.Personalizedtxt2imgAddModelTrainJobRequest,
    ) -> main_models.Personalizedtxt2imgAddModelTrainJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_add_model_train_job_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_query_image_asset_with_options(
        self,
        request: main_models.Personalizedtxt2imgQueryImageAssetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.Personalizedtxt2imgQueryImageAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encode_format):
            query['encodeFormat'] = request.encode_format
        if not DaraCore.is_null(request.image_id):
            query['imageId'] = request.image_id
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        if not DaraCore.is_null(request.prompt_id):
            query['promptId'] = request.prompt_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Personalizedtxt2imgQueryImageAsset',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/queryImageAsset',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'any'
        )
        return DaraCore.from_map(
            main_models.Personalizedtxt2imgQueryImageAssetResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_query_image_asset_with_options_async(
        self,
        request: main_models.Personalizedtxt2imgQueryImageAssetRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.Personalizedtxt2imgQueryImageAssetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encode_format):
            query['encodeFormat'] = request.encode_format
        if not DaraCore.is_null(request.image_id):
            query['imageId'] = request.image_id
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        if not DaraCore.is_null(request.prompt_id):
            query['promptId'] = request.prompt_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Personalizedtxt2imgQueryImageAsset',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/queryImageAsset',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'any'
        )
        return DaraCore.from_map(
            main_models.Personalizedtxt2imgQueryImageAssetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_query_image_asset(
        self,
        request: main_models.Personalizedtxt2imgQueryImageAssetRequest,
    ) -> main_models.Personalizedtxt2imgQueryImageAssetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_query_image_asset_with_options(request, headers, runtime)

    async def personalizedtxt_2img_query_image_asset_async(
        self,
        request: main_models.Personalizedtxt2imgQueryImageAssetRequest,
    ) -> main_models.Personalizedtxt2imgQueryImageAssetResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_query_image_asset_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_query_inference_job_info_with_options(
        self,
        request: main_models.Personalizedtxt2imgQueryInferenceJobInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.Personalizedtxt2imgQueryInferenceJobInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inference_job_id):
            query['inferenceJobId'] = request.inference_job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Personalizedtxt2imgQueryInferenceJobInfo',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/queryInferenceJobInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Personalizedtxt2imgQueryInferenceJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_query_inference_job_info_with_options_async(
        self,
        request: main_models.Personalizedtxt2imgQueryInferenceJobInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.Personalizedtxt2imgQueryInferenceJobInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.inference_job_id):
            query['inferenceJobId'] = request.inference_job_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Personalizedtxt2imgQueryInferenceJobInfo',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/queryInferenceJobInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Personalizedtxt2imgQueryInferenceJobInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_query_inference_job_info(
        self,
        request: main_models.Personalizedtxt2imgQueryInferenceJobInfoRequest,
    ) -> main_models.Personalizedtxt2imgQueryInferenceJobInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_query_inference_job_info_with_options(request, headers, runtime)

    async def personalizedtxt_2img_query_inference_job_info_async(
        self,
        request: main_models.Personalizedtxt2imgQueryInferenceJobInfoRequest,
    ) -> main_models.Personalizedtxt2imgQueryInferenceJobInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_query_inference_job_info_with_options_async(request, headers, runtime)

    def personalizedtxt_2img_query_model_train_job_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.Personalizedtxt2imgQueryModelTrainJobListResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'Personalizedtxt2imgQueryModelTrainJobList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/queryModelTrainJobList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Personalizedtxt2imgQueryModelTrainJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_query_model_train_job_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.Personalizedtxt2imgQueryModelTrainJobListResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'Personalizedtxt2imgQueryModelTrainJobList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/queryModelTrainJobList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Personalizedtxt2imgQueryModelTrainJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_query_model_train_job_list(self) -> main_models.Personalizedtxt2imgQueryModelTrainJobListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_query_model_train_job_list_with_options(headers, runtime)

    async def personalizedtxt_2img_query_model_train_job_list_async(self) -> main_models.Personalizedtxt2imgQueryModelTrainJobListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_query_model_train_job_list_with_options_async(headers, runtime)

    def personalizedtxt_2img_query_model_train_status_with_options(
        self,
        request: main_models.Personalizedtxt2imgQueryModelTrainStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.Personalizedtxt2imgQueryModelTrainStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Personalizedtxt2imgQueryModelTrainStatus',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/queryModelTrainStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Personalizedtxt2imgQueryModelTrainStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def personalizedtxt_2img_query_model_train_status_with_options_async(
        self,
        request: main_models.Personalizedtxt2imgQueryModelTrainStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.Personalizedtxt2imgQueryModelTrainStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.model_id):
            query['modelId'] = request.model_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Personalizedtxt2imgQueryModelTrainStatus',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/personalizedtxt2img/queryModelTrainStatus',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.Personalizedtxt2imgQueryModelTrainStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def personalizedtxt_2img_query_model_train_status(
        self,
        request: main_models.Personalizedtxt2imgQueryModelTrainStatusRequest,
    ) -> main_models.Personalizedtxt2imgQueryModelTrainStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.personalizedtxt_2img_query_model_train_status_with_options(request, headers, runtime)

    async def personalizedtxt_2img_query_model_train_status_async(
        self,
        request: main_models.Personalizedtxt2imgQueryModelTrainStatusRequest,
    ) -> main_models.Personalizedtxt2imgQueryModelTrainStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.personalizedtxt_2img_query_model_train_status_with_options_async(request, headers, runtime)

    def query_application_access_id_with_options(
        self,
        request: main_models.QueryApplicationAccessIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryApplicationAccessIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_access_id):
            query['applicationAccessId'] = request.application_access_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryApplicationAccessId',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/queryApplicationAccessId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryApplicationAccessIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_application_access_id_with_options_async(
        self,
        request: main_models.QueryApplicationAccessIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryApplicationAccessIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_access_id):
            query['applicationAccessId'] = request.application_access_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryApplicationAccessId',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/queryApplicationAccessId',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryApplicationAccessIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_application_access_id(
        self,
        request: main_models.QueryApplicationAccessIdRequest,
    ) -> main_models.QueryApplicationAccessIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_application_access_id_with_options(request, headers, runtime)

    async def query_application_access_id_async(
        self,
        request: main_models.QueryApplicationAccessIdRequest,
    ) -> main_models.QueryApplicationAccessIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_application_access_id_with_options_async(request, headers, runtime)

    def query_project_with_options(
        self,
        request: main_models.QueryProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['projectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryProject',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/queryProject',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_project_with_options_async(
        self,
        request: main_models.QueryProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_id):
            query['projectId'] = request.project_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryProject',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/queryProject',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_project(
        self,
        request: main_models.QueryProjectRequest,
    ) -> main_models.QueryProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_project_with_options(request, headers, runtime)

    async def query_project_async(
        self,
        request: main_models.QueryProjectRequest,
    ) -> main_models.QueryProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_project_with_options_async(request, headers, runtime)

    def query_project_list_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryProjectListResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'QueryProjectList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/queryProjectList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryProjectListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_project_list_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryProjectListResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'QueryProjectList',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/queryProjectList',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryProjectListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_project_list(self) -> main_models.QueryProjectListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_project_list_with_options(headers, runtime)

    async def query_project_list_async(self) -> main_models.QueryProjectListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_project_list_with_options_async(headers, runtime)

    def query_purchased_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryPurchasedServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'QueryPurchasedService',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/queryPurchasedService',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPurchasedServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_purchased_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryPurchasedServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'QueryPurchasedService',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/queryPurchasedService',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPurchasedServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_purchased_service(self) -> main_models.QueryPurchasedServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_purchased_service_with_options(headers, runtime)

    async def query_purchased_service_async(self) -> main_models.QueryPurchasedServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_purchased_service_with_options_async(headers, runtime)

    def update_project_with_options(
        self,
        request: main_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.project_name):
            body['projectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/updateProject',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        request: main_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.project_name):
            body['projectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '20240611',
            protocol = 'HTTPS',
            pathname = f'/api/v1/aliyunConsole/updateProject',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_project_with_options(request, headers, runtime)

    async def update_project_async(
        self,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_project_with_options_async(request, headers, runtime)
