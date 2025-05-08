# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iqs20241111 import models as iqs20241111_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def ai_search_with_options(
        self,
        request: iqs20241111_models.AiSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20241111_models.AiSearchResponse:
        """
        @summary AI搜索流式接口
        
        @param request: AiSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AiSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AiSearch',
            version='2024-11-11',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v3/linkedRetrieval/commands/aiSearch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20241111_models.AiSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def ai_search_with_options_async(
        self,
        request: iqs20241111_models.AiSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20241111_models.AiSearchResponse:
        """
        @summary AI搜索流式接口
        
        @param request: AiSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AiSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AiSearch',
            version='2024-11-11',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v3/linkedRetrieval/commands/aiSearch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20241111_models.AiSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ai_search(
        self,
        request: iqs20241111_models.AiSearchRequest,
    ) -> iqs20241111_models.AiSearchResponse:
        """
        @summary AI搜索流式接口
        
        @param request: AiSearchRequest
        @return: AiSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.ai_search_with_options(request, headers, runtime)

    async def ai_search_async(
        self,
        request: iqs20241111_models.AiSearchRequest,
    ) -> iqs20241111_models.AiSearchResponse:
        """
        @summary AI搜索流式接口
        
        @param request: AiSearchRequest
        @return: AiSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.ai_search_with_options_async(request, headers, runtime)

    def generic_advanced_search_with_options(
        self,
        request: iqs20241111_models.GenericAdvancedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20241111_models.GenericAdvancedSearchResponse:
        """
        @summary 增强版通用搜索
        
        @param request: GenericAdvancedSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenericAdvancedSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenericAdvancedSearch',
            version='2024-11-11',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v2/linkedRetrieval/commands/genericAdvancedSearch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20241111_models.GenericAdvancedSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def generic_advanced_search_with_options_async(
        self,
        request: iqs20241111_models.GenericAdvancedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20241111_models.GenericAdvancedSearchResponse:
        """
        @summary 增强版通用搜索
        
        @param request: GenericAdvancedSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenericAdvancedSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenericAdvancedSearch',
            version='2024-11-11',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v2/linkedRetrieval/commands/genericAdvancedSearch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20241111_models.GenericAdvancedSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generic_advanced_search(
        self,
        request: iqs20241111_models.GenericAdvancedSearchRequest,
    ) -> iqs20241111_models.GenericAdvancedSearchResponse:
        """
        @summary 增强版通用搜索
        
        @param request: GenericAdvancedSearchRequest
        @return: GenericAdvancedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generic_advanced_search_with_options(request, headers, runtime)

    async def generic_advanced_search_async(
        self,
        request: iqs20241111_models.GenericAdvancedSearchRequest,
    ) -> iqs20241111_models.GenericAdvancedSearchResponse:
        """
        @summary 增强版通用搜索
        
        @param request: GenericAdvancedSearchRequest
        @return: GenericAdvancedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generic_advanced_search_with_options_async(request, headers, runtime)

    def generic_search_with_options(
        self,
        request: iqs20241111_models.GenericSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20241111_models.GenericSearchResponse:
        """
        @summary 通用搜索
        
        @param request: GenericSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenericSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_rerank):
            query['enableRerank'] = request.enable_rerank
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.return_main_text):
            query['returnMainText'] = request.return_main_text
        if not UtilClient.is_unset(request.return_markdown_text):
            query['returnMarkdownText'] = request.return_markdown_text
        if not UtilClient.is_unset(request.return_summary):
            query['returnSummary'] = request.return_summary
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenericSearch',
            version='2024-11-11',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v2/linkedRetrieval/commands/genericSearch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20241111_models.GenericSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def generic_search_with_options_async(
        self,
        request: iqs20241111_models.GenericSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20241111_models.GenericSearchResponse:
        """
        @summary 通用搜索
        
        @param request: GenericSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenericSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_rerank):
            query['enableRerank'] = request.enable_rerank
        if not UtilClient.is_unset(request.industry):
            query['industry'] = request.industry
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.return_main_text):
            query['returnMainText'] = request.return_main_text
        if not UtilClient.is_unset(request.return_markdown_text):
            query['returnMarkdownText'] = request.return_markdown_text
        if not UtilClient.is_unset(request.return_summary):
            query['returnSummary'] = request.return_summary
        if not UtilClient.is_unset(request.session_id):
            query['sessionId'] = request.session_id
        if not UtilClient.is_unset(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenericSearch',
            version='2024-11-11',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v2/linkedRetrieval/commands/genericSearch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20241111_models.GenericSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generic_search(
        self,
        request: iqs20241111_models.GenericSearchRequest,
    ) -> iqs20241111_models.GenericSearchResponse:
        """
        @summary 通用搜索
        
        @param request: GenericSearchRequest
        @return: GenericSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generic_search_with_options(request, headers, runtime)

    async def generic_search_async(
        self,
        request: iqs20241111_models.GenericSearchRequest,
    ) -> iqs20241111_models.GenericSearchResponse:
        """
        @summary 通用搜索
        
        @param request: GenericSearchRequest
        @return: GenericSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generic_search_with_options_async(request, headers, runtime)

    def global_search_with_options(
        self,
        request: iqs20241111_models.GlobalSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20241111_models.GlobalSearchResponse:
        """
        @summary 通晓搜索-出海版(全球信息搜索)
        
        @param request: GlobalSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GlobalSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GlobalSearch',
            version='2024-11-11',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v1/iqs/search/global',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20241111_models.GlobalSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def global_search_with_options_async(
        self,
        request: iqs20241111_models.GlobalSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20241111_models.GlobalSearchResponse:
        """
        @summary 通晓搜索-出海版(全球信息搜索)
        
        @param request: GlobalSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GlobalSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GlobalSearch',
            version='2024-11-11',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v1/iqs/search/global',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20241111_models.GlobalSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def global_search(
        self,
        request: iqs20241111_models.GlobalSearchRequest,
    ) -> iqs20241111_models.GlobalSearchResponse:
        """
        @summary 通晓搜索-出海版(全球信息搜索)
        
        @param request: GlobalSearchRequest
        @return: GlobalSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.global_search_with_options(request, headers, runtime)

    async def global_search_async(
        self,
        request: iqs20241111_models.GlobalSearchRequest,
    ) -> iqs20241111_models.GlobalSearchResponse:
        """
        @summary 通晓搜索-出海版(全球信息搜索)
        
        @param request: GlobalSearchRequest
        @return: GlobalSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.global_search_with_options_async(request, headers, runtime)

    def unified_search_with_options(
        self,
        request: iqs20241111_models.UnifiedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20241111_models.UnifiedSearchResponse:
        """
        @summary 通晓统一搜索API
        
        @param request: UnifiedSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnifiedSearchResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UnifiedSearch',
            version='2024-11-11',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v1/iqs/search/unified',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20241111_models.UnifiedSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def unified_search_with_options_async(
        self,
        request: iqs20241111_models.UnifiedSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> iqs20241111_models.UnifiedSearchResponse:
        """
        @summary 通晓统一搜索API
        
        @param request: UnifiedSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnifiedSearchResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UnifiedSearch',
            version='2024-11-11',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v1/iqs/search/unified',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            iqs20241111_models.UnifiedSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unified_search(
        self,
        request: iqs20241111_models.UnifiedSearchRequest,
    ) -> iqs20241111_models.UnifiedSearchResponse:
        """
        @summary 通晓统一搜索API
        
        @param request: UnifiedSearchRequest
        @return: UnifiedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unified_search_with_options(request, headers, runtime)

    async def unified_search_async(
        self,
        request: iqs20241111_models.UnifiedSearchRequest,
    ) -> iqs20241111_models.UnifiedSearchResponse:
        """
        @summary 通晓统一搜索API
        
        @param request: UnifiedSearchRequest
        @return: UnifiedSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.unified_search_with_options_async(request, headers, runtime)
