# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkedmall20180116 import models as linkedmall_20180116_models
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

    def add_address_with_options(
        self,
        request: linkedmall_20180116_models.AddAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddAddressResponse(),
            self.do_rpcrequest('AddAddress', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_address_with_options_async(
        self,
        request: linkedmall_20180116_models.AddAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddAddressResponse(),
            await self.do_rpcrequest_async('AddAddress', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_address(
        self,
        request: linkedmall_20180116_models.AddAddressRequest,
    ) -> linkedmall_20180116_models.AddAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_address_with_options(request, runtime)

    async def add_address_async(
        self,
        request: linkedmall_20180116_models.AddAddressRequest,
    ) -> linkedmall_20180116_models.AddAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_address_with_options_async(request, runtime)

    def add_item_limit_rule_with_options(
        self,
        request: linkedmall_20180116_models.AddItemLimitRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddItemLimitRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddItemLimitRuleResponse(),
            self.do_rpcrequest('AddItemLimitRule', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_item_limit_rule_with_options_async(
        self,
        request: linkedmall_20180116_models.AddItemLimitRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddItemLimitRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddItemLimitRuleResponse(),
            await self.do_rpcrequest_async('AddItemLimitRule', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_item_limit_rule(
        self,
        request: linkedmall_20180116_models.AddItemLimitRuleRequest,
    ) -> linkedmall_20180116_models.AddItemLimitRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_item_limit_rule_with_options(request, runtime)

    async def add_item_limit_rule_async(
        self,
        request: linkedmall_20180116_models.AddItemLimitRuleRequest,
    ) -> linkedmall_20180116_models.AddItemLimitRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_item_limit_rule_with_options_async(request, runtime)

    def add_item_to_sub_bizs_with_options(
        self,
        tmp_req: linkedmall_20180116_models.AddItemToSubBizsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddItemToSubBizsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.AddItemToSubBizsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_biz_ids):
            request.sub_biz_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_biz_ids, 'SubBizIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddItemToSubBizsResponse(),
            self.do_rpcrequest('AddItemToSubBizs', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_item_to_sub_bizs_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.AddItemToSubBizsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddItemToSubBizsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.AddItemToSubBizsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_biz_ids):
            request.sub_biz_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_biz_ids, 'SubBizIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddItemToSubBizsResponse(),
            await self.do_rpcrequest_async('AddItemToSubBizs', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_item_to_sub_bizs(
        self,
        request: linkedmall_20180116_models.AddItemToSubBizsRequest,
    ) -> linkedmall_20180116_models.AddItemToSubBizsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_item_to_sub_bizs_with_options(request, runtime)

    async def add_item_to_sub_bizs_async(
        self,
        request: linkedmall_20180116_models.AddItemToSubBizsRequest,
    ) -> linkedmall_20180116_models.AddItemToSubBizsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_item_to_sub_bizs_with_options_async(request, runtime)

    def add_supplier_new_items_with_options(
        self,
        request: linkedmall_20180116_models.AddSupplierNewItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddSupplierNewItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddSupplierNewItemsResponse(),
            self.do_rpcrequest('AddSupplierNewItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_supplier_new_items_with_options_async(
        self,
        request: linkedmall_20180116_models.AddSupplierNewItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddSupplierNewItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddSupplierNewItemsResponse(),
            await self.do_rpcrequest_async('AddSupplierNewItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_supplier_new_items(
        self,
        request: linkedmall_20180116_models.AddSupplierNewItemsRequest,
    ) -> linkedmall_20180116_models.AddSupplierNewItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_supplier_new_items_with_options(request, runtime)

    async def add_supplier_new_items_async(
        self,
        request: linkedmall_20180116_models.AddSupplierNewItemsRequest,
    ) -> linkedmall_20180116_models.AddSupplierNewItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_supplier_new_items_with_options_async(request, runtime)

    def apply_refund_with_options(
        self,
        request: linkedmall_20180116_models.ApplyRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ApplyRefundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ApplyRefundResponse(),
            self.do_rpcrequest('ApplyRefund', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_refund_with_options_async(
        self,
        request: linkedmall_20180116_models.ApplyRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ApplyRefundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ApplyRefundResponse(),
            await self.do_rpcrequest_async('ApplyRefund', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_refund(
        self,
        request: linkedmall_20180116_models.ApplyRefundRequest,
    ) -> linkedmall_20180116_models.ApplyRefundResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_refund_with_options(request, runtime)

    async def apply_refund_async(
        self,
        request: linkedmall_20180116_models.ApplyRefundRequest,
    ) -> linkedmall_20180116_models.ApplyRefundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_refund_with_options_async(request, runtime)

    def batch_regist_anonymous_tb_account_with_options(
        self,
        request: linkedmall_20180116_models.BatchRegistAnonymousTbAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.BatchRegistAnonymousTbAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.BatchRegistAnonymousTbAccountResponse(),
            self.do_rpcrequest('BatchRegistAnonymousTbAccount', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def batch_regist_anonymous_tb_account_with_options_async(
        self,
        request: linkedmall_20180116_models.BatchRegistAnonymousTbAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.BatchRegistAnonymousTbAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.BatchRegistAnonymousTbAccountResponse(),
            await self.do_rpcrequest_async('BatchRegistAnonymousTbAccount', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_regist_anonymous_tb_account(
        self,
        request: linkedmall_20180116_models.BatchRegistAnonymousTbAccountRequest,
    ) -> linkedmall_20180116_models.BatchRegistAnonymousTbAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_regist_anonymous_tb_account_with_options(request, runtime)

    async def batch_regist_anonymous_tb_account_async(
        self,
        request: linkedmall_20180116_models.BatchRegistAnonymousTbAccountRequest,
    ) -> linkedmall_20180116_models.BatchRegistAnonymousTbAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_regist_anonymous_tb_account_with_options_async(request, runtime)

    def cancel_order_with_options(
        self,
        request: linkedmall_20180116_models.CancelOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelOrderResponse(),
            self.do_rpcrequest('CancelOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_order_with_options_async(
        self,
        request: linkedmall_20180116_models.CancelOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelOrderResponse(),
            await self.do_rpcrequest_async('CancelOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_order(
        self,
        request: linkedmall_20180116_models.CancelOrderRequest,
    ) -> linkedmall_20180116_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_with_options(request, runtime)

    async def cancel_order_async(
        self,
        request: linkedmall_20180116_models.CancelOrderRequest,
    ) -> linkedmall_20180116_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_order_with_options_async(request, runtime)

    def cancel_refund_with_options(
        self,
        request: linkedmall_20180116_models.CancelRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelRefundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelRefundResponse(),
            self.do_rpcrequest('CancelRefund', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_refund_with_options_async(
        self,
        request: linkedmall_20180116_models.CancelRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelRefundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelRefundResponse(),
            await self.do_rpcrequest_async('CancelRefund', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_refund(
        self,
        request: linkedmall_20180116_models.CancelRefundRequest,
    ) -> linkedmall_20180116_models.CancelRefundResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_refund_with_options(request, runtime)

    async def cancel_refund_async(
        self,
        request: linkedmall_20180116_models.CancelRefundRequest,
    ) -> linkedmall_20180116_models.CancelRefundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_refund_with_options_async(request, runtime)

    def confirm_disburse_with_options(
        self,
        request: linkedmall_20180116_models.ConfirmDisburseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ConfirmDisburseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ConfirmDisburseResponse(),
            self.do_rpcrequest('ConfirmDisburse', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def confirm_disburse_with_options_async(
        self,
        request: linkedmall_20180116_models.ConfirmDisburseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ConfirmDisburseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ConfirmDisburseResponse(),
            await self.do_rpcrequest_async('ConfirmDisburse', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def confirm_disburse(
        self,
        request: linkedmall_20180116_models.ConfirmDisburseRequest,
    ) -> linkedmall_20180116_models.ConfirmDisburseResponse:
        runtime = util_models.RuntimeOptions()
        return self.confirm_disburse_with_options(request, runtime)

    async def confirm_disburse_async(
        self,
        request: linkedmall_20180116_models.ConfirmDisburseRequest,
    ) -> linkedmall_20180116_models.ConfirmDisburseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_disburse_with_options_async(request, runtime)

    def create_movie_ticket_order_with_options(
        self,
        request: linkedmall_20180116_models.CreateMovieTicketOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateMovieTicketOrderResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateMovieTicketOrderResponse(),
            self.do_rpcrequest('CreateMovieTicketOrder', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def create_movie_ticket_order_with_options_async(
        self,
        request: linkedmall_20180116_models.CreateMovieTicketOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateMovieTicketOrderResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateMovieTicketOrderResponse(),
            await self.do_rpcrequest_async('CreateMovieTicketOrder', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def create_movie_ticket_order(
        self,
        request: linkedmall_20180116_models.CreateMovieTicketOrderRequest,
    ) -> linkedmall_20180116_models.CreateMovieTicketOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_movie_ticket_order_with_options(request, runtime)

    async def create_movie_ticket_order_async(
        self,
        request: linkedmall_20180116_models.CreateMovieTicketOrderRequest,
    ) -> linkedmall_20180116_models.CreateMovieTicketOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_movie_ticket_order_with_options_async(request, runtime)

    def create_order_with_options(
        self,
        request: linkedmall_20180116_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderResponse(),
            self.do_rpcrequest('CreateOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: linkedmall_20180116_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderResponse(),
            await self.do_rpcrequest_async('CreateOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_order(
        self,
        request: linkedmall_20180116_models.CreateOrderRequest,
    ) -> linkedmall_20180116_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    async def create_order_async(
        self,
        request: linkedmall_20180116_models.CreateOrderRequest,
    ) -> linkedmall_20180116_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_with_options_async(request, runtime)

    def create_order_v2with_options(
        self,
        request: linkedmall_20180116_models.CreateOrderV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderV2Response(),
            self.do_rpcrequest('CreateOrderV2', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_order_v2with_options_async(
        self,
        request: linkedmall_20180116_models.CreateOrderV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderV2Response(),
            await self.do_rpcrequest_async('CreateOrderV2', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_order_v2(
        self,
        request: linkedmall_20180116_models.CreateOrderV2Request,
    ) -> linkedmall_20180116_models.CreateOrderV2Response:
        runtime = util_models.RuntimeOptions()
        return self.create_order_v2with_options(request, runtime)

    async def create_order_v2_async(
        self,
        request: linkedmall_20180116_models.CreateOrderV2Request,
    ) -> linkedmall_20180116_models.CreateOrderV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_v2with_options_async(request, runtime)

    def create_pay_url_with_options(
        self,
        request: linkedmall_20180116_models.CreatePayUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreatePayUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreatePayUrlResponse(),
            self.do_rpcrequest('CreatePayUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_pay_url_with_options_async(
        self,
        request: linkedmall_20180116_models.CreatePayUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreatePayUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreatePayUrlResponse(),
            await self.do_rpcrequest_async('CreatePayUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_pay_url(
        self,
        request: linkedmall_20180116_models.CreatePayUrlRequest,
    ) -> linkedmall_20180116_models.CreatePayUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_pay_url_with_options(request, runtime)

    async def create_pay_url_async(
        self,
        request: linkedmall_20180116_models.CreatePayUrlRequest,
    ) -> linkedmall_20180116_models.CreatePayUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_pay_url_with_options_async(request, runtime)

    def create_virtual_product_order_with_options(
        self,
        request: linkedmall_20180116_models.CreateVirtualProductOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateVirtualProductOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateVirtualProductOrderResponse(),
            self.do_rpcrequest('CreateVirtualProductOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_virtual_product_order_with_options_async(
        self,
        request: linkedmall_20180116_models.CreateVirtualProductOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateVirtualProductOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateVirtualProductOrderResponse(),
            await self.do_rpcrequest_async('CreateVirtualProductOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_virtual_product_order(
        self,
        request: linkedmall_20180116_models.CreateVirtualProductOrderRequest,
    ) -> linkedmall_20180116_models.CreateVirtualProductOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_product_order_with_options(request, runtime)

    async def create_virtual_product_order_async(
        self,
        request: linkedmall_20180116_models.CreateVirtualProductOrderRequest,
    ) -> linkedmall_20180116_models.CreateVirtualProductOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_virtual_product_order_with_options_async(request, runtime)

    def create_withhold_trade_with_options(
        self,
        request: linkedmall_20180116_models.CreateWithholdTradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateWithholdTradeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateWithholdTradeResponse(),
            self.do_rpcrequest('CreateWithholdTrade', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_withhold_trade_with_options_async(
        self,
        request: linkedmall_20180116_models.CreateWithholdTradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateWithholdTradeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateWithholdTradeResponse(),
            await self.do_rpcrequest_async('CreateWithholdTrade', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_withhold_trade(
        self,
        request: linkedmall_20180116_models.CreateWithholdTradeRequest,
    ) -> linkedmall_20180116_models.CreateWithholdTradeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_withhold_trade_with_options(request, runtime)

    async def create_withhold_trade_async(
        self,
        request: linkedmall_20180116_models.CreateWithholdTradeRequest,
    ) -> linkedmall_20180116_models.CreateWithholdTradeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_withhold_trade_with_options_async(request, runtime)

    def delete_biz_items_with_options(
        self,
        request: linkedmall_20180116_models.DeleteBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DeleteBizItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DeleteBizItemsResponse(),
            self.do_rpcrequest('DeleteBizItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_biz_items_with_options_async(
        self,
        request: linkedmall_20180116_models.DeleteBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DeleteBizItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DeleteBizItemsResponse(),
            await self.do_rpcrequest_async('DeleteBizItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_biz_items(
        self,
        request: linkedmall_20180116_models.DeleteBizItemsRequest,
    ) -> linkedmall_20180116_models.DeleteBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_biz_items_with_options(request, runtime)

    async def delete_biz_items_async(
        self,
        request: linkedmall_20180116_models.DeleteBizItemsRequest,
    ) -> linkedmall_20180116_models.DeleteBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_biz_items_with_options_async(request, runtime)

    def delete_item_limit_rule_with_options(
        self,
        request: linkedmall_20180116_models.DeleteItemLimitRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DeleteItemLimitRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DeleteItemLimitRuleResponse(),
            self.do_rpcrequest('DeleteItemLimitRule', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_item_limit_rule_with_options_async(
        self,
        request: linkedmall_20180116_models.DeleteItemLimitRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DeleteItemLimitRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DeleteItemLimitRuleResponse(),
            await self.do_rpcrequest_async('DeleteItemLimitRule', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_item_limit_rule(
        self,
        request: linkedmall_20180116_models.DeleteItemLimitRuleRequest,
    ) -> linkedmall_20180116_models.DeleteItemLimitRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_item_limit_rule_with_options(request, runtime)

    async def delete_item_limit_rule_async(
        self,
        request: linkedmall_20180116_models.DeleteItemLimitRuleRequest,
    ) -> linkedmall_20180116_models.DeleteItemLimitRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_item_limit_rule_with_options_async(request, runtime)

    def enable_order_with_options(
        self,
        request: linkedmall_20180116_models.EnableOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.EnableOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.EnableOrderResponse(),
            self.do_rpcrequest('EnableOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_order_with_options_async(
        self,
        request: linkedmall_20180116_models.EnableOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.EnableOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.EnableOrderResponse(),
            await self.do_rpcrequest_async('EnableOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_order(
        self,
        request: linkedmall_20180116_models.EnableOrderRequest,
    ) -> linkedmall_20180116_models.EnableOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_order_with_options(request, runtime)

    async def enable_order_async(
        self,
        request: linkedmall_20180116_models.EnableOrderRequest,
    ) -> linkedmall_20180116_models.EnableOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_order_with_options_async(request, runtime)

    def execute_node_with_options(
        self,
        request: linkedmall_20180116_models.ExecuteNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ExecuteNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ExecuteNodeResponse(),
            self.do_rpcrequest('ExecuteNode', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def execute_node_with_options_async(
        self,
        request: linkedmall_20180116_models.ExecuteNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ExecuteNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ExecuteNodeResponse(),
            await self.do_rpcrequest_async('ExecuteNode', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_node(
        self,
        request: linkedmall_20180116_models.ExecuteNodeRequest,
    ) -> linkedmall_20180116_models.ExecuteNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_node_with_options(request, runtime)

    async def execute_node_async(
        self,
        request: linkedmall_20180116_models.ExecuteNodeRequest,
    ) -> linkedmall_20180116_models.ExecuteNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_node_with_options_async(request, runtime)

    def get_category_chain_with_options(
        self,
        request: linkedmall_20180116_models.GetCategoryChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetCategoryChainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCategoryChainResponse(),
            self.do_rpcrequest('GetCategoryChain', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_category_chain_with_options_async(
        self,
        request: linkedmall_20180116_models.GetCategoryChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetCategoryChainResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCategoryChainResponse(),
            await self.do_rpcrequest_async('GetCategoryChain', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_category_chain(
        self,
        request: linkedmall_20180116_models.GetCategoryChainRequest,
    ) -> linkedmall_20180116_models.GetCategoryChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_category_chain_with_options(request, runtime)

    async def get_category_chain_async(
        self,
        request: linkedmall_20180116_models.GetCategoryChainRequest,
    ) -> linkedmall_20180116_models.GetCategoryChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_category_chain_with_options_async(request, runtime)

    def get_category_list_with_options(
        self,
        request: linkedmall_20180116_models.GetCategoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetCategoryListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCategoryListResponse(),
            self.do_rpcrequest('GetCategoryList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_category_list_with_options_async(
        self,
        request: linkedmall_20180116_models.GetCategoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetCategoryListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCategoryListResponse(),
            await self.do_rpcrequest_async('GetCategoryList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_category_list(
        self,
        request: linkedmall_20180116_models.GetCategoryListRequest,
    ) -> linkedmall_20180116_models.GetCategoryListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_category_list_with_options(request, runtime)

    async def get_category_list_async(
        self,
        request: linkedmall_20180116_models.GetCategoryListRequest,
    ) -> linkedmall_20180116_models.GetCategoryListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_category_list_with_options_async(request, runtime)

    def get_custom_service_url_with_options(
        self,
        request: linkedmall_20180116_models.GetCustomServiceUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetCustomServiceUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCustomServiceUrlResponse(),
            self.do_rpcrequest('GetCustomServiceUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_custom_service_url_with_options_async(
        self,
        request: linkedmall_20180116_models.GetCustomServiceUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetCustomServiceUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCustomServiceUrlResponse(),
            await self.do_rpcrequest_async('GetCustomServiceUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_custom_service_url(
        self,
        request: linkedmall_20180116_models.GetCustomServiceUrlRequest,
    ) -> linkedmall_20180116_models.GetCustomServiceUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_custom_service_url_with_options(request, runtime)

    async def get_custom_service_url_async(
        self,
        request: linkedmall_20180116_models.GetCustomServiceUrlRequest,
    ) -> linkedmall_20180116_models.GetCustomServiceUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_custom_service_url_with_options_async(request, runtime)

    def get_guide_page_with_options(
        self,
        request: linkedmall_20180116_models.GetGuidePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetGuidePageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetGuidePageResponse(),
            self.do_rpcrequest('GetGuidePage', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_guide_page_with_options_async(
        self,
        request: linkedmall_20180116_models.GetGuidePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetGuidePageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetGuidePageResponse(),
            await self.do_rpcrequest_async('GetGuidePage', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_guide_page(
        self,
        request: linkedmall_20180116_models.GetGuidePageRequest,
    ) -> linkedmall_20180116_models.GetGuidePageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_guide_page_with_options(request, runtime)

    async def get_guide_page_async(
        self,
        request: linkedmall_20180116_models.GetGuidePageRequest,
    ) -> linkedmall_20180116_models.GetGuidePageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_guide_page_with_options_async(request, runtime)

    def get_item_promotion_with_options(
        self,
        request: linkedmall_20180116_models.GetItemPromotionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetItemPromotionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetItemPromotionResponse(),
            self.do_rpcrequest('GetItemPromotion', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_item_promotion_with_options_async(
        self,
        request: linkedmall_20180116_models.GetItemPromotionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetItemPromotionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetItemPromotionResponse(),
            await self.do_rpcrequest_async('GetItemPromotion', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_item_promotion(
        self,
        request: linkedmall_20180116_models.GetItemPromotionRequest,
    ) -> linkedmall_20180116_models.GetItemPromotionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_item_promotion_with_options(request, runtime)

    async def get_item_promotion_async(
        self,
        request: linkedmall_20180116_models.GetItemPromotionRequest,
    ) -> linkedmall_20180116_models.GetItemPromotionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_item_promotion_with_options_async(request, runtime)

    def get_login_page_with_options(
        self,
        request: linkedmall_20180116_models.GetLoginPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetLoginPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetLoginPageResponse(),
            self.do_rpcrequest('GetLoginPage', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_login_page_with_options_async(
        self,
        request: linkedmall_20180116_models.GetLoginPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetLoginPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetLoginPageResponse(),
            await self.do_rpcrequest_async('GetLoginPage', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_login_page(
        self,
        request: linkedmall_20180116_models.GetLoginPageRequest,
    ) -> linkedmall_20180116_models.GetLoginPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_login_page_with_options(request, runtime)

    async def get_login_page_async(
        self,
        request: linkedmall_20180116_models.GetLoginPageRequest,
    ) -> linkedmall_20180116_models.GetLoginPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_login_page_with_options_async(request, runtime)

    def get_switch_url_with_options(
        self,
        request: linkedmall_20180116_models.GetSwitchUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetSwitchUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetSwitchUrlResponse(),
            self.do_rpcrequest('GetSwitchUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_switch_url_with_options_async(
        self,
        request: linkedmall_20180116_models.GetSwitchUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetSwitchUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetSwitchUrlResponse(),
            await self.do_rpcrequest_async('GetSwitchUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_switch_url(
        self,
        request: linkedmall_20180116_models.GetSwitchUrlRequest,
    ) -> linkedmall_20180116_models.GetSwitchUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_switch_url_with_options(request, runtime)

    async def get_switch_url_async(
        self,
        request: linkedmall_20180116_models.GetSwitchUrlRequest,
    ) -> linkedmall_20180116_models.GetSwitchUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_switch_url_with_options_async(request, runtime)

    def get_user_info_with_options(
        self,
        request: linkedmall_20180116_models.GetUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetUserInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetUserInfoResponse(),
            self.do_rpcrequest('GetUserInfo', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_info_with_options_async(
        self,
        request: linkedmall_20180116_models.GetUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetUserInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetUserInfoResponse(),
            await self.do_rpcrequest_async('GetUserInfo', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_info(
        self,
        request: linkedmall_20180116_models.GetUserInfoRequest,
    ) -> linkedmall_20180116_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_info_with_options(request, runtime)

    async def get_user_info_async(
        self,
        request: linkedmall_20180116_models.GetUserInfoRequest,
    ) -> linkedmall_20180116_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_info_with_options_async(request, runtime)

    def get_withhold_sign_page_url_with_options(
        self,
        request: linkedmall_20180116_models.GetWithholdSignPageUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetWithholdSignPageUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetWithholdSignPageUrlResponse(),
            self.do_rpcrequest('GetWithholdSignPageUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_withhold_sign_page_url_with_options_async(
        self,
        request: linkedmall_20180116_models.GetWithholdSignPageUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetWithholdSignPageUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetWithholdSignPageUrlResponse(),
            await self.do_rpcrequest_async('GetWithholdSignPageUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_withhold_sign_page_url(
        self,
        request: linkedmall_20180116_models.GetWithholdSignPageUrlRequest,
    ) -> linkedmall_20180116_models.GetWithholdSignPageUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_withhold_sign_page_url_with_options(request, runtime)

    async def get_withhold_sign_page_url_async(
        self,
        request: linkedmall_20180116_models.GetWithholdSignPageUrlRequest,
    ) -> linkedmall_20180116_models.GetWithholdSignPageUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_withhold_sign_page_url_with_options_async(request, runtime)

    def init_apply_refund_with_options(
        self,
        request: linkedmall_20180116_models.InitApplyRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.InitApplyRefundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.InitApplyRefundResponse(),
            self.do_rpcrequest('InitApplyRefund', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def init_apply_refund_with_options_async(
        self,
        request: linkedmall_20180116_models.InitApplyRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.InitApplyRefundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.InitApplyRefundResponse(),
            await self.do_rpcrequest_async('InitApplyRefund', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def init_apply_refund(
        self,
        request: linkedmall_20180116_models.InitApplyRefundRequest,
    ) -> linkedmall_20180116_models.InitApplyRefundResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_apply_refund_with_options(request, runtime)

    async def init_apply_refund_async(
        self,
        request: linkedmall_20180116_models.InitApplyRefundRequest,
    ) -> linkedmall_20180116_models.InitApplyRefundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_apply_refund_with_options_async(request, runtime)

    def list_item_activities_with_options(
        self,
        tmp_req: linkedmall_20180116_models.ListItemActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ListItemActivitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.ListItemActivitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ListItemActivitiesResponse(),
            self.do_rpcrequest('ListItemActivities', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_item_activities_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.ListItemActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ListItemActivitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.ListItemActivitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ListItemActivitiesResponse(),
            await self.do_rpcrequest_async('ListItemActivities', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_item_activities(
        self,
        request: linkedmall_20180116_models.ListItemActivitiesRequest,
    ) -> linkedmall_20180116_models.ListItemActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_item_activities_with_options(request, runtime)

    async def list_item_activities_async(
        self,
        request: linkedmall_20180116_models.ListItemActivitiesRequest,
    ) -> linkedmall_20180116_models.ListItemActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_item_activities_with_options_async(request, runtime)

    def modify_basic_and_biz_items_with_options(
        self,
        request: linkedmall_20180116_models.ModifyBasicAndBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyBasicAndBizItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyBasicAndBizItemsResponse(),
            self.do_rpcrequest('ModifyBasicAndBizItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_basic_and_biz_items_with_options_async(
        self,
        request: linkedmall_20180116_models.ModifyBasicAndBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyBasicAndBizItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyBasicAndBizItemsResponse(),
            await self.do_rpcrequest_async('ModifyBasicAndBizItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_basic_and_biz_items(
        self,
        request: linkedmall_20180116_models.ModifyBasicAndBizItemsRequest,
    ) -> linkedmall_20180116_models.ModifyBasicAndBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_basic_and_biz_items_with_options(request, runtime)

    async def modify_basic_and_biz_items_async(
        self,
        request: linkedmall_20180116_models.ModifyBasicAndBizItemsRequest,
    ) -> linkedmall_20180116_models.ModifyBasicAndBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_basic_and_biz_items_with_options_async(request, runtime)

    def modify_biz_items_with_options(
        self,
        request: linkedmall_20180116_models.ModifyBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyBizItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyBizItemsResponse(),
            self.do_rpcrequest('ModifyBizItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_biz_items_with_options_async(
        self,
        request: linkedmall_20180116_models.ModifyBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyBizItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyBizItemsResponse(),
            await self.do_rpcrequest_async('ModifyBizItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_biz_items(
        self,
        request: linkedmall_20180116_models.ModifyBizItemsRequest,
    ) -> linkedmall_20180116_models.ModifyBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_biz_items_with_options(request, runtime)

    async def modify_biz_items_async(
        self,
        request: linkedmall_20180116_models.ModifyBizItemsRequest,
    ) -> linkedmall_20180116_models.ModifyBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_biz_items_with_options_async(request, runtime)

    def modify_item_limit_rule_with_options(
        self,
        request: linkedmall_20180116_models.ModifyItemLimitRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyItemLimitRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyItemLimitRuleResponse(),
            self.do_rpcrequest('ModifyItemLimitRule', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_item_limit_rule_with_options_async(
        self,
        request: linkedmall_20180116_models.ModifyItemLimitRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyItemLimitRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyItemLimitRuleResponse(),
            await self.do_rpcrequest_async('ModifyItemLimitRule', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_item_limit_rule(
        self,
        request: linkedmall_20180116_models.ModifyItemLimitRuleRequest,
    ) -> linkedmall_20180116_models.ModifyItemLimitRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_item_limit_rule_with_options(request, runtime)

    async def modify_item_limit_rule_async(
        self,
        request: linkedmall_20180116_models.ModifyItemLimitRuleRequest,
    ) -> linkedmall_20180116_models.ModifyItemLimitRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_item_limit_rule_with_options_async(request, runtime)

    def notify_pay_order_status_with_options(
        self,
        request: linkedmall_20180116_models.NotifyPayOrderStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.NotifyPayOrderStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.NotifyPayOrderStatusResponse(),
            self.do_rpcrequest('NotifyPayOrderStatus', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def notify_pay_order_status_with_options_async(
        self,
        request: linkedmall_20180116_models.NotifyPayOrderStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.NotifyPayOrderStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.NotifyPayOrderStatusResponse(),
            await self.do_rpcrequest_async('NotifyPayOrderStatus', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def notify_pay_order_status(
        self,
        request: linkedmall_20180116_models.NotifyPayOrderStatusRequest,
    ) -> linkedmall_20180116_models.NotifyPayOrderStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.notify_pay_order_status_with_options(request, runtime)

    async def notify_pay_order_status_async(
        self,
        request: linkedmall_20180116_models.NotifyPayOrderStatusRequest,
    ) -> linkedmall_20180116_models.NotifyPayOrderStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.notify_pay_order_status_with_options_async(request, runtime)

    def notify_withhold_fund_with_options(
        self,
        request: linkedmall_20180116_models.NotifyWithholdFundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.NotifyWithholdFundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.NotifyWithholdFundResponse(),
            self.do_rpcrequest('NotifyWithholdFund', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def notify_withhold_fund_with_options_async(
        self,
        request: linkedmall_20180116_models.NotifyWithholdFundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.NotifyWithholdFundResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.NotifyWithholdFundResponse(),
            await self.do_rpcrequest_async('NotifyWithholdFund', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def notify_withhold_fund(
        self,
        request: linkedmall_20180116_models.NotifyWithholdFundRequest,
    ) -> linkedmall_20180116_models.NotifyWithholdFundResponse:
        runtime = util_models.RuntimeOptions()
        return self.notify_withhold_fund_with_options(request, runtime)

    async def notify_withhold_fund_async(
        self,
        request: linkedmall_20180116_models.NotifyWithholdFundRequest,
    ) -> linkedmall_20180116_models.NotifyWithholdFundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.notify_withhold_fund_with_options_async(request, runtime)

    def query_activity_items_with_options(
        self,
        request: linkedmall_20180116_models.QueryActivityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryActivityItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryActivityItemsResponse(),
            self.do_rpcrequest('QueryActivityItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_activity_items_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryActivityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryActivityItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryActivityItemsResponse(),
            await self.do_rpcrequest_async('QueryActivityItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_activity_items(
        self,
        request: linkedmall_20180116_models.QueryActivityItemsRequest,
    ) -> linkedmall_20180116_models.QueryActivityItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_activity_items_with_options(request, runtime)

    async def query_activity_items_async(
        self,
        request: linkedmall_20180116_models.QueryActivityItemsRequest,
    ) -> linkedmall_20180116_models.QueryActivityItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_activity_items_with_options_async(request, runtime)

    def query_address_with_options(
        self,
        request: linkedmall_20180116_models.QueryAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressResponse(),
            self.do_rpcrequest('QueryAddress', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_address_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressResponse(),
            await self.do_rpcrequest_async('QueryAddress', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_address(
        self,
        request: linkedmall_20180116_models.QueryAddressRequest,
    ) -> linkedmall_20180116_models.QueryAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_address_with_options(request, runtime)

    async def query_address_async(
        self,
        request: linkedmall_20180116_models.QueryAddressRequest,
    ) -> linkedmall_20180116_models.QueryAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_address_with_options_async(request, runtime)

    def query_address_detail_with_options(
        self,
        request: linkedmall_20180116_models.QueryAddressDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAddressDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressDetailResponse(),
            self.do_rpcrequest('QueryAddressDetail', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_address_detail_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryAddressDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAddressDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressDetailResponse(),
            await self.do_rpcrequest_async('QueryAddressDetail', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_address_detail(
        self,
        request: linkedmall_20180116_models.QueryAddressDetailRequest,
    ) -> linkedmall_20180116_models.QueryAddressDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_address_detail_with_options(request, runtime)

    async def query_address_detail_async(
        self,
        request: linkedmall_20180116_models.QueryAddressDetailRequest,
    ) -> linkedmall_20180116_models.QueryAddressDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_address_detail_with_options_async(request, runtime)

    def query_address_list_with_options(
        self,
        request: linkedmall_20180116_models.QueryAddressListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAddressListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressListResponse(),
            self.do_rpcrequest('QueryAddressList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_address_list_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryAddressListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAddressListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressListResponse(),
            await self.do_rpcrequest_async('QueryAddressList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_address_list(
        self,
        request: linkedmall_20180116_models.QueryAddressListRequest,
    ) -> linkedmall_20180116_models.QueryAddressListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_address_list_with_options(request, runtime)

    async def query_address_list_async(
        self,
        request: linkedmall_20180116_models.QueryAddressListRequest,
    ) -> linkedmall_20180116_models.QueryAddressListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_address_list_with_options_async(request, runtime)

    def query_advertisement_settle_info_with_options(
        self,
        request: linkedmall_20180116_models.QueryAdvertisementSettleInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAdvertisementSettleInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAdvertisementSettleInfoResponse(),
            self.do_rpcrequest('QueryAdvertisementSettleInfo', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_advertisement_settle_info_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryAdvertisementSettleInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAdvertisementSettleInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAdvertisementSettleInfoResponse(),
            await self.do_rpcrequest_async('QueryAdvertisementSettleInfo', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_advertisement_settle_info(
        self,
        request: linkedmall_20180116_models.QueryAdvertisementSettleInfoRequest,
    ) -> linkedmall_20180116_models.QueryAdvertisementSettleInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_advertisement_settle_info_with_options(request, runtime)

    async def query_advertisement_settle_info_async(
        self,
        request: linkedmall_20180116_models.QueryAdvertisementSettleInfoRequest,
    ) -> linkedmall_20180116_models.QueryAdvertisementSettleInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_advertisement_settle_info_with_options_async(request, runtime)

    def query_agreement_with_options(
        self,
        request: linkedmall_20180116_models.QueryAgreementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAgreementResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAgreementResponse(),
            self.do_rpcrequest('QueryAgreement', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_agreement_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryAgreementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAgreementResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAgreementResponse(),
            await self.do_rpcrequest_async('QueryAgreement', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_agreement(
        self,
        request: linkedmall_20180116_models.QueryAgreementRequest,
    ) -> linkedmall_20180116_models.QueryAgreementResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_agreement_with_options(request, runtime)

    async def query_agreement_async(
        self,
        request: linkedmall_20180116_models.QueryAgreementRequest,
    ) -> linkedmall_20180116_models.QueryAgreementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_agreement_with_options_async(request, runtime)

    def query_all_cinemas_with_options(
        self,
        request: linkedmall_20180116_models.QueryAllCinemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAllCinemasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAllCinemasResponse(),
            self.do_rpcrequest('QueryAllCinemas', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_all_cinemas_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryAllCinemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAllCinemasResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAllCinemasResponse(),
            await self.do_rpcrequest_async('QueryAllCinemas', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_all_cinemas(
        self,
        request: linkedmall_20180116_models.QueryAllCinemasRequest,
    ) -> linkedmall_20180116_models.QueryAllCinemasResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_all_cinemas_with_options(request, runtime)

    async def query_all_cinemas_async(
        self,
        request: linkedmall_20180116_models.QueryAllCinemasRequest,
    ) -> linkedmall_20180116_models.QueryAllCinemasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_all_cinemas_with_options_async(request, runtime)

    def query_all_cities_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryAllCitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAllCitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryAllCitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_json):
            request.ext_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_json, 'ExtJson', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAllCitiesResponse(),
            self.do_rpcrequest('QueryAllCities', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_all_cities_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryAllCitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAllCitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryAllCitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_json):
            request.ext_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_json, 'ExtJson', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAllCitiesResponse(),
            await self.do_rpcrequest_async('QueryAllCities', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_all_cities(
        self,
        request: linkedmall_20180116_models.QueryAllCitiesRequest,
    ) -> linkedmall_20180116_models.QueryAllCitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_all_cities_with_options(request, runtime)

    async def query_all_cities_async(
        self,
        request: linkedmall_20180116_models.QueryAllCitiesRequest,
    ) -> linkedmall_20180116_models.QueryAllCitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_all_cities_with_options_async(request, runtime)

    def query_batch_regist_anonymous_tb_account_result_with_options(
        self,
        request: linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultResponse(),
            self.do_rpcrequest('QueryBatchRegistAnonymousTbAccountResult', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_batch_regist_anonymous_tb_account_result_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultResponse(),
            await self.do_rpcrequest_async('QueryBatchRegistAnonymousTbAccountResult', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_batch_regist_anonymous_tb_account_result(
        self,
        request: linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultRequest,
    ) -> linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_batch_regist_anonymous_tb_account_result_with_options(request, runtime)

    async def query_batch_regist_anonymous_tb_account_result_async(
        self,
        request: linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultRequest,
    ) -> linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_batch_regist_anonymous_tb_account_result_with_options_async(request, runtime)

    def query_best_session_4items_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryBestSession4ItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBestSession4ItemsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBestSession4ItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBestSession4ItemsResponse(),
            self.do_rpcrequest('QueryBestSession4Items', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_best_session_4items_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryBestSession4ItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBestSession4ItemsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBestSession4ItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBestSession4ItemsResponse(),
            await self.do_rpcrequest_async('QueryBestSession4Items', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_best_session_4items(
        self,
        request: linkedmall_20180116_models.QueryBestSession4ItemsRequest,
    ) -> linkedmall_20180116_models.QueryBestSession4ItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_best_session_4items_with_options(request, runtime)

    async def query_best_session_4items_async(
        self,
        request: linkedmall_20180116_models.QueryBestSession4ItemsRequest,
    ) -> linkedmall_20180116_models.QueryBestSession4ItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_best_session_4items_with_options_async(request, runtime)

    def query_biz_item_list_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryBizItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemListResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemListResponse(),
            self.do_rpcrequest('QueryBizItemList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_biz_item_list_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryBizItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemListResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemListResponse(),
            await self.do_rpcrequest_async('QueryBizItemList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_biz_item_list(
        self,
        request: linkedmall_20180116_models.QueryBizItemListRequest,
    ) -> linkedmall_20180116_models.QueryBizItemListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_biz_item_list_with_options(request, runtime)

    async def query_biz_item_list_async(
        self,
        request: linkedmall_20180116_models.QueryBizItemListRequest,
    ) -> linkedmall_20180116_models.QueryBizItemListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_biz_item_list_with_options_async(request, runtime)

    def query_biz_items_with_options(
        self,
        request: linkedmall_20180116_models.QueryBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemsResponse(),
            self.do_rpcrequest('QueryBizItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_biz_items_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemsResponse(),
            await self.do_rpcrequest_async('QueryBizItems', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_biz_items(
        self,
        request: linkedmall_20180116_models.QueryBizItemsRequest,
    ) -> linkedmall_20180116_models.QueryBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_biz_items_with_options(request, runtime)

    async def query_biz_items_async(
        self,
        request: linkedmall_20180116_models.QueryBizItemsRequest,
    ) -> linkedmall_20180116_models.QueryBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_biz_items_with_options_async(request, runtime)

    def query_biz_items_with_activity_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryBizItemsWithActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemsWithActivityResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemsWithActivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemsWithActivityResponse(),
            self.do_rpcrequest('QueryBizItemsWithActivity', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_biz_items_with_activity_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryBizItemsWithActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemsWithActivityResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemsWithActivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemsWithActivityResponse(),
            await self.do_rpcrequest_async('QueryBizItemsWithActivity', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_biz_items_with_activity(
        self,
        request: linkedmall_20180116_models.QueryBizItemsWithActivityRequest,
    ) -> linkedmall_20180116_models.QueryBizItemsWithActivityResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_biz_items_with_activity_with_options(request, runtime)

    async def query_biz_items_with_activity_async(
        self,
        request: linkedmall_20180116_models.QueryBizItemsWithActivityRequest,
    ) -> linkedmall_20180116_models.QueryBizItemsWithActivityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_biz_items_with_activity_with_options_async(request, runtime)

    def query_guide_item_group_with_options(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryGuideItemGroupResponse(),
            self.do_rpcrequest('QueryGuideItemGroup', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_guide_item_group_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryGuideItemGroupResponse(),
            await self.do_rpcrequest_async('QueryGuideItemGroup', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_guide_item_group(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupRequest,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_guide_item_group_with_options(request, runtime)

    async def query_guide_item_group_async(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupRequest,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_guide_item_group_with_options_async(request, runtime)

    def query_guide_item_group_with_out_inventory_with_options(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryResponse(),
            self.do_rpcrequest('QueryGuideItemGroupWithOutInventory', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_guide_item_group_with_out_inventory_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryResponse(),
            await self.do_rpcrequest_async('QueryGuideItemGroupWithOutInventory', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_guide_item_group_with_out_inventory(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryRequest,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_guide_item_group_with_out_inventory_with_options(request, runtime)

    async def query_guide_item_group_with_out_inventory_async(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryRequest,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_guide_item_group_with_out_inventory_with_options_async(request, runtime)

    def query_hot_movies_with_options(
        self,
        request: linkedmall_20180116_models.QueryHotMoviesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryHotMoviesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryHotMoviesResponse(),
            self.do_rpcrequest('QueryHotMovies', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_hot_movies_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryHotMoviesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryHotMoviesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryHotMoviesResponse(),
            await self.do_rpcrequest_async('QueryHotMovies', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_hot_movies(
        self,
        request: linkedmall_20180116_models.QueryHotMoviesRequest,
    ) -> linkedmall_20180116_models.QueryHotMoviesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_hot_movies_with_options(request, runtime)

    async def query_hot_movies_async(
        self,
        request: linkedmall_20180116_models.QueryHotMoviesRequest,
    ) -> linkedmall_20180116_models.QueryHotMoviesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_hot_movies_with_options_async(request, runtime)

    def query_inventory_of_items_in_biz_item_group_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupResponse(),
            self.do_rpcrequest('QueryInventoryOfItemsInBizItemGroup', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_inventory_of_items_in_biz_item_group_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupResponse(),
            await self.do_rpcrequest_async('QueryInventoryOfItemsInBizItemGroup', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_inventory_of_items_in_biz_item_group(
        self,
        request: linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupRequest,
    ) -> linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_inventory_of_items_in_biz_item_group_with_options(request, runtime)

    async def query_inventory_of_items_in_biz_item_group_async(
        self,
        request: linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupRequest,
    ) -> linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_inventory_of_items_in_biz_item_group_with_options_async(request, runtime)

    def query_item_detail_with_options(
        self,
        request: linkedmall_20180116_models.QueryItemDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemDetailResponse(),
            self.do_rpcrequest('QueryItemDetail', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_item_detail_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryItemDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemDetailResponse(),
            await self.do_rpcrequest_async('QueryItemDetail', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_item_detail(
        self,
        request: linkedmall_20180116_models.QueryItemDetailRequest,
    ) -> linkedmall_20180116_models.QueryItemDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_item_detail_with_options(request, runtime)

    async def query_item_detail_async(
        self,
        request: linkedmall_20180116_models.QueryItemDetailRequest,
    ) -> linkedmall_20180116_models.QueryItemDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_item_detail_with_options_async(request, runtime)

    def query_item_detail_inner_with_options(
        self,
        request: linkedmall_20180116_models.QueryItemDetailInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemDetailInnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemDetailInnerResponse(),
            self.do_rpcrequest('QueryItemDetailInner', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_item_detail_inner_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryItemDetailInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemDetailInnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemDetailInnerResponse(),
            await self.do_rpcrequest_async('QueryItemDetailInner', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_item_detail_inner(
        self,
        request: linkedmall_20180116_models.QueryItemDetailInnerRequest,
    ) -> linkedmall_20180116_models.QueryItemDetailInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_item_detail_inner_with_options(request, runtime)

    async def query_item_detail_inner_async(
        self,
        request: linkedmall_20180116_models.QueryItemDetailInnerRequest,
    ) -> linkedmall_20180116_models.QueryItemDetailInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_item_detail_inner_with_options_async(request, runtime)

    def query_item_in_sub_bizs_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryItemInSubBizsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemInSubBizsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryItemInSubBizsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_biz_ids):
            request.sub_biz_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_biz_ids, 'SubBizIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemInSubBizsResponse(),
            self.do_rpcrequest('QueryItemInSubBizs', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_item_in_sub_bizs_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryItemInSubBizsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemInSubBizsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryItemInSubBizsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_biz_ids):
            request.sub_biz_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_biz_ids, 'SubBizIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemInSubBizsResponse(),
            await self.do_rpcrequest_async('QueryItemInSubBizs', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_item_in_sub_bizs(
        self,
        request: linkedmall_20180116_models.QueryItemInSubBizsRequest,
    ) -> linkedmall_20180116_models.QueryItemInSubBizsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_item_in_sub_bizs_with_options(request, runtime)

    async def query_item_in_sub_bizs_async(
        self,
        request: linkedmall_20180116_models.QueryItemInSubBizsRequest,
    ) -> linkedmall_20180116_models.QueryItemInSubBizsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_item_in_sub_bizs_with_options_async(request, runtime)

    def query_item_inventory_with_options(
        self,
        request: linkedmall_20180116_models.QueryItemInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemInventoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemInventoryResponse(),
            self.do_rpcrequest('QueryItemInventory', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_item_inventory_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryItemInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemInventoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemInventoryResponse(),
            await self.do_rpcrequest_async('QueryItemInventory', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_item_inventory(
        self,
        request: linkedmall_20180116_models.QueryItemInventoryRequest,
    ) -> linkedmall_20180116_models.QueryItemInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_item_inventory_with_options(request, runtime)

    async def query_item_inventory_async(
        self,
        request: linkedmall_20180116_models.QueryItemInventoryRequest,
    ) -> linkedmall_20180116_models.QueryItemInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_item_inventory_with_options_async(request, runtime)

    def query_logistics_with_options(
        self,
        request: linkedmall_20180116_models.QueryLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryLogisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryLogisticsResponse(),
            self.do_rpcrequest('QueryLogistics', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_logistics_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryLogisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryLogisticsResponse(),
            await self.do_rpcrequest_async('QueryLogistics', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_logistics(
        self,
        request: linkedmall_20180116_models.QueryLogisticsRequest,
    ) -> linkedmall_20180116_models.QueryLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_logistics_with_options(request, runtime)

    async def query_logistics_async(
        self,
        request: linkedmall_20180116_models.QueryLogisticsRequest,
    ) -> linkedmall_20180116_models.QueryLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_logistics_with_options_async(request, runtime)

    def query_media_settle_info_with_options(
        self,
        request: linkedmall_20180116_models.QueryMediaSettleInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMediaSettleInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMediaSettleInfoResponse(),
            self.do_rpcrequest('QueryMediaSettleInfo', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_media_settle_info_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryMediaSettleInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMediaSettleInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMediaSettleInfoResponse(),
            await self.do_rpcrequest_async('QueryMediaSettleInfo', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_media_settle_info(
        self,
        request: linkedmall_20180116_models.QueryMediaSettleInfoRequest,
    ) -> linkedmall_20180116_models.QueryMediaSettleInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_media_settle_info_with_options(request, runtime)

    async def query_media_settle_info_async(
        self,
        request: linkedmall_20180116_models.QueryMediaSettleInfoRequest,
    ) -> linkedmall_20180116_models.QueryMediaSettleInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_media_settle_info_with_options_async(request, runtime)

    def query_messages_with_options(
        self,
        request: linkedmall_20180116_models.QueryMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMessagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMessagesResponse(),
            self.do_rpcrequest('QueryMessages', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_messages_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMessagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMessagesResponse(),
            await self.do_rpcrequest_async('QueryMessages', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_messages(
        self,
        request: linkedmall_20180116_models.QueryMessagesRequest,
    ) -> linkedmall_20180116_models.QueryMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_messages_with_options(request, runtime)

    async def query_messages_async(
        self,
        request: linkedmall_20180116_models.QueryMessagesRequest,
    ) -> linkedmall_20180116_models.QueryMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_messages_with_options_async(request, runtime)

    def query_movie_comments_with_options(
        self,
        request: linkedmall_20180116_models.QueryMovieCommentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieCommentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieCommentsResponse(),
            self.do_rpcrequest('QueryMovieComments', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_movie_comments_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryMovieCommentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieCommentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieCommentsResponse(),
            await self.do_rpcrequest_async('QueryMovieComments', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_movie_comments(
        self,
        request: linkedmall_20180116_models.QueryMovieCommentsRequest,
    ) -> linkedmall_20180116_models.QueryMovieCommentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_movie_comments_with_options(request, runtime)

    async def query_movie_comments_async(
        self,
        request: linkedmall_20180116_models.QueryMovieCommentsRequest,
    ) -> linkedmall_20180116_models.QueryMovieCommentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_movie_comments_with_options_async(request, runtime)

    def query_movie_schedules_with_options(
        self,
        request: linkedmall_20180116_models.QueryMovieSchedulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieSchedulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieSchedulesResponse(),
            self.do_rpcrequest('QueryMovieSchedules', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_movie_schedules_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryMovieSchedulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieSchedulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieSchedulesResponse(),
            await self.do_rpcrequest_async('QueryMovieSchedules', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_movie_schedules(
        self,
        request: linkedmall_20180116_models.QueryMovieSchedulesRequest,
    ) -> linkedmall_20180116_models.QueryMovieSchedulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_movie_schedules_with_options(request, runtime)

    async def query_movie_schedules_async(
        self,
        request: linkedmall_20180116_models.QueryMovieSchedulesRequest,
    ) -> linkedmall_20180116_models.QueryMovieSchedulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_movie_schedules_with_options_async(request, runtime)

    def query_movie_seats_with_options(
        self,
        request: linkedmall_20180116_models.QueryMovieSeatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieSeatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieSeatsResponse(),
            self.do_rpcrequest('QueryMovieSeats', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_movie_seats_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryMovieSeatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieSeatsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieSeatsResponse(),
            await self.do_rpcrequest_async('QueryMovieSeats', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_movie_seats(
        self,
        request: linkedmall_20180116_models.QueryMovieSeatsRequest,
    ) -> linkedmall_20180116_models.QueryMovieSeatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_movie_seats_with_options(request, runtime)

    async def query_movie_seats_async(
        self,
        request: linkedmall_20180116_models.QueryMovieSeatsRequest,
    ) -> linkedmall_20180116_models.QueryMovieSeatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_movie_seats_with_options_async(request, runtime)

    def query_movie_tickets_with_options(
        self,
        request: linkedmall_20180116_models.QueryMovieTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieTicketsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieTicketsResponse(),
            self.do_rpcrequest('QueryMovieTickets', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_movie_tickets_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryMovieTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieTicketsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieTicketsResponse(),
            await self.do_rpcrequest_async('QueryMovieTickets', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_movie_tickets(
        self,
        request: linkedmall_20180116_models.QueryMovieTicketsRequest,
    ) -> linkedmall_20180116_models.QueryMovieTicketsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_movie_tickets_with_options(request, runtime)

    async def query_movie_tickets_async(
        self,
        request: linkedmall_20180116_models.QueryMovieTicketsRequest,
    ) -> linkedmall_20180116_models.QueryMovieTicketsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_movie_tickets_with_options_async(request, runtime)

    def query_order_and_payment_list_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderAndPaymentListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderAndPaymentListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderAndPaymentListResponse(),
            self.do_rpcrequest('QueryOrderAndPaymentList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_order_and_payment_list_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderAndPaymentListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderAndPaymentListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderAndPaymentListResponse(),
            await self.do_rpcrequest_async('QueryOrderAndPaymentList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_and_payment_list(
        self,
        request: linkedmall_20180116_models.QueryOrderAndPaymentListRequest,
    ) -> linkedmall_20180116_models.QueryOrderAndPaymentListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_and_payment_list_with_options(request, runtime)

    async def query_order_and_payment_list_async(
        self,
        request: linkedmall_20180116_models.QueryOrderAndPaymentListRequest,
    ) -> linkedmall_20180116_models.QueryOrderAndPaymentListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_and_payment_list_with_options_async(request, runtime)

    def query_order_commission_rate_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderCommissionRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderCommissionRateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderCommissionRateResponse(),
            self.do_rpcrequest('QueryOrderCommissionRate', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_order_commission_rate_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderCommissionRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderCommissionRateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderCommissionRateResponse(),
            await self.do_rpcrequest_async('QueryOrderCommissionRate', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_commission_rate(
        self,
        request: linkedmall_20180116_models.QueryOrderCommissionRateRequest,
    ) -> linkedmall_20180116_models.QueryOrderCommissionRateResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_commission_rate_with_options(request, runtime)

    async def query_order_commission_rate_async(
        self,
        request: linkedmall_20180116_models.QueryOrderCommissionRateRequest,
    ) -> linkedmall_20180116_models.QueryOrderCommissionRateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_commission_rate_with_options_async(request, runtime)

    def query_order_detail_inner_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderDetailInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderDetailInnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderDetailInnerResponse(),
            self.do_rpcrequest('QueryOrderDetailInner', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_order_detail_inner_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderDetailInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderDetailInnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderDetailInnerResponse(),
            await self.do_rpcrequest_async('QueryOrderDetailInner', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_detail_inner(
        self,
        request: linkedmall_20180116_models.QueryOrderDetailInnerRequest,
    ) -> linkedmall_20180116_models.QueryOrderDetailInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_detail_inner_with_options(request, runtime)

    async def query_order_detail_inner_async(
        self,
        request: linkedmall_20180116_models.QueryOrderDetailInnerRequest,
    ) -> linkedmall_20180116_models.QueryOrderDetailInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_detail_inner_with_options_async(request, runtime)

    def query_order_id_by_pay_id_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderIdByPayIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderIdByPayIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderIdByPayIdResponse(),
            self.do_rpcrequest('QueryOrderIdByPayId', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_order_id_by_pay_id_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderIdByPayIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderIdByPayIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderIdByPayIdResponse(),
            await self.do_rpcrequest_async('QueryOrderIdByPayId', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_id_by_pay_id(
        self,
        request: linkedmall_20180116_models.QueryOrderIdByPayIdRequest,
    ) -> linkedmall_20180116_models.QueryOrderIdByPayIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_id_by_pay_id_with_options(request, runtime)

    async def query_order_id_by_pay_id_async(
        self,
        request: linkedmall_20180116_models.QueryOrderIdByPayIdRequest,
    ) -> linkedmall_20180116_models.QueryOrderIdByPayIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_id_by_pay_id_with_options_async(request, runtime)

    def query_order_info_after_sale_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderInfoAfterSaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderInfoAfterSaleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderInfoAfterSaleResponse(),
            self.do_rpcrequest('QueryOrderInfoAfterSale', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_order_info_after_sale_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderInfoAfterSaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderInfoAfterSaleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderInfoAfterSaleResponse(),
            await self.do_rpcrequest_async('QueryOrderInfoAfterSale', '2018-01-16', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_order_info_after_sale(
        self,
        request: linkedmall_20180116_models.QueryOrderInfoAfterSaleRequest,
    ) -> linkedmall_20180116_models.QueryOrderInfoAfterSaleResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_info_after_sale_with_options(request, runtime)

    async def query_order_info_after_sale_async(
        self,
        request: linkedmall_20180116_models.QueryOrderInfoAfterSaleRequest,
    ) -> linkedmall_20180116_models.QueryOrderInfoAfterSaleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_info_after_sale_with_options_async(request, runtime)

    def query_order_item_info_by_payment_id_for_ai_zhan_you_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouResponse(),
            self.do_rpcrequest('QueryOrderItemInfoByPaymentIdForAiZhanYou', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_order_item_info_by_payment_id_for_ai_zhan_you_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouResponse(),
            await self.do_rpcrequest_async('QueryOrderItemInfoByPaymentIdForAiZhanYou', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_item_info_by_payment_id_for_ai_zhan_you(
        self,
        request: linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouRequest,
    ) -> linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_item_info_by_payment_id_for_ai_zhan_you_with_options(request, runtime)

    async def query_order_item_info_by_payment_id_for_ai_zhan_you_async(
        self,
        request: linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouRequest,
    ) -> linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_item_info_by_payment_id_for_ai_zhan_you_with_options_async(request, runtime)

    def query_order_list_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderListResponse(),
            self.do_rpcrequest('QueryOrderList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_order_list_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderListResponse(),
            await self.do_rpcrequest_async('QueryOrderList', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_list(
        self,
        request: linkedmall_20180116_models.QueryOrderListRequest,
    ) -> linkedmall_20180116_models.QueryOrderListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_list_with_options(request, runtime)

    async def query_order_list_async(
        self,
        request: linkedmall_20180116_models.QueryOrderListRequest,
    ) -> linkedmall_20180116_models.QueryOrderListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_list_with_options_async(request, runtime)

    def query_order_logistics_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderLogisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderLogisticsResponse(),
            self.do_rpcrequest('QueryOrderLogistics', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_order_logistics_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderLogisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderLogisticsResponse(),
            await self.do_rpcrequest_async('QueryOrderLogistics', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_order_logistics(
        self,
        request: linkedmall_20180116_models.QueryOrderLogisticsRequest,
    ) -> linkedmall_20180116_models.QueryOrderLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_logistics_with_options(request, runtime)

    async def query_order_logistics_async(
        self,
        request: linkedmall_20180116_models.QueryOrderLogisticsRequest,
    ) -> linkedmall_20180116_models.QueryOrderLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_logistics_with_options_async(request, runtime)

    def query_refund_application_detail_with_options(
        self,
        request: linkedmall_20180116_models.QueryRefundApplicationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryRefundApplicationDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryRefundApplicationDetailResponse(),
            self.do_rpcrequest('QueryRefundApplicationDetail', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_refund_application_detail_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryRefundApplicationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryRefundApplicationDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryRefundApplicationDetailResponse(),
            await self.do_rpcrequest_async('QueryRefundApplicationDetail', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_refund_application_detail(
        self,
        request: linkedmall_20180116_models.QueryRefundApplicationDetailRequest,
    ) -> linkedmall_20180116_models.QueryRefundApplicationDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_refund_application_detail_with_options(request, runtime)

    async def query_refund_application_detail_async(
        self,
        request: linkedmall_20180116_models.QueryRefundApplicationDetailRequest,
    ) -> linkedmall_20180116_models.QueryRefundApplicationDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_refund_application_detail_with_options_async(request, runtime)

    def query_statements_with_options(
        self,
        request: linkedmall_20180116_models.QueryStatementsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryStatementsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryStatementsResponse(),
            self.do_rpcrequest('QueryStatements', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_statements_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryStatementsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryStatementsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryStatementsResponse(),
            await self.do_rpcrequest_async('QueryStatements', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_statements(
        self,
        request: linkedmall_20180116_models.QueryStatementsRequest,
    ) -> linkedmall_20180116_models.QueryStatementsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_statements_with_options(request, runtime)

    async def query_statements_async(
        self,
        request: linkedmall_20180116_models.QueryStatementsRequest,
    ) -> linkedmall_20180116_models.QueryStatementsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_statements_with_options_async(request, runtime)

    def query_unfinished_activities_with_options(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUnfinishedActivitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedActivitiesResponse(),
            self.do_rpcrequest('QueryUnfinishedActivities', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_unfinished_activities_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUnfinishedActivitiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedActivitiesResponse(),
            await self.do_rpcrequest_async('QueryUnfinishedActivities', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_unfinished_activities(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedActivitiesRequest,
    ) -> linkedmall_20180116_models.QueryUnfinishedActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_unfinished_activities_with_options(request, runtime)

    async def query_unfinished_activities_async(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedActivitiesRequest,
    ) -> linkedmall_20180116_models.QueryUnfinishedActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_unfinished_activities_with_options_async(request, runtime)

    def query_unfinished_sessions_with_options(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedSessionsResponse(),
            self.do_rpcrequest('QueryUnfinishedSessions', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_unfinished_sessions_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedSessionsResponse(),
            await self.do_rpcrequest_async('QueryUnfinishedSessions', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_unfinished_sessions(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedSessionsRequest,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_unfinished_sessions_with_options(request, runtime)

    async def query_unfinished_sessions_async(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedSessionsRequest,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_unfinished_sessions_with_options_async(request, runtime)

    def query_unfinished_sessions_4items_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryUnfinishedSessions4ItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessions4ItemsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUnfinishedSessions4ItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedSessions4ItemsResponse(),
            self.do_rpcrequest('QueryUnfinishedSessions4Items', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_unfinished_sessions_4items_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryUnfinishedSessions4ItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessions4ItemsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUnfinishedSessions4ItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedSessions4ItemsResponse(),
            await self.do_rpcrequest_async('QueryUnfinishedSessions4Items', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_unfinished_sessions_4items(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedSessions4ItemsRequest,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessions4ItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_unfinished_sessions_4items_with_options(request, runtime)

    async def query_unfinished_sessions_4items_async(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedSessions4ItemsRequest,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessions4ItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_unfinished_sessions_4items_with_options_async(request, runtime)

    def query_upcoming_movies_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryUpcomingMoviesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUpcomingMoviesResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUpcomingMoviesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_json):
            request.ext_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_json, 'ExtJson', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUpcomingMoviesResponse(),
            self.do_rpcrequest('QueryUpcomingMovies', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_upcoming_movies_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryUpcomingMoviesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUpcomingMoviesResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUpcomingMoviesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_json):
            request.ext_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_json, 'ExtJson', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUpcomingMoviesResponse(),
            await self.do_rpcrequest_async('QueryUpcomingMovies', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_upcoming_movies(
        self,
        request: linkedmall_20180116_models.QueryUpcomingMoviesRequest,
    ) -> linkedmall_20180116_models.QueryUpcomingMoviesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_upcoming_movies_with_options(request, runtime)

    async def query_upcoming_movies_async(
        self,
        request: linkedmall_20180116_models.QueryUpcomingMoviesRequest,
    ) -> linkedmall_20180116_models.QueryUpcomingMoviesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_upcoming_movies_with_options_async(request, runtime)

    def query_withhold_trade_with_options(
        self,
        request: linkedmall_20180116_models.QueryWithholdTradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryWithholdTradeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryWithholdTradeResponse(),
            self.do_rpcrequest('QueryWithholdTrade', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_withhold_trade_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryWithholdTradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryWithholdTradeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryWithholdTradeResponse(),
            await self.do_rpcrequest_async('QueryWithholdTrade', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_withhold_trade(
        self,
        request: linkedmall_20180116_models.QueryWithholdTradeRequest,
    ) -> linkedmall_20180116_models.QueryWithholdTradeResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_withhold_trade_with_options(request, runtime)

    async def query_withhold_trade_async(
        self,
        request: linkedmall_20180116_models.QueryWithholdTradeRequest,
    ) -> linkedmall_20180116_models.QueryWithholdTradeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_withhold_trade_with_options_async(request, runtime)

    def refund_order_with_options(
        self,
        request: linkedmall_20180116_models.RefundOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefundOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefundOrderResponse(),
            self.do_rpcrequest('RefundOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refund_order_with_options_async(
        self,
        request: linkedmall_20180116_models.RefundOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefundOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefundOrderResponse(),
            await self.do_rpcrequest_async('RefundOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund_order(
        self,
        request: linkedmall_20180116_models.RefundOrderRequest,
    ) -> linkedmall_20180116_models.RefundOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_order_with_options(request, runtime)

    async def refund_order_async(
        self,
        request: linkedmall_20180116_models.RefundOrderRequest,
    ) -> linkedmall_20180116_models.RefundOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_order_with_options_async(request, runtime)

    def refund_point_with_options(
        self,
        request: linkedmall_20180116_models.RefundPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefundPointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefundPointResponse(),
            self.do_rpcrequest('RefundPoint', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refund_point_with_options_async(
        self,
        request: linkedmall_20180116_models.RefundPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefundPointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefundPointResponse(),
            await self.do_rpcrequest_async('RefundPoint', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refund_point(
        self,
        request: linkedmall_20180116_models.RefundPointRequest,
    ) -> linkedmall_20180116_models.RefundPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_point_with_options(request, runtime)

    async def refund_point_async(
        self,
        request: linkedmall_20180116_models.RefundPointRequest,
    ) -> linkedmall_20180116_models.RefundPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_point_with_options_async(request, runtime)

    def refuse_merchant_sync_task_with_options(
        self,
        request: linkedmall_20180116_models.RefuseMerchantSyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefuseMerchantSyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefuseMerchantSyncTaskResponse(),
            self.do_rpcrequest('RefuseMerchantSyncTask', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refuse_merchant_sync_task_with_options_async(
        self,
        request: linkedmall_20180116_models.RefuseMerchantSyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefuseMerchantSyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefuseMerchantSyncTaskResponse(),
            await self.do_rpcrequest_async('RefuseMerchantSyncTask', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refuse_merchant_sync_task(
        self,
        request: linkedmall_20180116_models.RefuseMerchantSyncTaskRequest,
    ) -> linkedmall_20180116_models.RefuseMerchantSyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.refuse_merchant_sync_task_with_options(request, runtime)

    async def refuse_merchant_sync_task_async(
        self,
        request: linkedmall_20180116_models.RefuseMerchantSyncTaskRequest,
    ) -> linkedmall_20180116_models.RefuseMerchantSyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refuse_merchant_sync_task_with_options_async(request, runtime)

    def regist_anonymous_tb_account_with_options(
        self,
        request: linkedmall_20180116_models.RegistAnonymousTbAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RegistAnonymousTbAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RegistAnonymousTbAccountResponse(),
            self.do_rpcrequest('RegistAnonymousTbAccount', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def regist_anonymous_tb_account_with_options_async(
        self,
        request: linkedmall_20180116_models.RegistAnonymousTbAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RegistAnonymousTbAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RegistAnonymousTbAccountResponse(),
            await self.do_rpcrequest_async('RegistAnonymousTbAccount', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def regist_anonymous_tb_account(
        self,
        request: linkedmall_20180116_models.RegistAnonymousTbAccountRequest,
    ) -> linkedmall_20180116_models.RegistAnonymousTbAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.regist_anonymous_tb_account_with_options(request, runtime)

    async def regist_anonymous_tb_account_async(
        self,
        request: linkedmall_20180116_models.RegistAnonymousTbAccountRequest,
    ) -> linkedmall_20180116_models.RegistAnonymousTbAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.regist_anonymous_tb_account_with_options_async(request, runtime)

    def release_movie_seat_with_options(
        self,
        request: linkedmall_20180116_models.ReleaseMovieSeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ReleaseMovieSeatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ReleaseMovieSeatResponse(),
            self.do_rpcrequest('ReleaseMovieSeat', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_movie_seat_with_options_async(
        self,
        request: linkedmall_20180116_models.ReleaseMovieSeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ReleaseMovieSeatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ReleaseMovieSeatResponse(),
            await self.do_rpcrequest_async('ReleaseMovieSeat', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_movie_seat(
        self,
        request: linkedmall_20180116_models.ReleaseMovieSeatRequest,
    ) -> linkedmall_20180116_models.ReleaseMovieSeatResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_movie_seat_with_options(request, runtime)

    async def release_movie_seat_async(
        self,
        request: linkedmall_20180116_models.ReleaseMovieSeatRequest,
    ) -> linkedmall_20180116_models.ReleaseMovieSeatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_movie_seat_with_options_async(request, runtime)

    def remove_address_with_options(
        self,
        request: linkedmall_20180116_models.RemoveAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RemoveAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RemoveAddressResponse(),
            self.do_rpcrequest('RemoveAddress', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_address_with_options_async(
        self,
        request: linkedmall_20180116_models.RemoveAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RemoveAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RemoveAddressResponse(),
            await self.do_rpcrequest_async('RemoveAddress', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_address(
        self,
        request: linkedmall_20180116_models.RemoveAddressRequest,
    ) -> linkedmall_20180116_models.RemoveAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_address_with_options(request, runtime)

    async def remove_address_async(
        self,
        request: linkedmall_20180116_models.RemoveAddressRequest,
    ) -> linkedmall_20180116_models.RemoveAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_address_with_options_async(request, runtime)

    def remove_messages_with_options(
        self,
        request: linkedmall_20180116_models.RemoveMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RemoveMessagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RemoveMessagesResponse(),
            self.do_rpcrequest('RemoveMessages', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_messages_with_options_async(
        self,
        request: linkedmall_20180116_models.RemoveMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RemoveMessagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RemoveMessagesResponse(),
            await self.do_rpcrequest_async('RemoveMessages', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_messages(
        self,
        request: linkedmall_20180116_models.RemoveMessagesRequest,
    ) -> linkedmall_20180116_models.RemoveMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_messages_with_options(request, runtime)

    async def remove_messages_async(
        self,
        request: linkedmall_20180116_models.RemoveMessagesRequest,
    ) -> linkedmall_20180116_models.RemoveMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_messages_with_options_async(request, runtime)

    def render_h5order_with_options(
        self,
        request: linkedmall_20180116_models.RenderH5OrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RenderH5OrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RenderH5OrderResponse(),
            self.do_rpcrequest('RenderH5Order', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def render_h5order_with_options_async(
        self,
        request: linkedmall_20180116_models.RenderH5OrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RenderH5OrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RenderH5OrderResponse(),
            await self.do_rpcrequest_async('RenderH5Order', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def render_h5order(
        self,
        request: linkedmall_20180116_models.RenderH5OrderRequest,
    ) -> linkedmall_20180116_models.RenderH5OrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.render_h5order_with_options(request, runtime)

    async def render_h5order_async(
        self,
        request: linkedmall_20180116_models.RenderH5OrderRequest,
    ) -> linkedmall_20180116_models.RenderH5OrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.render_h5order_with_options_async(request, runtime)

    def render_order_with_options(
        self,
        request: linkedmall_20180116_models.RenderOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RenderOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RenderOrderResponse(),
            self.do_rpcrequest('RenderOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def render_order_with_options_async(
        self,
        request: linkedmall_20180116_models.RenderOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RenderOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RenderOrderResponse(),
            await self.do_rpcrequest_async('RenderOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def render_order(
        self,
        request: linkedmall_20180116_models.RenderOrderRequest,
    ) -> linkedmall_20180116_models.RenderOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.render_order_with_options(request, runtime)

    async def render_order_async(
        self,
        request: linkedmall_20180116_models.RenderOrderRequest,
    ) -> linkedmall_20180116_models.RenderOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.render_order_with_options_async(request, runtime)

    def repay_for_pay_url_with_options(
        self,
        request: linkedmall_20180116_models.RepayForPayUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RepayForPayUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RepayForPayUrlResponse(),
            self.do_rpcrequest('RepayForPayUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def repay_for_pay_url_with_options_async(
        self,
        request: linkedmall_20180116_models.RepayForPayUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RepayForPayUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RepayForPayUrlResponse(),
            await self.do_rpcrequest_async('RepayForPayUrl', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def repay_for_pay_url(
        self,
        request: linkedmall_20180116_models.RepayForPayUrlRequest,
    ) -> linkedmall_20180116_models.RepayForPayUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.repay_for_pay_url_with_options(request, runtime)

    async def repay_for_pay_url_async(
        self,
        request: linkedmall_20180116_models.RepayForPayUrlRequest,
    ) -> linkedmall_20180116_models.RepayForPayUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.repay_for_pay_url_with_options_async(request, runtime)

    def repay_order_with_options(
        self,
        request: linkedmall_20180116_models.RepayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RepayOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RepayOrderResponse(),
            self.do_rpcrequest('RepayOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def repay_order_with_options_async(
        self,
        request: linkedmall_20180116_models.RepayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RepayOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RepayOrderResponse(),
            await self.do_rpcrequest_async('RepayOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def repay_order(
        self,
        request: linkedmall_20180116_models.RepayOrderRequest,
    ) -> linkedmall_20180116_models.RepayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.repay_order_with_options(request, runtime)

    async def repay_order_async(
        self,
        request: linkedmall_20180116_models.RepayOrderRequest,
    ) -> linkedmall_20180116_models.RepayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.repay_order_with_options_async(request, runtime)

    def reserve_movie_seat_with_options(
        self,
        request: linkedmall_20180116_models.ReserveMovieSeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ReserveMovieSeatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ReserveMovieSeatResponse(),
            self.do_rpcrequest('ReserveMovieSeat', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reserve_movie_seat_with_options_async(
        self,
        request: linkedmall_20180116_models.ReserveMovieSeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ReserveMovieSeatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ReserveMovieSeatResponse(),
            await self.do_rpcrequest_async('ReserveMovieSeat', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reserve_movie_seat(
        self,
        request: linkedmall_20180116_models.ReserveMovieSeatRequest,
    ) -> linkedmall_20180116_models.ReserveMovieSeatResponse:
        runtime = util_models.RuntimeOptions()
        return self.reserve_movie_seat_with_options(request, runtime)

    async def reserve_movie_seat_async(
        self,
        request: linkedmall_20180116_models.ReserveMovieSeatRequest,
    ) -> linkedmall_20180116_models.ReserveMovieSeatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reserve_movie_seat_with_options_async(request, runtime)

    def settle_order_with_options(
        self,
        request: linkedmall_20180116_models.SettleOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SettleOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SettleOrderResponse(),
            self.do_rpcrequest('SettleOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def settle_order_with_options_async(
        self,
        request: linkedmall_20180116_models.SettleOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SettleOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SettleOrderResponse(),
            await self.do_rpcrequest_async('SettleOrder', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def settle_order(
        self,
        request: linkedmall_20180116_models.SettleOrderRequest,
    ) -> linkedmall_20180116_models.SettleOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.settle_order_with_options(request, runtime)

    async def settle_order_async(
        self,
        request: linkedmall_20180116_models.SettleOrderRequest,
    ) -> linkedmall_20180116_models.SettleOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.settle_order_with_options_async(request, runtime)

    def submit_return_good_logistics_with_options(
        self,
        request: linkedmall_20180116_models.SubmitReturnGoodLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SubmitReturnGoodLogisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SubmitReturnGoodLogisticsResponse(),
            self.do_rpcrequest('SubmitReturnGoodLogistics', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_return_good_logistics_with_options_async(
        self,
        request: linkedmall_20180116_models.SubmitReturnGoodLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SubmitReturnGoodLogisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SubmitReturnGoodLogisticsResponse(),
            await self.do_rpcrequest_async('SubmitReturnGoodLogistics', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_return_good_logistics(
        self,
        request: linkedmall_20180116_models.SubmitReturnGoodLogisticsRequest,
    ) -> linkedmall_20180116_models.SubmitReturnGoodLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_return_good_logistics_with_options(request, runtime)

    async def submit_return_good_logistics_async(
        self,
        request: linkedmall_20180116_models.SubmitReturnGoodLogisticsRequest,
    ) -> linkedmall_20180116_models.SubmitReturnGoodLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_return_good_logistics_with_options_async(request, runtime)

    def sync_merchant_info_with_options(
        self,
        request: linkedmall_20180116_models.SyncMerchantInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SyncMerchantInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SyncMerchantInfoResponse(),
            self.do_rpcrequest('SyncMerchantInfo', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sync_merchant_info_with_options_async(
        self,
        request: linkedmall_20180116_models.SyncMerchantInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SyncMerchantInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SyncMerchantInfoResponse(),
            await self.do_rpcrequest_async('SyncMerchantInfo', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_merchant_info(
        self,
        request: linkedmall_20180116_models.SyncMerchantInfoRequest,
    ) -> linkedmall_20180116_models.SyncMerchantInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_merchant_info_with_options(request, runtime)

    async def sync_merchant_info_async(
        self,
        request: linkedmall_20180116_models.SyncMerchantInfoRequest,
    ) -> linkedmall_20180116_models.SyncMerchantInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_merchant_info_with_options_async(request, runtime)

    def unsign_withhold_agreement_with_options(
        self,
        request: linkedmall_20180116_models.UnsignWithholdAgreementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.UnsignWithholdAgreementResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.UnsignWithholdAgreementResponse(),
            self.do_rpcrequest('UnsignWithholdAgreement', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unsign_withhold_agreement_with_options_async(
        self,
        request: linkedmall_20180116_models.UnsignWithholdAgreementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.UnsignWithholdAgreementResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.UnsignWithholdAgreementResponse(),
            await self.do_rpcrequest_async('UnsignWithholdAgreement', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unsign_withhold_agreement(
        self,
        request: linkedmall_20180116_models.UnsignWithholdAgreementRequest,
    ) -> linkedmall_20180116_models.UnsignWithholdAgreementResponse:
        runtime = util_models.RuntimeOptions()
        return self.unsign_withhold_agreement_with_options(request, runtime)

    async def unsign_withhold_agreement_async(
        self,
        request: linkedmall_20180116_models.UnsignWithholdAgreementRequest,
    ) -> linkedmall_20180116_models.UnsignWithholdAgreementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unsign_withhold_agreement_with_options_async(request, runtime)

    def update_address_with_options(
        self,
        request: linkedmall_20180116_models.UpdateAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.UpdateAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.UpdateAddressResponse(),
            self.do_rpcrequest('UpdateAddress', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_address_with_options_async(
        self,
        request: linkedmall_20180116_models.UpdateAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.UpdateAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.UpdateAddressResponse(),
            await self.do_rpcrequest_async('UpdateAddress', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_address(
        self,
        request: linkedmall_20180116_models.UpdateAddressRequest,
    ) -> linkedmall_20180116_models.UpdateAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_address_with_options(request, runtime)

    async def update_address_async(
        self,
        request: linkedmall_20180116_models.UpdateAddressRequest,
    ) -> linkedmall_20180116_models.UpdateAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_address_with_options_async(request, runtime)

    def validate_taobao_account_with_options(
        self,
        request: linkedmall_20180116_models.ValidateTaobaoAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ValidateTaobaoAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ValidateTaobaoAccountResponse(),
            self.do_rpcrequest('ValidateTaobaoAccount', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def validate_taobao_account_with_options_async(
        self,
        request: linkedmall_20180116_models.ValidateTaobaoAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ValidateTaobaoAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ValidateTaobaoAccountResponse(),
            await self.do_rpcrequest_async('ValidateTaobaoAccount', '2018-01-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def validate_taobao_account(
        self,
        request: linkedmall_20180116_models.ValidateTaobaoAccountRequest,
    ) -> linkedmall_20180116_models.ValidateTaobaoAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_taobao_account_with_options(request, runtime)

    async def validate_taobao_account_async(
        self,
        request: linkedmall_20180116_models.ValidateTaobaoAccountRequest,
    ) -> linkedmall_20180116_models.ValidateTaobaoAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_taobao_account_with_options_async(request, runtime)
