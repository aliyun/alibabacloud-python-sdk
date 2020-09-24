# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_bssopenapi20171214 import models as bss_open_api_20171214_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self._endpoint_map = {
            "ap-northeast-1": "business.ap-southeast-1.aliyuncs.com",
            "ap-northeast-2-pop": "business.ap-southeast-1.aliyuncs.com",
            "ap-south-1": "business.ap-southeast-1.aliyuncs.com",
            "ap-southeast-1": "business.ap-southeast-1.aliyuncs.com",
            "ap-southeast-2": "business.ap-southeast-1.aliyuncs.com",
            "ap-southeast-3": "business.ap-southeast-1.aliyuncs.com",
            "ap-southeast-5": "business.ap-southeast-1.aliyuncs.com",
            "cn-beijing": "business.aliyuncs.com",
            "cn-beijing-finance-1": "business.aliyuncs.com",
            "cn-beijing-finance-pop": "business.aliyuncs.com",
            "cn-beijing-gov-1": "business.aliyuncs.com",
            "cn-beijing-nu16-b01": "business.aliyuncs.com",
            "cn-chengdu": "business.aliyuncs.com",
            "cn-edge-1": "business.aliyuncs.com",
            "cn-fujian": "business.aliyuncs.com",
            "cn-haidian-cm12-c01": "business.aliyuncs.com",
            "cn-hangzhou": "business.aliyuncs.com",
            "cn-hangzhou-bj-b01": "business.aliyuncs.com",
            "cn-hangzhou-finance": "business.aliyuncs.com",
            "cn-hangzhou-internal-prod-1": "business.aliyuncs.com",
            "cn-hangzhou-internal-test-1": "business.aliyuncs.com",
            "cn-hangzhou-internal-test-2": "business.aliyuncs.com",
            "cn-hangzhou-internal-test-3": "business.aliyuncs.com",
            "cn-hangzhou-test-306": "business.aliyuncs.com",
            "cn-hongkong": "business.aliyuncs.com",
            "cn-hongkong-finance-pop": "business.aliyuncs.com",
            "cn-huhehaote": "business.aliyuncs.com",
            "cn-north-2-gov-1": "business.aliyuncs.com",
            "cn-qingdao": "business.aliyuncs.com",
            "cn-qingdao-nebula": "business.aliyuncs.com",
            "cn-shanghai": "business.aliyuncs.com",
            "cn-shanghai-et15-b01": "business.aliyuncs.com",
            "cn-shanghai-et2-b01": "business.aliyuncs.com",
            "cn-shanghai-finance-1": "business.aliyuncs.com",
            "cn-shanghai-inner": "business.aliyuncs.com",
            "cn-shanghai-internal-test-1": "business.aliyuncs.com",
            "cn-shenzhen": "business.aliyuncs.com",
            "cn-shenzhen-finance-1": "business.aliyuncs.com",
            "cn-shenzhen-inner": "business.aliyuncs.com",
            "cn-shenzhen-st4-d01": "business.aliyuncs.com",
            "cn-shenzhen-su18-b01": "business.aliyuncs.com",
            "cn-wuhan": "business.aliyuncs.com",
            "cn-yushanfang": "business.aliyuncs.com",
            "cn-zhangbei-na61-b01": "business.aliyuncs.com",
            "cn-zhangjiakou": "business.aliyuncs.com",
            "cn-zhangjiakou-na62-a01": "business.aliyuncs.com",
            "cn-zhengzhou-nebula-1": "business.aliyuncs.com",
            "eu-central-1": "business.ap-southeast-1.aliyuncs.com",
            "eu-west-1": "business.ap-southeast-1.aliyuncs.com",
            "eu-west-1-oxs": "business.ap-southeast-1.aliyuncs.com",
            "me-east-1": "business.ap-southeast-1.aliyuncs.com",
            "rus-west-1-pop": "business.ap-southeast-1.aliyuncs.com",
            "us-east-1": "business.ap-southeast-1.aliyuncs.com",
            "us-west-1": "business.ap-southeast-1.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint("bssopenapi", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def query_account_transaction_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryAccountTransactionDetailsResponse().from_map(self.do_request("QueryAccountTransactionDetails", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_account_transaction_details(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_account_transaction_details_with_options(request, runtime)

    def query_settle_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QuerySettleBillResponse().from_map(self.do_request("QuerySettleBill", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_settle_bill(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_settle_bill_with_options(request, runtime)

    def query_split_item_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QuerySplitItemBillResponse().from_map(self.do_request("QuerySplitItemBill", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_split_item_bill(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_split_item_bill_with_options(request, runtime)

    def query_riutilization_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryRIUtilizationDetailResponse().from_map(self.do_request("QueryRIUtilizationDetail", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_riutilization_detail(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_riutilization_detail_with_options(request, runtime)

    def query_bill_to_osssubscription_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryBillToOSSSubscriptionResponse().from_map(self.do_request("QueryBillToOSSSubscription", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_bill_to_osssubscription(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_bill_to_osssubscription_with_options(request, runtime)

    def query_account_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryAccountBillResponse().from_map(self.do_request("QueryAccountBill", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_account_bill(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_account_bill_with_options(request, runtime)

    def create_cost_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.CreateCostUnitResponse().from_map(self.do_request("CreateCostUnit", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def create_cost_unit(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_cost_unit_with_options(request, runtime)

    def modify_cost_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.ModifyCostUnitResponse().from_map(self.do_request("ModifyCostUnit", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def modify_cost_unit(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_cost_unit_with_options(request, runtime)

    def query_cost_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryCostUnitResponse().from_map(self.do_request("QueryCostUnit", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_cost_unit(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_cost_unit_with_options(request, runtime)

    def delete_cost_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.DeleteCostUnitResponse().from_map(self.do_request("DeleteCostUnit", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def delete_cost_unit(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_cost_unit_with_options(request, runtime)

    def allocate_cost_unit_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.AllocateCostUnitResourceResponse().from_map(self.do_request("AllocateCostUnitResource", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def allocate_cost_unit_resource(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.allocate_cost_unit_resource_with_options(request, runtime)

    def query_cost_unit_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryCostUnitResourceResponse().from_map(self.do_request("QueryCostUnitResource", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_cost_unit_resource(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_cost_unit_resource_with_options(request, runtime)

    def renew_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.RenewResourcePackageResponse().from_map(self.do_request("RenewResourcePackage", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def renew_resource_package(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.renew_resource_package_with_options(request, runtime)

    def upgrade_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.UpgradeResourcePackageResponse().from_map(self.do_request("UpgradeResourcePackage", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def upgrade_resource_package(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.upgrade_resource_package_with_options(request, runtime)

    def create_ag_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.CreateAgAccountResponse().from_map(self.do_request("CreateAgAccount", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def create_ag_account(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_ag_account_with_options(request, runtime)

    def get_customer_account_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.GetCustomerAccountInfoResponse().from_map(self.do_request("GetCustomerAccountInfo", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def get_customer_account_info(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_customer_account_info_with_options(request, runtime)

    def get_customer_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.GetCustomerListResponse().from_map(self.do_request("GetCustomerList", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def get_customer_list(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_customer_list_with_options(request, runtime)

    def change_reseller_consume_amount_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.ChangeResellerConsumeAmountResponse().from_map(self.do_request("ChangeResellerConsumeAmount", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def change_reseller_consume_amount(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.change_reseller_consume_amount_with_options(request, runtime)

    def set_reseller_user_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.SetResellerUserStatusResponse().from_map(self.do_request("SetResellerUserStatus", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def set_reseller_user_status(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.set_reseller_user_status_with_options(request, runtime)

    def create_reseller_user_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.CreateResellerUserQuotaResponse().from_map(self.do_request("CreateResellerUserQuota", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def create_reseller_user_quota(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_reseller_user_quota_with_options(request, runtime)

    def set_reseller_user_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.SetResellerUserQuotaResponse().from_map(self.do_request("SetResellerUserQuota", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def set_reseller_user_quota(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.set_reseller_user_quota_with_options(request, runtime)

    def query_reseller_available_quota_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryResellerAvailableQuotaResponse().from_map(self.do_request("QueryResellerAvailableQuota", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_reseller_available_quota(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_reseller_available_quota_with_options(request, runtime)

    def set_reseller_user_alarm_threshold_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.SetResellerUserAlarmThresholdResponse().from_map(self.do_request("SetResellerUserAlarmThreshold", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def set_reseller_user_alarm_threshold(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.set_reseller_user_alarm_threshold_with_options(request, runtime)

    def query_account_transactions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryAccountTransactionsResponse().from_map(self.do_request("QueryAccountTransactions", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_account_transactions(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_account_transactions_with_options(request, runtime)

    def unsubscribe_bill_to_osswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.UnsubscribeBillToOSSResponse().from_map(self.do_request("UnsubscribeBillToOSS", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def unsubscribe_bill_to_oss(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.unsubscribe_bill_to_osswith_options(request, runtime)

    def subscribe_bill_to_osswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.SubscribeBillToOSSResponse().from_map(self.do_request("SubscribeBillToOSS", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def subscribe_bill_to_oss(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.subscribe_bill_to_osswith_options(request, runtime)

    def query_user_oms_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryUserOmsDataResponse().from_map(self.do_request("QueryUserOmsData", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_user_oms_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_user_oms_data_with_options(request, runtime)

    def cancel_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.CancelOrderResponse().from_map(self.do_request("CancelOrder", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def cancel_order(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.cancel_order_with_options(request, runtime)

    def apply_invoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.ApplyInvoiceResponse().from_map(self.do_request("ApplyInvoice", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def apply_invoice(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.apply_invoice_with_options(request, runtime)

    def query_customer_address_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryCustomerAddressListResponse().from_map(self.do_request("QueryCustomerAddressList", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_customer_address_list(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_customer_address_list_with_options(request, runtime)

    def query_evaluate_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryEvaluateListResponse().from_map(self.do_request("QueryEvaluateList", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_evaluate_list(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_evaluate_list_with_options(request, runtime)

    def query_invoicing_customer_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryInvoicingCustomerListResponse().from_map(self.do_request("QueryInvoicingCustomerList", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_invoicing_customer_list(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_invoicing_customer_list_with_options(request, runtime)

    def query_bill_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryBillOverviewResponse().from_map(self.do_request("QueryBillOverview", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_bill_overview(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_bill_overview_with_options(request, runtime)

    def query_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryBillResponse().from_map(self.do_request("QueryBill", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_bill(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_bill_with_options(request, runtime)

    def query_instance_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryInstanceBillResponse().from_map(self.do_request("QueryInstanceBill", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_instance_bill(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_instance_bill_with_options(request, runtime)

    def enable_bill_generation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.EnableBillGenerationResponse().from_map(self.do_request("EnableBillGeneration", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def enable_bill_generation(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.enable_bill_generation_with_options(request, runtime)

    def query_redeem_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryRedeemResponse().from_map(self.do_request("QueryRedeem", "HTTPS", "GET", "2017-12-14", "AK", request.to_map(), None, runtime))

    def query_redeem(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_redeem_with_options(request, runtime)

    def convert_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.ConvertChargeTypeResponse().from_map(self.do_request("ConvertChargeType", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def convert_charge_type(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.convert_charge_type_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.CreateInstanceResponse().from_map(self.do_request("CreateInstance", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_instance_with_options(request, runtime)

    def modify_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.ModifyInstanceResponse().from_map(self.do_request("ModifyInstance", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def modify_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_instance_with_options(request, runtime)

    def describe_pricing_module_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.DescribePricingModuleResponse().from_map(self.do_request("DescribePricingModule", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def describe_pricing_module(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_pricing_module_with_options(request, runtime)

    def query_product_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryProductListResponse().from_map(self.do_request("QueryProductList", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_product_list(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_product_list_with_options(request, runtime)

    def query_instance_gaap_cost_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryInstanceGaapCostResponse().from_map(self.do_request("QueryInstanceGaapCost", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_instance_gaap_cost(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_instance_gaap_cost_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.RenewInstanceResponse().from_map(self.do_request("RenewInstance", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.renew_instance_with_options(request, runtime)

    def get_order_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.GetOrderDetailResponse().from_map(self.do_request("GetOrderDetail", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def get_order_detail(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_order_detail_with_options(request, runtime)

    def query_orders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryOrdersResponse().from_map(self.do_request("QueryOrders", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_orders(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_orders_with_options(request, runtime)

    def query_monthly_instance_consumption_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryMonthlyInstanceConsumptionResponse().from_map(self.do_request("QueryMonthlyInstanceConsumption", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_monthly_instance_consumption(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_monthly_instance_consumption_with_options(request, runtime)

    def query_settlement_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QuerySettlementBillResponse().from_map(self.do_request("QuerySettlementBill", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_settlement_bill(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_settlement_bill_with_options(request, runtime)

    def query_monthly_bill_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryMonthlyBillResponse().from_map(self.do_request("QueryMonthlyBill", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_monthly_bill(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_monthly_bill_with_options(request, runtime)

    def set_renewal_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.SetRenewalResponse().from_map(self.do_request("SetRenewal", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def set_renewal(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.set_renewal_with_options(request, runtime)

    def query_available_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryAvailableInstancesResponse().from_map(self.do_request("QueryAvailableInstances", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_available_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_available_instances_with_options(request, runtime)

    def create_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.CreateResourcePackageResponse().from_map(self.do_request("CreateResourcePackage", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def create_resource_package(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_resource_package_with_options(request, runtime)

    def query_resource_package_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryResourcePackageInstancesResponse().from_map(self.do_request("QueryResourcePackageInstances", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_resource_package_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_resource_package_instances_with_options(request, runtime)

    def get_resource_package_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.GetResourcePackagePriceResponse().from_map(self.do_request("GetResourcePackagePrice", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def get_resource_package_price(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_resource_package_price_with_options(request, runtime)

    def get_subscription_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.GetSubscriptionPriceResponse().from_map(self.do_request("GetSubscriptionPrice", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def get_subscription_price(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_subscription_price_with_options(request, runtime)

    def get_pay_as_you_go_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.GetPayAsYouGoPriceResponse().from_map(self.do_request("GetPayAsYouGoPrice", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def get_pay_as_you_go_price(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_pay_as_you_go_price_with_options(request, runtime)

    def query_prepaid_cards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryPrepaidCardsResponse().from_map(self.do_request("QueryPrepaidCards", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_prepaid_cards(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_prepaid_cards_with_options(request, runtime)

    def query_cash_coupons_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryCashCouponsResponse().from_map(self.do_request("QueryCashCoupons", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_cash_coupons(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_cash_coupons_with_options(request, runtime)

    def query_account_balance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.QueryAccountBalanceResponse().from_map(self.do_request("QueryAccountBalance", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def query_account_balance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.query_account_balance_with_options(request, runtime)

    def describe_resource_package_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return bss_open_api_20171214_models.DescribeResourcePackageProductResponse().from_map(self.do_request("DescribeResourcePackageProduct", "HTTPS", "POST", "2017-12-14", "AK", None, request.to_map(), runtime))

    def describe_resource_package_product(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_resource_package_product_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
