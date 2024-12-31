# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bss20140714 import models as bss_20140714_models
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
        self._endpoint = self.get_endpoint('bss', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: bss_20140714_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_20140714_models.CreateOrderResponse:
        """
        @param request: CreateOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_str):
            query['paramStr'] = request.param_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2014-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_20140714_models.CreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: bss_20140714_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_20140714_models.CreateOrderResponse:
        """
        @param request: CreateOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_str):
            query['paramStr'] = request.param_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2014-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_20140714_models.CreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order(
        self,
        request: bss_20140714_models.CreateOrderRequest,
    ) -> bss_20140714_models.CreateOrderResponse:
        """
        @param request: CreateOrderRequest
        @return: CreateOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    async def create_order_async(
        self,
        request: bss_20140714_models.CreateOrderRequest,
    ) -> bss_20140714_models.CreateOrderResponse:
        """
        @param request: CreateOrderRequest
        @return: CreateOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_order_with_options_async(request, runtime)

    def describe_cash_detail_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bss_20140714_models.DescribeCashDetailResponse:
        """
        @summary 获取现金明细
        
        @param request: DescribeCashDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCashDetailResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCashDetail',
            version='2014-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_20140714_models.DescribeCashDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cash_detail_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bss_20140714_models.DescribeCashDetailResponse:
        """
        @summary 获取现金明细
        
        @param request: DescribeCashDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCashDetailResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeCashDetail',
            version='2014-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_20140714_models.DescribeCashDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cash_detail(self) -> bss_20140714_models.DescribeCashDetailResponse:
        """
        @summary 获取现金明细
        
        @return: DescribeCashDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cash_detail_with_options(runtime)

    async def describe_cash_detail_async(self) -> bss_20140714_models.DescribeCashDetailResponse:
        """
        @summary 获取现金明细
        
        @return: DescribeCashDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cash_detail_with_options_async(runtime)

    def describe_coupon_list_with_options(
        self,
        request: bss_20140714_models.DescribeCouponListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_20140714_models.DescribeCouponListResponse:
        """
        @param request: DescribeCouponListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCouponListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_delivery_time):
            query['EndDeliveryTime'] = request.end_delivery_time
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_delivery_time):
            query['StartDeliveryTime'] = request.start_delivery_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCouponList',
            version='2014-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_20140714_models.DescribeCouponListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_coupon_list_with_options_async(
        self,
        request: bss_20140714_models.DescribeCouponListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_20140714_models.DescribeCouponListResponse:
        """
        @param request: DescribeCouponListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCouponListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_delivery_time):
            query['EndDeliveryTime'] = request.end_delivery_time
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_delivery_time):
            query['StartDeliveryTime'] = request.start_delivery_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCouponList',
            version='2014-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_20140714_models.DescribeCouponListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_coupon_list(
        self,
        request: bss_20140714_models.DescribeCouponListRequest,
    ) -> bss_20140714_models.DescribeCouponListResponse:
        """
        @param request: DescribeCouponListRequest
        @return: DescribeCouponListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_coupon_list_with_options(request, runtime)

    async def describe_coupon_list_async(
        self,
        request: bss_20140714_models.DescribeCouponListRequest,
    ) -> bss_20140714_models.DescribeCouponListResponse:
        """
        @param request: DescribeCouponListRequest
        @return: DescribeCouponListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_coupon_list_with_options_async(request, runtime)

    def open_callback_with_options(
        self,
        request: bss_20140714_models.OpenCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_20140714_models.OpenCallbackResponse:
        """
        @summary OpenCallback
        
        @param request: OpenCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_str):
            query['paramStr'] = request.param_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenCallback',
            version='2014-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_20140714_models.OpenCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_callback_with_options_async(
        self,
        request: bss_20140714_models.OpenCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_20140714_models.OpenCallbackResponse:
        """
        @summary OpenCallback
        
        @param request: OpenCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_str):
            query['paramStr'] = request.param_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenCallback',
            version='2014-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_20140714_models.OpenCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_callback(
        self,
        request: bss_20140714_models.OpenCallbackRequest,
    ) -> bss_20140714_models.OpenCallbackResponse:
        """
        @summary OpenCallback
        
        @param request: OpenCallbackRequest
        @return: OpenCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_callback_with_options(request, runtime)

    async def open_callback_async(
        self,
        request: bss_20140714_models.OpenCallbackRequest,
    ) -> bss_20140714_models.OpenCallbackResponse:
        """
        @summary OpenCallback
        
        @param request: OpenCallbackRequest
        @return: OpenCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_callback_with_options_async(request, runtime)

    def query_for_css_order_with_options(
        self,
        request: bss_20140714_models.QueryForCssOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_20140714_models.QueryForCssOrderResponse:
        """
        @param request: QueryForCssOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryForCssOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_str):
            query['paramStr'] = request.param_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryForCssOrder',
            version='2014-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_20140714_models.QueryForCssOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_for_css_order_with_options_async(
        self,
        request: bss_20140714_models.QueryForCssOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_20140714_models.QueryForCssOrderResponse:
        """
        @param request: QueryForCssOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryForCssOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_str):
            query['paramStr'] = request.param_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryForCssOrder',
            version='2014-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_20140714_models.QueryForCssOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_for_css_order(
        self,
        request: bss_20140714_models.QueryForCssOrderRequest,
    ) -> bss_20140714_models.QueryForCssOrderResponse:
        """
        @param request: QueryForCssOrderRequest
        @return: QueryForCssOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_for_css_order_with_options(request, runtime)

    async def query_for_css_order_async(
        self,
        request: bss_20140714_models.QueryForCssOrderRequest,
    ) -> bss_20140714_models.QueryForCssOrderResponse:
        """
        @param request: QueryForCssOrderRequest
        @return: QueryForCssOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_for_css_order_with_options_async(request, runtime)

    def vno_batch_refund_order_with_options(
        self,
        request: bss_20140714_models.VnoBatchRefundOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_20140714_models.VnoBatchRefundOrderResponse:
        """
        @param request: VnoBatchRefundOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VnoBatchRefundOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_str):
            query['paramStr'] = request.param_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='vnoBatchRefundOrder',
            version='2014-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_20140714_models.VnoBatchRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def vno_batch_refund_order_with_options_async(
        self,
        request: bss_20140714_models.VnoBatchRefundOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_20140714_models.VnoBatchRefundOrderResponse:
        """
        @param request: VnoBatchRefundOrderRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VnoBatchRefundOrderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.param_str):
            query['paramStr'] = request.param_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='vnoBatchRefundOrder',
            version='2014-07-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_20140714_models.VnoBatchRefundOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vno_batch_refund_order(
        self,
        request: bss_20140714_models.VnoBatchRefundOrderRequest,
    ) -> bss_20140714_models.VnoBatchRefundOrderResponse:
        """
        @param request: VnoBatchRefundOrderRequest
        @return: VnoBatchRefundOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.vno_batch_refund_order_with_options(request, runtime)

    async def vno_batch_refund_order_async(
        self,
        request: bss_20140714_models.VnoBatchRefundOrderRequest,
    ) -> bss_20140714_models.VnoBatchRefundOrderResponse:
        """
        @param request: VnoBatchRefundOrderRequest
        @return: VnoBatchRefundOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.vno_batch_refund_order_with_options_async(request, runtime)
