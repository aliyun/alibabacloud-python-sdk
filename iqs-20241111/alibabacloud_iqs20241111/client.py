# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_iqs20241111 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
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
        self._endpoint = self.get_endpoint('iqs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def ai_search_with_sse(
        self,
        request: main_models.AiSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.AiSearchResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AiSearch',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v3/linkedRetrieval/commands/aiSearch',
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
                main_models.AiSearchResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def ai_search_with_sse_async(
        self,
        request: main_models.AiSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.AiSearchResponse, None, None]:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AiSearch',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v3/linkedRetrieval/commands/aiSearch',
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
                main_models.AiSearchResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def ai_search_with_options(
        self,
        request: main_models.AiSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AiSearchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AiSearch',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v3/linkedRetrieval/commands/aiSearch',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AiSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def ai_search_with_options_async(
        self,
        request: main_models.AiSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AiSearchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AiSearch',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v3/linkedRetrieval/commands/aiSearch',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AiSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ai_search(
        self,
        request: main_models.AiSearchRequest,
    ) -> main_models.AiSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.ai_search_with_options(request, headers, runtime)

    async def ai_search_async(
        self,
        request: main_models.AiSearchRequest,
    ) -> main_models.AiSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.ai_search_with_options_async(request, headers, runtime)

    def generic_advanced_search_with_options(
        self,
        request: main_models.GenericAdvancedSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenericAdvancedSearchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenericAdvancedSearch',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v2/linkedRetrieval/commands/genericAdvancedSearch',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenericAdvancedSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def generic_advanced_search_with_options_async(
        self,
        request: main_models.GenericAdvancedSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenericAdvancedSearchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenericAdvancedSearch',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v2/linkedRetrieval/commands/genericAdvancedSearch',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenericAdvancedSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generic_advanced_search(
        self,
        request: main_models.GenericAdvancedSearchRequest,
    ) -> main_models.GenericAdvancedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generic_advanced_search_with_options(request, headers, runtime)

    async def generic_advanced_search_async(
        self,
        request: main_models.GenericAdvancedSearchRequest,
    ) -> main_models.GenericAdvancedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generic_advanced_search_with_options_async(request, headers, runtime)

    def generic_search_with_options(
        self,
        tmp_req: main_models.GenericSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenericSearchResponse:
        tmp_req.validate()
        request = main_models.GenericSearchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.advanced_params):
            request.advanced_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.advanced_params, 'advancedParams', 'json')
        query = {}
        if not DaraCore.is_null(request.advanced_params_shrink):
            query['advancedParams'] = request.advanced_params_shrink
        if not DaraCore.is_null(request.enable_rerank):
            query['enableRerank'] = request.enable_rerank
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.return_main_text):
            query['returnMainText'] = request.return_main_text
        if not DaraCore.is_null(request.return_markdown_text):
            query['returnMarkdownText'] = request.return_markdown_text
        if not DaraCore.is_null(request.return_rich_main_body):
            query['returnRichMainBody'] = request.return_rich_main_body
        if not DaraCore.is_null(request.return_summary):
            query['returnSummary'] = request.return_summary
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenericSearch',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v2/linkedRetrieval/commands/genericSearch',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenericSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def generic_search_with_options_async(
        self,
        tmp_req: main_models.GenericSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenericSearchResponse:
        tmp_req.validate()
        request = main_models.GenericSearchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.advanced_params):
            request.advanced_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.advanced_params, 'advancedParams', 'json')
        query = {}
        if not DaraCore.is_null(request.advanced_params_shrink):
            query['advancedParams'] = request.advanced_params_shrink
        if not DaraCore.is_null(request.enable_rerank):
            query['enableRerank'] = request.enable_rerank
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.return_main_text):
            query['returnMainText'] = request.return_main_text
        if not DaraCore.is_null(request.return_markdown_text):
            query['returnMarkdownText'] = request.return_markdown_text
        if not DaraCore.is_null(request.return_rich_main_body):
            query['returnRichMainBody'] = request.return_rich_main_body
        if not DaraCore.is_null(request.return_summary):
            query['returnSummary'] = request.return_summary
        if not DaraCore.is_null(request.session_id):
            query['sessionId'] = request.session_id
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenericSearch',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v2/linkedRetrieval/commands/genericSearch',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenericSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generic_search(
        self,
        request: main_models.GenericSearchRequest,
    ) -> main_models.GenericSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generic_search_with_options(request, headers, runtime)

    async def generic_search_async(
        self,
        request: main_models.GenericSearchRequest,
    ) -> main_models.GenericSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generic_search_with_options_async(request, headers, runtime)

    def get_iqs_usage_with_options(
        self,
        request: main_models.GetIqsUsageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIqsUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_id):
            query['callerId'] = request.caller_id
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIqsUsage',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/v1/iqs/usage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIqsUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_iqs_usage_with_options_async(
        self,
        request: main_models.GetIqsUsageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIqsUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.caller_id):
            query['callerId'] = request.caller_id
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIqsUsage',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-admin/v1/iqs/usage',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIqsUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_iqs_usage(
        self,
        request: main_models.GetIqsUsageRequest,
    ) -> main_models.GetIqsUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_iqs_usage_with_options(request, headers, runtime)

    async def get_iqs_usage_async(
        self,
        request: main_models.GetIqsUsageRequest,
    ) -> main_models.GetIqsUsageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_iqs_usage_with_options_async(request, headers, runtime)

    def global_search_with_options(
        self,
        request: main_models.GlobalSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalSearchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GlobalSearch',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v1/iqs/search/global',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_search_with_options_async(
        self,
        request: main_models.GlobalSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GlobalSearchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GlobalSearch',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v1/iqs/search/global',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GlobalSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_search(
        self,
        request: main_models.GlobalSearchRequest,
    ) -> main_models.GlobalSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.global_search_with_options(request, headers, runtime)

    async def global_search_async(
        self,
        request: main_models.GlobalSearchRequest,
    ) -> main_models.GlobalSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.global_search_with_options_async(request, headers, runtime)

    def read_page_basic_with_options(
        self,
        request: main_models.ReadPageBasicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReadPageBasicResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ReadPageBasic',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v1/iqs/readpage/basic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadPageBasicResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_page_basic_with_options_async(
        self,
        request: main_models.ReadPageBasicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReadPageBasicResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ReadPageBasic',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v1/iqs/readpage/basic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadPageBasicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_page_basic(
        self,
        request: main_models.ReadPageBasicRequest,
    ) -> main_models.ReadPageBasicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.read_page_basic_with_options(request, headers, runtime)

    async def read_page_basic_async(
        self,
        request: main_models.ReadPageBasicRequest,
    ) -> main_models.ReadPageBasicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.read_page_basic_with_options_async(request, headers, runtime)

    def read_page_scrape_with_options(
        self,
        request: main_models.ReadPageScrapeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReadPageScrapeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ReadPageScrape',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v1/iqs/readpage/scrape',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadPageScrapeResponse(),
            self.call_api(params, req, runtime)
        )

    async def read_page_scrape_with_options_async(
        self,
        request: main_models.ReadPageScrapeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ReadPageScrapeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ReadPageScrape',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v1/iqs/readpage/scrape',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReadPageScrapeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def read_page_scrape(
        self,
        request: main_models.ReadPageScrapeRequest,
    ) -> main_models.ReadPageScrapeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.read_page_scrape_with_options(request, headers, runtime)

    async def read_page_scrape_async(
        self,
        request: main_models.ReadPageScrapeRequest,
    ) -> main_models.ReadPageScrapeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.read_page_scrape_with_options_async(request, headers, runtime)

    def unified_search_with_options(
        self,
        request: main_models.UnifiedSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnifiedSearchResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UnifiedSearch',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v1/iqs/search/unified',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnifiedSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def unified_search_with_options_async(
        self,
        request: main_models.UnifiedSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnifiedSearchResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UnifiedSearch',
            version = '2024-11-11',
            protocol = 'HTTPS',
            pathname = f'/linked-retrieval/linked-retrieval-entry/v1/iqs/search/unified',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnifiedSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unified_search(
        self,
        request: main_models.UnifiedSearchRequest,
    ) -> main_models.UnifiedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.unified_search_with_options(request, headers, runtime)

    async def unified_search_async(
        self,
        request: main_models.UnifiedSearchRequest,
    ) -> main_models.UnifiedSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.unified_search_with_options_async(request, headers, runtime)
