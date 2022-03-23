# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yuqing20220301 import models as yuqing_20220301_models
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
        self._endpoint = self.get_endpoint('yuqing', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def close_product(
        self,
        request: yuqing_20220301_models.CloseProductRequest,
    ) -> yuqing_20220301_models.CloseProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_product_with_options(request, headers, runtime)

    async def close_product_async(
        self,
        request: yuqing_20220301_models.CloseProductRequest,
    ) -> yuqing_20220301_models.CloseProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.close_product_with_options_async(request, headers, runtime)

    def close_product_with_options(
        self,
        request: yuqing_20220301_models.CloseProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.CloseProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_instance):
            query['productInstance'] = request.product_instance
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseProduct',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/closeProduct.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.CloseProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_product_with_options_async(
        self,
        request: yuqing_20220301_models.CloseProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.CloseProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_instance):
            query['productInstance'] = request.product_instance
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseProduct',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/closeProduct.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.CloseProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def console_proxy(
        self,
        request: yuqing_20220301_models.ConsoleProxyRequest,
    ) -> yuqing_20220301_models.ConsoleProxyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.console_proxy_with_options(request, headers, runtime)

    async def console_proxy_async(
        self,
        request: yuqing_20220301_models.ConsoleProxyRequest,
    ) -> yuqing_20220301_models.ConsoleProxyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.console_proxy_with_options_async(request, headers, runtime)

    def console_proxy_with_options(
        self,
        request: yuqing_20220301_models.ConsoleProxyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.ConsoleProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['appCode'] = request.app_code
        if not UtilClient.is_unset(request.interface_name):
            query['interfaceName'] = request.interface_name
        if not UtilClient.is_unset(request.param_json):
            query['paramJson'] = request.param_json
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConsoleProxy',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/consoleProxy.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.ConsoleProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def console_proxy_with_options_async(
        self,
        request: yuqing_20220301_models.ConsoleProxyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.ConsoleProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['appCode'] = request.app_code
        if not UtilClient.is_unset(request.interface_name):
            query['interfaceName'] = request.interface_name
        if not UtilClient.is_unset(request.param_json):
            query['paramJson'] = request.param_json
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConsoleProxy',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/consoleProxy.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.ConsoleProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_product(
        self,
        request: yuqing_20220301_models.OpenProductRequest,
    ) -> yuqing_20220301_models.OpenProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_product_with_options(request, headers, runtime)

    async def open_product_async(
        self,
        request: yuqing_20220301_models.OpenProductRequest,
    ) -> yuqing_20220301_models.OpenProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.open_product_with_options_async(request, headers, runtime)

    def open_product_with_options(
        self,
        request: yuqing_20220301_models.OpenProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.OpenProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.product_instance):
            query['productInstance'] = request.product_instance
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenProduct',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/openProduct.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.OpenProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_product_with_options_async(
        self,
        request: yuqing_20220301_models.OpenProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.OpenProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.product_instance):
            query['productInstance'] = request.product_instance
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenProduct',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/openProduct.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.OpenProductResponse(),
            await self.call_api_async(params, req, runtime)
        )
