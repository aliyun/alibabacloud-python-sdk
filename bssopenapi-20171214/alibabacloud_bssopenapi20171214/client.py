# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bssopenapi20171214 import models as bss_open_api_20171214_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_account_relation_with_options(
        self,
        request: bss_open_api_20171214_models.AddAccountRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.AddAccountRelationResponse:
        """
        1\\. For more information about a financial relationship, see [Financial relationships](https://help.aliyun.com/document_detail/100376.html?spm=a2c4g.11186623.6.563.52a83908ypl4yE) or [Financial relationships](https://www.alibabacloud.com/help/en/doc-detail/116383.html). 2. If enterprise names used by the management account and a member for real-name verification are the same, you do not need to call an API operation for confirmation. Otherwise, you must call the ConfirmRelation operation for confirmation.
        
        @param request: AddAccountRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAccountRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_nick):
            query['ChildNick'] = request.child_nick
        if not UtilClient.is_unset(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not UtilClient.is_unset(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not UtilClient.is_unset(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.role_codes):
            query['RoleCodes'] = request.role_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAccountRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.AddAccountRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_account_relation_with_options_async(
        self,
        request: bss_open_api_20171214_models.AddAccountRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.AddAccountRelationResponse:
        """
        1\\. For more information about a financial relationship, see [Financial relationships](https://help.aliyun.com/document_detail/100376.html?spm=a2c4g.11186623.6.563.52a83908ypl4yE) or [Financial relationships](https://www.alibabacloud.com/help/en/doc-detail/116383.html). 2. If enterprise names used by the management account and a member for real-name verification are the same, you do not need to call an API operation for confirmation. Otherwise, you must call the ConfirmRelation operation for confirmation.
        
        @param request: AddAccountRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAccountRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_nick):
            query['ChildNick'] = request.child_nick
        if not UtilClient.is_unset(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not UtilClient.is_unset(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not UtilClient.is_unset(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.role_codes):
            query['RoleCodes'] = request.role_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAccountRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.AddAccountRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_account_relation(
        self,
        request: bss_open_api_20171214_models.AddAccountRelationRequest,
    ) -> bss_open_api_20171214_models.AddAccountRelationResponse:
        """
        1\\. For more information about a financial relationship, see [Financial relationships](https://help.aliyun.com/document_detail/100376.html?spm=a2c4g.11186623.6.563.52a83908ypl4yE) or [Financial relationships](https://www.alibabacloud.com/help/en/doc-detail/116383.html). 2. If enterprise names used by the management account and a member for real-name verification are the same, you do not need to call an API operation for confirmation. Otherwise, you must call the ConfirmRelation operation for confirmation.
        
        @param request: AddAccountRelationRequest
        @return: AddAccountRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_account_relation_with_options(request, runtime)

    async def add_account_relation_async(
        self,
        request: bss_open_api_20171214_models.AddAccountRelationRequest,
    ) -> bss_open_api_20171214_models.AddAccountRelationResponse:
        """
        1\\. For more information about a financial relationship, see [Financial relationships](https://help.aliyun.com/document_detail/100376.html?spm=a2c4g.11186623.6.563.52a83908ypl4yE) or [Financial relationships](https://www.alibabacloud.com/help/en/doc-detail/116383.html). 2. If enterprise names used by the management account and a member for real-name verification are the same, you do not need to call an API operation for confirmation. Otherwise, you must call the ConfirmRelation operation for confirmation.
        
        @param request: AddAccountRelationRequest
        @return: AddAccountRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_account_relation_with_options_async(request, runtime)

    def allocate_cost_unit_resource_with_options(
        self,
        request: bss_open_api_20171214_models.AllocateCostUnitResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.AllocateCostUnitResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_unit_id):
            query['FromUnitId'] = request.from_unit_id
        if not UtilClient.is_unset(request.from_unit_user_id):
            query['FromUnitUserId'] = request.from_unit_user_id
        if not UtilClient.is_unset(request.resource_instance_list):
            query['ResourceInstanceList'] = request.resource_instance_list
        if not UtilClient.is_unset(request.to_unit_id):
            query['ToUnitId'] = request.to_unit_id
        if not UtilClient.is_unset(request.to_unit_user_id):
            query['ToUnitUserId'] = request.to_unit_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateCostUnitResource',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.AllocateCostUnitResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_cost_unit_resource_with_options_async(
        self,
        request: bss_open_api_20171214_models.AllocateCostUnitResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.AllocateCostUnitResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_unit_id):
            query['FromUnitId'] = request.from_unit_id
        if not UtilClient.is_unset(request.from_unit_user_id):
            query['FromUnitUserId'] = request.from_unit_user_id
        if not UtilClient.is_unset(request.resource_instance_list):
            query['ResourceInstanceList'] = request.resource_instance_list
        if not UtilClient.is_unset(request.to_unit_id):
            query['ToUnitId'] = request.to_unit_id
        if not UtilClient.is_unset(request.to_unit_user_id):
            query['ToUnitUserId'] = request.to_unit_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateCostUnitResource',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.AllocateCostUnitResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_cost_unit_resource(
        self,
        request: bss_open_api_20171214_models.AllocateCostUnitResourceRequest,
    ) -> bss_open_api_20171214_models.AllocateCostUnitResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_cost_unit_resource_with_options(request, runtime)

    async def allocate_cost_unit_resource_async(
        self,
        request: bss_open_api_20171214_models.AllocateCostUnitResourceRequest,
    ) -> bss_open_api_20171214_models.AllocateCostUnitResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_cost_unit_resource_with_options_async(request, runtime)

    def apply_invoice_with_options(
        self,
        request: bss_open_api_20171214_models.ApplyInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ApplyInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.apply_user_nick):
            query['ApplyUserNick'] = request.apply_user_nick
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.invoice_amount):
            query['InvoiceAmount'] = request.invoice_amount
        if not UtilClient.is_unset(request.invoice_by_amount):
            query['InvoiceByAmount'] = request.invoice_by_amount
        if not UtilClient.is_unset(request.invoicing_type):
            query['InvoicingType'] = request.invoicing_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.process_way):
            query['ProcessWay'] = request.process_way
        if not UtilClient.is_unset(request.selected_ids):
            query['SelectedIds'] = request.selected_ids
        if not UtilClient.is_unset(request.user_remark):
            query['UserRemark'] = request.user_remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyInvoice',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ApplyInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_invoice_with_options_async(
        self,
        request: bss_open_api_20171214_models.ApplyInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ApplyInvoiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_id):
            query['AddressId'] = request.address_id
        if not UtilClient.is_unset(request.apply_user_nick):
            query['ApplyUserNick'] = request.apply_user_nick
        if not UtilClient.is_unset(request.customer_id):
            query['CustomerId'] = request.customer_id
        if not UtilClient.is_unset(request.invoice_amount):
            query['InvoiceAmount'] = request.invoice_amount
        if not UtilClient.is_unset(request.invoice_by_amount):
            query['InvoiceByAmount'] = request.invoice_by_amount
        if not UtilClient.is_unset(request.invoicing_type):
            query['InvoicingType'] = request.invoicing_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.process_way):
            query['ProcessWay'] = request.process_way
        if not UtilClient.is_unset(request.selected_ids):
            query['SelectedIds'] = request.selected_ids
        if not UtilClient.is_unset(request.user_remark):
            query['UserRemark'] = request.user_remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyInvoice',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ApplyInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_invoice(
        self,
        request: bss_open_api_20171214_models.ApplyInvoiceRequest,
    ) -> bss_open_api_20171214_models.ApplyInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_invoice_with_options(request, runtime)

    async def apply_invoice_async(
        self,
        request: bss_open_api_20171214_models.ApplyInvoiceRequest,
    ) -> bss_open_api_20171214_models.ApplyInvoiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_invoice_with_options_async(request, runtime)

    def cancel_order_with_options(
        self,
        request: bss_open_api_20171214_models.CancelOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOrder',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CancelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_order_with_options_async(
        self,
        request: bss_open_api_20171214_models.CancelOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOrder',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CancelOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_order(
        self,
        request: bss_open_api_20171214_models.CancelOrderRequest,
    ) -> bss_open_api_20171214_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_with_options(request, runtime)

    async def cancel_order_async(
        self,
        request: bss_open_api_20171214_models.CancelOrderRequest,
    ) -> bss_open_api_20171214_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_order_with_options_async(request, runtime)

    def change_reseller_consume_amount_with_options(
        self,
        request: bss_open_api_20171214_models.ChangeResellerConsumeAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ChangeResellerConsumeAmountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjust_type):
            query['AdjustType'] = request.adjust_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.currency):
            query['Currency'] = request.currency
        if not UtilClient.is_unset(request.extend_map):
            query['ExtendMap'] = request.extend_map
        if not UtilClient.is_unset(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResellerConsumeAmount',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ChangeResellerConsumeAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_reseller_consume_amount_with_options_async(
        self,
        request: bss_open_api_20171214_models.ChangeResellerConsumeAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ChangeResellerConsumeAmountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjust_type):
            query['AdjustType'] = request.adjust_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.currency):
            query['Currency'] = request.currency
        if not UtilClient.is_unset(request.extend_map):
            query['ExtendMap'] = request.extend_map
        if not UtilClient.is_unset(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResellerConsumeAmount',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ChangeResellerConsumeAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_reseller_consume_amount(
        self,
        request: bss_open_api_20171214_models.ChangeResellerConsumeAmountRequest,
    ) -> bss_open_api_20171214_models.ChangeResellerConsumeAmountResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_reseller_consume_amount_with_options(request, runtime)

    async def change_reseller_consume_amount_async(
        self,
        request: bss_open_api_20171214_models.ChangeResellerConsumeAmountRequest,
    ) -> bss_open_api_20171214_models.ChangeResellerConsumeAmountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_reseller_consume_amount_with_options_async(request, runtime)

    def confirm_relation_with_options(
        self,
        request: bss_open_api_20171214_models.ConfirmRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ConfirmRelationResponse:
        """
        1\\. A member needs to confirm an invitation only if a financial management relationship is established between the management account and the member and enterprise names used by the management account and the member for real-name verification are different. 2. The permissions to be confirmed must be the same as those granted to the member when the management account initiates the invitation.
        
        @param request: ConfirmRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not UtilClient.is_unset(request.confirm_code):
            query['ConfirmCode'] = request.confirm_code
        if not UtilClient.is_unset(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not UtilClient.is_unset(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not UtilClient.is_unset(request.relation_id):
            query['RelationId'] = request.relation_id
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ConfirmRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_relation_with_options_async(
        self,
        request: bss_open_api_20171214_models.ConfirmRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ConfirmRelationResponse:
        """
        1\\. A member needs to confirm an invitation only if a financial management relationship is established between the management account and the member and enterprise names used by the management account and the member for real-name verification are different. 2. The permissions to be confirmed must be the same as those granted to the member when the management account initiates the invitation.
        
        @param request: ConfirmRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfirmRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not UtilClient.is_unset(request.confirm_code):
            query['ConfirmCode'] = request.confirm_code
        if not UtilClient.is_unset(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not UtilClient.is_unset(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not UtilClient.is_unset(request.relation_id):
            query['RelationId'] = request.relation_id
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ConfirmRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_relation(
        self,
        request: bss_open_api_20171214_models.ConfirmRelationRequest,
    ) -> bss_open_api_20171214_models.ConfirmRelationResponse:
        """
        1\\. A member needs to confirm an invitation only if a financial management relationship is established between the management account and the member and enterprise names used by the management account and the member for real-name verification are different. 2. The permissions to be confirmed must be the same as those granted to the member when the management account initiates the invitation.
        
        @param request: ConfirmRelationRequest
        @return: ConfirmRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.confirm_relation_with_options(request, runtime)

    async def confirm_relation_async(
        self,
        request: bss_open_api_20171214_models.ConfirmRelationRequest,
    ) -> bss_open_api_20171214_models.ConfirmRelationResponse:
        """
        1\\. A member needs to confirm an invitation only if a financial management relationship is established between the management account and the member and enterprise names used by the management account and the member for real-name verification are different. 2. The permissions to be confirmed must be the same as those granted to the member when the management account initiates the invitation.
        
        @param request: ConfirmRelationRequest
        @return: ConfirmRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.confirm_relation_with_options_async(request, runtime)

    def convert_charge_type_with_options(
        self,
        request: bss_open_api_20171214_models.ConvertChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ConvertChargeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertChargeType',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ConvertChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_charge_type_with_options_async(
        self,
        request: bss_open_api_20171214_models.ConvertChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ConvertChargeTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertChargeType',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ConvertChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_charge_type(
        self,
        request: bss_open_api_20171214_models.ConvertChargeTypeRequest,
    ) -> bss_open_api_20171214_models.ConvertChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.convert_charge_type_with_options(request, runtime)

    async def convert_charge_type_async(
        self,
        request: bss_open_api_20171214_models.ConvertChargeTypeRequest,
    ) -> bss_open_api_20171214_models.ConvertChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.convert_charge_type_with_options_async(request, runtime)

    def create_ag_account_with_options(
        self,
        request: bss_open_api_20171214_models.CreateAgAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateAgAccountResponse:
        """
        You can call this operation to create an account so as to establish a master-member financial relationship.
        
        @param request: CreateAgAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_attr):
            query['AccountAttr'] = request.account_attr
        if not UtilClient.is_unset(request.city_name):
            query['CityName'] = request.city_name
        if not UtilClient.is_unset(request.enterprise_name):
            query['EnterpriseName'] = request.enterprise_name
        if not UtilClient.is_unset(request.first_name):
            query['FirstName'] = request.first_name
        if not UtilClient.is_unset(request.last_name):
            query['LastName'] = request.last_name
        if not UtilClient.is_unset(request.login_email):
            query['LoginEmail'] = request.login_email
        if not UtilClient.is_unset(request.nation_code):
            query['NationCode'] = request.nation_code
        if not UtilClient.is_unset(request.postcode):
            query['Postcode'] = request.postcode
        if not UtilClient.is_unset(request.province_name):
            query['ProvinceName'] = request.province_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAgAccount',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateAgAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ag_account_with_options_async(
        self,
        request: bss_open_api_20171214_models.CreateAgAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateAgAccountResponse:
        """
        You can call this operation to create an account so as to establish a master-member financial relationship.
        
        @param request: CreateAgAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAgAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_attr):
            query['AccountAttr'] = request.account_attr
        if not UtilClient.is_unset(request.city_name):
            query['CityName'] = request.city_name
        if not UtilClient.is_unset(request.enterprise_name):
            query['EnterpriseName'] = request.enterprise_name
        if not UtilClient.is_unset(request.first_name):
            query['FirstName'] = request.first_name
        if not UtilClient.is_unset(request.last_name):
            query['LastName'] = request.last_name
        if not UtilClient.is_unset(request.login_email):
            query['LoginEmail'] = request.login_email
        if not UtilClient.is_unset(request.nation_code):
            query['NationCode'] = request.nation_code
        if not UtilClient.is_unset(request.postcode):
            query['Postcode'] = request.postcode
        if not UtilClient.is_unset(request.province_name):
            query['ProvinceName'] = request.province_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAgAccount',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateAgAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ag_account(
        self,
        request: bss_open_api_20171214_models.CreateAgAccountRequest,
    ) -> bss_open_api_20171214_models.CreateAgAccountResponse:
        """
        You can call this operation to create an account so as to establish a master-member financial relationship.
        
        @param request: CreateAgAccountRequest
        @return: CreateAgAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ag_account_with_options(request, runtime)

    async def create_ag_account_async(
        self,
        request: bss_open_api_20171214_models.CreateAgAccountRequest,
    ) -> bss_open_api_20171214_models.CreateAgAccountResponse:
        """
        You can call this operation to create an account so as to establish a master-member financial relationship.
        
        @param request: CreateAgAccountRequest
        @return: CreateAgAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ag_account_with_options_async(request, runtime)

    def create_cost_unit_with_options(
        self,
        request: bss_open_api_20171214_models.CreateCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateCostUnitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.unit_entity_list):
            query['UnitEntityList'] = request.unit_entity_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCostUnit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateCostUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cost_unit_with_options_async(
        self,
        request: bss_open_api_20171214_models.CreateCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateCostUnitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.unit_entity_list):
            query['UnitEntityList'] = request.unit_entity_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCostUnit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateCostUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cost_unit(
        self,
        request: bss_open_api_20171214_models.CreateCostUnitRequest,
    ) -> bss_open_api_20171214_models.CreateCostUnitResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cost_unit_with_options(request, runtime)

    async def create_cost_unit_async(
        self,
        request: bss_open_api_20171214_models.CreateCostUnitRequest,
    ) -> bss_open_api_20171214_models.CreateCostUnitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cost_unit_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: bss_open_api_20171214_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logistics):
            query['Logistics'] = request.logistics
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter):
            query['Parameter'] = request.parameter
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: bss_open_api_20171214_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logistics):
            query['Logistics'] = request.logistics
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter):
            query['Parameter'] = request.parameter
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: bss_open_api_20171214_models.CreateInstanceRequest,
    ) -> bss_open_api_20171214_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: bss_open_api_20171214_models.CreateInstanceRequest,
    ) -> bss_open_api_20171214_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_reseller_user_quota_with_options(
        self,
        request: bss_open_api_20171214_models.CreateResellerUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateResellerUserQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.currency):
            query['Currency'] = request.currency
        if not UtilClient.is_unset(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResellerUserQuota',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateResellerUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_reseller_user_quota_with_options_async(
        self,
        request: bss_open_api_20171214_models.CreateResellerUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateResellerUserQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.currency):
            query['Currency'] = request.currency
        if not UtilClient.is_unset(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResellerUserQuota',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateResellerUserQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_reseller_user_quota(
        self,
        request: bss_open_api_20171214_models.CreateResellerUserQuotaRequest,
    ) -> bss_open_api_20171214_models.CreateResellerUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_reseller_user_quota_with_options(request, runtime)

    async def create_reseller_user_quota_async(
        self,
        request: bss_open_api_20171214_models.CreateResellerUserQuotaRequest,
    ) -> bss_open_api_20171214_models.CreateResellerUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_reseller_user_quota_with_options_async(request, runtime)

    def create_resource_package_with_options(
        self,
        request: bss_open_api_20171214_models.CreateResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateResourcePackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourcePackage',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_package_with_options_async(
        self,
        request: bss_open_api_20171214_models.CreateResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateResourcePackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourcePackage',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateResourcePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_package(
        self,
        request: bss_open_api_20171214_models.CreateResourcePackageRequest,
    ) -> bss_open_api_20171214_models.CreateResourcePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_package_with_options(request, runtime)

    async def create_resource_package_async(
        self,
        request: bss_open_api_20171214_models.CreateResourcePackageRequest,
    ) -> bss_open_api_20171214_models.CreateResourcePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_package_with_options_async(request, runtime)

    def create_savings_plans_instance_with_options(
        self,
        tmp_req: bss_open_api_20171214_models.CreateSavingsPlansInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateSavingsPlansInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20171214_models.CreateSavingsPlansInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_map):
            request.extend_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_map, 'ExtendMap', 'json')
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.extend_map_shrink):
            query['ExtendMap'] = request.extend_map_shrink
        if not UtilClient.is_unset(request.pay_mode):
            query['PayMode'] = request.pay_mode
        if not UtilClient.is_unset(request.pool_value):
            query['PoolValue'] = request.pool_value
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSavingsPlansInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateSavingsPlansInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_savings_plans_instance_with_options_async(
        self,
        tmp_req: bss_open_api_20171214_models.CreateSavingsPlansInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateSavingsPlansInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20171214_models.CreateSavingsPlansInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_map):
            request.extend_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_map, 'ExtendMap', 'json')
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.extend_map_shrink):
            query['ExtendMap'] = request.extend_map_shrink
        if not UtilClient.is_unset(request.pay_mode):
            query['PayMode'] = request.pay_mode
        if not UtilClient.is_unset(request.pool_value):
            query['PoolValue'] = request.pool_value
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSavingsPlansInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.CreateSavingsPlansInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_savings_plans_instance(
        self,
        request: bss_open_api_20171214_models.CreateSavingsPlansInstanceRequest,
    ) -> bss_open_api_20171214_models.CreateSavingsPlansInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_savings_plans_instance_with_options(request, runtime)

    async def create_savings_plans_instance_async(
        self,
        request: bss_open_api_20171214_models.CreateSavingsPlansInstanceRequest,
    ) -> bss_open_api_20171214_models.CreateSavingsPlansInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_savings_plans_instance_with_options_async(request, runtime)

    def delete_cost_unit_with_options(
        self,
        request: bss_open_api_20171214_models.DeleteCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DeleteCostUnitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.unit_id):
            query['UnitId'] = request.unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCostUnit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DeleteCostUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cost_unit_with_options_async(
        self,
        request: bss_open_api_20171214_models.DeleteCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DeleteCostUnitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.unit_id):
            query['UnitId'] = request.unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCostUnit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DeleteCostUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cost_unit(
        self,
        request: bss_open_api_20171214_models.DeleteCostUnitRequest,
    ) -> bss_open_api_20171214_models.DeleteCostUnitResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cost_unit_with_options(request, runtime)

    async def delete_cost_unit_async(
        self,
        request: bss_open_api_20171214_models.DeleteCostUnitRequest,
    ) -> bss_open_api_20171214_models.DeleteCostUnitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cost_unit_with_options_async(request, runtime)

    def describe_cost_budgets_summary_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeCostBudgetsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeCostBudgetsSummaryResponse:
        """
        This operation is in beta testing and is only available for specific users in the whitelist. Excessive calls may result in performance issues. For example, the response times out.
        
        @param request: DescribeCostBudgetsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCostBudgetsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.budget_name):
            query['BudgetName'] = request.budget_name
        if not UtilClient.is_unset(request.budget_status):
            query['BudgetStatus'] = request.budget_status
        if not UtilClient.is_unset(request.budget_type):
            query['BudgetType'] = request.budget_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCostBudgetsSummary',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeCostBudgetsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cost_budgets_summary_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeCostBudgetsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeCostBudgetsSummaryResponse:
        """
        This operation is in beta testing and is only available for specific users in the whitelist. Excessive calls may result in performance issues. For example, the response times out.
        
        @param request: DescribeCostBudgetsSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCostBudgetsSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.budget_name):
            query['BudgetName'] = request.budget_name
        if not UtilClient.is_unset(request.budget_status):
            query['BudgetStatus'] = request.budget_status
        if not UtilClient.is_unset(request.budget_type):
            query['BudgetType'] = request.budget_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCostBudgetsSummary',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeCostBudgetsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cost_budgets_summary(
        self,
        request: bss_open_api_20171214_models.DescribeCostBudgetsSummaryRequest,
    ) -> bss_open_api_20171214_models.DescribeCostBudgetsSummaryResponse:
        """
        This operation is in beta testing and is only available for specific users in the whitelist. Excessive calls may result in performance issues. For example, the response times out.
        
        @param request: DescribeCostBudgetsSummaryRequest
        @return: DescribeCostBudgetsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cost_budgets_summary_with_options(request, runtime)

    async def describe_cost_budgets_summary_async(
        self,
        request: bss_open_api_20171214_models.DescribeCostBudgetsSummaryRequest,
    ) -> bss_open_api_20171214_models.DescribeCostBudgetsSummaryResponse:
        """
        This operation is in beta testing and is only available for specific users in the whitelist. Excessive calls may result in performance issues. For example, the response times out.
        
        @param request: DescribeCostBudgetsSummaryRequest
        @return: DescribeCostBudgetsSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cost_budgets_summary_with_options_async(request, runtime)

    def describe_instance_amortized_cost_by_amortization_period_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponse:
        """
        You can view and export the allocated costs of the current month after 10:00 on the fourth day of the next month. The allocated costs of a single allocation month may involve orders or bills in different billing cycles. If a historical allocated amount is incorrect, the historical allocated costs need to be adjusted. As a result, the allocated costs displayed for a single allocation month may be different at different time points.
        
        @param request: DescribeInstanceAmortizedCostByAmortizationPeriodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAmortizedCostByAmortizationPeriodResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.consume_period_filter):
            body['ConsumePeriodFilter'] = request.consume_period_filter
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAmortizedCostByAmortizationPeriod',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_amortized_cost_by_amortization_period_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponse:
        """
        You can view and export the allocated costs of the current month after 10:00 on the fourth day of the next month. The allocated costs of a single allocation month may involve orders or bills in different billing cycles. If a historical allocated amount is incorrect, the historical allocated costs need to be adjusted. As a result, the allocated costs displayed for a single allocation month may be different at different time points.
        
        @param request: DescribeInstanceAmortizedCostByAmortizationPeriodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceAmortizedCostByAmortizationPeriodResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.consume_period_filter):
            body['ConsumePeriodFilter'] = request.consume_period_filter
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAmortizedCostByAmortizationPeriod',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_amortized_cost_by_amortization_period(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodRequest,
    ) -> bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponse:
        """
        You can view and export the allocated costs of the current month after 10:00 on the fourth day of the next month. The allocated costs of a single allocation month may involve orders or bills in different billing cycles. If a historical allocated amount is incorrect, the historical allocated costs need to be adjusted. As a result, the allocated costs displayed for a single allocation month may be different at different time points.
        
        @param request: DescribeInstanceAmortizedCostByAmortizationPeriodRequest
        @return: DescribeInstanceAmortizedCostByAmortizationPeriodResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_amortized_cost_by_amortization_period_with_options(request, runtime)

    async def describe_instance_amortized_cost_by_amortization_period_async(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodRequest,
    ) -> bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodResponse:
        """
        You can view and export the allocated costs of the current month after 10:00 on the fourth day of the next month. The allocated costs of a single allocation month may involve orders or bills in different billing cycles. If a historical allocated amount is incorrect, the historical allocated costs need to be adjusted. As a result, the allocated costs displayed for a single allocation month may be different at different time points.
        
        @param request: DescribeInstanceAmortizedCostByAmortizationPeriodRequest
        @return: DescribeInstanceAmortizedCostByAmortizationPeriodResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_amortized_cost_by_amortization_period_with_options_async(request, runtime)

    def describe_instance_amortized_cost_by_amortization_period_date_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amortization_date_end):
            body['AmortizationDateEnd'] = request.amortization_date_end
        if not UtilClient.is_unset(request.amortization_date_start):
            body['AmortizationDateStart'] = request.amortization_date_start
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAmortizedCostByAmortizationPeriodDate',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_amortized_cost_by_amortization_period_date_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amortization_date_end):
            body['AmortizationDateEnd'] = request.amortization_date_end
        if not UtilClient.is_unset(request.amortization_date_start):
            body['AmortizationDateStart'] = request.amortization_date_start
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAmortizedCostByAmortizationPeriodDate',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_amortized_cost_by_amortization_period_date(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateRequest,
    ) -> bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_amortized_cost_by_amortization_period_date_with_options(request, runtime)

    async def describe_instance_amortized_cost_by_amortization_period_date_async(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateRequest,
    ) -> bss_open_api_20171214_models.DescribeInstanceAmortizedCostByAmortizationPeriodDateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_amortized_cost_by_amortization_period_date_with_options_async(request, runtime)

    def describe_instance_amortized_cost_by_consume_period_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceAmortizedCostByConsumePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeInstanceAmortizedCostByConsumePeriodResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amortization_period_filter):
            body['AmortizationPeriodFilter'] = request.amortization_period_filter
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAmortizedCostByConsumePeriod',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeInstanceAmortizedCostByConsumePeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_amortized_cost_by_consume_period_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceAmortizedCostByConsumePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeInstanceAmortizedCostByConsumePeriodResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amortization_period_filter):
            body['AmortizationPeriodFilter'] = request.amortization_period_filter
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.instance_id_list):
            body['InstanceIdList'] = request.instance_id_list
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInstanceAmortizedCostByConsumePeriod',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeInstanceAmortizedCostByConsumePeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_amortized_cost_by_consume_period(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceAmortizedCostByConsumePeriodRequest,
    ) -> bss_open_api_20171214_models.DescribeInstanceAmortizedCostByConsumePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_amortized_cost_by_consume_period_with_options(request, runtime)

    async def describe_instance_amortized_cost_by_consume_period_async(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceAmortizedCostByConsumePeriodRequest,
    ) -> bss_open_api_20171214_models.DescribeInstanceAmortizedCostByConsumePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_amortized_cost_by_consume_period_with_options_async(request, runtime)

    def describe_instance_bill_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeInstanceBillResponse:
        """
        Instance bills are generated after the total bill is split. In most cases, the instance bills do not include data generated on the last day of the specified billing cycle.
        *   The instance information may change during the billing cycle. The instance configurations and types in monthly bills are subject to the point in time when you query bills. For more information, see the corresponding bill details.
        *   You can query data generated after June 2020 for Cloud Communications services. You can query data generated after November 2020 for Alibaba Cloud Domains.
        
        @param request: DescribeInstanceBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceID'] = request.instance_id
        if not UtilClient.is_unset(request.is_billing_item):
            query['IsBillingItem'] = request.is_billing_item
        if not UtilClient.is_unset(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeInstanceBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeInstanceBillResponse:
        """
        Instance bills are generated after the total bill is split. In most cases, the instance bills do not include data generated on the last day of the specified billing cycle.
        *   The instance information may change during the billing cycle. The instance configurations and types in monthly bills are subject to the point in time when you query bills. For more information, see the corresponding bill details.
        *   You can query data generated after June 2020 for Cloud Communications services. You can query data generated after November 2020 for Alibaba Cloud Domains.
        
        @param request: DescribeInstanceBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceID'] = request.instance_id
        if not UtilClient.is_unset(request.is_billing_item):
            query['IsBillingItem'] = request.is_billing_item
        if not UtilClient.is_unset(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeInstanceBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_bill(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceBillRequest,
    ) -> bss_open_api_20171214_models.DescribeInstanceBillResponse:
        """
        Instance bills are generated after the total bill is split. In most cases, the instance bills do not include data generated on the last day of the specified billing cycle.
        *   The instance information may change during the billing cycle. The instance configurations and types in monthly bills are subject to the point in time when you query bills. For more information, see the corresponding bill details.
        *   You can query data generated after June 2020 for Cloud Communications services. You can query data generated after November 2020 for Alibaba Cloud Domains.
        
        @param request: DescribeInstanceBillRequest
        @return: DescribeInstanceBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_bill_with_options(request, runtime)

    async def describe_instance_bill_async(
        self,
        request: bss_open_api_20171214_models.DescribeInstanceBillRequest,
    ) -> bss_open_api_20171214_models.DescribeInstanceBillResponse:
        """
        Instance bills are generated after the total bill is split. In most cases, the instance bills do not include data generated on the last day of the specified billing cycle.
        *   The instance information may change during the billing cycle. The instance configurations and types in monthly bills are subject to the point in time when you query bills. For more information, see the corresponding bill details.
        *   You can query data generated after June 2020 for Cloud Communications services. You can query data generated after November 2020 for Alibaba Cloud Domains.
        
        @param request: DescribeInstanceBillRequest
        @return: DescribeInstanceBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_bill_with_options_async(request, runtime)

    def describe_pricing_module_with_options(
        self,
        request: bss_open_api_20171214_models.DescribePricingModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribePricingModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePricingModule',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribePricingModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pricing_module_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribePricingModuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribePricingModuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePricingModule',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribePricingModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pricing_module(
        self,
        request: bss_open_api_20171214_models.DescribePricingModuleRequest,
    ) -> bss_open_api_20171214_models.DescribePricingModuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pricing_module_with_options(request, runtime)

    async def describe_pricing_module_async(
        self,
        request: bss_open_api_20171214_models.DescribePricingModuleRequest,
    ) -> bss_open_api_20171214_models.DescribePricingModuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pricing_module_with_options_async(request, runtime)

    def describe_product_amortized_cost_by_amortization_period_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeProductAmortizedCostByAmortizationPeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeProductAmortizedCostByAmortizationPeriodResponse:
        """
        You can view and export the allocated costs of the current month after 10:00 on the fourth day of the next month. The allocated costs of a single allocation month may involve orders or bills in different billing cycles. If a historical allocated amount is incorrect, the historical allocated costs need to be adjusted. As a result, the allocated costs displayed for a single allocation month may be different at different time points.
        
        @param request: DescribeProductAmortizedCostByAmortizationPeriodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProductAmortizedCostByAmortizationPeriodResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.consume_period_filter):
            body['ConsumePeriodFilter'] = request.consume_period_filter
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProductAmortizedCostByAmortizationPeriod',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeProductAmortizedCostByAmortizationPeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_product_amortized_cost_by_amortization_period_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeProductAmortizedCostByAmortizationPeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeProductAmortizedCostByAmortizationPeriodResponse:
        """
        You can view and export the allocated costs of the current month after 10:00 on the fourth day of the next month. The allocated costs of a single allocation month may involve orders or bills in different billing cycles. If a historical allocated amount is incorrect, the historical allocated costs need to be adjusted. As a result, the allocated costs displayed for a single allocation month may be different at different time points.
        
        @param request: DescribeProductAmortizedCostByAmortizationPeriodRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProductAmortizedCostByAmortizationPeriodResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.consume_period_filter):
            body['ConsumePeriodFilter'] = request.consume_period_filter
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProductAmortizedCostByAmortizationPeriod',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeProductAmortizedCostByAmortizationPeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_product_amortized_cost_by_amortization_period(
        self,
        request: bss_open_api_20171214_models.DescribeProductAmortizedCostByAmortizationPeriodRequest,
    ) -> bss_open_api_20171214_models.DescribeProductAmortizedCostByAmortizationPeriodResponse:
        """
        You can view and export the allocated costs of the current month after 10:00 on the fourth day of the next month. The allocated costs of a single allocation month may involve orders or bills in different billing cycles. If a historical allocated amount is incorrect, the historical allocated costs need to be adjusted. As a result, the allocated costs displayed for a single allocation month may be different at different time points.
        
        @param request: DescribeProductAmortizedCostByAmortizationPeriodRequest
        @return: DescribeProductAmortizedCostByAmortizationPeriodResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_product_amortized_cost_by_amortization_period_with_options(request, runtime)

    async def describe_product_amortized_cost_by_amortization_period_async(
        self,
        request: bss_open_api_20171214_models.DescribeProductAmortizedCostByAmortizationPeriodRequest,
    ) -> bss_open_api_20171214_models.DescribeProductAmortizedCostByAmortizationPeriodResponse:
        """
        You can view and export the allocated costs of the current month after 10:00 on the fourth day of the next month. The allocated costs of a single allocation month may involve orders or bills in different billing cycles. If a historical allocated amount is incorrect, the historical allocated costs need to be adjusted. As a result, the allocated costs displayed for a single allocation month may be different at different time points.
        
        @param request: DescribeProductAmortizedCostByAmortizationPeriodRequest
        @return: DescribeProductAmortizedCostByAmortizationPeriodResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_product_amortized_cost_by_amortization_period_with_options_async(request, runtime)

    def describe_product_amortized_cost_by_consume_period_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeProductAmortizedCostByConsumePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeProductAmortizedCostByConsumePeriodResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amortization_period_filter):
            body['AmortizationPeriodFilter'] = request.amortization_period_filter
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProductAmortizedCostByConsumePeriod',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeProductAmortizedCostByConsumePeriodResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_product_amortized_cost_by_consume_period_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeProductAmortizedCostByConsumePeriodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeProductAmortizedCostByConsumePeriodResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amortization_period_filter):
            body['AmortizationPeriodFilter'] = request.amortization_period_filter
        if not UtilClient.is_unset(request.bill_owner_id_list):
            body['BillOwnerIdList'] = request.bill_owner_id_list
        if not UtilClient.is_unset(request.bill_user_id_list):
            body['BillUserIdList'] = request.bill_user_id_list
        if not UtilClient.is_unset(request.billing_cycle):
            body['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.cost_unit_code):
            body['CostUnitCode'] = request.cost_unit_code
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.product_code):
            body['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_detail):
            body['ProductDetail'] = request.product_detail
        if not UtilClient.is_unset(request.subscription_type):
            body['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeProductAmortizedCostByConsumePeriod',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeProductAmortizedCostByConsumePeriodResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_product_amortized_cost_by_consume_period(
        self,
        request: bss_open_api_20171214_models.DescribeProductAmortizedCostByConsumePeriodRequest,
    ) -> bss_open_api_20171214_models.DescribeProductAmortizedCostByConsumePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_product_amortized_cost_by_consume_period_with_options(request, runtime)

    async def describe_product_amortized_cost_by_consume_period_async(
        self,
        request: bss_open_api_20171214_models.DescribeProductAmortizedCostByConsumePeriodRequest,
    ) -> bss_open_api_20171214_models.DescribeProductAmortizedCostByConsumePeriodResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_product_amortized_cost_by_consume_period_with_options_async(request, runtime)

    def describe_resource_coverage_detail_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeResourceCoverageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeResourceCoverageDetailResponse:
        """
        The amount of the resources deducted from a deduction plan.
        
        @param request: DescribeResourceCoverageDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceCoverageDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceCoverageDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourceCoverageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_coverage_detail_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeResourceCoverageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeResourceCoverageDetailResponse:
        """
        The amount of the resources deducted from a deduction plan.
        
        @param request: DescribeResourceCoverageDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceCoverageDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceCoverageDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourceCoverageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_coverage_detail(
        self,
        request: bss_open_api_20171214_models.DescribeResourceCoverageDetailRequest,
    ) -> bss_open_api_20171214_models.DescribeResourceCoverageDetailResponse:
        """
        The amount of the resources deducted from a deduction plan.
        
        @param request: DescribeResourceCoverageDetailRequest
        @return: DescribeResourceCoverageDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_coverage_detail_with_options(request, runtime)

    async def describe_resource_coverage_detail_async(
        self,
        request: bss_open_api_20171214_models.DescribeResourceCoverageDetailRequest,
    ) -> bss_open_api_20171214_models.DescribeResourceCoverageDetailResponse:
        """
        The amount of the resources deducted from a deduction plan.
        
        @param request: DescribeResourceCoverageDetailRequest
        @return: DescribeResourceCoverageDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_coverage_detail_with_options_async(request, runtime)

    def describe_resource_coverage_total_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeResourceCoverageTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeResourceCoverageTotalResponse:
        """
        Indicates whether the operation was successful.
        
        @param request: DescribeResourceCoverageTotalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceCoverageTotalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceCoverageTotal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourceCoverageTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_coverage_total_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeResourceCoverageTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeResourceCoverageTotalResponse:
        """
        Indicates whether the operation was successful.
        
        @param request: DescribeResourceCoverageTotalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeResourceCoverageTotalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceCoverageTotal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourceCoverageTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_coverage_total(
        self,
        request: bss_open_api_20171214_models.DescribeResourceCoverageTotalRequest,
    ) -> bss_open_api_20171214_models.DescribeResourceCoverageTotalResponse:
        """
        Indicates whether the operation was successful.
        
        @param request: DescribeResourceCoverageTotalRequest
        @return: DescribeResourceCoverageTotalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_coverage_total_with_options(request, runtime)

    async def describe_resource_coverage_total_async(
        self,
        request: bss_open_api_20171214_models.DescribeResourceCoverageTotalRequest,
    ) -> bss_open_api_20171214_models.DescribeResourceCoverageTotalResponse:
        """
        Indicates whether the operation was successful.
        
        @param request: DescribeResourceCoverageTotalRequest
        @return: DescribeResourceCoverageTotalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_coverage_total_with_options_async(request, runtime)

    def describe_resource_package_product_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeResourcePackageProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeResourcePackageProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourcePackageProduct',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourcePackageProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_package_product_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeResourcePackageProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeResourcePackageProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourcePackageProduct',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourcePackageProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_package_product(
        self,
        request: bss_open_api_20171214_models.DescribeResourcePackageProductRequest,
    ) -> bss_open_api_20171214_models.DescribeResourcePackageProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_package_product_with_options(request, runtime)

    async def describe_resource_package_product_async(
        self,
        request: bss_open_api_20171214_models.DescribeResourcePackageProductRequest,
    ) -> bss_open_api_20171214_models.DescribeResourcePackageProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_package_product_with_options_async(request, runtime)

    def describe_resource_usage_detail_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeResourceUsageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeResourceUsageDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceUsageDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourceUsageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_usage_detail_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeResourceUsageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeResourceUsageDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceUsageDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourceUsageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_usage_detail(
        self,
        request: bss_open_api_20171214_models.DescribeResourceUsageDetailRequest,
    ) -> bss_open_api_20171214_models.DescribeResourceUsageDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_usage_detail_with_options(request, runtime)

    async def describe_resource_usage_detail_async(
        self,
        request: bss_open_api_20171214_models.DescribeResourceUsageDetailRequest,
    ) -> bss_open_api_20171214_models.DescribeResourceUsageDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_usage_detail_with_options_async(request, runtime)

    def describe_resource_usage_total_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeResourceUsageTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeResourceUsageTotalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceUsageTotal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourceUsageTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_resource_usage_total_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeResourceUsageTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeResourceUsageTotalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeResourceUsageTotal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeResourceUsageTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_resource_usage_total(
        self,
        request: bss_open_api_20171214_models.DescribeResourceUsageTotalRequest,
    ) -> bss_open_api_20171214_models.DescribeResourceUsageTotalResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_usage_total_with_options(request, runtime)

    async def describe_resource_usage_total_async(
        self,
        request: bss_open_api_20171214_models.DescribeResourceUsageTotalRequest,
    ) -> bss_open_api_20171214_models.DescribeResourceUsageTotalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_usage_total_with_options_async(request, runtime)

    def describe_savings_plans_coverage_detail_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansCoverageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansCoverageDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSavingsPlansCoverageDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSavingsPlansCoverageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_savings_plans_coverage_detail_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansCoverageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansCoverageDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSavingsPlansCoverageDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSavingsPlansCoverageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_savings_plans_coverage_detail(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansCoverageDetailRequest,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansCoverageDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_savings_plans_coverage_detail_with_options(request, runtime)

    async def describe_savings_plans_coverage_detail_async(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansCoverageDetailRequest,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansCoverageDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_savings_plans_coverage_detail_with_options_async(request, runtime)

    def describe_savings_plans_coverage_total_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansCoverageTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansCoverageTotalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSavingsPlansCoverageTotal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSavingsPlansCoverageTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_savings_plans_coverage_total_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansCoverageTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansCoverageTotalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSavingsPlansCoverageTotal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSavingsPlansCoverageTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_savings_plans_coverage_total(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansCoverageTotalRequest,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansCoverageTotalResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_savings_plans_coverage_total_with_options(request, runtime)

    async def describe_savings_plans_coverage_total_async(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansCoverageTotalRequest,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansCoverageTotalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_savings_plans_coverage_total_with_options_async(request, runtime)

    def describe_savings_plans_usage_detail_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansUsageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansUsageDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSavingsPlansUsageDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSavingsPlansUsageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_savings_plans_usage_detail_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansUsageDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansUsageDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        if not UtilClient.is_unset(request.token):
            query['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSavingsPlansUsageDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSavingsPlansUsageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_savings_plans_usage_detail(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansUsageDetailRequest,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansUsageDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_savings_plans_usage_detail_with_options(request, runtime)

    async def describe_savings_plans_usage_detail_async(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansUsageDetailRequest,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansUsageDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_savings_plans_usage_detail_with_options_async(request, runtime)

    def describe_savings_plans_usage_total_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansUsageTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansUsageTotalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSavingsPlansUsageTotal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSavingsPlansUsageTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_savings_plans_usage_total_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansUsageTotalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansUsageTotalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.end_period):
            query['EndPeriod'] = request.end_period
        if not UtilClient.is_unset(request.period_type):
            query['PeriodType'] = request.period_type
        if not UtilClient.is_unset(request.start_period):
            query['StartPeriod'] = request.start_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSavingsPlansUsageTotal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSavingsPlansUsageTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_savings_plans_usage_total(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansUsageTotalRequest,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansUsageTotalResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_savings_plans_usage_total_with_options(request, runtime)

    async def describe_savings_plans_usage_total_async(
        self,
        request: bss_open_api_20171214_models.DescribeSavingsPlansUsageTotalRequest,
    ) -> bss_open_api_20171214_models.DescribeSavingsPlansUsageTotalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_savings_plans_usage_total_with_options_async(request, runtime)

    def describe_split_item_bill_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeSplitItemBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeSplitItemBillResponse:
        """
        The code of the service.
        
        @param request: DescribeSplitItemBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSplitItemBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceID'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.split_item_id):
            query['SplitItemID'] = request.split_item_id
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSplitItemBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSplitItemBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_split_item_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeSplitItemBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeSplitItemBillResponse:
        """
        The code of the service.
        
        @param request: DescribeSplitItemBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSplitItemBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceID'] = request.instance_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.split_item_id):
            query['SplitItemID'] = request.split_item_id
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not UtilClient.is_unset(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSplitItemBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.DescribeSplitItemBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_split_item_bill(
        self,
        request: bss_open_api_20171214_models.DescribeSplitItemBillRequest,
    ) -> bss_open_api_20171214_models.DescribeSplitItemBillResponse:
        """
        The code of the service.
        
        @param request: DescribeSplitItemBillRequest
        @return: DescribeSplitItemBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_split_item_bill_with_options(request, runtime)

    async def describe_split_item_bill_async(
        self,
        request: bss_open_api_20171214_models.DescribeSplitItemBillRequest,
    ) -> bss_open_api_20171214_models.DescribeSplitItemBillResponse:
        """
        The code of the service.
        
        @param request: DescribeSplitItemBillRequest
        @return: DescribeSplitItemBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_split_item_bill_with_options_async(request, runtime)

    def enable_bill_generation_with_options(
        self,
        request: bss_open_api_20171214_models.EnableBillGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.EnableBillGenerationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBillGeneration',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.EnableBillGenerationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_bill_generation_with_options_async(
        self,
        request: bss_open_api_20171214_models.EnableBillGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.EnableBillGenerationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBillGeneration',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.EnableBillGenerationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_bill_generation(
        self,
        request: bss_open_api_20171214_models.EnableBillGenerationRequest,
    ) -> bss_open_api_20171214_models.EnableBillGenerationResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_bill_generation_with_options(request, runtime)

    async def enable_bill_generation_async(
        self,
        request: bss_open_api_20171214_models.EnableBillGenerationRequest,
    ) -> bss_open_api_20171214_models.EnableBillGenerationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_bill_generation_with_options_async(request, runtime)

    def get_account_relation_with_options(
        self,
        request: bss_open_api_20171214_models.GetAccountRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetAccountRelationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetAccountRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_relation_with_options_async(
        self,
        request: bss_open_api_20171214_models.GetAccountRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetAccountRelationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetAccountRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_relation(
        self,
        request: bss_open_api_20171214_models.GetAccountRelationRequest,
    ) -> bss_open_api_20171214_models.GetAccountRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_relation_with_options(request, runtime)

    async def get_account_relation_async(
        self,
        request: bss_open_api_20171214_models.GetAccountRelationRequest,
    ) -> bss_open_api_20171214_models.GetAccountRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_relation_with_options_async(request, runtime)

    def get_customer_account_info_with_options(
        self,
        request: bss_open_api_20171214_models.GetCustomerAccountInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetCustomerAccountInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomerAccountInfo',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetCustomerAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customer_account_info_with_options_async(
        self,
        request: bss_open_api_20171214_models.GetCustomerAccountInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetCustomerAccountInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomerAccountInfo',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetCustomerAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customer_account_info(
        self,
        request: bss_open_api_20171214_models.GetCustomerAccountInfoRequest,
    ) -> bss_open_api_20171214_models.GetCustomerAccountInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_customer_account_info_with_options(request, runtime)

    async def get_customer_account_info_async(
        self,
        request: bss_open_api_20171214_models.GetCustomerAccountInfoRequest,
    ) -> bss_open_api_20171214_models.GetCustomerAccountInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_customer_account_info_with_options_async(request, runtime)

    def get_customer_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetCustomerListResponse:
        """
        The system queries the IDs of customers of a VNO based on the AccessKey pair used in the request.
        
        @param request: GetCustomerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomerListResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCustomerList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetCustomerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customer_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetCustomerListResponse:
        """
        The system queries the IDs of customers of a VNO based on the AccessKey pair used in the request.
        
        @param request: GetCustomerListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomerListResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCustomerList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetCustomerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customer_list(self) -> bss_open_api_20171214_models.GetCustomerListResponse:
        """
        The system queries the IDs of customers of a VNO based on the AccessKey pair used in the request.
        
        @return: GetCustomerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_customer_list_with_options(runtime)

    async def get_customer_list_async(self) -> bss_open_api_20171214_models.GetCustomerListResponse:
        """
        The system queries the IDs of customers of a VNO based on the AccessKey pair used in the request.
        
        @return: GetCustomerListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_customer_list_with_options_async(runtime)

    def get_order_detail_with_options(
        self,
        request: bss_open_api_20171214_models.GetOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetOrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_order_detail_with_options_async(
        self,
        request: bss_open_api_20171214_models.GetOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetOrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetOrderDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_order_detail(
        self,
        request: bss_open_api_20171214_models.GetOrderDetailRequest,
    ) -> bss_open_api_20171214_models.GetOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_order_detail_with_options(request, runtime)

    async def get_order_detail_async(
        self,
        request: bss_open_api_20171214_models.GetOrderDetailRequest,
    ) -> bss_open_api_20171214_models.GetOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_order_detail_with_options_async(request, runtime)

    def get_pay_as_you_go_price_with_options(
        self,
        request: bss_open_api_20171214_models.GetPayAsYouGoPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetPayAsYouGoPriceResponse:
        """
        ### Usage notes
        1.  Call the QueryProductList operation to obtain the code of the service. For more information, see [QueryProductList](~~95984~~).
        2.  Call the DescribePricingModule operation to obtain the configuration parameters of the service. For more information, see [DescribePricingModule](~~96469~~).
        3.  Call the GetPayAsYouGoPrice operation to obtain the pay-as-you-go price of the service based on the returned configuration parameters.
        
        @param request: GetPayAsYouGoPriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPayAsYouGoPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPayAsYouGoPrice',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetPayAsYouGoPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pay_as_you_go_price_with_options_async(
        self,
        request: bss_open_api_20171214_models.GetPayAsYouGoPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetPayAsYouGoPriceResponse:
        """
        ### Usage notes
        1.  Call the QueryProductList operation to obtain the code of the service. For more information, see [QueryProductList](~~95984~~).
        2.  Call the DescribePricingModule operation to obtain the configuration parameters of the service. For more information, see [DescribePricingModule](~~96469~~).
        3.  Call the GetPayAsYouGoPrice operation to obtain the pay-as-you-go price of the service based on the returned configuration parameters.
        
        @param request: GetPayAsYouGoPriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPayAsYouGoPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPayAsYouGoPrice',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetPayAsYouGoPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pay_as_you_go_price(
        self,
        request: bss_open_api_20171214_models.GetPayAsYouGoPriceRequest,
    ) -> bss_open_api_20171214_models.GetPayAsYouGoPriceResponse:
        """
        ### Usage notes
        1.  Call the QueryProductList operation to obtain the code of the service. For more information, see [QueryProductList](~~95984~~).
        2.  Call the DescribePricingModule operation to obtain the configuration parameters of the service. For more information, see [DescribePricingModule](~~96469~~).
        3.  Call the GetPayAsYouGoPrice operation to obtain the pay-as-you-go price of the service based on the returned configuration parameters.
        
        @param request: GetPayAsYouGoPriceRequest
        @return: GetPayAsYouGoPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_pay_as_you_go_price_with_options(request, runtime)

    async def get_pay_as_you_go_price_async(
        self,
        request: bss_open_api_20171214_models.GetPayAsYouGoPriceRequest,
    ) -> bss_open_api_20171214_models.GetPayAsYouGoPriceResponse:
        """
        ### Usage notes
        1.  Call the QueryProductList operation to obtain the code of the service. For more information, see [QueryProductList](~~95984~~).
        2.  Call the DescribePricingModule operation to obtain the configuration parameters of the service. For more information, see [DescribePricingModule](~~96469~~).
        3.  Call the GetPayAsYouGoPrice operation to obtain the pay-as-you-go price of the service based on the returned configuration parameters.
        
        @param request: GetPayAsYouGoPriceRequest
        @return: GetPayAsYouGoPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_pay_as_you_go_price_with_options_async(request, runtime)

    def get_resource_package_price_with_options(
        self,
        request: bss_open_api_20171214_models.GetResourcePackagePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetResourcePackagePriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourcePackagePrice',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetResourcePackagePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_package_price_with_options_async(
        self,
        request: bss_open_api_20171214_models.GetResourcePackagePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetResourcePackagePriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.package_type):
            query['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourcePackagePrice',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetResourcePackagePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_package_price(
        self,
        request: bss_open_api_20171214_models.GetResourcePackagePriceRequest,
    ) -> bss_open_api_20171214_models.GetResourcePackagePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_package_price_with_options(request, runtime)

    async def get_resource_package_price_async(
        self,
        request: bss_open_api_20171214_models.GetResourcePackagePriceRequest,
    ) -> bss_open_api_20171214_models.GetResourcePackagePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_package_price_with_options_async(request, runtime)

    def get_subscription_price_with_options(
        self,
        request: bss_open_api_20171214_models.GetSubscriptionPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetSubscriptionPriceResponse:
        """
        1.  Call the QueryProductList operation to obtain the code of the service. For more information, see [QueryProductList](~~95984~~).
        2.  Call the DescribePricingModule operation to obtain the configuration parameters of the service. For more information, see [DescribePricingModule](~~96469~~).
        3.  Call the GetSubscriptionPrice operation to obtain the pricing of the service based on the returned configuration parameters.
        
        @param request: GetSubscriptionPriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubscriptionPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.service_period_quantity):
            query['ServicePeriodQuantity'] = request.service_period_quantity
        if not UtilClient.is_unset(request.service_period_unit):
            query['ServicePeriodUnit'] = request.service_period_unit
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubscriptionPrice',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetSubscriptionPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subscription_price_with_options_async(
        self,
        request: bss_open_api_20171214_models.GetSubscriptionPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetSubscriptionPriceResponse:
        """
        1.  Call the QueryProductList operation to obtain the code of the service. For more information, see [QueryProductList](~~95984~~).
        2.  Call the DescribePricingModule operation to obtain the configuration parameters of the service. For more information, see [DescribePricingModule](~~96469~~).
        3.  Call the GetSubscriptionPrice operation to obtain the pricing of the service based on the returned configuration parameters.
        
        @param request: GetSubscriptionPriceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSubscriptionPriceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_list):
            query['ModuleList'] = request.module_list
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.service_period_quantity):
            query['ServicePeriodQuantity'] = request.service_period_quantity
        if not UtilClient.is_unset(request.service_period_unit):
            query['ServicePeriodUnit'] = request.service_period_unit
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSubscriptionPrice',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.GetSubscriptionPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subscription_price(
        self,
        request: bss_open_api_20171214_models.GetSubscriptionPriceRequest,
    ) -> bss_open_api_20171214_models.GetSubscriptionPriceResponse:
        """
        1.  Call the QueryProductList operation to obtain the code of the service. For more information, see [QueryProductList](~~95984~~).
        2.  Call the DescribePricingModule operation to obtain the configuration parameters of the service. For more information, see [DescribePricingModule](~~96469~~).
        3.  Call the GetSubscriptionPrice operation to obtain the pricing of the service based on the returned configuration parameters.
        
        @param request: GetSubscriptionPriceRequest
        @return: GetSubscriptionPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_subscription_price_with_options(request, runtime)

    async def get_subscription_price_async(
        self,
        request: bss_open_api_20171214_models.GetSubscriptionPriceRequest,
    ) -> bss_open_api_20171214_models.GetSubscriptionPriceResponse:
        """
        1.  Call the QueryProductList operation to obtain the code of the service. For more information, see [QueryProductList](~~95984~~).
        2.  Call the DescribePricingModule operation to obtain the configuration parameters of the service. For more information, see [DescribePricingModule](~~96469~~).
        3.  Call the GetSubscriptionPrice operation to obtain the pricing of the service based on the returned configuration parameters.
        
        @param request: GetSubscriptionPriceRequest
        @return: GetSubscriptionPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_subscription_price_with_options_async(request, runtime)

    def inquiry_price_refund_instance_with_options(
        self,
        request: bss_open_api_20171214_models.InquiryPriceRefundInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.InquiryPriceRefundInstanceResponse:
        """
        1.  *Check the information about unsubscription and confirm the unsubscription terms and refundable amount. The resource that is unsubscribed cannot be restored.**\
        2.  Refunds are applicable only for the actual paid amount. Vouchers used for the purchase are non-refundable.
        3.  For more information, see [Rules for unsubscribing from resources](https://help.aliyun.com/knowledge_detail/116043.html?spm=a2c81.e1d666e.app.2.62ae11271Kd6iM).
        
        @param request: InquiryPriceRefundInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InquiryPriceRefundInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InquiryPriceRefundInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.InquiryPriceRefundInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def inquiry_price_refund_instance_with_options_async(
        self,
        request: bss_open_api_20171214_models.InquiryPriceRefundInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.InquiryPriceRefundInstanceResponse:
        """
        1.  *Check the information about unsubscription and confirm the unsubscription terms and refundable amount. The resource that is unsubscribed cannot be restored.**\
        2.  Refunds are applicable only for the actual paid amount. Vouchers used for the purchase are non-refundable.
        3.  For more information, see [Rules for unsubscribing from resources](https://help.aliyun.com/knowledge_detail/116043.html?spm=a2c81.e1d666e.app.2.62ae11271Kd6iM).
        
        @param request: InquiryPriceRefundInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InquiryPriceRefundInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InquiryPriceRefundInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.InquiryPriceRefundInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def inquiry_price_refund_instance(
        self,
        request: bss_open_api_20171214_models.InquiryPriceRefundInstanceRequest,
    ) -> bss_open_api_20171214_models.InquiryPriceRefundInstanceResponse:
        """
        1.  *Check the information about unsubscription and confirm the unsubscription terms and refundable amount. The resource that is unsubscribed cannot be restored.**\
        2.  Refunds are applicable only for the actual paid amount. Vouchers used for the purchase are non-refundable.
        3.  For more information, see [Rules for unsubscribing from resources](https://help.aliyun.com/knowledge_detail/116043.html?spm=a2c81.e1d666e.app.2.62ae11271Kd6iM).
        
        @param request: InquiryPriceRefundInstanceRequest
        @return: InquiryPriceRefundInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.inquiry_price_refund_instance_with_options(request, runtime)

    async def inquiry_price_refund_instance_async(
        self,
        request: bss_open_api_20171214_models.InquiryPriceRefundInstanceRequest,
    ) -> bss_open_api_20171214_models.InquiryPriceRefundInstanceResponse:
        """
        1.  *Check the information about unsubscription and confirm the unsubscription terms and refundable amount. The resource that is unsubscribed cannot be restored.**\
        2.  Refunds are applicable only for the actual paid amount. Vouchers used for the purchase are non-refundable.
        3.  For more information, see [Rules for unsubscribing from resources](https://help.aliyun.com/knowledge_detail/116043.html?spm=a2c81.e1d666e.app.2.62ae11271Kd6iM).
        
        @param request: InquiryPriceRefundInstanceRequest
        @return: InquiryPriceRefundInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.inquiry_price_refund_instance_with_options_async(request, runtime)

    def modify_account_relation_with_options(
        self,
        request: bss_open_api_20171214_models.ModifyAccountRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ModifyAccountRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_nick):
            query['ChildNick'] = request.child_nick
        if not UtilClient.is_unset(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not UtilClient.is_unset(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not UtilClient.is_unset(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not UtilClient.is_unset(request.relation_id):
            query['RelationId'] = request.relation_id
        if not UtilClient.is_unset(request.relation_operation):
            query['RelationOperation'] = request.relation_operation
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.role_codes):
            query['RoleCodes'] = request.role_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ModifyAccountRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_relation_with_options_async(
        self,
        request: bss_open_api_20171214_models.ModifyAccountRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ModifyAccountRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_nick):
            query['ChildNick'] = request.child_nick
        if not UtilClient.is_unset(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not UtilClient.is_unset(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not UtilClient.is_unset(request.permission_codes):
            query['PermissionCodes'] = request.permission_codes
        if not UtilClient.is_unset(request.relation_id):
            query['RelationId'] = request.relation_id
        if not UtilClient.is_unset(request.relation_operation):
            query['RelationOperation'] = request.relation_operation
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.role_codes):
            query['RoleCodes'] = request.role_codes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ModifyAccountRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_relation(
        self,
        request: bss_open_api_20171214_models.ModifyAccountRelationRequest,
    ) -> bss_open_api_20171214_models.ModifyAccountRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_relation_with_options(request, runtime)

    async def modify_account_relation_async(
        self,
        request: bss_open_api_20171214_models.ModifyAccountRelationRequest,
    ) -> bss_open_api_20171214_models.ModifyAccountRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_relation_with_options_async(request, runtime)

    def modify_cost_unit_with_options(
        self,
        request: bss_open_api_20171214_models.ModifyCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ModifyCostUnitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.unit_entity_list):
            query['UnitEntityList'] = request.unit_entity_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCostUnit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ModifyCostUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cost_unit_with_options_async(
        self,
        request: bss_open_api_20171214_models.ModifyCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ModifyCostUnitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.unit_entity_list):
            query['UnitEntityList'] = request.unit_entity_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCostUnit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ModifyCostUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cost_unit(
        self,
        request: bss_open_api_20171214_models.ModifyCostUnitRequest,
    ) -> bss_open_api_20171214_models.ModifyCostUnitResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cost_unit_with_options(request, runtime)

    async def modify_cost_unit_async(
        self,
        request: bss_open_api_20171214_models.ModifyCostUnitRequest,
    ) -> bss_open_api_20171214_models.ModifyCostUnitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cost_unit_with_options_async(request, runtime)

    def modify_instance_with_options(
        self,
        request: bss_open_api_20171214_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter):
            query['Parameter'] = request.parameter
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ModifyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: bss_open_api_20171214_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.modify_type):
            query['ModifyType'] = request.modify_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parameter):
            query['Parameter'] = request.parameter
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ModifyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance(
        self,
        request: bss_open_api_20171214_models.ModifyInstanceRequest,
    ) -> bss_open_api_20171214_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    async def modify_instance_async(
        self,
        request: bss_open_api_20171214_models.ModifyInstanceRequest,
    ) -> bss_open_api_20171214_models.ModifyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_with_options_async(request, runtime)

    def query_account_balance_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAccountBalanceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryAccountBalance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAccountBalanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_balance_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAccountBalanceResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryAccountBalance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAccountBalanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_balance(self) -> bss_open_api_20171214_models.QueryAccountBalanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_account_balance_with_options(runtime)

    async def query_account_balance_async(self) -> bss_open_api_20171214_models.QueryAccountBalanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_account_balance_with_options_async(runtime)

    def query_account_bill_with_options(
        self,
        request: bss_open_api_20171214_models.QueryAccountBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAccountBillResponse:
        """
        ##
        Before you call this operation, take note of the following items:
        *   Account bills are summarized based on instance bills. In most cases, the account bills do not include the data generated on the last day of the specified period.
        *   You can query the data generated in June 2020 or later for Cloud Communications services. However, the query results do not include the data of Alibaba Cloud Domains.
        
        @param request: QueryAccountBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccountBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.is_group_by_product):
            query['IsGroupByProduct'] = request.is_group_by_product
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerID'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccountBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAccountBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryAccountBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAccountBillResponse:
        """
        ##
        Before you call this operation, take note of the following items:
        *   Account bills are summarized based on instance bills. In most cases, the account bills do not include the data generated on the last day of the specified period.
        *   You can query the data generated in June 2020 or later for Cloud Communications services. However, the query results do not include the data of Alibaba Cloud Domains.
        
        @param request: QueryAccountBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAccountBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.is_group_by_product):
            query['IsGroupByProduct'] = request.is_group_by_product
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerID'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccountBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAccountBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_bill(
        self,
        request: bss_open_api_20171214_models.QueryAccountBillRequest,
    ) -> bss_open_api_20171214_models.QueryAccountBillResponse:
        """
        ##
        Before you call this operation, take note of the following items:
        *   Account bills are summarized based on instance bills. In most cases, the account bills do not include the data generated on the last day of the specified period.
        *   You can query the data generated in June 2020 or later for Cloud Communications services. However, the query results do not include the data of Alibaba Cloud Domains.
        
        @param request: QueryAccountBillRequest
        @return: QueryAccountBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_account_bill_with_options(request, runtime)

    async def query_account_bill_async(
        self,
        request: bss_open_api_20171214_models.QueryAccountBillRequest,
    ) -> bss_open_api_20171214_models.QueryAccountBillResponse:
        """
        ##
        Before you call this operation, take note of the following items:
        *   Account bills are summarized based on instance bills. In most cases, the account bills do not include the data generated on the last day of the specified period.
        *   You can query the data generated in June 2020 or later for Cloud Communications services. However, the query results do not include the data of Alibaba Cloud Domains.
        
        @param request: QueryAccountBillRequest
        @return: QueryAccountBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_account_bill_with_options_async(request, runtime)

    def query_account_transaction_details_with_options(
        self,
        request: bss_open_api_20171214_models.QueryAccountTransactionDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAccountTransactionDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.record_id):
            query['RecordID'] = request.record_id
        if not UtilClient.is_unset(request.transaction_channel):
            query['TransactionChannel'] = request.transaction_channel
        if not UtilClient.is_unset(request.transaction_channel_sn):
            query['TransactionChannelSN'] = request.transaction_channel_sn
        if not UtilClient.is_unset(request.transaction_number):
            query['TransactionNumber'] = request.transaction_number
        if not UtilClient.is_unset(request.transaction_type):
            query['TransactionType'] = request.transaction_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccountTransactionDetails',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAccountTransactionDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_transaction_details_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryAccountTransactionDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAccountTransactionDetailsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.record_id):
            query['RecordID'] = request.record_id
        if not UtilClient.is_unset(request.transaction_channel):
            query['TransactionChannel'] = request.transaction_channel
        if not UtilClient.is_unset(request.transaction_channel_sn):
            query['TransactionChannelSN'] = request.transaction_channel_sn
        if not UtilClient.is_unset(request.transaction_number):
            query['TransactionNumber'] = request.transaction_number
        if not UtilClient.is_unset(request.transaction_type):
            query['TransactionType'] = request.transaction_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccountTransactionDetails',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAccountTransactionDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_transaction_details(
        self,
        request: bss_open_api_20171214_models.QueryAccountTransactionDetailsRequest,
    ) -> bss_open_api_20171214_models.QueryAccountTransactionDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_account_transaction_details_with_options(request, runtime)

    async def query_account_transaction_details_async(
        self,
        request: bss_open_api_20171214_models.QueryAccountTransactionDetailsRequest,
    ) -> bss_open_api_20171214_models.QueryAccountTransactionDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_account_transaction_details_with_options_async(request, runtime)

    def query_account_transactions_with_options(
        self,
        request: bss_open_api_20171214_models.QueryAccountTransactionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAccountTransactionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.record_id):
            query['RecordID'] = request.record_id
        if not UtilClient.is_unset(request.transaction_channel):
            query['TransactionChannel'] = request.transaction_channel
        if not UtilClient.is_unset(request.transaction_channel_sn):
            query['TransactionChannelSN'] = request.transaction_channel_sn
        if not UtilClient.is_unset(request.transaction_flow):
            query['TransactionFlow'] = request.transaction_flow
        if not UtilClient.is_unset(request.transaction_number):
            query['TransactionNumber'] = request.transaction_number
        if not UtilClient.is_unset(request.transaction_type):
            query['TransactionType'] = request.transaction_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccountTransactions',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAccountTransactionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_account_transactions_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryAccountTransactionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAccountTransactionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.record_id):
            query['RecordID'] = request.record_id
        if not UtilClient.is_unset(request.transaction_channel):
            query['TransactionChannel'] = request.transaction_channel
        if not UtilClient.is_unset(request.transaction_channel_sn):
            query['TransactionChannelSN'] = request.transaction_channel_sn
        if not UtilClient.is_unset(request.transaction_flow):
            query['TransactionFlow'] = request.transaction_flow
        if not UtilClient.is_unset(request.transaction_number):
            query['TransactionNumber'] = request.transaction_number
        if not UtilClient.is_unset(request.transaction_type):
            query['TransactionType'] = request.transaction_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAccountTransactions',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAccountTransactionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_account_transactions(
        self,
        request: bss_open_api_20171214_models.QueryAccountTransactionsRequest,
    ) -> bss_open_api_20171214_models.QueryAccountTransactionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_account_transactions_with_options(request, runtime)

    async def query_account_transactions_async(
        self,
        request: bss_open_api_20171214_models.QueryAccountTransactionsRequest,
    ) -> bss_open_api_20171214_models.QueryAccountTransactionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_account_transactions_with_options_async(request, runtime)

    def query_available_instances_with_options(
        self,
        request: bss_open_api_20171214_models.QueryAvailableInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAvailableInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.end_time_end):
            query['EndTimeEnd'] = request.end_time_end
        if not UtilClient.is_unset(request.end_time_start):
            query['EndTimeStart'] = request.end_time_start
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIDs'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvailableInstances',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAvailableInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_available_instances_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryAvailableInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAvailableInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.end_time_end):
            query['EndTimeEnd'] = request.end_time_end
        if not UtilClient.is_unset(request.end_time_start):
            query['EndTimeStart'] = request.end_time_start
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIDs'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAvailableInstances',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryAvailableInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_available_instances(
        self,
        request: bss_open_api_20171214_models.QueryAvailableInstancesRequest,
    ) -> bss_open_api_20171214_models.QueryAvailableInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_available_instances_with_options(request, runtime)

    async def query_available_instances_async(
        self,
        request: bss_open_api_20171214_models.QueryAvailableInstancesRequest,
    ) -> bss_open_api_20171214_models.QueryAvailableInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_available_instances_with_options_async(request, runtime)

    def query_bill_with_options(
        self,
        request: bss_open_api_20171214_models.QueryBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryBillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.is_display_local_currency):
            query['IsDisplayLocalCurrency'] = request.is_display_local_currency
        if not UtilClient.is_unset(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryBillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.is_display_local_currency):
            query['IsDisplayLocalCurrency'] = request.is_display_local_currency
        if not UtilClient.is_unset(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_bill(
        self,
        request: bss_open_api_20171214_models.QueryBillRequest,
    ) -> bss_open_api_20171214_models.QueryBillResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_bill_with_options(request, runtime)

    async def query_bill_async(
        self,
        request: bss_open_api_20171214_models.QueryBillRequest,
    ) -> bss_open_api_20171214_models.QueryBillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_bill_with_options_async(request, runtime)

    def query_bill_overview_with_options(
        self,
        request: bss_open_api_20171214_models.QueryBillOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryBillOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBillOverview',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryBillOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_bill_overview_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryBillOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryBillOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBillOverview',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryBillOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_bill_overview(
        self,
        request: bss_open_api_20171214_models.QueryBillOverviewRequest,
    ) -> bss_open_api_20171214_models.QueryBillOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_bill_overview_with_options(request, runtime)

    async def query_bill_overview_async(
        self,
        request: bss_open_api_20171214_models.QueryBillOverviewRequest,
    ) -> bss_open_api_20171214_models.QueryBillOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_bill_overview_with_options_async(request, runtime)

    def query_bill_to_osssubscription_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryBillToOSSSubscriptionResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryBillToOSSSubscription',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryBillToOSSSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_bill_to_osssubscription_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryBillToOSSSubscriptionResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryBillToOSSSubscription',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryBillToOSSSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_bill_to_osssubscription(self) -> bss_open_api_20171214_models.QueryBillToOSSSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_bill_to_osssubscription_with_options(runtime)

    async def query_bill_to_osssubscription_async(self) -> bss_open_api_20171214_models.QueryBillToOSSSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_bill_to_osssubscription_with_options_async(runtime)

    def query_cash_coupons_with_options(
        self,
        request: bss_open_api_20171214_models.QueryCashCouponsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCashCouponsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_or_not):
            query['EffectiveOrNot'] = request.effective_or_not
        if not UtilClient.is_unset(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not UtilClient.is_unset(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCashCoupons',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCashCouponsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cash_coupons_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryCashCouponsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCashCouponsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_or_not):
            query['EffectiveOrNot'] = request.effective_or_not
        if not UtilClient.is_unset(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not UtilClient.is_unset(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCashCoupons',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCashCouponsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cash_coupons(
        self,
        request: bss_open_api_20171214_models.QueryCashCouponsRequest,
    ) -> bss_open_api_20171214_models.QueryCashCouponsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cash_coupons_with_options(request, runtime)

    async def query_cash_coupons_async(
        self,
        request: bss_open_api_20171214_models.QueryCashCouponsRequest,
    ) -> bss_open_api_20171214_models.QueryCashCouponsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cash_coupons_with_options_async(request, runtime)

    def query_commodity_list_with_options(
        self,
        request: bss_open_api_20171214_models.QueryCommodityListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCommodityListResponse:
        """
        You can call this operation to query the information about a service based on the service code.
        
        @param request: QueryCommodityListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCommodityListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCommodityList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCommodityListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_commodity_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryCommodityListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCommodityListResponse:
        """
        You can call this operation to query the information about a service based on the service code.
        
        @param request: QueryCommodityListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCommodityListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCommodityList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCommodityListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_commodity_list(
        self,
        request: bss_open_api_20171214_models.QueryCommodityListRequest,
    ) -> bss_open_api_20171214_models.QueryCommodityListResponse:
        """
        You can call this operation to query the information about a service based on the service code.
        
        @param request: QueryCommodityListRequest
        @return: QueryCommodityListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_commodity_list_with_options(request, runtime)

    async def query_commodity_list_async(
        self,
        request: bss_open_api_20171214_models.QueryCommodityListRequest,
    ) -> bss_open_api_20171214_models.QueryCommodityListResponse:
        """
        You can call this operation to query the information about a service based on the service code.
        
        @param request: QueryCommodityListRequest
        @return: QueryCommodityListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_commodity_list_with_options_async(request, runtime)

    def query_cost_unit_with_options(
        self,
        request: bss_open_api_20171214_models.QueryCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCostUnitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_unit_id):
            query['ParentUnitId'] = request.parent_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCostUnit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCostUnitResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cost_unit_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCostUnitResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_unit_id):
            query['ParentUnitId'] = request.parent_unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCostUnit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCostUnitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cost_unit(
        self,
        request: bss_open_api_20171214_models.QueryCostUnitRequest,
    ) -> bss_open_api_20171214_models.QueryCostUnitResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cost_unit_with_options(request, runtime)

    async def query_cost_unit_async(
        self,
        request: bss_open_api_20171214_models.QueryCostUnitRequest,
    ) -> bss_open_api_20171214_models.QueryCostUnitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cost_unit_with_options_async(request, runtime)

    def query_cost_unit_resource_with_options(
        self,
        request: bss_open_api_20171214_models.QueryCostUnitResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCostUnitResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.unit_id):
            query['UnitId'] = request.unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCostUnitResource',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCostUnitResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cost_unit_resource_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryCostUnitResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCostUnitResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_uid):
            query['OwnerUid'] = request.owner_uid
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.unit_id):
            query['UnitId'] = request.unit_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCostUnitResource',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCostUnitResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cost_unit_resource(
        self,
        request: bss_open_api_20171214_models.QueryCostUnitResourceRequest,
    ) -> bss_open_api_20171214_models.QueryCostUnitResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cost_unit_resource_with_options(request, runtime)

    async def query_cost_unit_resource_async(
        self,
        request: bss_open_api_20171214_models.QueryCostUnitResourceRequest,
    ) -> bss_open_api_20171214_models.QueryCostUnitResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cost_unit_resource_with_options_async(request, runtime)

    def query_customer_address_list_with_options(
        self,
        request: bss_open_api_20171214_models.QueryCustomerAddressListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCustomerAddressListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCustomerAddressList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCustomerAddressListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_customer_address_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryCustomerAddressListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCustomerAddressListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCustomerAddressList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryCustomerAddressListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_customer_address_list(
        self,
        request: bss_open_api_20171214_models.QueryCustomerAddressListRequest,
    ) -> bss_open_api_20171214_models.QueryCustomerAddressListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_customer_address_list_with_options(request, runtime)

    async def query_customer_address_list_async(
        self,
        request: bss_open_api_20171214_models.QueryCustomerAddressListRequest,
    ) -> bss_open_api_20171214_models.QueryCustomerAddressListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_customer_address_list_with_options_async(request, runtime)

    def query_dputilization_detail_with_options(
        self,
        request: bss_open_api_20171214_models.QueryDPUtilizationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryDPUtilizationDetailResponse:
        """
        Limits:
        *   Only the usage records within the past year can be queried.
        
        @param request: QueryDPUtilizationDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDPUtilizationDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.deducted_instance_id):
            query['DeductedInstanceId'] = request.deducted_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.include_share):
            query['IncludeShare'] = request.include_share
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.last_token):
            query['LastToken'] = request.last_token
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDPUtilizationDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryDPUtilizationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dputilization_detail_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryDPUtilizationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryDPUtilizationDetailResponse:
        """
        Limits:
        *   Only the usage records within the past year can be queried.
        
        @param request: QueryDPUtilizationDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryDPUtilizationDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.deducted_instance_id):
            query['DeductedInstanceId'] = request.deducted_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.include_share):
            query['IncludeShare'] = request.include_share
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.last_token):
            query['LastToken'] = request.last_token
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.prod_code):
            query['ProdCode'] = request.prod_code
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDPUtilizationDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryDPUtilizationDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dputilization_detail(
        self,
        request: bss_open_api_20171214_models.QueryDPUtilizationDetailRequest,
    ) -> bss_open_api_20171214_models.QueryDPUtilizationDetailResponse:
        """
        Limits:
        *   Only the usage records within the past year can be queried.
        
        @param request: QueryDPUtilizationDetailRequest
        @return: QueryDPUtilizationDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_dputilization_detail_with_options(request, runtime)

    async def query_dputilization_detail_async(
        self,
        request: bss_open_api_20171214_models.QueryDPUtilizationDetailRequest,
    ) -> bss_open_api_20171214_models.QueryDPUtilizationDetailResponse:
        """
        Limits:
        *   Only the usage records within the past year can be queried.
        
        @param request: QueryDPUtilizationDetailRequest
        @return: QueryDPUtilizationDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_dputilization_detail_with_options_async(request, runtime)

    def query_evaluate_list_with_options(
        self,
        request: bss_open_api_20171214_models.QueryEvaluateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryEvaluateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.biz_type_list):
            query['BizTypeList'] = request.biz_type_list
        if not UtilClient.is_unset(request.end_amount):
            query['EndAmount'] = request.end_amount
        if not UtilClient.is_unset(request.end_biz_time):
            query['EndBizTime'] = request.end_biz_time
        if not UtilClient.is_unset(request.end_search_time):
            query['EndSearchTime'] = request.end_search_time
        if not UtilClient.is_unset(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.start_amount):
            query['StartAmount'] = request.start_amount
        if not UtilClient.is_unset(request.start_biz_time):
            query['StartBizTime'] = request.start_biz_time
        if not UtilClient.is_unset(request.start_search_time):
            query['StartSearchTime'] = request.start_search_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEvaluateList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryEvaluateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_evaluate_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryEvaluateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryEvaluateListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_cycle):
            query['BillCycle'] = request.bill_cycle
        if not UtilClient.is_unset(request.biz_type_list):
            query['BizTypeList'] = request.biz_type_list
        if not UtilClient.is_unset(request.end_amount):
            query['EndAmount'] = request.end_amount
        if not UtilClient.is_unset(request.end_biz_time):
            query['EndBizTime'] = request.end_biz_time
        if not UtilClient.is_unset(request.end_search_time):
            query['EndSearchTime'] = request.end_search_time
        if not UtilClient.is_unset(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.start_amount):
            query['StartAmount'] = request.start_amount
        if not UtilClient.is_unset(request.start_biz_time):
            query['StartBizTime'] = request.start_biz_time
        if not UtilClient.is_unset(request.start_search_time):
            query['StartSearchTime'] = request.start_search_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEvaluateList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryEvaluateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_evaluate_list(
        self,
        request: bss_open_api_20171214_models.QueryEvaluateListRequest,
    ) -> bss_open_api_20171214_models.QueryEvaluateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_evaluate_list_with_options(request, runtime)

    async def query_evaluate_list_async(
        self,
        request: bss_open_api_20171214_models.QueryEvaluateListRequest,
    ) -> bss_open_api_20171214_models.QueryEvaluateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_evaluate_list_with_options_async(request, runtime)

    def query_financial_account_info_with_options(
        self,
        request: bss_open_api_20171214_models.QueryFinancialAccountInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryFinancialAccountInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFinancialAccountInfo',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryFinancialAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_financial_account_info_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryFinancialAccountInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryFinancialAccountInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFinancialAccountInfo',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryFinancialAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_financial_account_info(
        self,
        request: bss_open_api_20171214_models.QueryFinancialAccountInfoRequest,
    ) -> bss_open_api_20171214_models.QueryFinancialAccountInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_financial_account_info_with_options(request, runtime)

    async def query_financial_account_info_async(
        self,
        request: bss_open_api_20171214_models.QueryFinancialAccountInfoRequest,
    ) -> bss_open_api_20171214_models.QueryFinancialAccountInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_financial_account_info_with_options_async(request, runtime)

    def query_instance_bill_with_options(
        self,
        request: bss_open_api_20171214_models.QueryInstanceBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryInstanceBillResponse:
        """
        ##
        *   This API operation has been upgraded to DescribeInstanceBill. We recommend that you call the [DescribeInstanceBill](~~209402~~) operation to query the bills of instances or billable items in a billing cycle. You can call the QueryInstanceBill operation to query a maximum of 50,000 data rows in a bill.
        *   Instance bills are generated after bills are split. In most cases, the instance bills do not include data generated on the last day of the specified period.
        *   The instance information changes within a billing cycle. The instance configurations and specifications and the time when the instance was used in the billing cycle are all recorded. For more information, see the corresponding bill details.
        *   You can query the data generated in June 2020 or later for Cloud Communications services, and the data generated in November 2020 or later for Alibaba Cloud Domains.
        
        @param request: QueryInstanceBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInstanceBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.is_billing_item):
            query['IsBillingItem'] = request.is_billing_item
        if not UtilClient.is_unset(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstanceBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryInstanceBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryInstanceBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryInstanceBillResponse:
        """
        ##
        *   This API operation has been upgraded to DescribeInstanceBill. We recommend that you call the [DescribeInstanceBill](~~209402~~) operation to query the bills of instances or billable items in a billing cycle. You can call the QueryInstanceBill operation to query a maximum of 50,000 data rows in a bill.
        *   Instance bills are generated after bills are split. In most cases, the instance bills do not include data generated on the last day of the specified period.
        *   The instance information changes within a billing cycle. The instance configurations and specifications and the time when the instance was used in the billing cycle are all recorded. For more information, see the corresponding bill details.
        *   You can query the data generated in June 2020 or later for Cloud Communications services, and the data generated in November 2020 or later for Alibaba Cloud Domains.
        
        @param request: QueryInstanceBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryInstanceBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.is_billing_item):
            query['IsBillingItem'] = request.is_billing_item
        if not UtilClient.is_unset(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstanceBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryInstanceBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance_bill(
        self,
        request: bss_open_api_20171214_models.QueryInstanceBillRequest,
    ) -> bss_open_api_20171214_models.QueryInstanceBillResponse:
        """
        ##
        *   This API operation has been upgraded to DescribeInstanceBill. We recommend that you call the [DescribeInstanceBill](~~209402~~) operation to query the bills of instances or billable items in a billing cycle. You can call the QueryInstanceBill operation to query a maximum of 50,000 data rows in a bill.
        *   Instance bills are generated after bills are split. In most cases, the instance bills do not include data generated on the last day of the specified period.
        *   The instance information changes within a billing cycle. The instance configurations and specifications and the time when the instance was used in the billing cycle are all recorded. For more information, see the corresponding bill details.
        *   You can query the data generated in June 2020 or later for Cloud Communications services, and the data generated in November 2020 or later for Alibaba Cloud Domains.
        
        @param request: QueryInstanceBillRequest
        @return: QueryInstanceBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_instance_bill_with_options(request, runtime)

    async def query_instance_bill_async(
        self,
        request: bss_open_api_20171214_models.QueryInstanceBillRequest,
    ) -> bss_open_api_20171214_models.QueryInstanceBillResponse:
        """
        ##
        *   This API operation has been upgraded to DescribeInstanceBill. We recommend that you call the [DescribeInstanceBill](~~209402~~) operation to query the bills of instances or billable items in a billing cycle. You can call the QueryInstanceBill operation to query a maximum of 50,000 data rows in a bill.
        *   Instance bills are generated after bills are split. In most cases, the instance bills do not include data generated on the last day of the specified period.
        *   The instance information changes within a billing cycle. The instance configurations and specifications and the time when the instance was used in the billing cycle are all recorded. For more information, see the corresponding bill details.
        *   You can query the data generated in June 2020 or later for Cloud Communications services, and the data generated in November 2020 or later for Alibaba Cloud Domains.
        
        @param request: QueryInstanceBillRequest
        @return: QueryInstanceBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_instance_bill_with_options_async(request, runtime)

    def query_instance_by_tag_with_options(
        self,
        request: bss_open_api_20171214_models.QueryInstanceByTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryInstanceByTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstanceByTag',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryInstanceByTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_by_tag_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryInstanceByTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryInstanceByTagResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstanceByTag',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryInstanceByTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance_by_tag(
        self,
        request: bss_open_api_20171214_models.QueryInstanceByTagRequest,
    ) -> bss_open_api_20171214_models.QueryInstanceByTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_instance_by_tag_with_options(request, runtime)

    async def query_instance_by_tag_async(
        self,
        request: bss_open_api_20171214_models.QueryInstanceByTagRequest,
    ) -> bss_open_api_20171214_models.QueryInstanceByTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_instance_by_tag_with_options_async(request, runtime)

    def query_instance_gaap_cost_with_options(
        self,
        request: bss_open_api_20171214_models.QueryInstanceGaapCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryInstanceGaapCostResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstanceGaapCost',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryInstanceGaapCostResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_instance_gaap_cost_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryInstanceGaapCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryInstanceGaapCostResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInstanceGaapCost',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryInstanceGaapCostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_instance_gaap_cost(
        self,
        request: bss_open_api_20171214_models.QueryInstanceGaapCostRequest,
    ) -> bss_open_api_20171214_models.QueryInstanceGaapCostResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_instance_gaap_cost_with_options(request, runtime)

    async def query_instance_gaap_cost_async(
        self,
        request: bss_open_api_20171214_models.QueryInstanceGaapCostRequest,
    ) -> bss_open_api_20171214_models.QueryInstanceGaapCostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_instance_gaap_cost_with_options_async(request, runtime)

    def query_invoicing_customer_list_with_options(
        self,
        request: bss_open_api_20171214_models.QueryInvoicingCustomerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryInvoicingCustomerListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInvoicingCustomerList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryInvoicingCustomerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_invoicing_customer_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryInvoicingCustomerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryInvoicingCustomerListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInvoicingCustomerList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryInvoicingCustomerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_invoicing_customer_list(
        self,
        request: bss_open_api_20171214_models.QueryInvoicingCustomerListRequest,
    ) -> bss_open_api_20171214_models.QueryInvoicingCustomerListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_invoicing_customer_list_with_options(request, runtime)

    async def query_invoicing_customer_list_async(
        self,
        request: bss_open_api_20171214_models.QueryInvoicingCustomerListRequest,
    ) -> bss_open_api_20171214_models.QueryInvoicingCustomerListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_invoicing_customer_list_with_options_async(request, runtime)

    def query_orders_with_options(
        self,
        request: bss_open_api_20171214_models.QueryOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payment_status):
            query['PaymentStatus'] = request.payment_status
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrders',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_orders_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payment_status):
            query['PaymentStatus'] = request.payment_status
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrders',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_orders(
        self,
        request: bss_open_api_20171214_models.QueryOrdersRequest,
    ) -> bss_open_api_20171214_models.QueryOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_orders_with_options(request, runtime)

    async def query_orders_async(
        self,
        request: bss_open_api_20171214_models.QueryOrdersRequest,
    ) -> bss_open_api_20171214_models.QueryOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_orders_with_options_async(request, runtime)

    def query_permission_list_with_options(
        self,
        request: bss_open_api_20171214_models.QueryPermissionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryPermissionListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relation_id):
            query['RelationId'] = request.relation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPermissionList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryPermissionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_permission_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryPermissionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryPermissionListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.relation_id):
            query['RelationId'] = request.relation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPermissionList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryPermissionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_permission_list(
        self,
        request: bss_open_api_20171214_models.QueryPermissionListRequest,
    ) -> bss_open_api_20171214_models.QueryPermissionListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_permission_list_with_options(request, runtime)

    async def query_permission_list_async(
        self,
        request: bss_open_api_20171214_models.QueryPermissionListRequest,
    ) -> bss_open_api_20171214_models.QueryPermissionListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_permission_list_with_options_async(request, runtime)

    def query_prepaid_cards_with_options(
        self,
        request: bss_open_api_20171214_models.QueryPrepaidCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryPrepaidCardsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_or_not):
            query['EffectiveOrNot'] = request.effective_or_not
        if not UtilClient.is_unset(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not UtilClient.is_unset(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPrepaidCards',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryPrepaidCardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_prepaid_cards_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryPrepaidCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryPrepaidCardsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_or_not):
            query['EffectiveOrNot'] = request.effective_or_not
        if not UtilClient.is_unset(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not UtilClient.is_unset(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPrepaidCards',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryPrepaidCardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_prepaid_cards(
        self,
        request: bss_open_api_20171214_models.QueryPrepaidCardsRequest,
    ) -> bss_open_api_20171214_models.QueryPrepaidCardsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_prepaid_cards_with_options(request, runtime)

    async def query_prepaid_cards_async(
        self,
        request: bss_open_api_20171214_models.QueryPrepaidCardsRequest,
    ) -> bss_open_api_20171214_models.QueryPrepaidCardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_prepaid_cards_with_options_async(request, runtime)

    def query_price_entity_list_with_options(
        self,
        request: bss_open_api_20171214_models.QueryPriceEntityListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryPriceEntityListResponse:
        """
        You can call this operation to query the billable items of a service. A billable item is the minimum unit used to calculate costs.
        
        @param request: QueryPriceEntityListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPriceEntityListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPriceEntityList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryPriceEntityListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_price_entity_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryPriceEntityListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryPriceEntityListResponse:
        """
        You can call this operation to query the billable items of a service. A billable item is the minimum unit used to calculate costs.
        
        @param request: QueryPriceEntityListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryPriceEntityListResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPriceEntityList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryPriceEntityListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_price_entity_list(
        self,
        request: bss_open_api_20171214_models.QueryPriceEntityListRequest,
    ) -> bss_open_api_20171214_models.QueryPriceEntityListResponse:
        """
        You can call this operation to query the billable items of a service. A billable item is the minimum unit used to calculate costs.
        
        @param request: QueryPriceEntityListRequest
        @return: QueryPriceEntityListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_price_entity_list_with_options(request, runtime)

    async def query_price_entity_list_async(
        self,
        request: bss_open_api_20171214_models.QueryPriceEntityListRequest,
    ) -> bss_open_api_20171214_models.QueryPriceEntityListResponse:
        """
        You can call this operation to query the billable items of a service. A billable item is the minimum unit used to calculate costs.
        
        @param request: QueryPriceEntityListRequest
        @return: QueryPriceEntityListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_price_entity_list_with_options_async(request, runtime)

    def query_product_list_with_options(
        self,
        request: bss_open_api_20171214_models.QueryProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryProductListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_total_count):
            query['QueryTotalCount'] = request.query_total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProductList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryProductListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_product_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryProductListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_total_count):
            query['QueryTotalCount'] = request.query_total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProductList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryProductListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_product_list(
        self,
        request: bss_open_api_20171214_models.QueryProductListRequest,
    ) -> bss_open_api_20171214_models.QueryProductListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_product_list_with_options(request, runtime)

    async def query_product_list_async(
        self,
        request: bss_open_api_20171214_models.QueryProductListRequest,
    ) -> bss_open_api_20171214_models.QueryProductListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_product_list_with_options_async(request, runtime)

    def query_riutilization_detail_with_options(
        self,
        request: bss_open_api_20171214_models.QueryRIUtilizationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryRIUtilizationDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deducted_instance_id):
            query['DeductedInstanceId'] = request.deducted_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.ricommodity_code):
            query['RICommodityCode'] = request.ricommodity_code
        if not UtilClient.is_unset(request.riinstance_id):
            query['RIInstanceId'] = request.riinstance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRIUtilizationDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryRIUtilizationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_riutilization_detail_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryRIUtilizationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryRIUtilizationDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deducted_instance_id):
            query['DeductedInstanceId'] = request.deducted_instance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_spec):
            query['InstanceSpec'] = request.instance_spec
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.ricommodity_code):
            query['RICommodityCode'] = request.ricommodity_code
        if not UtilClient.is_unset(request.riinstance_id):
            query['RIInstanceId'] = request.riinstance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRIUtilizationDetail',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryRIUtilizationDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_riutilization_detail(
        self,
        request: bss_open_api_20171214_models.QueryRIUtilizationDetailRequest,
    ) -> bss_open_api_20171214_models.QueryRIUtilizationDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_riutilization_detail_with_options(request, runtime)

    async def query_riutilization_detail_async(
        self,
        request: bss_open_api_20171214_models.QueryRIUtilizationDetailRequest,
    ) -> bss_open_api_20171214_models.QueryRIUtilizationDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_riutilization_detail_with_options_async(request, runtime)

    def query_redeem_with_options(
        self,
        request: bss_open_api_20171214_models.QueryRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryRedeemResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRedeem',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryRedeemResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_redeem_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryRedeemResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRedeem',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryRedeemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_redeem(
        self,
        request: bss_open_api_20171214_models.QueryRedeemRequest,
    ) -> bss_open_api_20171214_models.QueryRedeemResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_redeem_with_options(request, runtime)

    async def query_redeem_async(
        self,
        request: bss_open_api_20171214_models.QueryRedeemRequest,
    ) -> bss_open_api_20171214_models.QueryRedeemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_redeem_with_options_async(request, runtime)

    def query_relation_list_with_options(
        self,
        request: bss_open_api_20171214_models.QueryRelationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryRelationListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRelationList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryRelationListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_relation_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryRelationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryRelationListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRelationList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryRelationListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_relation_list(
        self,
        request: bss_open_api_20171214_models.QueryRelationListRequest,
    ) -> bss_open_api_20171214_models.QueryRelationListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_relation_list_with_options(request, runtime)

    async def query_relation_list_async(
        self,
        request: bss_open_api_20171214_models.QueryRelationListRequest,
    ) -> bss_open_api_20171214_models.QueryRelationListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_relation_list_with_options_async(request, runtime)

    def query_reseller_available_quota_with_options(
        self,
        request: bss_open_api_20171214_models.QueryResellerAvailableQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryResellerAvailableQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_codes):
            query['ItemCodes'] = request.item_codes
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResellerAvailableQuota',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryResellerAvailableQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_reseller_available_quota_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryResellerAvailableQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryResellerAvailableQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.item_codes):
            query['ItemCodes'] = request.item_codes
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResellerAvailableQuota',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryResellerAvailableQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_reseller_available_quota(
        self,
        request: bss_open_api_20171214_models.QueryResellerAvailableQuotaRequest,
    ) -> bss_open_api_20171214_models.QueryResellerAvailableQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_reseller_available_quota_with_options(request, runtime)

    async def query_reseller_available_quota_async(
        self,
        request: bss_open_api_20171214_models.QueryResellerAvailableQuotaRequest,
    ) -> bss_open_api_20171214_models.QueryResellerAvailableQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_reseller_available_quota_with_options_async(request, runtime)

    def query_reseller_user_alarm_threshold_with_options(
        self,
        request: bss_open_api_20171214_models.QueryResellerUserAlarmThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryResellerUserAlarmThresholdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_type):
            query['AlarmType'] = request.alarm_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResellerUserAlarmThreshold',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryResellerUserAlarmThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_reseller_user_alarm_threshold_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryResellerUserAlarmThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryResellerUserAlarmThresholdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_type):
            query['AlarmType'] = request.alarm_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResellerUserAlarmThreshold',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryResellerUserAlarmThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_reseller_user_alarm_threshold(
        self,
        request: bss_open_api_20171214_models.QueryResellerUserAlarmThresholdRequest,
    ) -> bss_open_api_20171214_models.QueryResellerUserAlarmThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_reseller_user_alarm_threshold_with_options(request, runtime)

    async def query_reseller_user_alarm_threshold_async(
        self,
        request: bss_open_api_20171214_models.QueryResellerUserAlarmThresholdRequest,
    ) -> bss_open_api_20171214_models.QueryResellerUserAlarmThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_reseller_user_alarm_threshold_with_options_async(request, runtime)

    def query_resource_package_instances_with_options(
        self,
        request: bss_open_api_20171214_models.QueryResourcePackageInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryResourcePackageInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not UtilClient.is_unset(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        if not UtilClient.is_unset(request.include_partner):
            query['IncludePartner'] = request.include_partner
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResourcePackageInstances',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryResourcePackageInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_resource_package_instances_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryResourcePackageInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryResourcePackageInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expiry_time_end):
            query['ExpiryTimeEnd'] = request.expiry_time_end
        if not UtilClient.is_unset(request.expiry_time_start):
            query['ExpiryTimeStart'] = request.expiry_time_start
        if not UtilClient.is_unset(request.include_partner):
            query['IncludePartner'] = request.include_partner
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryResourcePackageInstances',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryResourcePackageInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_resource_package_instances(
        self,
        request: bss_open_api_20171214_models.QueryResourcePackageInstancesRequest,
    ) -> bss_open_api_20171214_models.QueryResourcePackageInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_resource_package_instances_with_options(request, runtime)

    async def query_resource_package_instances_async(
        self,
        request: bss_open_api_20171214_models.QueryResourcePackageInstancesRequest,
    ) -> bss_open_api_20171214_models.QueryResourcePackageInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_resource_package_instances_with_options_async(request, runtime)

    def query_savings_plans_deduct_log_with_options(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansDeductLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansDeductLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySavingsPlansDeductLog',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySavingsPlansDeductLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_savings_plans_deduct_log_with_options_async(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansDeductLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansDeductLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySavingsPlansDeductLog',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySavingsPlansDeductLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_savings_plans_deduct_log(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansDeductLogRequest,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansDeductLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_savings_plans_deduct_log_with_options(request, runtime)

    async def query_savings_plans_deduct_log_async(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansDeductLogRequest,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansDeductLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_savings_plans_deduct_log_with_options_async(request, runtime)

    def query_savings_plans_discount_with_options(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansDiscountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansDiscountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySavingsPlansDiscount',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySavingsPlansDiscountResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_savings_plans_discount_with_options_async(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansDiscountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansDiscountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySavingsPlansDiscount',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySavingsPlansDiscountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_savings_plans_discount(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansDiscountRequest,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansDiscountResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_savings_plans_discount_with_options(request, runtime)

    async def query_savings_plans_discount_async(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansDiscountRequest,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansDiscountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_savings_plans_discount_with_options_async(request, runtime)

    def query_savings_plans_instance_with_options(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySavingsPlansInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySavingsPlansInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_savings_plans_instance_with_options_async(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySavingsPlansInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySavingsPlansInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_savings_plans_instance(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansInstanceRequest,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_savings_plans_instance_with_options(request, runtime)

    async def query_savings_plans_instance_async(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansInstanceRequest,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_savings_plans_instance_with_options_async(request, runtime)

    def query_settle_bill_with_options(
        self,
        request: bss_open_api_20171214_models.QuerySettleBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySettleBillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.is_display_local_currency):
            query['IsDisplayLocalCurrency'] = request.is_display_local_currency
        if not UtilClient.is_unset(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.record_id):
            query['RecordID'] = request.record_id
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySettleBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySettleBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_settle_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.QuerySettleBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySettleBillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.is_display_local_currency):
            query['IsDisplayLocalCurrency'] = request.is_display_local_currency
        if not UtilClient.is_unset(request.is_hide_zero_charge):
            query['IsHideZeroCharge'] = request.is_hide_zero_charge
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.record_id):
            query['RecordID'] = request.record_id
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySettleBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySettleBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_settle_bill(
        self,
        request: bss_open_api_20171214_models.QuerySettleBillRequest,
    ) -> bss_open_api_20171214_models.QuerySettleBillResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_settle_bill_with_options(request, runtime)

    async def query_settle_bill_async(
        self,
        request: bss_open_api_20171214_models.QuerySettleBillRequest,
    ) -> bss_open_api_20171214_models.QuerySettleBillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_settle_bill_with_options_async(request, runtime)

    def query_sku_price_list_with_options(
        self,
        tmp_req: bss_open_api_20171214_models.QuerySkuPriceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySkuPriceListResponse:
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20171214_models.QuerySkuPriceListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.price_factor_condition_map):
            request.price_factor_condition_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.price_factor_condition_map, 'PriceFactorConditionMap', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySkuPriceList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySkuPriceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_sku_price_list_with_options_async(
        self,
        tmp_req: bss_open_api_20171214_models.QuerySkuPriceListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySkuPriceListResponse:
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20171214_models.QuerySkuPriceListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.price_factor_condition_map):
            request.price_factor_condition_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.price_factor_condition_map, 'PriceFactorConditionMap', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySkuPriceList',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySkuPriceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_sku_price_list(
        self,
        request: bss_open_api_20171214_models.QuerySkuPriceListRequest,
    ) -> bss_open_api_20171214_models.QuerySkuPriceListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_sku_price_list_with_options(request, runtime)

    async def query_sku_price_list_async(
        self,
        request: bss_open_api_20171214_models.QuerySkuPriceListRequest,
    ) -> bss_open_api_20171214_models.QuerySkuPriceListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_sku_price_list_with_options_async(request, runtime)

    def query_split_item_bill_with_options(
        self,
        request: bss_open_api_20171214_models.QuerySplitItemBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySplitItemBillResponse:
        """
        This API operation has been upgraded to DescribeSplitItemBill. We recommend that you call the [DescribeSplitItemBill](~~208169~~) operation to query split bills. You can call the QuerySplitItemBill operation to query a maximum of 50,000 data rows in a bill.
        *   The data queried by calling the QuerySplitItemBill operation is consistent with the data that is displayed for the specified billing cycle on the Split Bill page in User Center.
        *   You can call this operation to query split bills generated within the last 12 months.
        *   This operation returns split bills only after you activate the [Split Bill](https://usercenter2.aliyun.com/finance/split-bill) service in User Center.
        
        @param request: QuerySplitItemBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySplitItemBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySplitItemBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySplitItemBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_split_item_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.QuerySplitItemBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySplitItemBillResponse:
        """
        This API operation has been upgraded to DescribeSplitItemBill. We recommend that you call the [DescribeSplitItemBill](~~208169~~) operation to query split bills. You can call the QuerySplitItemBill operation to query a maximum of 50,000 data rows in a bill.
        *   The data queried by calling the QuerySplitItemBill operation is consistent with the data that is displayed for the specified billing cycle on the Split Bill page in User Center.
        *   You can call this operation to query split bills generated within the last 12 months.
        *   This operation returns split bills only after you activate the [Split Bill](https://usercenter2.aliyun.com/finance/split-bill) service in User Center.
        
        @param request: QuerySplitItemBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySplitItemBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner_id):
            query['BillOwnerId'] = request.bill_owner_id
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySplitItemBill',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QuerySplitItemBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_split_item_bill(
        self,
        request: bss_open_api_20171214_models.QuerySplitItemBillRequest,
    ) -> bss_open_api_20171214_models.QuerySplitItemBillResponse:
        """
        This API operation has been upgraded to DescribeSplitItemBill. We recommend that you call the [DescribeSplitItemBill](~~208169~~) operation to query split bills. You can call the QuerySplitItemBill operation to query a maximum of 50,000 data rows in a bill.
        *   The data queried by calling the QuerySplitItemBill operation is consistent with the data that is displayed for the specified billing cycle on the Split Bill page in User Center.
        *   You can call this operation to query split bills generated within the last 12 months.
        *   This operation returns split bills only after you activate the [Split Bill](https://usercenter2.aliyun.com/finance/split-bill) service in User Center.
        
        @param request: QuerySplitItemBillRequest
        @return: QuerySplitItemBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_split_item_bill_with_options(request, runtime)

    async def query_split_item_bill_async(
        self,
        request: bss_open_api_20171214_models.QuerySplitItemBillRequest,
    ) -> bss_open_api_20171214_models.QuerySplitItemBillResponse:
        """
        This API operation has been upgraded to DescribeSplitItemBill. We recommend that you call the [DescribeSplitItemBill](~~208169~~) operation to query split bills. You can call the QuerySplitItemBill operation to query a maximum of 50,000 data rows in a bill.
        *   The data queried by calling the QuerySplitItemBill operation is consistent with the data that is displayed for the specified billing cycle on the Split Bill page in User Center.
        *   You can call this operation to query split bills generated within the last 12 months.
        *   This operation returns split bills only after you activate the [Split Bill](https://usercenter2.aliyun.com/finance/split-bill) service in User Center.
        
        @param request: QuerySplitItemBillRequest
        @return: QuerySplitItemBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_split_item_bill_with_options_async(request, runtime)

    def query_user_oms_data_with_options(
        self,
        request: bss_open_api_20171214_models.QueryUserOmsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryUserOmsDataResponse:
        """
        You can call this operation to query the usage data of an Alibaba Cloud service. Take note of the following items:
        *   The service code that you specify for querying the usage data of a specific Alibaba Cloud service must be valid. You can query the usage data by hour or by day.
        *   The time that you specify must follow the ISO8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        *   Latency exists in data pushes. Therefore, if you set the DataType parameter to Hour, the integrity of usage data recorded in the last 24 hours can be ensured. If you set the DataType parameter to Day, the integrity of usage data recorded in the last two days can be ensured.
        *   You can query the usage data that is recorded in the last quarter.
        
        @param request: QueryUserOmsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserOmsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table):
            query['Table'] = request.table
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserOmsData',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryUserOmsDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_oms_data_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryUserOmsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryUserOmsDataResponse:
        """
        You can call this operation to query the usage data of an Alibaba Cloud service. Take note of the following items:
        *   The service code that you specify for querying the usage data of a specific Alibaba Cloud service must be valid. You can query the usage data by hour or by day.
        *   The time that you specify must follow the ISO8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        *   Latency exists in data pushes. Therefore, if you set the DataType parameter to Hour, the integrity of usage data recorded in the last 24 hours can be ensured. If you set the DataType parameter to Day, the integrity of usage data recorded in the last two days can be ensured.
        *   You can query the usage data that is recorded in the last quarter.
        
        @param request: QueryUserOmsDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryUserOmsDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table):
            query['Table'] = request.table
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserOmsData',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.QueryUserOmsDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_oms_data(
        self,
        request: bss_open_api_20171214_models.QueryUserOmsDataRequest,
    ) -> bss_open_api_20171214_models.QueryUserOmsDataResponse:
        """
        You can call this operation to query the usage data of an Alibaba Cloud service. Take note of the following items:
        *   The service code that you specify for querying the usage data of a specific Alibaba Cloud service must be valid. You can query the usage data by hour or by day.
        *   The time that you specify must follow the ISO8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        *   Latency exists in data pushes. Therefore, if you set the DataType parameter to Hour, the integrity of usage data recorded in the last 24 hours can be ensured. If you set the DataType parameter to Day, the integrity of usage data recorded in the last two days can be ensured.
        *   You can query the usage data that is recorded in the last quarter.
        
        @param request: QueryUserOmsDataRequest
        @return: QueryUserOmsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_user_oms_data_with_options(request, runtime)

    async def query_user_oms_data_async(
        self,
        request: bss_open_api_20171214_models.QueryUserOmsDataRequest,
    ) -> bss_open_api_20171214_models.QueryUserOmsDataResponse:
        """
        You can call this operation to query the usage data of an Alibaba Cloud service. Take note of the following items:
        *   The service code that you specify for querying the usage data of a specific Alibaba Cloud service must be valid. You can query the usage data by hour or by day.
        *   The time that you specify must follow the ISO8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        *   Latency exists in data pushes. Therefore, if you set the DataType parameter to Hour, the integrity of usage data recorded in the last 24 hours can be ensured. If you set the DataType parameter to Day, the integrity of usage data recorded in the last two days can be ensured.
        *   You can query the usage data that is recorded in the last quarter.
        
        @param request: QueryUserOmsDataRequest
        @return: QueryUserOmsDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_user_oms_data_with_options_async(request, runtime)

    def refund_instance_with_options(
        self,
        request: bss_open_api_20171214_models.RefundInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.RefundInstanceResponse:
        """
        1.  Refunds are applicable only for the actual paid amount. Vouchers used for the purchase are non-refundable.
        2.  Check the information about unsubscription and confirm the unsubscription terms and refundable amount. The resource that is unsubscribed cannot be restored.
        3.  For more information, see [Rules for unsubscribing from resources](https://help.aliyun.com/knowledge_detail/116043.html?spm=a2c81.e1d666e.app.2.62ae11271Kd6iM).
        
        @param request: RefundInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefundInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.immediately_release):
            query['ImmediatelyRelease'] = request.immediately_release
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RefundInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_instance_with_options_async(
        self,
        request: bss_open_api_20171214_models.RefundInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.RefundInstanceResponse:
        """
        1.  Refunds are applicable only for the actual paid amount. Vouchers used for the purchase are non-refundable.
        2.  Check the information about unsubscription and confirm the unsubscription terms and refundable amount. The resource that is unsubscribed cannot be restored.
        3.  For more information, see [Rules for unsubscribing from resources](https://help.aliyun.com/knowledge_detail/116043.html?spm=a2c81.e1d666e.app.2.62ae11271Kd6iM).
        
        @param request: RefundInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefundInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.immediately_release):
            query['ImmediatelyRelease'] = request.immediately_release
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RefundInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_instance(
        self,
        request: bss_open_api_20171214_models.RefundInstanceRequest,
    ) -> bss_open_api_20171214_models.RefundInstanceResponse:
        """
        1.  Refunds are applicable only for the actual paid amount. Vouchers used for the purchase are non-refundable.
        2.  Check the information about unsubscription and confirm the unsubscription terms and refundable amount. The resource that is unsubscribed cannot be restored.
        3.  For more information, see [Rules for unsubscribing from resources](https://help.aliyun.com/knowledge_detail/116043.html?spm=a2c81.e1d666e.app.2.62ae11271Kd6iM).
        
        @param request: RefundInstanceRequest
        @return: RefundInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refund_instance_with_options(request, runtime)

    async def refund_instance_async(
        self,
        request: bss_open_api_20171214_models.RefundInstanceRequest,
    ) -> bss_open_api_20171214_models.RefundInstanceResponse:
        """
        1.  Refunds are applicable only for the actual paid amount. Vouchers used for the purchase are non-refundable.
        2.  Check the information about unsubscription and confirm the unsubscription terms and refundable amount. The resource that is unsubscribed cannot be restored.
        3.  For more information, see [Rules for unsubscribing from resources](https://help.aliyun.com/knowledge_detail/116043.html?spm=a2c81.e1d666e.app.2.62ae11271Kd6iM).
        
        @param request: RefundInstanceRequest
        @return: RefundInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refund_instance_with_options_async(request, runtime)

    def release_instance_with_options(
        self,
        request: bss_open_api_20171214_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ReleaseInstanceResponse:
        """
        A value of true indicates that the execution is complete.
        A value of false indicates that an error occurs during the execution.
        
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_with_options_async(
        self,
        request: bss_open_api_20171214_models.ReleaseInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ReleaseInstanceResponse:
        """
        A value of true indicates that the execution is complete.
        A value of false indicates that an error occurs during the execution.
        
        @param request: ReleaseInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.renew_status):
            query['RenewStatus'] = request.renew_status
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.ReleaseInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance(
        self,
        request: bss_open_api_20171214_models.ReleaseInstanceRequest,
    ) -> bss_open_api_20171214_models.ReleaseInstanceResponse:
        """
        A value of true indicates that the execution is complete.
        A value of false indicates that an error occurs during the execution.
        
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    async def release_instance_async(
        self,
        request: bss_open_api_20171214_models.ReleaseInstanceRequest,
    ) -> bss_open_api_20171214_models.ReleaseInstanceResponse:
        """
        A value of true indicates that the execution is complete.
        A value of false indicates that an error occurs during the execution.
        
        @param request: ReleaseInstanceRequest
        @return: ReleaseInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_with_options_async(request, runtime)

    def relieve_account_relation_with_options(
        self,
        request: bss_open_api_20171214_models.RelieveAccountRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.RelieveAccountRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not UtilClient.is_unset(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not UtilClient.is_unset(request.relation_id):
            query['RelationId'] = request.relation_id
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RelieveAccountRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RelieveAccountRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def relieve_account_relation_with_options_async(
        self,
        request: bss_open_api_20171214_models.RelieveAccountRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.RelieveAccountRelationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_user_id):
            query['ChildUserId'] = request.child_user_id
        if not UtilClient.is_unset(request.parent_user_id):
            query['ParentUserId'] = request.parent_user_id
        if not UtilClient.is_unset(request.relation_id):
            query['RelationId'] = request.relation_id
        if not UtilClient.is_unset(request.relation_type):
            query['RelationType'] = request.relation_type
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RelieveAccountRelation',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RelieveAccountRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def relieve_account_relation(
        self,
        request: bss_open_api_20171214_models.RelieveAccountRelationRequest,
    ) -> bss_open_api_20171214_models.RelieveAccountRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.relieve_account_relation_with_options(request, runtime)

    async def relieve_account_relation_async(
        self,
        request: bss_open_api_20171214_models.RelieveAccountRelationRequest,
    ) -> bss_open_api_20171214_models.RelieveAccountRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.relieve_account_relation_with_options_async(request, runtime)

    def renew_change_instance_with_options(
        self,
        request: bss_open_api_20171214_models.RenewChangeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.RenewChangeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.parameter):
            query['Parameter'] = request.parameter
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewChangeInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RenewChangeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_change_instance_with_options_async(
        self,
        request: bss_open_api_20171214_models.RenewChangeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.RenewChangeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.parameter):
            query['Parameter'] = request.parameter
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewChangeInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RenewChangeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_change_instance(
        self,
        request: bss_open_api_20171214_models.RenewChangeInstanceRequest,
    ) -> bss_open_api_20171214_models.RenewChangeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_change_instance_with_options(request, runtime)

    async def renew_change_instance_async(
        self,
        request: bss_open_api_20171214_models.RenewChangeInstanceRequest,
    ) -> bss_open_api_20171214_models.RenewChangeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_change_instance_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: bss_open_api_20171214_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: bss_open_api_20171214_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.renew_period):
            query['RenewPeriod'] = request.renew_period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: bss_open_api_20171214_models.RenewInstanceRequest,
    ) -> bss_open_api_20171214_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: bss_open_api_20171214_models.RenewInstanceRequest,
    ) -> bss_open_api_20171214_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def renew_resource_package_with_options(
        self,
        request: bss_open_api_20171214_models.RenewResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.RenewResourcePackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewResourcePackage',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RenewResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_resource_package_with_options_async(
        self,
        request: bss_open_api_20171214_models.RenewResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.RenewResourcePackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewResourcePackage',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.RenewResourcePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_resource_package(
        self,
        request: bss_open_api_20171214_models.RenewResourcePackageRequest,
    ) -> bss_open_api_20171214_models.RenewResourcePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_resource_package_with_options(request, runtime)

    async def renew_resource_package_async(
        self,
        request: bss_open_api_20171214_models.RenewResourcePackageRequest,
    ) -> bss_open_api_20171214_models.RenewResourcePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_resource_package_with_options_async(request, runtime)

    def save_user_credit_with_options(
        self,
        request: bss_open_api_20171214_models.SaveUserCreditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SaveUserCreditResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avoid_expiration):
            query['AvoidExpiration'] = request.avoid_expiration
        if not UtilClient.is_unset(request.avoid_notification):
            query['AvoidNotification'] = request.avoid_notification
        if not UtilClient.is_unset(request.avoid_prepaid_expiration):
            query['AvoidPrepaidExpiration'] = request.avoid_prepaid_expiration
        if not UtilClient.is_unset(request.avoid_prepaid_notification):
            query['AvoidPrepaidNotification'] = request.avoid_prepaid_notification
        if not UtilClient.is_unset(request.credit_type):
            query['CreditType'] = request.credit_type
        if not UtilClient.is_unset(request.credit_value):
            query['CreditValue'] = request.credit_value
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveUserCredit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SaveUserCreditResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_user_credit_with_options_async(
        self,
        request: bss_open_api_20171214_models.SaveUserCreditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SaveUserCreditResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.avoid_expiration):
            query['AvoidExpiration'] = request.avoid_expiration
        if not UtilClient.is_unset(request.avoid_notification):
            query['AvoidNotification'] = request.avoid_notification
        if not UtilClient.is_unset(request.avoid_prepaid_expiration):
            query['AvoidPrepaidExpiration'] = request.avoid_prepaid_expiration
        if not UtilClient.is_unset(request.avoid_prepaid_notification):
            query['AvoidPrepaidNotification'] = request.avoid_prepaid_notification
        if not UtilClient.is_unset(request.credit_type):
            query['CreditType'] = request.credit_type
        if not UtilClient.is_unset(request.credit_value):
            query['CreditValue'] = request.credit_value
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveUserCredit',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SaveUserCreditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_user_credit(
        self,
        request: bss_open_api_20171214_models.SaveUserCreditRequest,
    ) -> bss_open_api_20171214_models.SaveUserCreditResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_user_credit_with_options(request, runtime)

    async def save_user_credit_async(
        self,
        request: bss_open_api_20171214_models.SaveUserCreditRequest,
    ) -> bss_open_api_20171214_models.SaveUserCreditResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_user_credit_with_options_async(request, runtime)

    def set_all_expiration_day_with_options(
        self,
        request: bss_open_api_20171214_models.SetAllExpirationDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetAllExpirationDayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.unify_expire_day):
            query['UnifyExpireDay'] = request.unify_expire_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAllExpirationDay',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetAllExpirationDayResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_all_expiration_day_with_options_async(
        self,
        request: bss_open_api_20171214_models.SetAllExpirationDayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetAllExpirationDayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.unify_expire_day):
            query['UnifyExpireDay'] = request.unify_expire_day
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAllExpirationDay',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetAllExpirationDayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_all_expiration_day(
        self,
        request: bss_open_api_20171214_models.SetAllExpirationDayRequest,
    ) -> bss_open_api_20171214_models.SetAllExpirationDayResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_all_expiration_day_with_options(request, runtime)

    async def set_all_expiration_day_async(
        self,
        request: bss_open_api_20171214_models.SetAllExpirationDayRequest,
    ) -> bss_open_api_20171214_models.SetAllExpirationDayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_all_expiration_day_with_options_async(request, runtime)

    def set_credit_label_action_with_options(
        self,
        request: bss_open_api_20171214_models.SetCreditLabelActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetCreditLabelActionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.clear_cycle):
            query['ClearCycle'] = request.clear_cycle
        if not UtilClient.is_unset(request.credit_amount):
            query['CreditAmount'] = request.credit_amount
        if not UtilClient.is_unset(request.currency_code):
            query['CurrencyCode'] = request.currency_code
        if not UtilClient.is_unset(request.daily_cycle):
            query['DailyCycle'] = request.daily_cycle
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.is_need_add_settle_label):
            query['IsNeedAddSettleLabel'] = request.is_need_add_settle_label
        if not UtilClient.is_unset(request.is_need_adjust_credit_account):
            query['IsNeedAdjustCreditAccount'] = request.is_need_adjust_credit_account
        if not UtilClient.is_unset(request.is_need_save_notify_rule):
            query['IsNeedSaveNotifyRule'] = request.is_need_save_notify_rule
        if not UtilClient.is_unset(request.is_need_set_credit_amount):
            query['IsNeedSetCreditAmount'] = request.is_need_set_credit_amount
        if not UtilClient.is_unset(request.need_notice):
            query['NeedNotice'] = request.need_notice
        if not UtilClient.is_unset(request.new_create_mode):
            query['NewCreateMode'] = request.new_create_mode
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.site_code):
            query['SiteCode'] = request.site_code
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCreditLabelAction',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetCreditLabelActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_credit_label_action_with_options_async(
        self,
        request: bss_open_api_20171214_models.SetCreditLabelActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetCreditLabelActionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.clear_cycle):
            query['ClearCycle'] = request.clear_cycle
        if not UtilClient.is_unset(request.credit_amount):
            query['CreditAmount'] = request.credit_amount
        if not UtilClient.is_unset(request.currency_code):
            query['CurrencyCode'] = request.currency_code
        if not UtilClient.is_unset(request.daily_cycle):
            query['DailyCycle'] = request.daily_cycle
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.is_need_add_settle_label):
            query['IsNeedAddSettleLabel'] = request.is_need_add_settle_label
        if not UtilClient.is_unset(request.is_need_adjust_credit_account):
            query['IsNeedAdjustCreditAccount'] = request.is_need_adjust_credit_account
        if not UtilClient.is_unset(request.is_need_save_notify_rule):
            query['IsNeedSaveNotifyRule'] = request.is_need_save_notify_rule
        if not UtilClient.is_unset(request.is_need_set_credit_amount):
            query['IsNeedSetCreditAmount'] = request.is_need_set_credit_amount
        if not UtilClient.is_unset(request.need_notice):
            query['NeedNotice'] = request.need_notice
        if not UtilClient.is_unset(request.new_create_mode):
            query['NewCreateMode'] = request.new_create_mode
        if not UtilClient.is_unset(request.operator):
            query['Operator'] = request.operator
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.site_code):
            query['SiteCode'] = request.site_code
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCreditLabelAction',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetCreditLabelActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_credit_label_action(
        self,
        request: bss_open_api_20171214_models.SetCreditLabelActionRequest,
    ) -> bss_open_api_20171214_models.SetCreditLabelActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_credit_label_action_with_options(request, runtime)

    async def set_credit_label_action_async(
        self,
        request: bss_open_api_20171214_models.SetCreditLabelActionRequest,
    ) -> bss_open_api_20171214_models.SetCreditLabelActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_credit_label_action_with_options_async(request, runtime)

    def set_renewal_with_options(
        self,
        request: bss_open_api_20171214_models.SetRenewalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetRenewalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIDs'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.renewal_period):
            query['RenewalPeriod'] = request.renewal_period
        if not UtilClient.is_unset(request.renewal_period_unit):
            query['RenewalPeriodUnit'] = request.renewal_period_unit
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRenewal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetRenewalResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_renewal_with_options_async(
        self,
        request: bss_open_api_20171214_models.SetRenewalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetRenewalResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIDs'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.renewal_period):
            query['RenewalPeriod'] = request.renewal_period
        if not UtilClient.is_unset(request.renewal_period_unit):
            query['RenewalPeriodUnit'] = request.renewal_period_unit
        if not UtilClient.is_unset(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not UtilClient.is_unset(request.subscription_type):
            query['SubscriptionType'] = request.subscription_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRenewal',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetRenewalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_renewal(
        self,
        request: bss_open_api_20171214_models.SetRenewalRequest,
    ) -> bss_open_api_20171214_models.SetRenewalResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_renewal_with_options(request, runtime)

    async def set_renewal_async(
        self,
        request: bss_open_api_20171214_models.SetRenewalRequest,
    ) -> bss_open_api_20171214_models.SetRenewalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_renewal_with_options_async(request, runtime)

    def set_reseller_user_alarm_threshold_with_options(
        self,
        request: bss_open_api_20171214_models.SetResellerUserAlarmThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetResellerUserAlarmThresholdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_thresholds):
            query['AlarmThresholds'] = request.alarm_thresholds
        if not UtilClient.is_unset(request.alarm_type):
            query['AlarmType'] = request.alarm_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetResellerUserAlarmThreshold',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetResellerUserAlarmThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_reseller_user_alarm_threshold_with_options_async(
        self,
        request: bss_open_api_20171214_models.SetResellerUserAlarmThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetResellerUserAlarmThresholdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_thresholds):
            query['AlarmThresholds'] = request.alarm_thresholds
        if not UtilClient.is_unset(request.alarm_type):
            query['AlarmType'] = request.alarm_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetResellerUserAlarmThreshold',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetResellerUserAlarmThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_reseller_user_alarm_threshold(
        self,
        request: bss_open_api_20171214_models.SetResellerUserAlarmThresholdRequest,
    ) -> bss_open_api_20171214_models.SetResellerUserAlarmThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_reseller_user_alarm_threshold_with_options(request, runtime)

    async def set_reseller_user_alarm_threshold_async(
        self,
        request: bss_open_api_20171214_models.SetResellerUserAlarmThresholdRequest,
    ) -> bss_open_api_20171214_models.SetResellerUserAlarmThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_reseller_user_alarm_threshold_with_options_async(request, runtime)

    def set_reseller_user_quota_with_options(
        self,
        request: bss_open_api_20171214_models.SetResellerUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetResellerUserQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.currency):
            query['Currency'] = request.currency
        if not UtilClient.is_unset(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetResellerUserQuota',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetResellerUserQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_reseller_user_quota_with_options_async(
        self,
        request: bss_open_api_20171214_models.SetResellerUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetResellerUserQuotaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.currency):
            query['Currency'] = request.currency
        if not UtilClient.is_unset(request.out_biz_id):
            query['OutBizId'] = request.out_biz_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetResellerUserQuota',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetResellerUserQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_reseller_user_quota(
        self,
        request: bss_open_api_20171214_models.SetResellerUserQuotaRequest,
    ) -> bss_open_api_20171214_models.SetResellerUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_reseller_user_quota_with_options(request, runtime)

    async def set_reseller_user_quota_async(
        self,
        request: bss_open_api_20171214_models.SetResellerUserQuotaRequest,
    ) -> bss_open_api_20171214_models.SetResellerUserQuotaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_reseller_user_quota_with_options_async(request, runtime)

    def set_reseller_user_status_with_options(
        self,
        request: bss_open_api_20171214_models.SetResellerUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetResellerUserStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.stop_mode):
            query['StopMode'] = request.stop_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetResellerUserStatus',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetResellerUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_reseller_user_status_with_options_async(
        self,
        request: bss_open_api_20171214_models.SetResellerUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetResellerUserStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.stop_mode):
            query['StopMode'] = request.stop_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetResellerUserStatus',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SetResellerUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_reseller_user_status(
        self,
        request: bss_open_api_20171214_models.SetResellerUserStatusRequest,
    ) -> bss_open_api_20171214_models.SetResellerUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_reseller_user_status_with_options(request, runtime)

    async def set_reseller_user_status_async(
        self,
        request: bss_open_api_20171214_models.SetResellerUserStatusRequest,
    ) -> bss_open_api_20171214_models.SetResellerUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_reseller_user_status_with_options_async(request, runtime)

    def subscribe_bill_to_osswith_options(
        self,
        request: bss_open_api_20171214_models.SubscribeBillToOSSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SubscribeBillToOSSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not UtilClient.is_unset(request.bucket_owner_id):
            query['BucketOwnerId'] = request.bucket_owner_id
        if not UtilClient.is_unset(request.bucket_path):
            query['BucketPath'] = request.bucket_path
        if not UtilClient.is_unset(request.mult_account_rel_subscribe):
            query['MultAccountRelSubscribe'] = request.mult_account_rel_subscribe
        if not UtilClient.is_unset(request.row_limit_per_file):
            query['RowLimitPerFile'] = request.row_limit_per_file
        if not UtilClient.is_unset(request.subscribe_bucket):
            query['SubscribeBucket'] = request.subscribe_bucket
        if not UtilClient.is_unset(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubscribeBillToOSS',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SubscribeBillToOSSResponse(),
            self.call_api(params, req, runtime)
        )

    async def subscribe_bill_to_osswith_options_async(
        self,
        request: bss_open_api_20171214_models.SubscribeBillToOSSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SubscribeBillToOSSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not UtilClient.is_unset(request.bucket_owner_id):
            query['BucketOwnerId'] = request.bucket_owner_id
        if not UtilClient.is_unset(request.bucket_path):
            query['BucketPath'] = request.bucket_path
        if not UtilClient.is_unset(request.mult_account_rel_subscribe):
            query['MultAccountRelSubscribe'] = request.mult_account_rel_subscribe
        if not UtilClient.is_unset(request.row_limit_per_file):
            query['RowLimitPerFile'] = request.row_limit_per_file
        if not UtilClient.is_unset(request.subscribe_bucket):
            query['SubscribeBucket'] = request.subscribe_bucket
        if not UtilClient.is_unset(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubscribeBillToOSS',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.SubscribeBillToOSSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def subscribe_bill_to_oss(
        self,
        request: bss_open_api_20171214_models.SubscribeBillToOSSRequest,
    ) -> bss_open_api_20171214_models.SubscribeBillToOSSResponse:
        runtime = util_models.RuntimeOptions()
        return self.subscribe_bill_to_osswith_options(request, runtime)

    async def subscribe_bill_to_oss_async(
        self,
        request: bss_open_api_20171214_models.SubscribeBillToOSSRequest,
    ) -> bss_open_api_20171214_models.SubscribeBillToOSSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.subscribe_bill_to_osswith_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: bss_open_api_20171214_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: bss_open_api_20171214_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: bss_open_api_20171214_models.TagResourcesRequest,
    ) -> bss_open_api_20171214_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: bss_open_api_20171214_models.TagResourcesRequest,
    ) -> bss_open_api_20171214_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def unsubscribe_bill_to_osswith_options(
        self,
        request: bss_open_api_20171214_models.UnsubscribeBillToOSSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.UnsubscribeBillToOSSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mult_account_rel_subscribe):
            query['MultAccountRelSubscribe'] = request.mult_account_rel_subscribe
        if not UtilClient.is_unset(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnsubscribeBillToOSS',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.UnsubscribeBillToOSSResponse(),
            self.call_api(params, req, runtime)
        )

    async def unsubscribe_bill_to_osswith_options_async(
        self,
        request: bss_open_api_20171214_models.UnsubscribeBillToOSSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.UnsubscribeBillToOSSResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.mult_account_rel_subscribe):
            query['MultAccountRelSubscribe'] = request.mult_account_rel_subscribe
        if not UtilClient.is_unset(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnsubscribeBillToOSS',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.UnsubscribeBillToOSSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unsubscribe_bill_to_oss(
        self,
        request: bss_open_api_20171214_models.UnsubscribeBillToOSSRequest,
    ) -> bss_open_api_20171214_models.UnsubscribeBillToOSSResponse:
        runtime = util_models.RuntimeOptions()
        return self.unsubscribe_bill_to_osswith_options(request, runtime)

    async def unsubscribe_bill_to_oss_async(
        self,
        request: bss_open_api_20171214_models.UnsubscribeBillToOSSRequest,
    ) -> bss_open_api_20171214_models.UnsubscribeBillToOSSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unsubscribe_bill_to_osswith_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: bss_open_api_20171214_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: bss_open_api_20171214_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: bss_open_api_20171214_models.UntagResourcesRequest,
    ) -> bss_open_api_20171214_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: bss_open_api_20171214_models.UntagResourcesRequest,
    ) -> bss_open_api_20171214_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_resource_package_with_options(
        self,
        request: bss_open_api_20171214_models.UpgradeResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.UpgradeResourcePackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeResourcePackage',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.UpgradeResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_resource_package_with_options_async(
        self,
        request: bss_open_api_20171214_models.UpgradeResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.UpgradeResourcePackageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.effective_date):
            query['EffectiveDate'] = request.effective_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeResourcePackage',
            version='2017-12-14',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20171214_models.UpgradeResourcePackageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_resource_package(
        self,
        request: bss_open_api_20171214_models.UpgradeResourcePackageRequest,
    ) -> bss_open_api_20171214_models.UpgradeResourcePackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_resource_package_with_options(request, runtime)

    async def upgrade_resource_package_async(
        self,
        request: bss_open_api_20171214_models.UpgradeResourcePackageRequest,
    ) -> bss_open_api_20171214_models.UpgradeResourcePackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_resource_package_with_options_async(request, runtime)
