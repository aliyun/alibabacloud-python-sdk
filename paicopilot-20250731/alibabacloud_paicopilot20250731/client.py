# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paicopilot20250731 import models as paicopilot_20250731_models
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
        self._endpoint = self.get_endpoint('paicopilot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def search_info_with_options(
        self,
        request: paicopilot_20250731_models.SearchInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paicopilot_20250731_models.SearchInfoResponse:
        """
        @summary /api/v1/sessions
        
        @param request: SearchInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.knowledge_base_filters):
            body['KnowledgeBaseFilters'] = request.knowledge_base_filters
        if not UtilClient.is_unset(request.web_filters):
            body['WebFilters'] = request.web_filters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchInfo',
            version='2025-07-31',
            protocol='HTTPS',
            pathname=f'/api/v1/searches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paicopilot_20250731_models.SearchInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_info_with_options_async(
        self,
        request: paicopilot_20250731_models.SearchInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> paicopilot_20250731_models.SearchInfoResponse:
        """
        @summary /api/v1/sessions
        
        @param request: SearchInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.knowledge_base_filters):
            body['KnowledgeBaseFilters'] = request.knowledge_base_filters
        if not UtilClient.is_unset(request.web_filters):
            body['WebFilters'] = request.web_filters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchInfo',
            version='2025-07-31',
            protocol='HTTPS',
            pathname=f'/api/v1/searches',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            paicopilot_20250731_models.SearchInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_info(
        self,
        request: paicopilot_20250731_models.SearchInfoRequest,
    ) -> paicopilot_20250731_models.SearchInfoResponse:
        """
        @summary /api/v1/sessions
        
        @param request: SearchInfoRequest
        @return: SearchInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_info_with_options(request, headers, runtime)

    async def search_info_async(
        self,
        request: paicopilot_20250731_models.SearchInfoRequest,
    ) -> paicopilot_20250731_models.SearchInfoResponse:
        """
        @summary /api/v1/sessions
        
        @param request: SearchInfoRequest
        @return: SearchInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_info_with_options_async(request, headers, runtime)
