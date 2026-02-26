# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_linkedmall20230930 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_refund_order_with_options(
        self,
        dispute_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelRefundOrderResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CancelRefundOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/{DaraURL.percent_encode(dispute_id)}/commands/cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_refund_order_with_options_async(
        self,
        dispute_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelRefundOrderResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CancelRefundOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/{DaraURL.percent_encode(dispute_id)}/commands/cancel',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRefundOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_refund_order(
        self,
        dispute_id: str,
    ) -> main_models.CancelRefundOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_refund_order_with_options(dispute_id, headers, runtime)

    async def cancel_refund_order_async(
        self,
        dispute_id: str,
    ) -> main_models.CancelRefundOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_refund_order_with_options_async(dispute_id, headers, runtime)

    def confirm_disburse_with_options(
        self,
        request: main_models.ConfirmDisburseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmDisburseResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmDisburse',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/commands/confirmDisburse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmDisburseResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_disburse_with_options_async(
        self,
        request: main_models.ConfirmDisburseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmDisburseResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmDisburse',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/commands/confirmDisburse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmDisburseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_disburse(
        self,
        request: main_models.ConfirmDisburseRequest,
    ) -> main_models.ConfirmDisburseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.confirm_disburse_with_options(request, headers, runtime)

    async def confirm_disburse_async(
        self,
        request: main_models.ConfirmDisburseRequest,
    ) -> main_models.ConfirmDisburseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.confirm_disburse_with_options_async(request, headers, runtime)

    def create_goods_shipping_notice_with_options(
        self,
        request: main_models.CreateGoodsShippingNoticeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGoodsShippingNoticeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGoodsShippingNotice',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/command/createGoodsShippingNotice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGoodsShippingNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_goods_shipping_notice_with_options_async(
        self,
        request: main_models.CreateGoodsShippingNoticeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGoodsShippingNoticeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGoodsShippingNotice',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/command/createGoodsShippingNotice',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGoodsShippingNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_goods_shipping_notice(
        self,
        request: main_models.CreateGoodsShippingNoticeRequest,
    ) -> main_models.CreateGoodsShippingNoticeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_goods_shipping_notice_with_options(request, headers, runtime)

    async def create_goods_shipping_notice_async(
        self,
        request: main_models.CreateGoodsShippingNoticeRequest,
    ) -> main_models.CreateGoodsShippingNoticeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_goods_shipping_notice_with_options_async(request, headers, runtime)

    def create_purchase_order_with_options(
        self,
        request: main_models.CreatePurchaseOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePurchaseOrderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePurchaseOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePurchaseOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_purchase_order_with_options_async(
        self,
        request: main_models.CreatePurchaseOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePurchaseOrderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePurchaseOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePurchaseOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_purchase_order(
        self,
        request: main_models.CreatePurchaseOrderRequest,
    ) -> main_models.CreatePurchaseOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_purchase_order_with_options(request, headers, runtime)

    async def create_purchase_order_async(
        self,
        request: main_models.CreatePurchaseOrderRequest,
    ) -> main_models.CreatePurchaseOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_purchase_order_with_options_async(request, headers, runtime)

    def create_refund_order_with_options(
        self,
        request: main_models.CreateRefundOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRefundOrderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRefundOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_refund_order_with_options_async(
        self,
        request: main_models.CreateRefundOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRefundOrderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRefundOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRefundOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_refund_order(
        self,
        request: main_models.CreateRefundOrderRequest,
    ) -> main_models.CreateRefundOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_refund_order_with_options(request, headers, runtime)

    async def create_refund_order_async(
        self,
        request: main_models.CreateRefundOrderRequest,
    ) -> main_models.CreateRefundOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_refund_order_with_options_async(request, headers, runtime)

    def get_order_with_options(
        self,
        order_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOrderResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/{DaraURL.percent_encode(order_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_order_with_options_async(
        self,
        order_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetOrderResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/{DaraURL.percent_encode(order_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_order(
        self,
        order_id: str,
    ) -> main_models.GetOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_order_with_options(order_id, headers, runtime)

    async def get_order_async(
        self,
        order_id: str,
    ) -> main_models.GetOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_order_with_options_async(order_id, headers, runtime)

    def get_purchase_order_status_with_options(
        self,
        purchase_order_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPurchaseOrderStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPurchaseOrderStatus',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/{DaraURL.percent_encode(purchase_order_id)}/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPurchaseOrderStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_purchase_order_status_with_options_async(
        self,
        purchase_order_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPurchaseOrderStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPurchaseOrderStatus',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/{DaraURL.percent_encode(purchase_order_id)}/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPurchaseOrderStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_purchase_order_status(
        self,
        purchase_order_id: str,
    ) -> main_models.GetPurchaseOrderStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_purchase_order_status_with_options(purchase_order_id, headers, runtime)

    async def get_purchase_order_status_async(
        self,
        purchase_order_id: str,
    ) -> main_models.GetPurchaseOrderStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_purchase_order_status_with_options_async(purchase_order_id, headers, runtime)

    def get_purchaser_shop_with_options(
        self,
        purchaser_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPurchaserShopResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPurchaserShop',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaserShops/{DaraURL.percent_encode(purchaser_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPurchaserShopResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_purchaser_shop_with_options_async(
        self,
        purchaser_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPurchaserShopResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPurchaserShop',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaserShops/{DaraURL.percent_encode(purchaser_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPurchaserShopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_purchaser_shop(
        self,
        purchaser_id: str,
    ) -> main_models.GetPurchaserShopResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_purchaser_shop_with_options(purchaser_id, headers, runtime)

    async def get_purchaser_shop_async(
        self,
        purchaser_id: str,
    ) -> main_models.GetPurchaserShopResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_purchaser_shop_with_options_async(purchaser_id, headers, runtime)

    def get_refund_order_with_options(
        self,
        dispute_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRefundOrderResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRefundOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/{DaraURL.percent_encode(dispute_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_refund_order_with_options_async(
        self,
        dispute_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRefundOrderResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRefundOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/{DaraURL.percent_encode(dispute_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRefundOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_refund_order(
        self,
        dispute_id: str,
    ) -> main_models.GetRefundOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_refund_order_with_options(dispute_id, headers, runtime)

    async def get_refund_order_async(
        self,
        dispute_id: str,
    ) -> main_models.GetRefundOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_refund_order_with_options_async(dispute_id, headers, runtime)

    def get_selection_product_with_options(
        self,
        product_id: str,
        request: main_models.GetSelectionProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSelectionProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.division_code):
            query['divisionCode'] = request.division_code
        if not DaraCore.is_null(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSelectionProduct',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/{DaraURL.percent_encode(product_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSelectionProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_selection_product_with_options_async(
        self,
        product_id: str,
        request: main_models.GetSelectionProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSelectionProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.division_code):
            query['divisionCode'] = request.division_code
        if not DaraCore.is_null(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSelectionProduct',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/{DaraURL.percent_encode(product_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSelectionProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_selection_product(
        self,
        product_id: str,
        request: main_models.GetSelectionProductRequest,
    ) -> main_models.GetSelectionProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_selection_product_with_options(product_id, request, headers, runtime)

    async def get_selection_product_async(
        self,
        product_id: str,
        request: main_models.GetSelectionProductRequest,
    ) -> main_models.GetSelectionProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_selection_product_with_options_async(product_id, request, headers, runtime)

    def get_selection_product_sale_info_with_options(
        self,
        product_id: str,
        request: main_models.GetSelectionProductSaleInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSelectionProductSaleInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.division_code):
            query['divisionCode'] = request.division_code
        if not DaraCore.is_null(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSelectionProductSaleInfo',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/{DaraURL.percent_encode(product_id)}/saleInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSelectionProductSaleInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_selection_product_sale_info_with_options_async(
        self,
        product_id: str,
        request: main_models.GetSelectionProductSaleInfoRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetSelectionProductSaleInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.division_code):
            query['divisionCode'] = request.division_code
        if not DaraCore.is_null(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSelectionProductSaleInfo',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/{DaraURL.percent_encode(product_id)}/saleInfo',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSelectionProductSaleInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_selection_product_sale_info(
        self,
        product_id: str,
        request: main_models.GetSelectionProductSaleInfoRequest,
    ) -> main_models.GetSelectionProductSaleInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_selection_product_sale_info_with_options(product_id, request, headers, runtime)

    async def get_selection_product_sale_info_async(
        self,
        product_id: str,
        request: main_models.GetSelectionProductSaleInfoRequest,
    ) -> main_models.GetSelectionProductSaleInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_selection_product_sale_info_with_options_async(product_id, request, headers, runtime)

    def list_categories_with_options(
        self,
        request: main_models.ListCategoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCategoriesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ListCategories',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/categories/commands/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_categories_with_options_async(
        self,
        request: main_models.ListCategoriesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCategoriesResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ListCategories',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/categories/commands/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_categories(
        self,
        request: main_models.ListCategoriesRequest,
    ) -> main_models.ListCategoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_categories_with_options(request, headers, runtime)

    async def list_categories_async(
        self,
        request: main_models.ListCategoriesRequest,
    ) -> main_models.ListCategoriesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_categories_with_options_async(request, headers, runtime)

    def list_logistics_orders_with_options(
        self,
        order_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogisticsOrdersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListLogisticsOrders',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/{DaraURL.percent_encode(order_id)}/logisticsOrders',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogisticsOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_logistics_orders_with_options_async(
        self,
        order_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLogisticsOrdersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListLogisticsOrders',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/{DaraURL.percent_encode(order_id)}/logisticsOrders',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLogisticsOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_logistics_orders(
        self,
        order_id: str,
    ) -> main_models.ListLogisticsOrdersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_logistics_orders_with_options(order_id, headers, runtime)

    async def list_logistics_orders_async(
        self,
        order_id: str,
    ) -> main_models.ListLogisticsOrdersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_logistics_orders_with_options_async(order_id, headers, runtime)

    def list_purchaser_shops_with_options(
        self,
        request: main_models.ListPurchaserShopsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPurchaserShopsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPurchaserShops',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaserShops',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPurchaserShopsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_purchaser_shops_with_options_async(
        self,
        request: main_models.ListPurchaserShopsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPurchaserShopsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPurchaserShops',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaserShops',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPurchaserShopsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_purchaser_shops(
        self,
        request: main_models.ListPurchaserShopsRequest,
    ) -> main_models.ListPurchaserShopsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_purchaser_shops_with_options(request, headers, runtime)

    async def list_purchaser_shops_async(
        self,
        request: main_models.ListPurchaserShopsRequest,
    ) -> main_models.ListPurchaserShopsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_purchaser_shops_with_options_async(request, headers, runtime)

    def list_selection_product_sale_infos_with_options(
        self,
        request: main_models.ListSelectionProductSaleInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSelectionProductSaleInfosResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ListSelectionProductSaleInfos',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/saleInfo/commands/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSelectionProductSaleInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_selection_product_sale_infos_with_options_async(
        self,
        request: main_models.ListSelectionProductSaleInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSelectionProductSaleInfosResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ListSelectionProductSaleInfos',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products/saleInfo/commands/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSelectionProductSaleInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_selection_product_sale_infos(
        self,
        request: main_models.ListSelectionProductSaleInfosRequest,
    ) -> main_models.ListSelectionProductSaleInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_selection_product_sale_infos_with_options(request, headers, runtime)

    async def list_selection_product_sale_infos_async(
        self,
        request: main_models.ListSelectionProductSaleInfosRequest,
    ) -> main_models.ListSelectionProductSaleInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_selection_product_sale_infos_with_options_async(request, headers, runtime)

    def list_selection_products_with_options(
        self,
        request: main_models.ListSelectionProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSelectionProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSelectionProducts',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSelectionProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_selection_products_with_options_async(
        self,
        request: main_models.ListSelectionProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSelectionProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.purchaser_id):
            query['purchaserId'] = request.purchaser_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSelectionProducts',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/products',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSelectionProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_selection_products(
        self,
        request: main_models.ListSelectionProductsRequest,
    ) -> main_models.ListSelectionProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_selection_products_with_options(request, headers, runtime)

    async def list_selection_products_async(
        self,
        request: main_models.ListSelectionProductsRequest,
    ) -> main_models.ListSelectionProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_selection_products_with_options_async(request, headers, runtime)

    def list_selection_sku_sale_infos_with_options(
        self,
        request: main_models.ListSelectionSkuSaleInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSelectionSkuSaleInfosResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ListSelectionSkuSaleInfos',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/skus/saleInfo/commands/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSelectionSkuSaleInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_selection_sku_sale_infos_with_options_async(
        self,
        request: main_models.ListSelectionSkuSaleInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSelectionSkuSaleInfosResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ListSelectionSkuSaleInfos',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/skus/saleInfo/commands/list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSelectionSkuSaleInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_selection_sku_sale_infos(
        self,
        request: main_models.ListSelectionSkuSaleInfosRequest,
    ) -> main_models.ListSelectionSkuSaleInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_selection_sku_sale_infos_with_options(request, headers, runtime)

    async def list_selection_sku_sale_infos_async(
        self,
        request: main_models.ListSelectionSkuSaleInfosRequest,
    ) -> main_models.ListSelectionSkuSaleInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_selection_sku_sale_infos_with_options_async(request, headers, runtime)

    def query_child_division_code_with_options(
        self,
        request: main_models.QueryChildDivisionCodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryChildDivisionCodeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'QueryChildDivisionCode',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/division/commands/queryChildDivisionCode',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryChildDivisionCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_child_division_code_with_options_async(
        self,
        request: main_models.QueryChildDivisionCodeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryChildDivisionCodeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'QueryChildDivisionCode',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/division/commands/queryChildDivisionCode',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryChildDivisionCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_child_division_code(
        self,
        request: main_models.QueryChildDivisionCodeRequest,
    ) -> main_models.QueryChildDivisionCodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_child_division_code_with_options(request, headers, runtime)

    async def query_child_division_code_async(
        self,
        request: main_models.QueryChildDivisionCodeRequest,
    ) -> main_models.QueryChildDivisionCodeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_child_division_code_with_options_async(request, headers, runtime)

    def query_orders_with_options(
        self,
        request: main_models.QueryOrdersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrdersResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'QueryOrders',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/commands/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_orders_with_options_async(
        self,
        request: main_models.QueryOrdersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrdersResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'QueryOrders',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/orders/commands/query',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_orders(
        self,
        request: main_models.QueryOrdersRequest,
    ) -> main_models.QueryOrdersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.query_orders_with_options(request, headers, runtime)

    async def query_orders_async(
        self,
        request: main_models.QueryOrdersRequest,
    ) -> main_models.QueryOrdersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.query_orders_with_options_async(request, headers, runtime)

    def render_purchase_order_with_options(
        self,
        request: main_models.RenderPurchaseOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenderPurchaseOrderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RenderPurchaseOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/commands/render',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenderPurchaseOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def render_purchase_order_with_options_async(
        self,
        request: main_models.RenderPurchaseOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenderPurchaseOrderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RenderPurchaseOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/commands/render',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenderPurchaseOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def render_purchase_order(
        self,
        request: main_models.RenderPurchaseOrderRequest,
    ) -> main_models.RenderPurchaseOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.render_purchase_order_with_options(request, headers, runtime)

    async def render_purchase_order_async(
        self,
        request: main_models.RenderPurchaseOrderRequest,
    ) -> main_models.RenderPurchaseOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.render_purchase_order_with_options_async(request, headers, runtime)

    def render_refund_order_with_options(
        self,
        request: main_models.RenderRefundOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenderRefundOrderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RenderRefundOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/commands/render',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenderRefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def render_refund_order_with_options_async(
        self,
        request: main_models.RenderRefundOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenderRefundOrderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RenderRefundOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/refunds/commands/render',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenderRefundOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def render_refund_order(
        self,
        request: main_models.RenderRefundOrderRequest,
    ) -> main_models.RenderRefundOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.render_refund_order_with_options(request, headers, runtime)

    async def render_refund_order_async(
        self,
        request: main_models.RenderRefundOrderRequest,
    ) -> main_models.RenderRefundOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.render_refund_order_with_options_async(request, headers, runtime)

    def search_products_with_options(
        self,
        request: main_models.SearchProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchProductsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.brand_name):
            body['brandName'] = request.brand_name
        if not DaraCore.is_null(request.category_ids):
            body['categoryIds'] = request.category_ids
        if not DaraCore.is_null(request.create_end_time):
            body['createEndTime'] = request.create_end_time
        if not DaraCore.is_null(request.create_start_time):
            body['createStartTime'] = request.create_start_time
        if not DaraCore.is_null(request.distribution_high_price):
            body['distributionHighPrice'] = request.distribution_high_price
        if not DaraCore.is_null(request.distribution_high_price_ratio):
            body['distributionHighPriceRatio'] = request.distribution_high_price_ratio
        if not DaraCore.is_null(request.distribution_low_price):
            body['distributionLowPrice'] = request.distribution_low_price
        if not DaraCore.is_null(request.distribution_low_price_ratio):
            body['distributionLowPriceRatio'] = request.distribution_low_price_ratio
        if not DaraCore.is_null(request.high_mark_price):
            body['highMarkPrice'] = request.high_mark_price
        if not DaraCore.is_null(request.high_price):
            body['highPrice'] = request.high_price
        if not DaraCore.is_null(request.in_group):
            body['inGroup'] = request.in_group
        if not DaraCore.is_null(request.in_group_end_time):
            body['inGroupEndTime'] = request.in_group_end_time
        if not DaraCore.is_null(request.in_group_start_time):
            body['inGroupStartTime'] = request.in_group_start_time
        if not DaraCore.is_null(request.inventory_risk_level):
            body['inventoryRiskLevel'] = request.inventory_risk_level
        if not DaraCore.is_null(request.lm_item_id):
            body['lmItemId'] = request.lm_item_id
        if not DaraCore.is_null(request.low_mark_price):
            body['lowMarkPrice'] = request.low_mark_price
        if not DaraCore.is_null(request.low_price):
            body['lowPrice'] = request.low_price
        if not DaraCore.is_null(request.modify_end_time):
            body['modifyEndTime'] = request.modify_end_time
        if not DaraCore.is_null(request.modify_start_time):
            body['modifyStartTime'] = request.modify_start_time
        if not DaraCore.is_null(request.order_by):
            body['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            body['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            body['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.platform):
            body['platform'] = request.platform
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_name):
            body['productName'] = request.product_name
        if not DaraCore.is_null(request.product_status):
            body['productStatus'] = request.product_status
        if not DaraCore.is_null(request.purchaser_id):
            body['purchaserId'] = request.purchaser_id
        if not DaraCore.is_null(request.tax_rate):
            body['taxRate'] = request.tax_rate
        if not DaraCore.is_null(request.trade_mode_and_credit):
            body['tradeModeAndCredit'] = request.trade_mode_and_credit
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchProducts',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/selection-group/product/command/searchProduct',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_products_with_options_async(
        self,
        request: main_models.SearchProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchProductsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.brand_name):
            body['brandName'] = request.brand_name
        if not DaraCore.is_null(request.category_ids):
            body['categoryIds'] = request.category_ids
        if not DaraCore.is_null(request.create_end_time):
            body['createEndTime'] = request.create_end_time
        if not DaraCore.is_null(request.create_start_time):
            body['createStartTime'] = request.create_start_time
        if not DaraCore.is_null(request.distribution_high_price):
            body['distributionHighPrice'] = request.distribution_high_price
        if not DaraCore.is_null(request.distribution_high_price_ratio):
            body['distributionHighPriceRatio'] = request.distribution_high_price_ratio
        if not DaraCore.is_null(request.distribution_low_price):
            body['distributionLowPrice'] = request.distribution_low_price
        if not DaraCore.is_null(request.distribution_low_price_ratio):
            body['distributionLowPriceRatio'] = request.distribution_low_price_ratio
        if not DaraCore.is_null(request.high_mark_price):
            body['highMarkPrice'] = request.high_mark_price
        if not DaraCore.is_null(request.high_price):
            body['highPrice'] = request.high_price
        if not DaraCore.is_null(request.in_group):
            body['inGroup'] = request.in_group
        if not DaraCore.is_null(request.in_group_end_time):
            body['inGroupEndTime'] = request.in_group_end_time
        if not DaraCore.is_null(request.in_group_start_time):
            body['inGroupStartTime'] = request.in_group_start_time
        if not DaraCore.is_null(request.inventory_risk_level):
            body['inventoryRiskLevel'] = request.inventory_risk_level
        if not DaraCore.is_null(request.lm_item_id):
            body['lmItemId'] = request.lm_item_id
        if not DaraCore.is_null(request.low_mark_price):
            body['lowMarkPrice'] = request.low_mark_price
        if not DaraCore.is_null(request.low_price):
            body['lowPrice'] = request.low_price
        if not DaraCore.is_null(request.modify_end_time):
            body['modifyEndTime'] = request.modify_end_time
        if not DaraCore.is_null(request.modify_start_time):
            body['modifyStartTime'] = request.modify_start_time
        if not DaraCore.is_null(request.order_by):
            body['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            body['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            body['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['pageSize'] = request.page_size
        if not DaraCore.is_null(request.platform):
            body['platform'] = request.platform
        if not DaraCore.is_null(request.product_id):
            body['productId'] = request.product_id
        if not DaraCore.is_null(request.product_name):
            body['productName'] = request.product_name
        if not DaraCore.is_null(request.product_status):
            body['productStatus'] = request.product_status
        if not DaraCore.is_null(request.purchaser_id):
            body['purchaserId'] = request.purchaser_id
        if not DaraCore.is_null(request.tax_rate):
            body['taxRate'] = request.tax_rate
        if not DaraCore.is_null(request.trade_mode_and_credit):
            body['tradeModeAndCredit'] = request.trade_mode_and_credit
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SearchProducts',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/selection-group/product/command/searchProduct',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_products(
        self,
        request: main_models.SearchProductsRequest,
    ) -> main_models.SearchProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_products_with_options(request, headers, runtime)

    async def search_products_async(
        self,
        request: main_models.SearchProductsRequest,
    ) -> main_models.SearchProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_products_with_options_async(request, headers, runtime)

    def selection_group_add_product_with_options(
        self,
        request: main_models.SelectionGroupAddProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectionGroupAddProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_ids):
            body['productIds'] = request.product_ids
        if not DaraCore.is_null(request.purchaser_id):
            body['purchaserId'] = request.purchaser_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SelectionGroupAddProduct',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/selection-group/product/command/addProduct',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectionGroupAddProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def selection_group_add_product_with_options_async(
        self,
        request: main_models.SelectionGroupAddProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectionGroupAddProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_ids):
            body['productIds'] = request.product_ids
        if not DaraCore.is_null(request.purchaser_id):
            body['purchaserId'] = request.purchaser_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SelectionGroupAddProduct',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/selection-group/product/command/addProduct',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectionGroupAddProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def selection_group_add_product(
        self,
        request: main_models.SelectionGroupAddProductRequest,
    ) -> main_models.SelectionGroupAddProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.selection_group_add_product_with_options(request, headers, runtime)

    async def selection_group_add_product_async(
        self,
        request: main_models.SelectionGroupAddProductRequest,
    ) -> main_models.SelectionGroupAddProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.selection_group_add_product_with_options_async(request, headers, runtime)

    def selection_group_remove_product_with_options(
        self,
        request: main_models.SelectionGroupRemoveProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectionGroupRemoveProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_ids):
            body['productIds'] = request.product_ids
        if not DaraCore.is_null(request.purchaser_id):
            body['purchaserId'] = request.purchaser_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SelectionGroupRemoveProduct',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/selection-group/product/command/removeProduct',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectionGroupRemoveProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def selection_group_remove_product_with_options_async(
        self,
        request: main_models.SelectionGroupRemoveProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SelectionGroupRemoveProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_ids):
            body['productIds'] = request.product_ids
        if not DaraCore.is_null(request.purchaser_id):
            body['purchaserId'] = request.purchaser_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SelectionGroupRemoveProduct',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/selectionPool/selection-group/product/command/removeProduct',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SelectionGroupRemoveProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def selection_group_remove_product(
        self,
        request: main_models.SelectionGroupRemoveProductRequest,
    ) -> main_models.SelectionGroupRemoveProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.selection_group_remove_product_with_options(request, headers, runtime)

    async def selection_group_remove_product_async(
        self,
        request: main_models.SelectionGroupRemoveProductRequest,
    ) -> main_models.SelectionGroupRemoveProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.selection_group_remove_product_with_options_async(request, headers, runtime)

    def split_purchase_order_with_options(
        self,
        request: main_models.SplitPurchaseOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SplitPurchaseOrderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'SplitPurchaseOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/commands/split',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SplitPurchaseOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def split_purchase_order_with_options_async(
        self,
        request: main_models.SplitPurchaseOrderRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SplitPurchaseOrderResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'SplitPurchaseOrder',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = f'/opensaas-s2b/opensaas-s2b-biz-trade/v2/purchaseOrders/commands/split',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SplitPurchaseOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def split_purchase_order(
        self,
        request: main_models.SplitPurchaseOrderRequest,
    ) -> main_models.SplitPurchaseOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.split_purchase_order_with_options(request, headers, runtime)

    async def split_purchase_order_async(
        self,
        request: main_models.SplitPurchaseOrderRequest,
    ) -> main_models.SplitPurchaseOrderResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.split_purchase_order_with_options_async(request, headers, runtime)
