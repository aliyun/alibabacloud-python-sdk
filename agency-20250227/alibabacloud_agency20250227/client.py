# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_agency20250227 import models as agency_20250227_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_bill_detail_file_list_with_options(
        self,
        request: agency_20250227_models.GetBillDetailFileListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20250227_models.GetBillDetailFileListResponse:
        """
        @summary 查询账单导出文件
        
        @param request: GetBillDetailFileListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBillDetailFileListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_month):
            query['BillMonth'] = request.bill_month
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBillDetailFileList',
            version='2025-02-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                agency_20250227_models.GetBillDetailFileListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                agency_20250227_models.GetBillDetailFileListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_bill_detail_file_list_with_options_async(
        self,
        request: agency_20250227_models.GetBillDetailFileListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20250227_models.GetBillDetailFileListResponse:
        """
        @summary 查询账单导出文件
        
        @param request: GetBillDetailFileListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBillDetailFileListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_month):
            query['BillMonth'] = request.bill_month
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBillDetailFileList',
            version='2025-02-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                agency_20250227_models.GetBillDetailFileListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                agency_20250227_models.GetBillDetailFileListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_bill_detail_file_list(
        self,
        request: agency_20250227_models.GetBillDetailFileListRequest,
    ) -> agency_20250227_models.GetBillDetailFileListResponse:
        """
        @summary 查询账单导出文件
        
        @param request: GetBillDetailFileListRequest
        @return: GetBillDetailFileListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_bill_detail_file_list_with_options(request, runtime)

    async def get_bill_detail_file_list_async(
        self,
        request: agency_20250227_models.GetBillDetailFileListRequest,
    ) -> agency_20250227_models.GetBillDetailFileListResponse:
        """
        @summary 查询账单导出文件
        
        @param request: GetBillDetailFileListRequest
        @return: GetBillDetailFileListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_bill_detail_file_list_with_options_async(request, runtime)

    def get_commission_detail_file_list_with_options(
        self,
        request: agency_20250227_models.GetCommissionDetailFileListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20250227_models.GetCommissionDetailFileListResponse:
        """
        @summary 查询伙伴佣金明细
        
        @param request: GetCommissionDetailFileListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCommissionDetailFileListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_month):
            query['BillMonth'] = request.bill_month
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommissionDetailFileList',
            version='2025-02-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                agency_20250227_models.GetCommissionDetailFileListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                agency_20250227_models.GetCommissionDetailFileListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_commission_detail_file_list_with_options_async(
        self,
        request: agency_20250227_models.GetCommissionDetailFileListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20250227_models.GetCommissionDetailFileListResponse:
        """
        @summary 查询伙伴佣金明细
        
        @param request: GetCommissionDetailFileListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCommissionDetailFileListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_month):
            query['BillMonth'] = request.bill_month
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommissionDetailFileList',
            version='2025-02-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                agency_20250227_models.GetCommissionDetailFileListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                agency_20250227_models.GetCommissionDetailFileListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_commission_detail_file_list(
        self,
        request: agency_20250227_models.GetCommissionDetailFileListRequest,
    ) -> agency_20250227_models.GetCommissionDetailFileListResponse:
        """
        @summary 查询伙伴佣金明细
        
        @param request: GetCommissionDetailFileListRequest
        @return: GetCommissionDetailFileListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_commission_detail_file_list_with_options(request, runtime)

    async def get_commission_detail_file_list_async(
        self,
        request: agency_20250227_models.GetCommissionDetailFileListRequest,
    ) -> agency_20250227_models.GetCommissionDetailFileListResponse:
        """
        @summary 查询伙伴佣金明细
        
        @param request: GetCommissionDetailFileListRequest
        @return: GetCommissionDetailFileListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_commission_detail_file_list_with_options_async(request, runtime)

    def get_customer_order_list_with_options(
        self,
        tmp_req: agency_20250227_models.GetCustomerOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20250227_models.GetCustomerOrderListResponse:
        """
        @summary 查询伙伴拓客订单
        
        @param tmp_req: GetCustomerOrderListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomerOrderListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = agency_20250227_models.GetCustomerOrderListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_type_list):
            request.order_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_type_list, 'OrderTypeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.customer_account):
            query['CustomerAccount'] = request.customer_account
        if not UtilClient.is_unset(request.customer_uid):
            query['CustomerUid'] = request.customer_uid
        if not UtilClient.is_unset(request.order_create_after):
            query['OrderCreateAfter'] = request.order_create_after
        if not UtilClient.is_unset(request.order_create_before):
            query['OrderCreateBefore'] = request.order_create_before
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.order_pay_after):
            query['OrderPayAfter'] = request.order_pay_after
        if not UtilClient.is_unset(request.order_pay_before):
            query['OrderPayBefore'] = request.order_pay_before
        if not UtilClient.is_unset(request.order_status):
            query['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.order_type_list_shrink):
            query['OrderTypeList'] = request.order_type_list_shrink
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pay_amount_after):
            query['PayAmountAfter'] = request.pay_amount_after
        if not UtilClient.is_unset(request.pay_amount_before):
            query['PayAmountBefore'] = request.pay_amount_before
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.ram_account_for_customer_manager):
            query['RamAccountForCustomerManager'] = request.ram_account_for_customer_manager
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomerOrderList',
            version='2025-02-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                agency_20250227_models.GetCustomerOrderListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                agency_20250227_models.GetCustomerOrderListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_customer_order_list_with_options_async(
        self,
        tmp_req: agency_20250227_models.GetCustomerOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20250227_models.GetCustomerOrderListResponse:
        """
        @summary 查询伙伴拓客订单
        
        @param tmp_req: GetCustomerOrderListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomerOrderListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = agency_20250227_models.GetCustomerOrderListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_type_list):
            request.order_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_type_list, 'OrderTypeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.customer_account):
            query['CustomerAccount'] = request.customer_account
        if not UtilClient.is_unset(request.customer_uid):
            query['CustomerUid'] = request.customer_uid
        if not UtilClient.is_unset(request.order_create_after):
            query['OrderCreateAfter'] = request.order_create_after
        if not UtilClient.is_unset(request.order_create_before):
            query['OrderCreateBefore'] = request.order_create_before
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.order_pay_after):
            query['OrderPayAfter'] = request.order_pay_after
        if not UtilClient.is_unset(request.order_pay_before):
            query['OrderPayBefore'] = request.order_pay_before
        if not UtilClient.is_unset(request.order_status):
            query['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.order_type_list_shrink):
            query['OrderTypeList'] = request.order_type_list_shrink
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pay_amount_after):
            query['PayAmountAfter'] = request.pay_amount_after
        if not UtilClient.is_unset(request.pay_amount_before):
            query['PayAmountBefore'] = request.pay_amount_before
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.ram_account_for_customer_manager):
            query['RamAccountForCustomerManager'] = request.ram_account_for_customer_manager
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomerOrderList',
            version='2025-02-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                agency_20250227_models.GetCustomerOrderListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                agency_20250227_models.GetCustomerOrderListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_customer_order_list(
        self,
        request: agency_20250227_models.GetCustomerOrderListRequest,
    ) -> agency_20250227_models.GetCustomerOrderListResponse:
        """
        @summary 查询伙伴拓客订单
        
        @param request: GetCustomerOrderListRequest
        @return: GetCustomerOrderListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_customer_order_list_with_options(request, runtime)

    async def get_customer_order_list_async(
        self,
        request: agency_20250227_models.GetCustomerOrderListRequest,
    ) -> agency_20250227_models.GetCustomerOrderListResponse:
        """
        @summary 查询伙伴拓客订单
        
        @param request: GetCustomerOrderListRequest
        @return: GetCustomerOrderListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_customer_order_list_with_options_async(request, runtime)

    def get_renewal_rate_list_with_options(
        self,
        request: agency_20250227_models.GetRenewalRateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20250227_models.GetRenewalRateListResponse:
        """
        @summary 查询伙伴续费率
        
        @param request: GetRenewalRateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRenewalRateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fiscal_year_and_quarter):
            query['FiscalYearAndQuarter'] = request.fiscal_year_and_quarter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRenewalRateList',
            version='2025-02-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                agency_20250227_models.GetRenewalRateListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                agency_20250227_models.GetRenewalRateListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_renewal_rate_list_with_options_async(
        self,
        request: agency_20250227_models.GetRenewalRateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20250227_models.GetRenewalRateListResponse:
        """
        @summary 查询伙伴续费率
        
        @param request: GetRenewalRateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRenewalRateListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fiscal_year_and_quarter):
            query['FiscalYearAndQuarter'] = request.fiscal_year_and_quarter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRenewalRateList',
            version='2025-02-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                agency_20250227_models.GetRenewalRateListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                agency_20250227_models.GetRenewalRateListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_renewal_rate_list(
        self,
        request: agency_20250227_models.GetRenewalRateListRequest,
    ) -> agency_20250227_models.GetRenewalRateListResponse:
        """
        @summary 查询伙伴续费率
        
        @param request: GetRenewalRateListRequest
        @return: GetRenewalRateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_renewal_rate_list_with_options(request, runtime)

    async def get_renewal_rate_list_async(
        self,
        request: agency_20250227_models.GetRenewalRateListRequest,
    ) -> agency_20250227_models.GetRenewalRateListResponse:
        """
        @summary 查询伙伴续费率
        
        @param request: GetRenewalRateListRequest
        @return: GetRenewalRateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_renewal_rate_list_with_options_async(request, runtime)

    def get_sub_partner_list_with_options(
        self,
        request: agency_20250227_models.GetSubPartnerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20250227_models.GetSubPartnerListResponse:
        """
        @summary 查询二级分销商列表
        
        @param request: GetSubPartnerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubPartnerListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_partner_company_name):
            query['SubPartnerCompanyName'] = request.sub_partner_company_name
        if not UtilClient.is_unset(request.sub_partner_pid):
            query['SubPartnerPid'] = request.sub_partner_pid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubPartnerList',
            version='2025-02-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                agency_20250227_models.GetSubPartnerListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                agency_20250227_models.GetSubPartnerListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_sub_partner_list_with_options_async(
        self,
        request: agency_20250227_models.GetSubPartnerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20250227_models.GetSubPartnerListResponse:
        """
        @summary 查询二级分销商列表
        
        @param request: GetSubPartnerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubPartnerListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_partner_company_name):
            query['SubPartnerCompanyName'] = request.sub_partner_company_name
        if not UtilClient.is_unset(request.sub_partner_pid):
            query['SubPartnerPid'] = request.sub_partner_pid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubPartnerList',
            version='2025-02-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                agency_20250227_models.GetSubPartnerListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                agency_20250227_models.GetSubPartnerListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_sub_partner_list(
        self,
        request: agency_20250227_models.GetSubPartnerListRequest,
    ) -> agency_20250227_models.GetSubPartnerListResponse:
        """
        @summary 查询二级分销商列表
        
        @param request: GetSubPartnerListRequest
        @return: GetSubPartnerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sub_partner_list_with_options(request, runtime)

    async def get_sub_partner_list_async(
        self,
        request: agency_20250227_models.GetSubPartnerListRequest,
    ) -> agency_20250227_models.GetSubPartnerListResponse:
        """
        @summary 查询二级分销商列表
        
        @param request: GetSubPartnerListRequest
        @return: GetSubPartnerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sub_partner_list_with_options_async(request, runtime)

    def get_sub_partner_order_list_with_options(
        self,
        tmp_req: agency_20250227_models.GetSubPartnerOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20250227_models.GetSubPartnerOrderListResponse:
        """
        @summary 查询拓渠订单
        
        @param tmp_req: GetSubPartnerOrderListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubPartnerOrderListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = agency_20250227_models.GetSubPartnerOrderListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_type_list):
            request.order_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_type_list, 'OrderTypeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.order_create_after):
            query['OrderCreateAfter'] = request.order_create_after
        if not UtilClient.is_unset(request.order_create_before):
            query['OrderCreateBefore'] = request.order_create_before
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.order_pay_after):
            query['OrderPayAfter'] = request.order_pay_after
        if not UtilClient.is_unset(request.order_pay_before):
            query['OrderPayBefore'] = request.order_pay_before
        if not UtilClient.is_unset(request.order_status):
            query['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.order_type_list_shrink):
            query['OrderTypeList'] = request.order_type_list_shrink
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pay_amount_after):
            query['PayAmountAfter'] = request.pay_amount_after
        if not UtilClient.is_unset(request.pay_amount_before):
            query['PayAmountBefore'] = request.pay_amount_before
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sub_partner_name):
            query['SubPartnerName'] = request.sub_partner_name
        if not UtilClient.is_unset(request.sub_partner_uid):
            query['SubPartnerUid'] = request.sub_partner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubPartnerOrderList',
            version='2025-02-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                agency_20250227_models.GetSubPartnerOrderListResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                agency_20250227_models.GetSubPartnerOrderListResponse(),
                self.execute(params, req, runtime)
            )

    async def get_sub_partner_order_list_with_options_async(
        self,
        tmp_req: agency_20250227_models.GetSubPartnerOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20250227_models.GetSubPartnerOrderListResponse:
        """
        @summary 查询拓渠订单
        
        @param tmp_req: GetSubPartnerOrderListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubPartnerOrderListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = agency_20250227_models.GetSubPartnerOrderListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_type_list):
            request.order_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_type_list, 'OrderTypeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.order_create_after):
            query['OrderCreateAfter'] = request.order_create_after
        if not UtilClient.is_unset(request.order_create_before):
            query['OrderCreateBefore'] = request.order_create_before
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.order_pay_after):
            query['OrderPayAfter'] = request.order_pay_after
        if not UtilClient.is_unset(request.order_pay_before):
            query['OrderPayBefore'] = request.order_pay_before
        if not UtilClient.is_unset(request.order_status):
            query['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.order_type_list_shrink):
            query['OrderTypeList'] = request.order_type_list_shrink
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pay_amount_after):
            query['PayAmountAfter'] = request.pay_amount_after
        if not UtilClient.is_unset(request.pay_amount_before):
            query['PayAmountBefore'] = request.pay_amount_before
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.sub_partner_name):
            query['SubPartnerName'] = request.sub_partner_name
        if not UtilClient.is_unset(request.sub_partner_uid):
            query['SubPartnerUid'] = request.sub_partner_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubPartnerOrderList',
            version='2025-02-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                agency_20250227_models.GetSubPartnerOrderListResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                agency_20250227_models.GetSubPartnerOrderListResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_sub_partner_order_list(
        self,
        request: agency_20250227_models.GetSubPartnerOrderListRequest,
    ) -> agency_20250227_models.GetSubPartnerOrderListResponse:
        """
        @summary 查询拓渠订单
        
        @param request: GetSubPartnerOrderListRequest
        @return: GetSubPartnerOrderListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sub_partner_order_list_with_options(request, runtime)

    async def get_sub_partner_order_list_async(
        self,
        request: agency_20250227_models.GetSubPartnerOrderListRequest,
    ) -> agency_20250227_models.GetSubPartnerOrderListResponse:
        """
        @summary 查询拓渠订单
        
        @param request: GetSubPartnerOrderListRequest
        @return: GetSubPartnerOrderListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sub_partner_order_list_with_options_async(request, runtime)
