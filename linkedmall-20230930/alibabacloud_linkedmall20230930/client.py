# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_linkedmall20230930 import models as linkedmall_20230930_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-hangzhou': 'linkedmall.aliyuncs.com',
            'cn-shanghai': 'linkedmall.aliyuncs.com',
            'ap-northeast-1': 'linkedmall.aliyuncs.com',
            'ap-northeast-2-pop': 'linkedmall.aliyuncs.com',
            'ap-south-1': 'linkedmall.aliyuncs.com',
            'ap-southeast-1': 'linkedmall.aliyuncs.com',
            'ap-southeast-2': 'linkedmall.aliyuncs.com',
            'ap-southeast-3': 'linkedmall.aliyuncs.com',
            'ap-southeast-5': 'linkedmall.aliyuncs.com',
            'cn-beijing': 'linkedmall.aliyuncs.com',
            'cn-beijing-finance-1': 'linkedmall.aliyuncs.com',
            'cn-beijing-finance-pop': 'linkedmall.aliyuncs.com',
            'cn-beijing-gov-1': 'linkedmall.aliyuncs.com',
            'cn-beijing-nu16-b01': 'linkedmall.aliyuncs.com',
            'cn-chengdu': 'linkedmall.aliyuncs.com',
            'cn-edge-1': 'linkedmall.aliyuncs.com',
            'cn-fujian': 'linkedmall.aliyuncs.com',
            'cn-haidian-cm12-c01': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-finance': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-test-306': 'linkedmall.aliyuncs.com',
            'cn-hongkong': 'linkedmall.aliyuncs.com',
            'cn-hongkong-finance-pop': 'linkedmall.aliyuncs.com',
            'cn-huhehaote': 'linkedmall.aliyuncs.com',
            'cn-north-2-gov-1': 'linkedmall.aliyuncs.com',
            'cn-qingdao': 'linkedmall.aliyuncs.com',
            'cn-qingdao-nebula': 'linkedmall.aliyuncs.com',
            'cn-shanghai-et15-b01': 'linkedmall.aliyuncs.com',
            'cn-shanghai-et2-b01': 'linkedmall.aliyuncs.com',
            'cn-shanghai-finance-1': 'linkedmall.aliyuncs.com',
            'cn-shanghai-inner': 'linkedmall.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'linkedmall.aliyuncs.com',
            'cn-shenzhen': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-finance-1': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-inner': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'linkedmall.aliyuncs.com',
            'cn-wuhan': 'linkedmall.aliyuncs.com',
            'cn-yushanfang': 'linkedmall.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'linkedmall.aliyuncs.com',
            'cn-zhangjiakou': 'linkedmall.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'linkedmall.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'linkedmall.aliyuncs.com',
            'eu-central-1': 'linkedmall.aliyuncs.com',
            'eu-west-1': 'linkedmall.aliyuncs.com',
            'eu-west-1-oxs': 'linkedmall.aliyuncs.com',
            'me-east-1': 'linkedmall.aliyuncs.com',
            'rus-west-1-pop': 'linkedmall.aliyuncs.com',
            'us-east-1': 'linkedmall.aliyuncs.com',
            'us-west-1': 'linkedmall.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('linkedmall', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_refund_order_with_options(
        self,
        dispute_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.CancelRefundOrderResponse:
        """
        @summary 取消逆向单
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelRefundOrderResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelRefundOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/{OpenApiUtilClient.get_encode_param(dispute_id)}/commands/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.CancelRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_refund_order_with_options_async(
        self,
        dispute_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.CancelRefundOrderResponse:
        """
        @summary 取消逆向单
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelRefundOrderResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelRefundOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/{OpenApiUtilClient.get_encode_param(dispute_id)}/commands/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.CancelRefundOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_refund_order(
        self,
        dispute_id: str,
    ) -> linkedmall_20230930_models.CancelRefundOrderResponse:
        """
        @summary 取消逆向单
        
        @return: CancelRefundOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_refund_order_with_options(dispute_id, headers, runtime)

    async def cancel_refund_order_async(
        self,
        dispute_id: str,
    ) -> linkedmall_20230930_models.CancelRefundOrderResponse:
        """
        @summary 取消逆向单
        
        @return: CancelRefundOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_refund_order_with_options_async(dispute_id, headers, runtime)

    def confirm_disburse_with_options(
        self,
        request: linkedmall_20230930_models.ConfirmDisburseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ConfirmDisburseResponse:
        """
        @summary 确认收货（订单）
        
        @param request: ConfirmDisburseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmDisburseResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ConfirmDisburse',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/commands/confirmDisburse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ConfirmDisburseResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_disburse_with_options_async(
        self,
        request: linkedmall_20230930_models.ConfirmDisburseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ConfirmDisburseResponse:
        """
        @summary 确认收货（订单）
        
        @param request: ConfirmDisburseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmDisburseResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ConfirmDisburse',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/commands/confirmDisburse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ConfirmDisburseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_disburse(
        self,
        request: linkedmall_20230930_models.ConfirmDisburseRequest,
    ) -> linkedmall_20230930_models.ConfirmDisburseResponse:
        """
        @summary 确认收货（订单）
        
        @param request: ConfirmDisburseRequest
        @return: ConfirmDisburseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.confirm_disburse_with_options(request, headers, runtime)

    async def confirm_disburse_async(
        self,
        request: linkedmall_20230930_models.ConfirmDisburseRequest,
    ) -> linkedmall_20230930_models.ConfirmDisburseResponse:
        """
        @summary 确认收货（订单）
        
        @param request: ConfirmDisburseRequest
        @return: ConfirmDisburseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.confirm_disburse_with_options_async(request, headers, runtime)

    def create_goods_shipping_notice_with_options(
        self,
        request: linkedmall_20230930_models.CreateGoodsShippingNoticeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.CreateGoodsShippingNoticeResponse:
        """
        @summary 提交运单信息
        
        @param request: CreateGoodsShippingNoticeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGoodsShippingNoticeResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateGoodsShippingNotice',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/command/createGoodsShippingNotice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.CreateGoodsShippingNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_goods_shipping_notice_with_options_async(
        self,
        request: linkedmall_20230930_models.CreateGoodsShippingNoticeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.CreateGoodsShippingNoticeResponse:
        """
        @summary 提交运单信息
        
        @param request: CreateGoodsShippingNoticeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGoodsShippingNoticeResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateGoodsShippingNotice',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/command/createGoodsShippingNotice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.CreateGoodsShippingNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_goods_shipping_notice(
        self,
        request: linkedmall_20230930_models.CreateGoodsShippingNoticeRequest,
    ) -> linkedmall_20230930_models.CreateGoodsShippingNoticeResponse:
        """
        @summary 提交运单信息
        
        @param request: CreateGoodsShippingNoticeRequest
        @return: CreateGoodsShippingNoticeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_goods_shipping_notice_with_options(request, headers, runtime)

    async def create_goods_shipping_notice_async(
        self,
        request: linkedmall_20230930_models.CreateGoodsShippingNoticeRequest,
    ) -> linkedmall_20230930_models.CreateGoodsShippingNoticeResponse:
        """
        @summary 提交运单信息
        
        @param request: CreateGoodsShippingNoticeRequest
        @return: CreateGoodsShippingNoticeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_goods_shipping_notice_with_options_async(request, headers, runtime)

    def create_purchase_order_with_options(
        self,
        request: linkedmall_20230930_models.CreatePurchaseOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.CreatePurchaseOrderResponse:
        """
        @summary 创建采购单
        
        @param request: CreatePurchaseOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePurchaseOrderResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePurchaseOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.CreatePurchaseOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_purchase_order_with_options_async(
        self,
        request: linkedmall_20230930_models.CreatePurchaseOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.CreatePurchaseOrderResponse:
        """
        @summary 创建采购单
        
        @param request: CreatePurchaseOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePurchaseOrderResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreatePurchaseOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.CreatePurchaseOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_purchase_order(
        self,
        request: linkedmall_20230930_models.CreatePurchaseOrderRequest,
    ) -> linkedmall_20230930_models.CreatePurchaseOrderResponse:
        """
        @summary 创建采购单
        
        @param request: CreatePurchaseOrderRequest
        @return: CreatePurchaseOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_purchase_order_with_options(request, headers, runtime)

    async def create_purchase_order_async(
        self,
        request: linkedmall_20230930_models.CreatePurchaseOrderRequest,
    ) -> linkedmall_20230930_models.CreatePurchaseOrderResponse:
        """
        @summary 创建采购单
        
        @param request: CreatePurchaseOrderRequest
        @return: CreatePurchaseOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_purchase_order_with_options_async(request, headers, runtime)

    def create_refund_order_with_options(
        self,
        request: linkedmall_20230930_models.CreateRefundOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.CreateRefundOrderResponse:
        """
        @summary 创建逆向单
        
        @param request: CreateRefundOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRefundOrderResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateRefundOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.CreateRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_refund_order_with_options_async(
        self,
        request: linkedmall_20230930_models.CreateRefundOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.CreateRefundOrderResponse:
        """
        @summary 创建逆向单
        
        @param request: CreateRefundOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRefundOrderResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateRefundOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.CreateRefundOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_refund_order(
        self,
        request: linkedmall_20230930_models.CreateRefundOrderRequest,
    ) -> linkedmall_20230930_models.CreateRefundOrderResponse:
        """
        @summary 创建逆向单
        
        @param request: CreateRefundOrderRequest
        @return: CreateRefundOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_refund_order_with_options(request, headers, runtime)

    async def create_refund_order_async(
        self,
        request: linkedmall_20230930_models.CreateRefundOrderRequest,
    ) -> linkedmall_20230930_models.CreateRefundOrderResponse:
        """
        @summary 创建逆向单
        
        @param request: CreateRefundOrderRequest
        @return: CreateRefundOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_refund_order_with_options_async(request, headers, runtime)

    def get_order_with_options(
        self,
        order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.GetOrderResponse:
        """
        @summary 查询主单详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrderResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/{OpenApiUtilClient.get_encode_param(order_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_order_with_options_async(
        self,
        order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.GetOrderResponse:
        """
        @summary 查询主单详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrderResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/{OpenApiUtilClient.get_encode_param(order_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_order(
        self,
        order_id: str,
    ) -> linkedmall_20230930_models.GetOrderResponse:
        """
        @summary 查询主单详情
        
        @return: GetOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_order_with_options(order_id, headers, runtime)

    async def get_order_async(
        self,
        order_id: str,
    ) -> linkedmall_20230930_models.GetOrderResponse:
        """
        @summary 查询主单详情
        
        @return: GetOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_order_with_options_async(order_id, headers, runtime)

    def get_purchase_order_status_with_options(
        self,
        purchase_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.GetPurchaseOrderStatusResponse:
        """
        @summary 查询采购单状态
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPurchaseOrderStatusResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPurchaseOrderStatus',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/{OpenApiUtilClient.get_encode_param(purchase_order_id)}/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetPurchaseOrderStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_purchase_order_status_with_options_async(
        self,
        purchase_order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.GetPurchaseOrderStatusResponse:
        """
        @summary 查询采购单状态
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPurchaseOrderStatusResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPurchaseOrderStatus',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/{OpenApiUtilClient.get_encode_param(purchase_order_id)}/status',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetPurchaseOrderStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_purchase_order_status(
        self,
        purchase_order_id: str,
    ) -> linkedmall_20230930_models.GetPurchaseOrderStatusResponse:
        """
        @summary 查询采购单状态
        
        @return: GetPurchaseOrderStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_purchase_order_status_with_options(purchase_order_id, headers, runtime)

    async def get_purchase_order_status_async(
        self,
        purchase_order_id: str,
    ) -> linkedmall_20230930_models.GetPurchaseOrderStatusResponse:
        """
        @summary 查询采购单状态
        
        @return: GetPurchaseOrderStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_purchase_order_status_with_options_async(purchase_order_id, headers, runtime)

    def get_purchaser_shop_with_options(
        self,
        purchaser_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.GetPurchaserShopResponse:
        """
        @summary 查询分销商店铺
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPurchaserShopResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPurchaserShop',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaserShops/{OpenApiUtilClient.get_encode_param(purchaser_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetPurchaserShopResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_purchaser_shop_with_options_async(
        self,
        purchaser_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.GetPurchaserShopResponse:
        """
        @summary 查询分销商店铺
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPurchaserShopResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetPurchaserShop',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaserShops/{OpenApiUtilClient.get_encode_param(purchaser_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetPurchaserShopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_purchaser_shop(
        self,
        purchaser_id: str,
    ) -> linkedmall_20230930_models.GetPurchaserShopResponse:
        """
        @summary 查询分销商店铺
        
        @return: GetPurchaserShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_purchaser_shop_with_options(purchaser_id, headers, runtime)

    async def get_purchaser_shop_async(
        self,
        purchaser_id: str,
    ) -> linkedmall_20230930_models.GetPurchaserShopResponse:
        """
        @summary 查询分销商店铺
        
        @return: GetPurchaserShopResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_purchaser_shop_with_options_async(purchaser_id, headers, runtime)

    def get_refund_order_with_options(
        self,
        dispute_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.GetRefundOrderResponse:
        """
        @summary 查询逆向单详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRefundOrderResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRefundOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/{OpenApiUtilClient.get_encode_param(dispute_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_refund_order_with_options_async(
        self,
        dispute_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.GetRefundOrderResponse:
        """
        @summary 查询逆向单详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRefundOrderResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRefundOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/{OpenApiUtilClient.get_encode_param(dispute_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetRefundOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_refund_order(
        self,
        dispute_id: str,
    ) -> linkedmall_20230930_models.GetRefundOrderResponse:
        """
        @summary 查询逆向单详情
        
        @return: GetRefundOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_refund_order_with_options(dispute_id, headers, runtime)

    async def get_refund_order_async(
        self,
        dispute_id: str,
    ) -> linkedmall_20230930_models.GetRefundOrderResponse:
        """
        @summary 查询逆向单详情
        
        @return: GetRefundOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_refund_order_with_options_async(dispute_id, headers, runtime)

    def get_selection_product_with_options(
        self,
        product_id: str,
        request: linkedmall_20230930_models.GetSelectionProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.GetSelectionProductResponse:
        """
        @summary 查询选品池商品详情
        
        @param request: GetSelectionProductRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSelectionProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.division_code):
            query['divisionCode'] = request.division_code
        if not UtilClient.is_unset(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSelectionProduct',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/{OpenApiUtilClient.get_encode_param(product_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetSelectionProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_selection_product_with_options_async(
        self,
        product_id: str,
        request: linkedmall_20230930_models.GetSelectionProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.GetSelectionProductResponse:
        """
        @summary 查询选品池商品详情
        
        @param request: GetSelectionProductRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSelectionProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.division_code):
            query['divisionCode'] = request.division_code
        if not UtilClient.is_unset(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSelectionProduct',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/{OpenApiUtilClient.get_encode_param(product_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetSelectionProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_selection_product(
        self,
        product_id: str,
        request: linkedmall_20230930_models.GetSelectionProductRequest,
    ) -> linkedmall_20230930_models.GetSelectionProductResponse:
        """
        @summary 查询选品池商品详情
        
        @param request: GetSelectionProductRequest
        @return: GetSelectionProductResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_selection_product_with_options(product_id, request, headers, runtime)

    async def get_selection_product_async(
        self,
        product_id: str,
        request: linkedmall_20230930_models.GetSelectionProductRequest,
    ) -> linkedmall_20230930_models.GetSelectionProductResponse:
        """
        @summary 查询选品池商品详情
        
        @param request: GetSelectionProductRequest
        @return: GetSelectionProductResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_selection_product_with_options_async(product_id, request, headers, runtime)

    def get_selection_product_sale_info_with_options(
        self,
        product_id: str,
        request: linkedmall_20230930_models.GetSelectionProductSaleInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.GetSelectionProductSaleInfoResponse:
        """
        @summary 查询选品池商品库存
        
        @param request: GetSelectionProductSaleInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSelectionProductSaleInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.division_code):
            query['divisionCode'] = request.division_code
        if not UtilClient.is_unset(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSelectionProductSaleInfo',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/{OpenApiUtilClient.get_encode_param(product_id)}/saleInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetSelectionProductSaleInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_selection_product_sale_info_with_options_async(
        self,
        product_id: str,
        request: linkedmall_20230930_models.GetSelectionProductSaleInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.GetSelectionProductSaleInfoResponse:
        """
        @summary 查询选品池商品库存
        
        @param request: GetSelectionProductSaleInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSelectionProductSaleInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.division_code):
            query['divisionCode'] = request.division_code
        if not UtilClient.is_unset(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSelectionProductSaleInfo',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/{OpenApiUtilClient.get_encode_param(product_id)}/saleInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.GetSelectionProductSaleInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_selection_product_sale_info(
        self,
        product_id: str,
        request: linkedmall_20230930_models.GetSelectionProductSaleInfoRequest,
    ) -> linkedmall_20230930_models.GetSelectionProductSaleInfoResponse:
        """
        @summary 查询选品池商品库存
        
        @param request: GetSelectionProductSaleInfoRequest
        @return: GetSelectionProductSaleInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_selection_product_sale_info_with_options(product_id, request, headers, runtime)

    async def get_selection_product_sale_info_async(
        self,
        product_id: str,
        request: linkedmall_20230930_models.GetSelectionProductSaleInfoRequest,
    ) -> linkedmall_20230930_models.GetSelectionProductSaleInfoResponse:
        """
        @summary 查询选品池商品库存
        
        @param request: GetSelectionProductSaleInfoRequest
        @return: GetSelectionProductSaleInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_selection_product_sale_info_with_options_async(product_id, request, headers, runtime)

    def list_categories_with_options(
        self,
        request: linkedmall_20230930_models.ListCategoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ListCategoriesResponse:
        """
        @summary 查询类目
        
        @param request: ListCategoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCategoriesResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ListCategories',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/categories/commands/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_categories_with_options_async(
        self,
        request: linkedmall_20230930_models.ListCategoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ListCategoriesResponse:
        """
        @summary 查询类目
        
        @param request: ListCategoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCategoriesResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ListCategories',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/categories/commands/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_categories(
        self,
        request: linkedmall_20230930_models.ListCategoriesRequest,
    ) -> linkedmall_20230930_models.ListCategoriesResponse:
        """
        @summary 查询类目
        
        @param request: ListCategoriesRequest
        @return: ListCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_categories_with_options(request, headers, runtime)

    async def list_categories_async(
        self,
        request: linkedmall_20230930_models.ListCategoriesRequest,
    ) -> linkedmall_20230930_models.ListCategoriesResponse:
        """
        @summary 查询类目
        
        @param request: ListCategoriesRequest
        @return: ListCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_categories_with_options_async(request, headers, runtime)

    def list_logistics_orders_with_options(
        self,
        order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ListLogisticsOrdersResponse:
        """
        @summary 查询物流信息（订单）
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogisticsOrdersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListLogisticsOrders',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/{OpenApiUtilClient.get_encode_param(order_id)}/logisticsOrders',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListLogisticsOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logistics_orders_with_options_async(
        self,
        order_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ListLogisticsOrdersResponse:
        """
        @summary 查询物流信息（订单）
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLogisticsOrdersResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListLogisticsOrders',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/{OpenApiUtilClient.get_encode_param(order_id)}/logisticsOrders',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListLogisticsOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_logistics_orders(
        self,
        order_id: str,
    ) -> linkedmall_20230930_models.ListLogisticsOrdersResponse:
        """
        @summary 查询物流信息（订单）
        
        @return: ListLogisticsOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_logistics_orders_with_options(order_id, headers, runtime)

    async def list_logistics_orders_async(
        self,
        order_id: str,
    ) -> linkedmall_20230930_models.ListLogisticsOrdersResponse:
        """
        @summary 查询物流信息（订单）
        
        @return: ListLogisticsOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_logistics_orders_with_options_async(order_id, headers, runtime)

    def list_purchaser_shops_with_options(
        self,
        request: linkedmall_20230930_models.ListPurchaserShopsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ListPurchaserShopsResponse:
        """
        @summary 采购方店铺列表查询
        
        @param request: ListPurchaserShopsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPurchaserShopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPurchaserShops',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaserShops',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListPurchaserShopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_purchaser_shops_with_options_async(
        self,
        request: linkedmall_20230930_models.ListPurchaserShopsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ListPurchaserShopsResponse:
        """
        @summary 采购方店铺列表查询
        
        @param request: ListPurchaserShopsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPurchaserShopsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPurchaserShops',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaserShops',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListPurchaserShopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_purchaser_shops(
        self,
        request: linkedmall_20230930_models.ListPurchaserShopsRequest,
    ) -> linkedmall_20230930_models.ListPurchaserShopsResponse:
        """
        @summary 采购方店铺列表查询
        
        @param request: ListPurchaserShopsRequest
        @return: ListPurchaserShopsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_purchaser_shops_with_options(request, headers, runtime)

    async def list_purchaser_shops_async(
        self,
        request: linkedmall_20230930_models.ListPurchaserShopsRequest,
    ) -> linkedmall_20230930_models.ListPurchaserShopsResponse:
        """
        @summary 采购方店铺列表查询
        
        @param request: ListPurchaserShopsRequest
        @return: ListPurchaserShopsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_purchaser_shops_with_options_async(request, headers, runtime)

    def list_selection_product_sale_infos_with_options(
        self,
        request: linkedmall_20230930_models.ListSelectionProductSaleInfosRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ListSelectionProductSaleInfosResponse:
        """
        @summary 批量查询选品池商品库存
        
        @param request: ListSelectionProductSaleInfosRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSelectionProductSaleInfosResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ListSelectionProductSaleInfos',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/saleInfo/commands/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListSelectionProductSaleInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_selection_product_sale_infos_with_options_async(
        self,
        request: linkedmall_20230930_models.ListSelectionProductSaleInfosRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ListSelectionProductSaleInfosResponse:
        """
        @summary 批量查询选品池商品库存
        
        @param request: ListSelectionProductSaleInfosRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSelectionProductSaleInfosResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ListSelectionProductSaleInfos',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/saleInfo/commands/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListSelectionProductSaleInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_selection_product_sale_infos(
        self,
        request: linkedmall_20230930_models.ListSelectionProductSaleInfosRequest,
    ) -> linkedmall_20230930_models.ListSelectionProductSaleInfosResponse:
        """
        @summary 批量查询选品池商品库存
        
        @param request: ListSelectionProductSaleInfosRequest
        @return: ListSelectionProductSaleInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_selection_product_sale_infos_with_options(request, headers, runtime)

    async def list_selection_product_sale_infos_async(
        self,
        request: linkedmall_20230930_models.ListSelectionProductSaleInfosRequest,
    ) -> linkedmall_20230930_models.ListSelectionProductSaleInfosResponse:
        """
        @summary 批量查询选品池商品库存
        
        @param request: ListSelectionProductSaleInfosRequest
        @return: ListSelectionProductSaleInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_selection_product_sale_infos_with_options_async(request, headers, runtime)

    def list_selection_products_with_options(
        self,
        request: linkedmall_20230930_models.ListSelectionProductsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ListSelectionProductsResponse:
        """
        @summary 查询商品列表
        
        @param request: ListSelectionProductsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSelectionProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSelectionProducts',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListSelectionProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_selection_products_with_options_async(
        self,
        request: linkedmall_20230930_models.ListSelectionProductsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ListSelectionProductsResponse:
        """
        @summary 查询商品列表
        
        @param request: ListSelectionProductsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSelectionProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSelectionProducts',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListSelectionProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_selection_products(
        self,
        request: linkedmall_20230930_models.ListSelectionProductsRequest,
    ) -> linkedmall_20230930_models.ListSelectionProductsResponse:
        """
        @summary 查询商品列表
        
        @param request: ListSelectionProductsRequest
        @return: ListSelectionProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_selection_products_with_options(request, headers, runtime)

    async def list_selection_products_async(
        self,
        request: linkedmall_20230930_models.ListSelectionProductsRequest,
    ) -> linkedmall_20230930_models.ListSelectionProductsResponse:
        """
        @summary 查询商品列表
        
        @param request: ListSelectionProductsRequest
        @return: ListSelectionProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_selection_products_with_options_async(request, headers, runtime)

    def list_selection_sku_sale_infos_with_options(
        self,
        request: linkedmall_20230930_models.ListSelectionSkuSaleInfosRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ListSelectionSkuSaleInfosResponse:
        """
        @summary 批量查询选品池商品SKU库存
        
        @param request: ListSelectionSkuSaleInfosRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSelectionSkuSaleInfosResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ListSelectionSkuSaleInfos',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/skus/saleInfo/commands/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListSelectionSkuSaleInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_selection_sku_sale_infos_with_options_async(
        self,
        request: linkedmall_20230930_models.ListSelectionSkuSaleInfosRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.ListSelectionSkuSaleInfosResponse:
        """
        @summary 批量查询选品池商品SKU库存
        
        @param request: ListSelectionSkuSaleInfosRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSelectionSkuSaleInfosResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='ListSelectionSkuSaleInfos',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/skus/saleInfo/commands/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.ListSelectionSkuSaleInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_selection_sku_sale_infos(
        self,
        request: linkedmall_20230930_models.ListSelectionSkuSaleInfosRequest,
    ) -> linkedmall_20230930_models.ListSelectionSkuSaleInfosResponse:
        """
        @summary 批量查询选品池商品SKU库存
        
        @param request: ListSelectionSkuSaleInfosRequest
        @return: ListSelectionSkuSaleInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_selection_sku_sale_infos_with_options(request, headers, runtime)

    async def list_selection_sku_sale_infos_async(
        self,
        request: linkedmall_20230930_models.ListSelectionSkuSaleInfosRequest,
    ) -> linkedmall_20230930_models.ListSelectionSkuSaleInfosResponse:
        """
        @summary 批量查询选品池商品SKU库存
        
        @param request: ListSelectionSkuSaleInfosRequest
        @return: ListSelectionSkuSaleInfosResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_selection_sku_sale_infos_with_options_async(request, headers, runtime)

    def query_child_division_code_with_options(
        self,
        request: linkedmall_20230930_models.QueryChildDivisionCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.QueryChildDivisionCodeResponse:
        """
        @summary 查询地址divisionCode
        
        @param request: QueryChildDivisionCodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryChildDivisionCodeResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryChildDivisionCode',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/division/commands/queryChildDivisionCode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.QueryChildDivisionCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_child_division_code_with_options_async(
        self,
        request: linkedmall_20230930_models.QueryChildDivisionCodeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.QueryChildDivisionCodeResponse:
        """
        @summary 查询地址divisionCode
        
        @param request: QueryChildDivisionCodeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryChildDivisionCodeResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryChildDivisionCode',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/division/commands/queryChildDivisionCode',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.QueryChildDivisionCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_child_division_code(
        self,
        request: linkedmall_20230930_models.QueryChildDivisionCodeRequest,
    ) -> linkedmall_20230930_models.QueryChildDivisionCodeResponse:
        """
        @summary 查询地址divisionCode
        
        @param request: QueryChildDivisionCodeRequest
        @return: QueryChildDivisionCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_child_division_code_with_options(request, headers, runtime)

    async def query_child_division_code_async(
        self,
        request: linkedmall_20230930_models.QueryChildDivisionCodeRequest,
    ) -> linkedmall_20230930_models.QueryChildDivisionCodeResponse:
        """
        @summary 查询地址divisionCode
        
        @param request: QueryChildDivisionCodeRequest
        @return: QueryChildDivisionCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_child_division_code_with_options_async(request, headers, runtime)

    def query_orders_with_options(
        self,
        request: linkedmall_20230930_models.QueryOrdersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.QueryOrdersResponse:
        """
        @summary 查询主单列表
        
        @param request: QueryOrdersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOrdersResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryOrders',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/commands/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.QueryOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_orders_with_options_async(
        self,
        request: linkedmall_20230930_models.QueryOrdersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.QueryOrdersResponse:
        """
        @summary 查询主单列表
        
        @param request: QueryOrdersRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryOrdersResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='QueryOrders',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/commands/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.QueryOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_orders(
        self,
        request: linkedmall_20230930_models.QueryOrdersRequest,
    ) -> linkedmall_20230930_models.QueryOrdersResponse:
        """
        @summary 查询主单列表
        
        @param request: QueryOrdersRequest
        @return: QueryOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_orders_with_options(request, headers, runtime)

    async def query_orders_async(
        self,
        request: linkedmall_20230930_models.QueryOrdersRequest,
    ) -> linkedmall_20230930_models.QueryOrdersResponse:
        """
        @summary 查询主单列表
        
        @param request: QueryOrdersRequest
        @return: QueryOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_orders_with_options_async(request, headers, runtime)

    def render_purchase_order_with_options(
        self,
        request: linkedmall_20230930_models.RenderPurchaseOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.RenderPurchaseOrderResponse:
        """
        @summary 渲染采购单
        
        @param request: RenderPurchaseOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenderPurchaseOrderResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='RenderPurchaseOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/commands/render',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.RenderPurchaseOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def render_purchase_order_with_options_async(
        self,
        request: linkedmall_20230930_models.RenderPurchaseOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.RenderPurchaseOrderResponse:
        """
        @summary 渲染采购单
        
        @param request: RenderPurchaseOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenderPurchaseOrderResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='RenderPurchaseOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/commands/render',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.RenderPurchaseOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def render_purchase_order(
        self,
        request: linkedmall_20230930_models.RenderPurchaseOrderRequest,
    ) -> linkedmall_20230930_models.RenderPurchaseOrderResponse:
        """
        @summary 渲染采购单
        
        @param request: RenderPurchaseOrderRequest
        @return: RenderPurchaseOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.render_purchase_order_with_options(request, headers, runtime)

    async def render_purchase_order_async(
        self,
        request: linkedmall_20230930_models.RenderPurchaseOrderRequest,
    ) -> linkedmall_20230930_models.RenderPurchaseOrderResponse:
        """
        @summary 渲染采购单
        
        @param request: RenderPurchaseOrderRequest
        @return: RenderPurchaseOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.render_purchase_order_with_options_async(request, headers, runtime)

    def render_refund_order_with_options(
        self,
        request: linkedmall_20230930_models.RenderRefundOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.RenderRefundOrderResponse:
        """
        @summary 逆向单渲染
        
        @param request: RenderRefundOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenderRefundOrderResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='RenderRefundOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/commands/render',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.RenderRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def render_refund_order_with_options_async(
        self,
        request: linkedmall_20230930_models.RenderRefundOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.RenderRefundOrderResponse:
        """
        @summary 逆向单渲染
        
        @param request: RenderRefundOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenderRefundOrderResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='RenderRefundOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/commands/render',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.RenderRefundOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def render_refund_order(
        self,
        request: linkedmall_20230930_models.RenderRefundOrderRequest,
    ) -> linkedmall_20230930_models.RenderRefundOrderResponse:
        """
        @summary 逆向单渲染
        
        @param request: RenderRefundOrderRequest
        @return: RenderRefundOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.render_refund_order_with_options(request, headers, runtime)

    async def render_refund_order_async(
        self,
        request: linkedmall_20230930_models.RenderRefundOrderRequest,
    ) -> linkedmall_20230930_models.RenderRefundOrderResponse:
        """
        @summary 逆向单渲染
        
        @param request: RenderRefundOrderRequest
        @return: RenderRefundOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.render_refund_order_with_options_async(request, headers, runtime)

    def split_purchase_order_with_options(
        self,
        request: linkedmall_20230930_models.SplitPurchaseOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.SplitPurchaseOrderResponse:
        """
        @summary 渲染拆分采购单
        
        @param request: SplitPurchaseOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SplitPurchaseOrderResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='SplitPurchaseOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/commands/split',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.SplitPurchaseOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def split_purchase_order_with_options_async(
        self,
        request: linkedmall_20230930_models.SplitPurchaseOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20230930_models.SplitPurchaseOrderResponse:
        """
        @summary 渲染拆分采购单
        
        @param request: SplitPurchaseOrderRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SplitPurchaseOrderResponse
        """
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='SplitPurchaseOrder',
            version='2023-09-30',
            protocol='HTTPS',
            pathname=f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/commands/split',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20230930_models.SplitPurchaseOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def split_purchase_order(
        self,
        request: linkedmall_20230930_models.SplitPurchaseOrderRequest,
    ) -> linkedmall_20230930_models.SplitPurchaseOrderResponse:
        """
        @summary 渲染拆分采购单
        
        @param request: SplitPurchaseOrderRequest
        @return: SplitPurchaseOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.split_purchase_order_with_options(request, headers, runtime)

    async def split_purchase_order_async(
        self,
        request: linkedmall_20230930_models.SplitPurchaseOrderRequest,
    ) -> linkedmall_20230930_models.SplitPurchaseOrderResponse:
        """
        @summary 渲染拆分采购单
        
        @param request: SplitPurchaseOrderRequest
        @return: SplitPurchaseOrderResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.split_purchase_order_with_options_async(request, headers, runtime)
