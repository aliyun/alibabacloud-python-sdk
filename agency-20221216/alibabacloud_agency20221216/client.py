# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_agency20221216 import models as agency_20221216_models
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

    def cancel_subscription_bill_with_options(
        self,
        request: agency_20221216_models.CancelSubscriptionBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.CancelSubscriptionBillResponse:
        """
        Make sure that you are a distributor of the Alibaba Cloud international ecosystem.
        You can call this operation to cancel the subscription to only one type of bill at a time.
        After the subscription to a type of bill is canceled, bills of this type are no longer pushed to the specified Object Storage Service (OSS) bucket.
        **This topic is published only on the international site (alibabacloud.com).
        
        @param request: CancelSubscriptionBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSubscriptionBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelSubscriptionBill',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.CancelSubscriptionBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_subscription_bill_with_options_async(
        self,
        request: agency_20221216_models.CancelSubscriptionBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.CancelSubscriptionBillResponse:
        """
        Make sure that you are a distributor of the Alibaba Cloud international ecosystem.
        You can call this operation to cancel the subscription to only one type of bill at a time.
        After the subscription to a type of bill is canceled, bills of this type are no longer pushed to the specified Object Storage Service (OSS) bucket.
        **This topic is published only on the international site (alibabacloud.com).
        
        @param request: CancelSubscriptionBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelSubscriptionBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelSubscriptionBill',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.CancelSubscriptionBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_subscription_bill(
        self,
        request: agency_20221216_models.CancelSubscriptionBillRequest,
    ) -> agency_20221216_models.CancelSubscriptionBillResponse:
        """
        Make sure that you are a distributor of the Alibaba Cloud international ecosystem.
        You can call this operation to cancel the subscription to only one type of bill at a time.
        After the subscription to a type of bill is canceled, bills of this type are no longer pushed to the specified Object Storage Service (OSS) bucket.
        **This topic is published only on the international site (alibabacloud.com).
        
        @param request: CancelSubscriptionBillRequest
        @return: CancelSubscriptionBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_subscription_bill_with_options(request, runtime)

    async def cancel_subscription_bill_async(
        self,
        request: agency_20221216_models.CancelSubscriptionBillRequest,
    ) -> agency_20221216_models.CancelSubscriptionBillResponse:
        """
        Make sure that you are a distributor of the Alibaba Cloud international ecosystem.
        You can call this operation to cancel the subscription to only one type of bill at a time.
        After the subscription to a type of bill is canceled, bills of this type are no longer pushed to the specified Object Storage Service (OSS) bucket.
        **This topic is published only on the international site (alibabacloud.com).
        
        @param request: CancelSubscriptionBillRequest
        @return: CancelSubscriptionBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_subscription_bill_with_options_async(request, runtime)

    def create_customer_with_options(
        self,
        request: agency_20221216_models.CreateCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.CreateCustomerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_name):
            query['CustomerName'] = request.customer_name
        if not UtilClient.is_unset(request.customer_source):
            query['CustomerSource'] = request.customer_source
        if not UtilClient.is_unset(request.customer_sub_trade):
            query['CustomerSubTrade'] = request.customer_sub_trade
        if not UtilClient.is_unset(request.customer_trade):
            query['CustomerTrade'] = request.customer_trade
        if not UtilClient.is_unset(request.nation):
            query['Nation'] = request.nation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomer',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.CreateCustomerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_customer_with_options_async(
        self,
        request: agency_20221216_models.CreateCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.CreateCustomerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.customer_name):
            query['CustomerName'] = request.customer_name
        if not UtilClient.is_unset(request.customer_source):
            query['CustomerSource'] = request.customer_source
        if not UtilClient.is_unset(request.customer_sub_trade):
            query['CustomerSubTrade'] = request.customer_sub_trade
        if not UtilClient.is_unset(request.customer_trade):
            query['CustomerTrade'] = request.customer_trade
        if not UtilClient.is_unset(request.nation):
            query['Nation'] = request.nation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomer',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.CreateCustomerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_customer(
        self,
        request: agency_20221216_models.CreateCustomerRequest,
    ) -> agency_20221216_models.CreateCustomerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_customer_with_options(request, runtime)

    async def create_customer_async(
        self,
        request: agency_20221216_models.CreateCustomerRequest,
    ) -> agency_20221216_models.CreateCustomerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_customer_with_options_async(request, runtime)

    def deduct_outstanding_balance_with_options(
        self,
        request: agency_20221216_models.DeductOutstandingBalanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.DeductOutstandingBalanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deduct_amount):
            query['DeductAmount'] = request.deduct_amount
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeductOutstandingBalance',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.DeductOutstandingBalanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def deduct_outstanding_balance_with_options_async(
        self,
        request: agency_20221216_models.DeductOutstandingBalanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.DeductOutstandingBalanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deduct_amount):
            query['DeductAmount'] = request.deduct_amount
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeductOutstandingBalance',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.DeductOutstandingBalanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deduct_outstanding_balance(
        self,
        request: agency_20221216_models.DeductOutstandingBalanceRequest,
    ) -> agency_20221216_models.DeductOutstandingBalanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.deduct_outstanding_balance_with_options(request, runtime)

    async def deduct_outstanding_balance_async(
        self,
        request: agency_20221216_models.DeductOutstandingBalanceRequest,
    ) -> agency_20221216_models.DeductOutstandingBalanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deduct_outstanding_balance_with_options_async(request, runtime)

    def edit_end_user_status_with_options(
        self,
        request: agency_20221216_models.EditEndUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.EditEndUserStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditEndUserStatus',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.EditEndUserStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_end_user_status_with_options_async(
        self,
        request: agency_20221216_models.EditEndUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.EditEndUserStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditEndUserStatus',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.EditEndUserStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_end_user_status(
        self,
        request: agency_20221216_models.EditEndUserStatusRequest,
    ) -> agency_20221216_models.EditEndUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_end_user_status_with_options(request, runtime)

    async def edit_end_user_status_async(
        self,
        request: agency_20221216_models.EditEndUserStatusRequest,
    ) -> agency_20221216_models.EditEndUserStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_end_user_status_with_options_async(request, runtime)

    def edit_new_buy_status_with_options(
        self,
        request: agency_20221216_models.EditNewBuyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.EditNewBuyStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_buy_status):
            query['NewBuyStatus'] = request.new_buy_status
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditNewBuyStatus',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.EditNewBuyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_new_buy_status_with_options_async(
        self,
        request: agency_20221216_models.EditNewBuyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.EditNewBuyStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_buy_status):
            query['NewBuyStatus'] = request.new_buy_status
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditNewBuyStatus',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.EditNewBuyStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_new_buy_status(
        self,
        request: agency_20221216_models.EditNewBuyStatusRequest,
    ) -> agency_20221216_models.EditNewBuyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_new_buy_status_with_options(request, runtime)

    async def edit_new_buy_status_async(
        self,
        request: agency_20221216_models.EditNewBuyStatusRequest,
    ) -> agency_20221216_models.EditNewBuyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_new_buy_status_with_options_async(request, runtime)

    def edit_zero_credit_shutdown_with_options(
        self,
        request: agency_20221216_models.EditZeroCreditShutdownRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.EditZeroCreditShutdownResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.shutdown_policy):
            query['ShutdownPolicy'] = request.shutdown_policy
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditZeroCreditShutdown',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.EditZeroCreditShutdownResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_zero_credit_shutdown_with_options_async(
        self,
        request: agency_20221216_models.EditZeroCreditShutdownRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.EditZeroCreditShutdownResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.shutdown_policy):
            query['ShutdownPolicy'] = request.shutdown_policy
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditZeroCreditShutdown',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.EditZeroCreditShutdownResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_zero_credit_shutdown(
        self,
        request: agency_20221216_models.EditZeroCreditShutdownRequest,
    ) -> agency_20221216_models.EditZeroCreditShutdownResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_zero_credit_shutdown_with_options(request, runtime)

    async def edit_zero_credit_shutdown_async(
        self,
        request: agency_20221216_models.EditZeroCreditShutdownRequest,
    ) -> agency_20221216_models.EditZeroCreditShutdownResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_zero_credit_shutdown_with_options_async(request, runtime)

    def get_account_info_with_options(
        self,
        request: agency_20221216_models.GetAccountInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.GetAccountInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountInfo',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_info_with_options_async(
        self,
        request: agency_20221216_models.GetAccountInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.GetAccountInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountInfo',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_info(
        self,
        request: agency_20221216_models.GetAccountInfoRequest,
    ) -> agency_20221216_models.GetAccountInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_account_info_with_options(request, runtime)

    async def get_account_info_async(
        self,
        request: agency_20221216_models.GetAccountInfoRequest,
    ) -> agency_20221216_models.GetAccountInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_account_info_with_options_async(request, runtime)

    def get_credit_info_with_options(
        self,
        request: agency_20221216_models.GetCreditInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.GetCreditInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreditInfo',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetCreditInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_credit_info_with_options_async(
        self,
        request: agency_20221216_models.GetCreditInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.GetCreditInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCreditInfo',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetCreditInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_credit_info(
        self,
        request: agency_20221216_models.GetCreditInfoRequest,
    ) -> agency_20221216_models.GetCreditInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_credit_info_with_options(request, runtime)

    async def get_credit_info_async(
        self,
        request: agency_20221216_models.GetCreditInfoRequest,
    ) -> agency_20221216_models.GetCreditInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_credit_info_with_options_async(request, runtime)

    def get_daily_bill_with_options(
        self,
        request: agency_20221216_models.GetDailyBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.GetDailyBillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner):
            query['BillOwner'] = request.bill_owner
        if not UtilClient.is_unset(request.bill_type):
            query['BillType'] = request.bill_type
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDailyBill',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetDailyBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_daily_bill_with_options_async(
        self,
        request: agency_20221216_models.GetDailyBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.GetDailyBillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner):
            query['BillOwner'] = request.bill_owner
        if not UtilClient.is_unset(request.bill_type):
            query['BillType'] = request.bill_type
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDailyBill',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetDailyBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_daily_bill(
        self,
        request: agency_20221216_models.GetDailyBillRequest,
    ) -> agency_20221216_models.GetDailyBillResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_daily_bill_with_options(request, runtime)

    async def get_daily_bill_async(
        self,
        request: agency_20221216_models.GetDailyBillRequest,
    ) -> agency_20221216_models.GetDailyBillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_daily_bill_with_options_async(request, runtime)

    def get_invite_status_with_options(
        self,
        request: agency_20221216_models.GetInviteStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.GetInviteStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.invite_status_list):
            query['InviteStatusList'] = request.invite_status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInviteStatus',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetInviteStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_invite_status_with_options_async(
        self,
        request: agency_20221216_models.GetInviteStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.GetInviteStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.invite_status_list):
            query['InviteStatusList'] = request.invite_status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInviteStatus',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetInviteStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_invite_status(
        self,
        request: agency_20221216_models.GetInviteStatusRequest,
    ) -> agency_20221216_models.GetInviteStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_invite_status_with_options(request, runtime)

    async def get_invite_status_async(
        self,
        request: agency_20221216_models.GetInviteStatusRequest,
    ) -> agency_20221216_models.GetInviteStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_invite_status_with_options_async(request, runtime)

    def get_monthly_bill_with_options(
        self,
        request: agency_20221216_models.GetMonthlyBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.GetMonthlyBillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner):
            query['BillOwner'] = request.bill_owner
        if not UtilClient.is_unset(request.bill_type):
            query['BillType'] = request.bill_type
        if not UtilClient.is_unset(request.month):
            query['Month'] = request.month
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonthlyBill',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetMonthlyBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_monthly_bill_with_options_async(
        self,
        request: agency_20221216_models.GetMonthlyBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.GetMonthlyBillResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bill_owner):
            query['BillOwner'] = request.bill_owner
        if not UtilClient.is_unset(request.bill_type):
            query['BillType'] = request.bill_type
        if not UtilClient.is_unset(request.month):
            query['Month'] = request.month
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonthlyBill',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetMonthlyBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_monthly_bill(
        self,
        request: agency_20221216_models.GetMonthlyBillRequest,
    ) -> agency_20221216_models.GetMonthlyBillResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_monthly_bill_with_options(request, runtime)

    async def get_monthly_bill_async(
        self,
        request: agency_20221216_models.GetMonthlyBillRequest,
    ) -> agency_20221216_models.GetMonthlyBillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_monthly_bill_with_options_async(request, runtime)

    def get_unassociated_customer_with_options(
        self,
        request: agency_20221216_models.GetUnassociatedCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.GetUnassociatedCustomerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUnassociatedCustomer',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetUnassociatedCustomerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_unassociated_customer_with_options_async(
        self,
        request: agency_20221216_models.GetUnassociatedCustomerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.GetUnassociatedCustomerResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUnassociatedCustomer',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.GetUnassociatedCustomerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_unassociated_customer(
        self,
        request: agency_20221216_models.GetUnassociatedCustomerRequest,
    ) -> agency_20221216_models.GetUnassociatedCustomerResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_unassociated_customer_with_options(request, runtime)

    async def get_unassociated_customer_async(
        self,
        request: agency_20221216_models.GetUnassociatedCustomerRequest,
    ) -> agency_20221216_models.GetUnassociatedCustomerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_unassociated_customer_with_options_async(request, runtime)

    def invite_sub_account_with_options(
        self,
        request: agency_20221216_models.InviteSubAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.InviteSubAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_info_list):
            query['AccountInfoList'] = request.account_info_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InviteSubAccount',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.InviteSubAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def invite_sub_account_with_options_async(
        self,
        request: agency_20221216_models.InviteSubAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.InviteSubAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_info_list):
            query['AccountInfoList'] = request.account_info_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InviteSubAccount',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.InviteSubAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invite_sub_account(
        self,
        request: agency_20221216_models.InviteSubAccountRequest,
    ) -> agency_20221216_models.InviteSubAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.invite_sub_account_with_options(request, runtime)

    async def invite_sub_account_async(
        self,
        request: agency_20221216_models.InviteSubAccountRequest,
    ) -> agency_20221216_models.InviteSubAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invite_sub_account_with_options_async(request, runtime)

    def list_countries_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.ListCountriesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListCountries',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.ListCountriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_countries_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.ListCountriesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListCountries',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.ListCountriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_countries(self) -> agency_20221216_models.ListCountriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_countries_with_options(runtime)

    async def list_countries_async(self) -> agency_20221216_models.ListCountriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_countries_with_options_async(runtime)

    def resend_email_with_options(
        self,
        request: agency_20221216_models.ResendEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.ResendEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.invite_id):
            query['InviteId'] = request.invite_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendEmail',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.ResendEmailResponse(),
            self.call_api(params, req, runtime)
        )

    async def resend_email_with_options_async(
        self,
        request: agency_20221216_models.ResendEmailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.ResendEmailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.invite_id):
            query['InviteId'] = request.invite_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendEmail',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.ResendEmailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resend_email(
        self,
        request: agency_20221216_models.ResendEmailRequest,
    ) -> agency_20221216_models.ResendEmailResponse:
        runtime = util_models.RuntimeOptions()
        return self.resend_email_with_options(request, runtime)

    async def resend_email_async(
        self,
        request: agency_20221216_models.ResendEmailRequest,
    ) -> agency_20221216_models.ResendEmailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resend_email_with_options_async(request, runtime)

    def set_account_info_with_options(
        self,
        request: agency_20221216_models.SetAccountInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.SetAccountInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_nickname):
            query['AccountNickname'] = request.account_nickname
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccountInfo',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.SetAccountInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_account_info_with_options_async(
        self,
        request: agency_20221216_models.SetAccountInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.SetAccountInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_nickname):
            query['AccountNickname'] = request.account_nickname
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccountInfo',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.SetAccountInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_account_info(
        self,
        request: agency_20221216_models.SetAccountInfoRequest,
    ) -> agency_20221216_models.SetAccountInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_account_info_with_options(request, runtime)

    async def set_account_info_async(
        self,
        request: agency_20221216_models.SetAccountInfoRequest,
    ) -> agency_20221216_models.SetAccountInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_account_info_with_options_async(request, runtime)

    def set_credit_line_with_options(
        self,
        request: agency_20221216_models.SetCreditLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.SetCreditLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credit_line):
            query['CreditLine'] = request.credit_line
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCreditLine',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.SetCreditLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_credit_line_with_options_async(
        self,
        request: agency_20221216_models.SetCreditLineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.SetCreditLineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credit_line):
            query['CreditLine'] = request.credit_line
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCreditLine',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.SetCreditLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_credit_line(
        self,
        request: agency_20221216_models.SetCreditLineRequest,
    ) -> agency_20221216_models.SetCreditLineResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_credit_line_with_options(request, runtime)

    async def set_credit_line_async(
        self,
        request: agency_20221216_models.SetCreditLineRequest,
    ) -> agency_20221216_models.SetCreditLineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_credit_line_with_options_async(request, runtime)

    def set_warning_threshold_with_options(
        self,
        request: agency_20221216_models.SetWarningThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.SetWarningThresholdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.warning_value):
            query['WarningValue'] = request.warning_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetWarningThreshold',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.SetWarningThresholdResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_warning_threshold_with_options_async(
        self,
        request: agency_20221216_models.SetWarningThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.SetWarningThresholdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        if not UtilClient.is_unset(request.warning_value):
            query['WarningValue'] = request.warning_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetWarningThreshold',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.SetWarningThresholdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_warning_threshold(
        self,
        request: agency_20221216_models.SetWarningThresholdRequest,
    ) -> agency_20221216_models.SetWarningThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_warning_threshold_with_options(request, runtime)

    async def set_warning_threshold_async(
        self,
        request: agency_20221216_models.SetWarningThresholdRequest,
    ) -> agency_20221216_models.SetWarningThresholdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_warning_threshold_with_options_async(request, runtime)

    def subscription_bill_with_options(
        self,
        request: agency_20221216_models.SubscriptionBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.SubscriptionBillResponse:
        """
        Make sure that you are a distributor of the Alibaba Cloud international ecosystem.
        *   You can call this operation to subscribe to only one type of bill at a time.
        *   After the subscription to a type of bill is generated, the bill for the previous day is pushed on a daily basis from the next day. On the fifth day of each month, the full-data bill for the previous month is pushed.
        *   A daily bill may be delayed. The delayed bill is pushed the next day after it is generated. The delayed bill may contain the bill data that is delayed until the previous day. We recommend that you query the full-data bill for the previous month at the beginning of each month.
        *   Your account must be granted the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission.
        *   The following file name formats are supported for bills:
        ```
        BillingItemDetailForBillingPeriod
        
        File name format of a daily bill: UID_PartnerBillingItemDetail_YYYYMMDD_SquenceNo_fileNo. Example: 169**_BillingItemDetail_20190310_0001_01.
        
        File name format of a monthly full-data bill: UID_PartnerBillingItemDetail_YYYYMM_SquenceNo_fileNo. Example: 169**_BillingItemDetail_201903_0001_01.
        InstanceDetailForBillingPeriod
        
        File name format of a daily bill: UID_PartnerInstanceDetail_YYYYMMDD_SquenceNo_fileNo. Example: 169**_InstanceDetail_20190310_0001_01.
        
        File name format of a monthly full-data bill: UID_PartnerInstanceDetail_YYYYMM_SquenceNo_fileNo. Example: 169**_InstanceDetail_201903_1999-0001_01.
        BillingItemDetailMonthly
        
        File name format of a daily bill: UID_PartnerBillingItemDetailMonthly_YYYYMM_SquenceNo_fileNo. Example: 169**_BillingItemDetailMonthly_201903_0001_01. This bill contains the bill data that is generated from the beginning of the current month to the fifth day of the next month.
        InstanceDetailMonthly
        
        File name format of a daily bill: UID_PartnerInstanceDetailMonthly_YYYYMM_SquenceNo_fileNo. Example: 169**_InstanceDetailMonthly_201903_0001_01. This bill contains the bill data that is generated from the beginning of the current month to the fifth day of the next month.
        The fileNo field exists only when the number of bill rows reaches the maximum rows in a single bill file and the bill is split into multiple files.
        ```
        **This topic is published only on the international site (alibabacloud.com).
        
        @param request: SubscriptionBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubscriptionBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not UtilClient.is_unset(request.bill_format):
            query['BillFormat'] = request.bill_format
        if not UtilClient.is_unset(request.bucket_owner_id):
            query['BucketOwnerId'] = request.bucket_owner_id
        if not UtilClient.is_unset(request.subscribe_bucket):
            query['SubscribeBucket'] = request.subscribe_bucket
        if not UtilClient.is_unset(request.subscribe_segment_size):
            query['SubscribeSegmentSize'] = request.subscribe_segment_size
        if not UtilClient.is_unset(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubscriptionBill',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.SubscriptionBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def subscription_bill_with_options_async(
        self,
        request: agency_20221216_models.SubscriptionBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> agency_20221216_models.SubscriptionBillResponse:
        """
        Make sure that you are a distributor of the Alibaba Cloud international ecosystem.
        *   You can call this operation to subscribe to only one type of bill at a time.
        *   After the subscription to a type of bill is generated, the bill for the previous day is pushed on a daily basis from the next day. On the fifth day of each month, the full-data bill for the previous month is pushed.
        *   A daily bill may be delayed. The delayed bill is pushed the next day after it is generated. The delayed bill may contain the bill data that is delayed until the previous day. We recommend that you query the full-data bill for the previous month at the beginning of each month.
        *   Your account must be granted the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission.
        *   The following file name formats are supported for bills:
        ```
        BillingItemDetailForBillingPeriod
        
        File name format of a daily bill: UID_PartnerBillingItemDetail_YYYYMMDD_SquenceNo_fileNo. Example: 169**_BillingItemDetail_20190310_0001_01.
        
        File name format of a monthly full-data bill: UID_PartnerBillingItemDetail_YYYYMM_SquenceNo_fileNo. Example: 169**_BillingItemDetail_201903_0001_01.
        InstanceDetailForBillingPeriod
        
        File name format of a daily bill: UID_PartnerInstanceDetail_YYYYMMDD_SquenceNo_fileNo. Example: 169**_InstanceDetail_20190310_0001_01.
        
        File name format of a monthly full-data bill: UID_PartnerInstanceDetail_YYYYMM_SquenceNo_fileNo. Example: 169**_InstanceDetail_201903_1999-0001_01.
        BillingItemDetailMonthly
        
        File name format of a daily bill: UID_PartnerBillingItemDetailMonthly_YYYYMM_SquenceNo_fileNo. Example: 169**_BillingItemDetailMonthly_201903_0001_01. This bill contains the bill data that is generated from the beginning of the current month to the fifth day of the next month.
        InstanceDetailMonthly
        
        File name format of a daily bill: UID_PartnerInstanceDetailMonthly_YYYYMM_SquenceNo_fileNo. Example: 169**_InstanceDetailMonthly_201903_0001_01. This bill contains the bill data that is generated from the beginning of the current month to the fifth day of the next month.
        The fileNo field exists only when the number of bill rows reaches the maximum rows in a single bill file and the bill is split into multiple files.
        ```
        **This topic is published only on the international site (alibabacloud.com).
        
        @param request: SubscriptionBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubscriptionBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not UtilClient.is_unset(request.bill_format):
            query['BillFormat'] = request.bill_format
        if not UtilClient.is_unset(request.bucket_owner_id):
            query['BucketOwnerId'] = request.bucket_owner_id
        if not UtilClient.is_unset(request.subscribe_bucket):
            query['SubscribeBucket'] = request.subscribe_bucket
        if not UtilClient.is_unset(request.subscribe_segment_size):
            query['SubscribeSegmentSize'] = request.subscribe_segment_size
        if not UtilClient.is_unset(request.subscribe_type):
            query['SubscribeType'] = request.subscribe_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubscriptionBill',
            version='2022-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            agency_20221216_models.SubscriptionBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def subscription_bill(
        self,
        request: agency_20221216_models.SubscriptionBillRequest,
    ) -> agency_20221216_models.SubscriptionBillResponse:
        """
        Make sure that you are a distributor of the Alibaba Cloud international ecosystem.
        *   You can call this operation to subscribe to only one type of bill at a time.
        *   After the subscription to a type of bill is generated, the bill for the previous day is pushed on a daily basis from the next day. On the fifth day of each month, the full-data bill for the previous month is pushed.
        *   A daily bill may be delayed. The delayed bill is pushed the next day after it is generated. The delayed bill may contain the bill data that is delayed until the previous day. We recommend that you query the full-data bill for the previous month at the beginning of each month.
        *   Your account must be granted the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission.
        *   The following file name formats are supported for bills:
        ```
        BillingItemDetailForBillingPeriod
        
        File name format of a daily bill: UID_PartnerBillingItemDetail_YYYYMMDD_SquenceNo_fileNo. Example: 169**_BillingItemDetail_20190310_0001_01.
        
        File name format of a monthly full-data bill: UID_PartnerBillingItemDetail_YYYYMM_SquenceNo_fileNo. Example: 169**_BillingItemDetail_201903_0001_01.
        InstanceDetailForBillingPeriod
        
        File name format of a daily bill: UID_PartnerInstanceDetail_YYYYMMDD_SquenceNo_fileNo. Example: 169**_InstanceDetail_20190310_0001_01.
        
        File name format of a monthly full-data bill: UID_PartnerInstanceDetail_YYYYMM_SquenceNo_fileNo. Example: 169**_InstanceDetail_201903_1999-0001_01.
        BillingItemDetailMonthly
        
        File name format of a daily bill: UID_PartnerBillingItemDetailMonthly_YYYYMM_SquenceNo_fileNo. Example: 169**_BillingItemDetailMonthly_201903_0001_01. This bill contains the bill data that is generated from the beginning of the current month to the fifth day of the next month.
        InstanceDetailMonthly
        
        File name format of a daily bill: UID_PartnerInstanceDetailMonthly_YYYYMM_SquenceNo_fileNo. Example: 169**_InstanceDetailMonthly_201903_0001_01. This bill contains the bill data that is generated from the beginning of the current month to the fifth day of the next month.
        The fileNo field exists only when the number of bill rows reaches the maximum rows in a single bill file and the bill is split into multiple files.
        ```
        **This topic is published only on the international site (alibabacloud.com).
        
        @param request: SubscriptionBillRequest
        @return: SubscriptionBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.subscription_bill_with_options(request, runtime)

    async def subscription_bill_async(
        self,
        request: agency_20221216_models.SubscriptionBillRequest,
    ) -> agency_20221216_models.SubscriptionBillResponse:
        """
        Make sure that you are a distributor of the Alibaba Cloud international ecosystem.
        *   You can call this operation to subscribe to only one type of bill at a time.
        *   After the subscription to a type of bill is generated, the bill for the previous day is pushed on a daily basis from the next day. On the fifth day of each month, the full-data bill for the previous month is pushed.
        *   A daily bill may be delayed. The delayed bill is pushed the next day after it is generated. The delayed bill may contain the bill data that is delayed until the previous day. We recommend that you query the full-data bill for the previous month at the beginning of each month.
        *   Your account must be granted the [AliyunConsumeDump2OSSRole](https://ram.console.aliyun.com/?spm=api-workbench.API%20Document.0.0.68c71e0fhmTSJp#/role/authorize?request=%7B%22Requests%22:%20%7B%22request1%22:%20%7B%22RoleName%22:%20%22AliyunConsumeDump2OSSRole%22,%20%22TemplateId%22:%20%22Dump2OSSRole%22%7D%7D,%20%22ReturnUrl%22:%20%22https:%2F%2Fusercenter2.aliyun.com%22,%20%22Service%22:%20%22Consume%22%7D) permission.
        *   The following file name formats are supported for bills:
        ```
        BillingItemDetailForBillingPeriod
        
        File name format of a daily bill: UID_PartnerBillingItemDetail_YYYYMMDD_SquenceNo_fileNo. Example: 169**_BillingItemDetail_20190310_0001_01.
        
        File name format of a monthly full-data bill: UID_PartnerBillingItemDetail_YYYYMM_SquenceNo_fileNo. Example: 169**_BillingItemDetail_201903_0001_01.
        InstanceDetailForBillingPeriod
        
        File name format of a daily bill: UID_PartnerInstanceDetail_YYYYMMDD_SquenceNo_fileNo. Example: 169**_InstanceDetail_20190310_0001_01.
        
        File name format of a monthly full-data bill: UID_PartnerInstanceDetail_YYYYMM_SquenceNo_fileNo. Example: 169**_InstanceDetail_201903_1999-0001_01.
        BillingItemDetailMonthly
        
        File name format of a daily bill: UID_PartnerBillingItemDetailMonthly_YYYYMM_SquenceNo_fileNo. Example: 169**_BillingItemDetailMonthly_201903_0001_01. This bill contains the bill data that is generated from the beginning of the current month to the fifth day of the next month.
        InstanceDetailMonthly
        
        File name format of a daily bill: UID_PartnerInstanceDetailMonthly_YYYYMM_SquenceNo_fileNo. Example: 169**_InstanceDetailMonthly_201903_0001_01. This bill contains the bill data that is generated from the beginning of the current month to the fifth day of the next month.
        The fileNo field exists only when the number of bill rows reaches the maximum rows in a single bill file and the bill is split into multiple files.
        ```
        **This topic is published only on the international site (alibabacloud.com).
        
        @param request: SubscriptionBillRequest
        @return: SubscriptionBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.subscription_bill_with_options_async(request, runtime)
