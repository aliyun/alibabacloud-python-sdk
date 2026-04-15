# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_documentparseservice20260414 import models as main_models
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
        self._endpoint = self.get_endpoint('documentparseservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def document_parse_test_api_with_options(
        self,
        request: main_models.DocumentParseTestApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DocumentParseTestApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_url):
            body['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DocumentParseTestApi',
            version = '2026-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DocumentParseTestApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def document_parse_test_api_with_options_async(
        self,
        request: main_models.DocumentParseTestApiRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DocumentParseTestApiResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.image_url):
            body['ImageUrl'] = request.image_url
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DocumentParseTestApi',
            version = '2026-04-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DocumentParseTestApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def document_parse_test_api(
        self,
        request: main_models.DocumentParseTestApiRequest,
    ) -> main_models.DocumentParseTestApiResponse:
        runtime = RuntimeOptions()
        return self.document_parse_test_api_with_options(request, runtime)

    async def document_parse_test_api_async(
        self,
        request: main_models.DocumentParseTestApiRequest,
    ) -> main_models.DocumentParseTestApiResponse:
        runtime = RuntimeOptions()
        return await self.document_parse_test_api_with_options_async(request, runtime)
