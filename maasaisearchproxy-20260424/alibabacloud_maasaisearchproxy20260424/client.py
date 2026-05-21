# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_maasaisearchproxy20260424 import models as main_models
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
        self._endpoint = self.get_endpoint('maasaisearchproxy', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def open_dataset_import_data_with_options(
        self,
        request: main_models.OpenDatasetImportDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenDatasetImportDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['datasetId'] = request.dataset_id
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OpenDatasetImportData',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = f'/api/v1/dataset/open/upsert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenDatasetImportDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_dataset_import_data_with_options_async(
        self,
        request: main_models.OpenDatasetImportDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenDatasetImportDataResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['datasetId'] = request.dataset_id
        if not DaraCore.is_null(request.records):
            body['records'] = request.records
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OpenDatasetImportData',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = f'/api/v1/dataset/open/upsert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenDatasetImportDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_dataset_import_data(
        self,
        request: main_models.OpenDatasetImportDataRequest,
    ) -> main_models.OpenDatasetImportDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.open_dataset_import_data_with_options(request, headers, runtime)

    async def open_dataset_import_data_async(
        self,
        request: main_models.OpenDatasetImportDataRequest,
    ) -> main_models.OpenDatasetImportDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.open_dataset_import_data_with_options_async(request, headers, runtime)

    def open_dataset_resource_url_with_options(
        self,
        request: main_models.OpenDatasetResourceUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenDatasetResourceUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['datasetId'] = request.dataset_id
        if not DaraCore.is_null(request.primary_key):
            body['primaryKey'] = request.primary_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OpenDatasetResourceUrl',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = f'/api/v1/dataset/open/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenDatasetResourceUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_dataset_resource_url_with_options_async(
        self,
        request: main_models.OpenDatasetResourceUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenDatasetResourceUrlResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.dataset_id):
            body['datasetId'] = request.dataset_id
        if not DaraCore.is_null(request.primary_key):
            body['primaryKey'] = request.primary_key
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'OpenDatasetResourceUrl',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = f'/api/v1/dataset/open/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenDatasetResourceUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_dataset_resource_url(
        self,
        request: main_models.OpenDatasetResourceUrlRequest,
    ) -> main_models.OpenDatasetResourceUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.open_dataset_resource_url_with_options(request, headers, runtime)

    async def open_dataset_resource_url_async(
        self,
        request: main_models.OpenDatasetResourceUrlRequest,
    ) -> main_models.OpenDatasetResourceUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.open_dataset_resource_url_with_options_async(request, headers, runtime)

    def web_search_with_options(
        self,
        request: main_models.WebSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.WebSearchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.exclude_domain):
            body['excludeDomain'] = request.exclude_domain
        if not DaraCore.is_null(request.include_domain):
            body['includeDomain'] = request.include_domain
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        if not DaraCore.is_null(request.search_type):
            body['searchType'] = request.search_type
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'WebSearch',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = f'/api/web-search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WebSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def web_search_with_options_async(
        self,
        request: main_models.WebSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.WebSearchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['endTime'] = request.end_time
        if not DaraCore.is_null(request.exclude_domain):
            body['excludeDomain'] = request.exclude_domain
        if not DaraCore.is_null(request.include_domain):
            body['includeDomain'] = request.include_domain
        if not DaraCore.is_null(request.limit):
            body['limit'] = request.limit
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.region):
            body['region'] = request.region
        if not DaraCore.is_null(request.search_type):
            body['searchType'] = request.search_type
        if not DaraCore.is_null(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'WebSearch',
            version = '2026-04-24',
            protocol = 'HTTPS',
            pathname = f'/api/web-search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WebSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def web_search(
        self,
        request: main_models.WebSearchRequest,
    ) -> main_models.WebSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.web_search_with_options(request, headers, runtime)

    async def web_search_async(
        self,
        request: main_models.WebSearchRequest,
    ) -> main_models.WebSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.web_search_with_options_async(request, headers, runtime)
