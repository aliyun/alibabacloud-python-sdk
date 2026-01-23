# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agency20221216 import models as main_models
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
            'ap-northeast-1': 'agency.aliyuncs.com',
            'ap-northeast-2-pop': 'agency.aliyuncs.com',
            'ap-south-1': 'agency.aliyuncs.com',
            'ap-southeast-2': 'agency.aliyuncs.com',
            'ap-southeast-3': 'agency.aliyuncs.com',
            'ap-southeast-5': 'agency.aliyuncs.com',
            'cn-beijing': 'agency.aliyuncs.com',
            'cn-beijing-finance-1': 'agency.aliyuncs.com',
            'cn-beijing-finance-pop': 'agency.aliyuncs.com',
            'cn-beijing-gov-1': 'agency.aliyuncs.com',
            'cn-beijing-nu16-b01': 'agency.aliyuncs.com',
            'cn-chengdu': 'agency.aliyuncs.com',
            'cn-edge-1': 'agency.aliyuncs.com',
            'cn-fujian': 'agency.aliyuncs.com',
            'cn-haidian-cm12-c01': 'agency.aliyuncs.com',
            'cn-hangzhou': 'agency.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'agency.aliyuncs.com',
            'cn-hangzhou-finance': 'agency.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'agency.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'agency.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'agency.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'agency.aliyuncs.com',
            'cn-hangzhou-test-306': 'agency.aliyuncs.com',
            'cn-hongkong': 'agency.aliyuncs.com',
            'cn-hongkong-finance-pop': 'agency.aliyuncs.com',
            'cn-huhehaote': 'agency.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'agency.aliyuncs.com',
            'cn-north-2-gov-1': 'agency.aliyuncs.com',
            'cn-qingdao': 'agency.aliyuncs.com',
            'cn-qingdao-nebula': 'agency.aliyuncs.com',
            'cn-shanghai': 'agency.aliyuncs.com',
            'cn-shanghai-et15-b01': 'agency.aliyuncs.com',
            'cn-shanghai-et2-b01': 'agency.aliyuncs.com',
            'cn-shanghai-finance-1': 'agency.aliyuncs.com',
            'cn-shanghai-inner': 'agency.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'agency.aliyuncs.com',
            'cn-shenzhen': 'agency.aliyuncs.com',
            'cn-shenzhen-finance-1': 'agency.aliyuncs.com',
            'cn-shenzhen-inner': 'agency.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'agency.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'agency.aliyuncs.com',
            'cn-wuhan': 'agency.aliyuncs.com',
            'cn-wulanchabu': 'agency.aliyuncs.com',
            'cn-yushanfang': 'agency.aliyuncs.com',
            'cn-zhangbei': 'agency.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'agency.aliyuncs.com',
            'cn-zhangjiakou': 'agency.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'agency.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'agency.aliyuncs.com',
            'eu-central-1': 'agency.aliyuncs.com',
            'eu-west-1': 'agency.aliyuncs.com',
            'eu-west-1-oxs': 'agency.aliyuncs.com',
            'me-east-1': 'agency.aliyuncs.com',
            'rus-west-1-pop': 'agency.aliyuncs.com',
            'us-east-1': 'agency.aliyuncs.com',
            'us-west-1': 'agency.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('agency', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_coupon_with_options(
        self,
        request: main_models.CancelCouponRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelCouponResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_id):
            query['CouponId'] = request.coupon_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelCoupon',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelCouponResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_coupon_with_options_async(
        self,
        request: main_models.CancelCouponRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelCouponResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.coupon_id):
            query['CouponId'] = request.coupon_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelCoupon',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelCouponResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_coupon(
        self,
        request: main_models.CancelCouponRequest,
    ) -> main_models.CancelCouponResponse:
        runtime = RuntimeOptions()
        return self.cancel_coupon_with_options(request, runtime)

    async def cancel_coupon_async(
        self,
        request: main_models.CancelCouponRequest,
    ) -> main_models.CancelCouponResponse:
        runtime = RuntimeOptions()
        return await self.cancel_coupon_with_options_async(request, runtime)

    def cancel_subscription_bill_with_options(
        self,
        request: main_models.CancelSubscriptionBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelSubscriptionBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelSubscriptionBill',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelSubscriptionBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_subscription_bill_with_options_async(
        self,
        request: main_models.CancelSubscriptionBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelSubscriptionBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelSubscriptionBill',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelSubscriptionBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_subscription_bill(
        self,
        request: main_models.CancelSubscriptionBillRequest,
    ) -> main_models.CancelSubscriptionBillResponse:
        runtime = RuntimeOptions()
        return self.cancel_subscription_bill_with_options(request, runtime)

    async def cancel_subscription_bill_async(
        self,
        request: main_models.CancelSubscriptionBillRequest,
    ) -> main_models.CancelSubscriptionBillResponse:
        runtime = RuntimeOptions()
        return await self.cancel_subscription_bill_with_options_async(request, runtime)

    def coupon_approval_status_list_with_options(
        self,
        request: main_models.CouponApprovalStatusListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CouponApprovalStatusListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_status):
            query['TemplateStatus'] = request.template_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CouponApprovalStatusList',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CouponApprovalStatusListResponse(),
            self.call_api(params, req, runtime)
        )

    async def coupon_approval_status_list_with_options_async(
        self,
        request: main_models.CouponApprovalStatusListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CouponApprovalStatusListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_status):
            query['TemplateStatus'] = request.template_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CouponApprovalStatusList',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CouponApprovalStatusListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def coupon_approval_status_list(
        self,
        request: main_models.CouponApprovalStatusListRequest,
    ) -> main_models.CouponApprovalStatusListResponse:
        runtime = RuntimeOptions()
        return self.coupon_approval_status_list_with_options(request, runtime)

    async def coupon_approval_status_list_async(
        self,
        request: main_models.CouponApprovalStatusListRequest,
    ) -> main_models.CouponApprovalStatusListResponse:
        runtime = RuntimeOptions()
        return await self.coupon_approval_status_list_with_options_async(request, runtime)

    def create_coupon_template_with_options(
        self,
        tmp_req: main_models.CreateCouponTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCouponTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateCouponTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.product_type):
            request.product_type_shrink = Utils.array_to_string_with_specified_style(tmp_req.product_type, 'ProductType', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.applicable_products):
            query['ApplicableProducts'] = request.applicable_products
        if not DaraCore.is_null(request.cost_bearer):
            query['CostBearer'] = request.cost_bearer
        if not DaraCore.is_null(request.coupon_description):
            query['CouponDescription'] = request.coupon_description
        if not DaraCore.is_null(request.expireddate):
            query['Expireddate'] = request.expireddate
        if not DaraCore.is_null(request.limit_per_person):
            query['LimitPerPerson'] = request.limit_per_person
        if not DaraCore.is_null(request.product_type_shrink):
            query['ProductType'] = request.product_type_shrink
        if not DaraCore.is_null(request.purchase_type):
            query['PurchaseType'] = request.purchase_type
        if not DaraCore.is_null(request.reason_for_application):
            query['ReasonForApplication'] = request.reason_for_application
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.vailddate):
            query['Vailddate'] = request.vailddate
        if not DaraCore.is_null(request.vaildperioddays):
            query['Vaildperioddays'] = request.vaildperioddays
        if not DaraCore.is_null(request.valid_until):
            query['ValidUntil'] = request.valid_until
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCouponTemplate',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCouponTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_coupon_template_with_options_async(
        self,
        tmp_req: main_models.CreateCouponTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCouponTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateCouponTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.product_type):
            request.product_type_shrink = Utils.array_to_string_with_specified_style(tmp_req.product_type, 'ProductType', 'json')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.applicable_products):
            query['ApplicableProducts'] = request.applicable_products
        if not DaraCore.is_null(request.cost_bearer):
            query['CostBearer'] = request.cost_bearer
        if not DaraCore.is_null(request.coupon_description):
            query['CouponDescription'] = request.coupon_description
        if not DaraCore.is_null(request.expireddate):
            query['Expireddate'] = request.expireddate
        if not DaraCore.is_null(request.limit_per_person):
            query['LimitPerPerson'] = request.limit_per_person
        if not DaraCore.is_null(request.product_type_shrink):
            query['ProductType'] = request.product_type_shrink
        if not DaraCore.is_null(request.purchase_type):
            query['PurchaseType'] = request.purchase_type
        if not DaraCore.is_null(request.reason_for_application):
            query['ReasonForApplication'] = request.reason_for_application
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.vailddate):
            query['Vailddate'] = request.vailddate
        if not DaraCore.is_null(request.vaildperioddays):
            query['Vaildperioddays'] = request.vaildperioddays
        if not DaraCore.is_null(request.valid_until):
            query['ValidUntil'] = request.valid_until
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCouponTemplate',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCouponTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_coupon_template(
        self,
        request: main_models.CreateCouponTemplateRequest,
    ) -> main_models.CreateCouponTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_coupon_template_with_options(request, runtime)

    async def create_coupon_template_async(
        self,
        request: main_models.CreateCouponTemplateRequest,
    ) -> main_models.CreateCouponTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_coupon_template_with_options_async(request, runtime)

    def create_customer_with_options(
        self,
        request: main_models.CreateCustomerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_name):
            query['CustomerName'] = request.customer_name
        if not DaraCore.is_null(request.customer_source):
            query['CustomerSource'] = request.customer_source
        if not DaraCore.is_null(request.customer_sub_trade):
            query['CustomerSubTrade'] = request.customer_sub_trade
        if not DaraCore.is_null(request.customer_trade):
            query['CustomerTrade'] = request.customer_trade
        if not DaraCore.is_null(request.nation):
            query['Nation'] = request.nation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomer',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_customer_with_options_async(
        self,
        request: main_models.CreateCustomerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_name):
            query['CustomerName'] = request.customer_name
        if not DaraCore.is_null(request.customer_source):
            query['CustomerSource'] = request.customer_source
        if not DaraCore.is_null(request.customer_sub_trade):
            query['CustomerSubTrade'] = request.customer_sub_trade
        if not DaraCore.is_null(request.customer_trade):
            query['CustomerTrade'] = request.customer_trade
        if not DaraCore.is_null(request.nation):
            query['Nation'] = request.nation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomer',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_customer(
        self,
        request: main_models.CreateCustomerRequest,
    ) -> main_models.CreateCustomerResponse:
        runtime = RuntimeOptions()
        return self.create_customer_with_options(request, runtime)

    async def create_customer_async(
        self,
        request: main_models.CreateCustomerRequest,
    ) -> main_models.CreateCustomerResponse:
        runtime = RuntimeOptions()
        return await self.create_customer_with_options_async(request, runtime)

    def customer_quota_record_list_with_options(
        self,
        request: main_models.CustomerQuotaRecordListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CustomerQuotaRecordListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CustomerQuotaRecordList',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CustomerQuotaRecordListResponse(),
            self.call_api(params, req, runtime)
        )

    async def customer_quota_record_list_with_options_async(
        self,
        request: main_models.CustomerQuotaRecordListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CustomerQuotaRecordListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CustomerQuotaRecordList',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CustomerQuotaRecordListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def customer_quota_record_list(
        self,
        request: main_models.CustomerQuotaRecordListRequest,
    ) -> main_models.CustomerQuotaRecordListResponse:
        runtime = RuntimeOptions()
        return self.customer_quota_record_list_with_options(request, runtime)

    async def customer_quota_record_list_async(
        self,
        request: main_models.CustomerQuotaRecordListRequest,
    ) -> main_models.CustomerQuotaRecordListResponse:
        runtime = RuntimeOptions()
        return await self.customer_quota_record_list_with_options_async(request, runtime)

    def deduct_outstanding_balance_with_options(
        self,
        request: main_models.DeductOutstandingBalanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeductOutstandingBalanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deduct_amount):
            query['DeductAmount'] = request.deduct_amount
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeductOutstandingBalance',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeductOutstandingBalanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def deduct_outstanding_balance_with_options_async(
        self,
        request: main_models.DeductOutstandingBalanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeductOutstandingBalanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deduct_amount):
            query['DeductAmount'] = request.deduct_amount
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeductOutstandingBalance',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeductOutstandingBalanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deduct_outstanding_balance(
        self,
        request: main_models.DeductOutstandingBalanceRequest,
    ) -> main_models.DeductOutstandingBalanceResponse:
        runtime = RuntimeOptions()
        return self.deduct_outstanding_balance_with_options(request, runtime)

    async def deduct_outstanding_balance_async(
        self,
        request: main_models.DeductOutstandingBalanceRequest,
    ) -> main_models.DeductOutstandingBalanceResponse:
        runtime = RuntimeOptions()
        return await self.deduct_outstanding_balance_with_options_async(request, runtime)

    def delete_coupon_template_with_options(
        self,
        request: main_models.DeleteCouponTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCouponTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCouponTemplate',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCouponTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_coupon_template_with_options_async(
        self,
        request: main_models.DeleteCouponTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCouponTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCouponTemplate',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCouponTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_coupon_template(
        self,
        request: main_models.DeleteCouponTemplateRequest,
    ) -> main_models.DeleteCouponTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_coupon_template_with_options(request, runtime)

    async def delete_coupon_template_async(
        self,
        request: main_models.DeleteCouponTemplateRequest,
    ) -> main_models.DeleteCouponTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_coupon_template_with_options_async(request, runtime)

    def edit_end_user_status_with_options(
        self,
        request: main_models.EditEndUserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditEndUserStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditEndUserStatus',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditEndUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_end_user_status_with_options_async(
        self,
        request: main_models.EditEndUserStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditEndUserStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditEndUserStatus',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditEndUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_end_user_status(
        self,
        request: main_models.EditEndUserStatusRequest,
    ) -> main_models.EditEndUserStatusResponse:
        runtime = RuntimeOptions()
        return self.edit_end_user_status_with_options(request, runtime)

    async def edit_end_user_status_async(
        self,
        request: main_models.EditEndUserStatusRequest,
    ) -> main_models.EditEndUserStatusResponse:
        runtime = RuntimeOptions()
        return await self.edit_end_user_status_with_options_async(request, runtime)

    def edit_new_buy_status_with_options(
        self,
        request: main_models.EditNewBuyStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditNewBuyStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_buy_status):
            query['NewBuyStatus'] = request.new_buy_status
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditNewBuyStatus',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditNewBuyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_new_buy_status_with_options_async(
        self,
        request: main_models.EditNewBuyStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditNewBuyStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_buy_status):
            query['NewBuyStatus'] = request.new_buy_status
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditNewBuyStatus',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditNewBuyStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_new_buy_status(
        self,
        request: main_models.EditNewBuyStatusRequest,
    ) -> main_models.EditNewBuyStatusResponse:
        runtime = RuntimeOptions()
        return self.edit_new_buy_status_with_options(request, runtime)

    async def edit_new_buy_status_async(
        self,
        request: main_models.EditNewBuyStatusRequest,
    ) -> main_models.EditNewBuyStatusResponse:
        runtime = RuntimeOptions()
        return await self.edit_new_buy_status_with_options_async(request, runtime)

    def edit_zero_credit_shutdown_with_options(
        self,
        request: main_models.EditZeroCreditShutdownRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditZeroCreditShutdownResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.shutdown_policy):
            query['ShutdownPolicy'] = request.shutdown_policy
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditZeroCreditShutdown',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditZeroCreditShutdownResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_zero_credit_shutdown_with_options_async(
        self,
        request: main_models.EditZeroCreditShutdownRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EditZeroCreditShutdownResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.shutdown_policy):
            query['ShutdownPolicy'] = request.shutdown_policy
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EditZeroCreditShutdown',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EditZeroCreditShutdownResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_zero_credit_shutdown(
        self,
        request: main_models.EditZeroCreditShutdownRequest,
    ) -> main_models.EditZeroCreditShutdownResponse:
        runtime = RuntimeOptions()
        return self.edit_zero_credit_shutdown_with_options(request, runtime)

    async def edit_zero_credit_shutdown_async(
        self,
        request: main_models.EditZeroCreditShutdownRequest,
    ) -> main_models.EditZeroCreditShutdownResponse:
        runtime = RuntimeOptions()
        return await self.edit_zero_credit_shutdown_with_options_async(request, runtime)

    def export_customer_quota_record_with_options(
        self,
        request: main_models.ExportCustomerQuotaRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportCustomerQuotaRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.end_user_pk):
            query['EndUserPk'] = request.end_user_pk
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportCustomerQuotaRecord',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportCustomerQuotaRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_customer_quota_record_with_options_async(
        self,
        request: main_models.ExportCustomerQuotaRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportCustomerQuotaRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.end_user_pk):
            query['EndUserPk'] = request.end_user_pk
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportCustomerQuotaRecord',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportCustomerQuotaRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_customer_quota_record(
        self,
        request: main_models.ExportCustomerQuotaRecordRequest,
    ) -> main_models.ExportCustomerQuotaRecordResponse:
        runtime = RuntimeOptions()
        return self.export_customer_quota_record_with_options(request, runtime)

    async def export_customer_quota_record_async(
        self,
        request: main_models.ExportCustomerQuotaRecordRequest,
    ) -> main_models.ExportCustomerQuotaRecordResponse:
        runtime = RuntimeOptions()
        return await self.export_customer_quota_record_with_options_async(request, runtime)

    def export_reversed_deduction_history_with_options(
        self,
        request: main_models.ExportReversedDeductionHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportReversedDeductionHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.export_uid):
            query['ExportUid'] = request.export_uid
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportReversedDeductionHistory',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportReversedDeductionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_reversed_deduction_history_with_options_async(
        self,
        request: main_models.ExportReversedDeductionHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportReversedDeductionHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.export_uid):
            query['ExportUid'] = request.export_uid
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportReversedDeductionHistory',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportReversedDeductionHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_reversed_deduction_history(
        self,
        request: main_models.ExportReversedDeductionHistoryRequest,
    ) -> main_models.ExportReversedDeductionHistoryResponse:
        runtime = RuntimeOptions()
        return self.export_reversed_deduction_history_with_options(request, runtime)

    async def export_reversed_deduction_history_async(
        self,
        request: main_models.ExportReversedDeductionHistoryRequest,
    ) -> main_models.ExportReversedDeductionHistoryResponse:
        runtime = RuntimeOptions()
        return await self.export_reversed_deduction_history_with_options_async(request, runtime)

    def get_account_info_with_options(
        self,
        request: main_models.GetAccountInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountInfo',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_info_with_options_async(
        self,
        request: main_models.GetAccountInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountInfo',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_info(
        self,
        request: main_models.GetAccountInfoRequest,
    ) -> main_models.GetAccountInfoResponse:
        runtime = RuntimeOptions()
        return self.get_account_info_with_options(request, runtime)

    async def get_account_info_async(
        self,
        request: main_models.GetAccountInfoRequest,
    ) -> main_models.GetAccountInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_account_info_with_options_async(request, runtime)

    def get_commissionable_products_with_options(
        self,
        tmp_req: main_models.GetCommissionableProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCommissionableProductsResponse:
        tmp_req.validate()
        request = main_models.GetCommissionableProductsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_show_status_list):
            request.list_show_status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_show_status_list, 'ListShowStatusList', 'simple')
        query = {}
        if not DaraCore.is_null(request.commodity_code_list):
            query['CommodityCodeList'] = request.commodity_code_list
        if not DaraCore.is_null(request.fiscal_year):
            query['FiscalYear'] = request.fiscal_year
        if not DaraCore.is_null(request.list_show_status_list_shrink):
            query['ListShowStatusList'] = request.list_show_status_list_shrink
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pip_code_list):
            query['PipCodeList'] = request.pip_code_list
        if not DaraCore.is_null(request.real_end_month):
            query['RealEndMonth'] = request.real_end_month
        if not DaraCore.is_null(request.real_start_month):
            query['RealStartMonth'] = request.real_start_month
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCommissionableProducts',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCommissionableProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_commissionable_products_with_options_async(
        self,
        tmp_req: main_models.GetCommissionableProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCommissionableProductsResponse:
        tmp_req.validate()
        request = main_models.GetCommissionableProductsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.list_show_status_list):
            request.list_show_status_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.list_show_status_list, 'ListShowStatusList', 'simple')
        query = {}
        if not DaraCore.is_null(request.commodity_code_list):
            query['CommodityCodeList'] = request.commodity_code_list
        if not DaraCore.is_null(request.fiscal_year):
            query['FiscalYear'] = request.fiscal_year
        if not DaraCore.is_null(request.list_show_status_list_shrink):
            query['ListShowStatusList'] = request.list_show_status_list_shrink
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pip_code_list):
            query['PipCodeList'] = request.pip_code_list
        if not DaraCore.is_null(request.real_end_month):
            query['RealEndMonth'] = request.real_end_month
        if not DaraCore.is_null(request.real_start_month):
            query['RealStartMonth'] = request.real_start_month
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCommissionableProducts',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCommissionableProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_commissionable_products(
        self,
        request: main_models.GetCommissionableProductsRequest,
    ) -> main_models.GetCommissionableProductsResponse:
        runtime = RuntimeOptions()
        return self.get_commissionable_products_with_options(request, runtime)

    async def get_commissionable_products_async(
        self,
        request: main_models.GetCommissionableProductsRequest,
    ) -> main_models.GetCommissionableProductsResponse:
        runtime = RuntimeOptions()
        return await self.get_commissionable_products_with_options_async(request, runtime)

    def get_coupon_template_detail_with_options(
        self,
        request: main_models.GetCouponTemplateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCouponTemplateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCouponTemplateDetail',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCouponTemplateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_coupon_template_detail_with_options_async(
        self,
        request: main_models.GetCouponTemplateDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCouponTemplateDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCouponTemplateDetail',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCouponTemplateDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_coupon_template_detail(
        self,
        request: main_models.GetCouponTemplateDetailRequest,
    ) -> main_models.GetCouponTemplateDetailResponse:
        runtime = RuntimeOptions()
        return self.get_coupon_template_detail_with_options(request, runtime)

    async def get_coupon_template_detail_async(
        self,
        request: main_models.GetCouponTemplateDetailRequest,
    ) -> main_models.GetCouponTemplateDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_coupon_template_detail_with_options_async(request, runtime)

    def get_coupondeduct_product_code_with_options(
        self,
        request: main_models.GetCoupondeductProductCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCoupondeductProductCodeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCoupondeductProductCode',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCoupondeductProductCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_coupondeduct_product_code_with_options_async(
        self,
        request: main_models.GetCoupondeductProductCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCoupondeductProductCodeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCoupondeductProductCode',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCoupondeductProductCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_coupondeduct_product_code(
        self,
        request: main_models.GetCoupondeductProductCodeRequest,
    ) -> main_models.GetCoupondeductProductCodeResponse:
        runtime = RuntimeOptions()
        return self.get_coupondeduct_product_code_with_options(request, runtime)

    async def get_coupondeduct_product_code_async(
        self,
        request: main_models.GetCoupondeductProductCodeRequest,
    ) -> main_models.GetCoupondeductProductCodeResponse:
        runtime = RuntimeOptions()
        return await self.get_coupondeduct_product_code_with_options_async(request, runtime)

    def get_credit_info_with_options(
        self,
        request: main_models.GetCreditInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCreditInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCreditInfo',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCreditInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_credit_info_with_options_async(
        self,
        request: main_models.GetCreditInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCreditInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCreditInfo',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCreditInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_credit_info(
        self,
        request: main_models.GetCreditInfoRequest,
    ) -> main_models.GetCreditInfoResponse:
        runtime = RuntimeOptions()
        return self.get_credit_info_with_options(request, runtime)

    async def get_credit_info_async(
        self,
        request: main_models.GetCreditInfoRequest,
    ) -> main_models.GetCreditInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_credit_info_with_options_async(request, runtime)

    def get_customer_orders_with_options(
        self,
        request: main_models.GetCustomerOrdersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerOrdersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerOrders',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customer_orders_with_options_async(
        self,
        request: main_models.GetCustomerOrdersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerOrdersResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerOrders',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customer_orders(
        self,
        request: main_models.GetCustomerOrdersRequest,
    ) -> main_models.GetCustomerOrdersResponse:
        runtime = RuntimeOptions()
        return self.get_customer_orders_with_options(request, runtime)

    async def get_customer_orders_async(
        self,
        request: main_models.GetCustomerOrdersRequest,
    ) -> main_models.GetCustomerOrdersResponse:
        runtime = RuntimeOptions()
        return await self.get_customer_orders_with_options_async(request, runtime)

    def get_daily_bill_with_options(
        self,
        request: main_models.GetDailyBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDailyBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner):
            query['BillOwner'] = request.bill_owner
        if not DaraCore.is_null(request.bill_type):
            query['BillType'] = request.bill_type
        if not DaraCore.is_null(request.date):
            query['Date'] = request.date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDailyBill',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDailyBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_daily_bill_with_options_async(
        self,
        request: main_models.GetDailyBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDailyBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner):
            query['BillOwner'] = request.bill_owner
        if not DaraCore.is_null(request.bill_type):
            query['BillType'] = request.bill_type
        if not DaraCore.is_null(request.date):
            query['Date'] = request.date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDailyBill',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDailyBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_daily_bill(
        self,
        request: main_models.GetDailyBillRequest,
    ) -> main_models.GetDailyBillResponse:
        runtime = RuntimeOptions()
        return self.get_daily_bill_with_options(request, runtime)

    async def get_daily_bill_async(
        self,
        request: main_models.GetDailyBillRequest,
    ) -> main_models.GetDailyBillResponse:
        runtime = RuntimeOptions()
        return await self.get_daily_bill_with_options_async(request, runtime)

    def get_invite_status_with_options(
        self,
        request: main_models.GetInviteStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInviteStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.invite_status_list):
            query['InviteStatusList'] = request.invite_status_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInviteStatus',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInviteStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_invite_status_with_options_async(
        self,
        request: main_models.GetInviteStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInviteStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.invite_status_list):
            query['InviteStatusList'] = request.invite_status_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInviteStatus',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInviteStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_invite_status(
        self,
        request: main_models.GetInviteStatusRequest,
    ) -> main_models.GetInviteStatusResponse:
        runtime = RuntimeOptions()
        return self.get_invite_status_with_options(request, runtime)

    async def get_invite_status_async(
        self,
        request: main_models.GetInviteStatusRequest,
    ) -> main_models.GetInviteStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_invite_status_with_options_async(request, runtime)

    def get_monthly_bill_with_options(
        self,
        request: main_models.GetMonthlyBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMonthlyBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner):
            query['BillOwner'] = request.bill_owner
        if not DaraCore.is_null(request.bill_type):
            query['BillType'] = request.bill_type
        if not DaraCore.is_null(request.month):
            query['Month'] = request.month
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMonthlyBill',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonthlyBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_monthly_bill_with_options_async(
        self,
        request: main_models.GetMonthlyBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMonthlyBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_owner):
            query['BillOwner'] = request.bill_owner
        if not DaraCore.is_null(request.bill_type):
            query['BillType'] = request.bill_type
        if not DaraCore.is_null(request.month):
            query['Month'] = request.month
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMonthlyBill',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonthlyBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_monthly_bill(
        self,
        request: main_models.GetMonthlyBillRequest,
    ) -> main_models.GetMonthlyBillResponse:
        runtime = RuntimeOptions()
        return self.get_monthly_bill_with_options(request, runtime)

    async def get_monthly_bill_async(
        self,
        request: main_models.GetMonthlyBillRequest,
    ) -> main_models.GetMonthlyBillResponse:
        runtime = RuntimeOptions()
        return await self.get_monthly_bill_with_options_async(request, runtime)

    def get_purchase_control_record_with_options(
        self,
        request: main_models.GetPurchaseControlRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPurchaseControlRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_uid):
            query['CustomerUID'] = request.customer_uid
        if not DaraCore.is_null(request.operation_time):
            query['OperationTime'] = request.operation_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPurchaseControlRecord',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPurchaseControlRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_purchase_control_record_with_options_async(
        self,
        request: main_models.GetPurchaseControlRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPurchaseControlRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_uid):
            query['CustomerUID'] = request.customer_uid
        if not DaraCore.is_null(request.operation_time):
            query['OperationTime'] = request.operation_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPurchaseControlRecord',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPurchaseControlRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_purchase_control_record(
        self,
        request: main_models.GetPurchaseControlRecordRequest,
    ) -> main_models.GetPurchaseControlRecordResponse:
        runtime = RuntimeOptions()
        return self.get_purchase_control_record_with_options(request, runtime)

    async def get_purchase_control_record_async(
        self,
        request: main_models.GetPurchaseControlRecordRequest,
    ) -> main_models.GetPurchaseControlRecordResponse:
        runtime = RuntimeOptions()
        return await self.get_purchase_control_record_with_options_async(request, runtime)

    def get_shutdown_policy_record_with_options(
        self,
        request: main_models.GetShutdownPolicyRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetShutdownPolicyRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_uid):
            query['CustomerUID'] = request.customer_uid
        if not DaraCore.is_null(request.operation_time):
            query['OperationTime'] = request.operation_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetShutdownPolicyRecord',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetShutdownPolicyRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_shutdown_policy_record_with_options_async(
        self,
        request: main_models.GetShutdownPolicyRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetShutdownPolicyRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.customer_uid):
            query['CustomerUID'] = request.customer_uid
        if not DaraCore.is_null(request.operation_time):
            query['OperationTime'] = request.operation_time
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetShutdownPolicyRecord',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetShutdownPolicyRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_shutdown_policy_record(
        self,
        request: main_models.GetShutdownPolicyRecordRequest,
    ) -> main_models.GetShutdownPolicyRecordResponse:
        runtime = RuntimeOptions()
        return self.get_shutdown_policy_record_with_options(request, runtime)

    async def get_shutdown_policy_record_async(
        self,
        request: main_models.GetShutdownPolicyRecordRequest,
    ) -> main_models.GetShutdownPolicyRecordResponse:
        runtime = RuntimeOptions()
        return await self.get_shutdown_policy_record_with_options_async(request, runtime)

    def get_unassociated_customer_with_options(
        self,
        request: main_models.GetUnassociatedCustomerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUnassociatedCustomerResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUnassociatedCustomer',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUnassociatedCustomerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_unassociated_customer_with_options_async(
        self,
        request: main_models.GetUnassociatedCustomerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUnassociatedCustomerResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUnassociatedCustomer',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUnassociatedCustomerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_unassociated_customer(
        self,
        request: main_models.GetUnassociatedCustomerRequest,
    ) -> main_models.GetUnassociatedCustomerResponse:
        runtime = RuntimeOptions()
        return self.get_unassociated_customer_with_options(request, runtime)

    async def get_unassociated_customer_async(
        self,
        request: main_models.GetUnassociatedCustomerRequest,
    ) -> main_models.GetUnassociatedCustomerResponse:
        runtime = RuntimeOptions()
        return await self.get_unassociated_customer_with_options_async(request, runtime)

    def invite_sub_account_with_options(
        self,
        request: main_models.InviteSubAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InviteSubAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_info_list):
            query['AccountInfoList'] = request.account_info_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InviteSubAccount',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InviteSubAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def invite_sub_account_with_options_async(
        self,
        request: main_models.InviteSubAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InviteSubAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_info_list):
            query['AccountInfoList'] = request.account_info_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InviteSubAccount',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InviteSubAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invite_sub_account(
        self,
        request: main_models.InviteSubAccountRequest,
    ) -> main_models.InviteSubAccountResponse:
        runtime = RuntimeOptions()
        return self.invite_sub_account_with_options(request, runtime)

    async def invite_sub_account_async(
        self,
        request: main_models.InviteSubAccountRequest,
    ) -> main_models.InviteSubAccountResponse:
        runtime = RuntimeOptions()
        return await self.invite_sub_account_with_options_async(request, runtime)

    def issue_coupon_for_customer_with_options(
        self,
        request: main_models.IssueCouponForCustomerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IssueCouponForCustomerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.application_reason):
            query['ApplicationReason'] = request.application_reason
        if not DaraCore.is_null(request.coupon_template_id):
            query['CouponTemplateId'] = request.coupon_template_id
        if not DaraCore.is_null(request.is_use_benefit):
            query['IsUseBenefit'] = request.is_use_benefit
        if not DaraCore.is_null(request.uidlist):
            query['Uidlist'] = request.uidlist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IssueCouponForCustomer',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IssueCouponForCustomerResponse(),
            self.call_api(params, req, runtime)
        )

    async def issue_coupon_for_customer_with_options_async(
        self,
        request: main_models.IssueCouponForCustomerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IssueCouponForCustomerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.application_reason):
            query['ApplicationReason'] = request.application_reason
        if not DaraCore.is_null(request.coupon_template_id):
            query['CouponTemplateId'] = request.coupon_template_id
        if not DaraCore.is_null(request.is_use_benefit):
            query['IsUseBenefit'] = request.is_use_benefit
        if not DaraCore.is_null(request.uidlist):
            query['Uidlist'] = request.uidlist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IssueCouponForCustomer',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IssueCouponForCustomerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def issue_coupon_for_customer(
        self,
        request: main_models.IssueCouponForCustomerRequest,
    ) -> main_models.IssueCouponForCustomerResponse:
        runtime = RuntimeOptions()
        return self.issue_coupon_for_customer_with_options(request, runtime)

    async def issue_coupon_for_customer_async(
        self,
        request: main_models.IssueCouponForCustomerRequest,
    ) -> main_models.IssueCouponForCustomerResponse:
        runtime = RuntimeOptions()
        return await self.issue_coupon_for_customer_with_options_async(request, runtime)

    def list_countries_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListCountriesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListCountries',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCountriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_countries_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListCountriesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListCountries',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCountriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_countries(self) -> main_models.ListCountriesResponse:
        runtime = RuntimeOptions()
        return self.list_countries_with_options(runtime)

    async def list_countries_async(self) -> main_models.ListCountriesResponse:
        runtime = RuntimeOptions()
        return await self.list_countries_with_options_async(runtime)

    def list_coupon_usage_with_options(
        self,
        request: main_models.ListCouponUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCouponUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.coupon_template_id):
            query['CouponTemplateId'] = request.coupon_template_id
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.t_2partner_uid):
            query['T2PartnerUid'] = request.t_2partner_uid
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCouponUsage',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCouponUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_coupon_usage_with_options_async(
        self,
        request: main_models.ListCouponUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCouponUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account):
            query['Account'] = request.account
        if not DaraCore.is_null(request.coupon_template_id):
            query['CouponTemplateId'] = request.coupon_template_id
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.t_2partner_uid):
            query['T2PartnerUid'] = request.t_2partner_uid
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCouponUsage',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCouponUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_coupon_usage(
        self,
        request: main_models.ListCouponUsageRequest,
    ) -> main_models.ListCouponUsageResponse:
        runtime = RuntimeOptions()
        return self.list_coupon_usage_with_options(request, runtime)

    async def list_coupon_usage_async(
        self,
        request: main_models.ListCouponUsageRequest,
    ) -> main_models.ListCouponUsageResponse:
        runtime = RuntimeOptions()
        return await self.list_coupon_usage_with_options_async(request, runtime)

    def list_export_tasks_with_options(
        self,
        request: main_models.ListExportTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExportTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExportTasks',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExportTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_export_tasks_with_options_async(
        self,
        request: main_models.ListExportTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExportTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_code):
            query['SceneCode'] = request.scene_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExportTasks',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExportTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_export_tasks(
        self,
        request: main_models.ListExportTasksRequest,
    ) -> main_models.ListExportTasksResponse:
        runtime = RuntimeOptions()
        return self.list_export_tasks_with_options(request, runtime)

    async def list_export_tasks_async(
        self,
        request: main_models.ListExportTasksRequest,
    ) -> main_models.ListExportTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_export_tasks_with_options_async(request, runtime)

    def query_reversed_deduction_history_with_options(
        self,
        request: main_models.QueryReversedDeductionHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReversedDeductionHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReversedDeductionHistory',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReversedDeductionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_reversed_deduction_history_with_options_async(
        self,
        request: main_models.QueryReversedDeductionHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReversedDeductionHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReversedDeductionHistory',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReversedDeductionHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_reversed_deduction_history(
        self,
        request: main_models.QueryReversedDeductionHistoryRequest,
    ) -> main_models.QueryReversedDeductionHistoryResponse:
        runtime = RuntimeOptions()
        return self.query_reversed_deduction_history_with_options(request, runtime)

    async def query_reversed_deduction_history_async(
        self,
        request: main_models.QueryReversedDeductionHistoryRequest,
    ) -> main_models.QueryReversedDeductionHistoryResponse:
        runtime = RuntimeOptions()
        return await self.query_reversed_deduction_history_with_options_async(request, runtime)

    def quota_list_export_paged_with_options(
        self,
        request: main_models.QuotaListExportPagedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuotaListExportPagedResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuotaListExportPaged',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuotaListExportPagedResponse(),
            self.call_api(params, req, runtime)
        )

    async def quota_list_export_paged_with_options_async(
        self,
        request: main_models.QuotaListExportPagedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuotaListExportPagedResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuotaListExportPaged',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuotaListExportPagedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def quota_list_export_paged(
        self,
        request: main_models.QuotaListExportPagedRequest,
    ) -> main_models.QuotaListExportPagedResponse:
        runtime = RuntimeOptions()
        return self.quota_list_export_paged_with_options(request, runtime)

    async def quota_list_export_paged_async(
        self,
        request: main_models.QuotaListExportPagedRequest,
    ) -> main_models.QuotaListExportPagedResponse:
        runtime = RuntimeOptions()
        return await self.quota_list_export_paged_with_options_async(request, runtime)

    def resend_email_with_options(
        self,
        request: main_models.ResendEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResendEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.invite_id):
            query['InviteId'] = request.invite_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResendEmail',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResendEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def resend_email_with_options_async(
        self,
        request: main_models.ResendEmailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResendEmailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.invite_id):
            query['InviteId'] = request.invite_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResendEmail',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResendEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resend_email(
        self,
        request: main_models.ResendEmailRequest,
    ) -> main_models.ResendEmailResponse:
        runtime = RuntimeOptions()
        return self.resend_email_with_options(request, runtime)

    async def resend_email_async(
        self,
        request: main_models.ResendEmailRequest,
    ) -> main_models.ResendEmailResponse:
        runtime = RuntimeOptions()
        return await self.resend_email_with_options_async(request, runtime)

    def set_account_info_with_options(
        self,
        request: main_models.SetAccountInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAccountInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_nickname):
            query['AccountNickname'] = request.account_nickname
        if not DaraCore.is_null(request.customer_bd):
            query['CustomerBd'] = request.customer_bd
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAccountInfo',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_account_info_with_options_async(
        self,
        request: main_models.SetAccountInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetAccountInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_nickname):
            query['AccountNickname'] = request.account_nickname
        if not DaraCore.is_null(request.customer_bd):
            query['CustomerBd'] = request.customer_bd
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetAccountInfo',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_account_info(
        self,
        request: main_models.SetAccountInfoRequest,
    ) -> main_models.SetAccountInfoResponse:
        runtime = RuntimeOptions()
        return self.set_account_info_with_options(request, runtime)

    async def set_account_info_async(
        self,
        request: main_models.SetAccountInfoRequest,
    ) -> main_models.SetAccountInfoResponse:
        runtime = RuntimeOptions()
        return await self.set_account_info_with_options_async(request, runtime)

    def set_credit_line_with_options(
        self,
        request: main_models.SetCreditLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCreditLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credit_line):
            query['CreditLine'] = request.credit_line
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetCreditLine',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCreditLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_credit_line_with_options_async(
        self,
        request: main_models.SetCreditLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetCreditLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.credit_line):
            query['CreditLine'] = request.credit_line
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetCreditLine',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetCreditLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_credit_line(
        self,
        request: main_models.SetCreditLineRequest,
    ) -> main_models.SetCreditLineResponse:
        runtime = RuntimeOptions()
        return self.set_credit_line_with_options(request, runtime)

    async def set_credit_line_async(
        self,
        request: main_models.SetCreditLineRequest,
    ) -> main_models.SetCreditLineResponse:
        runtime = RuntimeOptions()
        return await self.set_credit_line_with_options_async(request, runtime)

    def set_warning_threshold_with_options(
        self,
        request: main_models.SetWarningThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetWarningThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        if not DaraCore.is_null(request.warning_value):
            query['WarningValue'] = request.warning_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetWarningThreshold',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetWarningThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_warning_threshold_with_options_async(
        self,
        request: main_models.SetWarningThresholdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetWarningThresholdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.uid):
            query['Uid'] = request.uid
        if not DaraCore.is_null(request.warning_value):
            query['WarningValue'] = request.warning_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetWarningThreshold',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetWarningThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_warning_threshold(
        self,
        request: main_models.SetWarningThresholdRequest,
    ) -> main_models.SetWarningThresholdResponse:
        runtime = RuntimeOptions()
        return self.set_warning_threshold_with_options(request, runtime)

    async def set_warning_threshold_async(
        self,
        request: main_models.SetWarningThresholdRequest,
    ) -> main_models.SetWarningThresholdResponse:
        runtime = RuntimeOptions()
        return await self.set_warning_threshold_with_options_async(request, runtime)

    def subscription_bill_with_options(
        self,
        request: main_models.SubscriptionBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubscriptionBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not DaraCore.is_null(request.bill_format):
            query['BillFormat'] = request.bill_format
        if not DaraCore.is_null(request.bucket_owner_id):
            query['BucketOwnerId'] = request.bucket_owner_id
        if not DaraCore.is_null(request.subscribe_bucket):
            query['SubscribeBucket'] = request.subscribe_bucket
        if not DaraCore.is_null(request.subscribe_segment_size):
            query['SubscribeSegmentSize'] = request.subscribe_segment_size
        if not DaraCore.is_null(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubscriptionBill',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubscriptionBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def subscription_bill_with_options_async(
        self,
        request: main_models.SubscriptionBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubscriptionBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not DaraCore.is_null(request.bill_format):
            query['BillFormat'] = request.bill_format
        if not DaraCore.is_null(request.bucket_owner_id):
            query['BucketOwnerId'] = request.bucket_owner_id
        if not DaraCore.is_null(request.subscribe_bucket):
            query['SubscribeBucket'] = request.subscribe_bucket
        if not DaraCore.is_null(request.subscribe_segment_size):
            query['SubscribeSegmentSize'] = request.subscribe_segment_size
        if not DaraCore.is_null(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubscriptionBill',
            version = '2022-12-16',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubscriptionBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def subscription_bill(
        self,
        request: main_models.SubscriptionBillRequest,
    ) -> main_models.SubscriptionBillResponse:
        runtime = RuntimeOptions()
        return self.subscription_bill_with_options(request, runtime)

    async def subscription_bill_async(
        self,
        request: main_models.SubscriptionBillRequest,
    ) -> main_models.SubscriptionBillResponse:
        runtime = RuntimeOptions()
        return await self.subscription_bill_with_options_async(request, runtime)
