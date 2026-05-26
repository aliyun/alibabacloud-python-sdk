# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_aisearchengine20260417 import models as main_models
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
        self._endpoint = self.get_endpoint('aisearchengine', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def engine_search_with_options(
        self,
        request: main_models.EngineSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EngineSearchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.grey):
            body['grey'] = request.grey
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.recall):
            body['recall'] = request.recall
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.strategy_id):
            body['strategyId'] = request.strategy_id
        if not DaraCore.is_null(request.user):
            body['user'] = request.user
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EngineSearch',
            version = '2026-04-17',
            protocol = 'HTTPS',
            pathname = f'/api/v1/platform/app/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EngineSearchResponse(),
            self.call_api(params, req, runtime)
        )

    async def engine_search_with_options_async(
        self,
        request: main_models.EngineSearchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EngineSearchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.grey):
            body['grey'] = request.grey
        if not DaraCore.is_null(request.query):
            body['query'] = request.query
        if not DaraCore.is_null(request.recall):
            body['recall'] = request.recall
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        if not DaraCore.is_null(request.strategy_id):
            body['strategyId'] = request.strategy_id
        if not DaraCore.is_null(request.user):
            body['user'] = request.user
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'EngineSearch',
            version = '2026-04-17',
            protocol = 'HTTPS',
            pathname = f'/api/v1/platform/app/search',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EngineSearchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def engine_search(
        self,
        request: main_models.EngineSearchRequest,
    ) -> main_models.EngineSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.engine_search_with_options(request, headers, runtime)

    async def engine_search_async(
        self,
        request: main_models.EngineSearchRequest,
    ) -> main_models.EngineSearchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.engine_search_with_options_async(request, headers, runtime)

    def get_dataset_resource_url_with_options(
        self,
        request: main_models.GetDatasetResourceUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResourceUrlResponse:
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
            action = 'GetDatasetResourceUrl',
            version = '2026-04-17',
            protocol = 'HTTPS',
            pathname = f'/api/v1/dataset/open/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResourceUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_resource_url_with_options_async(
        self,
        request: main_models.GetDatasetResourceUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResourceUrlResponse:
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
            action = 'GetDatasetResourceUrl',
            version = '2026-04-17',
            protocol = 'HTTPS',
            pathname = f'/api/v1/dataset/open/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResourceUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset_resource_url(
        self,
        request: main_models.GetDatasetResourceUrlRequest,
    ) -> main_models.GetDatasetResourceUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_dataset_resource_url_with_options(request, headers, runtime)

    async def get_dataset_resource_url_async(
        self,
        request: main_models.GetDatasetResourceUrlRequest,
    ) -> main_models.GetDatasetResourceUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_dataset_resource_url_with_options_async(request, headers, runtime)

    def import_dataset_data_with_options(
        self,
        request: main_models.ImportDatasetDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ImportDatasetDataResponse:
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
            action = 'ImportDatasetData',
            version = '2026-04-17',
            protocol = 'HTTPS',
            pathname = f'/api/v1/dataset/open/upsert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportDatasetDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_dataset_data_with_options_async(
        self,
        request: main_models.ImportDatasetDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ImportDatasetDataResponse:
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
            action = 'ImportDatasetData',
            version = '2026-04-17',
            protocol = 'HTTPS',
            pathname = f'/api/v1/dataset/open/upsert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportDatasetDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_dataset_data(
        self,
        request: main_models.ImportDatasetDataRequest,
    ) -> main_models.ImportDatasetDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.import_dataset_data_with_options(request, headers, runtime)

    async def import_dataset_data_async(
        self,
        request: main_models.ImportDatasetDataRequest,
    ) -> main_models.ImportDatasetDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.import_dataset_data_with_options_async(request, headers, runtime)

    def qa_chat_with_sse(
        self,
        request: main_models.QaChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.QaChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.message):
            body['message'] = request.message
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QaChat',
            version = '2026-04-17',
            protocol = 'HTTPS',
            pathname = f'/api/v1/platform/app/chat',
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
                    main_models.QaChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def qa_chat_with_sse_async(
        self,
        request: main_models.QaChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.QaChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.message):
            body['message'] = request.message
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QaChat',
            version = '2026-04-17',
            protocol = 'HTTPS',
            pathname = f'/api/v1/platform/app/chat',
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
                    main_models.QaChatResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def qa_chat_with_options(
        self,
        request: main_models.QaChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QaChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.message):
            body['message'] = request.message
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QaChat',
            version = '2026-04-17',
            protocol = 'HTTPS',
            pathname = f'/api/v1/platform/app/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QaChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def qa_chat_with_options_async(
        self,
        request: main_models.QaChatRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QaChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.app_id):
            body['appId'] = request.app_id
        if not DaraCore.is_null(request.message):
            body['message'] = request.message
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        if not DaraCore.is_null(request.session_id):
            body['sessionId'] = request.session_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QaChat',
            version = '2026-04-17',
            protocol = 'HTTPS',
            pathname = f'/api/v1/platform/app/chat',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QaChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def qa_chat(
        self,
        request: main_models.QaChatRequest,
    ) -> main_models.QaChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.qa_chat_with_options(request, headers, runtime)

    async def qa_chat_async(
        self,
        request: main_models.QaChatRequest,
    ) -> main_models.QaChatResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.qa_chat_with_options_async(request, headers, runtime)
