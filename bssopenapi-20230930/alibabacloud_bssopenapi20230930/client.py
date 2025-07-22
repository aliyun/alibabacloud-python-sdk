# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bssopenapi20230930 import models as bss_open_api_20230930_models
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

    def add_coupon_deduct_tag_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.AddCouponDeductTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.AddCouponDeductTagResponse:
        """
        @summary 添加优惠券抵扣标签
        
        @param tmp_req: AddCouponDeductTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCouponDeductTagResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.AddCouponDeductTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCouponDeductTag',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.AddCouponDeductTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_coupon_deduct_tag_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.AddCouponDeductTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.AddCouponDeductTagResponse:
        """
        @summary 添加优惠券抵扣标签
        
        @param tmp_req: AddCouponDeductTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddCouponDeductTagResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.AddCouponDeductTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCouponDeductTag',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.AddCouponDeductTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_coupon_deduct_tag(
        self,
        request: bss_open_api_20230930_models.AddCouponDeductTagRequest,
    ) -> bss_open_api_20230930_models.AddCouponDeductTagResponse:
        """
        @summary 添加优惠券抵扣标签
        
        @param request: AddCouponDeductTagRequest
        @return: AddCouponDeductTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_coupon_deduct_tag_with_options(request, runtime)

    async def add_coupon_deduct_tag_async(
        self,
        request: bss_open_api_20230930_models.AddCouponDeductTagRequest,
    ) -> bss_open_api_20230930_models.AddCouponDeductTagResponse:
        """
        @summary 添加优惠券抵扣标签
        
        @param request: AddCouponDeductTagRequest
        @return: AddCouponDeductTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_coupon_deduct_tag_with_options_async(request, runtime)

    def allocate_cost_center_resource_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.AllocateCostCenterResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.AllocateCostCenterResourceResponse:
        """
        @summary 财务单元实例重分配
        
        @param tmp_req: AllocateCostCenterResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateCostCenterResourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.AllocateCostCenterResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_instance_list):
            request.resource_instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_instance_list, 'ResourceInstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.from_cost_center_id):
            body['FromCostCenterId'] = request.from_cost_center_id
        if not UtilClient.is_unset(request.from_owner_account_id):
            body['FromOwnerAccountId'] = request.from_owner_account_id
        if not UtilClient.is_unset(request.resource_instance_list_shrink):
            body['ResourceInstanceList'] = request.resource_instance_list_shrink
        if not UtilClient.is_unset(request.to_cost_center_id):
            body['ToCostCenterId'] = request.to_cost_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AllocateCostCenterResource',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.AllocateCostCenterResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_cost_center_resource_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.AllocateCostCenterResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.AllocateCostCenterResourceResponse:
        """
        @summary 财务单元实例重分配
        
        @param tmp_req: AllocateCostCenterResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AllocateCostCenterResourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.AllocateCostCenterResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_instance_list):
            request.resource_instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_instance_list, 'ResourceInstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.from_cost_center_id):
            body['FromCostCenterId'] = request.from_cost_center_id
        if not UtilClient.is_unset(request.from_owner_account_id):
            body['FromOwnerAccountId'] = request.from_owner_account_id
        if not UtilClient.is_unset(request.resource_instance_list_shrink):
            body['ResourceInstanceList'] = request.resource_instance_list_shrink
        if not UtilClient.is_unset(request.to_cost_center_id):
            body['ToCostCenterId'] = request.to_cost_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AllocateCostCenterResource',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.AllocateCostCenterResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_cost_center_resource(
        self,
        request: bss_open_api_20230930_models.AllocateCostCenterResourceRequest,
    ) -> bss_open_api_20230930_models.AllocateCostCenterResourceResponse:
        """
        @summary 财务单元实例重分配
        
        @param request: AllocateCostCenterResourceRequest
        @return: AllocateCostCenterResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.allocate_cost_center_resource_with_options(request, runtime)

    async def allocate_cost_center_resource_async(
        self,
        request: bss_open_api_20230930_models.AllocateCostCenterResourceRequest,
    ) -> bss_open_api_20230930_models.AllocateCostCenterResourceResponse:
        """
        @summary 财务单元实例重分配
        
        @param request: AllocateCostCenterResourceRequest
        @return: AllocateCostCenterResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.allocate_cost_center_resource_with_options_async(request, runtime)

    def cancel_fund_account_low_available_amount_alarm_with_options(
        self,
        request: bss_open_api_20230930_models.CancelFundAccountLowAvailableAmountAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CancelFundAccountLowAvailableAmountAlarmResponse:
        """
        @summary 取消资金账户低额预警
        
        @param request: CancelFundAccountLowAvailableAmountAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelFundAccountLowAvailableAmountAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelFundAccountLowAvailableAmountAlarm',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CancelFundAccountLowAvailableAmountAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_fund_account_low_available_amount_alarm_with_options_async(
        self,
        request: bss_open_api_20230930_models.CancelFundAccountLowAvailableAmountAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CancelFundAccountLowAvailableAmountAlarmResponse:
        """
        @summary 取消资金账户低额预警
        
        @param request: CancelFundAccountLowAvailableAmountAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelFundAccountLowAvailableAmountAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelFundAccountLowAvailableAmountAlarm',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CancelFundAccountLowAvailableAmountAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_fund_account_low_available_amount_alarm(
        self,
        request: bss_open_api_20230930_models.CancelFundAccountLowAvailableAmountAlarmRequest,
    ) -> bss_open_api_20230930_models.CancelFundAccountLowAvailableAmountAlarmResponse:
        """
        @summary 取消资金账户低额预警
        
        @param request: CancelFundAccountLowAvailableAmountAlarmRequest
        @return: CancelFundAccountLowAvailableAmountAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_fund_account_low_available_amount_alarm_with_options(request, runtime)

    async def cancel_fund_account_low_available_amount_alarm_async(
        self,
        request: bss_open_api_20230930_models.CancelFundAccountLowAvailableAmountAlarmRequest,
    ) -> bss_open_api_20230930_models.CancelFundAccountLowAvailableAmountAlarmResponse:
        """
        @summary 取消资金账户低额预警
        
        @param request: CancelFundAccountLowAvailableAmountAlarmRequest
        @return: CancelFundAccountLowAvailableAmountAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_fund_account_low_available_amount_alarm_with_options_async(request, runtime)

    def create_cost_center_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.CreateCostCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CreateCostCenterResponse:
        """
        @summary 创建财务单元
        
        @param tmp_req: CreateCostCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCostCenterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.CreateCostCenterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cost_center_entity_list):
            request.cost_center_entity_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cost_center_entity_list, 'CostCenterEntityList', 'json')
        query = {}
        if not UtilClient.is_unset(request.cost_center_entity_list_shrink):
            query['CostCenterEntityList'] = request.cost_center_entity_list_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCostCenter',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CreateCostCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cost_center_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.CreateCostCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CreateCostCenterResponse:
        """
        @summary 创建财务单元
        
        @param tmp_req: CreateCostCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCostCenterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.CreateCostCenterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cost_center_entity_list):
            request.cost_center_entity_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cost_center_entity_list, 'CostCenterEntityList', 'json')
        query = {}
        if not UtilClient.is_unset(request.cost_center_entity_list_shrink):
            query['CostCenterEntityList'] = request.cost_center_entity_list_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCostCenter',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CreateCostCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cost_center(
        self,
        request: bss_open_api_20230930_models.CreateCostCenterRequest,
    ) -> bss_open_api_20230930_models.CreateCostCenterResponse:
        """
        @summary 创建财务单元
        
        @param request: CreateCostCenterRequest
        @return: CreateCostCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cost_center_with_options(request, runtime)

    async def create_cost_center_async(
        self,
        request: bss_open_api_20230930_models.CreateCostCenterRequest,
    ) -> bss_open_api_20230930_models.CreateCostCenterResponse:
        """
        @summary 创建财务单元
        
        @param request: CreateCostCenterRequest
        @return: CreateCostCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cost_center_with_options_async(request, runtime)

    def create_cost_center_rule_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.CreateCostCenterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CreateCostCenterRuleResponse:
        """
        @summary 新建财务单元规则
        
        @param tmp_req: CreateCostCenterRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCostCenterRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.CreateCostCenterRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_expression):
            request.filter_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_expression, 'FilterExpression', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_expression_shrink):
            query['FilterExpression'] = request.filter_expression_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCostCenterRule',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CreateCostCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cost_center_rule_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.CreateCostCenterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CreateCostCenterRuleResponse:
        """
        @summary 新建财务单元规则
        
        @param tmp_req: CreateCostCenterRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCostCenterRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.CreateCostCenterRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_expression):
            request.filter_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_expression, 'FilterExpression', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_expression_shrink):
            query['FilterExpression'] = request.filter_expression_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCostCenterRule',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CreateCostCenterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cost_center_rule(
        self,
        request: bss_open_api_20230930_models.CreateCostCenterRuleRequest,
    ) -> bss_open_api_20230930_models.CreateCostCenterRuleResponse:
        """
        @summary 新建财务单元规则
        
        @param request: CreateCostCenterRuleRequest
        @return: CreateCostCenterRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cost_center_rule_with_options(request, runtime)

    async def create_cost_center_rule_async(
        self,
        request: bss_open_api_20230930_models.CreateCostCenterRuleRequest,
    ) -> bss_open_api_20230930_models.CreateCostCenterRuleResponse:
        """
        @summary 新建财务单元规则
        
        @param request: CreateCostCenterRuleRequest
        @return: CreateCostCenterRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cost_center_rule_with_options_async(request, runtime)

    def create_fund_account_pay_relation_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.CreateFundAccountPayRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CreateFundAccountPayRelationResponse:
        """
        @summary 创建资金账户付款关系
        
        @param tmp_req: CreateFundAccountPayRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFundAccountPayRelationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.CreateFundAccountPayRelationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFundAccountPayRelation',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CreateFundAccountPayRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fund_account_pay_relation_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.CreateFundAccountPayRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CreateFundAccountPayRelationResponse:
        """
        @summary 创建资金账户付款关系
        
        @param tmp_req: CreateFundAccountPayRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFundAccountPayRelationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.CreateFundAccountPayRelationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFundAccountPayRelation',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CreateFundAccountPayRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fund_account_pay_relation(
        self,
        request: bss_open_api_20230930_models.CreateFundAccountPayRelationRequest,
    ) -> bss_open_api_20230930_models.CreateFundAccountPayRelationResponse:
        """
        @summary 创建资金账户付款关系
        
        @param request: CreateFundAccountPayRelationRequest
        @return: CreateFundAccountPayRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_fund_account_pay_relation_with_options(request, runtime)

    async def create_fund_account_pay_relation_async(
        self,
        request: bss_open_api_20230930_models.CreateFundAccountPayRelationRequest,
    ) -> bss_open_api_20230930_models.CreateFundAccountPayRelationResponse:
        """
        @summary 创建资金账户付款关系
        
        @param request: CreateFundAccountPayRelationRequest
        @return: CreateFundAccountPayRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_fund_account_pay_relation_with_options_async(request, runtime)

    def create_fund_account_transfer_with_options(
        self,
        request: bss_open_api_20230930_models.CreateFundAccountTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CreateFundAccountTransferResponse:
        """
        @summary 创建资金账户划拨/回收
        
        @param request: CreateFundAccountTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFundAccountTransferResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['Amount'] = request.amount
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.finance_type):
            body['FinanceType'] = request.finance_type
        if not UtilClient.is_unset(request.from_fund_account_id):
            body['FromFundAccountId'] = request.from_fund_account_id
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.to_fund_account_id):
            body['ToFundAccountId'] = request.to_fund_account_id
        if not UtilClient.is_unset(request.transfer_type):
            body['TransferType'] = request.transfer_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFundAccountTransfer',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CreateFundAccountTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fund_account_transfer_with_options_async(
        self,
        request: bss_open_api_20230930_models.CreateFundAccountTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CreateFundAccountTransferResponse:
        """
        @summary 创建资金账户划拨/回收
        
        @param request: CreateFundAccountTransferRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFundAccountTransferResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.amount):
            body['Amount'] = request.amount
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.finance_type):
            body['FinanceType'] = request.finance_type
        if not UtilClient.is_unset(request.from_fund_account_id):
            body['FromFundAccountId'] = request.from_fund_account_id
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.to_fund_account_id):
            body['ToFundAccountId'] = request.to_fund_account_id
        if not UtilClient.is_unset(request.transfer_type):
            body['TransferType'] = request.transfer_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFundAccountTransfer',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CreateFundAccountTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fund_account_transfer(
        self,
        request: bss_open_api_20230930_models.CreateFundAccountTransferRequest,
    ) -> bss_open_api_20230930_models.CreateFundAccountTransferResponse:
        """
        @summary 创建资金账户划拨/回收
        
        @param request: CreateFundAccountTransferRequest
        @return: CreateFundAccountTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_fund_account_transfer_with_options(request, runtime)

    async def create_fund_account_transfer_async(
        self,
        request: bss_open_api_20230930_models.CreateFundAccountTransferRequest,
    ) -> bss_open_api_20230930_models.CreateFundAccountTransferResponse:
        """
        @summary 创建资金账户划拨/回收
        
        @param request: CreateFundAccountTransferRequest
        @return: CreateFundAccountTransferResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_fund_account_transfer_with_options_async(request, runtime)

    def create_invoice_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.CreateInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CreateInvoiceResponse:
        """
        @summary 申请发票
        
        @param tmp_req: CreateInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInvoiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.CreateInvoiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.invoice_candidate_ids):
            request.invoice_candidate_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invoice_candidate_ids, 'InvoiceCandidateIds', 'json')
        if not UtilClient.is_unset(tmp_req.recipient_emails):
            request.recipient_emails_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.recipient_emails, 'RecipientEmails', 'json')
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.invoice_candidate_ids_shrink):
            query['InvoiceCandidateIds'] = request.invoice_candidate_ids_shrink
        if not UtilClient.is_unset(request.invoice_mode):
            query['InvoiceMode'] = request.invoice_mode
        if not UtilClient.is_unset(request.invoice_remark):
            query['InvoiceRemark'] = request.invoice_remark
        if not UtilClient.is_unset(request.invoice_title_id):
            query['InvoiceTitleId'] = request.invoice_title_id
        if not UtilClient.is_unset(request.invoice_type):
            query['InvoiceType'] = request.invoice_type
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.recipient_emails_shrink):
            query['RecipientEmails'] = request.recipient_emails_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInvoice',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CreateInvoiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_invoice_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.CreateInvoiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CreateInvoiceResponse:
        """
        @summary 申请发票
        
        @param tmp_req: CreateInvoiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInvoiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.CreateInvoiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.invoice_candidate_ids):
            request.invoice_candidate_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invoice_candidate_ids, 'InvoiceCandidateIds', 'json')
        if not UtilClient.is_unset(tmp_req.recipient_emails):
            request.recipient_emails_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.recipient_emails, 'RecipientEmails', 'json')
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.invoice_candidate_ids_shrink):
            query['InvoiceCandidateIds'] = request.invoice_candidate_ids_shrink
        if not UtilClient.is_unset(request.invoice_mode):
            query['InvoiceMode'] = request.invoice_mode
        if not UtilClient.is_unset(request.invoice_remark):
            query['InvoiceRemark'] = request.invoice_remark
        if not UtilClient.is_unset(request.invoice_title_id):
            query['InvoiceTitleId'] = request.invoice_title_id
        if not UtilClient.is_unset(request.invoice_type):
            query['InvoiceType'] = request.invoice_type
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.recipient_emails_shrink):
            query['RecipientEmails'] = request.recipient_emails_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInvoice',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CreateInvoiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_invoice(
        self,
        request: bss_open_api_20230930_models.CreateInvoiceRequest,
    ) -> bss_open_api_20230930_models.CreateInvoiceResponse:
        """
        @summary 申请发票
        
        @param request: CreateInvoiceRequest
        @return: CreateInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_invoice_with_options(request, runtime)

    async def create_invoice_async(
        self,
        request: bss_open_api_20230930_models.CreateInvoiceRequest,
    ) -> bss_open_api_20230930_models.CreateInvoiceResponse:
        """
        @summary 申请发票
        
        @param request: CreateInvoiceRequest
        @return: CreateInvoiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_invoice_with_options_async(request, runtime)

    def create_report_definition_with_options(
        self,
        request: bss_open_api_20230930_models.CreateReportDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CreateReportDefinitionResponse:
        """
        @summary 创建账单订阅
        
        @param request: CreateReportDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateReportDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_bucket_owner_account_id):
            query['OssBucketOwnerAccountId'] = request.oss_bucket_owner_account_id
        if not UtilClient.is_unset(request.oss_bucket_path):
            query['OssBucketPath'] = request.oss_bucket_path
        if not UtilClient.is_unset(request.report_type):
            query['ReportType'] = request.report_type
        body = {}
        if not UtilClient.is_unset(request.mc_project):
            body['McProject'] = request.mc_project
        if not UtilClient.is_unset(request.mc_table_name):
            body['McTableName'] = request.mc_table_name
        if not UtilClient.is_unset(request.report_source_type):
            body['ReportSourceType'] = request.report_source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateReportDefinition',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CreateReportDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_report_definition_with_options_async(
        self,
        request: bss_open_api_20230930_models.CreateReportDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.CreateReportDefinitionResponse:
        """
        @summary 创建账单订阅
        
        @param request: CreateReportDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateReportDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_billing_cycle):
            query['BeginBillingCycle'] = request.begin_billing_cycle
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.oss_bucket_name):
            query['OssBucketName'] = request.oss_bucket_name
        if not UtilClient.is_unset(request.oss_bucket_owner_account_id):
            query['OssBucketOwnerAccountId'] = request.oss_bucket_owner_account_id
        if not UtilClient.is_unset(request.oss_bucket_path):
            query['OssBucketPath'] = request.oss_bucket_path
        if not UtilClient.is_unset(request.report_type):
            query['ReportType'] = request.report_type
        body = {}
        if not UtilClient.is_unset(request.mc_project):
            body['McProject'] = request.mc_project
        if not UtilClient.is_unset(request.mc_table_name):
            body['McTableName'] = request.mc_table_name
        if not UtilClient.is_unset(request.report_source_type):
            body['ReportSourceType'] = request.report_source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateReportDefinition',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.CreateReportDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_report_definition(
        self,
        request: bss_open_api_20230930_models.CreateReportDefinitionRequest,
    ) -> bss_open_api_20230930_models.CreateReportDefinitionResponse:
        """
        @summary 创建账单订阅
        
        @param request: CreateReportDefinitionRequest
        @return: CreateReportDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_report_definition_with_options(request, runtime)

    async def create_report_definition_async(
        self,
        request: bss_open_api_20230930_models.CreateReportDefinitionRequest,
    ) -> bss_open_api_20230930_models.CreateReportDefinitionResponse:
        """
        @summary 创建账单订阅
        
        @param request: CreateReportDefinitionRequest
        @return: CreateReportDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_report_definition_with_options_async(request, runtime)

    def delete_cost_center_with_options(
        self,
        request: bss_open_api_20230930_models.DeleteCostCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DeleteCostCenterResponse:
        """
        @summary 删除财务单元
        
        @param request: DeleteCostCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCostCenterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cost_center_id):
            query['CostCenterId'] = request.cost_center_id
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.owner_account_id):
            query['OwnerAccountId'] = request.owner_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCostCenter',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DeleteCostCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cost_center_with_options_async(
        self,
        request: bss_open_api_20230930_models.DeleteCostCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DeleteCostCenterResponse:
        """
        @summary 删除财务单元
        
        @param request: DeleteCostCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCostCenterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cost_center_id):
            query['CostCenterId'] = request.cost_center_id
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.owner_account_id):
            query['OwnerAccountId'] = request.owner_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCostCenter',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DeleteCostCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cost_center(
        self,
        request: bss_open_api_20230930_models.DeleteCostCenterRequest,
    ) -> bss_open_api_20230930_models.DeleteCostCenterResponse:
        """
        @summary 删除财务单元
        
        @param request: DeleteCostCenterRequest
        @return: DeleteCostCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cost_center_with_options(request, runtime)

    async def delete_cost_center_async(
        self,
        request: bss_open_api_20230930_models.DeleteCostCenterRequest,
    ) -> bss_open_api_20230930_models.DeleteCostCenterResponse:
        """
        @summary 删除财务单元
        
        @param request: DeleteCostCenterRequest
        @return: DeleteCostCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cost_center_with_options_async(request, runtime)

    def delete_cost_center_rule_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.DeleteCostCenterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DeleteCostCenterRuleResponse:
        """
        @summary 删除财务单元规则
        
        @param tmp_req: DeleteCostCenterRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCostCenterRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.DeleteCostCenterRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_expression):
            request.filter_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_expression, 'FilterExpression', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_expression_shrink):
            query['FilterExpression'] = request.filter_expression_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCostCenterRule',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DeleteCostCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cost_center_rule_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.DeleteCostCenterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DeleteCostCenterRuleResponse:
        """
        @summary 删除财务单元规则
        
        @param tmp_req: DeleteCostCenterRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCostCenterRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.DeleteCostCenterRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_expression):
            request.filter_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_expression, 'FilterExpression', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_expression_shrink):
            query['FilterExpression'] = request.filter_expression_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCostCenterRule',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DeleteCostCenterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cost_center_rule(
        self,
        request: bss_open_api_20230930_models.DeleteCostCenterRuleRequest,
    ) -> bss_open_api_20230930_models.DeleteCostCenterRuleResponse:
        """
        @summary 删除财务单元规则
        
        @param request: DeleteCostCenterRuleRequest
        @return: DeleteCostCenterRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cost_center_rule_with_options(request, runtime)

    async def delete_cost_center_rule_async(
        self,
        request: bss_open_api_20230930_models.DeleteCostCenterRuleRequest,
    ) -> bss_open_api_20230930_models.DeleteCostCenterRuleResponse:
        """
        @summary 删除财务单元规则
        
        @param request: DeleteCostCenterRuleRequest
        @return: DeleteCostCenterRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cost_center_rule_with_options_async(request, runtime)

    def delete_coupon_deduct_tag_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.DeleteCouponDeductTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DeleteCouponDeductTagResponse:
        """
        @summary 删除优惠券的抵扣标签
        
        @param tmp_req: DeleteCouponDeductTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCouponDeductTagResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.DeleteCouponDeductTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        query = {}
        if not UtilClient.is_unset(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCouponDeductTag',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DeleteCouponDeductTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_coupon_deduct_tag_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.DeleteCouponDeductTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DeleteCouponDeductTagResponse:
        """
        @summary 删除优惠券的抵扣标签
        
        @param tmp_req: DeleteCouponDeductTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCouponDeductTagResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.DeleteCouponDeductTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.tag_keys):
            request.tag_keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        query = {}
        if not UtilClient.is_unset(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCouponDeductTag',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DeleteCouponDeductTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_coupon_deduct_tag(
        self,
        request: bss_open_api_20230930_models.DeleteCouponDeductTagRequest,
    ) -> bss_open_api_20230930_models.DeleteCouponDeductTagResponse:
        """
        @summary 删除优惠券的抵扣标签
        
        @param request: DeleteCouponDeductTagRequest
        @return: DeleteCouponDeductTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_coupon_deduct_tag_with_options(request, runtime)

    async def delete_coupon_deduct_tag_async(
        self,
        request: bss_open_api_20230930_models.DeleteCouponDeductTagRequest,
    ) -> bss_open_api_20230930_models.DeleteCouponDeductTagResponse:
        """
        @summary 删除优惠券的抵扣标签
        
        @param request: DeleteCouponDeductTagRequest
        @return: DeleteCouponDeductTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_coupon_deduct_tag_with_options_async(request, runtime)

    def delete_report_definition_with_options(
        self,
        request: bss_open_api_20230930_models.DeleteReportDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DeleteReportDefinitionResponse:
        """
        @summary 取消账单订阅
        
        @param request: DeleteReportDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteReportDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.report_task_id):
            query['ReportTaskId'] = request.report_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReportDefinition',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DeleteReportDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_report_definition_with_options_async(
        self,
        request: bss_open_api_20230930_models.DeleteReportDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DeleteReportDefinitionResponse:
        """
        @summary 取消账单订阅
        
        @param request: DeleteReportDefinitionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteReportDefinitionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.report_task_id):
            query['ReportTaskId'] = request.report_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteReportDefinition',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DeleteReportDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_report_definition(
        self,
        request: bss_open_api_20230930_models.DeleteReportDefinitionRequest,
    ) -> bss_open_api_20230930_models.DeleteReportDefinitionResponse:
        """
        @summary 取消账单订阅
        
        @param request: DeleteReportDefinitionRequest
        @return: DeleteReportDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_report_definition_with_options(request, runtime)

    async def delete_report_definition_async(
        self,
        request: bss_open_api_20230930_models.DeleteReportDefinitionRequest,
    ) -> bss_open_api_20230930_models.DeleteReportDefinitionResponse:
        """
        @summary 取消账单订阅
        
        @param request: DeleteReportDefinitionRequest
        @return: DeleteReportDefinitionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_report_definition_with_options_async(request, runtime)

    def describe_coupon_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.DescribeCouponRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DescribeCouponResponse:
        """
        @summary 查询优惠券列表
        
        @param tmp_req: DescribeCouponRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCouponResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.DescribeCouponShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCoupon',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DescribeCouponResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_coupon_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.DescribeCouponRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DescribeCouponResponse:
        """
        @summary 查询优惠券列表
        
        @param tmp_req: DescribeCouponRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCouponResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.DescribeCouponShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCoupon',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DescribeCouponResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_coupon(
        self,
        request: bss_open_api_20230930_models.DescribeCouponRequest,
    ) -> bss_open_api_20230930_models.DescribeCouponResponse:
        """
        @summary 查询优惠券列表
        
        @param request: DescribeCouponRequest
        @return: DescribeCouponResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_coupon_with_options(request, runtime)

    async def describe_coupon_async(
        self,
        request: bss_open_api_20230930_models.DescribeCouponRequest,
    ) -> bss_open_api_20230930_models.DescribeCouponResponse:
        """
        @summary 查询优惠券列表
        
        @param request: DescribeCouponRequest
        @return: DescribeCouponResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_coupon_with_options_async(request, runtime)

    def describe_coupon_item_list_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.DescribeCouponItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DescribeCouponItemListResponse:
        """
        @summary 查询优惠券可用商品列表
        
        @param tmp_req: DescribeCouponItemListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCouponItemListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.DescribeCouponItemListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCouponItemList',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DescribeCouponItemListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_coupon_item_list_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.DescribeCouponItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DescribeCouponItemListResponse:
        """
        @summary 查询优惠券可用商品列表
        
        @param tmp_req: DescribeCouponItemListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCouponItemListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.DescribeCouponItemListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCouponItemList',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DescribeCouponItemListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_coupon_item_list(
        self,
        request: bss_open_api_20230930_models.DescribeCouponItemListRequest,
    ) -> bss_open_api_20230930_models.DescribeCouponItemListResponse:
        """
        @summary 查询优惠券可用商品列表
        
        @param request: DescribeCouponItemListRequest
        @return: DescribeCouponItemListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_coupon_item_list_with_options(request, runtime)

    async def describe_coupon_item_list_async(
        self,
        request: bss_open_api_20230930_models.DescribeCouponItemListRequest,
    ) -> bss_open_api_20230930_models.DescribeCouponItemListResponse:
        """
        @summary 查询优惠券可用商品列表
        
        @param request: DescribeCouponItemListRequest
        @return: DescribeCouponItemListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_coupon_item_list_with_options_async(request, runtime)

    def describe_user_spn_summary_info_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.DescribeUserSpnSummaryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DescribeUserSpnSummaryInfoResponse:
        """
        @summary 获取客户使用SPN的概述信息
        
        @param tmp_req: DescribeUserSpnSummaryInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserSpnSummaryInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.DescribeUserSpnSummaryInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserSpnSummaryInfo',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DescribeUserSpnSummaryInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_spn_summary_info_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.DescribeUserSpnSummaryInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.DescribeUserSpnSummaryInfoResponse:
        """
        @summary 获取客户使用SPN的概述信息
        
        @param tmp_req: DescribeUserSpnSummaryInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserSpnSummaryInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.DescribeUserSpnSummaryInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserSpnSummaryInfo',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.DescribeUserSpnSummaryInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_spn_summary_info(
        self,
        request: bss_open_api_20230930_models.DescribeUserSpnSummaryInfoRequest,
    ) -> bss_open_api_20230930_models.DescribeUserSpnSummaryInfoResponse:
        """
        @summary 获取客户使用SPN的概述信息
        
        @param request: DescribeUserSpnSummaryInfoRequest
        @return: DescribeUserSpnSummaryInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_spn_summary_info_with_options(request, runtime)

    async def describe_user_spn_summary_info_async(
        self,
        request: bss_open_api_20230930_models.DescribeUserSpnSummaryInfoRequest,
    ) -> bss_open_api_20230930_models.DescribeUserSpnSummaryInfoResponse:
        """
        @summary 获取客户使用SPN的概述信息
        
        @param request: DescribeUserSpnSummaryInfoRequest
        @return: DescribeUserSpnSummaryInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_spn_summary_info_with_options_async(request, runtime)

    def get_fund_account_available_amount_with_options(
        self,
        request: bss_open_api_20230930_models.GetFundAccountAvailableAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountAvailableAmountResponse:
        """
        @summary 查询资金账户可用金
        
        @param request: GetFundAccountAvailableAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountAvailableAmountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountAvailableAmount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountAvailableAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_available_amount_with_options_async(
        self,
        request: bss_open_api_20230930_models.GetFundAccountAvailableAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountAvailableAmountResponse:
        """
        @summary 查询资金账户可用金
        
        @param request: GetFundAccountAvailableAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountAvailableAmountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountAvailableAmount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountAvailableAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_available_amount(
        self,
        request: bss_open_api_20230930_models.GetFundAccountAvailableAmountRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountAvailableAmountResponse:
        """
        @summary 查询资金账户可用金
        
        @param request: GetFundAccountAvailableAmountRequest
        @return: GetFundAccountAvailableAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_fund_account_available_amount_with_options(request, runtime)

    async def get_fund_account_available_amount_async(
        self,
        request: bss_open_api_20230930_models.GetFundAccountAvailableAmountRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountAvailableAmountResponse:
        """
        @summary 查询资金账户可用金
        
        @param request: GetFundAccountAvailableAmountRequest
        @return: GetFundAccountAvailableAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_fund_account_available_amount_with_options_async(request, runtime)

    def get_fund_account_can_allocate_credit_amount_with_options(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanAllocateCreditAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountCanAllocateCreditAmountResponse:
        """
        @summary 查询资金账户可分配信控额度
        
        @param request: GetFundAccountCanAllocateCreditAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountCanAllocateCreditAmountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountCanAllocateCreditAmount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountCanAllocateCreditAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_can_allocate_credit_amount_with_options_async(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanAllocateCreditAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountCanAllocateCreditAmountResponse:
        """
        @summary 查询资金账户可分配信控额度
        
        @param request: GetFundAccountCanAllocateCreditAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountCanAllocateCreditAmountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountCanAllocateCreditAmount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountCanAllocateCreditAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_can_allocate_credit_amount(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanAllocateCreditAmountRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountCanAllocateCreditAmountResponse:
        """
        @summary 查询资金账户可分配信控额度
        
        @param request: GetFundAccountCanAllocateCreditAmountRequest
        @return: GetFundAccountCanAllocateCreditAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_fund_account_can_allocate_credit_amount_with_options(request, runtime)

    async def get_fund_account_can_allocate_credit_amount_async(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanAllocateCreditAmountRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountCanAllocateCreditAmountResponse:
        """
        @summary 查询资金账户可分配信控额度
        
        @param request: GetFundAccountCanAllocateCreditAmountRequest
        @return: GetFundAccountCanAllocateCreditAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_fund_account_can_allocate_credit_amount_with_options_async(request, runtime)

    def get_fund_account_can_recycle_amount_with_options(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanRecycleAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountCanRecycleAmountResponse:
        """
        @summary 查询资金账户可回收金额
        
        @param request: GetFundAccountCanRecycleAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountCanRecycleAmountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.recycle_from_fund_account_id):
            body['RecycleFromFundAccountId'] = request.recycle_from_fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountCanRecycleAmount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountCanRecycleAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_can_recycle_amount_with_options_async(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanRecycleAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountCanRecycleAmountResponse:
        """
        @summary 查询资金账户可回收金额
        
        @param request: GetFundAccountCanRecycleAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountCanRecycleAmountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.recycle_from_fund_account_id):
            body['RecycleFromFundAccountId'] = request.recycle_from_fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountCanRecycleAmount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountCanRecycleAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_can_recycle_amount(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanRecycleAmountRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountCanRecycleAmountResponse:
        """
        @summary 查询资金账户可回收金额
        
        @param request: GetFundAccountCanRecycleAmountRequest
        @return: GetFundAccountCanRecycleAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_fund_account_can_recycle_amount_with_options(request, runtime)

    async def get_fund_account_can_recycle_amount_async(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanRecycleAmountRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountCanRecycleAmountResponse:
        """
        @summary 查询资金账户可回收金额
        
        @param request: GetFundAccountCanRecycleAmountRequest
        @return: GetFundAccountCanRecycleAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_fund_account_can_recycle_amount_with_options_async(request, runtime)

    def get_fund_account_can_transfer_amount_with_options(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanTransferAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountCanTransferAmountResponse:
        """
        @summary 查询资金账户的可转出金额
        
        @param request: GetFundAccountCanTransferAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountCanTransferAmountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountCanTransferAmount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountCanTransferAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_can_transfer_amount_with_options_async(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanTransferAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountCanTransferAmountResponse:
        """
        @summary 查询资金账户的可转出金额
        
        @param request: GetFundAccountCanTransferAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountCanTransferAmountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountCanTransferAmount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountCanTransferAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_can_transfer_amount(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanTransferAmountRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountCanTransferAmountResponse:
        """
        @summary 查询资金账户的可转出金额
        
        @param request: GetFundAccountCanTransferAmountRequest
        @return: GetFundAccountCanTransferAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_fund_account_can_transfer_amount_with_options(request, runtime)

    async def get_fund_account_can_transfer_amount_async(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanTransferAmountRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountCanTransferAmountResponse:
        """
        @summary 查询资金账户的可转出金额
        
        @param request: GetFundAccountCanTransferAmountRequest
        @return: GetFundAccountCanTransferAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_fund_account_can_transfer_amount_with_options_async(request, runtime)

    def get_fund_account_can_withdraw_amount_with_options(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanWithdrawAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountCanWithdrawAmountResponse:
        """
        @summary 查询资金账户可提现金额
        
        @param request: GetFundAccountCanWithdrawAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountCanWithdrawAmountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountCanWithdrawAmount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountCanWithdrawAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_can_withdraw_amount_with_options_async(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanWithdrawAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountCanWithdrawAmountResponse:
        """
        @summary 查询资金账户可提现金额
        
        @param request: GetFundAccountCanWithdrawAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountCanWithdrawAmountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountCanWithdrawAmount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountCanWithdrawAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_can_withdraw_amount(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanWithdrawAmountRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountCanWithdrawAmountResponse:
        """
        @summary 查询资金账户可提现金额
        
        @param request: GetFundAccountCanWithdrawAmountRequest
        @return: GetFundAccountCanWithdrawAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_fund_account_can_withdraw_amount_with_options(request, runtime)

    async def get_fund_account_can_withdraw_amount_async(
        self,
        request: bss_open_api_20230930_models.GetFundAccountCanWithdrawAmountRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountCanWithdrawAmountResponse:
        """
        @summary 查询资金账户可提现金额
        
        @param request: GetFundAccountCanWithdrawAmountRequest
        @return: GetFundAccountCanWithdrawAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_fund_account_can_withdraw_amount_with_options_async(request, runtime)

    def get_fund_account_low_available_amount_alarm_with_options(
        self,
        request: bss_open_api_20230930_models.GetFundAccountLowAvailableAmountAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountLowAvailableAmountAlarmResponse:
        """
        @summary 查询资金账户低额预警
        
        @param request: GetFundAccountLowAvailableAmountAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountLowAvailableAmountAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountLowAvailableAmountAlarm',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountLowAvailableAmountAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_low_available_amount_alarm_with_options_async(
        self,
        request: bss_open_api_20230930_models.GetFundAccountLowAvailableAmountAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountLowAvailableAmountAlarmResponse:
        """
        @summary 查询资金账户低额预警
        
        @param request: GetFundAccountLowAvailableAmountAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountLowAvailableAmountAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountLowAvailableAmountAlarm',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountLowAvailableAmountAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_low_available_amount_alarm(
        self,
        request: bss_open_api_20230930_models.GetFundAccountLowAvailableAmountAlarmRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountLowAvailableAmountAlarmResponse:
        """
        @summary 查询资金账户低额预警
        
        @param request: GetFundAccountLowAvailableAmountAlarmRequest
        @return: GetFundAccountLowAvailableAmountAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_fund_account_low_available_amount_alarm_with_options(request, runtime)

    async def get_fund_account_low_available_amount_alarm_async(
        self,
        request: bss_open_api_20230930_models.GetFundAccountLowAvailableAmountAlarmRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountLowAvailableAmountAlarmResponse:
        """
        @summary 查询资金账户低额预警
        
        @param request: GetFundAccountLowAvailableAmountAlarmRequest
        @return: GetFundAccountLowAvailableAmountAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_fund_account_low_available_amount_alarm_with_options_async(request, runtime)

    def get_fund_account_transaction_details_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.GetFundAccountTransactionDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountTransactionDetailsResponse:
        """
        @summary 查询资金账户收支明细
        
        @param tmp_req: GetFundAccountTransactionDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountTransactionDetailsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.GetFundAccountTransactionDetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.transaction_channel_list):
            request.transaction_channel_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transaction_channel_list, 'TransactionChannelList', 'json')
        if not UtilClient.is_unset(tmp_req.transaction_type_list):
            request.transaction_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transaction_type_list, 'TransactionTypeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.bill_number):
            body['BillNumber'] = request.bill_number
        if not UtilClient.is_unset(request.channel_transaction_number):
            body['ChannelTransactionNumber'] = request.channel_transaction_number
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.transaction_channel_list_shrink):
            body['TransactionChannelList'] = request.transaction_channel_list_shrink
        if not UtilClient.is_unset(request.transaction_direction):
            body['TransactionDirection'] = request.transaction_direction
        if not UtilClient.is_unset(request.transaction_number):
            body['TransactionNumber'] = request.transaction_number
        if not UtilClient.is_unset(request.transaction_type):
            body['TransactionType'] = request.transaction_type
        if not UtilClient.is_unset(request.transaction_type_list_shrink):
            body['TransactionTypeList'] = request.transaction_type_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountTransactionDetails',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountTransactionDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fund_account_transaction_details_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.GetFundAccountTransactionDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetFundAccountTransactionDetailsResponse:
        """
        @summary 查询资金账户收支明细
        
        @param tmp_req: GetFundAccountTransactionDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFundAccountTransactionDetailsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.GetFundAccountTransactionDetailsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.transaction_channel_list):
            request.transaction_channel_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transaction_channel_list, 'TransactionChannelList', 'json')
        if not UtilClient.is_unset(tmp_req.transaction_type_list):
            request.transaction_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transaction_type_list, 'TransactionTypeList', 'json')
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.bill_number):
            body['BillNumber'] = request.bill_number
        if not UtilClient.is_unset(request.channel_transaction_number):
            body['ChannelTransactionNumber'] = request.channel_transaction_number
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.transaction_channel_list_shrink):
            body['TransactionChannelList'] = request.transaction_channel_list_shrink
        if not UtilClient.is_unset(request.transaction_direction):
            body['TransactionDirection'] = request.transaction_direction
        if not UtilClient.is_unset(request.transaction_number):
            body['TransactionNumber'] = request.transaction_number
        if not UtilClient.is_unset(request.transaction_type):
            body['TransactionType'] = request.transaction_type
        if not UtilClient.is_unset(request.transaction_type_list_shrink):
            body['TransactionTypeList'] = request.transaction_type_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFundAccountTransactionDetails',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetFundAccountTransactionDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fund_account_transaction_details(
        self,
        request: bss_open_api_20230930_models.GetFundAccountTransactionDetailsRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountTransactionDetailsResponse:
        """
        @summary 查询资金账户收支明细
        
        @param request: GetFundAccountTransactionDetailsRequest
        @return: GetFundAccountTransactionDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_fund_account_transaction_details_with_options(request, runtime)

    async def get_fund_account_transaction_details_async(
        self,
        request: bss_open_api_20230930_models.GetFundAccountTransactionDetailsRequest,
    ) -> bss_open_api_20230930_models.GetFundAccountTransactionDetailsResponse:
        """
        @summary 查询资金账户收支明细
        
        @param request: GetFundAccountTransactionDetailsRequest
        @return: GetFundAccountTransactionDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_fund_account_transaction_details_with_options_async(request, runtime)

    def get_order_detail_with_options(
        self,
        request: bss_open_api_20230930_models.GetOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetOrderDetailResponse:
        """
        @summary 订单详情查询
        
        @param request: GetOrderDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrderDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderDetail',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_order_detail_with_options_async(
        self,
        request: bss_open_api_20230930_models.GetOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetOrderDetailResponse:
        """
        @summary 订单详情查询
        
        @param request: GetOrderDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrderDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOrderDetail',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetOrderDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_order_detail(
        self,
        request: bss_open_api_20230930_models.GetOrderDetailRequest,
    ) -> bss_open_api_20230930_models.GetOrderDetailResponse:
        """
        @summary 订单详情查询
        
        @param request: GetOrderDetailRequest
        @return: GetOrderDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_order_detail_with_options(request, runtime)

    async def get_order_detail_async(
        self,
        request: bss_open_api_20230930_models.GetOrderDetailRequest,
    ) -> bss_open_api_20230930_models.GetOrderDetailResponse:
        """
        @summary 订单详情查询
        
        @param request: GetOrderDetailRequest
        @return: GetOrderDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_order_detail_with_options_async(request, runtime)

    def get_orders_with_options(
        self,
        request: bss_open_api_20230930_models.GetOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetOrdersResponse:
        """
        @summary 订单列表查询
        
        @param request: GetOrdersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrdersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
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
            action='GetOrders',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_orders_with_options_async(
        self,
        request: bss_open_api_20230930_models.GetOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetOrdersResponse:
        """
        @summary 订单列表查询
        
        @param request: GetOrdersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOrdersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_end):
            query['CreateTimeEnd'] = request.create_time_end
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.member_uid):
            query['MemberUid'] = request.member_uid
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
            action='GetOrders',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_orders(
        self,
        request: bss_open_api_20230930_models.GetOrdersRequest,
    ) -> bss_open_api_20230930_models.GetOrdersResponse:
        """
        @summary 订单列表查询
        
        @param request: GetOrdersRequest
        @return: GetOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_orders_with_options(request, runtime)

    async def get_orders_async(
        self,
        request: bss_open_api_20230930_models.GetOrdersRequest,
    ) -> bss_open_api_20230930_models.GetOrdersResponse:
        """
        @summary 订单列表查询
        
        @param request: GetOrdersRequest
        @return: GetOrdersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_orders_with_options_async(request, runtime)

    def get_saving_plan_deductable_commodity_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.GetSavingPlanDeductableCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetSavingPlanDeductableCommodityResponse:
        """
        @summary 获取节省计划及可抵扣商品信息
        
        @param tmp_req: GetSavingPlanDeductableCommodityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavingPlanDeductableCommodityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.GetSavingPlanDeductableCommodityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSavingPlanDeductableCommodity',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetSavingPlanDeductableCommodityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_saving_plan_deductable_commodity_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.GetSavingPlanDeductableCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetSavingPlanDeductableCommodityResponse:
        """
        @summary 获取节省计划及可抵扣商品信息
        
        @param tmp_req: GetSavingPlanDeductableCommodityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavingPlanDeductableCommodityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.GetSavingPlanDeductableCommodityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSavingPlanDeductableCommodity',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetSavingPlanDeductableCommodityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_saving_plan_deductable_commodity(
        self,
        request: bss_open_api_20230930_models.GetSavingPlanDeductableCommodityRequest,
    ) -> bss_open_api_20230930_models.GetSavingPlanDeductableCommodityResponse:
        """
        @summary 获取节省计划及可抵扣商品信息
        
        @param request: GetSavingPlanDeductableCommodityRequest
        @return: GetSavingPlanDeductableCommodityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_saving_plan_deductable_commodity_with_options(request, runtime)

    async def get_saving_plan_deductable_commodity_async(
        self,
        request: bss_open_api_20230930_models.GetSavingPlanDeductableCommodityRequest,
    ) -> bss_open_api_20230930_models.GetSavingPlanDeductableCommodityResponse:
        """
        @summary 获取节省计划及可抵扣商品信息
        
        @param request: GetSavingPlanDeductableCommodityRequest
        @return: GetSavingPlanDeductableCommodityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_saving_plan_deductable_commodity_with_options_async(request, runtime)

    def get_saving_plan_share_accounts_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.GetSavingPlanShareAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetSavingPlanShareAccountsResponse:
        """
        @summary 获取节省计划实例共享账号信息
        
        @param tmp_req: GetSavingPlanShareAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavingPlanShareAccountsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.GetSavingPlanShareAccountsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.spn_instance_code):
            query['SpnInstanceCode'] = request.spn_instance_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSavingPlanShareAccounts',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetSavingPlanShareAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_saving_plan_share_accounts_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.GetSavingPlanShareAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetSavingPlanShareAccountsResponse:
        """
        @summary 获取节省计划实例共享账号信息
        
        @param tmp_req: GetSavingPlanShareAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavingPlanShareAccountsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.GetSavingPlanShareAccountsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.spn_instance_code):
            query['SpnInstanceCode'] = request.spn_instance_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSavingPlanShareAccounts',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetSavingPlanShareAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_saving_plan_share_accounts(
        self,
        request: bss_open_api_20230930_models.GetSavingPlanShareAccountsRequest,
    ) -> bss_open_api_20230930_models.GetSavingPlanShareAccountsResponse:
        """
        @summary 获取节省计划实例共享账号信息
        
        @param request: GetSavingPlanShareAccountsRequest
        @return: GetSavingPlanShareAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_saving_plan_share_accounts_with_options(request, runtime)

    async def get_saving_plan_share_accounts_async(
        self,
        request: bss_open_api_20230930_models.GetSavingPlanShareAccountsRequest,
    ) -> bss_open_api_20230930_models.GetSavingPlanShareAccountsResponse:
        """
        @summary 获取节省计划实例共享账号信息
        
        @param request: GetSavingPlanShareAccountsRequest
        @return: GetSavingPlanShareAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_saving_plan_share_accounts_with_options_async(request, runtime)

    def get_saving_plan_user_deduct_rule_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.GetSavingPlanUserDeductRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetSavingPlanUserDeductRuleResponse:
        """
        @summary 获取节省计划实例客户自定义规则
        
        @param tmp_req: GetSavingPlanUserDeductRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavingPlanUserDeductRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.GetSavingPlanUserDeductRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.spn_instance_code):
            query['SpnInstanceCode'] = request.spn_instance_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSavingPlanUserDeductRule',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetSavingPlanUserDeductRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_saving_plan_user_deduct_rule_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.GetSavingPlanUserDeductRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.GetSavingPlanUserDeductRuleResponse:
        """
        @summary 获取节省计划实例客户自定义规则
        
        @param tmp_req: GetSavingPlanUserDeductRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSavingPlanUserDeductRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.GetSavingPlanUserDeductRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.spn_instance_code):
            query['SpnInstanceCode'] = request.spn_instance_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSavingPlanUserDeductRule',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.GetSavingPlanUserDeductRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_saving_plan_user_deduct_rule(
        self,
        request: bss_open_api_20230930_models.GetSavingPlanUserDeductRuleRequest,
    ) -> bss_open_api_20230930_models.GetSavingPlanUserDeductRuleResponse:
        """
        @summary 获取节省计划实例客户自定义规则
        
        @param request: GetSavingPlanUserDeductRuleRequest
        @return: GetSavingPlanUserDeductRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_saving_plan_user_deduct_rule_with_options(request, runtime)

    async def get_saving_plan_user_deduct_rule_async(
        self,
        request: bss_open_api_20230930_models.GetSavingPlanUserDeductRuleRequest,
    ) -> bss_open_api_20230930_models.GetSavingPlanUserDeductRuleResponse:
        """
        @summary 获取节省计划实例客户自定义规则
        
        @param request: GetSavingPlanUserDeductRuleRequest
        @return: GetSavingPlanUserDeductRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_saving_plan_user_deduct_rule_with_options_async(request, runtime)

    def list_coupon_deduct_tag_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.ListCouponDeductTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ListCouponDeductTagResponse:
        """
        @summary 查询优惠券设置的抵扣标签
        
        @param tmp_req: ListCouponDeductTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCouponDeductTagResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.ListCouponDeductTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCouponDeductTag',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ListCouponDeductTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_coupon_deduct_tag_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.ListCouponDeductTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ListCouponDeductTagResponse:
        """
        @summary 查询优惠券设置的抵扣标签
        
        @param tmp_req: ListCouponDeductTagRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCouponDeductTagResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.ListCouponDeductTagShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.coupon_id):
            query['CouponId'] = request.coupon_id
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCouponDeductTag',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ListCouponDeductTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_coupon_deduct_tag(
        self,
        request: bss_open_api_20230930_models.ListCouponDeductTagRequest,
    ) -> bss_open_api_20230930_models.ListCouponDeductTagResponse:
        """
        @summary 查询优惠券设置的抵扣标签
        
        @param request: ListCouponDeductTagRequest
        @return: ListCouponDeductTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_coupon_deduct_tag_with_options(request, runtime)

    async def list_coupon_deduct_tag_async(
        self,
        request: bss_open_api_20230930_models.ListCouponDeductTagRequest,
    ) -> bss_open_api_20230930_models.ListCouponDeductTagResponse:
        """
        @summary 查询优惠券设置的抵扣标签
        
        @param request: ListCouponDeductTagRequest
        @return: ListCouponDeductTagResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_coupon_deduct_tag_with_options_async(request, runtime)

    def list_fund_account_with_options(
        self,
        request: bss_open_api_20230930_models.ListFundAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ListFundAccountResponse:
        """
        @summary 查询资金账户列表
        
        @param request: ListFundAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFundAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.query_only_in_use):
            body['QueryOnlyInUse'] = request.query_only_in_use
        if not UtilClient.is_unset(request.query_only_manage):
            body['QueryOnlyManage'] = request.query_only_manage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFundAccount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ListFundAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fund_account_with_options_async(
        self,
        request: bss_open_api_20230930_models.ListFundAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ListFundAccountResponse:
        """
        @summary 查询资金账户列表
        
        @param request: ListFundAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFundAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.query_only_in_use):
            body['QueryOnlyInUse'] = request.query_only_in_use
        if not UtilClient.is_unset(request.query_only_manage):
            body['QueryOnlyManage'] = request.query_only_manage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFundAccount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ListFundAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fund_account(
        self,
        request: bss_open_api_20230930_models.ListFundAccountRequest,
    ) -> bss_open_api_20230930_models.ListFundAccountResponse:
        """
        @summary 查询资金账户列表
        
        @param request: ListFundAccountRequest
        @return: ListFundAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_fund_account_with_options(request, runtime)

    async def list_fund_account_async(
        self,
        request: bss_open_api_20230930_models.ListFundAccountRequest,
    ) -> bss_open_api_20230930_models.ListFundAccountResponse:
        """
        @summary 查询资金账户列表
        
        @param request: ListFundAccountRequest
        @return: ListFundAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_fund_account_with_options_async(request, runtime)

    def list_fund_account_pay_relation_with_options(
        self,
        request: bss_open_api_20230930_models.ListFundAccountPayRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ListFundAccountPayRelationResponse:
        """
        @summary 查询资金账户的付款关系
        
        @param request: ListFundAccountPayRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFundAccountPayRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFundAccountPayRelation',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ListFundAccountPayRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fund_account_pay_relation_with_options_async(
        self,
        request: bss_open_api_20230930_models.ListFundAccountPayRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ListFundAccountPayRelationResponse:
        """
        @summary 查询资金账户的付款关系
        
        @param request: ListFundAccountPayRelationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFundAccountPayRelationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFundAccountPayRelation',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ListFundAccountPayRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fund_account_pay_relation(
        self,
        request: bss_open_api_20230930_models.ListFundAccountPayRelationRequest,
    ) -> bss_open_api_20230930_models.ListFundAccountPayRelationResponse:
        """
        @summary 查询资金账户的付款关系
        
        @param request: ListFundAccountPayRelationRequest
        @return: ListFundAccountPayRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_fund_account_pay_relation_with_options(request, runtime)

    async def list_fund_account_pay_relation_async(
        self,
        request: bss_open_api_20230930_models.ListFundAccountPayRelationRequest,
    ) -> bss_open_api_20230930_models.ListFundAccountPayRelationResponse:
        """
        @summary 查询资金账户的付款关系
        
        @param request: ListFundAccountPayRelationRequest
        @return: ListFundAccountPayRelationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_fund_account_pay_relation_with_options_async(request, runtime)

    def list_invoice_candidate_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.ListInvoiceCandidateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ListInvoiceCandidateResponse:
        """
        @summary 对客OpenAPI开票对象查询
        
        @param tmp_req: ListInvoiceCandidateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInvoiceCandidateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.ListInvoiceCandidateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.billing_cycles):
            request.billing_cycles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.billing_cycles, 'BillingCycles', 'json')
        if not UtilClient.is_unset(tmp_req.business_ids):
            request.business_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.business_ids, 'BusinessIds', 'json')
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.invoice_issuers):
            request.invoice_issuers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invoice_issuers, 'InvoiceIssuers', 'json')
        if not UtilClient.is_unset(tmp_req.status):
            request.status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status, 'Status', 'json')
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'Types', 'json')
        query = {}
        if not UtilClient.is_unset(request.billing_cycles_shrink):
            query['BillingCycles'] = request.billing_cycles_shrink
        if not UtilClient.is_unset(request.business_ids_shrink):
            query['BusinessIds'] = request.business_ids_shrink
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.invoice_issuers_shrink):
            query['InvoiceIssuers'] = request.invoice_issuers_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status_shrink):
            query['Status'] = request.status_shrink
        if not UtilClient.is_unset(request.types_shrink):
            query['Types'] = request.types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInvoiceCandidate',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ListInvoiceCandidateResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_invoice_candidate_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.ListInvoiceCandidateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ListInvoiceCandidateResponse:
        """
        @summary 对客OpenAPI开票对象查询
        
        @param tmp_req: ListInvoiceCandidateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInvoiceCandidateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.ListInvoiceCandidateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.billing_cycles):
            request.billing_cycles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.billing_cycles, 'BillingCycles', 'json')
        if not UtilClient.is_unset(tmp_req.business_ids):
            request.business_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.business_ids, 'BusinessIds', 'json')
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.invoice_issuers):
            request.invoice_issuers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.invoice_issuers, 'InvoiceIssuers', 'json')
        if not UtilClient.is_unset(tmp_req.status):
            request.status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.status, 'Status', 'json')
        if not UtilClient.is_unset(tmp_req.types):
            request.types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.types, 'Types', 'json')
        query = {}
        if not UtilClient.is_unset(request.billing_cycles_shrink):
            query['BillingCycles'] = request.billing_cycles_shrink
        if not UtilClient.is_unset(request.business_ids_shrink):
            query['BusinessIds'] = request.business_ids_shrink
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.invoice_issuers_shrink):
            query['InvoiceIssuers'] = request.invoice_issuers_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status_shrink):
            query['Status'] = request.status_shrink
        if not UtilClient.is_unset(request.types_shrink):
            query['Types'] = request.types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInvoiceCandidate',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ListInvoiceCandidateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_invoice_candidate(
        self,
        request: bss_open_api_20230930_models.ListInvoiceCandidateRequest,
    ) -> bss_open_api_20230930_models.ListInvoiceCandidateResponse:
        """
        @summary 对客OpenAPI开票对象查询
        
        @param request: ListInvoiceCandidateRequest
        @return: ListInvoiceCandidateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_invoice_candidate_with_options(request, runtime)

    async def list_invoice_candidate_async(
        self,
        request: bss_open_api_20230930_models.ListInvoiceCandidateRequest,
    ) -> bss_open_api_20230930_models.ListInvoiceCandidateResponse:
        """
        @summary 对客OpenAPI开票对象查询
        
        @param request: ListInvoiceCandidateRequest
        @return: ListInvoiceCandidateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_invoice_candidate_with_options_async(request, runtime)

    def list_invoice_title_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ListInvoiceTitleResponse:
        """
        @summary 发票抬头查询服务
        
        @param request: ListInvoiceTitleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInvoiceTitleResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListInvoiceTitle',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ListInvoiceTitleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_invoice_title_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ListInvoiceTitleResponse:
        """
        @summary 发票抬头查询服务
        
        @param request: ListInvoiceTitleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInvoiceTitleResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListInvoiceTitle',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ListInvoiceTitleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_invoice_title(self) -> bss_open_api_20230930_models.ListInvoiceTitleResponse:
        """
        @summary 发票抬头查询服务
        
        @return: ListInvoiceTitleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_invoice_title_with_options(runtime)

    async def list_invoice_title_async(self) -> bss_open_api_20230930_models.ListInvoiceTitleResponse:
        """
        @summary 发票抬头查询服务
        
        @return: ListInvoiceTitleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_invoice_title_with_options_async(runtime)

    def list_report_definitions_with_options(
        self,
        request: bss_open_api_20230930_models.ListReportDefinitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ListReportDefinitionsResponse:
        """
        @summary 查看已订阅的报告列表
        
        @param request: ListReportDefinitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListReportDefinitionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReportDefinitions',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ListReportDefinitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_report_definitions_with_options_async(
        self,
        request: bss_open_api_20230930_models.ListReportDefinitionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ListReportDefinitionsResponse:
        """
        @summary 查看已订阅的报告列表
        
        @param request: ListReportDefinitionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListReportDefinitionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReportDefinitions',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ListReportDefinitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_report_definitions(
        self,
        request: bss_open_api_20230930_models.ListReportDefinitionsRequest,
    ) -> bss_open_api_20230930_models.ListReportDefinitionsResponse:
        """
        @summary 查看已订阅的报告列表
        
        @param request: ListReportDefinitionsRequest
        @return: ListReportDefinitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_report_definitions_with_options(request, runtime)

    async def list_report_definitions_async(
        self,
        request: bss_open_api_20230930_models.ListReportDefinitionsRequest,
    ) -> bss_open_api_20230930_models.ListReportDefinitionsResponse:
        """
        @summary 查看已订阅的报告列表
        
        @param request: ListReportDefinitionsRequest
        @return: ListReportDefinitionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_report_definitions_with_options_async(request, runtime)

    def modify_cost_center_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.ModifyCostCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ModifyCostCenterResponse:
        """
        @summary 修改财务单元
        
        @param tmp_req: ModifyCostCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCostCenterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.ModifyCostCenterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cost_center_entity_list):
            request.cost_center_entity_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cost_center_entity_list, 'CostCenterEntityList', 'json')
        query = {}
        if not UtilClient.is_unset(request.cost_center_entity_list_shrink):
            query['CostCenterEntityList'] = request.cost_center_entity_list_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCostCenter',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ModifyCostCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cost_center_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.ModifyCostCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ModifyCostCenterResponse:
        """
        @summary 修改财务单元
        
        @param tmp_req: ModifyCostCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCostCenterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.ModifyCostCenterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cost_center_entity_list):
            request.cost_center_entity_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cost_center_entity_list, 'CostCenterEntityList', 'json')
        query = {}
        if not UtilClient.is_unset(request.cost_center_entity_list_shrink):
            query['CostCenterEntityList'] = request.cost_center_entity_list_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCostCenter',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ModifyCostCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cost_center(
        self,
        request: bss_open_api_20230930_models.ModifyCostCenterRequest,
    ) -> bss_open_api_20230930_models.ModifyCostCenterResponse:
        """
        @summary 修改财务单元
        
        @param request: ModifyCostCenterRequest
        @return: ModifyCostCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cost_center_with_options(request, runtime)

    async def modify_cost_center_async(
        self,
        request: bss_open_api_20230930_models.ModifyCostCenterRequest,
    ) -> bss_open_api_20230930_models.ModifyCostCenterResponse:
        """
        @summary 修改财务单元
        
        @param request: ModifyCostCenterRequest
        @return: ModifyCostCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cost_center_with_options_async(request, runtime)

    def modify_cost_center_rule_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.ModifyCostCenterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ModifyCostCenterRuleResponse:
        """
        @summary 修改财务单元规则
        
        @param tmp_req: ModifyCostCenterRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCostCenterRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.ModifyCostCenterRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_expression):
            request.filter_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_expression, 'FilterExpression', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_expression_shrink):
            query['FilterExpression'] = request.filter_expression_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        if not UtilClient.is_unset(request.owner_account_id):
            body['OwnerAccountId'] = request.owner_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyCostCenterRule',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ModifyCostCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cost_center_rule_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.ModifyCostCenterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.ModifyCostCenterRuleResponse:
        """
        @summary 修改财务单元规则
        
        @param tmp_req: ModifyCostCenterRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCostCenterRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.ModifyCostCenterRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_expression):
            request.filter_expression_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter_expression, 'FilterExpression', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_expression_shrink):
            query['FilterExpression'] = request.filter_expression_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        if not UtilClient.is_unset(request.owner_account_id):
            body['OwnerAccountId'] = request.owner_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyCostCenterRule',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.ModifyCostCenterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cost_center_rule(
        self,
        request: bss_open_api_20230930_models.ModifyCostCenterRuleRequest,
    ) -> bss_open_api_20230930_models.ModifyCostCenterRuleResponse:
        """
        @summary 修改财务单元规则
        
        @param request: ModifyCostCenterRuleRequest
        @return: ModifyCostCenterRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_cost_center_rule_with_options(request, runtime)

    async def modify_cost_center_rule_async(
        self,
        request: bss_open_api_20230930_models.ModifyCostCenterRuleRequest,
    ) -> bss_open_api_20230930_models.ModifyCostCenterRuleResponse:
        """
        @summary 修改财务单元规则
        
        @param request: ModifyCostCenterRuleRequest
        @return: ModifyCostCenterRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_cost_center_rule_with_options_async(request, runtime)

    def query_cost_center_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.QueryCostCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.QueryCostCenterResponse:
        """
        @summary 查询财务单元
        
        @param tmp_req: QueryCostCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCostCenterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.QueryCostCenterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.owner_account_id):
            query['OwnerAccountId'] = request.owner_account_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_cost_center_id):
            query['ParentCostCenterId'] = request.parent_cost_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCostCenter',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.QueryCostCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cost_center_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.QueryCostCenterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.QueryCostCenterResponse:
        """
        @summary 查询财务单元
        
        @param tmp_req: QueryCostCenterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCostCenterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.QueryCostCenterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.owner_account_id):
            query['OwnerAccountId'] = request.owner_account_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_cost_center_id):
            query['ParentCostCenterId'] = request.parent_cost_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCostCenter',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.QueryCostCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cost_center(
        self,
        request: bss_open_api_20230930_models.QueryCostCenterRequest,
    ) -> bss_open_api_20230930_models.QueryCostCenterResponse:
        """
        @summary 查询财务单元
        
        @param request: QueryCostCenterRequest
        @return: QueryCostCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_cost_center_with_options(request, runtime)

    async def query_cost_center_async(
        self,
        request: bss_open_api_20230930_models.QueryCostCenterRequest,
    ) -> bss_open_api_20230930_models.QueryCostCenterResponse:
        """
        @summary 查询财务单元
        
        @param request: QueryCostCenterRequest
        @return: QueryCostCenterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_cost_center_with_options_async(request, runtime)

    def query_cost_center_resource_with_options(
        self,
        request: bss_open_api_20230930_models.QueryCostCenterResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.QueryCostCenterResourceResponse:
        """
        @summary 查询财务单元下资源信息
        
        @param request: QueryCostCenterResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCostCenterResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        if not UtilClient.is_unset(request.owner_account_id):
            body['OwnerAccountId'] = request.owner_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCostCenterResource',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.QueryCostCenterResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cost_center_resource_with_options_async(
        self,
        request: bss_open_api_20230930_models.QueryCostCenterResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.QueryCostCenterResourceResponse:
        """
        @summary 查询财务单元下资源信息
        
        @param request: QueryCostCenterResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCostCenterResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        if not UtilClient.is_unset(request.owner_account_id):
            body['OwnerAccountId'] = request.owner_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCostCenterResource',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.QueryCostCenterResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cost_center_resource(
        self,
        request: bss_open_api_20230930_models.QueryCostCenterResourceRequest,
    ) -> bss_open_api_20230930_models.QueryCostCenterResourceResponse:
        """
        @summary 查询财务单元下资源信息
        
        @param request: QueryCostCenterResourceRequest
        @return: QueryCostCenterResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_cost_center_resource_with_options(request, runtime)

    async def query_cost_center_resource_async(
        self,
        request: bss_open_api_20230930_models.QueryCostCenterResourceRequest,
    ) -> bss_open_api_20230930_models.QueryCostCenterResourceResponse:
        """
        @summary 查询财务单元下资源信息
        
        @param request: QueryCostCenterResourceRequest
        @return: QueryCostCenterResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_cost_center_resource_with_options_async(request, runtime)

    def query_cost_center_rule_with_options(
        self,
        request: bss_open_api_20230930_models.QueryCostCenterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.QueryCostCenterRuleResponse:
        """
        @summary 查询财务单元规则
        
        @param request: QueryCostCenterRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCostCenterRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCostCenterRule',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.QueryCostCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cost_center_rule_with_options_async(
        self,
        request: bss_open_api_20230930_models.QueryCostCenterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.QueryCostCenterRuleResponse:
        """
        @summary 查询财务单元规则
        
        @param request: QueryCostCenterRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCostCenterRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ec_id_account_ids):
            query['EcIdAccountIds'] = request.ec_id_account_ids
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.cost_center_id):
            body['CostCenterId'] = request.cost_center_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCostCenterRule',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.QueryCostCenterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cost_center_rule(
        self,
        request: bss_open_api_20230930_models.QueryCostCenterRuleRequest,
    ) -> bss_open_api_20230930_models.QueryCostCenterRuleResponse:
        """
        @summary 查询财务单元规则
        
        @param request: QueryCostCenterRuleRequest
        @return: QueryCostCenterRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_cost_center_rule_with_options(request, runtime)

    async def query_cost_center_rule_async(
        self,
        request: bss_open_api_20230930_models.QueryCostCenterRuleRequest,
    ) -> bss_open_api_20230930_models.QueryCostCenterRuleResponse:
        """
        @summary 查询财务单元规则
        
        @param request: QueryCostCenterRuleRequest
        @return: QueryCostCenterRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_cost_center_rule_with_options_async(request, runtime)

    def set_fund_account_credit_amount_with_options(
        self,
        request: bss_open_api_20230930_models.SetFundAccountCreditAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.SetFundAccountCreditAmountResponse:
        """
        @summary 设置资金账户的信控限额
        
        @param request: SetFundAccountCreditAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetFundAccountCreditAmountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.credit_amount):
            body['CreditAmount'] = request.credit_amount
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetFundAccountCreditAmount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.SetFundAccountCreditAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_fund_account_credit_amount_with_options_async(
        self,
        request: bss_open_api_20230930_models.SetFundAccountCreditAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.SetFundAccountCreditAmountResponse:
        """
        @summary 设置资金账户的信控限额
        
        @param request: SetFundAccountCreditAmountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetFundAccountCreditAmountResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.credit_amount):
            body['CreditAmount'] = request.credit_amount
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetFundAccountCreditAmount',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.SetFundAccountCreditAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_fund_account_credit_amount(
        self,
        request: bss_open_api_20230930_models.SetFundAccountCreditAmountRequest,
    ) -> bss_open_api_20230930_models.SetFundAccountCreditAmountResponse:
        """
        @summary 设置资金账户的信控限额
        
        @param request: SetFundAccountCreditAmountRequest
        @return: SetFundAccountCreditAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_fund_account_credit_amount_with_options(request, runtime)

    async def set_fund_account_credit_amount_async(
        self,
        request: bss_open_api_20230930_models.SetFundAccountCreditAmountRequest,
    ) -> bss_open_api_20230930_models.SetFundAccountCreditAmountResponse:
        """
        @summary 设置资金账户的信控限额
        
        @param request: SetFundAccountCreditAmountRequest
        @return: SetFundAccountCreditAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_fund_account_credit_amount_with_options_async(request, runtime)

    def set_fund_account_low_available_amount_alarm_with_options(
        self,
        request: bss_open_api_20230930_models.SetFundAccountLowAvailableAmountAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.SetFundAccountLowAvailableAmountAlarmResponse:
        """
        @summary 设置资金账户低额预警
        
        @param request: SetFundAccountLowAvailableAmountAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetFundAccountLowAvailableAmountAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        if not UtilClient.is_unset(request.threshold_amount):
            body['ThresholdAmount'] = request.threshold_amount
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetFundAccountLowAvailableAmountAlarm',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.SetFundAccountLowAvailableAmountAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_fund_account_low_available_amount_alarm_with_options_async(
        self,
        request: bss_open_api_20230930_models.SetFundAccountLowAvailableAmountAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.SetFundAccountLowAvailableAmountAlarmResponse:
        """
        @summary 设置资金账户低额预警
        
        @param request: SetFundAccountLowAvailableAmountAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetFundAccountLowAvailableAmountAlarmResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fund_account_id):
            body['FundAccountId'] = request.fund_account_id
        if not UtilClient.is_unset(request.threshold_amount):
            body['ThresholdAmount'] = request.threshold_amount
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetFundAccountLowAvailableAmountAlarm',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.SetFundAccountLowAvailableAmountAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_fund_account_low_available_amount_alarm(
        self,
        request: bss_open_api_20230930_models.SetFundAccountLowAvailableAmountAlarmRequest,
    ) -> bss_open_api_20230930_models.SetFundAccountLowAvailableAmountAlarmResponse:
        """
        @summary 设置资金账户低额预警
        
        @param request: SetFundAccountLowAvailableAmountAlarmRequest
        @return: SetFundAccountLowAvailableAmountAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_fund_account_low_available_amount_alarm_with_options(request, runtime)

    async def set_fund_account_low_available_amount_alarm_async(
        self,
        request: bss_open_api_20230930_models.SetFundAccountLowAvailableAmountAlarmRequest,
    ) -> bss_open_api_20230930_models.SetFundAccountLowAvailableAmountAlarmResponse:
        """
        @summary 设置资金账户低额预警
        
        @param request: SetFundAccountLowAvailableAmountAlarmRequest
        @return: SetFundAccountLowAvailableAmountAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_fund_account_low_available_amount_alarm_with_options_async(request, runtime)

    def set_saving_plan_user_deduct_rule_with_options(
        self,
        tmp_req: bss_open_api_20230930_models.SetSavingPlanUserDeductRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.SetSavingPlanUserDeductRuleResponse:
        """
        @summary 设置节省计划用户级抵扣规则
        
        @param tmp_req: SetSavingPlanUserDeductRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSavingPlanUserDeductRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.SetSavingPlanUserDeductRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.user_deduct_rules):
            request.user_deduct_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_deduct_rules, 'UserDeductRules', 'json')
        query = {}
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.spn_instance_code):
            body['SpnInstanceCode'] = request.spn_instance_code
        if not UtilClient.is_unset(request.user_deduct_rules_shrink):
            body['UserDeductRules'] = request.user_deduct_rules_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetSavingPlanUserDeductRule',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.SetSavingPlanUserDeductRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_saving_plan_user_deduct_rule_with_options_async(
        self,
        tmp_req: bss_open_api_20230930_models.SetSavingPlanUserDeductRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bss_open_api_20230930_models.SetSavingPlanUserDeductRuleResponse:
        """
        @summary 设置节省计划用户级抵扣规则
        
        @param tmp_req: SetSavingPlanUserDeductRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetSavingPlanUserDeductRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = bss_open_api_20230930_models.SetSavingPlanUserDeductRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ec_id_account_ids):
            request.ec_id_account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ec_id_account_ids, 'EcIdAccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.user_deduct_rules):
            request.user_deduct_rules_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_deduct_rules, 'UserDeductRules', 'json')
        query = {}
        if not UtilClient.is_unset(request.ec_id_account_ids_shrink):
            query['EcIdAccountIds'] = request.ec_id_account_ids_shrink
        if not UtilClient.is_unset(request.nbid):
            query['Nbid'] = request.nbid
        body = {}
        if not UtilClient.is_unset(request.spn_instance_code):
            body['SpnInstanceCode'] = request.spn_instance_code
        if not UtilClient.is_unset(request.user_deduct_rules_shrink):
            body['UserDeductRules'] = request.user_deduct_rules_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetSavingPlanUserDeductRule',
            version='2023-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bss_open_api_20230930_models.SetSavingPlanUserDeductRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_saving_plan_user_deduct_rule(
        self,
        request: bss_open_api_20230930_models.SetSavingPlanUserDeductRuleRequest,
    ) -> bss_open_api_20230930_models.SetSavingPlanUserDeductRuleResponse:
        """
        @summary 设置节省计划用户级抵扣规则
        
        @param request: SetSavingPlanUserDeductRuleRequest
        @return: SetSavingPlanUserDeductRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_saving_plan_user_deduct_rule_with_options(request, runtime)

    async def set_saving_plan_user_deduct_rule_async(
        self,
        request: bss_open_api_20230930_models.SetSavingPlanUserDeductRuleRequest,
    ) -> bss_open_api_20230930_models.SetSavingPlanUserDeductRuleResponse:
        """
        @summary 设置节省计划用户级抵扣规则
        
        @param request: SetSavingPlanUserDeductRuleRequest
        @return: SetSavingPlanUserDeductRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_saving_plan_user_deduct_rule_with_options_async(request, runtime)
