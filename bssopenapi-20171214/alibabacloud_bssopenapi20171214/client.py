# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_bssopenapi20171214 import models as main_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-hangzhou': 'business.aliyuncs.com',
            'cn-shanghai': 'business.aliyuncs.com',
            'ap-southeast-1': 'business.ap-southeast-1.aliyuncs.com',
            'ap-northeast-1': 'business.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2': 'business.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2-pop': 'business.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'business.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'business.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'business.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'business.ap-southeast-1.aliyuncs.com',
            'cn-beijing': 'business.aliyuncs.com',
            'cn-beijing-finance-1': 'business.aliyuncs.com',
            'cn-beijing-finance-pop': 'business.aliyuncs.com',
            'cn-beijing-gov-1': 'business.aliyuncs.com',
            'cn-beijing-nu16-b01': 'business.aliyuncs.com',
            'cn-chengdu': 'business.aliyuncs.com',
            'cn-edge-1': 'business.aliyuncs.com',
            'cn-fujian': 'business.aliyuncs.com',
            'cn-haidian-cm12-c01': 'business.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'business.aliyuncs.com',
            'cn-hangzhou-finance': 'business.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'business.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'business.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'business.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'business.aliyuncs.com',
            'cn-hangzhou-test-306': 'business.aliyuncs.com',
            'cn-hongkong': 'business.aliyuncs.com',
            'cn-hongkong-finance-pop': 'business.aliyuncs.com',
            'cn-huhehaote': 'business.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'business.aliyuncs.com',
            'cn-north-2-gov-1': 'business.aliyuncs.com',
            'cn-qingdao': 'business.aliyuncs.com',
            'cn-qingdao-nebula': 'business.aliyuncs.com',
            'cn-shanghai-et15-b01': 'business.aliyuncs.com',
            'cn-shanghai-et2-b01': 'business.aliyuncs.com',
            'cn-shanghai-finance-1': 'business.aliyuncs.com',
            'cn-shanghai-inner': 'business.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'business.aliyuncs.com',
            'cn-shenzhen': 'business.aliyuncs.com',
            'cn-shenzhen-finance-1': 'business.aliyuncs.com',
            'cn-shenzhen-inner': 'business.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'business.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'business.aliyuncs.com',
            'cn-wuhan': 'business.aliyuncs.com',
            'cn-wulanchabu': 'business.aliyuncs.com',
            'cn-yushanfang': 'business.aliyuncs.com',
            'cn-zhangbei': 'business.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'business.aliyuncs.com',
            'cn-zhangjiakou': 'business.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'business.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'business.aliyuncs.com',
            'eu-central-1': 'business.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'business.ap-southeast-1.aliyuncs.com',
            'eu-west-1-oxs': 'business.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'business.ap-southeast-1.aliyuncs.com',
            'rus-west-1-pop': 'business.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'business.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'business.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('bssopenapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_account_relation_with_options(
        self,
        request: main_models.AddAccountRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAccountRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_nick):
            query['ChildNick'] = request.child_nick
        if not DaraCore.is_null(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not DaraCore.is_null(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not DaraCore.is_null(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not DaraCore.is_null(request.relation_type):
            query['RelationType'] = request.relation_type
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.role_codes):
            query['RoleCodes'] = request.role_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAccountRelation',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAccountRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_account_relation_with_options_async(
        self,
        request: main_models.AddAccountRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAccountRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_nick):
            query['ChildNick'] = request.child_nick
        if not DaraCore.is_null(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not DaraCore.is_null(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not DaraCore.is_null(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not DaraCore.is_null(request.relation_type):
            query['RelationType'] = request.relation_type
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.role_codes):
            query['RoleCodes'] = request.role_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAccountRelation',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAccountRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_account_relation(
        self,
        request: main_models.AddAccountRelationRequest,
    ) -> main_models.AddAccountRelationResponse:
        runtime = RuntimeOptions()
        return self.add_account_relation_with_options(request, runtime)

    async def add_account_relation_async(
        self,
        request: main_models.AddAccountRelationRequest,
    ) -> main_models.AddAccountRelationResponse:
        runtime = RuntimeOptions()
        return await self.add_account_relation_with_options_async(request, runtime)

    def allocate_cost_unit_resource_with_options(
        self,
        request: main_models.AllocateCostUnitResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateCostUnitResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_unit_id):
            query['FromUnitId'] = request.from_unit_id
        if not DaraCore.is_null(request.from_unit_user_id):
            query['FromUnitUserId'] = request.from_unit_user_id
        if not DaraCore.is_null(request.resource_instance_list):
            query['ResourceInstanceList'] = request.resource_instance_list
        if not DaraCore.is_null(request.to_unit_id):
            query['ToUnitId'] = request.to_unit_id
        if not DaraCore.is_null(request.to_unit_user_id):
            query['ToUnitUserId'] = request.to_unit_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateCostUnitResource',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateCostUnitResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_cost_unit_resource_with_options_async(
        self,
        request: main_models.AllocateCostUnitResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateCostUnitResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_unit_id):
            query['FromUnitId'] = request.from_unit_id
        if not DaraCore.is_null(request.from_unit_user_id):
            query['FromUnitUserId'] = request.from_unit_user_id
        if not DaraCore.is_null(request.resource_instance_list):
            query['ResourceInstanceList'] = request.resource_instance_list
        if not DaraCore.is_null(request.to_unit_id):
            query['ToUnitId'] = request.to_unit_id
        if not DaraCore.is_null(request.to_unit_user_id):
            query['ToUnitUserId'] = request.to_unit_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateCostUnitResource',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateCostUnitResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_cost_unit_resource(
        self,
        request: main_models.AllocateCostUnitResourceRequest,
    ) -> main_models.AllocateCostUnitResourceResponse:
        runtime = RuntimeOptions()
        return self.allocate_cost_unit_resource_with_options(request, runtime)

    async def allocate_cost_unit_resource_async(
        self,
        request: main_models.AllocateCostUnitResourceRequest,
    ) -> main_models.AllocateCostUnitResourceResponse:
        runtime = RuntimeOptions()
        return await self.allocate_cost_unit_resource_with_options_async(request, runtime)

    def apply_invoice_with_options(
        self,
        request: main_models.ApplyInvoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyInvoiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.apply_user_nick):
            query['ApplyUserNick'] = request.apply_user_nick
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.invoice_amount):
            query['InvoiceAmount'] = request.invoice_amount
        if not DaraCore.is_null(request.invoice_by_amount):
            query['InvoiceByAmount'] = request.invoice_by_amount
        if not DaraCore.is_null(request.invoicing_type):
            query['InvoicingType'] = request.invoicing_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.process_way):
            query['ProcessWay'] = request.process_way
        if not DaraCore.is_null(request.selected_ids):
            query['SelectedIds'] = request.selected_ids
        if not DaraCore.is_null(request.user_remark):
            query['UserRemark'] = request.user_remark
        if not DaraCore.is_null(request.emails):
            query['emails'] = request.emails
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyInvoice',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_invoice_with_options_async(
        self,
        request: main_models.ApplyInvoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyInvoiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address_id):
            query['AddressId'] = request.address_id
        if not DaraCore.is_null(request.apply_user_nick):
            query['ApplyUserNick'] = request.apply_user_nick
        if not DaraCore.is_null(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not DaraCore.is_null(request.invoice_amount):
            query['InvoiceAmount'] = request.invoice_amount
        if not DaraCore.is_null(request.invoice_by_amount):
            query['InvoiceByAmount'] = request.invoice_by_amount
        if not DaraCore.is_null(request.invoicing_type):
            query['InvoicingType'] = request.invoicing_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.process_way):
            query['ProcessWay'] = request.process_way
        if not DaraCore.is_null(request.selected_ids):
            query['SelectedIds'] = request.selected_ids
        if not DaraCore.is_null(request.user_remark):
            query['UserRemark'] = request.user_remark
        if not DaraCore.is_null(request.emails):
            query['emails'] = request.emails
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyInvoice',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_invoice(
        self,
        request: main_models.ApplyInvoiceRequest,
    ) -> main_models.ApplyInvoiceResponse:
        runtime = RuntimeOptions()
        return self.apply_invoice_with_options(request, runtime)

    async def apply_invoice_async(
        self,
        request: main_models.ApplyInvoiceRequest,
    ) -> main_models.ApplyInvoiceResponse:
        runtime = RuntimeOptions()
        return await self.apply_invoice_with_options_async(request, runtime)

    def cancel_order_with_options(
        self,
        request: main_models.CancelOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelOrder',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_order_with_options_async(
        self,
        request: main_models.CancelOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelOrder',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_order(
        self,
        request: main_models.CancelOrderRequest,
    ) -> main_models.CancelOrderResponse:
        runtime = RuntimeOptions()
        return self.cancel_order_with_options(request, runtime)

    async def cancel_order_async(
        self,
        request: main_models.CancelOrderRequest,
    ) -> main_models.CancelOrderResponse:
        runtime = RuntimeOptions()
        return await self.cancel_order_with_options_async(request, runtime)

    def change_reseller_consume_amount_with_options(
        self,
        request: main_models.ChangeResellerConsumeAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResellerConsumeAmountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.adjust_type):
            query['AdjustType'] = request.adjust_type
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.currency):
            query['Currency'] = request.currency
        if not DaraCore.is_null(request.extend_map):
            query['ExtendMap'] = request.extend_map
        if not DaraCore.is_null(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResellerConsumeAmount',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResellerConsumeAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_reseller_consume_amount_with_options_async(
        self,
        request: main_models.ChangeResellerConsumeAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResellerConsumeAmountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.adjust_type):
            query['AdjustType'] = request.adjust_type
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.currency):
            query['Currency'] = request.currency
        if not DaraCore.is_null(request.extend_map):
            query['ExtendMap'] = request.extend_map
        if not DaraCore.is_null(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResellerConsumeAmount',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResellerConsumeAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_reseller_consume_amount(
        self,
        request: main_models.ChangeResellerConsumeAmountRequest,
    ) -> main_models.ChangeResellerConsumeAmountResponse:
        runtime = RuntimeOptions()
        return self.change_reseller_consume_amount_with_options(request, runtime)

    async def change_reseller_consume_amount_async(
        self,
        request: main_models.ChangeResellerConsumeAmountRequest,
    ) -> main_models.ChangeResellerConsumeAmountResponse:
        runtime = RuntimeOptions()
        return await self.change_reseller_consume_amount_with_options_async(request, runtime)

    def confirm_relation_with_options(
        self,
        request: main_models.ConfirmRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not DaraCore.is_null(request.confirm_code):
            query['ConfirmCode'] = request.confirm_code
        if not DaraCore.is_null(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not DaraCore.is_null(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not DaraCore.is_null(request.relation_id):
            query['RelationId'] = request.relation_id
        if not DaraCore.is_null(request.relation_type):
            query['RelationType'] = request.relation_type
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmRelation',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_relation_with_options_async(
        self,
        request: main_models.ConfirmRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not DaraCore.is_null(request.confirm_code):
            query['ConfirmCode'] = request.confirm_code
        if not DaraCore.is_null(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not DaraCore.is_null(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not DaraCore.is_null(request.relation_id):
            query['RelationId'] = request.relation_id
        if not DaraCore.is_null(request.relation_type):
            query['RelationType'] = request.relation_type
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmRelation',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_relation(
        self,
        request: main_models.ConfirmRelationRequest,
    ) -> main_models.ConfirmRelationResponse:
        runtime = RuntimeOptions()
        return self.confirm_relation_with_options(request, runtime)

    async def confirm_relation_async(
        self,
        request: main_models.ConfirmRelationRequest,
    ) -> main_models.ConfirmRelationResponse:
        runtime = RuntimeOptions()
        return await self.confirm_relation_with_options_async(request, runtime)

    def convert_charge_type_with_options(
        self,
        request: main_models.ConvertChargeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConvertChargeType',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_charge_type_with_options_async(
        self,
        request: main_models.ConvertChargeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConvertChargeType',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_charge_type(
        self,
        request: main_models.ConvertChargeTypeRequest,
    ) -> main_models.ConvertChargeTypeResponse:
        runtime = RuntimeOptions()
        return self.convert_charge_type_with_options(request, runtime)

    async def convert_charge_type_async(
        self,
        request: main_models.ConvertChargeTypeRequest,
    ) -> main_models.ConvertChargeTypeResponse:
        runtime = RuntimeOptions()
        return await self.convert_charge_type_with_options_async(request, runtime)

    def create_ag_account_with_options(
        self,
        request: main_models.CreateAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_attr):
            query['AccountAttr'] = request.account_attr
        if not DaraCore.is_null(request.city_name):
            query['CityName'] = request.city_name
        if not DaraCore.is_null(request.enterprise_name):
            query['EnterpriseName'] = request.enterprise_name
        if not DaraCore.is_null(request.first_name):
            query['FirstName'] = request.first_name
        if not DaraCore.is_null(request.last_name):
            query['LastName'] = request.last_name
        if not DaraCore.is_null(request.login_email):
            query['LoginEmail'] = request.login_email
        if not DaraCore.is_null(request.nation_code):
            query['NationCode'] = request.nation_code
        if not DaraCore.is_null(request.postcode):
            query['Postcode'] = request.postcode
        if not DaraCore.is_null(request.province_name):
            query['ProvinceName'] = request.province_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgAccount',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ag_account_with_options_async(
        self,
        request: main_models.CreateAgAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAgAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_attr):
            query['AccountAttr'] = request.account_attr
        if not DaraCore.is_null(request.city_name):
            query['CityName'] = request.city_name
        if not DaraCore.is_null(request.enterprise_name):
            query['EnterpriseName'] = request.enterprise_name
        if not DaraCore.is_null(request.first_name):
            query['FirstName'] = request.first_name
        if not DaraCore.is_null(request.last_name):
            query['LastName'] = request.last_name
        if not DaraCore.is_null(request.login_email):
            query['LoginEmail'] = request.login_email
        if not DaraCore.is_null(request.nation_code):
            query['NationCode'] = request.nation_code
        if not DaraCore.is_null(request.postcode):
            query['Postcode'] = request.postcode
        if not DaraCore.is_null(request.province_name):
            query['ProvinceName'] = request.province_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAgAccount',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAgAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ag_account(
        self,
        request: main_models.CreateAgAccountRequest,
    ) -> main_models.CreateAgAccountResponse:
        runtime = RuntimeOptions()
        return self.create_ag_account_with_options(request, runtime)

    async def create_ag_account_async(
        self,
        request: main_models.CreateAgAccountRequest,
    ) -> main_models.CreateAgAccountResponse:
        runtime = RuntimeOptions()
        return await self.create_ag_account_with_options_async(request, runtime)

    def create_cost_unit_with_options(
        self,
        request: main_models.CreateCostUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCostUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.unit_entity_list):
            query['UnitEntityList'] = request.unit_entity_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCostUnit',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCostUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cost_unit_with_options_async(
        self,
        request: main_models.CreateCostUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCostUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.unit_entity_list):
            query['UnitEntityList'] = request.unit_entity_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCostUnit',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCostUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cost_unit(
        self,
        request: main_models.CreateCostUnitRequest,
    ) -> main_models.CreateCostUnitResponse:
        runtime = RuntimeOptions()
        return self.create_cost_unit_with_options(request, runtime)

    async def create_cost_unit_async(
        self,
        request: main_models.CreateCostUnitRequest,
    ) -> main_models.CreateCostUnitResponse:
        runtime = RuntimeOptions()
        return await self.create_cost_unit_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.logistics):
            query['Logistics'] = request.logistics
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parameter):
            query['Parameter'] = request.parameter
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        if not DaraCore.is_null(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.logistics):
            query['Logistics'] = request.logistics
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parameter):
            query['Parameter'] = request.parameter
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        if not DaraCore.is_null(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_reseller_user_quota_with_options(
        self,
        request: main_models.CreateResellerUserQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResellerUserQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.currency):
            query['Currency'] = request.currency
        if not DaraCore.is_null(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResellerUserQuota',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResellerUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_reseller_user_quota_with_options_async(
        self,
        request: main_models.CreateResellerUserQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResellerUserQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.currency):
            query['Currency'] = request.currency
        if not DaraCore.is_null(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResellerUserQuota',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResellerUserQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_reseller_user_quota(
        self,
        request: main_models.CreateResellerUserQuotaRequest,
    ) -> main_models.CreateResellerUserQuotaResponse:
        runtime = RuntimeOptions()
        return self.create_reseller_user_quota_with_options(request, runtime)

    async def create_reseller_user_quota_async(
        self,
        request: main_models.CreateResellerUserQuotaRequest,
    ) -> main_models.CreateResellerUserQuotaResponse:
        runtime = RuntimeOptions()
        return await self.create_reseller_user_quota_with_options_async(request, runtime)

    def create_resource_package_with_options(
        self,
        request: main_models.CreateResourcePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourcePackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourcePackage',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_package_with_options_async(
        self,
        request: main_models.CreateResourcePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourcePackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourcePackage',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourcePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_package(
        self,
        request: main_models.CreateResourcePackageRequest,
    ) -> main_models.CreateResourcePackageResponse:
        runtime = RuntimeOptions()
        return self.create_resource_package_with_options(request, runtime)

    async def create_resource_package_async(
        self,
        request: main_models.CreateResourcePackageRequest,
    ) -> main_models.CreateResourcePackageResponse:
        runtime = RuntimeOptions()
        return await self.create_resource_package_with_options_async(request, runtime)

    def create_savings_plans_instance_with_options(
        self,
        tmp_req: main_models.CreateSavingsPlansInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSavingsPlansInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateSavingsPlansInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extend_map):
            request.extend_map_shrink = Utils.array_to_string_with_specified_style(tmp_req.extend_map, 'ExtendMap', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not DaraCore.is_null(request.extend_map_shrink):
            query['ExtendMap'] = request.extend_map_shrink
        if not DaraCore.is_null(request.pay_mode):
            query['PayMode'] = request.pay_mode
        if not DaraCore.is_null(request.pool_value):
            query['PoolValue'] = request.pool_value
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSavingsPlansInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSavingsPlansInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_savings_plans_instance_with_options_async(
        self,
        tmp_req: main_models.CreateSavingsPlansInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSavingsPlansInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateSavingsPlansInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extend_map):
            request.extend_map_shrink = Utils.array_to_string_with_specified_style(tmp_req.extend_map, 'ExtendMap', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not DaraCore.is_null(request.extend_map_shrink):
            query['ExtendMap'] = request.extend_map_shrink
        if not DaraCore.is_null(request.pay_mode):
            query['PayMode'] = request.pay_mode
        if not DaraCore.is_null(request.pool_value):
            query['PoolValue'] = request.pool_value
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.spec_type):
            query['SpecType'] = request.spec_type
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSavingsPlansInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSavingsPlansInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_savings_plans_instance(
        self,
        request: main_models.CreateSavingsPlansInstanceRequest,
    ) -> main_models.CreateSavingsPlansInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_savings_plans_instance_with_options(request, runtime)

    async def create_savings_plans_instance_async(
        self,
        request: main_models.CreateSavingsPlansInstanceRequest,
    ) -> main_models.CreateSavingsPlansInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_savings_plans_instance_with_options_async(request, runtime)

    def delete_cost_unit_with_options(
        self,
        request: main_models.DeleteCostUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCostUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not DaraCore.is_null(request.unit_id):
            query['UnitId'] = request.unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCostUnit',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCostUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cost_unit_with_options_async(
        self,
        request: main_models.DeleteCostUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCostUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not DaraCore.is_null(request.unit_id):
            query['UnitId'] = request.unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCostUnit',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCostUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cost_unit(
        self,
        request: main_models.DeleteCostUnitRequest,
    ) -> main_models.DeleteCostUnitResponse:
        runtime = RuntimeOptions()
        return self.delete_cost_unit_with_options(request, runtime)

    async def delete_cost_unit_async(
        self,
        request: main_models.DeleteCostUnitRequest,
    ) -> main_models.DeleteCostUnitResponse:
        runtime = RuntimeOptions()
        return await self.delete_cost_unit_with_options_async(request, runtime)

    def describe_cost_budgets_summary_with_options(
        self,
        request: main_models.DescribeCostBudgetsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCostBudgetsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.budget_name):
            query['BudgetName'] = request.budget_name
        if not DaraCore.is_null(request.budget_status):
            query['BudgetStatus'] = request.budget_status
        if not DaraCore.is_null(request.budget_type):
            query['BudgetType'] = request.budget_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCostBudgetsSummary',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCostBudgetsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cost_budgets_summary_with_options_async(
        self,
        request: main_models.DescribeCostBudgetsSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCostBudgetsSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.budget_name):
            query['BudgetName'] = request.budget_name
        if not DaraCore.is_null(request.budget_status):
            query['BudgetStatus'] = request.budget_status
        if not DaraCore.is_null(request.budget_type):
            query['BudgetType'] = request.budget_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCostBudgetsSummary',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCostBudgetsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cost_budgets_summary(
        self,
        request: main_models.DescribeCostBudgetsSummaryRequest,
    ) -> main_models.DescribeCostBudgetsSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_cost_budgets_summary_with_options(request, runtime)

    async def describe_cost_budgets_summary_async(
        self,
        request: main_models.DescribeCostBudgetsSummaryRequest,
    ) -> main_models.DescribeCostBudgetsSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_cost_budgets_summary_with_options_async(request, runtime)

    def describe_instance_amortized_cost_by_amortization_period_with_options(
        self,
        request: main_models.DescribeInstanceAmortizedCostByAmortizationPeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not DaraCore.is_null(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not DaraCore.is_null(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.consume_period_filter):
            body['ConsumePeriodFilter'] = request.consume_period_filter
        if not DaraCore.is_null(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not DaraCore.is_null(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not DaraCore.is_null(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceAmortizedCostByAmortizationPeriod',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_amortized_cost_by_amortization_period_with_options_async(
        self,
        request: main_models.DescribeInstanceAmortizedCostByAmortizationPeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not DaraCore.is_null(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not DaraCore.is_null(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.consume_period_filter):
            body['ConsumePeriodFilter'] = request.consume_period_filter
        if not DaraCore.is_null(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not DaraCore.is_null(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not DaraCore.is_null(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceAmortizedCostByAmortizationPeriod',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_amortized_cost_by_amortization_period(
        self,
        request: main_models.DescribeInstanceAmortizedCostByAmortizationPeriodRequest,
    ) -> main_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_amortized_cost_by_amortization_period_with_options(request, runtime)

    async def describe_instance_amortized_cost_by_amortization_period_async(
        self,
        request: main_models.DescribeInstanceAmortizedCostByAmortizationPeriodRequest,
    ) -> main_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_amortized_cost_by_amortization_period_with_options_async(request, runtime)

    def describe_instance_amortized_cost_by_amortization_period_date_with_options(
        self,
        request: main_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amortization_date_end):
            body['AmortizationDateEnd'] = request.amortization_date_end
        if not DaraCore.is_null(request.amortization_date_start):
            body['AmortizationDateStart'] = request.amortization_date_start
        if not DaraCore.is_null(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not DaraCore.is_null(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not DaraCore.is_null(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not DaraCore.is_null(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not DaraCore.is_null(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceAmortizedCostByAmortizationPeriodDate',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_amortized_cost_by_amortization_period_date_with_options_async(
        self,
        request: main_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amortization_date_end):
            body['AmortizationDateEnd'] = request.amortization_date_end
        if not DaraCore.is_null(request.amortization_date_start):
            body['AmortizationDateStart'] = request.amortization_date_start
        if not DaraCore.is_null(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not DaraCore.is_null(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not DaraCore.is_null(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not DaraCore.is_null(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not DaraCore.is_null(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceAmortizedCostByAmortizationPeriodDate',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_amortized_cost_by_amortization_period_date(
        self,
        request: main_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateRequest,
    ) -> main_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_amortized_cost_by_amortization_period_date_with_options(request, runtime)

    async def describe_instance_amortized_cost_by_amortization_period_date_async(
        self,
        request: main_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateRequest,
    ) -> main_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_amortized_cost_by_amortization_period_date_with_options_async(request, runtime)

    def describe_instance_amortized_cost_by_consume_period_with_options(
        self,
        request: main_models.DescribeInstanceAmortizedCostByConsumePeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAmortizedCostByConsumePeriodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amortization_period_filter):
            body['AmortizationPeriodFilter'] = request.amortization_period_filter
        if not DaraCore.is_null(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not DaraCore.is_null(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not DaraCore.is_null(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not DaraCore.is_null(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not DaraCore.is_null(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceAmortizedCostByConsumePeriod',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAmortizedCostByConsumePeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_amortized_cost_by_consume_period_with_options_async(
        self,
        request: main_models.DescribeInstanceAmortizedCostByConsumePeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAmortizedCostByConsumePeriodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amortization_period_filter):
            body['AmortizationPeriodFilter'] = request.amortization_period_filter
        if not DaraCore.is_null(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not DaraCore.is_null(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not DaraCore.is_null(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not DaraCore.is_null(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not DaraCore.is_null(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceAmortizedCostByConsumePeriod',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAmortizedCostByConsumePeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_amortized_cost_by_consume_period(
        self,
        request: main_models.DescribeInstanceAmortizedCostByConsumePeriodRequest,
    ) -> main_models.DescribeInstanceAmortizedCostByConsumePeriodResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_amortized_cost_by_consume_period_with_options(request, runtime)

    async def describe_instance_amortized_cost_by_consume_period_async(
        self,
        request: main_models.DescribeInstanceAmortizedCostByConsumePeriodRequest,
    ) -> main_models.DescribeInstanceAmortizedCostByConsumePeriodResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_amortized_cost_by_consume_period_with_options_async(request, runtime)

    def describe_instance_bill_with_options(
        self,
        request: main_models.DescribeInstanceBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.instance_id):
            query['InstanceID'] = request.instance_id
        if not DaraCore.is_null(request.is_billing_item):
            query['IsBillingItem'] = request.is_billing_item
        if not DaraCore.is_null(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pip_code):
            query['PipCode'] = request.pip_code
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_bill_with_options_async(
        self,
        request: main_models.DescribeInstanceBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.instance_id):
            query['InstanceID'] = request.instance_id
        if not DaraCore.is_null(request.is_billing_item):
            query['IsBillingItem'] = request.is_billing_item
        if not DaraCore.is_null(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pip_code):
            query['PipCode'] = request.pip_code
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_bill(
        self,
        request: main_models.DescribeInstanceBillRequest,
    ) -> main_models.DescribeInstanceBillResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_bill_with_options(request, runtime)

    async def describe_instance_bill_async(
        self,
        request: main_models.DescribeInstanceBillRequest,
    ) -> main_models.DescribeInstanceBillResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_bill_with_options_async(request, runtime)

    def describe_instance_deduct_amortized_cost_by_amortization_period_with_options(
        self,
        request: main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not DaraCore.is_null(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not DaraCore.is_null(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not DaraCore.is_null(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not DaraCore.is_null(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDeductAmortizedCostByAmortizationPeriod',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_deduct_amortized_cost_by_amortization_period_with_options_async(
        self,
        request: main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not DaraCore.is_null(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not DaraCore.is_null(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not DaraCore.is_null(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not DaraCore.is_null(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceDeductAmortizedCostByAmortizationPeriod',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_deduct_amortized_cost_by_amortization_period(
        self,
        request: main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodRequest,
    ) -> main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_deduct_amortized_cost_by_amortization_period_with_options(request, runtime)

    async def describe_instance_deduct_amortized_cost_by_amortization_period_async(
        self,
        request: main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodRequest,
    ) -> main_models.DescribeInstanceDeductAmortizedCostByAmortizationPeriodResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_deduct_amortized_cost_by_amortization_period_with_options_async(request, runtime)

    def describe_pricing_module_with_options(
        self,
        request: main_models.DescribePricingModuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePricingModuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePricingModule',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePricingModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pricing_module_with_options_async(
        self,
        request: main_models.DescribePricingModuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePricingModuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePricingModule',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePricingModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pricing_module(
        self,
        request: main_models.DescribePricingModuleRequest,
    ) -> main_models.DescribePricingModuleResponse:
        runtime = RuntimeOptions()
        return self.describe_pricing_module_with_options(request, runtime)

    async def describe_pricing_module_async(
        self,
        request: main_models.DescribePricingModuleRequest,
    ) -> main_models.DescribePricingModuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_pricing_module_with_options_async(request, runtime)

    def describe_product_amortized_cost_by_amortization_period_with_options(
        self,
        request: main_models.DescribeProductAmortizedCostByAmortizationPeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductAmortizedCostByAmortizationPeriodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not DaraCore.is_null(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not DaraCore.is_null(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.consume_period_filter):
            body['ConsumePeriodFilter'] = request.consume_period_filter
        if not DaraCore.is_null(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not DaraCore.is_null(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProductAmortizedCostByAmortizationPeriod',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductAmortizedCostByAmortizationPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_product_amortized_cost_by_amortization_period_with_options_async(
        self,
        request: main_models.DescribeProductAmortizedCostByAmortizationPeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductAmortizedCostByAmortizationPeriodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not DaraCore.is_null(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not DaraCore.is_null(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.consume_period_filter):
            body['ConsumePeriodFilter'] = request.consume_period_filter
        if not DaraCore.is_null(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not DaraCore.is_null(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProductAmortizedCostByAmortizationPeriod',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductAmortizedCostByAmortizationPeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_product_amortized_cost_by_amortization_period(
        self,
        request: main_models.DescribeProductAmortizedCostByAmortizationPeriodRequest,
    ) -> main_models.DescribeProductAmortizedCostByAmortizationPeriodResponse:
        runtime = RuntimeOptions()
        return self.describe_product_amortized_cost_by_amortization_period_with_options(request, runtime)

    async def describe_product_amortized_cost_by_amortization_period_async(
        self,
        request: main_models.DescribeProductAmortizedCostByAmortizationPeriodRequest,
    ) -> main_models.DescribeProductAmortizedCostByAmortizationPeriodResponse:
        runtime = RuntimeOptions()
        return await self.describe_product_amortized_cost_by_amortization_period_with_options_async(request, runtime)

    def describe_product_amortized_cost_by_consume_period_with_options(
        self,
        request: main_models.DescribeProductAmortizedCostByConsumePeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductAmortizedCostByConsumePeriodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amortization_period_filter):
            body['AmortizationPeriodFilter'] = request.amortization_period_filter
        if not DaraCore.is_null(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not DaraCore.is_null(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not DaraCore.is_null(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not DaraCore.is_null(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProductAmortizedCostByConsumePeriod',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductAmortizedCostByConsumePeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_product_amortized_cost_by_consume_period_with_options_async(
        self,
        request: main_models.DescribeProductAmortizedCostByConsumePeriodRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductAmortizedCostByConsumePeriodResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amortization_period_filter):
            body['AmortizationPeriodFilter'] = request.amortization_period_filter
        if not DaraCore.is_null(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not DaraCore.is_null(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not DaraCore.is_null(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.product_code):
            body['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not DaraCore.is_null(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProductAmortizedCostByConsumePeriod',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductAmortizedCostByConsumePeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_product_amortized_cost_by_consume_period(
        self,
        request: main_models.DescribeProductAmortizedCostByConsumePeriodRequest,
    ) -> main_models.DescribeProductAmortizedCostByConsumePeriodResponse:
        runtime = RuntimeOptions()
        return self.describe_product_amortized_cost_by_consume_period_with_options(request, runtime)

    async def describe_product_amortized_cost_by_consume_period_async(
        self,
        request: main_models.DescribeProductAmortizedCostByConsumePeriodRequest,
    ) -> main_models.DescribeProductAmortizedCostByConsumePeriodResponse:
        runtime = RuntimeOptions()
        return await self.describe_product_amortized_cost_by_consume_period_with_options_async(request, runtime)

    def describe_resource_coverage_detail_with_options(
        self,
        request: main_models.DescribeResourceCoverageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceCoverageDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceCoverageDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceCoverageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_coverage_detail_with_options_async(
        self,
        request: main_models.DescribeResourceCoverageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceCoverageDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceCoverageDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceCoverageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_coverage_detail(
        self,
        request: main_models.DescribeResourceCoverageDetailRequest,
    ) -> main_models.DescribeResourceCoverageDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_coverage_detail_with_options(request, runtime)

    async def describe_resource_coverage_detail_async(
        self,
        request: main_models.DescribeResourceCoverageDetailRequest,
    ) -> main_models.DescribeResourceCoverageDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_coverage_detail_with_options_async(request, runtime)

    def describe_resource_coverage_total_with_options(
        self,
        request: main_models.DescribeResourceCoverageTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceCoverageTotalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceCoverageTotal',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceCoverageTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_coverage_total_with_options_async(
        self,
        request: main_models.DescribeResourceCoverageTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceCoverageTotalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceCoverageTotal',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceCoverageTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_coverage_total(
        self,
        request: main_models.DescribeResourceCoverageTotalRequest,
    ) -> main_models.DescribeResourceCoverageTotalResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_coverage_total_with_options(request, runtime)

    async def describe_resource_coverage_total_async(
        self,
        request: main_models.DescribeResourceCoverageTotalRequest,
    ) -> main_models.DescribeResourceCoverageTotalResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_coverage_total_with_options_async(request, runtime)

    def describe_resource_package_product_with_options(
        self,
        request: main_models.DescribeResourcePackageProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourcePackageProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourcePackageProduct',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourcePackageProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_package_product_with_options_async(
        self,
        request: main_models.DescribeResourcePackageProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourcePackageProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourcePackageProduct',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourcePackageProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_package_product(
        self,
        request: main_models.DescribeResourcePackageProductRequest,
    ) -> main_models.DescribeResourcePackageProductResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_package_product_with_options(request, runtime)

    async def describe_resource_package_product_async(
        self,
        request: main_models.DescribeResourcePackageProductRequest,
    ) -> main_models.DescribeResourcePackageProductResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_package_product_with_options_async(request, runtime)

    def describe_resource_usage_detail_with_options(
        self,
        request: main_models.DescribeResourceUsageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceUsageDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceUsageDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceUsageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_usage_detail_with_options_async(
        self,
        request: main_models.DescribeResourceUsageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceUsageDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceUsageDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceUsageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_usage_detail(
        self,
        request: main_models.DescribeResourceUsageDetailRequest,
    ) -> main_models.DescribeResourceUsageDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_usage_detail_with_options(request, runtime)

    async def describe_resource_usage_detail_async(
        self,
        request: main_models.DescribeResourceUsageDetailRequest,
    ) -> main_models.DescribeResourceUsageDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_usage_detail_with_options_async(request, runtime)

    def describe_resource_usage_total_with_options(
        self,
        request: main_models.DescribeResourceUsageTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceUsageTotalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceUsageTotal',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceUsageTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_usage_total_with_options_async(
        self,
        request: main_models.DescribeResourceUsageTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeResourceUsageTotalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeResourceUsageTotal',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeResourceUsageTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_usage_total(
        self,
        request: main_models.DescribeResourceUsageTotalRequest,
    ) -> main_models.DescribeResourceUsageTotalResponse:
        runtime = RuntimeOptions()
        return self.describe_resource_usage_total_with_options(request, runtime)

    async def describe_resource_usage_total_async(
        self,
        request: main_models.DescribeResourceUsageTotalRequest,
    ) -> main_models.DescribeResourceUsageTotalResponse:
        runtime = RuntimeOptions()
        return await self.describe_resource_usage_total_with_options_async(request, runtime)

    def describe_savings_plans_coverage_detail_with_options(
        self,
        tmp_req: main_models.DescribeSavingsPlansCoverageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSavingsPlansCoverageDetailResponse:
        tmp_req.validate()
        request = main_models.DescribeSavingsPlansCoverageDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_param):
            request.filter_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_param, 'FilterParam', 'json')
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.filter_param_shrink):
            query['FilterParam'] = request.filter_param_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSavingsPlansCoverageDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSavingsPlansCoverageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_savings_plans_coverage_detail_with_options_async(
        self,
        tmp_req: main_models.DescribeSavingsPlansCoverageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSavingsPlansCoverageDetailResponse:
        tmp_req.validate()
        request = main_models.DescribeSavingsPlansCoverageDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_param):
            request.filter_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_param, 'FilterParam', 'json')
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.filter_param_shrink):
            query['FilterParam'] = request.filter_param_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSavingsPlansCoverageDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSavingsPlansCoverageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_savings_plans_coverage_detail(
        self,
        request: main_models.DescribeSavingsPlansCoverageDetailRequest,
    ) -> main_models.DescribeSavingsPlansCoverageDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_savings_plans_coverage_detail_with_options(request, runtime)

    async def describe_savings_plans_coverage_detail_async(
        self,
        request: main_models.DescribeSavingsPlansCoverageDetailRequest,
    ) -> main_models.DescribeSavingsPlansCoverageDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_savings_plans_coverage_detail_with_options_async(request, runtime)

    def describe_savings_plans_coverage_total_with_options(
        self,
        tmp_req: main_models.DescribeSavingsPlansCoverageTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSavingsPlansCoverageTotalResponse:
        tmp_req.validate()
        request = main_models.DescribeSavingsPlansCoverageTotalShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_param):
            request.filter_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_param, 'FilterParam', 'json')
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.filter_param_shrink):
            query['FilterParam'] = request.filter_param_shrink
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSavingsPlansCoverageTotal',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSavingsPlansCoverageTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_savings_plans_coverage_total_with_options_async(
        self,
        tmp_req: main_models.DescribeSavingsPlansCoverageTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSavingsPlansCoverageTotalResponse:
        tmp_req.validate()
        request = main_models.DescribeSavingsPlansCoverageTotalShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_param):
            request.filter_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_param, 'FilterParam', 'json')
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.filter_param_shrink):
            query['FilterParam'] = request.filter_param_shrink
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSavingsPlansCoverageTotal',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSavingsPlansCoverageTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_savings_plans_coverage_total(
        self,
        request: main_models.DescribeSavingsPlansCoverageTotalRequest,
    ) -> main_models.DescribeSavingsPlansCoverageTotalResponse:
        runtime = RuntimeOptions()
        return self.describe_savings_plans_coverage_total_with_options(request, runtime)

    async def describe_savings_plans_coverage_total_async(
        self,
        request: main_models.DescribeSavingsPlansCoverageTotalRequest,
    ) -> main_models.DescribeSavingsPlansCoverageTotalResponse:
        runtime = RuntimeOptions()
        return await self.describe_savings_plans_coverage_total_with_options_async(request, runtime)

    def describe_savings_plans_usage_detail_with_options(
        self,
        tmp_req: main_models.DescribeSavingsPlansUsageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSavingsPlansUsageDetailResponse:
        tmp_req.validate()
        request = main_models.DescribeSavingsPlansUsageDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_param):
            request.filter_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_param, 'FilterParam', 'json')
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.filter_param_shrink):
            query['FilterParam'] = request.filter_param_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSavingsPlansUsageDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSavingsPlansUsageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_savings_plans_usage_detail_with_options_async(
        self,
        tmp_req: main_models.DescribeSavingsPlansUsageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSavingsPlansUsageDetailResponse:
        tmp_req.validate()
        request = main_models.DescribeSavingsPlansUsageDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_param):
            request.filter_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_param, 'FilterParam', 'json')
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.filter_param_shrink):
            query['FilterParam'] = request.filter_param_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSavingsPlansUsageDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSavingsPlansUsageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_savings_plans_usage_detail(
        self,
        request: main_models.DescribeSavingsPlansUsageDetailRequest,
    ) -> main_models.DescribeSavingsPlansUsageDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_savings_plans_usage_detail_with_options(request, runtime)

    async def describe_savings_plans_usage_detail_async(
        self,
        request: main_models.DescribeSavingsPlansUsageDetailRequest,
    ) -> main_models.DescribeSavingsPlansUsageDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_savings_plans_usage_detail_with_options_async(request, runtime)

    def describe_savings_plans_usage_total_with_options(
        self,
        tmp_req: main_models.DescribeSavingsPlansUsageTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSavingsPlansUsageTotalResponse:
        tmp_req.validate()
        request = main_models.DescribeSavingsPlansUsageTotalShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_param):
            request.filter_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_param, 'FilterParam', 'json')
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.filter_param_shrink):
            query['FilterParam'] = request.filter_param_shrink
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSavingsPlansUsageTotal',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSavingsPlansUsageTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_savings_plans_usage_total_with_options_async(
        self,
        tmp_req: main_models.DescribeSavingsPlansUsageTotalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSavingsPlansUsageTotalResponse:
        tmp_req.validate()
        request = main_models.DescribeSavingsPlansUsageTotalShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_param):
            request.filter_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_param, 'FilterParam', 'json')
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.end_period):
            query['EndPeriod'] = request.end_period
        if not DaraCore.is_null(request.filter_param_shrink):
            query['FilterParam'] = request.filter_param_shrink
        if not DaraCore.is_null(request.period_type):
            query['PeriodType'] = request.period_type
        if not DaraCore.is_null(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSavingsPlansUsageTotal',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSavingsPlansUsageTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_savings_plans_usage_total(
        self,
        request: main_models.DescribeSavingsPlansUsageTotalRequest,
    ) -> main_models.DescribeSavingsPlansUsageTotalResponse:
        runtime = RuntimeOptions()
        return self.describe_savings_plans_usage_total_with_options(request, runtime)

    async def describe_savings_plans_usage_total_async(
        self,
        request: main_models.DescribeSavingsPlansUsageTotalRequest,
    ) -> main_models.DescribeSavingsPlansUsageTotalResponse:
        runtime = RuntimeOptions()
        return await self.describe_savings_plans_usage_total_with_options_async(request, runtime)

    def describe_split_item_bill_with_options(
        self,
        request: main_models.DescribeSplitItemBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSplitItemBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.instance_id):
            query['InstanceID'] = request.instance_id
        if not DaraCore.is_null(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pip_code):
            query['PipCode'] = request.pip_code
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.split_item_id):
            query['SplitItemID'] = request.split_item_id
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not DaraCore.is_null(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSplitItemBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSplitItemBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_split_item_bill_with_options_async(
        self,
        request: main_models.DescribeSplitItemBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSplitItemBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.instance_id):
            query['InstanceID'] = request.instance_id
        if not DaraCore.is_null(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pip_code):
            query['PipCode'] = request.pip_code
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.split_item_id):
            query['SplitItemID'] = request.split_item_id
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not DaraCore.is_null(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSplitItemBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSplitItemBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_split_item_bill(
        self,
        request: main_models.DescribeSplitItemBillRequest,
    ) -> main_models.DescribeSplitItemBillResponse:
        runtime = RuntimeOptions()
        return self.describe_split_item_bill_with_options(request, runtime)

    async def describe_split_item_bill_async(
        self,
        request: main_models.DescribeSplitItemBillRequest,
    ) -> main_models.DescribeSplitItemBillResponse:
        runtime = RuntimeOptions()
        return await self.describe_split_item_bill_with_options_async(request, runtime)

    def get_account_relation_with_options(
        self,
        request: main_models.GetAccountRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountRelationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountRelation',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_relation_with_options_async(
        self,
        request: main_models.GetAccountRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountRelationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountRelation',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_relation(
        self,
        request: main_models.GetAccountRelationRequest,
    ) -> main_models.GetAccountRelationResponse:
        runtime = RuntimeOptions()
        return self.get_account_relation_with_options(request, runtime)

    async def get_account_relation_async(
        self,
        request: main_models.GetAccountRelationRequest,
    ) -> main_models.GetAccountRelationResponse:
        runtime = RuntimeOptions()
        return await self.get_account_relation_with_options_async(request, runtime)

    def get_customer_account_info_with_options(
        self,
        request: main_models.GetCustomerAccountInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerAccountInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerAccountInfo',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customer_account_info_with_options_async(
        self,
        request: main_models.GetCustomerAccountInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerAccountInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerAccountInfo',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customer_account_info(
        self,
        request: main_models.GetCustomerAccountInfoRequest,
    ) -> main_models.GetCustomerAccountInfoResponse:
        runtime = RuntimeOptions()
        return self.get_customer_account_info_with_options(request, runtime)

    async def get_customer_account_info_async(
        self,
        request: main_models.GetCustomerAccountInfoRequest,
    ) -> main_models.GetCustomerAccountInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_customer_account_info_with_options_async(request, runtime)

    def get_customer_list_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetCustomerList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customer_list_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetCustomerList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customer_list(self) -> main_models.GetCustomerListResponse:
        runtime = RuntimeOptions()
        return self.get_customer_list_with_options(runtime)

    async def get_customer_list_async(self) -> main_models.GetCustomerListResponse:
        runtime = RuntimeOptions()
        return await self.get_customer_list_with_options_async(runtime)

    def get_order_detail_with_options(
        self,
        request: main_models.GetOrderDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOrderDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOrderDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_order_detail_with_options_async(
        self,
        request: main_models.GetOrderDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOrderDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOrderDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrderDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_order_detail(
        self,
        request: main_models.GetOrderDetailRequest,
    ) -> main_models.GetOrderDetailResponse:
        runtime = RuntimeOptions()
        return self.get_order_detail_with_options(request, runtime)

    async def get_order_detail_async(
        self,
        request: main_models.GetOrderDetailRequest,
    ) -> main_models.GetOrderDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_order_detail_with_options_async(request, runtime)

    def get_pay_as_you_go_price_with_options(
        self,
        request: main_models.GetPayAsYouGoPriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPayAsYouGoPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.module_list):
            query['ModuleList'] = request.module_list
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPayAsYouGoPrice',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPayAsYouGoPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pay_as_you_go_price_with_options_async(
        self,
        request: main_models.GetPayAsYouGoPriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPayAsYouGoPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.module_list):
            query['ModuleList'] = request.module_list
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPayAsYouGoPrice',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPayAsYouGoPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pay_as_you_go_price(
        self,
        request: main_models.GetPayAsYouGoPriceRequest,
    ) -> main_models.GetPayAsYouGoPriceResponse:
        runtime = RuntimeOptions()
        return self.get_pay_as_you_go_price_with_options(request, runtime)

    async def get_pay_as_you_go_price_async(
        self,
        request: main_models.GetPayAsYouGoPriceRequest,
    ) -> main_models.GetPayAsYouGoPriceResponse:
        runtime = RuntimeOptions()
        return await self.get_pay_as_you_go_price_with_options_async(request, runtime)

    def get_resource_package_price_with_options(
        self,
        request: main_models.GetResourcePackagePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourcePackagePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourcePackagePrice',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourcePackagePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_package_price_with_options_async(
        self,
        request: main_models.GetResourcePackagePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourcePackagePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.package_type):
            query['PackageType'] = request.package_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourcePackagePrice',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourcePackagePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_package_price(
        self,
        request: main_models.GetResourcePackagePriceRequest,
    ) -> main_models.GetResourcePackagePriceResponse:
        runtime = RuntimeOptions()
        return self.get_resource_package_price_with_options(request, runtime)

    async def get_resource_package_price_async(
        self,
        request: main_models.GetResourcePackagePriceRequest,
    ) -> main_models.GetResourcePackagePriceResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_package_price_with_options_async(request, runtime)

    def get_subscription_price_with_options(
        self,
        request: main_models.GetSubscriptionPriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubscriptionPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_list):
            query['ModuleList'] = request.module_list
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.quantity):
            query['Quantity'] = request.quantity
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.service_period_quantity):
            query['ServicePeriodQuantity'] = request.service_period_quantity
        if not DaraCore.is_null(request.service_period_unit):
            query['ServicePeriodUnit'] = request.service_period_unit
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubscriptionPrice',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubscriptionPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subscription_price_with_options_async(
        self,
        request: main_models.GetSubscriptionPriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubscriptionPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_list):
            query['ModuleList'] = request.module_list
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.quantity):
            query['Quantity'] = request.quantity
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.service_period_quantity):
            query['ServicePeriodQuantity'] = request.service_period_quantity
        if not DaraCore.is_null(request.service_period_unit):
            query['ServicePeriodUnit'] = request.service_period_unit
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubscriptionPrice',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubscriptionPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subscription_price(
        self,
        request: main_models.GetSubscriptionPriceRequest,
    ) -> main_models.GetSubscriptionPriceResponse:
        runtime = RuntimeOptions()
        return self.get_subscription_price_with_options(request, runtime)

    async def get_subscription_price_async(
        self,
        request: main_models.GetSubscriptionPriceRequest,
    ) -> main_models.GetSubscriptionPriceResponse:
        runtime = RuntimeOptions()
        return await self.get_subscription_price_with_options_async(request, runtime)

    def inquiry_price_refund_instance_with_options(
        self,
        request: main_models.InquiryPriceRefundInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InquiryPriceRefundInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InquiryPriceRefundInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InquiryPriceRefundInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def inquiry_price_refund_instance_with_options_async(
        self,
        request: main_models.InquiryPriceRefundInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InquiryPriceRefundInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InquiryPriceRefundInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InquiryPriceRefundInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def inquiry_price_refund_instance(
        self,
        request: main_models.InquiryPriceRefundInstanceRequest,
    ) -> main_models.InquiryPriceRefundInstanceResponse:
        runtime = RuntimeOptions()
        return self.inquiry_price_refund_instance_with_options(request, runtime)

    async def inquiry_price_refund_instance_async(
        self,
        request: main_models.InquiryPriceRefundInstanceRequest,
    ) -> main_models.InquiryPriceRefundInstanceResponse:
        runtime = RuntimeOptions()
        return await self.inquiry_price_refund_instance_with_options_async(request, runtime)

    def modify_account_relation_with_options(
        self,
        request: main_models.ModifyAccountRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_nick):
            query['ChildNick'] = request.child_nick
        if not DaraCore.is_null(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not DaraCore.is_null(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not DaraCore.is_null(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not DaraCore.is_null(request.relation_id):
            query['RelationId'] = request.relation_id
        if not DaraCore.is_null(request.relation_operation):
            query['RelationOperation'] = request.relation_operation
        if not DaraCore.is_null(request.relation_type):
            query['RelationType'] = request.relation_type
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.role_codes):
            query['RoleCodes'] = request.role_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountRelation',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_relation_with_options_async(
        self,
        request: main_models.ModifyAccountRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_nick):
            query['ChildNick'] = request.child_nick
        if not DaraCore.is_null(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not DaraCore.is_null(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not DaraCore.is_null(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not DaraCore.is_null(request.relation_id):
            query['RelationId'] = request.relation_id
        if not DaraCore.is_null(request.relation_operation):
            query['RelationOperation'] = request.relation_operation
        if not DaraCore.is_null(request.relation_type):
            query['RelationType'] = request.relation_type
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        if not DaraCore.is_null(request.role_codes):
            query['RoleCodes'] = request.role_codes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountRelation',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_relation(
        self,
        request: main_models.ModifyAccountRelationRequest,
    ) -> main_models.ModifyAccountRelationResponse:
        runtime = RuntimeOptions()
        return self.modify_account_relation_with_options(request, runtime)

    async def modify_account_relation_async(
        self,
        request: main_models.ModifyAccountRelationRequest,
    ) -> main_models.ModifyAccountRelationResponse:
        runtime = RuntimeOptions()
        return await self.modify_account_relation_with_options_async(request, runtime)

    def modify_cost_unit_with_options(
        self,
        request: main_models.ModifyCostUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCostUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.unit_entity_list):
            query['UnitEntityList'] = request.unit_entity_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCostUnit',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCostUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cost_unit_with_options_async(
        self,
        request: main_models.ModifyCostUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCostUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.unit_entity_list):
            query['UnitEntityList'] = request.unit_entity_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCostUnit',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCostUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cost_unit(
        self,
        request: main_models.ModifyCostUnitRequest,
    ) -> main_models.ModifyCostUnitResponse:
        runtime = RuntimeOptions()
        return self.modify_cost_unit_with_options(request, runtime)

    async def modify_cost_unit_async(
        self,
        request: main_models.ModifyCostUnitRequest,
    ) -> main_models.ModifyCostUnitResponse:
        runtime = RuntimeOptions()
        return await self.modify_cost_unit_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: main_models.ModifyInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parameter):
            query['Parameter'] = request.parameter
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: main_models.ModifyInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parameter):
            query['Parameter'] = request.parameter
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance(
        self,
        request: main_models.ModifyInstanceRequest,
    ) -> main_models.ModifyInstanceResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    async def modify_instance_async(
        self,
        request: main_models.ModifyInstanceRequest,
    ) -> main_models.ModifyInstanceResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_with_options_async(request, runtime)

    def pay_order_with_options(
        self,
        request: main_models.PayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PayOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buyer_id):
            query['BuyerId'] = request.buyer_id
        if not DaraCore.is_null(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.pay_submit_uid):
            query['PaySubmitUid'] = request.pay_submit_uid
        if not DaraCore.is_null(request.payer_id):
            query['PayerId'] = request.payer_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PayOrder',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def pay_order_with_options_async(
        self,
        request: main_models.PayOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PayOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buyer_id):
            query['BuyerId'] = request.buyer_id
        if not DaraCore.is_null(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.pay_submit_uid):
            query['PaySubmitUid'] = request.pay_submit_uid
        if not DaraCore.is_null(request.payer_id):
            query['PayerId'] = request.payer_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PayOrder',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pay_order(
        self,
        request: main_models.PayOrderRequest,
    ) -> main_models.PayOrderResponse:
        runtime = RuntimeOptions()
        return self.pay_order_with_options(request, runtime)

    async def pay_order_async(
        self,
        request: main_models.PayOrderRequest,
    ) -> main_models.PayOrderResponse:
        runtime = RuntimeOptions()
        return await self.pay_order_with_options_async(request, runtime)

    def query_account_balance_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountBalanceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryAccountBalance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountBalanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_balance_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountBalanceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryAccountBalance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountBalanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_balance(self) -> main_models.QueryAccountBalanceResponse:
        runtime = RuntimeOptions()
        return self.query_account_balance_with_options(runtime)

    async def query_account_balance_async(self) -> main_models.QueryAccountBalanceResponse:
        runtime = RuntimeOptions()
        return await self.query_account_balance_with_options_async(runtime)

    def query_account_bill_with_options(
        self,
        request: main_models.QueryAccountBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.is_group_by_product):
            query['IsGroupByProduct'] = request.is_group_by_product
        if not DaraCore.is_null(request.owner_id):
            query['OwnerID'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_bill_with_options_async(
        self,
        request: main_models.QueryAccountBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.is_group_by_product):
            query['IsGroupByProduct'] = request.is_group_by_product
        if not DaraCore.is_null(request.owner_id):
            query['OwnerID'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_bill(
        self,
        request: main_models.QueryAccountBillRequest,
    ) -> main_models.QueryAccountBillResponse:
        runtime = RuntimeOptions()
        return self.query_account_bill_with_options(request, runtime)

    async def query_account_bill_async(
        self,
        request: main_models.QueryAccountBillRequest,
    ) -> main_models.QueryAccountBillResponse:
        runtime = RuntimeOptions()
        return await self.query_account_bill_with_options_async(request, runtime)

    def query_account_transaction_details_with_options(
        self,
        request: main_models.QueryAccountTransactionDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountTransactionDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.record_id):
            query['RecordID'] = request.record_id
        if not DaraCore.is_null(request.transaction_channel):
            query['TransactionChannel'] = request.transaction_channel
        if not DaraCore.is_null(request.transaction_channel_sn):
            query['TransactionChannelSN'] = request.transaction_channel_sn
        if not DaraCore.is_null(request.transaction_number):
            query['TransactionNumber'] = request.transaction_number
        if not DaraCore.is_null(request.transaction_type):
            query['TransactionType'] = request.transaction_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountTransactionDetails',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountTransactionDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_transaction_details_with_options_async(
        self,
        request: main_models.QueryAccountTransactionDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountTransactionDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.record_id):
            query['RecordID'] = request.record_id
        if not DaraCore.is_null(request.transaction_channel):
            query['TransactionChannel'] = request.transaction_channel
        if not DaraCore.is_null(request.transaction_channel_sn):
            query['TransactionChannelSN'] = request.transaction_channel_sn
        if not DaraCore.is_null(request.transaction_number):
            query['TransactionNumber'] = request.transaction_number
        if not DaraCore.is_null(request.transaction_type):
            query['TransactionType'] = request.transaction_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountTransactionDetails',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountTransactionDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_transaction_details(
        self,
        request: main_models.QueryAccountTransactionDetailsRequest,
    ) -> main_models.QueryAccountTransactionDetailsResponse:
        runtime = RuntimeOptions()
        return self.query_account_transaction_details_with_options(request, runtime)

    async def query_account_transaction_details_async(
        self,
        request: main_models.QueryAccountTransactionDetailsRequest,
    ) -> main_models.QueryAccountTransactionDetailsResponse:
        runtime = RuntimeOptions()
        return await self.query_account_transaction_details_with_options_async(request, runtime)

    def query_account_transactions_with_options(
        self,
        request: main_models.QueryAccountTransactionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountTransactionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.record_id):
            query['RecordID'] = request.record_id
        if not DaraCore.is_null(request.transaction_channel):
            query['TransactionChannel'] = request.transaction_channel
        if not DaraCore.is_null(request.transaction_channel_sn):
            query['TransactionChannelSN'] = request.transaction_channel_sn
        if not DaraCore.is_null(request.transaction_flow):
            query['TransactionFlow'] = request.transaction_flow
        if not DaraCore.is_null(request.transaction_number):
            query['TransactionNumber'] = request.transaction_number
        if not DaraCore.is_null(request.transaction_type):
            query['TransactionType'] = request.transaction_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountTransactions',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountTransactionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_transactions_with_options_async(
        self,
        request: main_models.QueryAccountTransactionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAccountTransactionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.record_id):
            query['RecordID'] = request.record_id
        if not DaraCore.is_null(request.transaction_channel):
            query['TransactionChannel'] = request.transaction_channel
        if not DaraCore.is_null(request.transaction_channel_sn):
            query['TransactionChannelSN'] = request.transaction_channel_sn
        if not DaraCore.is_null(request.transaction_flow):
            query['TransactionFlow'] = request.transaction_flow
        if not DaraCore.is_null(request.transaction_number):
            query['TransactionNumber'] = request.transaction_number
        if not DaraCore.is_null(request.transaction_type):
            query['TransactionType'] = request.transaction_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAccountTransactions',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAccountTransactionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_transactions(
        self,
        request: main_models.QueryAccountTransactionsRequest,
    ) -> main_models.QueryAccountTransactionsResponse:
        runtime = RuntimeOptions()
        return self.query_account_transactions_with_options(request, runtime)

    async def query_account_transactions_async(
        self,
        request: main_models.QueryAccountTransactionsRequest,
    ) -> main_models.QueryAccountTransactionsResponse:
        runtime = RuntimeOptions()
        return await self.query_account_transactions_with_options_async(request, runtime)

    def query_available_instances_with_options(
        self,
        request: main_models.QueryAvailableInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvailableInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.end_time_end):
            query['EndTimeEnd'] = request.end_time_end
        if not DaraCore.is_null(request.end_time_start):
            query['EndTimeStart'] = request.end_time_start
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIDs'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAvailableInstances',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvailableInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_available_instances_with_options_async(
        self,
        request: main_models.QueryAvailableInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvailableInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.end_time_end):
            query['EndTimeEnd'] = request.end_time_end
        if not DaraCore.is_null(request.end_time_start):
            query['EndTimeStart'] = request.end_time_start
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIDs'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAvailableInstances',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvailableInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_available_instances(
        self,
        request: main_models.QueryAvailableInstancesRequest,
    ) -> main_models.QueryAvailableInstancesResponse:
        runtime = RuntimeOptions()
        return self.query_available_instances_with_options(request, runtime)

    async def query_available_instances_async(
        self,
        request: main_models.QueryAvailableInstancesRequest,
    ) -> main_models.QueryAvailableInstancesResponse:
        runtime = RuntimeOptions()
        return await self.query_available_instances_with_options_async(request, runtime)

    def query_bill_with_options(
        self,
        request: main_models.QueryBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.is_display_local_currency):
            query['IsDisplayLocalCurrency'] = request.is_display_local_currency
        if not DaraCore.is_null(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_bill_with_options_async(
        self,
        request: main_models.QueryBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.is_display_local_currency):
            query['IsDisplayLocalCurrency'] = request.is_display_local_currency
        if not DaraCore.is_null(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_bill(
        self,
        request: main_models.QueryBillRequest,
    ) -> main_models.QueryBillResponse:
        runtime = RuntimeOptions()
        return self.query_bill_with_options(request, runtime)

    async def query_bill_async(
        self,
        request: main_models.QueryBillRequest,
    ) -> main_models.QueryBillResponse:
        runtime = RuntimeOptions()
        return await self.query_bill_with_options_async(request, runtime)

    def query_bill_overview_with_options(
        self,
        request: main_models.QueryBillOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBillOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBillOverview',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBillOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_bill_overview_with_options_async(
        self,
        request: main_models.QueryBillOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBillOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryBillOverview',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBillOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_bill_overview(
        self,
        request: main_models.QueryBillOverviewRequest,
    ) -> main_models.QueryBillOverviewResponse:
        runtime = RuntimeOptions()
        return self.query_bill_overview_with_options(request, runtime)

    async def query_bill_overview_async(
        self,
        request: main_models.QueryBillOverviewRequest,
    ) -> main_models.QueryBillOverviewResponse:
        runtime = RuntimeOptions()
        return await self.query_bill_overview_with_options_async(request, runtime)

    def query_bill_to_osssubscription_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBillToOSSSubscriptionResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryBillToOSSSubscription',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBillToOSSSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_bill_to_osssubscription_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.QueryBillToOSSSubscriptionResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'QueryBillToOSSSubscription',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryBillToOSSSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_bill_to_osssubscription(self) -> main_models.QueryBillToOSSSubscriptionResponse:
        runtime = RuntimeOptions()
        return self.query_bill_to_osssubscription_with_options(runtime)

    async def query_bill_to_osssubscription_async(self) -> main_models.QueryBillToOSSSubscriptionResponse:
        runtime = RuntimeOptions()
        return await self.query_bill_to_osssubscription_with_options_async(runtime)

    def query_cash_coupons_with_options(
        self,
        request: main_models.QueryCashCouponsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCashCouponsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_or_not):
            query['EffectiveOrNot'] = request.effective_or_not
        if not DaraCore.is_null(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not DaraCore.is_null(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCashCoupons',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCashCouponsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cash_coupons_with_options_async(
        self,
        request: main_models.QueryCashCouponsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCashCouponsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_or_not):
            query['EffectiveOrNot'] = request.effective_or_not
        if not DaraCore.is_null(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not DaraCore.is_null(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCashCoupons',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCashCouponsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cash_coupons(
        self,
        request: main_models.QueryCashCouponsRequest,
    ) -> main_models.QueryCashCouponsResponse:
        runtime = RuntimeOptions()
        return self.query_cash_coupons_with_options(request, runtime)

    async def query_cash_coupons_async(
        self,
        request: main_models.QueryCashCouponsRequest,
    ) -> main_models.QueryCashCouponsResponse:
        runtime = RuntimeOptions()
        return await self.query_cash_coupons_with_options_async(request, runtime)

    def query_commodity_list_with_options(
        self,
        request: main_models.QueryCommodityListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCommodityListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCommodityList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCommodityListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_commodity_list_with_options_async(
        self,
        request: main_models.QueryCommodityListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCommodityListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCommodityList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCommodityListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_commodity_list(
        self,
        request: main_models.QueryCommodityListRequest,
    ) -> main_models.QueryCommodityListResponse:
        runtime = RuntimeOptions()
        return self.query_commodity_list_with_options(request, runtime)

    async def query_commodity_list_async(
        self,
        request: main_models.QueryCommodityListRequest,
    ) -> main_models.QueryCommodityListResponse:
        runtime = RuntimeOptions()
        return await self.query_commodity_list_with_options_async(request, runtime)

    def query_cost_unit_with_options(
        self,
        request: main_models.QueryCostUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCostUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_unit_id):
            query['ParentUnitId'] = request.parent_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCostUnit',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCostUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cost_unit_with_options_async(
        self,
        request: main_models.QueryCostUnitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCostUnitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_unit_id):
            query['ParentUnitId'] = request.parent_unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCostUnit',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCostUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cost_unit(
        self,
        request: main_models.QueryCostUnitRequest,
    ) -> main_models.QueryCostUnitResponse:
        runtime = RuntimeOptions()
        return self.query_cost_unit_with_options(request, runtime)

    async def query_cost_unit_async(
        self,
        request: main_models.QueryCostUnitRequest,
    ) -> main_models.QueryCostUnitResponse:
        runtime = RuntimeOptions()
        return await self.query_cost_unit_with_options_async(request, runtime)

    def query_cost_unit_resource_with_options(
        self,
        request: main_models.QueryCostUnitResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCostUnitResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.unit_id):
            query['UnitId'] = request.unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCostUnitResource',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCostUnitResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cost_unit_resource_with_options_async(
        self,
        request: main_models.QueryCostUnitResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCostUnitResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.unit_id):
            query['UnitId'] = request.unit_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCostUnitResource',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCostUnitResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cost_unit_resource(
        self,
        request: main_models.QueryCostUnitResourceRequest,
    ) -> main_models.QueryCostUnitResourceResponse:
        runtime = RuntimeOptions()
        return self.query_cost_unit_resource_with_options(request, runtime)

    async def query_cost_unit_resource_async(
        self,
        request: main_models.QueryCostUnitResourceRequest,
    ) -> main_models.QueryCostUnitResourceResponse:
        runtime = RuntimeOptions()
        return await self.query_cost_unit_resource_with_options_async(request, runtime)

    def query_customer_address_list_with_options(
        self,
        request: main_models.QueryCustomerAddressListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomerAddressListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomerAddressList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomerAddressListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_customer_address_list_with_options_async(
        self,
        request: main_models.QueryCustomerAddressListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomerAddressListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomerAddressList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomerAddressListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_customer_address_list(
        self,
        request: main_models.QueryCustomerAddressListRequest,
    ) -> main_models.QueryCustomerAddressListResponse:
        runtime = RuntimeOptions()
        return self.query_customer_address_list_with_options(request, runtime)

    async def query_customer_address_list_async(
        self,
        request: main_models.QueryCustomerAddressListRequest,
    ) -> main_models.QueryCustomerAddressListResponse:
        runtime = RuntimeOptions()
        return await self.query_customer_address_list_with_options_async(request, runtime)

    def query_dputilization_detail_with_options(
        self,
        request: main_models.QueryDPUtilizationDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDPUtilizationDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.deducted_instance_id):
            query['DeductedInstanceId'] = request.deducted_instance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.include_share):
            query['IncludeShare'] = request.include_share
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.last_token):
            query['LastToken'] = request.last_token
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDPUtilizationDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDPUtilizationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dputilization_detail_with_options_async(
        self,
        request: main_models.QueryDPUtilizationDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDPUtilizationDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.deducted_instance_id):
            query['DeductedInstanceId'] = request.deducted_instance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.include_share):
            query['IncludeShare'] = request.include_share
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.last_token):
            query['LastToken'] = request.last_token
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDPUtilizationDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDPUtilizationDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dputilization_detail(
        self,
        request: main_models.QueryDPUtilizationDetailRequest,
    ) -> main_models.QueryDPUtilizationDetailResponse:
        runtime = RuntimeOptions()
        return self.query_dputilization_detail_with_options(request, runtime)

    async def query_dputilization_detail_async(
        self,
        request: main_models.QueryDPUtilizationDetailRequest,
    ) -> main_models.QueryDPUtilizationDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_dputilization_detail_with_options_async(request, runtime)

    def query_evaluate_list_with_options(
        self,
        request: main_models.QueryEvaluateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEvaluateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not DaraCore.is_null(request.biz_type_list):
            query['BizTypeList'] = request.biz_type_list
        if not DaraCore.is_null(request.end_amount):
            query['EndAmount'] = request.end_amount
        if not DaraCore.is_null(request.end_biz_time):
            query['EndBizTime'] = request.end_biz_time
        if not DaraCore.is_null(request.end_search_time):
            query['EndSearchTime'] = request.end_search_time
        if not DaraCore.is_null(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        if not DaraCore.is_null(request.start_amount):
            query['StartAmount'] = request.start_amount
        if not DaraCore.is_null(request.start_biz_time):
            query['StartBizTime'] = request.start_biz_time
        if not DaraCore.is_null(request.start_search_time):
            query['StartSearchTime'] = request.start_search_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEvaluateList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEvaluateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_evaluate_list_with_options_async(
        self,
        request: main_models.QueryEvaluateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryEvaluateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not DaraCore.is_null(request.biz_type_list):
            query['BizTypeList'] = request.biz_type_list
        if not DaraCore.is_null(request.end_amount):
            query['EndAmount'] = request.end_amount
        if not DaraCore.is_null(request.end_biz_time):
            query['EndBizTime'] = request.end_biz_time
        if not DaraCore.is_null(request.end_search_time):
            query['EndSearchTime'] = request.end_search_time
        if not DaraCore.is_null(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        if not DaraCore.is_null(request.start_amount):
            query['StartAmount'] = request.start_amount
        if not DaraCore.is_null(request.start_biz_time):
            query['StartBizTime'] = request.start_biz_time
        if not DaraCore.is_null(request.start_search_time):
            query['StartSearchTime'] = request.start_search_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryEvaluateList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryEvaluateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_evaluate_list(
        self,
        request: main_models.QueryEvaluateListRequest,
    ) -> main_models.QueryEvaluateListResponse:
        runtime = RuntimeOptions()
        return self.query_evaluate_list_with_options(request, runtime)

    async def query_evaluate_list_async(
        self,
        request: main_models.QueryEvaluateListRequest,
    ) -> main_models.QueryEvaluateListResponse:
        runtime = RuntimeOptions()
        return await self.query_evaluate_list_with_options_async(request, runtime)

    def query_financial_account_info_with_options(
        self,
        request: main_models.QueryFinancialAccountInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFinancialAccountInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFinancialAccountInfo',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFinancialAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_financial_account_info_with_options_async(
        self,
        request: main_models.QueryFinancialAccountInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFinancialAccountInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFinancialAccountInfo',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFinancialAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_financial_account_info(
        self,
        request: main_models.QueryFinancialAccountInfoRequest,
    ) -> main_models.QueryFinancialAccountInfoResponse:
        runtime = RuntimeOptions()
        return self.query_financial_account_info_with_options(request, runtime)

    async def query_financial_account_info_async(
        self,
        request: main_models.QueryFinancialAccountInfoRequest,
    ) -> main_models.QueryFinancialAccountInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_financial_account_info_with_options_async(request, runtime)

    def query_instance_bill_with_options(
        self,
        request: main_models.QueryInstanceBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.is_billing_item):
            query['IsBillingItem'] = request.is_billing_item
        if not DaraCore.is_null(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstanceBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_bill_with_options_async(
        self,
        request: main_models.QueryInstanceBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.is_billing_item):
            query['IsBillingItem'] = request.is_billing_item
        if not DaraCore.is_null(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstanceBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance_bill(
        self,
        request: main_models.QueryInstanceBillRequest,
    ) -> main_models.QueryInstanceBillResponse:
        runtime = RuntimeOptions()
        return self.query_instance_bill_with_options(request, runtime)

    async def query_instance_bill_async(
        self,
        request: main_models.QueryInstanceBillRequest,
    ) -> main_models.QueryInstanceBillResponse:
        runtime = RuntimeOptions()
        return await self.query_instance_bill_with_options_async(request, runtime)

    def query_instance_by_tag_with_options(
        self,
        request: main_models.QueryInstanceByTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceByTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstanceByTag',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceByTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_by_tag_with_options_async(
        self,
        request: main_models.QueryInstanceByTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceByTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstanceByTag',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceByTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance_by_tag(
        self,
        request: main_models.QueryInstanceByTagRequest,
    ) -> main_models.QueryInstanceByTagResponse:
        runtime = RuntimeOptions()
        return self.query_instance_by_tag_with_options(request, runtime)

    async def query_instance_by_tag_async(
        self,
        request: main_models.QueryInstanceByTagRequest,
    ) -> main_models.QueryInstanceByTagResponse:
        runtime = RuntimeOptions()
        return await self.query_instance_by_tag_with_options_async(request, runtime)

    def query_instance_gaap_cost_with_options(
        self,
        request: main_models.QueryInstanceGaapCostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceGaapCostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstanceGaapCost',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceGaapCostResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_gaap_cost_with_options_async(
        self,
        request: main_models.QueryInstanceGaapCostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInstanceGaapCostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInstanceGaapCost',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInstanceGaapCostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance_gaap_cost(
        self,
        request: main_models.QueryInstanceGaapCostRequest,
    ) -> main_models.QueryInstanceGaapCostResponse:
        runtime = RuntimeOptions()
        return self.query_instance_gaap_cost_with_options(request, runtime)

    async def query_instance_gaap_cost_async(
        self,
        request: main_models.QueryInstanceGaapCostRequest,
    ) -> main_models.QueryInstanceGaapCostResponse:
        runtime = RuntimeOptions()
        return await self.query_instance_gaap_cost_with_options_async(request, runtime)

    def query_invoicing_customer_list_with_options(
        self,
        request: main_models.QueryInvoicingCustomerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInvoicingCustomerListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInvoicingCustomerList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInvoicingCustomerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_invoicing_customer_list_with_options_async(
        self,
        request: main_models.QueryInvoicingCustomerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInvoicingCustomerListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInvoicingCustomerList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInvoicingCustomerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_invoicing_customer_list(
        self,
        request: main_models.QueryInvoicingCustomerListRequest,
    ) -> main_models.QueryInvoicingCustomerListResponse:
        runtime = RuntimeOptions()
        return self.query_invoicing_customer_list_with_options(request, runtime)

    async def query_invoicing_customer_list_async(
        self,
        request: main_models.QueryInvoicingCustomerListRequest,
    ) -> main_models.QueryInvoicingCustomerListResponse:
        runtime = RuntimeOptions()
        return await self.query_invoicing_customer_list_with_options_async(request, runtime)

    def query_orders_with_options(
        self,
        request: main_models.QueryOrdersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrdersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_status):
            query['PaymentStatus'] = request.payment_status
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOrders',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_orders_with_options_async(
        self,
        request: main_models.QueryOrdersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryOrdersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_status):
            query['PaymentStatus'] = request.payment_status
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryOrders',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.query_orders_with_options(request, runtime)

    async def query_orders_async(
        self,
        request: main_models.QueryOrdersRequest,
    ) -> main_models.QueryOrdersResponse:
        runtime = RuntimeOptions()
        return await self.query_orders_with_options_async(request, runtime)

    def query_permission_list_with_options(
        self,
        request: main_models.QueryPermissionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPermissionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.relation_id):
            query['RelationId'] = request.relation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPermissionList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPermissionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_permission_list_with_options_async(
        self,
        request: main_models.QueryPermissionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPermissionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.relation_id):
            query['RelationId'] = request.relation_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPermissionList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPermissionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_permission_list(
        self,
        request: main_models.QueryPermissionListRequest,
    ) -> main_models.QueryPermissionListResponse:
        runtime = RuntimeOptions()
        return self.query_permission_list_with_options(request, runtime)

    async def query_permission_list_async(
        self,
        request: main_models.QueryPermissionListRequest,
    ) -> main_models.QueryPermissionListResponse:
        runtime = RuntimeOptions()
        return await self.query_permission_list_with_options_async(request, runtime)

    def query_prepaid_cards_with_options(
        self,
        request: main_models.QueryPrepaidCardsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPrepaidCardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_or_not):
            query['EffectiveOrNot'] = request.effective_or_not
        if not DaraCore.is_null(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not DaraCore.is_null(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPrepaidCards',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPrepaidCardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_prepaid_cards_with_options_async(
        self,
        request: main_models.QueryPrepaidCardsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPrepaidCardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_or_not):
            query['EffectiveOrNot'] = request.effective_or_not
        if not DaraCore.is_null(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not DaraCore.is_null(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPrepaidCards',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPrepaidCardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_prepaid_cards(
        self,
        request: main_models.QueryPrepaidCardsRequest,
    ) -> main_models.QueryPrepaidCardsResponse:
        runtime = RuntimeOptions()
        return self.query_prepaid_cards_with_options(request, runtime)

    async def query_prepaid_cards_async(
        self,
        request: main_models.QueryPrepaidCardsRequest,
    ) -> main_models.QueryPrepaidCardsResponse:
        runtime = RuntimeOptions()
        return await self.query_prepaid_cards_with_options_async(request, runtime)

    def query_price_entity_list_with_options(
        self,
        request: main_models.QueryPriceEntityListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPriceEntityListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPriceEntityList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPriceEntityListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_price_entity_list_with_options_async(
        self,
        request: main_models.QueryPriceEntityListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPriceEntityListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryPriceEntityList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPriceEntityListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_price_entity_list(
        self,
        request: main_models.QueryPriceEntityListRequest,
    ) -> main_models.QueryPriceEntityListResponse:
        runtime = RuntimeOptions()
        return self.query_price_entity_list_with_options(request, runtime)

    async def query_price_entity_list_async(
        self,
        request: main_models.QueryPriceEntityListRequest,
    ) -> main_models.QueryPriceEntityListResponse:
        runtime = RuntimeOptions()
        return await self.query_price_entity_list_with_options_async(request, runtime)

    def query_product_list_with_options(
        self,
        request: main_models.QueryProductListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryProductListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_total_count):
            query['QueryTotalCount'] = request.query_total_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryProductList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryProductListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_product_list_with_options_async(
        self,
        request: main_models.QueryProductListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryProductListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_total_count):
            query['QueryTotalCount'] = request.query_total_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryProductList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryProductListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_product_list(
        self,
        request: main_models.QueryProductListRequest,
    ) -> main_models.QueryProductListResponse:
        runtime = RuntimeOptions()
        return self.query_product_list_with_options(request, runtime)

    async def query_product_list_async(
        self,
        request: main_models.QueryProductListRequest,
    ) -> main_models.QueryProductListResponse:
        runtime = RuntimeOptions()
        return await self.query_product_list_with_options_async(request, runtime)

    def query_riutilization_detail_with_options(
        self,
        request: main_models.QueryRIUtilizationDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRIUtilizationDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deducted_instance_id):
            query['DeductedInstanceId'] = request.deducted_instance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.ricommodity_code):
            query['RICommodityCode'] = request.ricommodity_code
        if not DaraCore.is_null(request.riinstance_id):
            query['RIInstanceId'] = request.riinstance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRIUtilizationDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRIUtilizationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_riutilization_detail_with_options_async(
        self,
        request: main_models.QueryRIUtilizationDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRIUtilizationDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deducted_instance_id):
            query['DeductedInstanceId'] = request.deducted_instance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.ricommodity_code):
            query['RICommodityCode'] = request.ricommodity_code
        if not DaraCore.is_null(request.riinstance_id):
            query['RIInstanceId'] = request.riinstance_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRIUtilizationDetail',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRIUtilizationDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_riutilization_detail(
        self,
        request: main_models.QueryRIUtilizationDetailRequest,
    ) -> main_models.QueryRIUtilizationDetailResponse:
        runtime = RuntimeOptions()
        return self.query_riutilization_detail_with_options(request, runtime)

    async def query_riutilization_detail_async(
        self,
        request: main_models.QueryRIUtilizationDetailRequest,
    ) -> main_models.QueryRIUtilizationDetailResponse:
        runtime = RuntimeOptions()
        return await self.query_riutilization_detail_with_options_async(request, runtime)

    def query_redeem_with_options(
        self,
        request: main_models.QueryRedeemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRedeemResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRedeem',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRedeemResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_redeem_with_options_async(
        self,
        request: main_models.QueryRedeemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRedeemResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRedeem',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRedeemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_redeem(
        self,
        request: main_models.QueryRedeemRequest,
    ) -> main_models.QueryRedeemResponse:
        runtime = RuntimeOptions()
        return self.query_redeem_with_options(request, runtime)

    async def query_redeem_async(
        self,
        request: main_models.QueryRedeemRequest,
    ) -> main_models.QueryRedeemResponse:
        runtime = RuntimeOptions()
        return await self.query_redeem_with_options_async(request, runtime)

    def query_relation_list_with_options(
        self,
        request: main_models.QueryRelationListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRelationListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRelationList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRelationListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_relation_list_with_options_async(
        self,
        request: main_models.QueryRelationListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryRelationListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status_list):
            query['StatusList'] = request.status_list
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryRelationList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryRelationListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_relation_list(
        self,
        request: main_models.QueryRelationListRequest,
    ) -> main_models.QueryRelationListResponse:
        runtime = RuntimeOptions()
        return self.query_relation_list_with_options(request, runtime)

    async def query_relation_list_async(
        self,
        request: main_models.QueryRelationListRequest,
    ) -> main_models.QueryRelationListResponse:
        runtime = RuntimeOptions()
        return await self.query_relation_list_with_options_async(request, runtime)

    def query_reseller_available_quota_with_options(
        self,
        request: main_models.QueryResellerAvailableQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryResellerAvailableQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.item_codes):
            query['ItemCodes'] = request.item_codes
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryResellerAvailableQuota',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryResellerAvailableQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_reseller_available_quota_with_options_async(
        self,
        request: main_models.QueryResellerAvailableQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryResellerAvailableQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.item_codes):
            query['ItemCodes'] = request.item_codes
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryResellerAvailableQuota',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryResellerAvailableQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_reseller_available_quota(
        self,
        request: main_models.QueryResellerAvailableQuotaRequest,
    ) -> main_models.QueryResellerAvailableQuotaResponse:
        runtime = RuntimeOptions()
        return self.query_reseller_available_quota_with_options(request, runtime)

    async def query_reseller_available_quota_async(
        self,
        request: main_models.QueryResellerAvailableQuotaRequest,
    ) -> main_models.QueryResellerAvailableQuotaResponse:
        runtime = RuntimeOptions()
        return await self.query_reseller_available_quota_with_options_async(request, runtime)

    def query_reseller_user_alarm_threshold_with_options(
        self,
        request: main_models.QueryResellerUserAlarmThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryResellerUserAlarmThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_type):
            query['AlarmType'] = request.alarm_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryResellerUserAlarmThreshold',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryResellerUserAlarmThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_reseller_user_alarm_threshold_with_options_async(
        self,
        request: main_models.QueryResellerUserAlarmThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryResellerUserAlarmThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_type):
            query['AlarmType'] = request.alarm_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryResellerUserAlarmThreshold',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryResellerUserAlarmThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_reseller_user_alarm_threshold(
        self,
        request: main_models.QueryResellerUserAlarmThresholdRequest,
    ) -> main_models.QueryResellerUserAlarmThresholdResponse:
        runtime = RuntimeOptions()
        return self.query_reseller_user_alarm_threshold_with_options(request, runtime)

    async def query_reseller_user_alarm_threshold_async(
        self,
        request: main_models.QueryResellerUserAlarmThresholdRequest,
    ) -> main_models.QueryResellerUserAlarmThresholdResponse:
        runtime = RuntimeOptions()
        return await self.query_reseller_user_alarm_threshold_with_options_async(request, runtime)

    def query_resource_package_instances_with_options(
        self,
        request: main_models.QueryResourcePackageInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryResourcePackageInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not DaraCore.is_null(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        if not DaraCore.is_null(request.include_partner):
            query['IncludePartner'] = request.include_partner
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryResourcePackageInstances',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryResourcePackageInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_resource_package_instances_with_options_async(
        self,
        request: main_models.QueryResourcePackageInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryResourcePackageInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not DaraCore.is_null(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        if not DaraCore.is_null(request.include_partner):
            query['IncludePartner'] = request.include_partner
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryResourcePackageInstances',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryResourcePackageInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_resource_package_instances(
        self,
        request: main_models.QueryResourcePackageInstancesRequest,
    ) -> main_models.QueryResourcePackageInstancesResponse:
        runtime = RuntimeOptions()
        return self.query_resource_package_instances_with_options(request, runtime)

    async def query_resource_package_instances_async(
        self,
        request: main_models.QueryResourcePackageInstancesRequest,
    ) -> main_models.QueryResourcePackageInstancesResponse:
        runtime = RuntimeOptions()
        return await self.query_resource_package_instances_with_options_async(request, runtime)

    def query_savings_plans_deduct_log_with_options(
        self,
        request: main_models.QuerySavingsPlansDeductLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySavingsPlansDeductLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySavingsPlansDeductLog',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySavingsPlansDeductLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_savings_plans_deduct_log_with_options_async(
        self,
        request: main_models.QuerySavingsPlansDeductLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySavingsPlansDeductLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySavingsPlansDeductLog',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySavingsPlansDeductLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_savings_plans_deduct_log(
        self,
        request: main_models.QuerySavingsPlansDeductLogRequest,
    ) -> main_models.QuerySavingsPlansDeductLogResponse:
        runtime = RuntimeOptions()
        return self.query_savings_plans_deduct_log_with_options(request, runtime)

    async def query_savings_plans_deduct_log_async(
        self,
        request: main_models.QuerySavingsPlansDeductLogRequest,
    ) -> main_models.QuerySavingsPlansDeductLogResponse:
        runtime = RuntimeOptions()
        return await self.query_savings_plans_deduct_log_with_options_async(request, runtime)

    def query_savings_plans_discount_with_options(
        self,
        request: main_models.QuerySavingsPlansDiscountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySavingsPlansDiscountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySavingsPlansDiscount',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySavingsPlansDiscountResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_savings_plans_discount_with_options_async(
        self,
        request: main_models.QuerySavingsPlansDiscountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySavingsPlansDiscountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySavingsPlansDiscount',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySavingsPlansDiscountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_savings_plans_discount(
        self,
        request: main_models.QuerySavingsPlansDiscountRequest,
    ) -> main_models.QuerySavingsPlansDiscountResponse:
        runtime = RuntimeOptions()
        return self.query_savings_plans_discount_with_options(request, runtime)

    async def query_savings_plans_discount_async(
        self,
        request: main_models.QuerySavingsPlansDiscountRequest,
    ) -> main_models.QuerySavingsPlansDiscountResponse:
        runtime = RuntimeOptions()
        return await self.query_savings_plans_discount_with_options_async(request, runtime)

    def query_savings_plans_instance_with_options(
        self,
        request: main_models.QuerySavingsPlansInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySavingsPlansInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySavingsPlansInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySavingsPlansInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_savings_plans_instance_with_options_async(
        self,
        request: main_models.QuerySavingsPlansInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySavingsPlansInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.locale):
            query['Locale'] = request.locale
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySavingsPlansInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySavingsPlansInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_savings_plans_instance(
        self,
        request: main_models.QuerySavingsPlansInstanceRequest,
    ) -> main_models.QuerySavingsPlansInstanceResponse:
        runtime = RuntimeOptions()
        return self.query_savings_plans_instance_with_options(request, runtime)

    async def query_savings_plans_instance_async(
        self,
        request: main_models.QuerySavingsPlansInstanceRequest,
    ) -> main_models.QuerySavingsPlansInstanceResponse:
        runtime = RuntimeOptions()
        return await self.query_savings_plans_instance_with_options_async(request, runtime)

    def query_settle_bill_with_options(
        self,
        request: main_models.QuerySettleBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySettleBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.is_display_local_currency):
            query['IsDisplayLocalCurrency'] = request.is_display_local_currency
        if not DaraCore.is_null(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.record_id):
            query['RecordID'] = request.record_id
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySettleBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySettleBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_settle_bill_with_options_async(
        self,
        request: main_models.QuerySettleBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySettleBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.is_display_local_currency):
            query['IsDisplayLocalCurrency'] = request.is_display_local_currency
        if not DaraCore.is_null(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.record_id):
            query['RecordID'] = request.record_id
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySettleBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySettleBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_settle_bill(
        self,
        request: main_models.QuerySettleBillRequest,
    ) -> main_models.QuerySettleBillResponse:
        runtime = RuntimeOptions()
        return self.query_settle_bill_with_options(request, runtime)

    async def query_settle_bill_async(
        self,
        request: main_models.QuerySettleBillRequest,
    ) -> main_models.QuerySettleBillResponse:
        runtime = RuntimeOptions()
        return await self.query_settle_bill_with_options_async(request, runtime)

    def query_sku_price_list_with_options(
        self,
        tmp_req: main_models.QuerySkuPriceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySkuPriceListResponse:
        tmp_req.validate()
        request = main_models.QuerySkuPriceListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.price_factor_condition_map):
            request.price_factor_condition_map_shrink = Utils.array_to_string_with_specified_style(tmp_req.price_factor_condition_map, 'PriceFactorConditionMap', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySkuPriceList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySkuPriceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sku_price_list_with_options_async(
        self,
        tmp_req: main_models.QuerySkuPriceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySkuPriceListResponse:
        tmp_req.validate()
        request = main_models.QuerySkuPriceListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.price_factor_condition_map):
            request.price_factor_condition_map_shrink = Utils.array_to_string_with_specified_style(tmp_req.price_factor_condition_map, 'PriceFactorConditionMap', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySkuPriceList',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySkuPriceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sku_price_list(
        self,
        request: main_models.QuerySkuPriceListRequest,
    ) -> main_models.QuerySkuPriceListResponse:
        runtime = RuntimeOptions()
        return self.query_sku_price_list_with_options(request, runtime)

    async def query_sku_price_list_async(
        self,
        request: main_models.QuerySkuPriceListRequest,
    ) -> main_models.QuerySkuPriceListResponse:
        runtime = RuntimeOptions()
        return await self.query_sku_price_list_with_options_async(request, runtime)

    def query_split_item_bill_with_options(
        self,
        request: main_models.QuerySplitItemBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySplitItemBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySplitItemBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySplitItemBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_split_item_bill_with_options_async(
        self,
        request: main_models.QuerySplitItemBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySplitItemBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySplitItemBill',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySplitItemBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_split_item_bill(
        self,
        request: main_models.QuerySplitItemBillRequest,
    ) -> main_models.QuerySplitItemBillResponse:
        runtime = RuntimeOptions()
        return self.query_split_item_bill_with_options(request, runtime)

    async def query_split_item_bill_async(
        self,
        request: main_models.QuerySplitItemBillRequest,
    ) -> main_models.QuerySplitItemBillResponse:
        runtime = RuntimeOptions()
        return await self.query_split_item_bill_with_options_async(request, runtime)

    def query_user_oms_data_with_options(
        self,
        request: main_models.QueryUserOmsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserOmsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.table):
            query['Table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserOmsData',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserOmsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_oms_data_with_options_async(
        self,
        request: main_models.QueryUserOmsDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUserOmsDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.marker):
            query['Marker'] = request.marker
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.table):
            query['Table'] = request.table
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUserOmsData',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUserOmsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_oms_data(
        self,
        request: main_models.QueryUserOmsDataRequest,
    ) -> main_models.QueryUserOmsDataResponse:
        runtime = RuntimeOptions()
        return self.query_user_oms_data_with_options(request, runtime)

    async def query_user_oms_data_async(
        self,
        request: main_models.QueryUserOmsDataRequest,
    ) -> main_models.QueryUserOmsDataResponse:
        runtime = RuntimeOptions()
        return await self.query_user_oms_data_with_options_async(request, runtime)

    def refund_instance_with_options(
        self,
        request: main_models.RefundInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefundInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.immediately_release):
            query['ImmediatelyRelease'] = request.immediately_release
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefundInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_instance_with_options_async(
        self,
        request: main_models.RefundInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefundInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.immediately_release):
            query['ImmediatelyRelease'] = request.immediately_release
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefundInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefundInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_instance(
        self,
        request: main_models.RefundInstanceRequest,
    ) -> main_models.RefundInstanceResponse:
        runtime = RuntimeOptions()
        return self.refund_instance_with_options(request, runtime)

    async def refund_instance_async(
        self,
        request: main_models.RefundInstanceRequest,
    ) -> main_models.RefundInstanceResponse:
        runtime = RuntimeOptions()
        return await self.refund_instance_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: main_models.ReleaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: main_models.ReleaseInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance(
        self,
        request: main_models.ReleaseInstanceRequest,
    ) -> main_models.ReleaseInstanceResponse:
        runtime = RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: main_models.ReleaseInstanceRequest,
    ) -> main_models.ReleaseInstanceResponse:
        runtime = RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def relieve_account_relation_with_options(
        self,
        request: main_models.RelieveAccountRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RelieveAccountRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not DaraCore.is_null(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not DaraCore.is_null(request.relation_id):
            query['RelationId'] = request.relation_id
        if not DaraCore.is_null(request.relation_type):
            query['RelationType'] = request.relation_type
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RelieveAccountRelation',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RelieveAccountRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def relieve_account_relation_with_options_async(
        self,
        request: main_models.RelieveAccountRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RelieveAccountRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not DaraCore.is_null(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not DaraCore.is_null(request.relation_id):
            query['RelationId'] = request.relation_id
        if not DaraCore.is_null(request.relation_type):
            query['RelationType'] = request.relation_type
        if not DaraCore.is_null(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RelieveAccountRelation',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RelieveAccountRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def relieve_account_relation(
        self,
        request: main_models.RelieveAccountRelationRequest,
    ) -> main_models.RelieveAccountRelationResponse:
        runtime = RuntimeOptions()
        return self.relieve_account_relation_with_options(request, runtime)

    async def relieve_account_relation_async(
        self,
        request: main_models.RelieveAccountRelationRequest,
    ) -> main_models.RelieveAccountRelationResponse:
        runtime = RuntimeOptions()
        return await self.relieve_account_relation_with_options_async(request, runtime)

    def renew_change_instance_with_options(
        self,
        request: main_models.RenewChangeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewChangeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parameter):
            query['Parameter'] = request.parameter
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewChangeInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewChangeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_change_instance_with_options_async(
        self,
        request: main_models.RenewChangeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewChangeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parameter):
            query['Parameter'] = request.parameter
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewChangeInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewChangeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_change_instance(
        self,
        request: main_models.RenewChangeInstanceRequest,
    ) -> main_models.RenewChangeInstanceResponse:
        runtime = RuntimeOptions()
        return self.renew_change_instance_with_options(request, runtime)

    async def renew_change_instance_async(
        self,
        request: main_models.RenewChangeInstanceRequest,
    ) -> main_models.RenewChangeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.renew_change_instance_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: main_models.RenewInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: main_models.RenewInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def renew_resource_package_with_options(
        self,
        request: main_models.RenewResourcePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewResourcePackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewResourcePackage',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_resource_package_with_options_async(
        self,
        request: main_models.RenewResourcePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewResourcePackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewResourcePackage',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewResourcePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_resource_package(
        self,
        request: main_models.RenewResourcePackageRequest,
    ) -> main_models.RenewResourcePackageResponse:
        runtime = RuntimeOptions()
        return self.renew_resource_package_with_options(request, runtime)

    async def renew_resource_package_async(
        self,
        request: main_models.RenewResourcePackageRequest,
    ) -> main_models.RenewResourcePackageResponse:
        runtime = RuntimeOptions()
        return await self.renew_resource_package_with_options_async(request, runtime)

    def set_all_expiration_day_with_options(
        self,
        request: main_models.SetAllExpirationDayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAllExpirationDayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.unify_expire_day):
            query['UnifyExpireDay'] = request.unify_expire_day
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAllExpirationDay',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAllExpirationDayResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_all_expiration_day_with_options_async(
        self,
        request: main_models.SetAllExpirationDayRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAllExpirationDayResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.unify_expire_day):
            query['UnifyExpireDay'] = request.unify_expire_day
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAllExpirationDay',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAllExpirationDayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_all_expiration_day(
        self,
        request: main_models.SetAllExpirationDayRequest,
    ) -> main_models.SetAllExpirationDayResponse:
        runtime = RuntimeOptions()
        return self.set_all_expiration_day_with_options(request, runtime)

    async def set_all_expiration_day_async(
        self,
        request: main_models.SetAllExpirationDayRequest,
    ) -> main_models.SetAllExpirationDayResponse:
        runtime = RuntimeOptions()
        return await self.set_all_expiration_day_with_options_async(request, runtime)

    def set_renewal_with_options(
        self,
        request: main_models.SetRenewalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetRenewalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIDs'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.renewal_period):
            query['RenewalPeriod'] = request.renewal_period
        if not DaraCore.is_null(request.renewal_period_unit):
            query['RenewalPeriodUnit'] = request.renewal_period_unit
        if not DaraCore.is_null(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetRenewal',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetRenewalResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_renewal_with_options_async(
        self,
        request: main_models.SetRenewalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetRenewalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIDs'] = request.instance_ids
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.renewal_period):
            query['RenewalPeriod'] = request.renewal_period
        if not DaraCore.is_null(request.renewal_period_unit):
            query['RenewalPeriodUnit'] = request.renewal_period_unit
        if not DaraCore.is_null(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not DaraCore.is_null(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetRenewal',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetRenewalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_renewal(
        self,
        request: main_models.SetRenewalRequest,
    ) -> main_models.SetRenewalResponse:
        runtime = RuntimeOptions()
        return self.set_renewal_with_options(request, runtime)

    async def set_renewal_async(
        self,
        request: main_models.SetRenewalRequest,
    ) -> main_models.SetRenewalResponse:
        runtime = RuntimeOptions()
        return await self.set_renewal_with_options_async(request, runtime)

    def set_reseller_user_alarm_threshold_with_options(
        self,
        request: main_models.SetResellerUserAlarmThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetResellerUserAlarmThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_thresholds):
            query['AlarmThresholds'] = request.alarm_thresholds
        if not DaraCore.is_null(request.alarm_type):
            query['AlarmType'] = request.alarm_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetResellerUserAlarmThreshold',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetResellerUserAlarmThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_reseller_user_alarm_threshold_with_options_async(
        self,
        request: main_models.SetResellerUserAlarmThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetResellerUserAlarmThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_thresholds):
            query['AlarmThresholds'] = request.alarm_thresholds
        if not DaraCore.is_null(request.alarm_type):
            query['AlarmType'] = request.alarm_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetResellerUserAlarmThreshold',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetResellerUserAlarmThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_reseller_user_alarm_threshold(
        self,
        request: main_models.SetResellerUserAlarmThresholdRequest,
    ) -> main_models.SetResellerUserAlarmThresholdResponse:
        runtime = RuntimeOptions()
        return self.set_reseller_user_alarm_threshold_with_options(request, runtime)

    async def set_reseller_user_alarm_threshold_async(
        self,
        request: main_models.SetResellerUserAlarmThresholdRequest,
    ) -> main_models.SetResellerUserAlarmThresholdResponse:
        runtime = RuntimeOptions()
        return await self.set_reseller_user_alarm_threshold_with_options_async(request, runtime)

    def set_reseller_user_quota_with_options(
        self,
        request: main_models.SetResellerUserQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetResellerUserQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.currency):
            query['Currency'] = request.currency
        if not DaraCore.is_null(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetResellerUserQuota',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetResellerUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_reseller_user_quota_with_options_async(
        self,
        request: main_models.SetResellerUserQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetResellerUserQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.currency):
            query['Currency'] = request.currency
        if not DaraCore.is_null(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetResellerUserQuota',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetResellerUserQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_reseller_user_quota(
        self,
        request: main_models.SetResellerUserQuotaRequest,
    ) -> main_models.SetResellerUserQuotaResponse:
        runtime = RuntimeOptions()
        return self.set_reseller_user_quota_with_options(request, runtime)

    async def set_reseller_user_quota_async(
        self,
        request: main_models.SetResellerUserQuotaRequest,
    ) -> main_models.SetResellerUserQuotaResponse:
        runtime = RuntimeOptions()
        return await self.set_reseller_user_quota_with_options_async(request, runtime)

    def set_reseller_user_status_with_options(
        self,
        request: main_models.SetResellerUserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetResellerUserStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.stop_mode):
            query['StopMode'] = request.stop_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetResellerUserStatus',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetResellerUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_reseller_user_status_with_options_async(
        self,
        request: main_models.SetResellerUserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetResellerUserStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_type):
            query['BusinessType'] = request.business_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.stop_mode):
            query['StopMode'] = request.stop_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetResellerUserStatus',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetResellerUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_reseller_user_status(
        self,
        request: main_models.SetResellerUserStatusRequest,
    ) -> main_models.SetResellerUserStatusResponse:
        runtime = RuntimeOptions()
        return self.set_reseller_user_status_with_options(request, runtime)

    async def set_reseller_user_status_async(
        self,
        request: main_models.SetResellerUserStatusRequest,
    ) -> main_models.SetResellerUserStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_reseller_user_status_with_options_async(request, runtime)

    def set_saving_plan_user_deduct_rule_with_options(
        self,
        tmp_req: main_models.SetSavingPlanUserDeductRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSavingPlanUserDeductRuleResponse:
        tmp_req.validate()
        request = main_models.SetSavingPlanUserDeductRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not DaraCore.is_null(tmp_req.user_deduct_rules):
            request.user_deduct_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_deduct_rules, 'UserDeductRules', 'json')
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.spn_instance_code):
            body['SpnInstanceCode'] = request.spn_instance_code
        if not DaraCore.is_null(request.user_deduct_rules_shrink):
            body['UserDeductRules'] = request.user_deduct_rules_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetSavingPlanUserDeductRule',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSavingPlanUserDeductRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_saving_plan_user_deduct_rule_with_options_async(
        self,
        tmp_req: main_models.SetSavingPlanUserDeductRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetSavingPlanUserDeductRuleResponse:
        tmp_req.validate()
        request = main_models.SetSavingPlanUserDeductRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not DaraCore.is_null(tmp_req.user_deduct_rules):
            request.user_deduct_rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_deduct_rules, 'UserDeductRules', 'json')
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.spn_instance_code):
            body['SpnInstanceCode'] = request.spn_instance_code
        if not DaraCore.is_null(request.user_deduct_rules_shrink):
            body['UserDeductRules'] = request.user_deduct_rules_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetSavingPlanUserDeductRule',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetSavingPlanUserDeductRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_saving_plan_user_deduct_rule(
        self,
        request: main_models.SetSavingPlanUserDeductRuleRequest,
    ) -> main_models.SetSavingPlanUserDeductRuleResponse:
        runtime = RuntimeOptions()
        return self.set_saving_plan_user_deduct_rule_with_options(request, runtime)

    async def set_saving_plan_user_deduct_rule_async(
        self,
        request: main_models.SetSavingPlanUserDeductRuleRequest,
    ) -> main_models.SetSavingPlanUserDeductRuleResponse:
        runtime = RuntimeOptions()
        return await self.set_saving_plan_user_deduct_rule_with_options_async(request, runtime)

    def subscribe_bill_to_osswith_options(
        self,
        request: main_models.SubscribeBillToOSSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubscribeBillToOSSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not DaraCore.is_null(request.bucket_owner_id):
            query['BucketOwnerId'] = request.bucket_owner_id
        if not DaraCore.is_null(request.bucket_path):
            query['BucketPath'] = request.bucket_path
        if not DaraCore.is_null(request.mult_account_rel_subscribe):
            query['MultAccountRelSubscribe'] = request.mult_account_rel_subscribe
        if not DaraCore.is_null(request.row_limit_per_file):
            query['RowLimitPerFile'] = request.row_limit_per_file
        if not DaraCore.is_null(request.subscribe_bucket):
            query['SubscribeBucket'] = request.subscribe_bucket
        if not DaraCore.is_null(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        if not DaraCore.is_null(request.using_ssl):
            query['UsingSsl'] = request.using_ssl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubscribeBillToOSS',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubscribeBillToOSSResponse(),
            self.call_api(params, req, runtime)
        )

    async def subscribe_bill_to_osswith_options_async(
        self,
        request: main_models.SubscribeBillToOSSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubscribeBillToOSSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not DaraCore.is_null(request.bucket_owner_id):
            query['BucketOwnerId'] = request.bucket_owner_id
        if not DaraCore.is_null(request.bucket_path):
            query['BucketPath'] = request.bucket_path
        if not DaraCore.is_null(request.mult_account_rel_subscribe):
            query['MultAccountRelSubscribe'] = request.mult_account_rel_subscribe
        if not DaraCore.is_null(request.row_limit_per_file):
            query['RowLimitPerFile'] = request.row_limit_per_file
        if not DaraCore.is_null(request.subscribe_bucket):
            query['SubscribeBucket'] = request.subscribe_bucket
        if not DaraCore.is_null(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        if not DaraCore.is_null(request.using_ssl):
            query['UsingSsl'] = request.using_ssl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubscribeBillToOSS',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubscribeBillToOSSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def subscribe_bill_to_oss(
        self,
        request: main_models.SubscribeBillToOSSRequest,
    ) -> main_models.SubscribeBillToOSSResponse:
        runtime = RuntimeOptions()
        return self.subscribe_bill_to_osswith_options(request, runtime)

    async def subscribe_bill_to_oss_async(
        self,
        request: main_models.SubscribeBillToOSSRequest,
    ) -> main_models.SubscribeBillToOSSResponse:
        runtime = RuntimeOptions()
        return await self.subscribe_bill_to_osswith_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unsubscribe_bill_to_osswith_options(
        self,
        request: main_models.UnsubscribeBillToOSSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnsubscribeBillToOSSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mult_account_rel_subscribe):
            query['MultAccountRelSubscribe'] = request.mult_account_rel_subscribe
        if not DaraCore.is_null(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnsubscribeBillToOSS',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnsubscribeBillToOSSResponse(),
            self.call_api(params, req, runtime)
        )

    async def unsubscribe_bill_to_osswith_options_async(
        self,
        request: main_models.UnsubscribeBillToOSSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnsubscribeBillToOSSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mult_account_rel_subscribe):
            query['MultAccountRelSubscribe'] = request.mult_account_rel_subscribe
        if not DaraCore.is_null(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnsubscribeBillToOSS',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnsubscribeBillToOSSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unsubscribe_bill_to_oss(
        self,
        request: main_models.UnsubscribeBillToOSSRequest,
    ) -> main_models.UnsubscribeBillToOSSResponse:
        runtime = RuntimeOptions()
        return self.unsubscribe_bill_to_osswith_options(request, runtime)

    async def unsubscribe_bill_to_oss_async(
        self,
        request: main_models.UnsubscribeBillToOSSRequest,
    ) -> main_models.UnsubscribeBillToOSSResponse:
        runtime = RuntimeOptions()
        return await self.unsubscribe_bill_to_osswith_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_resource_package_with_options(
        self,
        request: main_models.UpgradeResourcePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeResourcePackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeResourcePackage',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_resource_package_with_options_async(
        self,
        request: main_models.UpgradeResourcePackageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeResourcePackageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.specification):
            query['Specification'] = request.specification
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeResourcePackage',
            version = '2017-12-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeResourcePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_resource_package(
        self,
        request: main_models.UpgradeResourcePackageRequest,
    ) -> main_models.UpgradeResourcePackageResponse:
        runtime = RuntimeOptions()
        return self.upgrade_resource_package_with_options(request, runtime)

    async def upgrade_resource_package_async(
        self,
        request: main_models.UpgradeResourcePackageRequest,
    ) -> main_models.UpgradeResourcePackageResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_resource_package_with_options_async(request, runtime)
