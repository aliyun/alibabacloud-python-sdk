# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkedmallretrieval20240501 import models as linkedmall_retrieval_20240501_models
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
        self._endpoint = self.get_endpoint('linkedmallretrieval', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def a_isearch_v2with_options(
        self,
        request: linkedmall_retrieval_20240501_models.AISearchV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_retrieval_20240501_models.AISearchV2Response:
        """
        @summary 提供通用检索与检索后处理的多阶段优化结果，为开放域QA提供信源
        
        @param request: AISearchV2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AISearchV2Response
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='AISearchV2',
            version='2024-05-01',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v2/linkedRetrieval/commands/aiSearch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_retrieval_20240501_models.AISearchV2Response(),
            self.call_api(params, req, runtime)
        )

    async def a_isearch_v2with_options_async(
        self,
        request: linkedmall_retrieval_20240501_models.AISearchV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_retrieval_20240501_models.AISearchV2Response:
        """
        @summary 提供通用检索与检索后处理的多阶段优化结果，为开放域QA提供信源
        
        @param request: AISearchV2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AISearchV2Response
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='AISearchV2',
            version='2024-05-01',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v2/linkedRetrieval/commands/aiSearch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_retrieval_20240501_models.AISearchV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def a_isearch_v2(
        self,
        request: linkedmall_retrieval_20240501_models.AISearchV2Request,
    ) -> linkedmall_retrieval_20240501_models.AISearchV2Response:
        """
        @summary 提供通用检索与检索后处理的多阶段优化结果，为开放域QA提供信源
        
        @param request: AISearchV2Request
        @return: AISearchV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.a_isearch_v2with_options(request, headers, runtime)

    async def a_isearch_v2_async(
        self,
        request: linkedmall_retrieval_20240501_models.AISearchV2Request,
    ) -> linkedmall_retrieval_20240501_models.AISearchV2Response:
        """
        @summary 提供通用检索与检索后处理的多阶段优化结果，为开放域QA提供信源
        
        @param request: AISearchV2Request
        @return: AISearchV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.a_isearch_v2with_options_async(request, headers, runtime)

    def generic_search_with_options(
        self,
        request: linkedmall_retrieval_20240501_models.GenericSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_retrieval_20240501_models.GenericSearchResponse:
        """
        @summary 通用搜索
        
        @param request: GenericSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenericSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenericSearch',
            version='2024-05-01',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v2/linkedRetrieval/commands/genericSearch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_retrieval_20240501_models.GenericSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def generic_search_with_options_async(
        self,
        request: linkedmall_retrieval_20240501_models.GenericSearchRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_retrieval_20240501_models.GenericSearchResponse:
        """
        @summary 通用搜索
        
        @param request: GenericSearchRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenericSearchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.query):
            query['query'] = request.query
        if not UtilClient.is_unset(request.time_range):
            query['timeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenericSearch',
            version='2024-05-01',
            protocol='HTTPS',
            pathname=f'/linked-retrieval/linked-retrieval-entry/v2/linkedRetrieval/commands/genericSearch',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_retrieval_20240501_models.GenericSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generic_search(
        self,
        request: linkedmall_retrieval_20240501_models.GenericSearchRequest,
    ) -> linkedmall_retrieval_20240501_models.GenericSearchResponse:
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
        request: linkedmall_retrieval_20240501_models.GenericSearchRequest,
    ) -> linkedmall_retrieval_20240501_models.GenericSearchResponse:
        """
        @summary 通用搜索
        
        @param request: GenericSearchRequest
        @return: GenericSearchResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generic_search_with_options_async(request, headers, runtime)
