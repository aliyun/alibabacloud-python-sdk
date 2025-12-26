# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_paicopilot20250731 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def search_info_with_options(
        self,
        request: main_models.SearchInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.knowledge_base_filters):
            body['KnowledgeBaseFilters'] = request.knowledge_base_filters
        if not DaraCore.is_null(request.web_filters):
            body['WebFilters'] = request.web_filters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchInfo',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/searches',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_info_with_options_async(
        self,
        request: main_models.SearchInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchInfoResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.knowledge_base_filters):
            body['KnowledgeBaseFilters'] = request.knowledge_base_filters
        if not DaraCore.is_null(request.web_filters):
            body['WebFilters'] = request.web_filters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchInfo',
            version = '2025-07-31',
            protocol = 'HTTPS',
            pathname = f'/api/v1/searches',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_info(
        self,
        request: main_models.SearchInfoRequest,
    ) -> main_models.SearchInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_info_with_options(request, headers, runtime)

    async def search_info_async(
        self,
        request: main_models.SearchInfoRequest,
    ) -> main_models.SearchInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_info_with_options_async(request, headers, runtime)
