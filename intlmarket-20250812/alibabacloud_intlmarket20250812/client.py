# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_intlmarket20250812 import models as intl_market_20250812_models
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
        self._endpoint = self.get_endpoint('intlmarket', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_order_with_options(
        self,
        request: intl_market_20250812_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> intl_market_20250812_models.CreateOrderResponse:
        """
        @summary 创建云市场订单
        
        @param request: CreateOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.order_souce):
            query['OrderSouce'] = request.order_souce
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2025-08-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            intl_market_20250812_models.CreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: intl_market_20250812_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> intl_market_20250812_models.CreateOrderResponse:
        """
        @summary 创建云市场订单
        
        @param request: CreateOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.order_souce):
            query['OrderSouce'] = request.order_souce
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2025-08-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            intl_market_20250812_models.CreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order(
        self,
        request: intl_market_20250812_models.CreateOrderRequest,
    ) -> intl_market_20250812_models.CreateOrderResponse:
        """
        @summary 创建云市场订单
        
        @param request: CreateOrderRequest
        @return: CreateOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    async def create_order_async(
        self,
        request: intl_market_20250812_models.CreateOrderRequest,
    ) -> intl_market_20250812_models.CreateOrderResponse:
        """
        @summary 创建云市场订单
        
        @param request: CreateOrderRequest
        @return: CreateOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_order_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: intl_market_20250812_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> intl_market_20250812_models.DescribePriceResponse:
        """
        @summary 询价
        
        @param request: DescribePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2025-08-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            intl_market_20250812_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: intl_market_20250812_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> intl_market_20250812_models.DescribePriceResponse:
        """
        @summary 询价
        
        @param request: DescribePriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrice',
            version='2025-08-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            intl_market_20250812_models.DescribePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_price(
        self,
        request: intl_market_20250812_models.DescribePriceRequest,
    ) -> intl_market_20250812_models.DescribePriceResponse:
        """
        @summary 询价
        
        @param request: DescribePriceRequest
        @return: DescribePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: intl_market_20250812_models.DescribePriceRequest,
    ) -> intl_market_20250812_models.DescribePriceResponse:
        """
        @summary 询价
        
        @param request: DescribePriceRequest
        @return: DescribePriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)
