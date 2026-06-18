# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agency20250227 import models as main_models
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
            'us-west-1': 'agency.aliyuncs.com',
            'ap-southeast-1': 'agency.ap-southeast-1.aliyuncs.com'
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

    def get_bill_detail_file_list_with_options(
        self,
        request: main_models.GetBillDetailFileListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBillDetailFileListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_month):
            query['BillMonth'] = request.bill_month
        if not DaraCore.is_null(request.oss_access_key_id):
            query['OssAccessKeyId'] = request.oss_access_key_id
        if not DaraCore.is_null(request.oss_access_key_secret):
            query['OssAccessKeySecret'] = request.oss_access_key_secret
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_region):
            query['OssRegion'] = request.oss_region
        if not DaraCore.is_null(request.oss_security_token):
            query['OssSecurityToken'] = request.oss_security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBillDetailFileList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBillDetailFileListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_bill_detail_file_list_with_options_async(
        self,
        request: main_models.GetBillDetailFileListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBillDetailFileListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_month):
            query['BillMonth'] = request.bill_month
        if not DaraCore.is_null(request.oss_access_key_id):
            query['OssAccessKeyId'] = request.oss_access_key_id
        if not DaraCore.is_null(request.oss_access_key_secret):
            query['OssAccessKeySecret'] = request.oss_access_key_secret
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_region):
            query['OssRegion'] = request.oss_region
        if not DaraCore.is_null(request.oss_security_token):
            query['OssSecurityToken'] = request.oss_security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBillDetailFileList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBillDetailFileListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_bill_detail_file_list(
        self,
        request: main_models.GetBillDetailFileListRequest,
    ) -> main_models.GetBillDetailFileListResponse:
        runtime = RuntimeOptions()
        return self.get_bill_detail_file_list_with_options(request, runtime)

    async def get_bill_detail_file_list_async(
        self,
        request: main_models.GetBillDetailFileListRequest,
    ) -> main_models.GetBillDetailFileListResponse:
        runtime = RuntimeOptions()
        return await self.get_bill_detail_file_list_with_options_async(request, runtime)

    def get_commission_detail_file_list_with_options(
        self,
        request: main_models.GetCommissionDetailFileListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCommissionDetailFileListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_month):
            query['BillMonth'] = request.bill_month
        if not DaraCore.is_null(request.oss_access_key_id):
            query['OssAccessKeyId'] = request.oss_access_key_id
        if not DaraCore.is_null(request.oss_access_key_secret):
            query['OssAccessKeySecret'] = request.oss_access_key_secret
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_region):
            query['OssRegion'] = request.oss_region
        if not DaraCore.is_null(request.oss_security_token):
            query['OssSecurityToken'] = request.oss_security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCommissionDetailFileList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCommissionDetailFileListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_commission_detail_file_list_with_options_async(
        self,
        request: main_models.GetCommissionDetailFileListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCommissionDetailFileListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_month):
            query['BillMonth'] = request.bill_month
        if not DaraCore.is_null(request.oss_access_key_id):
            query['OssAccessKeyId'] = request.oss_access_key_id
        if not DaraCore.is_null(request.oss_access_key_secret):
            query['OssAccessKeySecret'] = request.oss_access_key_secret
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_region):
            query['OssRegion'] = request.oss_region
        if not DaraCore.is_null(request.oss_security_token):
            query['OssSecurityToken'] = request.oss_security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCommissionDetailFileList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCommissionDetailFileListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_commission_detail_file_list(
        self,
        request: main_models.GetCommissionDetailFileListRequest,
    ) -> main_models.GetCommissionDetailFileListResponse:
        runtime = RuntimeOptions()
        return self.get_commission_detail_file_list_with_options(request, runtime)

    async def get_commission_detail_file_list_async(
        self,
        request: main_models.GetCommissionDetailFileListRequest,
    ) -> main_models.GetCommissionDetailFileListResponse:
        runtime = RuntimeOptions()
        return await self.get_commission_detail_file_list_with_options_async(request, runtime)

    def get_customer_order_list_with_options(
        self,
        tmp_req: main_models.GetCustomerOrderListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerOrderListResponse:
        tmp_req.validate()
        request = main_models.GetCustomerOrderListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.order_type_list):
            request.order_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.order_type_list, 'OrderTypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.customer_account):
            query['CustomerAccount'] = request.customer_account
        if not DaraCore.is_null(request.customer_uid):
            query['CustomerUid'] = request.customer_uid
        if not DaraCore.is_null(request.order_create_after):
            query['OrderCreateAfter'] = request.order_create_after
        if not DaraCore.is_null(request.order_create_before):
            query['OrderCreateBefore'] = request.order_create_before
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.order_pay_after):
            query['OrderPayAfter'] = request.order_pay_after
        if not DaraCore.is_null(request.order_pay_before):
            query['OrderPayBefore'] = request.order_pay_before
        if not DaraCore.is_null(request.order_status):
            query['OrderStatus'] = request.order_status
        if not DaraCore.is_null(request.order_type_list_shrink):
            query['OrderTypeList'] = request.order_type_list_shrink
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pay_amount_after):
            query['PayAmountAfter'] = request.pay_amount_after
        if not DaraCore.is_null(request.pay_amount_before):
            query['PayAmountBefore'] = request.pay_amount_before
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.ram_account_for_customer_manager):
            query['RamAccountForCustomerManager'] = request.ram_account_for_customer_manager
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerOrderList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerOrderListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customer_order_list_with_options_async(
        self,
        tmp_req: main_models.GetCustomerOrderListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomerOrderListResponse:
        tmp_req.validate()
        request = main_models.GetCustomerOrderListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.order_type_list):
            request.order_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.order_type_list, 'OrderTypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.customer_account):
            query['CustomerAccount'] = request.customer_account
        if not DaraCore.is_null(request.customer_uid):
            query['CustomerUid'] = request.customer_uid
        if not DaraCore.is_null(request.order_create_after):
            query['OrderCreateAfter'] = request.order_create_after
        if not DaraCore.is_null(request.order_create_before):
            query['OrderCreateBefore'] = request.order_create_before
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.order_pay_after):
            query['OrderPayAfter'] = request.order_pay_after
        if not DaraCore.is_null(request.order_pay_before):
            query['OrderPayBefore'] = request.order_pay_before
        if not DaraCore.is_null(request.order_status):
            query['OrderStatus'] = request.order_status
        if not DaraCore.is_null(request.order_type_list_shrink):
            query['OrderTypeList'] = request.order_type_list_shrink
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pay_amount_after):
            query['PayAmountAfter'] = request.pay_amount_after
        if not DaraCore.is_null(request.pay_amount_before):
            query['PayAmountBefore'] = request.pay_amount_before
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.ram_account_for_customer_manager):
            query['RamAccountForCustomerManager'] = request.ram_account_for_customer_manager
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomerOrderList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomerOrderListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customer_order_list(
        self,
        request: main_models.GetCustomerOrderListRequest,
    ) -> main_models.GetCustomerOrderListResponse:
        runtime = RuntimeOptions()
        return self.get_customer_order_list_with_options(request, runtime)

    async def get_customer_order_list_async(
        self,
        request: main_models.GetCustomerOrderListRequest,
    ) -> main_models.GetCustomerOrderListResponse:
        runtime = RuntimeOptions()
        return await self.get_customer_order_list_with_options_async(request, runtime)

    def get_intl_commission_detail_file_list_with_options(
        self,
        request: main_models.GetIntlCommissionDetailFileListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIntlCommissionDetailFileListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_month):
            query['BillMonth'] = request.bill_month
        if not DaraCore.is_null(request.oss_access_key_id):
            query['OssAccessKeyId'] = request.oss_access_key_id
        if not DaraCore.is_null(request.oss_access_key_secret):
            query['OssAccessKeySecret'] = request.oss_access_key_secret
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_region):
            query['OssRegion'] = request.oss_region
        if not DaraCore.is_null(request.oss_security_token):
            query['OssSecurityToken'] = request.oss_security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIntlCommissionDetailFileList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntlCommissionDetailFileListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_intl_commission_detail_file_list_with_options_async(
        self,
        request: main_models.GetIntlCommissionDetailFileListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIntlCommissionDetailFileListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bill_month):
            query['BillMonth'] = request.bill_month
        if not DaraCore.is_null(request.oss_access_key_id):
            query['OssAccessKeyId'] = request.oss_access_key_id
        if not DaraCore.is_null(request.oss_access_key_secret):
            query['OssAccessKeySecret'] = request.oss_access_key_secret
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not DaraCore.is_null(request.oss_region):
            query['OssRegion'] = request.oss_region
        if not DaraCore.is_null(request.oss_security_token):
            query['OssSecurityToken'] = request.oss_security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIntlCommissionDetailFileList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntlCommissionDetailFileListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_intl_commission_detail_file_list(
        self,
        request: main_models.GetIntlCommissionDetailFileListRequest,
    ) -> main_models.GetIntlCommissionDetailFileListResponse:
        runtime = RuntimeOptions()
        return self.get_intl_commission_detail_file_list_with_options(request, runtime)

    async def get_intl_commission_detail_file_list_async(
        self,
        request: main_models.GetIntlCommissionDetailFileListRequest,
    ) -> main_models.GetIntlCommissionDetailFileListResponse:
        runtime = RuntimeOptions()
        return await self.get_intl_commission_detail_file_list_with_options_async(request, runtime)

    def get_renewal_rate_list_with_options(
        self,
        request: main_models.GetRenewalRateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRenewalRateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fiscal_year_and_quarter):
            query['FiscalYearAndQuarter'] = request.fiscal_year_and_quarter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRenewalRateList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRenewalRateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_renewal_rate_list_with_options_async(
        self,
        request: main_models.GetRenewalRateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRenewalRateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fiscal_year_and_quarter):
            query['FiscalYearAndQuarter'] = request.fiscal_year_and_quarter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRenewalRateList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRenewalRateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_renewal_rate_list(
        self,
        request: main_models.GetRenewalRateListRequest,
    ) -> main_models.GetRenewalRateListResponse:
        runtime = RuntimeOptions()
        return self.get_renewal_rate_list_with_options(request, runtime)

    async def get_renewal_rate_list_async(
        self,
        request: main_models.GetRenewalRateListRequest,
    ) -> main_models.GetRenewalRateListResponse:
        runtime = RuntimeOptions()
        return await self.get_renewal_rate_list_with_options_async(request, runtime)

    def get_sub_partner_list_with_options(
        self,
        request: main_models.GetSubPartnerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubPartnerListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sub_partner_company_name):
            query['SubPartnerCompanyName'] = request.sub_partner_company_name
        if not DaraCore.is_null(request.sub_partner_pid):
            query['SubPartnerPid'] = request.sub_partner_pid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubPartnerList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubPartnerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sub_partner_list_with_options_async(
        self,
        request: main_models.GetSubPartnerListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubPartnerListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sub_partner_company_name):
            query['SubPartnerCompanyName'] = request.sub_partner_company_name
        if not DaraCore.is_null(request.sub_partner_pid):
            query['SubPartnerPid'] = request.sub_partner_pid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubPartnerList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubPartnerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sub_partner_list(
        self,
        request: main_models.GetSubPartnerListRequest,
    ) -> main_models.GetSubPartnerListResponse:
        runtime = RuntimeOptions()
        return self.get_sub_partner_list_with_options(request, runtime)

    async def get_sub_partner_list_async(
        self,
        request: main_models.GetSubPartnerListRequest,
    ) -> main_models.GetSubPartnerListResponse:
        runtime = RuntimeOptions()
        return await self.get_sub_partner_list_with_options_async(request, runtime)

    def get_sub_partner_order_list_with_options(
        self,
        tmp_req: main_models.GetSubPartnerOrderListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubPartnerOrderListResponse:
        tmp_req.validate()
        request = main_models.GetSubPartnerOrderListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.order_type_list):
            request.order_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.order_type_list, 'OrderTypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.order_create_after):
            query['OrderCreateAfter'] = request.order_create_after
        if not DaraCore.is_null(request.order_create_before):
            query['OrderCreateBefore'] = request.order_create_before
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.order_pay_after):
            query['OrderPayAfter'] = request.order_pay_after
        if not DaraCore.is_null(request.order_pay_before):
            query['OrderPayBefore'] = request.order_pay_before
        if not DaraCore.is_null(request.order_status):
            query['OrderStatus'] = request.order_status
        if not DaraCore.is_null(request.order_type_list_shrink):
            query['OrderTypeList'] = request.order_type_list_shrink
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pay_amount_after):
            query['PayAmountAfter'] = request.pay_amount_after
        if not DaraCore.is_null(request.pay_amount_before):
            query['PayAmountBefore'] = request.pay_amount_before
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sub_partner_name):
            query['SubPartnerName'] = request.sub_partner_name
        if not DaraCore.is_null(request.sub_partner_uid):
            query['SubPartnerUid'] = request.sub_partner_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubPartnerOrderList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubPartnerOrderListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sub_partner_order_list_with_options_async(
        self,
        tmp_req: main_models.GetSubPartnerOrderListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSubPartnerOrderListResponse:
        tmp_req.validate()
        request = main_models.GetSubPartnerOrderListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.order_type_list):
            request.order_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.order_type_list, 'OrderTypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.order_create_after):
            query['OrderCreateAfter'] = request.order_create_after
        if not DaraCore.is_null(request.order_create_before):
            query['OrderCreateBefore'] = request.order_create_before
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.order_pay_after):
            query['OrderPayAfter'] = request.order_pay_after
        if not DaraCore.is_null(request.order_pay_before):
            query['OrderPayBefore'] = request.order_pay_before
        if not DaraCore.is_null(request.order_status):
            query['OrderStatus'] = request.order_status
        if not DaraCore.is_null(request.order_type_list_shrink):
            query['OrderTypeList'] = request.order_type_list_shrink
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pay_amount_after):
            query['PayAmountAfter'] = request.pay_amount_after
        if not DaraCore.is_null(request.pay_amount_before):
            query['PayAmountBefore'] = request.pay_amount_before
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.product_name):
            query['ProductName'] = request.product_name
        if not DaraCore.is_null(request.project_id):
            query['ProjectId'] = request.project_id
        if not DaraCore.is_null(request.sub_partner_name):
            query['SubPartnerName'] = request.sub_partner_name
        if not DaraCore.is_null(request.sub_partner_uid):
            query['SubPartnerUid'] = request.sub_partner_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSubPartnerOrderList',
            version = '2025-02-27',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSubPartnerOrderListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sub_partner_order_list(
        self,
        request: main_models.GetSubPartnerOrderListRequest,
    ) -> main_models.GetSubPartnerOrderListResponse:
        runtime = RuntimeOptions()
        return self.get_sub_partner_order_list_with_options(request, runtime)

    async def get_sub_partner_order_list_async(
        self,
        request: main_models.GetSubPartnerOrderListRequest,
    ) -> main_models.GetSubPartnerOrderListResponse:
        runtime = RuntimeOptions()
        return await self.get_sub_partner_order_list_with_options_async(request, runtime)
