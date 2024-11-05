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
