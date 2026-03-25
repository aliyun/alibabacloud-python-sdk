# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_bssopenapi20230930 import models as main_models
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

    def add_coupon_deduct_tag_with_options(
        self,
        tmp_req: main_models.AddCouponDeductTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCouponDeductTagResponse:
        tmp_req.validate()
        request = main_models.AddCouponDeductTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCouponDeductTag',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCouponDeductTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_coupon_deduct_tag_with_options_async(
        self,
        tmp_req: main_models.AddCouponDeductTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCouponDeductTagResponse:
        tmp_req.validate()
        request = main_models.AddCouponDeductTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCouponDeductTag',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCouponDeductTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_coupon_deduct_tag(
        self,
        request: main_models.AddCouponDeductTagRequest,
    ) -> main_models.AddCouponDeductTagResponse:
        runtime = RuntimeOptions()
        return self.add_coupon_deduct_tag_with_options(request, runtime)

    async def add_coupon_deduct_tag_async(
        self,
        request: main_models.AddCouponDeductTagRequest,
    ) -> main_models.AddCouponDeductTagResponse:
        runtime = RuntimeOptions()
        return await self.add_coupon_deduct_tag_with_options_async(request, runtime)

    def allocate_cost_center_resource_with_options(
        self,
        tmp_req: main_models.AllocateCostCenterResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateCostCenterResourceResponse:
        tmp_req.validate()
        request = main_models.AllocateCostCenterResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_instance_list):
            request.resource_instance_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_instance_list, 'ResourceInstanceList', 'json')
        query = {}
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.from_cost_center_id):
            body['FromCostCenterId'] = request.from_cost_center_id
        if not DaraCore.is_null(request.from_owner_account_id):
            body['FromOwnerAccountId'] = request.from_owner_account_id
        if not DaraCore.is_null(request.resource_instance_list_shrink):
            body['ResourceInstanceList'] = request.resource_instance_list_shrink
        if not DaraCore.is_null(request.to_cost_center_id):
            body['ToCostCenterId'] = request.to_cost_center_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AllocateCostCenterResource',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateCostCenterResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_cost_center_resource_with_options_async(
        self,
        tmp_req: main_models.AllocateCostCenterResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateCostCenterResourceResponse:
        tmp_req.validate()
        request = main_models.AllocateCostCenterResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_instance_list):
            request.resource_instance_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_instance_list, 'ResourceInstanceList', 'json')
        query = {}
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.from_cost_center_id):
            body['FromCostCenterId'] = request.from_cost_center_id
        if not DaraCore.is_null(request.from_owner_account_id):
            body['FromOwnerAccountId'] = request.from_owner_account_id
        if not DaraCore.is_null(request.resource_instance_list_shrink):
            body['ResourceInstanceList'] = request.resource_instance_list_shrink
        if not DaraCore.is_null(request.to_cost_center_id):
            body['ToCostCenterId'] = request.to_cost_center_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AllocateCostCenterResource',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateCostCenterResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_cost_center_resource(
        self,
        request: main_models.AllocateCostCenterResourceRequest,
    ) -> main_models.AllocateCostCenterResourceResponse:
        runtime = RuntimeOptions()
        return self.allocate_cost_center_resource_with_options(request, runtime)

    async def allocate_cost_center_resource_async(
        self,
        request: main_models.AllocateCostCenterResourceRequest,
    ) -> main_models.AllocateCostCenterResourceResponse:
        runtime = RuntimeOptions()
        return await self.allocate_cost_center_resource_with_options_async(request, runtime)

    def cancel_fund_account_low_available_amount_alarm_with_options(
        self,
        request: main_models.CancelFundAccountLowAvailableAmountAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelFundAccountLowAvailableAmountAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelFundAccountLowAvailableAmountAlarm',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelFundAccountLowAvailableAmountAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_fund_account_low_available_amount_alarm_with_options_async(
        self,
        request: main_models.CancelFundAccountLowAvailableAmountAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelFundAccountLowAvailableAmountAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelFundAccountLowAvailableAmountAlarm',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelFundAccountLowAvailableAmountAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_fund_account_low_available_amount_alarm(
        self,
        request: main_models.CancelFundAccountLowAvailableAmountAlarmRequest,
    ) -> main_models.CancelFundAccountLowAvailableAmountAlarmResponse:
        runtime = RuntimeOptions()
        return self.cancel_fund_account_low_available_amount_alarm_with_options(request, runtime)

    async def cancel_fund_account_low_available_amount_alarm_async(
        self,
        request: main_models.CancelFundAccountLowAvailableAmountAlarmRequest,
    ) -> main_models.CancelFundAccountLowAvailableAmountAlarmResponse:
        runtime = RuntimeOptions()
        return await self.cancel_fund_account_low_available_amount_alarm_with_options_async(request, runtime)

    def check_account_exist_with_options(
        self,
        request: main_models.CheckAccountExistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckAccountExistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.to_user_type):
            body['ToUserType'] = request.to_user_type
        if not DaraCore.is_null(request.transfer_account):
            body['TransferAccount'] = request.transfer_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckAccountExist',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAccountExistResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_account_exist_with_options_async(
        self,
        request: main_models.CheckAccountExistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckAccountExistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.to_user_type):
            body['ToUserType'] = request.to_user_type
        if not DaraCore.is_null(request.transfer_account):
            body['TransferAccount'] = request.transfer_account
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckAccountExist',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckAccountExistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_account_exist(
        self,
        request: main_models.CheckAccountExistRequest,
    ) -> main_models.CheckAccountExistResponse:
        runtime = RuntimeOptions()
        return self.check_account_exist_with_options(request, runtime)

    async def check_account_exist_async(
        self,
        request: main_models.CheckAccountExistRequest,
    ) -> main_models.CheckAccountExistResponse:
        runtime = RuntimeOptions()
        return await self.check_account_exist_with_options_async(request, runtime)

    def create_cost_center_with_options(
        self,
        tmp_req: main_models.CreateCostCenterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCostCenterResponse:
        tmp_req.validate()
        request = main_models.CreateCostCenterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cost_center_entity_list):
            request.cost_center_entity_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.cost_center_entity_list, 'CostCenterEntityList', 'json')
        query = {}
        if not DaraCore.is_null(request.cost_center_entity_list_shrink):
            query['CostCenterEntityList'] = request.cost_center_entity_list_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCostCenter',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCostCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cost_center_with_options_async(
        self,
        tmp_req: main_models.CreateCostCenterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCostCenterResponse:
        tmp_req.validate()
        request = main_models.CreateCostCenterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cost_center_entity_list):
            request.cost_center_entity_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.cost_center_entity_list, 'CostCenterEntityList', 'json')
        query = {}
        if not DaraCore.is_null(request.cost_center_entity_list_shrink):
            query['CostCenterEntityList'] = request.cost_center_entity_list_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCostCenter',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCostCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cost_center(
        self,
        request: main_models.CreateCostCenterRequest,
    ) -> main_models.CreateCostCenterResponse:
        runtime = RuntimeOptions()
        return self.create_cost_center_with_options(request, runtime)

    async def create_cost_center_async(
        self,
        request: main_models.CreateCostCenterRequest,
    ) -> main_models.CreateCostCenterResponse:
        runtime = RuntimeOptions()
        return await self.create_cost_center_with_options_async(request, runtime)

    def create_cost_center_rule_with_options(
        self,
        tmp_req: main_models.CreateCostCenterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCostCenterRuleResponse:
        tmp_req.validate()
        request = main_models.CreateCostCenterRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_expression):
            request.filter_expression_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_expression, 'FilterExpression', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_expression_shrink):
            query['FilterExpression'] = request.filter_expression_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCostCenterRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCostCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cost_center_rule_with_options_async(
        self,
        tmp_req: main_models.CreateCostCenterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCostCenterRuleResponse:
        tmp_req.validate()
        request = main_models.CreateCostCenterRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_expression):
            request.filter_expression_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_expression, 'FilterExpression', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_expression_shrink):
            query['FilterExpression'] = request.filter_expression_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCostCenterRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCostCenterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cost_center_rule(
        self,
        request: main_models.CreateCostCenterRuleRequest,
    ) -> main_models.CreateCostCenterRuleResponse:
        runtime = RuntimeOptions()
        return self.create_cost_center_rule_with_options(request, runtime)

    async def create_cost_center_rule_async(
        self,
        request: main_models.CreateCostCenterRuleRequest,
    ) -> main_models.CreateCostCenterRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_cost_center_rule_with_options_async(request, runtime)

    def create_fund_account_pay_relation_with_options(
        self,
        tmp_req: main_models.CreateFundAccountPayRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFundAccountPayRelationResponse:
        tmp_req.validate()
        request = main_models.CreateFundAccountPayRelationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFundAccountPayRelation',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFundAccountPayRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fund_account_pay_relation_with_options_async(
        self,
        tmp_req: main_models.CreateFundAccountPayRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFundAccountPayRelationResponse:
        tmp_req.validate()
        request = main_models.CreateFundAccountPayRelationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFundAccountPayRelation',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFundAccountPayRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fund_account_pay_relation(
        self,
        request: main_models.CreateFundAccountPayRelationRequest,
    ) -> main_models.CreateFundAccountPayRelationResponse:
        runtime = RuntimeOptions()
        return self.create_fund_account_pay_relation_with_options(request, runtime)

    async def create_fund_account_pay_relation_async(
        self,
        request: main_models.CreateFundAccountPayRelationRequest,
    ) -> main_models.CreateFundAccountPayRelationResponse:
        runtime = RuntimeOptions()
        return await self.create_fund_account_pay_relation_with_options_async(request, runtime)

    def create_fund_account_transfer_with_options(
        self,
        request: main_models.CreateFundAccountTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFundAccountTransferResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amount):
            body['Amount'] = request.amount
        if not DaraCore.is_null(request.currency):
            body['Currency'] = request.currency
        if not DaraCore.is_null(request.finance_type):
            body['FinanceType'] = request.finance_type
        if not DaraCore.is_null(request.from_fund_account_id):
            body['FromFundAccountId'] = request.from_fund_account_id
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        if not DaraCore.is_null(request.to_fund_account_id):
            body['ToFundAccountId'] = request.to_fund_account_id
        if not DaraCore.is_null(request.transfer_type):
            body['TransferType'] = request.transfer_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFundAccountTransfer',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFundAccountTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fund_account_transfer_with_options_async(
        self,
        request: main_models.CreateFundAccountTransferRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFundAccountTransferResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.amount):
            body['Amount'] = request.amount
        if not DaraCore.is_null(request.currency):
            body['Currency'] = request.currency
        if not DaraCore.is_null(request.finance_type):
            body['FinanceType'] = request.finance_type
        if not DaraCore.is_null(request.from_fund_account_id):
            body['FromFundAccountId'] = request.from_fund_account_id
        if not DaraCore.is_null(request.remark):
            body['Remark'] = request.remark
        if not DaraCore.is_null(request.to_fund_account_id):
            body['ToFundAccountId'] = request.to_fund_account_id
        if not DaraCore.is_null(request.transfer_type):
            body['TransferType'] = request.transfer_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateFundAccountTransfer',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFundAccountTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fund_account_transfer(
        self,
        request: main_models.CreateFundAccountTransferRequest,
    ) -> main_models.CreateFundAccountTransferResponse:
        runtime = RuntimeOptions()
        return self.create_fund_account_transfer_with_options(request, runtime)

    async def create_fund_account_transfer_async(
        self,
        request: main_models.CreateFundAccountTransferRequest,
    ) -> main_models.CreateFundAccountTransferResponse:
        runtime = RuntimeOptions()
        return await self.create_fund_account_transfer_with_options_async(request, runtime)

    def create_invoice_with_options(
        self,
        tmp_req: main_models.CreateInvoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInvoiceResponse:
        tmp_req.validate()
        request = main_models.CreateInvoiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not DaraCore.is_null(tmp_req.invoice_candidate_ids):
            request.invoice_candidate_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.invoice_candidate_ids, 'InvoiceCandidateIds', 'json')
        if not DaraCore.is_null(tmp_req.recipient_emails):
            request.recipient_emails_shrink = Utils.array_to_string_with_specified_style(tmp_req.recipient_emails, 'RecipientEmails', 'json')
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.invoice_candidate_ids_shrink):
            query['InvoiceCandidateIds'] = request.invoice_candidate_ids_shrink
        if not DaraCore.is_null(request.invoice_mode):
            query['InvoiceMode'] = request.invoice_mode
        if not DaraCore.is_null(request.invoice_remark):
            query['InvoiceRemark'] = request.invoice_remark
        if not DaraCore.is_null(request.invoice_title_id):
            query['InvoiceTitleId'] = request.invoice_title_id
        if not DaraCore.is_null(request.invoice_type):
            query['InvoiceType'] = request.invoice_type
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.recipient_emails_shrink):
            query['RecipientEmails'] = request.recipient_emails_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInvoice',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_invoice_with_options_async(
        self,
        tmp_req: main_models.CreateInvoiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInvoiceResponse:
        tmp_req.validate()
        request = main_models.CreateInvoiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not DaraCore.is_null(tmp_req.invoice_candidate_ids):
            request.invoice_candidate_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.invoice_candidate_ids, 'InvoiceCandidateIds', 'json')
        if not DaraCore.is_null(tmp_req.recipient_emails):
            request.recipient_emails_shrink = Utils.array_to_string_with_specified_style(tmp_req.recipient_emails, 'RecipientEmails', 'json')
        query = {}
        if not DaraCore.is_null(request.amount):
            query['Amount'] = request.amount
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.invoice_candidate_ids_shrink):
            query['InvoiceCandidateIds'] = request.invoice_candidate_ids_shrink
        if not DaraCore.is_null(request.invoice_mode):
            query['InvoiceMode'] = request.invoice_mode
        if not DaraCore.is_null(request.invoice_remark):
            query['InvoiceRemark'] = request.invoice_remark
        if not DaraCore.is_null(request.invoice_title_id):
            query['InvoiceTitleId'] = request.invoice_title_id
        if not DaraCore.is_null(request.invoice_type):
            query['InvoiceType'] = request.invoice_type
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.recipient_emails_shrink):
            query['RecipientEmails'] = request.recipient_emails_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInvoice',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_invoice(
        self,
        request: main_models.CreateInvoiceRequest,
    ) -> main_models.CreateInvoiceResponse:
        runtime = RuntimeOptions()
        return self.create_invoice_with_options(request, runtime)

    async def create_invoice_async(
        self,
        request: main_models.CreateInvoiceRequest,
    ) -> main_models.CreateInvoiceResponse:
        runtime = RuntimeOptions()
        return await self.create_invoice_with_options_async(request, runtime)

    def create_report_definition_with_options(
        self,
        request: main_models.CreateReportDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateReportDefinitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not DaraCore.is_null(request.include_members):
            query['IncludeMembers'] = request.include_members
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.not_send_on_no_data):
            query['NotSendOnNoData'] = request.not_send_on_no_data
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_bucket_owner_account_id):
            query['OssBucketOwnerAccountId'] = request.oss_bucket_owner_account_id
        if not DaraCore.is_null(request.oss_bucket_path):
            query['OssBucketPath'] = request.oss_bucket_path
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        if not DaraCore.is_null(request.send_with_attach):
            query['SendWithAttach'] = request.send_with_attach
        if not DaraCore.is_null(request.split_file_on_user_id):
            query['SplitFileOnUserId'] = request.split_file_on_user_id
        body = {}
        if not DaraCore.is_null(request.mc_project):
            body['McProject'] = request.mc_project
        if not DaraCore.is_null(request.mc_table_name):
            body['McTableName'] = request.mc_table_name
        if not DaraCore.is_null(request.report_source_type):
            body['ReportSourceType'] = request.report_source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateReportDefinition',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateReportDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_report_definition_with_options_async(
        self,
        request: main_models.CreateReportDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateReportDefinitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not DaraCore.is_null(request.include_members):
            query['IncludeMembers'] = request.include_members
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.not_send_on_no_data):
            query['NotSendOnNoData'] = request.not_send_on_no_data
        if not DaraCore.is_null(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not DaraCore.is_null(request.oss_bucket_owner_account_id):
            query['OssBucketOwnerAccountId'] = request.oss_bucket_owner_account_id
        if not DaraCore.is_null(request.oss_bucket_path):
            query['OssBucketPath'] = request.oss_bucket_path
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        if not DaraCore.is_null(request.send_with_attach):
            query['SendWithAttach'] = request.send_with_attach
        if not DaraCore.is_null(request.split_file_on_user_id):
            query['SplitFileOnUserId'] = request.split_file_on_user_id
        body = {}
        if not DaraCore.is_null(request.mc_project):
            body['McProject'] = request.mc_project
        if not DaraCore.is_null(request.mc_table_name):
            body['McTableName'] = request.mc_table_name
        if not DaraCore.is_null(request.report_source_type):
            body['ReportSourceType'] = request.report_source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateReportDefinition',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateReportDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_report_definition(
        self,
        request: main_models.CreateReportDefinitionRequest,
    ) -> main_models.CreateReportDefinitionResponse:
        runtime = RuntimeOptions()
        return self.create_report_definition_with_options(request, runtime)

    async def create_report_definition_async(
        self,
        request: main_models.CreateReportDefinitionRequest,
    ) -> main_models.CreateReportDefinitionResponse:
        runtime = RuntimeOptions()
        return await self.create_report_definition_with_options_async(request, runtime)

    def delete_cost_center_with_options(
        self,
        request: main_models.DeleteCostCenterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCostCenterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cost_center_id):
            query['CostCenterId'] = request.cost_center_id
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.owner_account_id):
            query['OwnerAccountId'] = request.owner_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCostCenter',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCostCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cost_center_with_options_async(
        self,
        request: main_models.DeleteCostCenterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCostCenterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cost_center_id):
            query['CostCenterId'] = request.cost_center_id
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.owner_account_id):
            query['OwnerAccountId'] = request.owner_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCostCenter',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCostCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cost_center(
        self,
        request: main_models.DeleteCostCenterRequest,
    ) -> main_models.DeleteCostCenterResponse:
        runtime = RuntimeOptions()
        return self.delete_cost_center_with_options(request, runtime)

    async def delete_cost_center_async(
        self,
        request: main_models.DeleteCostCenterRequest,
    ) -> main_models.DeleteCostCenterResponse:
        runtime = RuntimeOptions()
        return await self.delete_cost_center_with_options_async(request, runtime)

    def delete_cost_center_rule_with_options(
        self,
        tmp_req: main_models.DeleteCostCenterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCostCenterRuleResponse:
        tmp_req.validate()
        request = main_models.DeleteCostCenterRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_expression):
            request.filter_expression_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_expression, 'FilterExpression', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_expression_shrink):
            query['FilterExpression'] = request.filter_expression_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCostCenterRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCostCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cost_center_rule_with_options_async(
        self,
        tmp_req: main_models.DeleteCostCenterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCostCenterRuleResponse:
        tmp_req.validate()
        request = main_models.DeleteCostCenterRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_expression):
            request.filter_expression_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_expression, 'FilterExpression', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_expression_shrink):
            query['FilterExpression'] = request.filter_expression_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCostCenterRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCostCenterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cost_center_rule(
        self,
        request: main_models.DeleteCostCenterRuleRequest,
    ) -> main_models.DeleteCostCenterRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_cost_center_rule_with_options(request, runtime)

    async def delete_cost_center_rule_async(
        self,
        request: main_models.DeleteCostCenterRuleRequest,
    ) -> main_models.DeleteCostCenterRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_cost_center_rule_with_options_async(request, runtime)

    def delete_coupon_deduct_tag_with_options(
        self,
        tmp_req: main_models.DeleteCouponDeductTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCouponDeductTagResponse:
        tmp_req.validate()
        request = main_models.DeleteCouponDeductTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not DaraCore.is_null(tmp_req.tag_keys):
            request.tag_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCouponDeductTag',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCouponDeductTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_coupon_deduct_tag_with_options_async(
        self,
        tmp_req: main_models.DeleteCouponDeductTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCouponDeductTagResponse:
        tmp_req.validate()
        request = main_models.DeleteCouponDeductTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not DaraCore.is_null(tmp_req.tag_keys):
            request.tag_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCouponDeductTag',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCouponDeductTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_coupon_deduct_tag(
        self,
        request: main_models.DeleteCouponDeductTagRequest,
    ) -> main_models.DeleteCouponDeductTagResponse:
        runtime = RuntimeOptions()
        return self.delete_coupon_deduct_tag_with_options(request, runtime)

    async def delete_coupon_deduct_tag_async(
        self,
        request: main_models.DeleteCouponDeductTagRequest,
    ) -> main_models.DeleteCouponDeductTagResponse:
        runtime = RuntimeOptions()
        return await self.delete_coupon_deduct_tag_with_options_async(request, runtime)

    def delete_report_definition_with_options(
        self,
        request: main_models.DeleteReportDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteReportDefinitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.report_task_id):
            query['ReportTaskId'] = request.report_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteReportDefinition',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteReportDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_report_definition_with_options_async(
        self,
        request: main_models.DeleteReportDefinitionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteReportDefinitionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.report_task_id):
            query['ReportTaskId'] = request.report_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteReportDefinition',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteReportDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_report_definition(
        self,
        request: main_models.DeleteReportDefinitionRequest,
    ) -> main_models.DeleteReportDefinitionResponse:
        runtime = RuntimeOptions()
        return self.delete_report_definition_with_options(request, runtime)

    async def delete_report_definition_async(
        self,
        request: main_models.DeleteReportDefinitionRequest,
    ) -> main_models.DeleteReportDefinitionResponse:
        runtime = RuntimeOptions()
        return await self.delete_report_definition_with_options_async(request, runtime)

    def describe_coupon_with_options(
        self,
        tmp_req: main_models.DescribeCouponRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCouponResponse:
        tmp_req.validate()
        request = main_models.DescribeCouponShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.coupon_type):
            query['CouponType'] = request.coupon_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not DaraCore.is_null(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not DaraCore.is_null(request.expire_end_date):
            query['ExpireEndDate'] = request.expire_end_date
        if not DaraCore.is_null(request.expire_start_date):
            query['ExpireStartDate'] = request.expire_start_date
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCoupon',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCouponResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_coupon_with_options_async(
        self,
        tmp_req: main_models.DescribeCouponRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCouponResponse:
        tmp_req.validate()
        request = main_models.DescribeCouponShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.coupon_type):
            query['CouponType'] = request.coupon_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.effective_end_time):
            query['EffectiveEndTime'] = request.effective_end_time
        if not DaraCore.is_null(request.effective_start_time):
            query['EffectiveStartTime'] = request.effective_start_time
        if not DaraCore.is_null(request.expire_end_date):
            query['ExpireEndDate'] = request.expire_end_date
        if not DaraCore.is_null(request.expire_start_date):
            query['ExpireStartDate'] = request.expire_start_date
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCoupon',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCouponResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_coupon(
        self,
        request: main_models.DescribeCouponRequest,
    ) -> main_models.DescribeCouponResponse:
        runtime = RuntimeOptions()
        return self.describe_coupon_with_options(request, runtime)

    async def describe_coupon_async(
        self,
        request: main_models.DescribeCouponRequest,
    ) -> main_models.DescribeCouponResponse:
        runtime = RuntimeOptions()
        return await self.describe_coupon_with_options_async(request, runtime)

    def describe_coupon_item_list_with_options(
        self,
        tmp_req: main_models.DescribeCouponItemListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCouponItemListResponse:
        tmp_req.validate()
        request = main_models.DescribeCouponItemListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCouponItemList',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCouponItemListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_coupon_item_list_with_options_async(
        self,
        tmp_req: main_models.DescribeCouponItemListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCouponItemListResponse:
        tmp_req.validate()
        request = main_models.DescribeCouponItemListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCouponItemList',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCouponItemListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_coupon_item_list(
        self,
        request: main_models.DescribeCouponItemListRequest,
    ) -> main_models.DescribeCouponItemListResponse:
        runtime = RuntimeOptions()
        return self.describe_coupon_item_list_with_options(request, runtime)

    async def describe_coupon_item_list_async(
        self,
        request: main_models.DescribeCouponItemListRequest,
    ) -> main_models.DescribeCouponItemListResponse:
        runtime = RuntimeOptions()
        return await self.describe_coupon_item_list_with_options_async(request, runtime)

    def describe_user_spn_summary_info_with_options(
        self,
        tmp_req: main_models.DescribeUserSpnSummaryInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserSpnSummaryInfoResponse:
        tmp_req.validate()
        request = main_models.DescribeUserSpnSummaryInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserSpnSummaryInfo',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserSpnSummaryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_spn_summary_info_with_options_async(
        self,
        tmp_req: main_models.DescribeUserSpnSummaryInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserSpnSummaryInfoResponse:
        tmp_req.validate()
        request = main_models.DescribeUserSpnSummaryInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserSpnSummaryInfo',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserSpnSummaryInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_spn_summary_info(
        self,
        request: main_models.DescribeUserSpnSummaryInfoRequest,
    ) -> main_models.DescribeUserSpnSummaryInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_user_spn_summary_info_with_options(request, runtime)

    async def describe_user_spn_summary_info_async(
        self,
        request: main_models.DescribeUserSpnSummaryInfoRequest,
    ) -> main_models.DescribeUserSpnSummaryInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_spn_summary_info_with_options_async(request, runtime)

    def get_fund_account_available_amount_with_options(
        self,
        request: main_models.GetFundAccountAvailableAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountAvailableAmountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountAvailableAmount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountAvailableAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_available_amount_with_options_async(
        self,
        request: main_models.GetFundAccountAvailableAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountAvailableAmountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountAvailableAmount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountAvailableAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_available_amount(
        self,
        request: main_models.GetFundAccountAvailableAmountRequest,
    ) -> main_models.GetFundAccountAvailableAmountResponse:
        runtime = RuntimeOptions()
        return self.get_fund_account_available_amount_with_options(request, runtime)

    async def get_fund_account_available_amount_async(
        self,
        request: main_models.GetFundAccountAvailableAmountRequest,
    ) -> main_models.GetFundAccountAvailableAmountResponse:
        runtime = RuntimeOptions()
        return await self.get_fund_account_available_amount_with_options_async(request, runtime)

    def get_fund_account_can_allocate_credit_amount_with_options(
        self,
        request: main_models.GetFundAccountCanAllocateCreditAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountCanAllocateCreditAmountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountCanAllocateCreditAmount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountCanAllocateCreditAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_can_allocate_credit_amount_with_options_async(
        self,
        request: main_models.GetFundAccountCanAllocateCreditAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountCanAllocateCreditAmountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountCanAllocateCreditAmount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountCanAllocateCreditAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_can_allocate_credit_amount(
        self,
        request: main_models.GetFundAccountCanAllocateCreditAmountRequest,
    ) -> main_models.GetFundAccountCanAllocateCreditAmountResponse:
        runtime = RuntimeOptions()
        return self.get_fund_account_can_allocate_credit_amount_with_options(request, runtime)

    async def get_fund_account_can_allocate_credit_amount_async(
        self,
        request: main_models.GetFundAccountCanAllocateCreditAmountRequest,
    ) -> main_models.GetFundAccountCanAllocateCreditAmountResponse:
        runtime = RuntimeOptions()
        return await self.get_fund_account_can_allocate_credit_amount_with_options_async(request, runtime)

    def get_fund_account_can_recycle_amount_with_options(
        self,
        request: main_models.GetFundAccountCanRecycleAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountCanRecycleAmountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.currency):
            body['Currency'] = request.currency
        if not DaraCore.is_null(request.recycle_from_fund_account_id):
            body['RecycleFromFundAccountId'] = request.recycle_from_fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountCanRecycleAmount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountCanRecycleAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_can_recycle_amount_with_options_async(
        self,
        request: main_models.GetFundAccountCanRecycleAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountCanRecycleAmountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.currency):
            body['Currency'] = request.currency
        if not DaraCore.is_null(request.recycle_from_fund_account_id):
            body['RecycleFromFundAccountId'] = request.recycle_from_fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountCanRecycleAmount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountCanRecycleAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_can_recycle_amount(
        self,
        request: main_models.GetFundAccountCanRecycleAmountRequest,
    ) -> main_models.GetFundAccountCanRecycleAmountResponse:
        runtime = RuntimeOptions()
        return self.get_fund_account_can_recycle_amount_with_options(request, runtime)

    async def get_fund_account_can_recycle_amount_async(
        self,
        request: main_models.GetFundAccountCanRecycleAmountRequest,
    ) -> main_models.GetFundAccountCanRecycleAmountResponse:
        runtime = RuntimeOptions()
        return await self.get_fund_account_can_recycle_amount_with_options_async(request, runtime)

    def get_fund_account_can_transfer_amount_with_options(
        self,
        request: main_models.GetFundAccountCanTransferAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountCanTransferAmountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.currency):
            body['Currency'] = request.currency
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountCanTransferAmount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountCanTransferAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_can_transfer_amount_with_options_async(
        self,
        request: main_models.GetFundAccountCanTransferAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountCanTransferAmountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.currency):
            body['Currency'] = request.currency
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountCanTransferAmount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountCanTransferAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_can_transfer_amount(
        self,
        request: main_models.GetFundAccountCanTransferAmountRequest,
    ) -> main_models.GetFundAccountCanTransferAmountResponse:
        runtime = RuntimeOptions()
        return self.get_fund_account_can_transfer_amount_with_options(request, runtime)

    async def get_fund_account_can_transfer_amount_async(
        self,
        request: main_models.GetFundAccountCanTransferAmountRequest,
    ) -> main_models.GetFundAccountCanTransferAmountResponse:
        runtime = RuntimeOptions()
        return await self.get_fund_account_can_transfer_amount_with_options_async(request, runtime)

    def get_fund_account_can_withdraw_amount_with_options(
        self,
        request: main_models.GetFundAccountCanWithdrawAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountCanWithdrawAmountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountCanWithdrawAmount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountCanWithdrawAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_can_withdraw_amount_with_options_async(
        self,
        request: main_models.GetFundAccountCanWithdrawAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountCanWithdrawAmountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountCanWithdrawAmount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountCanWithdrawAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_can_withdraw_amount(
        self,
        request: main_models.GetFundAccountCanWithdrawAmountRequest,
    ) -> main_models.GetFundAccountCanWithdrawAmountResponse:
        runtime = RuntimeOptions()
        return self.get_fund_account_can_withdraw_amount_with_options(request, runtime)

    async def get_fund_account_can_withdraw_amount_async(
        self,
        request: main_models.GetFundAccountCanWithdrawAmountRequest,
    ) -> main_models.GetFundAccountCanWithdrawAmountResponse:
        runtime = RuntimeOptions()
        return await self.get_fund_account_can_withdraw_amount_with_options_async(request, runtime)

    def get_fund_account_low_available_amount_alarm_with_options(
        self,
        request: main_models.GetFundAccountLowAvailableAmountAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountLowAvailableAmountAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountLowAvailableAmountAlarm',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountLowAvailableAmountAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_low_available_amount_alarm_with_options_async(
        self,
        request: main_models.GetFundAccountLowAvailableAmountAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountLowAvailableAmountAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountLowAvailableAmountAlarm',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountLowAvailableAmountAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_low_available_amount_alarm(
        self,
        request: main_models.GetFundAccountLowAvailableAmountAlarmRequest,
    ) -> main_models.GetFundAccountLowAvailableAmountAlarmResponse:
        runtime = RuntimeOptions()
        return self.get_fund_account_low_available_amount_alarm_with_options(request, runtime)

    async def get_fund_account_low_available_amount_alarm_async(
        self,
        request: main_models.GetFundAccountLowAvailableAmountAlarmRequest,
    ) -> main_models.GetFundAccountLowAvailableAmountAlarmResponse:
        runtime = RuntimeOptions()
        return await self.get_fund_account_low_available_amount_alarm_with_options_async(request, runtime)

    def get_fund_account_transaction_details_with_options(
        self,
        tmp_req: main_models.GetFundAccountTransactionDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountTransactionDetailsResponse:
        tmp_req.validate()
        request = main_models.GetFundAccountTransactionDetailsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.transaction_channel_list):
            request.transaction_channel_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.transaction_channel_list, 'TransactionChannelList', 'json')
        if not DaraCore.is_null(tmp_req.transaction_type_list):
            request.transaction_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.transaction_type_list, 'TransactionTypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.bill_number):
            body['BillNumber'] = request.bill_number
        if not DaraCore.is_null(request.channel_transaction_number):
            body['ChannelTransactionNumber'] = request.channel_transaction_number
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.transaction_channel_list_shrink):
            body['TransactionChannelList'] = request.transaction_channel_list_shrink
        if not DaraCore.is_null(request.transaction_direction):
            body['TransactionDirection'] = request.transaction_direction
        if not DaraCore.is_null(request.transaction_number):
            body['TransactionNumber'] = request.transaction_number
        if not DaraCore.is_null(request.transaction_type):
            body['TransactionType'] = request.transaction_type
        if not DaraCore.is_null(request.transaction_type_list_shrink):
            body['TransactionTypeList'] = request.transaction_type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountTransactionDetails',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountTransactionDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_transaction_details_with_options_async(
        self,
        tmp_req: main_models.GetFundAccountTransactionDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFundAccountTransactionDetailsResponse:
        tmp_req.validate()
        request = main_models.GetFundAccountTransactionDetailsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.transaction_channel_list):
            request.transaction_channel_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.transaction_channel_list, 'TransactionChannelList', 'json')
        if not DaraCore.is_null(tmp_req.transaction_type_list):
            request.transaction_type_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.transaction_type_list, 'TransactionTypeList', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.bill_number):
            body['BillNumber'] = request.bill_number
        if not DaraCore.is_null(request.channel_transaction_number):
            body['ChannelTransactionNumber'] = request.channel_transaction_number
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.transaction_channel_list_shrink):
            body['TransactionChannelList'] = request.transaction_channel_list_shrink
        if not DaraCore.is_null(request.transaction_direction):
            body['TransactionDirection'] = request.transaction_direction
        if not DaraCore.is_null(request.transaction_number):
            body['TransactionNumber'] = request.transaction_number
        if not DaraCore.is_null(request.transaction_type):
            body['TransactionType'] = request.transaction_type
        if not DaraCore.is_null(request.transaction_type_list_shrink):
            body['TransactionTypeList'] = request.transaction_type_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFundAccountTransactionDetails',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFundAccountTransactionDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_transaction_details(
        self,
        request: main_models.GetFundAccountTransactionDetailsRequest,
    ) -> main_models.GetFundAccountTransactionDetailsResponse:
        runtime = RuntimeOptions()
        return self.get_fund_account_transaction_details_with_options(request, runtime)

    async def get_fund_account_transaction_details_async(
        self,
        request: main_models.GetFundAccountTransactionDetailsRequest,
    ) -> main_models.GetFundAccountTransactionDetailsResponse:
        runtime = RuntimeOptions()
        return await self.get_fund_account_transaction_details_with_options_async(request, runtime)

    def get_order_detail_with_options(
        self,
        request: main_models.GetOrderDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOrderDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOrderDetail',
            version = '2023-09-30',
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
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not DaraCore.is_null(request.order_id):
            query['OrderId'] = request.order_id
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOrderDetail',
            version = '2023-09-30',
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

    def get_orders_with_options(
        self,
        request: main_models.GetOrdersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOrdersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
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
            action = 'GetOrders',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_orders_with_options_async(
        self,
        request: main_models.GetOrdersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOrdersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not DaraCore.is_null(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not DaraCore.is_null(request.member_uid):
            query['MemberUid'] = request.member_uid
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
            action = 'GetOrders',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_orders(
        self,
        request: main_models.GetOrdersRequest,
    ) -> main_models.GetOrdersResponse:
        runtime = RuntimeOptions()
        return self.get_orders_with_options(request, runtime)

    async def get_orders_async(
        self,
        request: main_models.GetOrdersRequest,
    ) -> main_models.GetOrdersResponse:
        runtime = RuntimeOptions()
        return await self.get_orders_with_options_async(request, runtime)

    def get_saving_plan_deductable_commodity_with_options(
        self,
        tmp_req: main_models.GetSavingPlanDeductableCommodityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSavingPlanDeductableCommodityResponse:
        tmp_req.validate()
        request = main_models.GetSavingPlanDeductableCommodityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSavingPlanDeductableCommodity',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSavingPlanDeductableCommodityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_saving_plan_deductable_commodity_with_options_async(
        self,
        tmp_req: main_models.GetSavingPlanDeductableCommodityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSavingPlanDeductableCommodityResponse:
        tmp_req.validate()
        request = main_models.GetSavingPlanDeductableCommodityShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSavingPlanDeductableCommodity',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSavingPlanDeductableCommodityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_saving_plan_deductable_commodity(
        self,
        request: main_models.GetSavingPlanDeductableCommodityRequest,
    ) -> main_models.GetSavingPlanDeductableCommodityResponse:
        runtime = RuntimeOptions()
        return self.get_saving_plan_deductable_commodity_with_options(request, runtime)

    async def get_saving_plan_deductable_commodity_async(
        self,
        request: main_models.GetSavingPlanDeductableCommodityRequest,
    ) -> main_models.GetSavingPlanDeductableCommodityResponse:
        runtime = RuntimeOptions()
        return await self.get_saving_plan_deductable_commodity_with_options_async(request, runtime)

    def get_saving_plan_share_accounts_with_options(
        self,
        tmp_req: main_models.GetSavingPlanShareAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSavingPlanShareAccountsResponse:
        tmp_req.validate()
        request = main_models.GetSavingPlanShareAccountsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.spn_instance_code):
            query['SpnInstanceCode'] = request.spn_instance_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSavingPlanShareAccounts',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSavingPlanShareAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_saving_plan_share_accounts_with_options_async(
        self,
        tmp_req: main_models.GetSavingPlanShareAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSavingPlanShareAccountsResponse:
        tmp_req.validate()
        request = main_models.GetSavingPlanShareAccountsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.spn_instance_code):
            query['SpnInstanceCode'] = request.spn_instance_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSavingPlanShareAccounts',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSavingPlanShareAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_saving_plan_share_accounts(
        self,
        request: main_models.GetSavingPlanShareAccountsRequest,
    ) -> main_models.GetSavingPlanShareAccountsResponse:
        runtime = RuntimeOptions()
        return self.get_saving_plan_share_accounts_with_options(request, runtime)

    async def get_saving_plan_share_accounts_async(
        self,
        request: main_models.GetSavingPlanShareAccountsRequest,
    ) -> main_models.GetSavingPlanShareAccountsResponse:
        runtime = RuntimeOptions()
        return await self.get_saving_plan_share_accounts_with_options_async(request, runtime)

    def get_saving_plan_user_deduct_rule_with_options(
        self,
        tmp_req: main_models.GetSavingPlanUserDeductRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSavingPlanUserDeductRuleResponse:
        tmp_req.validate()
        request = main_models.GetSavingPlanUserDeductRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.spn_instance_code):
            query['SpnInstanceCode'] = request.spn_instance_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSavingPlanUserDeductRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSavingPlanUserDeductRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_saving_plan_user_deduct_rule_with_options_async(
        self,
        tmp_req: main_models.GetSavingPlanUserDeductRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSavingPlanUserDeductRuleResponse:
        tmp_req.validate()
        request = main_models.GetSavingPlanUserDeductRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.spn_instance_code):
            query['SpnInstanceCode'] = request.spn_instance_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSavingPlanUserDeductRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSavingPlanUserDeductRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_saving_plan_user_deduct_rule(
        self,
        request: main_models.GetSavingPlanUserDeductRuleRequest,
    ) -> main_models.GetSavingPlanUserDeductRuleResponse:
        runtime = RuntimeOptions()
        return self.get_saving_plan_user_deduct_rule_with_options(request, runtime)

    async def get_saving_plan_user_deduct_rule_async(
        self,
        request: main_models.GetSavingPlanUserDeductRuleRequest,
    ) -> main_models.GetSavingPlanUserDeductRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_saving_plan_user_deduct_rule_with_options_async(request, runtime)

    def list_coupon_deduct_tag_with_options(
        self,
        tmp_req: main_models.ListCouponDeductTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCouponDeductTagResponse:
        tmp_req.validate()
        request = main_models.ListCouponDeductTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCouponDeductTag',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCouponDeductTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_coupon_deduct_tag_with_options_async(
        self,
        tmp_req: main_models.ListCouponDeductTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCouponDeductTagResponse:
        tmp_req.validate()
        request = main_models.ListCouponDeductTagShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCouponDeductTag',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCouponDeductTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_coupon_deduct_tag(
        self,
        request: main_models.ListCouponDeductTagRequest,
    ) -> main_models.ListCouponDeductTagResponse:
        runtime = RuntimeOptions()
        return self.list_coupon_deduct_tag_with_options(request, runtime)

    async def list_coupon_deduct_tag_async(
        self,
        request: main_models.ListCouponDeductTagRequest,
    ) -> main_models.ListCouponDeductTagResponse:
        runtime = RuntimeOptions()
        return await self.list_coupon_deduct_tag_with_options_async(request, runtime)

    def list_fund_account_with_options(
        self,
        request: main_models.ListFundAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFundAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.query_only_in_use):
            body['QueryOnlyInUse'] = request.query_only_in_use
        if not DaraCore.is_null(request.query_only_manage):
            body['QueryOnlyManage'] = request.query_only_manage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFundAccount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFundAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fund_account_with_options_async(
        self,
        request: main_models.ListFundAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFundAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.query_only_in_use):
            body['QueryOnlyInUse'] = request.query_only_in_use
        if not DaraCore.is_null(request.query_only_manage):
            body['QueryOnlyManage'] = request.query_only_manage
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFundAccount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFundAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fund_account(
        self,
        request: main_models.ListFundAccountRequest,
    ) -> main_models.ListFundAccountResponse:
        runtime = RuntimeOptions()
        return self.list_fund_account_with_options(request, runtime)

    async def list_fund_account_async(
        self,
        request: main_models.ListFundAccountRequest,
    ) -> main_models.ListFundAccountResponse:
        runtime = RuntimeOptions()
        return await self.list_fund_account_with_options_async(request, runtime)

    def list_fund_account_pay_relation_with_options(
        self,
        request: main_models.ListFundAccountPayRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFundAccountPayRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFundAccountPayRelation',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFundAccountPayRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fund_account_pay_relation_with_options_async(
        self,
        request: main_models.ListFundAccountPayRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFundAccountPayRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFundAccountPayRelation',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFundAccountPayRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fund_account_pay_relation(
        self,
        request: main_models.ListFundAccountPayRelationRequest,
    ) -> main_models.ListFundAccountPayRelationResponse:
        runtime = RuntimeOptions()
        return self.list_fund_account_pay_relation_with_options(request, runtime)

    async def list_fund_account_pay_relation_async(
        self,
        request: main_models.ListFundAccountPayRelationRequest,
    ) -> main_models.ListFundAccountPayRelationResponse:
        runtime = RuntimeOptions()
        return await self.list_fund_account_pay_relation_with_options_async(request, runtime)

    def list_invoice_candidate_with_options(
        self,
        tmp_req: main_models.ListInvoiceCandidateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInvoiceCandidateResponse:
        tmp_req.validate()
        request = main_models.ListInvoiceCandidateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.billing_cycles):
            request.billing_cycles_shrink = Utils.array_to_string_with_specified_style(tmp_req.billing_cycles, 'BillingCycles', 'json')
        if not DaraCore.is_null(tmp_req.business_ids):
            request.business_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.business_ids, 'BusinessIds', 'json')
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not DaraCore.is_null(tmp_req.invoice_issuers):
            request.invoice_issuers_shrink = Utils.array_to_string_with_specified_style(tmp_req.invoice_issuers, 'InvoiceIssuers', 'json')
        if not DaraCore.is_null(tmp_req.status):
            request.status_shrink = Utils.array_to_string_with_specified_style(tmp_req.status, 'Status', 'json')
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'json')
        query = {}
        if not DaraCore.is_null(request.billing_cycles_shrink):
            query['BillingCycles'] = request.billing_cycles_shrink
        if not DaraCore.is_null(request.business_ids_shrink):
            query['BusinessIds'] = request.business_ids_shrink
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.invoice_issuers_shrink):
            query['InvoiceIssuers'] = request.invoice_issuers_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status_shrink):
            query['Status'] = request.status_shrink
        if not DaraCore.is_null(request.types_shrink):
            query['Types'] = request.types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInvoiceCandidate',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInvoiceCandidateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_invoice_candidate_with_options_async(
        self,
        tmp_req: main_models.ListInvoiceCandidateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInvoiceCandidateResponse:
        tmp_req.validate()
        request = main_models.ListInvoiceCandidateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.billing_cycles):
            request.billing_cycles_shrink = Utils.array_to_string_with_specified_style(tmp_req.billing_cycles, 'BillingCycles', 'json')
        if not DaraCore.is_null(tmp_req.business_ids):
            request.business_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.business_ids, 'BusinessIds', 'json')
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not DaraCore.is_null(tmp_req.invoice_issuers):
            request.invoice_issuers_shrink = Utils.array_to_string_with_specified_style(tmp_req.invoice_issuers, 'InvoiceIssuers', 'json')
        if not DaraCore.is_null(tmp_req.status):
            request.status_shrink = Utils.array_to_string_with_specified_style(tmp_req.status, 'Status', 'json')
        if not DaraCore.is_null(tmp_req.types):
            request.types_shrink = Utils.array_to_string_with_specified_style(tmp_req.types, 'Types', 'json')
        query = {}
        if not DaraCore.is_null(request.billing_cycles_shrink):
            query['BillingCycles'] = request.billing_cycles_shrink
        if not DaraCore.is_null(request.business_ids_shrink):
            query['BusinessIds'] = request.business_ids_shrink
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.invoice_issuers_shrink):
            query['InvoiceIssuers'] = request.invoice_issuers_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status_shrink):
            query['Status'] = request.status_shrink
        if not DaraCore.is_null(request.types_shrink):
            query['Types'] = request.types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInvoiceCandidate',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInvoiceCandidateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_invoice_candidate(
        self,
        request: main_models.ListInvoiceCandidateRequest,
    ) -> main_models.ListInvoiceCandidateResponse:
        runtime = RuntimeOptions()
        return self.list_invoice_candidate_with_options(request, runtime)

    async def list_invoice_candidate_async(
        self,
        request: main_models.ListInvoiceCandidateRequest,
    ) -> main_models.ListInvoiceCandidateResponse:
        runtime = RuntimeOptions()
        return await self.list_invoice_candidate_with_options_async(request, runtime)

    def list_invoice_title_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListInvoiceTitleResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListInvoiceTitle',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInvoiceTitleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_invoice_title_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListInvoiceTitleResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListInvoiceTitle',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInvoiceTitleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_invoice_title(self) -> main_models.ListInvoiceTitleResponse:
        runtime = RuntimeOptions()
        return self.list_invoice_title_with_options(runtime)

    async def list_invoice_title_async(self) -> main_models.ListInvoiceTitleResponse:
        runtime = RuntimeOptions()
        return await self.list_invoice_title_with_options_async(runtime)

    def list_report_definitions_with_options(
        self,
        request: main_models.ListReportDefinitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListReportDefinitionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReportDefinitions',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReportDefinitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_report_definitions_with_options_async(
        self,
        request: main_models.ListReportDefinitionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListReportDefinitionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReportDefinitions',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReportDefinitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_report_definitions(
        self,
        request: main_models.ListReportDefinitionsRequest,
    ) -> main_models.ListReportDefinitionsResponse:
        runtime = RuntimeOptions()
        return self.list_report_definitions_with_options(request, runtime)

    async def list_report_definitions_async(
        self,
        request: main_models.ListReportDefinitionsRequest,
    ) -> main_models.ListReportDefinitionsResponse:
        runtime = RuntimeOptions()
        return await self.list_report_definitions_with_options_async(request, runtime)

    def modify_cost_center_with_options(
        self,
        tmp_req: main_models.ModifyCostCenterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCostCenterResponse:
        tmp_req.validate()
        request = main_models.ModifyCostCenterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cost_center_entity_list):
            request.cost_center_entity_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.cost_center_entity_list, 'CostCenterEntityList', 'json')
        query = {}
        if not DaraCore.is_null(request.cost_center_entity_list_shrink):
            query['CostCenterEntityList'] = request.cost_center_entity_list_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCostCenter',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCostCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cost_center_with_options_async(
        self,
        tmp_req: main_models.ModifyCostCenterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCostCenterResponse:
        tmp_req.validate()
        request = main_models.ModifyCostCenterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cost_center_entity_list):
            request.cost_center_entity_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.cost_center_entity_list, 'CostCenterEntityList', 'json')
        query = {}
        if not DaraCore.is_null(request.cost_center_entity_list_shrink):
            query['CostCenterEntityList'] = request.cost_center_entity_list_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCostCenter',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCostCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cost_center(
        self,
        request: main_models.ModifyCostCenterRequest,
    ) -> main_models.ModifyCostCenterResponse:
        runtime = RuntimeOptions()
        return self.modify_cost_center_with_options(request, runtime)

    async def modify_cost_center_async(
        self,
        request: main_models.ModifyCostCenterRequest,
    ) -> main_models.ModifyCostCenterResponse:
        runtime = RuntimeOptions()
        return await self.modify_cost_center_with_options_async(request, runtime)

    def modify_cost_center_rule_with_options(
        self,
        tmp_req: main_models.ModifyCostCenterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCostCenterRuleResponse:
        tmp_req.validate()
        request = main_models.ModifyCostCenterRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_expression):
            request.filter_expression_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_expression, 'FilterExpression', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_expression_shrink):
            query['FilterExpression'] = request.filter_expression_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        if not DaraCore.is_null(request.owner_account_id):
            body['OwnerAccountId'] = request.owner_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCostCenterRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCostCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cost_center_rule_with_options_async(
        self,
        tmp_req: main_models.ModifyCostCenterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCostCenterRuleResponse:
        tmp_req.validate()
        request = main_models.ModifyCostCenterRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter_expression):
            request.filter_expression_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter_expression, 'FilterExpression', 'json')
        query = {}
        if not DaraCore.is_null(request.filter_expression_shrink):
            query['FilterExpression'] = request.filter_expression_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        if not DaraCore.is_null(request.owner_account_id):
            body['OwnerAccountId'] = request.owner_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCostCenterRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCostCenterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cost_center_rule(
        self,
        request: main_models.ModifyCostCenterRuleRequest,
    ) -> main_models.ModifyCostCenterRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_cost_center_rule_with_options(request, runtime)

    async def modify_cost_center_rule_async(
        self,
        request: main_models.ModifyCostCenterRuleRequest,
    ) -> main_models.ModifyCostCenterRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_cost_center_rule_with_options_async(request, runtime)

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
            version = '2023-09-30',
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
            version = '2023-09-30',
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

    def query_cost_center_with_options(
        self,
        tmp_req: main_models.QueryCostCenterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCostCenterResponse:
        tmp_req.validate()
        request = main_models.QueryCostCenterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.owner_account_id):
            query['OwnerAccountId'] = request.owner_account_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_cost_center_id):
            query['ParentCostCenterId'] = request.parent_cost_center_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCostCenter',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCostCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cost_center_with_options_async(
        self,
        tmp_req: main_models.QueryCostCenterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCostCenterResponse:
        tmp_req.validate()
        request = main_models.QueryCostCenterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.owner_account_id):
            query['OwnerAccountId'] = request.owner_account_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_cost_center_id):
            query['ParentCostCenterId'] = request.parent_cost_center_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCostCenter',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCostCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cost_center(
        self,
        request: main_models.QueryCostCenterRequest,
    ) -> main_models.QueryCostCenterResponse:
        runtime = RuntimeOptions()
        return self.query_cost_center_with_options(request, runtime)

    async def query_cost_center_async(
        self,
        request: main_models.QueryCostCenterRequest,
    ) -> main_models.QueryCostCenterResponse:
        runtime = RuntimeOptions()
        return await self.query_cost_center_with_options_async(request, runtime)

    def query_cost_center_resource_with_options(
        self,
        request: main_models.QueryCostCenterResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCostCenterResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not DaraCore.is_null(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        if not DaraCore.is_null(request.owner_account_id):
            body['OwnerAccountId'] = request.owner_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryCostCenterResource',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCostCenterResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cost_center_resource_with_options_async(
        self,
        request: main_models.QueryCostCenterResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCostCenterResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not DaraCore.is_null(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        if not DaraCore.is_null(request.owner_account_id):
            body['OwnerAccountId'] = request.owner_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryCostCenterResource',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCostCenterResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cost_center_resource(
        self,
        request: main_models.QueryCostCenterResourceRequest,
    ) -> main_models.QueryCostCenterResourceResponse:
        runtime = RuntimeOptions()
        return self.query_cost_center_resource_with_options(request, runtime)

    async def query_cost_center_resource_async(
        self,
        request: main_models.QueryCostCenterResourceRequest,
    ) -> main_models.QueryCostCenterResourceResponse:
        runtime = RuntimeOptions()
        return await self.query_cost_center_resource_with_options_async(request, runtime)

    def query_cost_center_rule_with_options(
        self,
        request: main_models.QueryCostCenterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCostCenterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryCostCenterRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCostCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cost_center_rule_with_options_async(
        self,
        request: main_models.QueryCostCenterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCostCenterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not DaraCore.is_null(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryCostCenterRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCostCenterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cost_center_rule(
        self,
        request: main_models.QueryCostCenterRuleRequest,
    ) -> main_models.QueryCostCenterRuleResponse:
        runtime = RuntimeOptions()
        return self.query_cost_center_rule_with_options(request, runtime)

    async def query_cost_center_rule_async(
        self,
        request: main_models.QueryCostCenterRuleRequest,
    ) -> main_models.QueryCostCenterRuleResponse:
        runtime = RuntimeOptions()
        return await self.query_cost_center_rule_with_options_async(request, runtime)

    def query_cost_center_share_rule_with_options(
        self,
        request: main_models.QueryCostCenterShareRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCostCenterShareRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account_id):
            query['OwnerAccountId'] = request.owner_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCostCenterShareRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCostCenterShareRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cost_center_share_rule_with_options_async(
        self,
        request: main_models.QueryCostCenterShareRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCostCenterShareRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account_id):
            query['OwnerAccountId'] = request.owner_account_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCostCenterShareRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCostCenterShareRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cost_center_share_rule(
        self,
        request: main_models.QueryCostCenterShareRuleRequest,
    ) -> main_models.QueryCostCenterShareRuleResponse:
        runtime = RuntimeOptions()
        return self.query_cost_center_share_rule_with_options(request, runtime)

    async def query_cost_center_share_rule_async(
        self,
        request: main_models.QueryCostCenterShareRuleRequest,
    ) -> main_models.QueryCostCenterShareRuleResponse:
        runtime = RuntimeOptions()
        return await self.query_cost_center_share_rule_with_options_async(request, runtime)

    def save_cost_center_share_rule_with_options(
        self,
        tmp_req: main_models.SaveCostCenterShareRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveCostCenterShareRuleResponse:
        tmp_req.validate()
        request = main_models.SaveCostCenterShareRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_share_rule_list):
            request.create_share_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_share_rule_list, 'CreateShareRuleList', 'json')
        if not DaraCore.is_null(tmp_req.modify_share_rule_list):
            request.modify_share_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.modify_share_rule_list, 'ModifyShareRuleList', 'json')
        if not DaraCore.is_null(tmp_req.remove_share_rule_list):
            request.remove_share_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.remove_share_rule_list, 'RemoveShareRuleList', 'json')
        query = {}
        if not DaraCore.is_null(request.create_share_rule_list_shrink):
            query['CreateShareRuleList'] = request.create_share_rule_list_shrink
        if not DaraCore.is_null(request.modify_share_rule_list_shrink):
            query['ModifyShareRuleList'] = request.modify_share_rule_list_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.owner_account_id):
            query['OwnerAccountId'] = request.owner_account_id
        if not DaraCore.is_null(request.remove_share_rule_list_shrink):
            query['RemoveShareRuleList'] = request.remove_share_rule_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveCostCenterShareRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveCostCenterShareRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_cost_center_share_rule_with_options_async(
        self,
        tmp_req: main_models.SaveCostCenterShareRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveCostCenterShareRuleResponse:
        tmp_req.validate()
        request = main_models.SaveCostCenterShareRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_share_rule_list):
            request.create_share_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_share_rule_list, 'CreateShareRuleList', 'json')
        if not DaraCore.is_null(tmp_req.modify_share_rule_list):
            request.modify_share_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.modify_share_rule_list, 'ModifyShareRuleList', 'json')
        if not DaraCore.is_null(tmp_req.remove_share_rule_list):
            request.remove_share_rule_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.remove_share_rule_list, 'RemoveShareRuleList', 'json')
        query = {}
        if not DaraCore.is_null(request.create_share_rule_list_shrink):
            query['CreateShareRuleList'] = request.create_share_rule_list_shrink
        if not DaraCore.is_null(request.modify_share_rule_list_shrink):
            query['ModifyShareRuleList'] = request.modify_share_rule_list_shrink
        if not DaraCore.is_null(request.nbid):
            query['Nbid'] = request.nbid
        if not DaraCore.is_null(request.owner_account_id):
            query['OwnerAccountId'] = request.owner_account_id
        if not DaraCore.is_null(request.remove_share_rule_list_shrink):
            query['RemoveShareRuleList'] = request.remove_share_rule_list_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveCostCenterShareRule',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveCostCenterShareRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_cost_center_share_rule(
        self,
        request: main_models.SaveCostCenterShareRuleRequest,
    ) -> main_models.SaveCostCenterShareRuleResponse:
        runtime = RuntimeOptions()
        return self.save_cost_center_share_rule_with_options(request, runtime)

    async def save_cost_center_share_rule_async(
        self,
        request: main_models.SaveCostCenterShareRuleRequest,
    ) -> main_models.SaveCostCenterShareRuleResponse:
        runtime = RuntimeOptions()
        return await self.save_cost_center_share_rule_with_options_async(request, runtime)

    def set_fund_account_credit_amount_with_options(
        self,
        request: main_models.SetFundAccountCreditAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetFundAccountCreditAmountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.credit_amount):
            body['CreditAmount'] = request.credit_amount
        if not DaraCore.is_null(request.currency):
            body['Currency'] = request.currency
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetFundAccountCreditAmount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetFundAccountCreditAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_fund_account_credit_amount_with_options_async(
        self,
        request: main_models.SetFundAccountCreditAmountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetFundAccountCreditAmountResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.credit_amount):
            body['CreditAmount'] = request.credit_amount
        if not DaraCore.is_null(request.currency):
            body['Currency'] = request.currency
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetFundAccountCreditAmount',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetFundAccountCreditAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_fund_account_credit_amount(
        self,
        request: main_models.SetFundAccountCreditAmountRequest,
    ) -> main_models.SetFundAccountCreditAmountResponse:
        runtime = RuntimeOptions()
        return self.set_fund_account_credit_amount_with_options(request, runtime)

    async def set_fund_account_credit_amount_async(
        self,
        request: main_models.SetFundAccountCreditAmountRequest,
    ) -> main_models.SetFundAccountCreditAmountResponse:
        runtime = RuntimeOptions()
        return await self.set_fund_account_credit_amount_with_options_async(request, runtime)

    def set_fund_account_low_available_amount_alarm_with_options(
        self,
        request: main_models.SetFundAccountLowAvailableAmountAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetFundAccountLowAvailableAmountAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        if not DaraCore.is_null(request.threshold_amount):
            body['ThresholdAmount'] = request.threshold_amount
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetFundAccountLowAvailableAmountAlarm',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetFundAccountLowAvailableAmountAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_fund_account_low_available_amount_alarm_with_options_async(
        self,
        request: main_models.SetFundAccountLowAvailableAmountAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetFundAccountLowAvailableAmountAlarmResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        if not DaraCore.is_null(request.threshold_amount):
            body['ThresholdAmount'] = request.threshold_amount
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SetFundAccountLowAvailableAmountAlarm',
            version = '2023-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetFundAccountLowAvailableAmountAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_fund_account_low_available_amount_alarm(
        self,
        request: main_models.SetFundAccountLowAvailableAmountAlarmRequest,
    ) -> main_models.SetFundAccountLowAvailableAmountAlarmResponse:
        runtime = RuntimeOptions()
        return self.set_fund_account_low_available_amount_alarm_with_options(request, runtime)

    async def set_fund_account_low_available_amount_alarm_async(
        self,
        request: main_models.SetFundAccountLowAvailableAmountAlarmRequest,
    ) -> main_models.SetFundAccountLowAvailableAmountAlarmResponse:
        runtime = RuntimeOptions()
        return await self.set_fund_account_low_available_amount_alarm_with_options_async(request, runtime)

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
            version = '2023-09-30',
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
            version = '2023-09-30',
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
