# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_internetbankopen20240612 import models as main_models
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
        self._product_id = 'InternetBankOpen'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('internetbankopen', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def invoke_data_product_with_options(
        self,
        request: main_models.InvokeDataProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InvokeDataProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.product_code):
            query['productCode'] = request.product_code
        if not DaraCore.is_null(request.service_parameters):
            query['serviceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeDataProduct',
            version = '2024-06-12',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/rpc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeDataProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def invoke_data_product_with_options_async(
        self,
        request: main_models.InvokeDataProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.InvokeDataProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        if not DaraCore.is_null(request.product_code):
            query['productCode'] = request.product_code
        if not DaraCore.is_null(request.service_parameters):
            query['serviceParameters'] = request.service_parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvokeDataProduct',
            version = '2024-06-12',
            protocol = 'HTTPS',
            pathname = f'/pop/api/v1/rpc',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvokeDataProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invoke_data_product(
        self,
        request: main_models.InvokeDataProductRequest,
    ) -> main_models.InvokeDataProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.invoke_data_product_with_options(request, headers, runtime)

    async def invoke_data_product_async(
        self,
        request: main_models.InvokeDataProductRequest,
    ) -> main_models.InvokeDataProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.invoke_data_product_with_options_async(request, headers, runtime)
