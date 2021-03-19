# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

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
            'ap-northeast-1': 'business.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2-pop': 'business.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'business.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'business.ap-southeast-1.aliyuncs.com',
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
            'cn-hangzhou': 'business.aliyuncs.com',
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
            'cn-north-2-gov-1': 'business.aliyuncs.com',
            'cn-qingdao': 'business.aliyuncs.com',
            'cn-qingdao-nebula': 'business.aliyuncs.com',
            'cn-shanghai': 'business.aliyuncs.com',
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
            'cn-yushanfang': 'business.aliyuncs.com',
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

    def allocate_cost_unit_resource_with_options(
        self,
        request: bss_open_api_20171214_models.AllocateCostUnitResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.AllocateCostUnitResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.AllocateCostUnitResourceResponse().from_map(
            self.do_rpcrequest('AllocateCostUnitResource', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_cost_unit_resource_with_options_async(
        self,
        request: bss_open_api_20171214_models.AllocateCostUnitResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.AllocateCostUnitResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.AllocateCostUnitResourceResponse().from_map(
            await self.do_rpcrequest_async('AllocateCostUnitResource', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ApplyInvoiceResponse().from_map(
            self.do_rpcrequest('ApplyInvoice', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_invoice_with_options_async(
        self,
        request: bss_open_api_20171214_models.ApplyInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ApplyInvoiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ApplyInvoiceResponse().from_map(
            await self.do_rpcrequest_async('ApplyInvoice', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CancelOrderResponse().from_map(
            self.do_rpcrequest('CancelOrder', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_order_with_options_async(
        self,
        request: bss_open_api_20171214_models.CancelOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CancelOrderResponse().from_map(
            await self.do_rpcrequest_async('CancelOrder', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ChangeResellerConsumeAmountResponse().from_map(
            self.do_rpcrequest('ChangeResellerConsumeAmount', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_reseller_consume_amount_with_options_async(
        self,
        request: bss_open_api_20171214_models.ChangeResellerConsumeAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ChangeResellerConsumeAmountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ChangeResellerConsumeAmountResponse().from_map(
            await self.do_rpcrequest_async('ChangeResellerConsumeAmount', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def convert_charge_type_with_options(
        self,
        request: bss_open_api_20171214_models.ConvertChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ConvertChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ConvertChargeTypeResponse().from_map(
            self.do_rpcrequest('ConvertChargeType', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def convert_charge_type_with_options_async(
        self,
        request: bss_open_api_20171214_models.ConvertChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ConvertChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ConvertChargeTypeResponse().from_map(
            await self.do_rpcrequest_async('ConvertChargeType', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateAgAccountResponse().from_map(
            self.do_rpcrequest('CreateAgAccount', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ag_account_with_options_async(
        self,
        request: bss_open_api_20171214_models.CreateAgAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateAgAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateAgAccountResponse().from_map(
            await self.do_rpcrequest_async('CreateAgAccount', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ag_account(
        self,
        request: bss_open_api_20171214_models.CreateAgAccountRequest,
    ) -> bss_open_api_20171214_models.CreateAgAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ag_account_with_options(request, runtime)

    async def create_ag_account_async(
        self,
        request: bss_open_api_20171214_models.CreateAgAccountRequest,
    ) -> bss_open_api_20171214_models.CreateAgAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ag_account_with_options_async(request, runtime)

    def create_cost_unit_with_options(
        self,
        request: bss_open_api_20171214_models.CreateCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateCostUnitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateCostUnitResponse().from_map(
            self.do_rpcrequest('CreateCostUnit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cost_unit_with_options_async(
        self,
        request: bss_open_api_20171214_models.CreateCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateCostUnitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateCostUnitResponse().from_map(
            await self.do_rpcrequest_async('CreateCostUnit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateInstanceResponse().from_map(
            self.do_rpcrequest('CreateInstance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: bss_open_api_20171214_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateInstance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateResellerUserQuotaResponse().from_map(
            self.do_rpcrequest('CreateResellerUserQuota', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_reseller_user_quota_with_options_async(
        self,
        request: bss_open_api_20171214_models.CreateResellerUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateResellerUserQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateResellerUserQuotaResponse().from_map(
            await self.do_rpcrequest_async('CreateResellerUserQuota', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateResourcePackageResponse().from_map(
            self.do_rpcrequest('CreateResourcePackage', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_resource_package_with_options_async(
        self,
        request: bss_open_api_20171214_models.CreateResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.CreateResourcePackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.CreateResourcePackageResponse().from_map(
            await self.do_rpcrequest_async('CreateResourcePackage', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_cost_unit_with_options(
        self,
        request: bss_open_api_20171214_models.DeleteCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DeleteCostUnitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.DeleteCostUnitResponse().from_map(
            self.do_rpcrequest('DeleteCostUnit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cost_unit_with_options_async(
        self,
        request: bss_open_api_20171214_models.DeleteCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DeleteCostUnitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.DeleteCostUnitResponse().from_map(
            await self.do_rpcrequest_async('DeleteCostUnit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_resource_package_product_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeResourcePackageProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeResourcePackageProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.DescribeResourcePackageProductResponse().from_map(
            self.do_rpcrequest('DescribeResourcePackageProduct', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_resource_package_product_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeResourcePackageProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeResourcePackageProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.DescribeResourcePackageProductResponse().from_map(
            await self.do_rpcrequest_async('DescribeResourcePackageProduct', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_split_item_bill_with_options(
        self,
        request: bss_open_api_20171214_models.DescribeSplitItemBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeSplitItemBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.DescribeSplitItemBillResponse().from_map(
            self.do_rpcrequest('DescribeSplitItemBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_split_item_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.DescribeSplitItemBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.DescribeSplitItemBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.DescribeSplitItemBillResponse().from_map(
            await self.do_rpcrequest_async('DescribeSplitItemBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_split_item_bill(
        self,
        request: bss_open_api_20171214_models.DescribeSplitItemBillRequest,
    ) -> bss_open_api_20171214_models.DescribeSplitItemBillResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_split_item_bill_with_options(request, runtime)

    async def describe_split_item_bill_async(
        self,
        request: bss_open_api_20171214_models.DescribeSplitItemBillRequest,
    ) -> bss_open_api_20171214_models.DescribeSplitItemBillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_split_item_bill_with_options_async(request, runtime)

    def enable_bill_generation_with_options(
        self,
        request: bss_open_api_20171214_models.EnableBillGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.EnableBillGenerationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.EnableBillGenerationResponse().from_map(
            self.do_rpcrequest('EnableBillGeneration', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_bill_generation_with_options_async(
        self,
        request: bss_open_api_20171214_models.EnableBillGenerationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.EnableBillGenerationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.EnableBillGenerationResponse().from_map(
            await self.do_rpcrequest_async('EnableBillGeneration', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_customer_account_info_with_options(
        self,
        request: bss_open_api_20171214_models.GetCustomerAccountInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetCustomerAccountInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetCustomerAccountInfoResponse().from_map(
            self.do_rpcrequest('GetCustomerAccountInfo', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_customer_account_info_with_options_async(
        self,
        request: bss_open_api_20171214_models.GetCustomerAccountInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetCustomerAccountInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetCustomerAccountInfoResponse().from_map(
            await self.do_rpcrequest_async('GetCustomerAccountInfo', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest()
        return bss_open_api_20171214_models.GetCustomerListResponse().from_map(
            self.do_rpcrequest('GetCustomerList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_customer_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetCustomerListResponse:
        req = open_api_models.OpenApiRequest()
        return bss_open_api_20171214_models.GetCustomerListResponse().from_map(
            await self.do_rpcrequest_async('GetCustomerList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_customer_list(self) -> bss_open_api_20171214_models.GetCustomerListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_customer_list_with_options(runtime)

    async def get_customer_list_async(self) -> bss_open_api_20171214_models.GetCustomerListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_customer_list_with_options_async(runtime)

    def get_order_detail_with_options(
        self,
        request: bss_open_api_20171214_models.GetOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetOrderDetailResponse().from_map(
            self.do_rpcrequest('GetOrderDetail', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_order_detail_with_options_async(
        self,
        request: bss_open_api_20171214_models.GetOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetOrderDetailResponse().from_map(
            await self.do_rpcrequest_async('GetOrderDetail', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetPayAsYouGoPriceResponse().from_map(
            self.do_rpcrequest('GetPayAsYouGoPrice', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_pay_as_you_go_price_with_options_async(
        self,
        request: bss_open_api_20171214_models.GetPayAsYouGoPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetPayAsYouGoPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetPayAsYouGoPriceResponse().from_map(
            await self.do_rpcrequest_async('GetPayAsYouGoPrice', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_pay_as_you_go_price(
        self,
        request: bss_open_api_20171214_models.GetPayAsYouGoPriceRequest,
    ) -> bss_open_api_20171214_models.GetPayAsYouGoPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pay_as_you_go_price_with_options(request, runtime)

    async def get_pay_as_you_go_price_async(
        self,
        request: bss_open_api_20171214_models.GetPayAsYouGoPriceRequest,
    ) -> bss_open_api_20171214_models.GetPayAsYouGoPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pay_as_you_go_price_with_options_async(request, runtime)

    def get_resource_package_price_with_options(
        self,
        request: bss_open_api_20171214_models.GetResourcePackagePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetResourcePackagePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetResourcePackagePriceResponse().from_map(
            self.do_rpcrequest('GetResourcePackagePrice', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_resource_package_price_with_options_async(
        self,
        request: bss_open_api_20171214_models.GetResourcePackagePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetResourcePackagePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetResourcePackagePriceResponse().from_map(
            await self.do_rpcrequest_async('GetResourcePackagePrice', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetSubscriptionPriceResponse().from_map(
            self.do_rpcrequest('GetSubscriptionPrice', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_subscription_price_with_options_async(
        self,
        request: bss_open_api_20171214_models.GetSubscriptionPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.GetSubscriptionPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.GetSubscriptionPriceResponse().from_map(
            await self.do_rpcrequest_async('GetSubscriptionPrice', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_subscription_price(
        self,
        request: bss_open_api_20171214_models.GetSubscriptionPriceRequest,
    ) -> bss_open_api_20171214_models.GetSubscriptionPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_subscription_price_with_options(request, runtime)

    async def get_subscription_price_async(
        self,
        request: bss_open_api_20171214_models.GetSubscriptionPriceRequest,
    ) -> bss_open_api_20171214_models.GetSubscriptionPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_subscription_price_with_options_async(request, runtime)

    def modify_cost_unit_with_options(
        self,
        request: bss_open_api_20171214_models.ModifyCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ModifyCostUnitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ModifyCostUnitResponse().from_map(
            self.do_rpcrequest('ModifyCostUnit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cost_unit_with_options_async(
        self,
        request: bss_open_api_20171214_models.ModifyCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ModifyCostUnitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ModifyCostUnitResponse().from_map(
            await self.do_rpcrequest_async('ModifyCostUnit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ModifyInstanceResponse().from_map(
            self.do_rpcrequest('ModifyInstance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_with_options_async(
        self,
        request: bss_open_api_20171214_models.ModifyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.ModifyInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.ModifyInstanceResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return bss_open_api_20171214_models.QueryAccountBalanceResponse().from_map(
            self.do_rpcrequest('QueryAccountBalance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_account_balance_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAccountBalanceResponse:
        req = open_api_models.OpenApiRequest()
        return bss_open_api_20171214_models.QueryAccountBalanceResponse().from_map(
            await self.do_rpcrequest_async('QueryAccountBalance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryAccountBillResponse().from_map(
            self.do_rpcrequest('QueryAccountBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_account_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryAccountBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAccountBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryAccountBillResponse().from_map(
            await self.do_rpcrequest_async('QueryAccountBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_account_bill(
        self,
        request: bss_open_api_20171214_models.QueryAccountBillRequest,
    ) -> bss_open_api_20171214_models.QueryAccountBillResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_account_bill_with_options(request, runtime)

    async def query_account_bill_async(
        self,
        request: bss_open_api_20171214_models.QueryAccountBillRequest,
    ) -> bss_open_api_20171214_models.QueryAccountBillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_account_bill_with_options_async(request, runtime)

    def query_account_transaction_details_with_options(
        self,
        request: bss_open_api_20171214_models.QueryAccountTransactionDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAccountTransactionDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryAccountTransactionDetailsResponse().from_map(
            self.do_rpcrequest('QueryAccountTransactionDetails', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_account_transaction_details_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryAccountTransactionDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAccountTransactionDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryAccountTransactionDetailsResponse().from_map(
            await self.do_rpcrequest_async('QueryAccountTransactionDetails', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryAccountTransactionsResponse().from_map(
            self.do_rpcrequest('QueryAccountTransactions', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_account_transactions_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryAccountTransactionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAccountTransactionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryAccountTransactionsResponse().from_map(
            await self.do_rpcrequest_async('QueryAccountTransactions', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryAvailableInstancesResponse().from_map(
            self.do_rpcrequest('QueryAvailableInstances', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_available_instances_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryAvailableInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryAvailableInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryAvailableInstancesResponse().from_map(
            await self.do_rpcrequest_async('QueryAvailableInstances', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryBillResponse().from_map(
            self.do_rpcrequest('QueryBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryBillResponse().from_map(
            await self.do_rpcrequest_async('QueryBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryBillOverviewResponse().from_map(
            self.do_rpcrequest('QueryBillOverview', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_bill_overview_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryBillOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryBillOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryBillOverviewResponse().from_map(
            await self.do_rpcrequest_async('QueryBillOverview', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return bss_open_api_20171214_models.QueryBillToOSSSubscriptionResponse().from_map(
            self.do_rpcrequest('QueryBillToOSSSubscription', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_bill_to_osssubscription_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryBillToOSSSubscriptionResponse:
        req = open_api_models.OpenApiRequest()
        return bss_open_api_20171214_models.QueryBillToOSSSubscriptionResponse().from_map(
            await self.do_rpcrequest_async('QueryBillToOSSSubscription', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryCashCouponsResponse().from_map(
            self.do_rpcrequest('QueryCashCoupons', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_cash_coupons_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryCashCouponsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCashCouponsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryCashCouponsResponse().from_map(
            await self.do_rpcrequest_async('QueryCashCoupons', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_cost_unit_with_options(
        self,
        request: bss_open_api_20171214_models.QueryCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCostUnitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryCostUnitResponse().from_map(
            self.do_rpcrequest('QueryCostUnit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_cost_unit_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryCostUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCostUnitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryCostUnitResponse().from_map(
            await self.do_rpcrequest_async('QueryCostUnit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryCostUnitResourceResponse().from_map(
            self.do_rpcrequest('QueryCostUnitResource', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_cost_unit_resource_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryCostUnitResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCostUnitResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryCostUnitResourceResponse().from_map(
            await self.do_rpcrequest_async('QueryCostUnitResource', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryCustomerAddressListResponse().from_map(
            self.do_rpcrequest('QueryCustomerAddressList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_customer_address_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryCustomerAddressListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryCustomerAddressListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryCustomerAddressListResponse().from_map(
            await self.do_rpcrequest_async('QueryCustomerAddressList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_evaluate_list_with_options(
        self,
        request: bss_open_api_20171214_models.QueryEvaluateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryEvaluateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryEvaluateListResponse().from_map(
            self.do_rpcrequest('QueryEvaluateList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_evaluate_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryEvaluateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryEvaluateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryEvaluateListResponse().from_map(
            await self.do_rpcrequest_async('QueryEvaluateList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryFinancialAccountInfoResponse().from_map(
            self.do_rpcrequest('QueryFinancialAccountInfo', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_financial_account_info_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryFinancialAccountInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryFinancialAccountInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryFinancialAccountInfoResponse().from_map(
            await self.do_rpcrequest_async('QueryFinancialAccountInfo', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryInstanceBillResponse().from_map(
            self.do_rpcrequest('QueryInstanceBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_instance_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryInstanceBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryInstanceBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryInstanceBillResponse().from_map(
            await self.do_rpcrequest_async('QueryInstanceBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_instance_bill(
        self,
        request: bss_open_api_20171214_models.QueryInstanceBillRequest,
    ) -> bss_open_api_20171214_models.QueryInstanceBillResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_instance_bill_with_options(request, runtime)

    async def query_instance_bill_async(
        self,
        request: bss_open_api_20171214_models.QueryInstanceBillRequest,
    ) -> bss_open_api_20171214_models.QueryInstanceBillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_instance_bill_with_options_async(request, runtime)

    def query_instance_by_tag_with_options(
        self,
        request: bss_open_api_20171214_models.QueryInstanceByTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryInstanceByTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryInstanceByTagResponse().from_map(
            self.do_rpcrequest('QueryInstanceByTag', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_instance_by_tag_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryInstanceByTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryInstanceByTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryInstanceByTagResponse().from_map(
            await self.do_rpcrequest_async('QueryInstanceByTag', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryInstanceGaapCostResponse().from_map(
            self.do_rpcrequest('QueryInstanceGaapCost', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_instance_gaap_cost_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryInstanceGaapCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryInstanceGaapCostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryInstanceGaapCostResponse().from_map(
            await self.do_rpcrequest_async('QueryInstanceGaapCost', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryInvoicingCustomerListResponse().from_map(
            self.do_rpcrequest('QueryInvoicingCustomerList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_invoicing_customer_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryInvoicingCustomerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryInvoicingCustomerListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryInvoicingCustomerListResponse().from_map(
            await self.do_rpcrequest_async('QueryInvoicingCustomerList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_monthly_bill_with_options(
        self,
        request: bss_open_api_20171214_models.QueryMonthlyBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryMonthlyBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryMonthlyBillResponse().from_map(
            self.do_rpcrequest('QueryMonthlyBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_monthly_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryMonthlyBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryMonthlyBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryMonthlyBillResponse().from_map(
            await self.do_rpcrequest_async('QueryMonthlyBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_monthly_bill(
        self,
        request: bss_open_api_20171214_models.QueryMonthlyBillRequest,
    ) -> bss_open_api_20171214_models.QueryMonthlyBillResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_monthly_bill_with_options(request, runtime)

    async def query_monthly_bill_async(
        self,
        request: bss_open_api_20171214_models.QueryMonthlyBillRequest,
    ) -> bss_open_api_20171214_models.QueryMonthlyBillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_monthly_bill_with_options_async(request, runtime)

    def query_monthly_instance_consumption_with_options(
        self,
        request: bss_open_api_20171214_models.QueryMonthlyInstanceConsumptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryMonthlyInstanceConsumptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryMonthlyInstanceConsumptionResponse().from_map(
            self.do_rpcrequest('QueryMonthlyInstanceConsumption', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_monthly_instance_consumption_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryMonthlyInstanceConsumptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryMonthlyInstanceConsumptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryMonthlyInstanceConsumptionResponse().from_map(
            await self.do_rpcrequest_async('QueryMonthlyInstanceConsumption', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_monthly_instance_consumption(
        self,
        request: bss_open_api_20171214_models.QueryMonthlyInstanceConsumptionRequest,
    ) -> bss_open_api_20171214_models.QueryMonthlyInstanceConsumptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_monthly_instance_consumption_with_options(request, runtime)

    async def query_monthly_instance_consumption_async(
        self,
        request: bss_open_api_20171214_models.QueryMonthlyInstanceConsumptionRequest,
    ) -> bss_open_api_20171214_models.QueryMonthlyInstanceConsumptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_monthly_instance_consumption_with_options_async(request, runtime)

    def query_orders_with_options(
        self,
        request: bss_open_api_20171214_models.QueryOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryOrdersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryOrdersResponse().from_map(
            self.do_rpcrequest('QueryOrders', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_orders_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryOrdersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryOrdersResponse().from_map(
            await self.do_rpcrequest_async('QueryOrders', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryPermissionListResponse().from_map(
            self.do_rpcrequest('QueryPermissionList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_permission_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryPermissionListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryPermissionListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryPermissionListResponse().from_map(
            await self.do_rpcrequest_async('QueryPermissionList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryPrepaidCardsResponse().from_map(
            self.do_rpcrequest('QueryPrepaidCards', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_prepaid_cards_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryPrepaidCardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryPrepaidCardsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryPrepaidCardsResponse().from_map(
            await self.do_rpcrequest_async('QueryPrepaidCards', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_product_list_with_options(
        self,
        request: bss_open_api_20171214_models.QueryProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryProductListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryProductListResponse().from_map(
            self.do_rpcrequest('QueryProductList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_product_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryProductListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryProductListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryProductListResponse().from_map(
            await self.do_rpcrequest_async('QueryProductList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_redeem_with_options(
        self,
        request: bss_open_api_20171214_models.QueryRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryRedeemResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return bss_open_api_20171214_models.QueryRedeemResponse().from_map(
            self.do_rpcrequest('QueryRedeem', '2017-12-14', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_redeem_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryRedeemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryRedeemResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return bss_open_api_20171214_models.QueryRedeemResponse().from_map(
            await self.do_rpcrequest_async('QueryRedeem', '2017-12-14', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryRelationListResponse().from_map(
            self.do_rpcrequest('QueryRelationList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_relation_list_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryRelationListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryRelationListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryRelationListResponse().from_map(
            await self.do_rpcrequest_async('QueryRelationList', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryResellerAvailableQuotaResponse().from_map(
            self.do_rpcrequest('QueryResellerAvailableQuota', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_reseller_available_quota_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryResellerAvailableQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryResellerAvailableQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryResellerAvailableQuotaResponse().from_map(
            await self.do_rpcrequest_async('QueryResellerAvailableQuota', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_riutilization_detail_with_options(
        self,
        request: bss_open_api_20171214_models.QueryRIUtilizationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryRIUtilizationDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryRIUtilizationDetailResponse().from_map(
            self.do_rpcrequest('QueryRIUtilizationDetail', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_riutilization_detail_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryRIUtilizationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryRIUtilizationDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryRIUtilizationDetailResponse().from_map(
            await self.do_rpcrequest_async('QueryRIUtilizationDetail', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_savings_plans_deduct_log_with_options(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansDeductLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansDeductLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySavingsPlansDeductLogResponse().from_map(
            self.do_rpcrequest('QuerySavingsPlansDeductLog', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_savings_plans_deduct_log_with_options_async(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansDeductLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansDeductLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySavingsPlansDeductLogResponse().from_map(
            await self.do_rpcrequest_async('QuerySavingsPlansDeductLog', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_savings_plans_instance_with_options(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySavingsPlansInstanceResponse().from_map(
            self.do_rpcrequest('QuerySavingsPlansInstance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_savings_plans_instance_with_options_async(
        self,
        request: bss_open_api_20171214_models.QuerySavingsPlansInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySavingsPlansInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySavingsPlansInstanceResponse().from_map(
            await self.do_rpcrequest_async('QuerySavingsPlansInstance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySettleBillResponse().from_map(
            self.do_rpcrequest('QuerySettleBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_settle_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.QuerySettleBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySettleBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySettleBillResponse().from_map(
            await self.do_rpcrequest_async('QuerySettleBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def query_settlement_bill_with_options(
        self,
        request: bss_open_api_20171214_models.QuerySettlementBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySettlementBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySettlementBillResponse().from_map(
            self.do_rpcrequest('QuerySettlementBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_settlement_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.QuerySettlementBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySettlementBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySettlementBillResponse().from_map(
            await self.do_rpcrequest_async('QuerySettlementBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_settlement_bill(
        self,
        request: bss_open_api_20171214_models.QuerySettlementBillRequest,
    ) -> bss_open_api_20171214_models.QuerySettlementBillResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_settlement_bill_with_options(request, runtime)

    async def query_settlement_bill_async(
        self,
        request: bss_open_api_20171214_models.QuerySettlementBillRequest,
    ) -> bss_open_api_20171214_models.QuerySettlementBillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_settlement_bill_with_options_async(request, runtime)

    def query_split_item_bill_with_options(
        self,
        request: bss_open_api_20171214_models.QuerySplitItemBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySplitItemBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySplitItemBillResponse().from_map(
            self.do_rpcrequest('QuerySplitItemBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_split_item_bill_with_options_async(
        self,
        request: bss_open_api_20171214_models.QuerySplitItemBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QuerySplitItemBillResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QuerySplitItemBillResponse().from_map(
            await self.do_rpcrequest_async('QuerySplitItemBill', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_split_item_bill(
        self,
        request: bss_open_api_20171214_models.QuerySplitItemBillRequest,
    ) -> bss_open_api_20171214_models.QuerySplitItemBillResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_split_item_bill_with_options(request, runtime)

    async def query_split_item_bill_async(
        self,
        request: bss_open_api_20171214_models.QuerySplitItemBillRequest,
    ) -> bss_open_api_20171214_models.QuerySplitItemBillResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_split_item_bill_with_options_async(request, runtime)

    def query_user_oms_data_with_options(
        self,
        request: bss_open_api_20171214_models.QueryUserOmsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryUserOmsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryUserOmsDataResponse().from_map(
            self.do_rpcrequest('QueryUserOmsData', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_user_oms_data_with_options_async(
        self,
        request: bss_open_api_20171214_models.QueryUserOmsDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.QueryUserOmsDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.QueryUserOmsDataResponse().from_map(
            await self.do_rpcrequest_async('QueryUserOmsData', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_user_oms_data(
        self,
        request: bss_open_api_20171214_models.QueryUserOmsDataRequest,
    ) -> bss_open_api_20171214_models.QueryUserOmsDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_oms_data_with_options(request, runtime)

    async def query_user_oms_data_async(
        self,
        request: bss_open_api_20171214_models.QueryUserOmsDataRequest,
    ) -> bss_open_api_20171214_models.QueryUserOmsDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_oms_data_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: bss_open_api_20171214_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.RenewInstanceResponse().from_map(
            self.do_rpcrequest('RenewInstance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: bss_open_api_20171214_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.RenewInstanceResponse().from_map(
            await self.do_rpcrequest_async('RenewInstance', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.RenewResourcePackageResponse().from_map(
            self.do_rpcrequest('RenewResourcePackage', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_resource_package_with_options_async(
        self,
        request: bss_open_api_20171214_models.RenewResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.RenewResourcePackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.RenewResourcePackageResponse().from_map(
            await self.do_rpcrequest_async('RenewResourcePackage', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SaveUserCreditResponse().from_map(
            self.do_rpcrequest('SaveUserCredit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_user_credit_with_options_async(
        self,
        request: bss_open_api_20171214_models.SaveUserCreditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SaveUserCreditResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SaveUserCreditResponse().from_map(
            await self.do_rpcrequest_async('SaveUserCredit', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def set_credit_label_action_with_options(
        self,
        request: bss_open_api_20171214_models.SetCreditLabelActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetCreditLabelActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetCreditLabelActionResponse().from_map(
            self.do_rpcrequest('SetCreditLabelAction', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_credit_label_action_with_options_async(
        self,
        request: bss_open_api_20171214_models.SetCreditLabelActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetCreditLabelActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetCreditLabelActionResponse().from_map(
            await self.do_rpcrequest_async('SetCreditLabelAction', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetRenewalResponse().from_map(
            self.do_rpcrequest('SetRenewal', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_renewal_with_options_async(
        self,
        request: bss_open_api_20171214_models.SetRenewalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetRenewalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetRenewalResponse().from_map(
            await self.do_rpcrequest_async('SetRenewal', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetResellerUserAlarmThresholdResponse().from_map(
            self.do_rpcrequest('SetResellerUserAlarmThreshold', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_reseller_user_alarm_threshold_with_options_async(
        self,
        request: bss_open_api_20171214_models.SetResellerUserAlarmThresholdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetResellerUserAlarmThresholdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetResellerUserAlarmThresholdResponse().from_map(
            await self.do_rpcrequest_async('SetResellerUserAlarmThreshold', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetResellerUserQuotaResponse().from_map(
            self.do_rpcrequest('SetResellerUserQuota', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_reseller_user_quota_with_options_async(
        self,
        request: bss_open_api_20171214_models.SetResellerUserQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetResellerUserQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetResellerUserQuotaResponse().from_map(
            await self.do_rpcrequest_async('SetResellerUserQuota', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetResellerUserStatusResponse().from_map(
            self.do_rpcrequest('SetResellerUserStatus', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_reseller_user_status_with_options_async(
        self,
        request: bss_open_api_20171214_models.SetResellerUserStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SetResellerUserStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SetResellerUserStatusResponse().from_map(
            await self.do_rpcrequest_async('SetResellerUserStatus', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SubscribeBillToOSSResponse().from_map(
            self.do_rpcrequest('SubscribeBillToOSS', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def subscribe_bill_to_osswith_options_async(
        self,
        request: bss_open_api_20171214_models.SubscribeBillToOSSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.SubscribeBillToOSSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.SubscribeBillToOSSResponse().from_map(
            await self.do_rpcrequest_async('SubscribeBillToOSS', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: bss_open_api_20171214_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.UnsubscribeBillToOSSResponse().from_map(
            self.do_rpcrequest('UnsubscribeBillToOSS', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unsubscribe_bill_to_osswith_options_async(
        self,
        request: bss_open_api_20171214_models.UnsubscribeBillToOSSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.UnsubscribeBillToOSSResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.UnsubscribeBillToOSSResponse().from_map(
            await self.do_rpcrequest_async('UnsubscribeBillToOSS', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: bss_open_api_20171214_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.UpgradeResourcePackageResponse().from_map(
            self.do_rpcrequest('UpgradeResourcePackage', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_resource_package_with_options_async(
        self,
        request: bss_open_api_20171214_models.UpgradeResourcePackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20171214_models.UpgradeResourcePackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return bss_open_api_20171214_models.UpgradeResourcePackageResponse().from_map(
            await self.do_rpcrequest_async('UpgradeResourcePackage', '2017-12-14', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
