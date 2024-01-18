# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkedmall20180116 import models as linkedmall_20180116_models
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
            'cn-hangzhou': 'linkedmall.aliyuncs.com',
            'cn-shanghai': 'linkedmall.aliyuncs.com',
            'ap-northeast-1': 'linkedmall.aliyuncs.com',
            'ap-northeast-2-pop': 'linkedmall.aliyuncs.com',
            'ap-south-1': 'linkedmall.aliyuncs.com',
            'ap-southeast-1': 'linkedmall.aliyuncs.com',
            'ap-southeast-2': 'linkedmall.aliyuncs.com',
            'ap-southeast-3': 'linkedmall.aliyuncs.com',
            'ap-southeast-5': 'linkedmall.aliyuncs.com',
            'cn-beijing': 'linkedmall.aliyuncs.com',
            'cn-beijing-finance-1': 'linkedmall.aliyuncs.com',
            'cn-beijing-finance-pop': 'linkedmall.aliyuncs.com',
            'cn-beijing-gov-1': 'linkedmall.aliyuncs.com',
            'cn-beijing-nu16-b01': 'linkedmall.aliyuncs.com',
            'cn-chengdu': 'linkedmall.aliyuncs.com',
            'cn-edge-1': 'linkedmall.aliyuncs.com',
            'cn-fujian': 'linkedmall.aliyuncs.com',
            'cn-haidian-cm12-c01': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-finance': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'linkedmall.aliyuncs.com',
            'cn-hangzhou-test-306': 'linkedmall.aliyuncs.com',
            'cn-hongkong': 'linkedmall.aliyuncs.com',
            'cn-hongkong-finance-pop': 'linkedmall.aliyuncs.com',
            'cn-huhehaote': 'linkedmall.aliyuncs.com',
            'cn-north-2-gov-1': 'linkedmall.aliyuncs.com',
            'cn-qingdao': 'linkedmall.aliyuncs.com',
            'cn-qingdao-nebula': 'linkedmall.aliyuncs.com',
            'cn-shanghai-et15-b01': 'linkedmall.aliyuncs.com',
            'cn-shanghai-et2-b01': 'linkedmall.aliyuncs.com',
            'cn-shanghai-finance-1': 'linkedmall.aliyuncs.com',
            'cn-shanghai-inner': 'linkedmall.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'linkedmall.aliyuncs.com',
            'cn-shenzhen': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-finance-1': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-inner': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'linkedmall.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'linkedmall.aliyuncs.com',
            'cn-wuhan': 'linkedmall.aliyuncs.com',
            'cn-yushanfang': 'linkedmall.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'linkedmall.aliyuncs.com',
            'cn-zhangjiakou': 'linkedmall.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'linkedmall.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'linkedmall.aliyuncs.com',
            'eu-central-1': 'linkedmall.aliyuncs.com',
            'eu-west-1': 'linkedmall.aliyuncs.com',
            'eu-west-1-oxs': 'linkedmall.aliyuncs.com',
            'me-east-1': 'linkedmall.aliyuncs.com',
            'rus-west-1-pop': 'linkedmall.aliyuncs.com',
            'us-east-1': 'linkedmall.aliyuncs.com',
            'us-west-1': 'linkedmall.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('linkedmall', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_address_with_options(
        self,
        request: linkedmall_20180116_models.AddAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.address_info):
            body['AddressInfo'] = request.address_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAddress',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_address_with_options_async(
        self,
        request: linkedmall_20180116_models.AddAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.address_info):
            body['AddressInfo'] = request.address_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAddress',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_address(
        self,
        request: linkedmall_20180116_models.AddAddressRequest,
    ) -> linkedmall_20180116_models.AddAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_address_with_options(request, runtime)

    async def add_address_async(
        self,
        request: linkedmall_20180116_models.AddAddressRequest,
    ) -> linkedmall_20180116_models.AddAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_address_with_options_async(request, runtime)

    def add_item_limit_rule_with_options(
        self,
        request: linkedmall_20180116_models.AddItemLimitRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddItemLimitRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_activity_id):
            query['LmActivityId'] = request.lm_activity_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.sub_biz_code):
            query['SubBizCode'] = request.sub_biz_code
        if not UtilClient.is_unset(request.upper_num):
            query['UpperNum'] = request.upper_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddItemLimitRule',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddItemLimitRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_item_limit_rule_with_options_async(
        self,
        request: linkedmall_20180116_models.AddItemLimitRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddItemLimitRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_activity_id):
            query['LmActivityId'] = request.lm_activity_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.sub_biz_code):
            query['SubBizCode'] = request.sub_biz_code
        if not UtilClient.is_unset(request.upper_num):
            query['UpperNum'] = request.upper_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddItemLimitRule',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddItemLimitRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_item_limit_rule(
        self,
        request: linkedmall_20180116_models.AddItemLimitRuleRequest,
    ) -> linkedmall_20180116_models.AddItemLimitRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_item_limit_rule_with_options(request, runtime)

    async def add_item_limit_rule_async(
        self,
        request: linkedmall_20180116_models.AddItemLimitRuleRequest,
    ) -> linkedmall_20180116_models.AddItemLimitRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_item_limit_rule_with_options_async(request, runtime)

    def add_item_to_sub_bizs_with_options(
        self,
        tmp_req: linkedmall_20180116_models.AddItemToSubBizsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddItemToSubBizsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.AddItemToSubBizsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_biz_ids):
            request.sub_biz_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_biz_ids, 'SubBizIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_item_id):
            body['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.sub_biz_ids_shrink):
            body['SubBizIds'] = request.sub_biz_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddItemToSubBizs',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddItemToSubBizsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_item_to_sub_bizs_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.AddItemToSubBizsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddItemToSubBizsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.AddItemToSubBizsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_biz_ids):
            request.sub_biz_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_biz_ids, 'SubBizIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_item_id):
            body['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.sub_biz_ids_shrink):
            body['SubBizIds'] = request.sub_biz_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddItemToSubBizs',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddItemToSubBizsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_item_to_sub_bizs(
        self,
        request: linkedmall_20180116_models.AddItemToSubBizsRequest,
    ) -> linkedmall_20180116_models.AddItemToSubBizsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_item_to_sub_bizs_with_options(request, runtime)

    async def add_item_to_sub_bizs_async(
        self,
        request: linkedmall_20180116_models.AddItemToSubBizsRequest,
    ) -> linkedmall_20180116_models.AddItemToSubBizsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_item_to_sub_bizs_with_options_async(request, runtime)

    def add_supplier_new_items_with_options(
        self,
        request: linkedmall_20180116_models.AddSupplierNewItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddSupplierNewItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSupplierNewItems',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddSupplierNewItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_supplier_new_items_with_options_async(
        self,
        request: linkedmall_20180116_models.AddSupplierNewItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.AddSupplierNewItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSupplierNewItems',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.AddSupplierNewItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_supplier_new_items(
        self,
        request: linkedmall_20180116_models.AddSupplierNewItemsRequest,
    ) -> linkedmall_20180116_models.AddSupplierNewItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_supplier_new_items_with_options(request, runtime)

    async def add_supplier_new_items_async(
        self,
        request: linkedmall_20180116_models.AddSupplierNewItemsRequest,
    ) -> linkedmall_20180116_models.AddSupplierNewItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_supplier_new_items_with_options_async(request, runtime)

    def apply_refund_with_options(
        self,
        request: linkedmall_20180116_models.ApplyRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ApplyRefundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.apply_reason_text_id):
            query['ApplyReasonTextId'] = request.apply_reason_text_id
        if not UtilClient.is_unset(request.apply_refund_count):
            query['ApplyRefundCount'] = request.apply_refund_count
        if not UtilClient.is_unset(request.apply_refund_fee):
            query['ApplyRefundFee'] = request.apply_refund_fee
        if not UtilClient.is_unset(request.biz_claim_type):
            query['BizClaimType'] = request.biz_claim_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.goods_status):
            query['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.leave_message):
            body['LeaveMessage'] = request.leave_message
        if not UtilClient.is_unset(request.leave_picture_list):
            body['LeavePictureList'] = request.leave_picture_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyRefund',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ApplyRefundResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_refund_with_options_async(
        self,
        request: linkedmall_20180116_models.ApplyRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ApplyRefundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.apply_reason_text_id):
            query['ApplyReasonTextId'] = request.apply_reason_text_id
        if not UtilClient.is_unset(request.apply_refund_count):
            query['ApplyRefundCount'] = request.apply_refund_count
        if not UtilClient.is_unset(request.apply_refund_fee):
            query['ApplyRefundFee'] = request.apply_refund_fee
        if not UtilClient.is_unset(request.biz_claim_type):
            query['BizClaimType'] = request.biz_claim_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.goods_status):
            query['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.leave_message):
            body['LeaveMessage'] = request.leave_message
        if not UtilClient.is_unset(request.leave_picture_list):
            body['LeavePictureList'] = request.leave_picture_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyRefund',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ApplyRefundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_refund(
        self,
        request: linkedmall_20180116_models.ApplyRefundRequest,
    ) -> linkedmall_20180116_models.ApplyRefundResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_refund_with_options(request, runtime)

    async def apply_refund_async(
        self,
        request: linkedmall_20180116_models.ApplyRefundRequest,
    ) -> linkedmall_20180116_models.ApplyRefundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_refund_with_options_async(request, runtime)

    def apply_refund_with_designated_tb_uid_with_options(
        self,
        tmp_req: linkedmall_20180116_models.ApplyRefundWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ApplyRefundWithDesignatedTbUidResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.ApplyRefundWithDesignatedTbUidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.proofs):
            request.proofs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.proofs, 'Proofs', 'json')
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.goods_status):
            body['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.proofs_shrink):
            body['Proofs'] = request.proofs_shrink
        if not UtilClient.is_unset(request.reason_id):
            body['ReasonId'] = request.reason_id
        if not UtilClient.is_unset(request.refund_code):
            body['RefundCode'] = request.refund_code
        if not UtilClient.is_unset(request.refund_count):
            body['RefundCount'] = request.refund_count
        if not UtilClient.is_unset(request.refund_fee):
            body['RefundFee'] = request.refund_fee
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyRefundWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ApplyRefundWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_refund_with_designated_tb_uid_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.ApplyRefundWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ApplyRefundWithDesignatedTbUidResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.ApplyRefundWithDesignatedTbUidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.proofs):
            request.proofs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.proofs, 'Proofs', 'json')
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.goods_status):
            body['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.proofs_shrink):
            body['Proofs'] = request.proofs_shrink
        if not UtilClient.is_unset(request.reason_id):
            body['ReasonId'] = request.reason_id
        if not UtilClient.is_unset(request.refund_code):
            body['RefundCode'] = request.refund_code
        if not UtilClient.is_unset(request.refund_count):
            body['RefundCount'] = request.refund_count
        if not UtilClient.is_unset(request.refund_fee):
            body['RefundFee'] = request.refund_fee
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyRefundWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ApplyRefundWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_refund_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.ApplyRefundWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.ApplyRefundWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_refund_with_designated_tb_uid_with_options(request, runtime)

    async def apply_refund_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.ApplyRefundWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.ApplyRefundWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_refund_with_designated_tb_uid_with_options_async(request, runtime)

    def batch_regist_anonymous_tb_account_with_options(
        self,
        request: linkedmall_20180116_models.BatchRegistAnonymousTbAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.BatchRegistAnonymousTbAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.id_json_list):
            query['IdJsonList'] = request.id_json_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchRegistAnonymousTbAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.BatchRegistAnonymousTbAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_regist_anonymous_tb_account_with_options_async(
        self,
        request: linkedmall_20180116_models.BatchRegistAnonymousTbAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.BatchRegistAnonymousTbAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.id_json_list):
            query['IdJsonList'] = request.id_json_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchRegistAnonymousTbAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.BatchRegistAnonymousTbAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_regist_anonymous_tb_account(
        self,
        request: linkedmall_20180116_models.BatchRegistAnonymousTbAccountRequest,
    ) -> linkedmall_20180116_models.BatchRegistAnonymousTbAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_regist_anonymous_tb_account_with_options(request, runtime)

    async def batch_regist_anonymous_tb_account_async(
        self,
        request: linkedmall_20180116_models.BatchRegistAnonymousTbAccountRequest,
    ) -> linkedmall_20180116_models.BatchRegistAnonymousTbAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_regist_anonymous_tb_account_with_options_async(request, runtime)

    def cancel_order_with_options(
        self,
        request: linkedmall_20180116_models.CancelOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_order_with_options_async(
        self,
        request: linkedmall_20180116_models.CancelOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_order(
        self,
        request: linkedmall_20180116_models.CancelOrderRequest,
    ) -> linkedmall_20180116_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_with_options(request, runtime)

    async def cancel_order_async(
        self,
        request: linkedmall_20180116_models.CancelOrderRequest,
    ) -> linkedmall_20180116_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_order_with_options_async(request, runtime)

    def cancel_order_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.CancelOrderWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelOrderWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_order_id):
            body['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelOrderWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelOrderWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_order_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.CancelOrderWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelOrderWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_order_id):
            body['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelOrderWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelOrderWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_order_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.CancelOrderWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.CancelOrderWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_with_designated_tb_uid_with_options(request, runtime)

    async def cancel_order_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.CancelOrderWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.CancelOrderWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_order_with_designated_tb_uid_with_options_async(request, runtime)

    def cancel_real_tb_account_support_with_options(
        self,
        request: linkedmall_20180116_models.CancelRealTbAccountSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelRealTbAccountSupportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelRealTbAccountSupport',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelRealTbAccountSupportResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_real_tb_account_support_with_options_async(
        self,
        request: linkedmall_20180116_models.CancelRealTbAccountSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelRealTbAccountSupportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelRealTbAccountSupport',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelRealTbAccountSupportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_real_tb_account_support(
        self,
        request: linkedmall_20180116_models.CancelRealTbAccountSupportRequest,
    ) -> linkedmall_20180116_models.CancelRealTbAccountSupportResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_real_tb_account_support_with_options(request, runtime)

    async def cancel_real_tb_account_support_async(
        self,
        request: linkedmall_20180116_models.CancelRealTbAccountSupportRequest,
    ) -> linkedmall_20180116_models.CancelRealTbAccountSupportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_real_tb_account_support_with_options_async(request, runtime)

    def cancel_refund_with_options(
        self,
        request: linkedmall_20180116_models.CancelRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelRefundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.dispute_id):
            query['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelRefund',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelRefundResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_refund_with_options_async(
        self,
        request: linkedmall_20180116_models.CancelRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelRefundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.dispute_id):
            query['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelRefund',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelRefundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_refund(
        self,
        request: linkedmall_20180116_models.CancelRefundRequest,
    ) -> linkedmall_20180116_models.CancelRefundResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_refund_with_options(request, runtime)

    async def cancel_refund_async(
        self,
        request: linkedmall_20180116_models.CancelRefundRequest,
    ) -> linkedmall_20180116_models.CancelRefundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_refund_with_options_async(request, runtime)

    def cancel_refund_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.CancelRefundWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelRefundWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelRefundWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelRefundWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_refund_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.CancelRefundWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CancelRefundWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelRefundWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CancelRefundWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_refund_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.CancelRefundWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.CancelRefundWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_refund_with_designated_tb_uid_with_options(request, runtime)

    async def cancel_refund_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.CancelRefundWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.CancelRefundWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_refund_with_designated_tb_uid_with_options_async(request, runtime)

    def confirm_disburse_with_options(
        self,
        request: linkedmall_20180116_models.ConfirmDisburseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ConfirmDisburseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmDisburse',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ConfirmDisburseResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_disburse_with_options_async(
        self,
        request: linkedmall_20180116_models.ConfirmDisburseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ConfirmDisburseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmDisburse',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ConfirmDisburseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_disburse(
        self,
        request: linkedmall_20180116_models.ConfirmDisburseRequest,
    ) -> linkedmall_20180116_models.ConfirmDisburseResponse:
        runtime = util_models.RuntimeOptions()
        return self.confirm_disburse_with_options(request, runtime)

    async def confirm_disburse_async(
        self,
        request: linkedmall_20180116_models.ConfirmDisburseRequest,
    ) -> linkedmall_20180116_models.ConfirmDisburseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_disburse_with_options_async(request, runtime)

    def confirm_disburse_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.ConfirmDisburseWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ConfirmDisburseWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_order_id):
            body['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfirmDisburseWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ConfirmDisburseWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_disburse_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.ConfirmDisburseWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ConfirmDisburseWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_order_id):
            body['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfirmDisburseWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ConfirmDisburseWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_disburse_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.ConfirmDisburseWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.ConfirmDisburseWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.confirm_disburse_with_designated_tb_uid_with_options(request, runtime)

    async def confirm_disburse_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.ConfirmDisburseWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.ConfirmDisburseWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_disburse_with_designated_tb_uid_with_options_async(request, runtime)

    def create_movie_ticket_order_with_options(
        self,
        request: linkedmall_20180116_models.CreateMovieTicketOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateMovieTicketOrderResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMovieTicketOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateMovieTicketOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_movie_ticket_order_with_options_async(
        self,
        request: linkedmall_20180116_models.CreateMovieTicketOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateMovieTicketOrderResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMovieTicketOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateMovieTicketOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_movie_ticket_order(
        self,
        request: linkedmall_20180116_models.CreateMovieTicketOrderRequest,
    ) -> linkedmall_20180116_models.CreateMovieTicketOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_movie_ticket_order_with_options(request, runtime)

    async def create_movie_ticket_order_async(
        self,
        request: linkedmall_20180116_models.CreateMovieTicketOrderRequest,
    ) -> linkedmall_20180116_models.CreateMovieTicketOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_movie_ticket_order_with_options_async(request, runtime)

    def create_order_with_options(
        self,
        request: linkedmall_20180116_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.buyer_message_map):
            query['BuyerMessageMap'] = request.buyer_message_map
        if not UtilClient.is_unset(request.delivery_address):
            query['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.order_expire_time):
            query['OrderExpireTime'] = request.order_expire_time
        if not UtilClient.is_unset(request.out_trade_id):
            query['OutTradeId'] = request.out_trade_id
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.total_amount):
            query['TotalAmount'] = request.total_amount
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_with_options_async(
        self,
        request: linkedmall_20180116_models.CreateOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.buyer_message_map):
            query['BuyerMessageMap'] = request.buyer_message_map
        if not UtilClient.is_unset(request.delivery_address):
            query['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.order_expire_time):
            query['OrderExpireTime'] = request.order_expire_time
        if not UtilClient.is_unset(request.out_trade_id):
            query['OutTradeId'] = request.out_trade_id
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.total_amount):
            query['TotalAmount'] = request.total_amount
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order(
        self,
        request: linkedmall_20180116_models.CreateOrderRequest,
    ) -> linkedmall_20180116_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_options(request, runtime)

    async def create_order_async(
        self,
        request: linkedmall_20180116_models.CreateOrderRequest,
    ) -> linkedmall_20180116_models.CreateOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_with_options_async(request, runtime)

    def create_order_pay_url_for_out_discount_with_options(
        self,
        request: linkedmall_20180116_models.CreateOrderPayUrlForOutDiscountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderPayUrlForOutDiscountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.buy_info):
            body['BuyInfo'] = request.buy_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrderPayUrlForOutDiscount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderPayUrlForOutDiscountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_pay_url_for_out_discount_with_options_async(
        self,
        request: linkedmall_20180116_models.CreateOrderPayUrlForOutDiscountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderPayUrlForOutDiscountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.buy_info):
            body['BuyInfo'] = request.buy_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrderPayUrlForOutDiscount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderPayUrlForOutDiscountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order_pay_url_for_out_discount(
        self,
        request: linkedmall_20180116_models.CreateOrderPayUrlForOutDiscountRequest,
    ) -> linkedmall_20180116_models.CreateOrderPayUrlForOutDiscountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_order_pay_url_for_out_discount_with_options(request, runtime)

    async def create_order_pay_url_for_out_discount_async(
        self,
        request: linkedmall_20180116_models.CreateOrderPayUrlForOutDiscountRequest,
    ) -> linkedmall_20180116_models.CreateOrderPayUrlForOutDiscountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_pay_url_for_out_discount_with_options_async(request, runtime)

    def create_order_transaction_detail_file_with_options(
        self,
        request: linkedmall_20180116_models.CreateOrderTransactionDetailFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderTransactionDetailFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.channel_name):
            body['ChannelName'] = request.channel_name
        if not UtilClient.is_unset(request.create_end_time):
            body['CreateEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            body['CreateStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_shop_id):
            body['LmShopId'] = request.lm_shop_id
        if not UtilClient.is_unset(request.order_status):
            body['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.pay_status):
            body['PayStatus'] = request.pay_status
        if not UtilClient.is_unset(request.payment_end_time):
            body['PaymentEndTime'] = request.payment_end_time
        if not UtilClient.is_unset(request.payment_start_time):
            body['PaymentStartTime'] = request.payment_start_time
        if not UtilClient.is_unset(request.po_code):
            body['PoCode'] = request.po_code
        if not UtilClient.is_unset(request.refund_end_time):
            body['RefundEndTime'] = request.refund_end_time
        if not UtilClient.is_unset(request.refund_start_time):
            body['RefundStartTime'] = request.refund_start_time
        if not UtilClient.is_unset(request.seller_id):
            body['SellerId'] = request.seller_id
        if not UtilClient.is_unset(request.seller_name):
            body['SellerName'] = request.seller_name
        if not UtilClient.is_unset(request.settlement_node):
            body['SettlementNode'] = request.settlement_node
        if not UtilClient.is_unset(request.shop_name):
            body['ShopName'] = request.shop_name
        if not UtilClient.is_unset(request.tb_main_order_id):
            body['TbMainOrderId'] = request.tb_main_order_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrderTransactionDetailFile',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderTransactionDetailFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_transaction_detail_file_with_options_async(
        self,
        request: linkedmall_20180116_models.CreateOrderTransactionDetailFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderTransactionDetailFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.channel_name):
            body['ChannelName'] = request.channel_name
        if not UtilClient.is_unset(request.create_end_time):
            body['CreateEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            body['CreateStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_shop_id):
            body['LmShopId'] = request.lm_shop_id
        if not UtilClient.is_unset(request.order_status):
            body['OrderStatus'] = request.order_status
        if not UtilClient.is_unset(request.pay_status):
            body['PayStatus'] = request.pay_status
        if not UtilClient.is_unset(request.payment_end_time):
            body['PaymentEndTime'] = request.payment_end_time
        if not UtilClient.is_unset(request.payment_start_time):
            body['PaymentStartTime'] = request.payment_start_time
        if not UtilClient.is_unset(request.po_code):
            body['PoCode'] = request.po_code
        if not UtilClient.is_unset(request.refund_end_time):
            body['RefundEndTime'] = request.refund_end_time
        if not UtilClient.is_unset(request.refund_start_time):
            body['RefundStartTime'] = request.refund_start_time
        if not UtilClient.is_unset(request.seller_id):
            body['SellerId'] = request.seller_id
        if not UtilClient.is_unset(request.seller_name):
            body['SellerName'] = request.seller_name
        if not UtilClient.is_unset(request.settlement_node):
            body['SettlementNode'] = request.settlement_node
        if not UtilClient.is_unset(request.shop_name):
            body['ShopName'] = request.shop_name
        if not UtilClient.is_unset(request.tb_main_order_id):
            body['TbMainOrderId'] = request.tb_main_order_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrderTransactionDetailFile',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderTransactionDetailFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order_transaction_detail_file(
        self,
        request: linkedmall_20180116_models.CreateOrderTransactionDetailFileRequest,
    ) -> linkedmall_20180116_models.CreateOrderTransactionDetailFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_order_transaction_detail_file_with_options(request, runtime)

    async def create_order_transaction_detail_file_async(
        self,
        request: linkedmall_20180116_models.CreateOrderTransactionDetailFileRequest,
    ) -> linkedmall_20180116_models.CreateOrderTransactionDetailFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_transaction_detail_file_with_options_async(request, runtime)

    def create_order_v2with_options(
        self,
        request: linkedmall_20180116_models.CreateOrderV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.buyer_message_map):
            query['BuyerMessageMap'] = request.buyer_message_map
        if not UtilClient.is_unset(request.delivery_address):
            query['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.order_expire_time):
            query['OrderExpireTime'] = request.order_expire_time
        if not UtilClient.is_unset(request.out_trade_id):
            query['OutTradeId'] = request.out_trade_id
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.total_amount):
            query['TotalAmount'] = request.total_amount
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrderV2',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_order_v2with_options_async(
        self,
        request: linkedmall_20180116_models.CreateOrderV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.buyer_message_map):
            query['BuyerMessageMap'] = request.buyer_message_map
        if not UtilClient.is_unset(request.delivery_address):
            query['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.order_expire_time):
            query['OrderExpireTime'] = request.order_expire_time
        if not UtilClient.is_unset(request.out_trade_id):
            query['OutTradeId'] = request.out_trade_id
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.total_amount):
            query['TotalAmount'] = request.total_amount
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOrderV2',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order_v2(
        self,
        request: linkedmall_20180116_models.CreateOrderV2Request,
    ) -> linkedmall_20180116_models.CreateOrderV2Response:
        runtime = util_models.RuntimeOptions()
        return self.create_order_v2with_options(request, runtime)

    async def create_order_v2_async(
        self,
        request: linkedmall_20180116_models.CreateOrderV2Request,
    ) -> linkedmall_20180116_models.CreateOrderV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_v2with_options_async(request, runtime)

    def create_order_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.CreateOrderWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.buyer_messages):
            body['BuyerMessages'] = request.buyer_messages
        if not UtilClient.is_unset(request.delivery_address):
            body['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.delivery_info):
            body['DeliveryInfo'] = request.delivery_info
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.order_expire_time):
            body['OrderExpireTime'] = request.order_expire_time
        if not UtilClient.is_unset(request.order_items):
            body['OrderItems'] = request.order_items
        if not UtilClient.is_unset(request.out_trade_id):
            body['OutTradeId'] = request.out_trade_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrderWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_order_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.CreateOrderWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOrderWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.buyer_messages):
            body['BuyerMessages'] = request.buyer_messages
        if not UtilClient.is_unset(request.delivery_address):
            body['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.delivery_info):
            body['DeliveryInfo'] = request.delivery_info
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.order_expire_time):
            body['OrderExpireTime'] = request.order_expire_time
        if not UtilClient.is_unset(request.order_items):
            body['OrderItems'] = request.order_items
        if not UtilClient.is_unset(request.out_trade_id):
            body['OutTradeId'] = request.out_trade_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrderWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOrderWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_order_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.CreateOrderWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.CreateOrderWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_order_with_designated_tb_uid_with_options(request, runtime)

    async def create_order_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.CreateOrderWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.CreateOrderWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_with_designated_tb_uid_with_options_async(request, runtime)

    def create_out_discount_order_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.CreateOutDiscountOrderWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOutDiscountOrderWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.buyer_messages):
            body['BuyerMessages'] = request.buyer_messages
        if not UtilClient.is_unset(request.delivery_address):
            body['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.delivery_info):
            body['DeliveryInfo'] = request.delivery_info
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.order_expire_time):
            body['OrderExpireTime'] = request.order_expire_time
        if not UtilClient.is_unset(request.order_items):
            body['OrderItems'] = request.order_items
        if not UtilClient.is_unset(request.out_discount_infos):
            body['OutDiscountInfos'] = request.out_discount_infos
        if not UtilClient.is_unset(request.out_trade_id):
            body['OutTradeId'] = request.out_trade_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOutDiscountOrderWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOutDiscountOrderWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_out_discount_order_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.CreateOutDiscountOrderWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateOutDiscountOrderWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.buyer_messages):
            body['BuyerMessages'] = request.buyer_messages
        if not UtilClient.is_unset(request.delivery_address):
            body['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.delivery_info):
            body['DeliveryInfo'] = request.delivery_info
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.order_expire_time):
            body['OrderExpireTime'] = request.order_expire_time
        if not UtilClient.is_unset(request.order_items):
            body['OrderItems'] = request.order_items
        if not UtilClient.is_unset(request.out_discount_infos):
            body['OutDiscountInfos'] = request.out_discount_infos
        if not UtilClient.is_unset(request.out_trade_id):
            body['OutTradeId'] = request.out_trade_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOutDiscountOrderWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateOutDiscountOrderWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_out_discount_order_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.CreateOutDiscountOrderWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.CreateOutDiscountOrderWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_out_discount_order_with_designated_tb_uid_with_options(request, runtime)

    async def create_out_discount_order_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.CreateOutDiscountOrderWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.CreateOutDiscountOrderWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_out_discount_order_with_designated_tb_uid_with_options_async(request, runtime)

    def create_pay_url_with_options(
        self,
        request: linkedmall_20180116_models.CreatePayUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreatePayUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.buy_info):
            body['BuyInfo'] = request.buy_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePayUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreatePayUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pay_url_with_options_async(
        self,
        request: linkedmall_20180116_models.CreatePayUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreatePayUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.buy_info):
            body['BuyInfo'] = request.buy_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePayUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreatePayUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pay_url(
        self,
        request: linkedmall_20180116_models.CreatePayUrlRequest,
    ) -> linkedmall_20180116_models.CreatePayUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_pay_url_with_options(request, runtime)

    async def create_pay_url_async(
        self,
        request: linkedmall_20180116_models.CreatePayUrlRequest,
    ) -> linkedmall_20180116_models.CreatePayUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_pay_url_with_options_async(request, runtime)

    def create_settle_confirm_with_options(
        self,
        request: linkedmall_20180116_models.CreateSettleConfirmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateSettleConfirmResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.out_request_no):
            body['OutRequestNo'] = request.out_request_no
        if not UtilClient.is_unset(request.out_trade_no):
            body['OutTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.settle_info):
            body['SettleInfo'] = request.settle_info
        if not UtilClient.is_unset(request.trade_no):
            body['TradeNo'] = request.trade_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSettleConfirm',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateSettleConfirmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_settle_confirm_with_options_async(
        self,
        request: linkedmall_20180116_models.CreateSettleConfirmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateSettleConfirmResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.out_request_no):
            body['OutRequestNo'] = request.out_request_no
        if not UtilClient.is_unset(request.out_trade_no):
            body['OutTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.settle_info):
            body['SettleInfo'] = request.settle_info
        if not UtilClient.is_unset(request.trade_no):
            body['TradeNo'] = request.trade_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSettleConfirm',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateSettleConfirmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_settle_confirm(
        self,
        request: linkedmall_20180116_models.CreateSettleConfirmRequest,
    ) -> linkedmall_20180116_models.CreateSettleConfirmResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_settle_confirm_with_options(request, runtime)

    async def create_settle_confirm_async(
        self,
        request: linkedmall_20180116_models.CreateSettleConfirmRequest,
    ) -> linkedmall_20180116_models.CreateSettleConfirmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_settle_confirm_with_options_async(request, runtime)

    def create_virtual_product_order_with_options(
        self,
        request: linkedmall_20180116_models.CreateVirtualProductOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateVirtualProductOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.delivery_address):
            query['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.order_expire_time):
            query['OrderExpireTime'] = request.order_expire_time
        if not UtilClient.is_unset(request.out_trade_id):
            query['OutTradeId'] = request.out_trade_id
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.total_amount):
            query['TotalAmount'] = request.total_amount
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVirtualProductOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateVirtualProductOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_virtual_product_order_with_options_async(
        self,
        request: linkedmall_20180116_models.CreateVirtualProductOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateVirtualProductOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.delivery_address):
            query['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.order_expire_time):
            query['OrderExpireTime'] = request.order_expire_time
        if not UtilClient.is_unset(request.out_trade_id):
            query['OutTradeId'] = request.out_trade_id
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.total_amount):
            query['TotalAmount'] = request.total_amount
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVirtualProductOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateVirtualProductOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_virtual_product_order(
        self,
        request: linkedmall_20180116_models.CreateVirtualProductOrderRequest,
    ) -> linkedmall_20180116_models.CreateVirtualProductOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_product_order_with_options(request, runtime)

    async def create_virtual_product_order_async(
        self,
        request: linkedmall_20180116_models.CreateVirtualProductOrderRequest,
    ) -> linkedmall_20180116_models.CreateVirtualProductOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_virtual_product_order_with_options_async(request, runtime)

    def create_withhold_trade_with_options(
        self,
        request: linkedmall_20180116_models.CreateWithholdTradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateWithholdTradeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agreement_no):
            body['AgreementNo'] = request.agreement_no
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.buyer_id):
            body['BuyerId'] = request.buyer_id
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.goods_detail):
            body['GoodsDetail'] = request.goods_detail
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.out_request_no):
            body['OutRequestNo'] = request.out_request_no
        if not UtilClient.is_unset(request.out_trade_no):
            body['OutTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.settle_mode):
            body['SettleMode'] = request.settle_mode
        if not UtilClient.is_unset(request.subject):
            body['Subject'] = request.subject
        if not UtilClient.is_unset(request.total_amount):
            body['TotalAmount'] = request.total_amount
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWithholdTrade',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateWithholdTradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_withhold_trade_with_options_async(
        self,
        request: linkedmall_20180116_models.CreateWithholdTradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.CreateWithholdTradeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agreement_no):
            body['AgreementNo'] = request.agreement_no
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.buyer_id):
            body['BuyerId'] = request.buyer_id
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.goods_detail):
            body['GoodsDetail'] = request.goods_detail
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.out_request_no):
            body['OutRequestNo'] = request.out_request_no
        if not UtilClient.is_unset(request.out_trade_no):
            body['OutTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.settle_mode):
            body['SettleMode'] = request.settle_mode
        if not UtilClient.is_unset(request.subject):
            body['Subject'] = request.subject
        if not UtilClient.is_unset(request.total_amount):
            body['TotalAmount'] = request.total_amount
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWithholdTrade',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.CreateWithholdTradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_withhold_trade(
        self,
        request: linkedmall_20180116_models.CreateWithholdTradeRequest,
    ) -> linkedmall_20180116_models.CreateWithholdTradeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_withhold_trade_with_options(request, runtime)

    async def create_withhold_trade_async(
        self,
        request: linkedmall_20180116_models.CreateWithholdTradeRequest,
    ) -> linkedmall_20180116_models.CreateWithholdTradeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_withhold_trade_with_options_async(request, runtime)

    def deduct_user_point_with_options(
        self,
        tmp_req: linkedmall_20180116_models.DeductUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DeductUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.DeductUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeductUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DeductUserPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def deduct_user_point_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.DeductUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DeductUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.DeductUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeductUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DeductUserPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deduct_user_point(
        self,
        request: linkedmall_20180116_models.DeductUserPointRequest,
    ) -> linkedmall_20180116_models.DeductUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.deduct_user_point_with_options(request, runtime)

    async def deduct_user_point_async(
        self,
        request: linkedmall_20180116_models.DeductUserPointRequest,
    ) -> linkedmall_20180116_models.DeductUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deduct_user_point_with_options_async(request, runtime)

    def delete_biz_items_with_options(
        self,
        request: linkedmall_20180116_models.DeleteBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DeleteBizItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_id_list):
            query['ItemIdList'] = request.item_id_list
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBizItems',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DeleteBizItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_biz_items_with_options_async(
        self,
        request: linkedmall_20180116_models.DeleteBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DeleteBizItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_id_list):
            query['ItemIdList'] = request.item_id_list
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBizItems',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DeleteBizItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_biz_items(
        self,
        request: linkedmall_20180116_models.DeleteBizItemsRequest,
    ) -> linkedmall_20180116_models.DeleteBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_biz_items_with_options(request, runtime)

    async def delete_biz_items_async(
        self,
        request: linkedmall_20180116_models.DeleteBizItemsRequest,
    ) -> linkedmall_20180116_models.DeleteBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_biz_items_with_options_async(request, runtime)

    def delete_item_limit_rule_with_options(
        self,
        request: linkedmall_20180116_models.DeleteItemLimitRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DeleteItemLimitRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_activity_id):
            query['LmActivityId'] = request.lm_activity_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.sub_biz_code):
            query['SubBizCode'] = request.sub_biz_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteItemLimitRule',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DeleteItemLimitRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_item_limit_rule_with_options_async(
        self,
        request: linkedmall_20180116_models.DeleteItemLimitRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DeleteItemLimitRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_activity_id):
            query['LmActivityId'] = request.lm_activity_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.sub_biz_code):
            query['SubBizCode'] = request.sub_biz_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteItemLimitRule',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DeleteItemLimitRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_item_limit_rule(
        self,
        request: linkedmall_20180116_models.DeleteItemLimitRuleRequest,
    ) -> linkedmall_20180116_models.DeleteItemLimitRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_item_limit_rule_with_options(request, runtime)

    async def delete_item_limit_rule_async(
        self,
        request: linkedmall_20180116_models.DeleteItemLimitRuleRequest,
    ) -> linkedmall_20180116_models.DeleteItemLimitRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_item_limit_rule_with_options_async(request, runtime)

    def download_cps_bill_file_with_options(
        self,
        request: linkedmall_20180116_models.DownloadCpsBillFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DownloadCpsBillFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_id):
            body['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadCpsBillFile',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DownloadCpsBillFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_cps_bill_file_with_options_async(
        self,
        request: linkedmall_20180116_models.DownloadCpsBillFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DownloadCpsBillFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_id):
            body['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadCpsBillFile',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DownloadCpsBillFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_cps_bill_file(
        self,
        request: linkedmall_20180116_models.DownloadCpsBillFileRequest,
    ) -> linkedmall_20180116_models.DownloadCpsBillFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_cps_bill_file_with_options(request, runtime)

    async def download_cps_bill_file_async(
        self,
        request: linkedmall_20180116_models.DownloadCpsBillFileRequest,
    ) -> linkedmall_20180116_models.DownloadCpsBillFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_cps_bill_file_with_options_async(request, runtime)

    def download_item_bill_file_with_options(
        self,
        request: linkedmall_20180116_models.DownloadItemBillFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DownloadItemBillFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_id):
            body['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadItemBillFile',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DownloadItemBillFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_item_bill_file_with_options_async(
        self,
        request: linkedmall_20180116_models.DownloadItemBillFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DownloadItemBillFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_id):
            body['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadItemBillFile',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DownloadItemBillFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_item_bill_file(
        self,
        request: linkedmall_20180116_models.DownloadItemBillFileRequest,
    ) -> linkedmall_20180116_models.DownloadItemBillFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_item_bill_file_with_options(request, runtime)

    async def download_item_bill_file_async(
        self,
        request: linkedmall_20180116_models.DownloadItemBillFileRequest,
    ) -> linkedmall_20180116_models.DownloadItemBillFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_item_bill_file_with_options_async(request, runtime)

    def download_order_transaction_detail_file_with_options(
        self,
        request: linkedmall_20180116_models.DownloadOrderTransactionDetailFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DownloadOrderTransactionDetailFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.record_id):
            body['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadOrderTransactionDetailFile',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DownloadOrderTransactionDetailFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_order_transaction_detail_file_with_options_async(
        self,
        request: linkedmall_20180116_models.DownloadOrderTransactionDetailFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.DownloadOrderTransactionDetailFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.record_id):
            body['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadOrderTransactionDetailFile',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.DownloadOrderTransactionDetailFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_order_transaction_detail_file(
        self,
        request: linkedmall_20180116_models.DownloadOrderTransactionDetailFileRequest,
    ) -> linkedmall_20180116_models.DownloadOrderTransactionDetailFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_order_transaction_detail_file_with_options(request, runtime)

    async def download_order_transaction_detail_file_async(
        self,
        request: linkedmall_20180116_models.DownloadOrderTransactionDetailFileRequest,
    ) -> linkedmall_20180116_models.DownloadOrderTransactionDetailFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_order_transaction_detail_file_with_options_async(request, runtime)

    def enable_order_with_options(
        self,
        request: linkedmall_20180116_models.EnableOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.EnableOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.out_trade_id):
            query['OutTradeId'] = request.out_trade_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.EnableOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_order_with_options_async(
        self,
        request: linkedmall_20180116_models.EnableOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.EnableOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.out_trade_id):
            query['OutTradeId'] = request.out_trade_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.EnableOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_order(
        self,
        request: linkedmall_20180116_models.EnableOrderRequest,
    ) -> linkedmall_20180116_models.EnableOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_order_with_options(request, runtime)

    async def enable_order_async(
        self,
        request: linkedmall_20180116_models.EnableOrderRequest,
    ) -> linkedmall_20180116_models.EnableOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_order_with_options_async(request, runtime)

    def enable_order_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.EnableOrderWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.EnableOrderWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_order_id):
            body['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableOrderWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.EnableOrderWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_order_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.EnableOrderWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.EnableOrderWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_order_id):
            body['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableOrderWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.EnableOrderWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_order_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.EnableOrderWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.EnableOrderWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_order_with_designated_tb_uid_with_options(request, runtime)

    async def enable_order_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.EnableOrderWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.EnableOrderWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_order_with_designated_tb_uid_with_options_async(request, runtime)

    def execute_node_with_options(
        self,
        request: linkedmall_20180116_models.ExecuteNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ExecuteNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_instance_id):
            query['NodeInstanceId'] = request.node_instance_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.process_instance_id):
            query['ProcessInstanceId'] = request.process_instance_id
        if not UtilClient.is_unset(request.request_data):
            query['RequestData'] = request.request_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteNode',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ExecuteNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_node_with_options_async(
        self,
        request: linkedmall_20180116_models.ExecuteNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ExecuteNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.node_instance_id):
            query['NodeInstanceId'] = request.node_instance_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.process_instance_id):
            query['ProcessInstanceId'] = request.process_instance_id
        if not UtilClient.is_unset(request.request_data):
            query['RequestData'] = request.request_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteNode',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ExecuteNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_node(
        self,
        request: linkedmall_20180116_models.ExecuteNodeRequest,
    ) -> linkedmall_20180116_models.ExecuteNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_node_with_options(request, runtime)

    async def execute_node_async(
        self,
        request: linkedmall_20180116_models.ExecuteNodeRequest,
    ) -> linkedmall_20180116_models.ExecuteNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_node_with_options_async(request, runtime)

    def freeze_user_point_with_options(
        self,
        tmp_req: linkedmall_20180116_models.FreezeUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.FreezeUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.FreezeUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FreezeUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.FreezeUserPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def freeze_user_point_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.FreezeUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.FreezeUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.FreezeUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FreezeUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.FreezeUserPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def freeze_user_point(
        self,
        request: linkedmall_20180116_models.FreezeUserPointRequest,
    ) -> linkedmall_20180116_models.FreezeUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.freeze_user_point_with_options(request, runtime)

    async def freeze_user_point_async(
        self,
        request: linkedmall_20180116_models.FreezeUserPointRequest,
    ) -> linkedmall_20180116_models.FreezeUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.freeze_user_point_with_options_async(request, runtime)

    def get_activity_game_info_with_options(
        self,
        tmp_req: linkedmall_20180116_models.GetActivityGameInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetActivityGameInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.GetActivityGameInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.game_id):
            query['GameId'] = request.game_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetActivityGameInfo',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetActivityGameInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_activity_game_info_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.GetActivityGameInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetActivityGameInfoResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.GetActivityGameInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.game_id):
            query['GameId'] = request.game_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetActivityGameInfo',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetActivityGameInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_activity_game_info(
        self,
        request: linkedmall_20180116_models.GetActivityGameInfoRequest,
    ) -> linkedmall_20180116_models.GetActivityGameInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_activity_game_info_with_options(request, runtime)

    async def get_activity_game_info_async(
        self,
        request: linkedmall_20180116_models.GetActivityGameInfoRequest,
    ) -> linkedmall_20180116_models.GetActivityGameInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_activity_game_info_with_options_async(request, runtime)

    def get_category_chain_with_options(
        self,
        request: linkedmall_20180116_models.GetCategoryChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetCategoryChainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCategoryChain',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCategoryChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_category_chain_with_options_async(
        self,
        request: linkedmall_20180116_models.GetCategoryChainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetCategoryChainResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCategoryChain',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCategoryChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_category_chain(
        self,
        request: linkedmall_20180116_models.GetCategoryChainRequest,
    ) -> linkedmall_20180116_models.GetCategoryChainResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_category_chain_with_options(request, runtime)

    async def get_category_chain_async(
        self,
        request: linkedmall_20180116_models.GetCategoryChainRequest,
    ) -> linkedmall_20180116_models.GetCategoryChainResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_category_chain_with_options_async(request, runtime)

    def get_category_list_with_options(
        self,
        request: linkedmall_20180116_models.GetCategoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetCategoryListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCategoryList',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCategoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_category_list_with_options_async(
        self,
        request: linkedmall_20180116_models.GetCategoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetCategoryListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCategoryList',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCategoryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_category_list(
        self,
        request: linkedmall_20180116_models.GetCategoryListRequest,
    ) -> linkedmall_20180116_models.GetCategoryListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_category_list_with_options(request, runtime)

    async def get_category_list_async(
        self,
        request: linkedmall_20180116_models.GetCategoryListRequest,
    ) -> linkedmall_20180116_models.GetCategoryListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_category_list_with_options_async(request, runtime)

    def get_custom_service_url_with_options(
        self,
        request: linkedmall_20180116_models.GetCustomServiceUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetCustomServiceUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.cuid):
            query['Cuid'] = request.cuid
        if not UtilClient.is_unset(request.nick):
            query['Nick'] = request.nick
        if not UtilClient.is_unset(request.seller_id):
            query['SellerId'] = request.seller_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomServiceUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCustomServiceUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_service_url_with_options_async(
        self,
        request: linkedmall_20180116_models.GetCustomServiceUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetCustomServiceUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.cuid):
            query['Cuid'] = request.cuid
        if not UtilClient.is_unset(request.nick):
            query['Nick'] = request.nick
        if not UtilClient.is_unset(request.seller_id):
            query['SellerId'] = request.seller_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomServiceUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetCustomServiceUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_service_url(
        self,
        request: linkedmall_20180116_models.GetCustomServiceUrlRequest,
    ) -> linkedmall_20180116_models.GetCustomServiceUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_custom_service_url_with_options(request, runtime)

    async def get_custom_service_url_async(
        self,
        request: linkedmall_20180116_models.GetCustomServiceUrlRequest,
    ) -> linkedmall_20180116_models.GetCustomServiceUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_custom_service_url_with_options_async(request, runtime)

    def get_guide_page_with_options(
        self,
        request: linkedmall_20180116_models.GetGuidePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetGuidePageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGuidePage',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetGuidePageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_guide_page_with_options_async(
        self,
        request: linkedmall_20180116_models.GetGuidePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetGuidePageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGuidePage',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetGuidePageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_guide_page(
        self,
        request: linkedmall_20180116_models.GetGuidePageRequest,
    ) -> linkedmall_20180116_models.GetGuidePageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_guide_page_with_options(request, runtime)

    async def get_guide_page_async(
        self,
        request: linkedmall_20180116_models.GetGuidePageRequest,
    ) -> linkedmall_20180116_models.GetGuidePageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_guide_page_with_options_async(request, runtime)

    def get_item_promotion_with_options(
        self,
        request: linkedmall_20180116_models.GetItemPromotionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetItemPromotionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetItemPromotion',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetItemPromotionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_item_promotion_with_options_async(
        self,
        request: linkedmall_20180116_models.GetItemPromotionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetItemPromotionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetItemPromotion',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetItemPromotionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_item_promotion(
        self,
        request: linkedmall_20180116_models.GetItemPromotionRequest,
    ) -> linkedmall_20180116_models.GetItemPromotionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_item_promotion_with_options(request, runtime)

    async def get_item_promotion_async(
        self,
        request: linkedmall_20180116_models.GetItemPromotionRequest,
    ) -> linkedmall_20180116_models.GetItemPromotionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_item_promotion_with_options_async(request, runtime)

    def get_login_page_with_options(
        self,
        request: linkedmall_20180116_models.GetLoginPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetLoginPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.fail_url):
            body['FailUrl'] = request.fail_url
        if not UtilClient.is_unset(request.target_url):
            body['TargetUrl'] = request.target_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLoginPage',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetLoginPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_page_with_options_async(
        self,
        request: linkedmall_20180116_models.GetLoginPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetLoginPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.fail_url):
            body['FailUrl'] = request.fail_url
        if not UtilClient.is_unset(request.target_url):
            body['TargetUrl'] = request.target_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLoginPage',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetLoginPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_page(
        self,
        request: linkedmall_20180116_models.GetLoginPageRequest,
    ) -> linkedmall_20180116_models.GetLoginPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_login_page_with_options(request, runtime)

    async def get_login_page_async(
        self,
        request: linkedmall_20180116_models.GetLoginPageRequest,
    ) -> linkedmall_20180116_models.GetLoginPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_login_page_with_options_async(request, runtime)

    def get_switch_url_with_options(
        self,
        request: linkedmall_20180116_models.GetSwitchUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetSwitchUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwitchUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetSwitchUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_switch_url_with_options_async(
        self,
        request: linkedmall_20180116_models.GetSwitchUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetSwitchUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSwitchUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetSwitchUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_switch_url(
        self,
        request: linkedmall_20180116_models.GetSwitchUrlRequest,
    ) -> linkedmall_20180116_models.GetSwitchUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_switch_url_with_options(request, runtime)

    async def get_switch_url_async(
        self,
        request: linkedmall_20180116_models.GetSwitchUrlRequest,
    ) -> linkedmall_20180116_models.GetSwitchUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_switch_url_with_options_async(request, runtime)

    def get_user_info_with_options(
        self,
        request: linkedmall_20180116_models.GetUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetUserInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.user_flag):
            query['UserFlag'] = request.user_flag
        body = {}
        if not UtilClient.is_unset(request.query_json):
            body['QueryJson'] = request.query_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_info_with_options_async(
        self,
        request: linkedmall_20180116_models.GetUserInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetUserInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.user_flag):
            query['UserFlag'] = request.user_flag
        body = {}
        if not UtilClient.is_unset(request.query_json):
            body['QueryJson'] = request.query_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserInfo',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_info(
        self,
        request: linkedmall_20180116_models.GetUserInfoRequest,
    ) -> linkedmall_20180116_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_info_with_options(request, runtime)

    async def get_user_info_async(
        self,
        request: linkedmall_20180116_models.GetUserInfoRequest,
    ) -> linkedmall_20180116_models.GetUserInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_info_with_options_async(request, runtime)

    def get_user_token_page_with_options(
        self,
        request: linkedmall_20180116_models.GetUserTokenPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetUserTokenPageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserTokenPage',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetUserTokenPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_token_page_with_options_async(
        self,
        request: linkedmall_20180116_models.GetUserTokenPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetUserTokenPageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserTokenPage',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetUserTokenPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_token_page(
        self,
        request: linkedmall_20180116_models.GetUserTokenPageRequest,
    ) -> linkedmall_20180116_models.GetUserTokenPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_token_page_with_options(request, runtime)

    async def get_user_token_page_async(
        self,
        request: linkedmall_20180116_models.GetUserTokenPageRequest,
    ) -> linkedmall_20180116_models.GetUserTokenPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_token_page_with_options_async(request, runtime)

    def get_withhold_sign_page_url_with_options(
        self,
        request: linkedmall_20180116_models.GetWithholdSignPageUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetWithholdSignPageUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.external_agreement_no):
            body['ExternalAgreementNo'] = request.external_agreement_no
        if not UtilClient.is_unset(request.identity_parameters):
            body['IdentityParameters'] = request.identity_parameters
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.merchant_service_description):
            body['MerchantServiceDescription'] = request.merchant_service_description
        if not UtilClient.is_unset(request.merchant_service_name):
            body['MerchantServiceName'] = request.merchant_service_name
        if not UtilClient.is_unset(request.notify_url):
            body['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.out_request_no):
            body['OutRequestNo'] = request.out_request_no
        if not UtilClient.is_unset(request.return_url):
            body['ReturnUrl'] = request.return_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWithholdSignPageUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetWithholdSignPageUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_withhold_sign_page_url_with_options_async(
        self,
        request: linkedmall_20180116_models.GetWithholdSignPageUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GetWithholdSignPageUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.external_agreement_no):
            body['ExternalAgreementNo'] = request.external_agreement_no
        if not UtilClient.is_unset(request.identity_parameters):
            body['IdentityParameters'] = request.identity_parameters
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.merchant_service_description):
            body['MerchantServiceDescription'] = request.merchant_service_description
        if not UtilClient.is_unset(request.merchant_service_name):
            body['MerchantServiceName'] = request.merchant_service_name
        if not UtilClient.is_unset(request.notify_url):
            body['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.out_request_no):
            body['OutRequestNo'] = request.out_request_no
        if not UtilClient.is_unset(request.return_url):
            body['ReturnUrl'] = request.return_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWithholdSignPageUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GetWithholdSignPageUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_withhold_sign_page_url(
        self,
        request: linkedmall_20180116_models.GetWithholdSignPageUrlRequest,
    ) -> linkedmall_20180116_models.GetWithholdSignPageUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_withhold_sign_page_url_with_options(request, runtime)

    async def get_withhold_sign_page_url_async(
        self,
        request: linkedmall_20180116_models.GetWithholdSignPageUrlRequest,
    ) -> linkedmall_20180116_models.GetWithholdSignPageUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_withhold_sign_page_url_with_options_async(request, runtime)

    def give_user_point_with_options(
        self,
        tmp_req: linkedmall_20180116_models.GiveUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GiveUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.GiveUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.target_biz_uid):
            query['TargetBizUid'] = request.target_biz_uid
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GiveUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GiveUserPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def give_user_point_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.GiveUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GiveUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.GiveUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.target_biz_uid):
            query['TargetBizUid'] = request.target_biz_uid
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GiveUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GiveUserPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def give_user_point(
        self,
        request: linkedmall_20180116_models.GiveUserPointRequest,
    ) -> linkedmall_20180116_models.GiveUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.give_user_point_with_options(request, runtime)

    async def give_user_point_async(
        self,
        request: linkedmall_20180116_models.GiveUserPointRequest,
    ) -> linkedmall_20180116_models.GiveUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.give_user_point_with_options_async(request, runtime)

    def grant_promotion_to_user_with_options(
        self,
        tmp_req: linkedmall_20180116_models.GrantPromotionToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GrantPromotionToUserResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.GrantPromotionToUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.expire_seconds):
            query['ExpireSeconds'] = request.expire_seconds
        if not UtilClient.is_unset(request.grant_mode):
            query['GrantMode'] = request.grant_mode
        if not UtilClient.is_unset(request.grant_way):
            query['GrantWay'] = request.grant_way
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.security_code):
            query['SecurityCode'] = request.security_code
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        body = {}
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantPromotionToUser',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GrantPromotionToUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_promotion_to_user_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.GrantPromotionToUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GrantPromotionToUserResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.GrantPromotionToUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.expire_seconds):
            query['ExpireSeconds'] = request.expire_seconds
        if not UtilClient.is_unset(request.grant_mode):
            query['GrantMode'] = request.grant_mode
        if not UtilClient.is_unset(request.grant_way):
            query['GrantWay'] = request.grant_way
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.promotion_id):
            query['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.security_code):
            query['SecurityCode'] = request.security_code
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        body = {}
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantPromotionToUser',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GrantPromotionToUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_promotion_to_user(
        self,
        request: linkedmall_20180116_models.GrantPromotionToUserRequest,
    ) -> linkedmall_20180116_models.GrantPromotionToUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_promotion_to_user_with_options(request, runtime)

    async def grant_promotion_to_user_async(
        self,
        request: linkedmall_20180116_models.GrantPromotionToUserRequest,
    ) -> linkedmall_20180116_models.GrantPromotionToUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_promotion_to_user_with_options_async(request, runtime)

    def grant_user_point_with_options(
        self,
        tmp_req: linkedmall_20180116_models.GrantUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GrantUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.GrantUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GrantUserPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_user_point_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.GrantUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.GrantUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.GrantUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.GrantUserPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_user_point(
        self,
        request: linkedmall_20180116_models.GrantUserPointRequest,
    ) -> linkedmall_20180116_models.GrantUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_user_point_with_options(request, runtime)

    async def grant_user_point_async(
        self,
        request: linkedmall_20180116_models.GrantUserPointRequest,
    ) -> linkedmall_20180116_models.GrantUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_user_point_with_options_async(request, runtime)

    def init_apply_refund_with_options(
        self,
        request: linkedmall_20180116_models.InitApplyRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.InitApplyRefundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_claim_type):
            query['BizClaimType'] = request.biz_claim_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.goods_status):
            query['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitApplyRefund',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.InitApplyRefundResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_apply_refund_with_options_async(
        self,
        request: linkedmall_20180116_models.InitApplyRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.InitApplyRefundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_claim_type):
            query['BizClaimType'] = request.biz_claim_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.goods_status):
            query['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitApplyRefund',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.InitApplyRefundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_apply_refund(
        self,
        request: linkedmall_20180116_models.InitApplyRefundRequest,
    ) -> linkedmall_20180116_models.InitApplyRefundResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_apply_refund_with_options(request, runtime)

    async def init_apply_refund_async(
        self,
        request: linkedmall_20180116_models.InitApplyRefundRequest,
    ) -> linkedmall_20180116_models.InitApplyRefundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_apply_refund_with_options_async(request, runtime)

    def init_apply_refund_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.InitApplyRefundWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.InitApplyRefundWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.refund_code):
            body['RefundCode'] = request.refund_code
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitApplyRefundWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.InitApplyRefundWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_apply_refund_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.InitApplyRefundWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.InitApplyRefundWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.refund_code):
            body['RefundCode'] = request.refund_code
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitApplyRefundWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.InitApplyRefundWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_apply_refund_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.InitApplyRefundWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.InitApplyRefundWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_apply_refund_with_designated_tb_uid_with_options(request, runtime)

    async def init_apply_refund_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.InitApplyRefundWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.InitApplyRefundWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_apply_refund_with_designated_tb_uid_with_options_async(request, runtime)

    def init_modify_refund_with_options(
        self,
        request: linkedmall_20180116_models.InitModifyRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.InitModifyRefundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_claim_type):
            query['BizClaimType'] = request.biz_claim_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.dispute_id):
            query['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.goods_status):
            query['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitModifyRefund',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.InitModifyRefundResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_modify_refund_with_options_async(
        self,
        request: linkedmall_20180116_models.InitModifyRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.InitModifyRefundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_claim_type):
            query['BizClaimType'] = request.biz_claim_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.dispute_id):
            query['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.goods_status):
            query['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitModifyRefund',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.InitModifyRefundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_modify_refund(
        self,
        request: linkedmall_20180116_models.InitModifyRefundRequest,
    ) -> linkedmall_20180116_models.InitModifyRefundResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_modify_refund_with_options(request, runtime)

    async def init_modify_refund_async(
        self,
        request: linkedmall_20180116_models.InitModifyRefundRequest,
    ) -> linkedmall_20180116_models.InitModifyRefundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_modify_refund_with_options_async(request, runtime)

    def init_modify_refund_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.InitModifyRefundWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.InitModifyRefundWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.refund_code):
            body['RefundCode'] = request.refund_code
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitModifyRefundWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.InitModifyRefundWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_modify_refund_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.InitModifyRefundWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.InitModifyRefundWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.refund_code):
            body['RefundCode'] = request.refund_code
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InitModifyRefundWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.InitModifyRefundWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_modify_refund_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.InitModifyRefundWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.InitModifyRefundWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_modify_refund_with_designated_tb_uid_with_options(request, runtime)

    async def init_modify_refund_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.InitModifyRefundWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.InitModifyRefundWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_modify_refund_with_designated_tb_uid_with_options_async(request, runtime)

    def list_activity_atmosphere_with_options(
        self,
        request: linkedmall_20180116_models.ListActivityAtmosphereRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ListActivityAtmosphereResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActivityAtmosphere',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ListActivityAtmosphereResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_activity_atmosphere_with_options_async(
        self,
        request: linkedmall_20180116_models.ListActivityAtmosphereRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ListActivityAtmosphereResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActivityAtmosphere',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ListActivityAtmosphereResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_activity_atmosphere(
        self,
        request: linkedmall_20180116_models.ListActivityAtmosphereRequest,
    ) -> linkedmall_20180116_models.ListActivityAtmosphereResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_activity_atmosphere_with_options(request, runtime)

    async def list_activity_atmosphere_async(
        self,
        request: linkedmall_20180116_models.ListActivityAtmosphereRequest,
    ) -> linkedmall_20180116_models.ListActivityAtmosphereResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_activity_atmosphere_with_options_async(request, runtime)

    def list_activity_game_info_with_options(
        self,
        request: linkedmall_20180116_models.ListActivityGameInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ListActivityGameInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActivityGameInfo',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ListActivityGameInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_activity_game_info_with_options_async(
        self,
        request: linkedmall_20180116_models.ListActivityGameInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ListActivityGameInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActivityGameInfo',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ListActivityGameInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_activity_game_info(
        self,
        request: linkedmall_20180116_models.ListActivityGameInfoRequest,
    ) -> linkedmall_20180116_models.ListActivityGameInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_activity_game_info_with_options(request, runtime)

    async def list_activity_game_info_async(
        self,
        request: linkedmall_20180116_models.ListActivityGameInfoRequest,
    ) -> linkedmall_20180116_models.ListActivityGameInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_activity_game_info_with_options_async(request, runtime)

    def list_item_activities_with_options(
        self,
        tmp_req: linkedmall_20180116_models.ListItemActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ListItemActivitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.ListItemActivitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_ids_shrink):
            query['ItemIds'] = request.item_ids_shrink
        if not UtilClient.is_unset(request.lm_item_ids_shrink):
            query['LmItemIds'] = request.lm_item_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListItemActivities',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ListItemActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_item_activities_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.ListItemActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ListItemActivitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.ListItemActivitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_ids_shrink):
            query['ItemIds'] = request.item_ids_shrink
        if not UtilClient.is_unset(request.lm_item_ids_shrink):
            query['LmItemIds'] = request.lm_item_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListItemActivities',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ListItemActivitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_item_activities(
        self,
        request: linkedmall_20180116_models.ListItemActivitiesRequest,
    ) -> linkedmall_20180116_models.ListItemActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_item_activities_with_options(request, runtime)

    async def list_item_activities_async(
        self,
        request: linkedmall_20180116_models.ListItemActivitiesRequest,
    ) -> linkedmall_20180116_models.ListItemActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_item_activities_with_options_async(request, runtime)

    def list_user_game_process_with_options(
        self,
        request: linkedmall_20180116_models.ListUserGameProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ListUserGameProcessResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGameProcess',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ListUserGameProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_game_process_with_options_async(
        self,
        request: linkedmall_20180116_models.ListUserGameProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ListUserGameProcessResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGameProcess',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ListUserGameProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_game_process(
        self,
        request: linkedmall_20180116_models.ListUserGameProcessRequest,
    ) -> linkedmall_20180116_models.ListUserGameProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_game_process_with_options(request, runtime)

    async def list_user_game_process_async(
        self,
        request: linkedmall_20180116_models.ListUserGameProcessRequest,
    ) -> linkedmall_20180116_models.ListUserGameProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_game_process_with_options_async(request, runtime)

    def list_user_point_records_with_options(
        self,
        request: linkedmall_20180116_models.ListUserPointRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ListUserPointRecordsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserPointRecords',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ListUserPointRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_point_records_with_options_async(
        self,
        request: linkedmall_20180116_models.ListUserPointRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ListUserPointRecordsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserPointRecords',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ListUserPointRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_point_records(
        self,
        request: linkedmall_20180116_models.ListUserPointRecordsRequest,
    ) -> linkedmall_20180116_models.ListUserPointRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_point_records_with_options(request, runtime)

    async def list_user_point_records_async(
        self,
        request: linkedmall_20180116_models.ListUserPointRecordsRequest,
    ) -> linkedmall_20180116_models.ListUserPointRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_point_records_with_options_async(request, runtime)

    def modify_basic_and_biz_items_with_options(
        self,
        request: linkedmall_20180116_models.ModifyBasicAndBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyBasicAndBizItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        body = {}
        if not UtilClient.is_unset(request.item_list):
            body['ItemList'] = request.item_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyBasicAndBizItems',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyBasicAndBizItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_basic_and_biz_items_with_options_async(
        self,
        request: linkedmall_20180116_models.ModifyBasicAndBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyBasicAndBizItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        body = {}
        if not UtilClient.is_unset(request.item_list):
            body['ItemList'] = request.item_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyBasicAndBizItems',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyBasicAndBizItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_basic_and_biz_items(
        self,
        request: linkedmall_20180116_models.ModifyBasicAndBizItemsRequest,
    ) -> linkedmall_20180116_models.ModifyBasicAndBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_basic_and_biz_items_with_options(request, runtime)

    async def modify_basic_and_biz_items_async(
        self,
        request: linkedmall_20180116_models.ModifyBasicAndBizItemsRequest,
    ) -> linkedmall_20180116_models.ModifyBasicAndBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_basic_and_biz_items_with_options_async(request, runtime)

    def modify_basic_item_supplier_price_with_options(
        self,
        request: linkedmall_20180116_models.ModifyBasicItemSupplierPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyBasicItemSupplierPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.lm_shop_id):
            query['LmShopId'] = request.lm_shop_id
        if not UtilClient.is_unset(request.sku_id):
            query['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.supplier_price):
            query['SupplierPrice'] = request.supplier_price
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBasicItemSupplierPrice',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyBasicItemSupplierPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_basic_item_supplier_price_with_options_async(
        self,
        request: linkedmall_20180116_models.ModifyBasicItemSupplierPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyBasicItemSupplierPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.lm_shop_id):
            query['LmShopId'] = request.lm_shop_id
        if not UtilClient.is_unset(request.sku_id):
            query['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.supplier_price):
            query['SupplierPrice'] = request.supplier_price
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBasicItemSupplierPrice',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyBasicItemSupplierPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_basic_item_supplier_price(
        self,
        request: linkedmall_20180116_models.ModifyBasicItemSupplierPriceRequest,
    ) -> linkedmall_20180116_models.ModifyBasicItemSupplierPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_basic_item_supplier_price_with_options(request, runtime)

    async def modify_basic_item_supplier_price_async(
        self,
        request: linkedmall_20180116_models.ModifyBasicItemSupplierPriceRequest,
    ) -> linkedmall_20180116_models.ModifyBasicItemSupplierPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_basic_item_supplier_price_with_options_async(request, runtime)

    def modify_biz_items_with_options(
        self,
        request: linkedmall_20180116_models.ModifyBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyBizItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        body = {}
        if not UtilClient.is_unset(request.item_list):
            body['ItemList'] = request.item_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyBizItems',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyBizItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_biz_items_with_options_async(
        self,
        request: linkedmall_20180116_models.ModifyBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyBizItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        body = {}
        if not UtilClient.is_unset(request.item_list):
            body['ItemList'] = request.item_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyBizItems',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyBizItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_biz_items(
        self,
        request: linkedmall_20180116_models.ModifyBizItemsRequest,
    ) -> linkedmall_20180116_models.ModifyBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_biz_items_with_options(request, runtime)

    async def modify_biz_items_async(
        self,
        request: linkedmall_20180116_models.ModifyBizItemsRequest,
    ) -> linkedmall_20180116_models.ModifyBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_biz_items_with_options_async(request, runtime)

    def modify_item_limit_rule_with_options(
        self,
        request: linkedmall_20180116_models.ModifyItemLimitRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyItemLimitRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_activity_id):
            query['LmActivityId'] = request.lm_activity_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.sub_biz_code):
            query['SubBizCode'] = request.sub_biz_code
        if not UtilClient.is_unset(request.upper_num):
            query['UpperNum'] = request.upper_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyItemLimitRule',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyItemLimitRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_item_limit_rule_with_options_async(
        self,
        request: linkedmall_20180116_models.ModifyItemLimitRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyItemLimitRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_activity_id):
            query['LmActivityId'] = request.lm_activity_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_type):
            query['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.sub_biz_code):
            query['SubBizCode'] = request.sub_biz_code
        if not UtilClient.is_unset(request.upper_num):
            query['UpperNum'] = request.upper_num
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyItemLimitRule',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyItemLimitRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_item_limit_rule(
        self,
        request: linkedmall_20180116_models.ModifyItemLimitRuleRequest,
    ) -> linkedmall_20180116_models.ModifyItemLimitRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_item_limit_rule_with_options(request, runtime)

    async def modify_item_limit_rule_async(
        self,
        request: linkedmall_20180116_models.ModifyItemLimitRuleRequest,
    ) -> linkedmall_20180116_models.ModifyItemLimitRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_item_limit_rule_with_options_async(request, runtime)

    def modify_order_delivery_address_with_options(
        self,
        request: linkedmall_20180116_models.ModifyOrderDeliveryAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyOrderDeliveryAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.delivery_address):
            query['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOrderDeliveryAddress',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyOrderDeliveryAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_order_delivery_address_with_options_async(
        self,
        request: linkedmall_20180116_models.ModifyOrderDeliveryAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyOrderDeliveryAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.delivery_address):
            query['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyOrderDeliveryAddress',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyOrderDeliveryAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_order_delivery_address(
        self,
        request: linkedmall_20180116_models.ModifyOrderDeliveryAddressRequest,
    ) -> linkedmall_20180116_models.ModifyOrderDeliveryAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_order_delivery_address_with_options(request, runtime)

    async def modify_order_delivery_address_async(
        self,
        request: linkedmall_20180116_models.ModifyOrderDeliveryAddressRequest,
    ) -> linkedmall_20180116_models.ModifyOrderDeliveryAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_order_delivery_address_with_options_async(request, runtime)

    def modify_refund_with_options(
        self,
        request: linkedmall_20180116_models.ModifyRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyRefundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.apply_reason_text_id):
            query['ApplyReasonTextId'] = request.apply_reason_text_id
        if not UtilClient.is_unset(request.apply_refund_count):
            query['ApplyRefundCount'] = request.apply_refund_count
        if not UtilClient.is_unset(request.apply_refund_fee):
            query['ApplyRefundFee'] = request.apply_refund_fee
        if not UtilClient.is_unset(request.biz_claim_type):
            query['BizClaimType'] = request.biz_claim_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.dispute_id):
            query['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.goods_status):
            query['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.leave_message):
            body['LeaveMessage'] = request.leave_message
        if not UtilClient.is_unset(request.leave_picture_list):
            body['LeavePictureList'] = request.leave_picture_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyRefund',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyRefundResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_refund_with_options_async(
        self,
        request: linkedmall_20180116_models.ModifyRefundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyRefundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.apply_reason_text_id):
            query['ApplyReasonTextId'] = request.apply_reason_text_id
        if not UtilClient.is_unset(request.apply_refund_count):
            query['ApplyRefundCount'] = request.apply_refund_count
        if not UtilClient.is_unset(request.apply_refund_fee):
            query['ApplyRefundFee'] = request.apply_refund_fee
        if not UtilClient.is_unset(request.biz_claim_type):
            query['BizClaimType'] = request.biz_claim_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.dispute_id):
            query['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.goods_status):
            query['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.leave_message):
            body['LeaveMessage'] = request.leave_message
        if not UtilClient.is_unset(request.leave_picture_list):
            body['LeavePictureList'] = request.leave_picture_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyRefund',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyRefundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_refund(
        self,
        request: linkedmall_20180116_models.ModifyRefundRequest,
    ) -> linkedmall_20180116_models.ModifyRefundResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_refund_with_options(request, runtime)

    async def modify_refund_async(
        self,
        request: linkedmall_20180116_models.ModifyRefundRequest,
    ) -> linkedmall_20180116_models.ModifyRefundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_refund_with_options_async(request, runtime)

    def modify_refund_with_designated_tb_uid_with_options(
        self,
        tmp_req: linkedmall_20180116_models.ModifyRefundWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyRefundWithDesignatedTbUidResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.ModifyRefundWithDesignatedTbUidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.proofs):
            request.proofs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.proofs, 'Proofs', 'json')
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.goods_status):
            body['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.proofs_shrink):
            body['Proofs'] = request.proofs_shrink
        if not UtilClient.is_unset(request.reason_id):
            body['ReasonId'] = request.reason_id
        if not UtilClient.is_unset(request.refund_code):
            body['RefundCode'] = request.refund_code
        if not UtilClient.is_unset(request.refund_count):
            body['RefundCount'] = request.refund_count
        if not UtilClient.is_unset(request.refund_fee):
            body['RefundFee'] = request.refund_fee
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyRefundWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyRefundWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_refund_with_designated_tb_uid_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.ModifyRefundWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifyRefundWithDesignatedTbUidResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.ModifyRefundWithDesignatedTbUidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.proofs):
            request.proofs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.proofs, 'Proofs', 'json')
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.goods_status):
            body['GoodsStatus'] = request.goods_status
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.proofs_shrink):
            body['Proofs'] = request.proofs_shrink
        if not UtilClient.is_unset(request.reason_id):
            body['ReasonId'] = request.reason_id
        if not UtilClient.is_unset(request.refund_code):
            body['RefundCode'] = request.refund_code
        if not UtilClient.is_unset(request.refund_count):
            body['RefundCount'] = request.refund_count
        if not UtilClient.is_unset(request.refund_fee):
            body['RefundFee'] = request.refund_fee
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyRefundWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifyRefundWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_refund_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.ModifyRefundWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.ModifyRefundWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_refund_with_designated_tb_uid_with_options(request, runtime)

    async def modify_refund_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.ModifyRefundWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.ModifyRefundWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_refund_with_designated_tb_uid_with_options_async(request, runtime)

    def modify_settle_account_with_options(
        self,
        request: linkedmall_20180116_models.ModifySettleAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifySettleAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_channel):
            body['AccountChannel'] = request.account_channel
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_no):
            body['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.account_pay_type):
            body['AccountPayType'] = request.account_pay_type
        if not UtilClient.is_unset(request.account_type):
            body['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.country_or_area_code):
            body['CountryOrAreaCode'] = request.country_or_area_code
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.idempotent_id):
            body['IdempotentId'] = request.idempotent_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySettleAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifySettleAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_settle_account_with_options_async(
        self,
        request: linkedmall_20180116_models.ModifySettleAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifySettleAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_channel):
            body['AccountChannel'] = request.account_channel
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_no):
            body['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.account_pay_type):
            body['AccountPayType'] = request.account_pay_type
        if not UtilClient.is_unset(request.account_type):
            body['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.country_or_area_code):
            body['CountryOrAreaCode'] = request.country_or_area_code
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.idempotent_id):
            body['IdempotentId'] = request.idempotent_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySettleAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifySettleAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_settle_account(
        self,
        request: linkedmall_20180116_models.ModifySettleAccountRequest,
    ) -> linkedmall_20180116_models.ModifySettleAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_settle_account_with_options(request, runtime)

    async def modify_settle_account_async(
        self,
        request: linkedmall_20180116_models.ModifySettleAccountRequest,
    ) -> linkedmall_20180116_models.ModifySettleAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_settle_account_with_options_async(request, runtime)

    def modify_supplier_price_and_price_cent_with_options(
        self,
        request: linkedmall_20180116_models.ModifySupplierPriceAndPriceCentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifySupplierPriceAndPriceCentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.lm_shop_id):
            query['LmShopId'] = request.lm_shop_id
        if not UtilClient.is_unset(request.price_cent):
            query['PriceCent'] = request.price_cent
        if not UtilClient.is_unset(request.sku_id):
            query['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.supplier_price):
            query['SupplierPrice'] = request.supplier_price
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySupplierPriceAndPriceCent',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifySupplierPriceAndPriceCentResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_supplier_price_and_price_cent_with_options_async(
        self,
        request: linkedmall_20180116_models.ModifySupplierPriceAndPriceCentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ModifySupplierPriceAndPriceCentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.lm_shop_id):
            query['LmShopId'] = request.lm_shop_id
        if not UtilClient.is_unset(request.price_cent):
            query['PriceCent'] = request.price_cent
        if not UtilClient.is_unset(request.sku_id):
            query['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.supplier_price):
            query['SupplierPrice'] = request.supplier_price
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySupplierPriceAndPriceCent',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ModifySupplierPriceAndPriceCentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_supplier_price_and_price_cent(
        self,
        request: linkedmall_20180116_models.ModifySupplierPriceAndPriceCentRequest,
    ) -> linkedmall_20180116_models.ModifySupplierPriceAndPriceCentResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_supplier_price_and_price_cent_with_options(request, runtime)

    async def modify_supplier_price_and_price_cent_async(
        self,
        request: linkedmall_20180116_models.ModifySupplierPriceAndPriceCentRequest,
    ) -> linkedmall_20180116_models.ModifySupplierPriceAndPriceCentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_supplier_price_and_price_cent_with_options_async(request, runtime)

    def notify_pay_order_status_with_options(
        self,
        request: linkedmall_20180116_models.NotifyPayOrderStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.NotifyPayOrderStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.operation_date):
            query['OperationDate'] = request.operation_date
        if not UtilClient.is_unset(request.pay_types):
            query['PayTypes'] = request.pay_types
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NotifyPayOrderStatus',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.NotifyPayOrderStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def notify_pay_order_status_with_options_async(
        self,
        request: linkedmall_20180116_models.NotifyPayOrderStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.NotifyPayOrderStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.operation_date):
            query['OperationDate'] = request.operation_date
        if not UtilClient.is_unset(request.pay_types):
            query['PayTypes'] = request.pay_types
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NotifyPayOrderStatus',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.NotifyPayOrderStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def notify_pay_order_status(
        self,
        request: linkedmall_20180116_models.NotifyPayOrderStatusRequest,
    ) -> linkedmall_20180116_models.NotifyPayOrderStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.notify_pay_order_status_with_options(request, runtime)

    async def notify_pay_order_status_async(
        self,
        request: linkedmall_20180116_models.NotifyPayOrderStatusRequest,
    ) -> linkedmall_20180116_models.NotifyPayOrderStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.notify_pay_order_status_with_options_async(request, runtime)

    def notify_withhold_fund_with_options(
        self,
        request: linkedmall_20180116_models.NotifyWithholdFundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.NotifyWithholdFundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.operation_date):
            query['OperationDate'] = request.operation_date
        if not UtilClient.is_unset(request.pay_types):
            query['PayTypes'] = request.pay_types
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.tenant_order_id):
            query['TenantOrderId'] = request.tenant_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NotifyWithholdFund',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.NotifyWithholdFundResponse(),
            self.call_api(params, req, runtime)
        )

    async def notify_withhold_fund_with_options_async(
        self,
        request: linkedmall_20180116_models.NotifyWithholdFundRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.NotifyWithholdFundResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.operation_date):
            query['OperationDate'] = request.operation_date
        if not UtilClient.is_unset(request.pay_types):
            query['PayTypes'] = request.pay_types
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.tenant_order_id):
            query['TenantOrderId'] = request.tenant_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NotifyWithholdFund',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.NotifyWithholdFundResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def notify_withhold_fund(
        self,
        request: linkedmall_20180116_models.NotifyWithholdFundRequest,
    ) -> linkedmall_20180116_models.NotifyWithholdFundResponse:
        runtime = util_models.RuntimeOptions()
        return self.notify_withhold_fund_with_options(request, runtime)

    async def notify_withhold_fund_async(
        self,
        request: linkedmall_20180116_models.NotifyWithholdFundRequest,
    ) -> linkedmall_20180116_models.NotifyWithholdFundResponse:
        runtime = util_models.RuntimeOptions()
        return await self.notify_withhold_fund_with_options_async(request, runtime)

    def open_real_tb_account_support_with_options(
        self,
        request: linkedmall_20180116_models.OpenRealTbAccountSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.OpenRealTbAccountSupportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenRealTbAccountSupport',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.OpenRealTbAccountSupportResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_real_tb_account_support_with_options_async(
        self,
        request: linkedmall_20180116_models.OpenRealTbAccountSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.OpenRealTbAccountSupportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenRealTbAccountSupport',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.OpenRealTbAccountSupportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_real_tb_account_support(
        self,
        request: linkedmall_20180116_models.OpenRealTbAccountSupportRequest,
    ) -> linkedmall_20180116_models.OpenRealTbAccountSupportResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_real_tb_account_support_with_options(request, runtime)

    async def open_real_tb_account_support_async(
        self,
        request: linkedmall_20180116_models.OpenRealTbAccountSupportRequest,
    ) -> linkedmall_20180116_models.OpenRealTbAccountSupportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_real_tb_account_support_with_options_async(request, runtime)

    def push_user_game_process_with_options(
        self,
        tmp_req: linkedmall_20180116_models.PushUserGameProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.PushUserGameProcessResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.PushUserGameProcessShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.current_step_id):
            query['CurrentStepId'] = request.current_step_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushUserGameProcess',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.PushUserGameProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_user_game_process_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.PushUserGameProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.PushUserGameProcessResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.PushUserGameProcessShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        if not UtilClient.is_unset(tmp_req.body):
            request.body_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body, 'body', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.current_step_id):
            query['CurrentStepId'] = request.current_step_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        if not UtilClient.is_unset(request.body_shrink):
            body['body'] = request.body_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushUserGameProcess',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.PushUserGameProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_user_game_process(
        self,
        request: linkedmall_20180116_models.PushUserGameProcessRequest,
    ) -> linkedmall_20180116_models.PushUserGameProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.push_user_game_process_with_options(request, runtime)

    async def push_user_game_process_async(
        self,
        request: linkedmall_20180116_models.PushUserGameProcessRequest,
    ) -> linkedmall_20180116_models.PushUserGameProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.push_user_game_process_with_options_async(request, runtime)

    def query_activity_items_with_options(
        self,
        request: linkedmall_20180116_models.QueryActivityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryActivityItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_activity_id):
            query['LmActivityId'] = request.lm_activity_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryActivityItems',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryActivityItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_activity_items_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryActivityItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryActivityItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_activity_id):
            query['LmActivityId'] = request.lm_activity_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryActivityItems',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryActivityItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_activity_items(
        self,
        request: linkedmall_20180116_models.QueryActivityItemsRequest,
    ) -> linkedmall_20180116_models.QueryActivityItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_activity_items_with_options(request, runtime)

    async def query_activity_items_async(
        self,
        request: linkedmall_20180116_models.QueryActivityItemsRequest,
    ) -> linkedmall_20180116_models.QueryActivityItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_activity_items_with_options_async(request, runtime)

    def query_address_with_options(
        self,
        request: linkedmall_20180116_models.QueryAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.division_code):
            query['DivisionCode'] = request.division_code
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAddress',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_address_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.division_code):
            query['DivisionCode'] = request.division_code
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAddress',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_address(
        self,
        request: linkedmall_20180116_models.QueryAddressRequest,
    ) -> linkedmall_20180116_models.QueryAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_address_with_options(request, runtime)

    async def query_address_async(
        self,
        request: linkedmall_20180116_models.QueryAddressRequest,
    ) -> linkedmall_20180116_models.QueryAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_address_with_options_async(request, runtime)

    def query_address_detail_with_options(
        self,
        request: linkedmall_20180116_models.QueryAddressDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAddressDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_info):
            query['AddressInfo'] = request.address_info
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAddressDetail',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_address_detail_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryAddressDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAddressDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_info):
            query['AddressInfo'] = request.address_info
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAddressDetail',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_address_detail(
        self,
        request: linkedmall_20180116_models.QueryAddressDetailRequest,
    ) -> linkedmall_20180116_models.QueryAddressDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_address_detail_with_options(request, runtime)

    async def query_address_detail_async(
        self,
        request: linkedmall_20180116_models.QueryAddressDetailRequest,
    ) -> linkedmall_20180116_models.QueryAddressDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_address_detail_with_options_async(request, runtime)

    def query_address_list_with_options(
        self,
        request: linkedmall_20180116_models.QueryAddressListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAddressListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAddressList',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_address_list_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryAddressListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAddressListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAddressList',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAddressListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_address_list(
        self,
        request: linkedmall_20180116_models.QueryAddressListRequest,
    ) -> linkedmall_20180116_models.QueryAddressListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_address_list_with_options(request, runtime)

    async def query_address_list_async(
        self,
        request: linkedmall_20180116_models.QueryAddressListRequest,
    ) -> linkedmall_20180116_models.QueryAddressListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_address_list_with_options_async(request, runtime)

    def query_advertisement_settle_info_with_options(
        self,
        request: linkedmall_20180116_models.QueryAdvertisementSettleInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAdvertisementSettleInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.media_settle_detail_id):
            query['MediaSettleDetailId'] = request.media_settle_detail_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.settle_no):
            query['SettleNo'] = request.settle_no
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAdvertisementSettleInfo',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAdvertisementSettleInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_advertisement_settle_info_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryAdvertisementSettleInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAdvertisementSettleInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.media_settle_detail_id):
            query['MediaSettleDetailId'] = request.media_settle_detail_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.settle_no):
            query['SettleNo'] = request.settle_no
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAdvertisementSettleInfo',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAdvertisementSettleInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_advertisement_settle_info(
        self,
        request: linkedmall_20180116_models.QueryAdvertisementSettleInfoRequest,
    ) -> linkedmall_20180116_models.QueryAdvertisementSettleInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_advertisement_settle_info_with_options(request, runtime)

    async def query_advertisement_settle_info_async(
        self,
        request: linkedmall_20180116_models.QueryAdvertisementSettleInfoRequest,
    ) -> linkedmall_20180116_models.QueryAdvertisementSettleInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_advertisement_settle_info_with_options_async(request, runtime)

    def query_agreement_with_options(
        self,
        request: linkedmall_20180116_models.QueryAgreementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAgreementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agreement_no):
            body['AgreementNo'] = request.agreement_no
        if not UtilClient.is_unset(request.external_agreement_no):
            body['ExternalAgreementNo'] = request.external_agreement_no
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAgreement',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAgreementResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_agreement_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryAgreementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAgreementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agreement_no):
            body['AgreementNo'] = request.agreement_no
        if not UtilClient.is_unset(request.external_agreement_no):
            body['ExternalAgreementNo'] = request.external_agreement_no
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryAgreement',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAgreementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_agreement(
        self,
        request: linkedmall_20180116_models.QueryAgreementRequest,
    ) -> linkedmall_20180116_models.QueryAgreementResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_agreement_with_options(request, runtime)

    async def query_agreement_async(
        self,
        request: linkedmall_20180116_models.QueryAgreementRequest,
    ) -> linkedmall_20180116_models.QueryAgreementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_agreement_with_options_async(request, runtime)

    def query_all_cinemas_with_options(
        self,
        request: linkedmall_20180116_models.QueryAllCinemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAllCinemasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.city_code):
            query['CityCode'] = request.city_code
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAllCinemas',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAllCinemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_all_cinemas_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryAllCinemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAllCinemasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.city_code):
            query['CityCode'] = request.city_code
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAllCinemas',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAllCinemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_all_cinemas(
        self,
        request: linkedmall_20180116_models.QueryAllCinemasRequest,
    ) -> linkedmall_20180116_models.QueryAllCinemasResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_all_cinemas_with_options(request, runtime)

    async def query_all_cinemas_async(
        self,
        request: linkedmall_20180116_models.QueryAllCinemasRequest,
    ) -> linkedmall_20180116_models.QueryAllCinemasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_all_cinemas_with_options_async(request, runtime)

    def query_all_cities_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryAllCitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAllCitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryAllCitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_json):
            request.ext_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_json, 'ExtJson', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_json_shrink):
            query['ExtJson'] = request.ext_json_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAllCities',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAllCitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_all_cities_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryAllCitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryAllCitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryAllCitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_json):
            request.ext_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_json, 'ExtJson', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_json_shrink):
            query['ExtJson'] = request.ext_json_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAllCities',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryAllCitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_all_cities(
        self,
        request: linkedmall_20180116_models.QueryAllCitiesRequest,
    ) -> linkedmall_20180116_models.QueryAllCitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_all_cities_with_options(request, runtime)

    async def query_all_cities_async(
        self,
        request: linkedmall_20180116_models.QueryAllCitiesRequest,
    ) -> linkedmall_20180116_models.QueryAllCitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_all_cities_with_options_async(request, runtime)

    def query_batch_regist_anonymous_tb_account_result_with_options(
        self,
        request: linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBatchRegistAnonymousTbAccountResult',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_batch_regist_anonymous_tb_account_result_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBatchRegistAnonymousTbAccountResult',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_batch_regist_anonymous_tb_account_result(
        self,
        request: linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultRequest,
    ) -> linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_batch_regist_anonymous_tb_account_result_with_options(request, runtime)

    async def query_batch_regist_anonymous_tb_account_result_async(
        self,
        request: linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultRequest,
    ) -> linkedmall_20180116_models.QueryBatchRegistAnonymousTbAccountResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_batch_regist_anonymous_tb_account_result_with_options_async(request, runtime)

    def query_best_session_4items_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryBestSession4ItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBestSession4ItemsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBestSession4ItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_ids_shrink):
            query['ItemIds'] = request.item_ids_shrink
        if not UtilClient.is_unset(request.lm_item_ids_shrink):
            query['LmItemIds'] = request.lm_item_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBestSession4Items',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBestSession4ItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_best_session_4items_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryBestSession4ItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBestSession4ItemsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBestSession4ItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_ids_shrink):
            query['ItemIds'] = request.item_ids_shrink
        if not UtilClient.is_unset(request.lm_item_ids_shrink):
            query['LmItemIds'] = request.lm_item_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBestSession4Items',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBestSession4ItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_best_session_4items(
        self,
        request: linkedmall_20180116_models.QueryBestSession4ItemsRequest,
    ) -> linkedmall_20180116_models.QueryBestSession4ItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_best_session_4items_with_options(request, runtime)

    async def query_best_session_4items_async(
        self,
        request: linkedmall_20180116_models.QueryBestSession4ItemsRequest,
    ) -> linkedmall_20180116_models.QueryBestSession4ItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_best_session_4items_with_options_async(request, runtime)

    def query_biz_item_list_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryBizItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemListResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.item_ids_shrink):
            query['ItemIds'] = request.item_ids_shrink
        if not UtilClient.is_unset(request.lm_item_ids_shrink):
            query['LmItemIds'] = request.lm_item_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBizItemList',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_biz_item_list_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryBizItemListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemListResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.item_ids_shrink):
            query['ItemIds'] = request.item_ids_shrink
        if not UtilClient.is_unset(request.lm_item_ids_shrink):
            query['LmItemIds'] = request.lm_item_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBizItemList',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_biz_item_list(
        self,
        request: linkedmall_20180116_models.QueryBizItemListRequest,
    ) -> linkedmall_20180116_models.QueryBizItemListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_biz_item_list_with_options(request, runtime)

    async def query_biz_item_list_async(
        self,
        request: linkedmall_20180116_models.QueryBizItemListRequest,
    ) -> linkedmall_20180116_models.QueryBizItemListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_biz_item_list_with_options_async(request, runtime)

    def query_biz_item_list_v2with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryBizItemListV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemListV2Response:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemListV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.item_ids_shrink):
            query['ItemIds'] = request.item_ids_shrink
        if not UtilClient.is_unset(request.lm_item_ids_shrink):
            query['LmItemIds'] = request.lm_item_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBizItemListV2',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemListV2Response(),
            self.call_api(params, req, runtime)
        )

    async def query_biz_item_list_v2with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryBizItemListV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemListV2Response:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemListV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.item_ids_shrink):
            query['ItemIds'] = request.item_ids_shrink
        if not UtilClient.is_unset(request.lm_item_ids_shrink):
            query['LmItemIds'] = request.lm_item_ids_shrink
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBizItemListV2',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemListV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def query_biz_item_list_v2(
        self,
        request: linkedmall_20180116_models.QueryBizItemListV2Request,
    ) -> linkedmall_20180116_models.QueryBizItemListV2Response:
        runtime = util_models.RuntimeOptions()
        return self.query_biz_item_list_v2with_options(request, runtime)

    async def query_biz_item_list_v2_async(
        self,
        request: linkedmall_20180116_models.QueryBizItemListV2Request,
    ) -> linkedmall_20180116_models.QueryBizItemListV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.query_biz_item_list_v2with_options_async(request, runtime)

    def query_biz_item_list_with_cache_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryBizItemListWithCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemListWithCacheResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemListWithCacheShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBizItemListWithCache',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemListWithCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_biz_item_list_with_cache_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryBizItemListWithCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemListWithCacheResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemListWithCacheShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBizItemListWithCache',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemListWithCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_biz_item_list_with_cache(
        self,
        request: linkedmall_20180116_models.QueryBizItemListWithCacheRequest,
    ) -> linkedmall_20180116_models.QueryBizItemListWithCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_biz_item_list_with_cache_with_options(request, runtime)

    async def query_biz_item_list_with_cache_async(
        self,
        request: linkedmall_20180116_models.QueryBizItemListWithCacheRequest,
    ) -> linkedmall_20180116_models.QueryBizItemListWithCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_biz_item_list_with_cache_with_options_async(request, runtime)

    def query_biz_items_with_options(
        self,
        request: linkedmall_20180116_models.QueryBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBizItems',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_biz_items_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryBizItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBizItems',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_biz_items(
        self,
        request: linkedmall_20180116_models.QueryBizItemsRequest,
    ) -> linkedmall_20180116_models.QueryBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_biz_items_with_options(request, runtime)

    async def query_biz_items_async(
        self,
        request: linkedmall_20180116_models.QueryBizItemsRequest,
    ) -> linkedmall_20180116_models.QueryBizItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_biz_items_with_options_async(request, runtime)

    def query_biz_items_with_activity_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryBizItemsWithActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemsWithActivityResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemsWithActivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBizItemsWithActivity',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemsWithActivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_biz_items_with_activity_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryBizItemsWithActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBizItemsWithActivityResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryBizItemsWithActivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBizItemsWithActivity',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBizItemsWithActivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_biz_items_with_activity(
        self,
        request: linkedmall_20180116_models.QueryBizItemsWithActivityRequest,
    ) -> linkedmall_20180116_models.QueryBizItemsWithActivityResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_biz_items_with_activity_with_options(request, runtime)

    async def query_biz_items_with_activity_async(
        self,
        request: linkedmall_20180116_models.QueryBizItemsWithActivityRequest,
    ) -> linkedmall_20180116_models.QueryBizItemsWithActivityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_biz_items_with_activity_with_options_async(request, runtime)

    def query_budget_ticket_item_list_by_biz_id_with_options(
        self,
        request: linkedmall_20180116_models.QueryBudgetTicketItemListByBizIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBudgetTicketItemListByBizIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.budget_ticket_no):
            query['BudgetTicketNo'] = request.budget_ticket_no
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBudgetTicketItemListByBizId',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBudgetTicketItemListByBizIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_budget_ticket_item_list_by_biz_id_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryBudgetTicketItemListByBizIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryBudgetTicketItemListByBizIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.budget_ticket_no):
            query['BudgetTicketNo'] = request.budget_ticket_no
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBudgetTicketItemListByBizId',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryBudgetTicketItemListByBizIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_budget_ticket_item_list_by_biz_id(
        self,
        request: linkedmall_20180116_models.QueryBudgetTicketItemListByBizIdRequest,
    ) -> linkedmall_20180116_models.QueryBudgetTicketItemListByBizIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_budget_ticket_item_list_by_biz_id_with_options(request, runtime)

    async def query_budget_ticket_item_list_by_biz_id_async(
        self,
        request: linkedmall_20180116_models.QueryBudgetTicketItemListByBizIdRequest,
    ) -> linkedmall_20180116_models.QueryBudgetTicketItemListByBizIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_budget_ticket_item_list_by_biz_id_with_options_async(request, runtime)

    def query_channel_item_bill_download_url_with_options(
        self,
        request: linkedmall_20180116_models.QueryChannelItemBillDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryChannelItemBillDownloadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_id):
            body['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.bill_period):
            body['BillPeriod'] = request.bill_period
        if not UtilClient.is_unset(request.bill_status):
            body['BillStatus'] = request.bill_status
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.lm_shop_id):
            body['LmShopId'] = request.lm_shop_id
        if not UtilClient.is_unset(request.lm_shop_name):
            body['LmShopName'] = request.lm_shop_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryChannelItemBillDownloadUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryChannelItemBillDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_channel_item_bill_download_url_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryChannelItemBillDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryChannelItemBillDownloadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_id):
            body['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.bill_period):
            body['BillPeriod'] = request.bill_period
        if not UtilClient.is_unset(request.bill_status):
            body['BillStatus'] = request.bill_status
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.lm_shop_id):
            body['LmShopId'] = request.lm_shop_id
        if not UtilClient.is_unset(request.lm_shop_name):
            body['LmShopName'] = request.lm_shop_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryChannelItemBillDownloadUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryChannelItemBillDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_channel_item_bill_download_url(
        self,
        request: linkedmall_20180116_models.QueryChannelItemBillDownloadUrlRequest,
    ) -> linkedmall_20180116_models.QueryChannelItemBillDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_channel_item_bill_download_url_with_options(request, runtime)

    async def query_channel_item_bill_download_url_async(
        self,
        request: linkedmall_20180116_models.QueryChannelItemBillDownloadUrlRequest,
    ) -> linkedmall_20180116_models.QueryChannelItemBillDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_channel_item_bill_download_url_with_options_async(request, runtime)

    def query_guide_item_group_with_options(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.item_state):
            query['ItemState'] = request.item_state
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGuideItemGroup',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryGuideItemGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_guide_item_group_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.item_state):
            query['ItemState'] = request.item_state
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGuideItemGroup',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryGuideItemGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_guide_item_group(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupRequest,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_guide_item_group_with_options(request, runtime)

    async def query_guide_item_group_async(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupRequest,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_guide_item_group_with_options_async(request, runtime)

    def query_guide_item_group_for_crowd_operation_with_options(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupForCrowdOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupForCrowdOperationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.item_state):
            query['ItemState'] = request.item_state
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_flag):
            query['UserFlag'] = request.user_flag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGuideItemGroupForCrowdOperation',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryGuideItemGroupForCrowdOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_guide_item_group_for_crowd_operation_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupForCrowdOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupForCrowdOperationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.item_state):
            query['ItemState'] = request.item_state
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_flag):
            query['UserFlag'] = request.user_flag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGuideItemGroupForCrowdOperation',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryGuideItemGroupForCrowdOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_guide_item_group_for_crowd_operation(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupForCrowdOperationRequest,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupForCrowdOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_guide_item_group_for_crowd_operation_with_options(request, runtime)

    async def query_guide_item_group_for_crowd_operation_async(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupForCrowdOperationRequest,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupForCrowdOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_guide_item_group_for_crowd_operation_with_options_async(request, runtime)

    def query_guide_item_group_with_out_inventory_with_options(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGuideItemGroupWithOutInventory',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_guide_item_group_with_out_inventory_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGuideItemGroupWithOutInventory',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_guide_item_group_with_out_inventory(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryRequest,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_guide_item_group_with_out_inventory_with_options(request, runtime)

    async def query_guide_item_group_with_out_inventory_async(
        self,
        request: linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryRequest,
    ) -> linkedmall_20180116_models.QueryGuideItemGroupWithOutInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_guide_item_group_with_out_inventory_with_options_async(request, runtime)

    def query_hot_movies_with_options(
        self,
        request: linkedmall_20180116_models.QueryHotMoviesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryHotMoviesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.city_code):
            query['CityCode'] = request.city_code
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryHotMovies',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryHotMoviesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_hot_movies_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryHotMoviesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryHotMoviesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.city_code):
            query['CityCode'] = request.city_code
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryHotMovies',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryHotMoviesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_hot_movies(
        self,
        request: linkedmall_20180116_models.QueryHotMoviesRequest,
    ) -> linkedmall_20180116_models.QueryHotMoviesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_hot_movies_with_options(request, runtime)

    async def query_hot_movies_async(
        self,
        request: linkedmall_20180116_models.QueryHotMoviesRequest,
    ) -> linkedmall_20180116_models.QueryHotMoviesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_hot_movies_with_options_async(request, runtime)

    def query_inventory_of_items_in_biz_item_group_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInventoryOfItemsInBizItemGroup',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_inventory_of_items_in_biz_item_group_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryInventoryOfItemsInBizItemGroup',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_inventory_of_items_in_biz_item_group(
        self,
        request: linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupRequest,
    ) -> linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_inventory_of_items_in_biz_item_group_with_options(request, runtime)

    async def query_inventory_of_items_in_biz_item_group_async(
        self,
        request: linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupRequest,
    ) -> linkedmall_20180116_models.QueryInventoryOfItemsInBizItemGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_inventory_of_items_in_biz_item_group_with_options_async(request, runtime)

    def query_item_detail_with_options(
        self,
        request: linkedmall_20180116_models.QueryItemDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemDetail',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_item_detail_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryItemDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemDetail',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_item_detail(
        self,
        request: linkedmall_20180116_models.QueryItemDetailRequest,
    ) -> linkedmall_20180116_models.QueryItemDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_item_detail_with_options(request, runtime)

    async def query_item_detail_async(
        self,
        request: linkedmall_20180116_models.QueryItemDetailRequest,
    ) -> linkedmall_20180116_models.QueryItemDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_item_detail_with_options_async(request, runtime)

    def query_item_detail_inner_with_options(
        self,
        request: linkedmall_20180116_models.QueryItemDetailInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemDetailInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.division_code):
            query['DivisionCode'] = request.division_code
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemDetailInner',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemDetailInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_item_detail_inner_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryItemDetailInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemDetailInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.division_code):
            query['DivisionCode'] = request.division_code
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemDetailInner',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemDetailInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_item_detail_inner(
        self,
        request: linkedmall_20180116_models.QueryItemDetailInnerRequest,
    ) -> linkedmall_20180116_models.QueryItemDetailInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_item_detail_inner_with_options(request, runtime)

    async def query_item_detail_inner_async(
        self,
        request: linkedmall_20180116_models.QueryItemDetailInnerRequest,
    ) -> linkedmall_20180116_models.QueryItemDetailInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_item_detail_inner_with_options_async(request, runtime)

    def query_item_detail_tea_with_options(
        self,
        request: linkedmall_20180116_models.QueryItemDetailTeaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemDetailTeaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemDetailTea',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemDetailTeaResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_item_detail_tea_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryItemDetailTeaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemDetailTeaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_id):
            query['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemDetailTea',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemDetailTeaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_item_detail_tea(
        self,
        request: linkedmall_20180116_models.QueryItemDetailTeaRequest,
    ) -> linkedmall_20180116_models.QueryItemDetailTeaResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_item_detail_tea_with_options(request, runtime)

    async def query_item_detail_tea_async(
        self,
        request: linkedmall_20180116_models.QueryItemDetailTeaRequest,
    ) -> linkedmall_20180116_models.QueryItemDetailTeaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_item_detail_tea_with_options_async(request, runtime)

    def query_item_in_sub_bizs_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryItemInSubBizsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemInSubBizsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryItemInSubBizsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_biz_ids):
            request.sub_biz_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_biz_ids, 'SubBizIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemInSubBizs',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemInSubBizsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_item_in_sub_bizs_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryItemInSubBizsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemInSubBizsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryItemInSubBizsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_biz_ids):
            request.sub_biz_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_biz_ids, 'SubBizIds', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemInSubBizs',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemInSubBizsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_item_in_sub_bizs(
        self,
        request: linkedmall_20180116_models.QueryItemInSubBizsRequest,
    ) -> linkedmall_20180116_models.QueryItemInSubBizsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_item_in_sub_bizs_with_options(request, runtime)

    async def query_item_in_sub_bizs_async(
        self,
        request: linkedmall_20180116_models.QueryItemInSubBizsRequest,
    ) -> linkedmall_20180116_models.QueryItemInSubBizsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_item_in_sub_bizs_with_options_async(request, runtime)

    def query_item_inventory_with_options(
        self,
        request: linkedmall_20180116_models.QueryItemInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemInventoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.division_code):
            query['DivisionCode'] = request.division_code
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemInventory',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_item_inventory_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryItemInventoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemInventoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.division_code):
            query['DivisionCode'] = request.division_code
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemInventory',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemInventoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_item_inventory(
        self,
        request: linkedmall_20180116_models.QueryItemInventoryRequest,
    ) -> linkedmall_20180116_models.QueryItemInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_item_inventory_with_options(request, runtime)

    async def query_item_inventory_async(
        self,
        request: linkedmall_20180116_models.QueryItemInventoryRequest,
    ) -> linkedmall_20180116_models.QueryItemInventoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_item_inventory_with_options_async(request, runtime)

    def query_item_inventory_v2with_options(
        self,
        request: linkedmall_20180116_models.QueryItemInventoryV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemInventoryV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.division_code):
            query['DivisionCode'] = request.division_code
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemInventoryV2',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemInventoryV2Response(),
            self.call_api(params, req, runtime)
        )

    async def query_item_inventory_v2with_options_async(
        self,
        request: linkedmall_20180116_models.QueryItemInventoryV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemInventoryV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.division_code):
            query['DivisionCode'] = request.division_code
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryItemInventoryV2',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemInventoryV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def query_item_inventory_v2(
        self,
        request: linkedmall_20180116_models.QueryItemInventoryV2Request,
    ) -> linkedmall_20180116_models.QueryItemInventoryV2Response:
        runtime = util_models.RuntimeOptions()
        return self.query_item_inventory_v2with_options(request, runtime)

    async def query_item_inventory_v2_async(
        self,
        request: linkedmall_20180116_models.QueryItemInventoryV2Request,
    ) -> linkedmall_20180116_models.QueryItemInventoryV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.query_item_inventory_v2with_options_async(request, runtime)

    def query_item_next_cycle_restriction_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryItemNextCycleRestrictionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemNextCycleRestrictionResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryItemNextCycleRestrictionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_id):
            request.lm_item_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_id, 'LmItemId', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        body = {}
        if not UtilClient.is_unset(request.lm_item_id_shrink):
            body['LmItemId'] = request.lm_item_id_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryItemNextCycleRestriction',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemNextCycleRestrictionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_item_next_cycle_restriction_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryItemNextCycleRestrictionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryItemNextCycleRestrictionResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryItemNextCycleRestrictionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lm_item_id):
            request.lm_item_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_id, 'LmItemId', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.sub_biz_id):
            query['SubBizId'] = request.sub_biz_id
        body = {}
        if not UtilClient.is_unset(request.lm_item_id_shrink):
            body['LmItemId'] = request.lm_item_id_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryItemNextCycleRestriction',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryItemNextCycleRestrictionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_item_next_cycle_restriction(
        self,
        request: linkedmall_20180116_models.QueryItemNextCycleRestrictionRequest,
    ) -> linkedmall_20180116_models.QueryItemNextCycleRestrictionResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_item_next_cycle_restriction_with_options(request, runtime)

    async def query_item_next_cycle_restriction_async(
        self,
        request: linkedmall_20180116_models.QueryItemNextCycleRestrictionRequest,
    ) -> linkedmall_20180116_models.QueryItemNextCycleRestrictionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_item_next_cycle_restriction_with_options_async(request, runtime)

    def query_logistics_with_options(
        self,
        request: linkedmall_20180116_models.QueryLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryLogisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLogistics',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryLogisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_logistics_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryLogisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLogistics',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryLogisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_logistics(
        self,
        request: linkedmall_20180116_models.QueryLogisticsRequest,
    ) -> linkedmall_20180116_models.QueryLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_logistics_with_options(request, runtime)

    async def query_logistics_async(
        self,
        request: linkedmall_20180116_models.QueryLogisticsRequest,
    ) -> linkedmall_20180116_models.QueryLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_logistics_with_options_async(request, runtime)

    def query_media_settle_info_with_options(
        self,
        request: linkedmall_20180116_models.QueryMediaSettleInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMediaSettleInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.media_name):
            query['MediaName'] = request.media_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.settle_no):
            query['SettleNo'] = request.settle_no
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaSettleInfo',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMediaSettleInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_settle_info_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryMediaSettleInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMediaSettleInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.media_name):
            query['MediaName'] = request.media_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.settle_no):
            query['SettleNo'] = request.settle_no
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaSettleInfo',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMediaSettleInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_settle_info(
        self,
        request: linkedmall_20180116_models.QueryMediaSettleInfoRequest,
    ) -> linkedmall_20180116_models.QueryMediaSettleInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_media_settle_info_with_options(request, runtime)

    async def query_media_settle_info_async(
        self,
        request: linkedmall_20180116_models.QueryMediaSettleInfoRequest,
    ) -> linkedmall_20180116_models.QueryMediaSettleInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_media_settle_info_with_options_async(request, runtime)

    def query_messages_with_options(
        self,
        request: linkedmall_20180116_models.QueryMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMessagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessages',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_messages_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMessagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessages',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_messages(
        self,
        request: linkedmall_20180116_models.QueryMessagesRequest,
    ) -> linkedmall_20180116_models.QueryMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_messages_with_options(request, runtime)

    async def query_messages_async(
        self,
        request: linkedmall_20180116_models.QueryMessagesRequest,
    ) -> linkedmall_20180116_models.QueryMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_messages_with_options_async(request, runtime)

    def query_movie_comments_with_options(
        self,
        request: linkedmall_20180116_models.QueryMovieCommentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieCommentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.movie_id):
            query['MovieId'] = request.movie_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMovieComments',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieCommentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_movie_comments_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryMovieCommentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieCommentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.movie_id):
            query['MovieId'] = request.movie_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMovieComments',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieCommentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_movie_comments(
        self,
        request: linkedmall_20180116_models.QueryMovieCommentsRequest,
    ) -> linkedmall_20180116_models.QueryMovieCommentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_movie_comments_with_options(request, runtime)

    async def query_movie_comments_async(
        self,
        request: linkedmall_20180116_models.QueryMovieCommentsRequest,
    ) -> linkedmall_20180116_models.QueryMovieCommentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_movie_comments_with_options_async(request, runtime)

    def query_movie_schedules_with_options(
        self,
        request: linkedmall_20180116_models.QueryMovieSchedulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieSchedulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.cinema_id):
            query['CinemaId'] = request.cinema_id
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMovieSchedules',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieSchedulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_movie_schedules_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryMovieSchedulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieSchedulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.cinema_id):
            query['CinemaId'] = request.cinema_id
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMovieSchedules',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieSchedulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_movie_schedules(
        self,
        request: linkedmall_20180116_models.QueryMovieSchedulesRequest,
    ) -> linkedmall_20180116_models.QueryMovieSchedulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_movie_schedules_with_options(request, runtime)

    async def query_movie_schedules_async(
        self,
        request: linkedmall_20180116_models.QueryMovieSchedulesRequest,
    ) -> linkedmall_20180116_models.QueryMovieSchedulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_movie_schedules_with_options_async(request, runtime)

    def query_movie_seats_with_options(
        self,
        request: linkedmall_20180116_models.QueryMovieSeatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieSeatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.schedule_id):
            query['ScheduleId'] = request.schedule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMovieSeats',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieSeatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_movie_seats_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryMovieSeatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieSeatsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.schedule_id):
            query['ScheduleId'] = request.schedule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMovieSeats',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieSeatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_movie_seats(
        self,
        request: linkedmall_20180116_models.QueryMovieSeatsRequest,
    ) -> linkedmall_20180116_models.QueryMovieSeatsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_movie_seats_with_options(request, runtime)

    async def query_movie_seats_async(
        self,
        request: linkedmall_20180116_models.QueryMovieSeatsRequest,
    ) -> linkedmall_20180116_models.QueryMovieSeatsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_movie_seats_with_options_async(request, runtime)

    def query_movie_tickets_with_options(
        self,
        request: linkedmall_20180116_models.QueryMovieTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieTicketsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMovieTickets',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieTicketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_movie_tickets_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryMovieTicketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryMovieTicketsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMovieTickets',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryMovieTicketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_movie_tickets(
        self,
        request: linkedmall_20180116_models.QueryMovieTicketsRequest,
    ) -> linkedmall_20180116_models.QueryMovieTicketsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_movie_tickets_with_options(request, runtime)

    async def query_movie_tickets_async(
        self,
        request: linkedmall_20180116_models.QueryMovieTicketsRequest,
    ) -> linkedmall_20180116_models.QueryMovieTicketsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_movie_tickets_with_options_async(request, runtime)

    def query_order_and_payment_list_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderAndPaymentListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderAndPaymentListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.filter_option):
            query['FilterOption'] = request.filter_option
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderAndPaymentList',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderAndPaymentListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_and_payment_list_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderAndPaymentListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderAndPaymentListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.filter_option):
            query['FilterOption'] = request.filter_option
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderAndPaymentList',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderAndPaymentListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_and_payment_list(
        self,
        request: linkedmall_20180116_models.QueryOrderAndPaymentListRequest,
    ) -> linkedmall_20180116_models.QueryOrderAndPaymentListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_and_payment_list_with_options(request, runtime)

    async def query_order_and_payment_list_async(
        self,
        request: linkedmall_20180116_models.QueryOrderAndPaymentListRequest,
    ) -> linkedmall_20180116_models.QueryOrderAndPaymentListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_and_payment_list_with_options_async(request, runtime)

    def query_order_and_payment_list_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderAndPaymentListWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderAndPaymentListWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.filter_option):
            body['FilterOption'] = request.filter_option
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrderAndPaymentListWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderAndPaymentListWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_and_payment_list_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderAndPaymentListWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderAndPaymentListWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.filter_option):
            body['FilterOption'] = request.filter_option
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrderAndPaymentListWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderAndPaymentListWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_and_payment_list_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.QueryOrderAndPaymentListWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.QueryOrderAndPaymentListWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_and_payment_list_with_designated_tb_uid_with_options(request, runtime)

    async def query_order_and_payment_list_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.QueryOrderAndPaymentListWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.QueryOrderAndPaymentListWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_and_payment_list_with_designated_tb_uid_with_options_async(request, runtime)

    def query_order_commission_rate_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderCommissionRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderCommissionRateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderCommissionRate',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderCommissionRateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_commission_rate_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderCommissionRateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderCommissionRateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderCommissionRate',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderCommissionRateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_commission_rate(
        self,
        request: linkedmall_20180116_models.QueryOrderCommissionRateRequest,
    ) -> linkedmall_20180116_models.QueryOrderCommissionRateResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_commission_rate_with_options(request, runtime)

    async def query_order_commission_rate_async(
        self,
        request: linkedmall_20180116_models.QueryOrderCommissionRateRequest,
    ) -> linkedmall_20180116_models.QueryOrderCommissionRateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_commission_rate_with_options_async(request, runtime)

    def query_order_detail_inner_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderDetailInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderDetailInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.filter_option):
            query['FilterOption'] = request.filter_option
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderDetailInner',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderDetailInnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_detail_inner_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderDetailInnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderDetailInnerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.filter_option):
            query['FilterOption'] = request.filter_option
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderDetailInner',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderDetailInnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_detail_inner(
        self,
        request: linkedmall_20180116_models.QueryOrderDetailInnerRequest,
    ) -> linkedmall_20180116_models.QueryOrderDetailInnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_detail_inner_with_options(request, runtime)

    async def query_order_detail_inner_async(
        self,
        request: linkedmall_20180116_models.QueryOrderDetailInnerRequest,
    ) -> linkedmall_20180116_models.QueryOrderDetailInnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_detail_inner_with_options_async(request, runtime)

    def query_order_id_by_pay_id_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderIdByPayIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderIdByPayIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.payment_id):
            query['PaymentId'] = request.payment_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderIdByPayId',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderIdByPayIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_id_by_pay_id_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderIdByPayIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderIdByPayIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.payment_id):
            query['PaymentId'] = request.payment_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderIdByPayId',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderIdByPayIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_id_by_pay_id(
        self,
        request: linkedmall_20180116_models.QueryOrderIdByPayIdRequest,
    ) -> linkedmall_20180116_models.QueryOrderIdByPayIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_id_by_pay_id_with_options(request, runtime)

    async def query_order_id_by_pay_id_async(
        self,
        request: linkedmall_20180116_models.QueryOrderIdByPayIdRequest,
    ) -> linkedmall_20180116_models.QueryOrderIdByPayIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_id_by_pay_id_with_options_async(request, runtime)

    def query_order_info_after_sale_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderInfoAfterSaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderInfoAfterSaleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderInfoAfterSale',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderInfoAfterSaleResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_info_after_sale_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderInfoAfterSaleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderInfoAfterSaleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderInfoAfterSale',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderInfoAfterSaleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_info_after_sale(
        self,
        request: linkedmall_20180116_models.QueryOrderInfoAfterSaleRequest,
    ) -> linkedmall_20180116_models.QueryOrderInfoAfterSaleResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_info_after_sale_with_options(request, runtime)

    async def query_order_info_after_sale_async(
        self,
        request: linkedmall_20180116_models.QueryOrderInfoAfterSaleRequest,
    ) -> linkedmall_20180116_models.QueryOrderInfoAfterSaleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_info_after_sale_with_options_async(request, runtime)

    def query_order_item_info_by_payment_id_for_ai_zhan_you_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.payment_id):
            query['PaymentId'] = request.payment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderItemInfoByPaymentIdForAiZhanYou',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_item_info_by_payment_id_for_ai_zhan_you_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.payment_id):
            query['PaymentId'] = request.payment_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderItemInfoByPaymentIdForAiZhanYou',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_item_info_by_payment_id_for_ai_zhan_you(
        self,
        request: linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouRequest,
    ) -> linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_item_info_by_payment_id_for_ai_zhan_you_with_options(request, runtime)

    async def query_order_item_info_by_payment_id_for_ai_zhan_you_async(
        self,
        request: linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouRequest,
    ) -> linkedmall_20180116_models.QueryOrderItemInfoByPaymentIdForAiZhanYouResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_item_info_by_payment_id_for_ai_zhan_you_with_options_async(request, runtime)

    def query_order_list_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.filter_option):
            query['FilterOption'] = request.filter_option
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderList',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_list_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.filter_option):
            query['FilterOption'] = request.filter_option
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderList',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_list(
        self,
        request: linkedmall_20180116_models.QueryOrderListRequest,
    ) -> linkedmall_20180116_models.QueryOrderListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_list_with_options(request, runtime)

    async def query_order_list_async(
        self,
        request: linkedmall_20180116_models.QueryOrderListRequest,
    ) -> linkedmall_20180116_models.QueryOrderListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_list_with_options_async(request, runtime)

    def query_order_list_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderListWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderListWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.filter_option):
            body['FilterOption'] = request.filter_option
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrderListWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderListWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_list_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderListWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderListWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.filter_option):
            body['FilterOption'] = request.filter_option
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrderListWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderListWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_list_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.QueryOrderListWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.QueryOrderListWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_list_with_designated_tb_uid_with_options(request, runtime)

    async def query_order_list_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.QueryOrderListWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.QueryOrderListWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_list_with_designated_tb_uid_with_options_async(request, runtime)

    def query_order_logistics_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderLogisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderLogistics',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderLogisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_logistics_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderLogisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrderLogistics',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderLogisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_logistics(
        self,
        request: linkedmall_20180116_models.QueryOrderLogisticsRequest,
    ) -> linkedmall_20180116_models.QueryOrderLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_logistics_with_options(request, runtime)

    async def query_order_logistics_async(
        self,
        request: linkedmall_20180116_models.QueryOrderLogisticsRequest,
    ) -> linkedmall_20180116_models.QueryOrderLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_logistics_with_options_async(request, runtime)

    def query_order_logistics_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.QueryOrderLogisticsWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderLogisticsWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_order_id):
            body['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrderLogisticsWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderLogisticsWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_logistics_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryOrderLogisticsWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryOrderLogisticsWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_order_id):
            body['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryOrderLogisticsWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryOrderLogisticsWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order_logistics_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.QueryOrderLogisticsWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.QueryOrderLogisticsWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_order_logistics_with_designated_tb_uid_with_options(request, runtime)

    async def query_order_logistics_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.QueryOrderLogisticsWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.QueryOrderLogisticsWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_order_logistics_with_designated_tb_uid_with_options_async(request, runtime)

    def query_real_tb_account_support_with_options(
        self,
        request: linkedmall_20180116_models.QueryRealTbAccountSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryRealTbAccountSupportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRealTbAccountSupport',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryRealTbAccountSupportResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_real_tb_account_support_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryRealTbAccountSupportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryRealTbAccountSupportResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRealTbAccountSupport',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryRealTbAccountSupportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_real_tb_account_support(
        self,
        request: linkedmall_20180116_models.QueryRealTbAccountSupportRequest,
    ) -> linkedmall_20180116_models.QueryRealTbAccountSupportResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_real_tb_account_support_with_options(request, runtime)

    async def query_real_tb_account_support_async(
        self,
        request: linkedmall_20180116_models.QueryRealTbAccountSupportRequest,
    ) -> linkedmall_20180116_models.QueryRealTbAccountSupportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_real_tb_account_support_with_options_async(request, runtime)

    def query_refund_application_detail_with_options(
        self,
        request: linkedmall_20180116_models.QueryRefundApplicationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryRefundApplicationDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRefundApplicationDetail',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryRefundApplicationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_refund_application_detail_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryRefundApplicationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryRefundApplicationDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRefundApplicationDetail',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryRefundApplicationDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_refund_application_detail(
        self,
        request: linkedmall_20180116_models.QueryRefundApplicationDetailRequest,
    ) -> linkedmall_20180116_models.QueryRefundApplicationDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_refund_application_detail_with_options(request, runtime)

    async def query_refund_application_detail_async(
        self,
        request: linkedmall_20180116_models.QueryRefundApplicationDetailRequest,
    ) -> linkedmall_20180116_models.QueryRefundApplicationDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_refund_application_detail_with_options_async(request, runtime)

    def query_refund_apply_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.QueryRefundApplyWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryRefundApplyWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRefundApplyWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryRefundApplyWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_refund_apply_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryRefundApplyWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryRefundApplyWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryRefundApplyWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryRefundApplyWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_refund_apply_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.QueryRefundApplyWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.QueryRefundApplyWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_refund_apply_with_designated_tb_uid_with_options(request, runtime)

    async def query_refund_apply_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.QueryRefundApplyWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.QueryRefundApplyWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_refund_apply_with_designated_tb_uid_with_options_async(request, runtime)

    def query_seller_license_with_options(
        self,
        request: linkedmall_20180116_models.QuerySellerLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QuerySellerLicenseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.seller_id):
            body['SellerId'] = request.seller_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySellerLicense',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QuerySellerLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_seller_license_with_options_async(
        self,
        request: linkedmall_20180116_models.QuerySellerLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QuerySellerLicenseResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.seller_id):
            body['SellerId'] = request.seller_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySellerLicense',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QuerySellerLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_seller_license(
        self,
        request: linkedmall_20180116_models.QuerySellerLicenseRequest,
    ) -> linkedmall_20180116_models.QuerySellerLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_seller_license_with_options(request, runtime)

    async def query_seller_license_async(
        self,
        request: linkedmall_20180116_models.QuerySellerLicenseRequest,
    ) -> linkedmall_20180116_models.QuerySellerLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_seller_license_with_options_async(request, runtime)

    def query_statements_with_options(
        self,
        request: linkedmall_20180116_models.QueryStatementsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryStatementsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.currency):
            query['Currency'] = request.currency
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payee_ids):
            query['PayeeIds'] = request.payee_ids
        if not UtilClient.is_unset(request.settle_noes):
            query['SettleNoes'] = request.settle_noes
        if not UtilClient.is_unset(request.settle_status):
            query['SettleStatus'] = request.settle_status
        if not UtilClient.is_unset(request.settle_type):
            query['SettleType'] = request.settle_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStatements',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryStatementsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_statements_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryStatementsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryStatementsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.currency):
            query['Currency'] = request.currency
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ext_info):
            query['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.payee_ids):
            query['PayeeIds'] = request.payee_ids
        if not UtilClient.is_unset(request.settle_noes):
            query['SettleNoes'] = request.settle_noes
        if not UtilClient.is_unset(request.settle_status):
            query['SettleStatus'] = request.settle_status
        if not UtilClient.is_unset(request.settle_type):
            query['SettleType'] = request.settle_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tenant_id):
            query['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStatements',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryStatementsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_statements(
        self,
        request: linkedmall_20180116_models.QueryStatementsRequest,
    ) -> linkedmall_20180116_models.QueryStatementsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_statements_with_options(request, runtime)

    async def query_statements_async(
        self,
        request: linkedmall_20180116_models.QueryStatementsRequest,
    ) -> linkedmall_20180116_models.QueryStatementsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_statements_with_options_async(request, runtime)

    def query_supplier_item_bill_download_url_with_options(
        self,
        request: linkedmall_20180116_models.QuerySupplierItemBillDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QuerySupplierItemBillDownloadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_id):
            body['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.bill_period):
            body['BillPeriod'] = request.bill_period
        if not UtilClient.is_unset(request.bill_status):
            body['BillStatus'] = request.bill_status
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.lm_shop_id):
            body['LmShopId'] = request.lm_shop_id
        if not UtilClient.is_unset(request.lm_shop_name):
            body['LmShopName'] = request.lm_shop_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySupplierItemBillDownloadUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QuerySupplierItemBillDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_supplier_item_bill_download_url_with_options_async(
        self,
        request: linkedmall_20180116_models.QuerySupplierItemBillDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QuerySupplierItemBillDownloadUrlResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bill_id):
            body['BillId'] = request.bill_id
        if not UtilClient.is_unset(request.bill_period):
            body['BillPeriod'] = request.bill_period
        if not UtilClient.is_unset(request.bill_status):
            body['BillStatus'] = request.bill_status
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_name):
            body['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.lm_shop_id):
            body['LmShopId'] = request.lm_shop_id
        if not UtilClient.is_unset(request.lm_shop_name):
            body['LmShopName'] = request.lm_shop_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySupplierItemBillDownloadUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QuerySupplierItemBillDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_supplier_item_bill_download_url(
        self,
        request: linkedmall_20180116_models.QuerySupplierItemBillDownloadUrlRequest,
    ) -> linkedmall_20180116_models.QuerySupplierItemBillDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_supplier_item_bill_download_url_with_options(request, runtime)

    async def query_supplier_item_bill_download_url_async(
        self,
        request: linkedmall_20180116_models.QuerySupplierItemBillDownloadUrlRequest,
    ) -> linkedmall_20180116_models.QuerySupplierItemBillDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_supplier_item_bill_download_url_with_options_async(request, runtime)

    def query_unfinished_activities_with_options(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUnfinishedActivitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUnfinishedActivities',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_unfinished_activities_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUnfinishedActivitiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUnfinishedActivities',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedActivitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_unfinished_activities(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedActivitiesRequest,
    ) -> linkedmall_20180116_models.QueryUnfinishedActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_unfinished_activities_with_options(request, runtime)

    async def query_unfinished_activities_async(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedActivitiesRequest,
    ) -> linkedmall_20180116_models.QueryUnfinishedActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_unfinished_activities_with_options_async(request, runtime)

    def query_unfinished_sessions_with_options(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_time):
            query['QueryTime'] = request.query_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUnfinishedSessions',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedSessionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_unfinished_sessions_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_time):
            query['QueryTime'] = request.query_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUnfinishedSessions',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedSessionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_unfinished_sessions(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedSessionsRequest,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_unfinished_sessions_with_options(request, runtime)

    async def query_unfinished_sessions_async(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedSessionsRequest,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_unfinished_sessions_with_options_async(request, runtime)

    def query_unfinished_sessions_4items_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryUnfinishedSessions4ItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessions4ItemsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUnfinishedSessions4ItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_ids_shrink):
            query['ItemIds'] = request.item_ids_shrink
        if not UtilClient.is_unset(request.lm_item_ids_shrink):
            query['LmItemIds'] = request.lm_item_ids_shrink
        if not UtilClient.is_unset(request.query_time):
            query['QueryTime'] = request.query_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUnfinishedSessions4Items',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedSessions4ItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_unfinished_sessions_4items_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryUnfinishedSessions4ItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessions4ItemsResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUnfinishedSessions4ItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_ids):
            request.item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_ids, 'ItemIds', 'json')
        if not UtilClient.is_unset(tmp_req.lm_item_ids):
            request.lm_item_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lm_item_ids, 'LmItemIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.item_ids_shrink):
            query['ItemIds'] = request.item_ids_shrink
        if not UtilClient.is_unset(request.lm_item_ids_shrink):
            query['LmItemIds'] = request.lm_item_ids_shrink
        if not UtilClient.is_unset(request.query_time):
            query['QueryTime'] = request.query_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUnfinishedSessions4Items',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUnfinishedSessions4ItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_unfinished_sessions_4items(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedSessions4ItemsRequest,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessions4ItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_unfinished_sessions_4items_with_options(request, runtime)

    async def query_unfinished_sessions_4items_async(
        self,
        request: linkedmall_20180116_models.QueryUnfinishedSessions4ItemsRequest,
    ) -> linkedmall_20180116_models.QueryUnfinishedSessions4ItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_unfinished_sessions_4items_with_options_async(request, runtime)

    def query_upcoming_movies_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryUpcomingMoviesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUpcomingMoviesResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUpcomingMoviesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_json):
            request.ext_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_json, 'ExtJson', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.city_code):
            query['CityCode'] = request.city_code
        if not UtilClient.is_unset(request.ext_json_shrink):
            query['ExtJson'] = request.ext_json_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUpcomingMovies',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUpcomingMoviesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_upcoming_movies_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryUpcomingMoviesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUpcomingMoviesResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUpcomingMoviesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_json):
            request.ext_json_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_json, 'ExtJson', 'json')
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.city_code):
            query['CityCode'] = request.city_code
        if not UtilClient.is_unset(request.ext_json_shrink):
            query['ExtJson'] = request.ext_json_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUpcomingMovies',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUpcomingMoviesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_upcoming_movies(
        self,
        request: linkedmall_20180116_models.QueryUpcomingMoviesRequest,
    ) -> linkedmall_20180116_models.QueryUpcomingMoviesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_upcoming_movies_with_options(request, runtime)

    async def query_upcoming_movies_async(
        self,
        request: linkedmall_20180116_models.QueryUpcomingMoviesRequest,
    ) -> linkedmall_20180116_models.QueryUpcomingMoviesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_upcoming_movies_with_options_async(request, runtime)

    def query_user_account_with_options(
        self,
        request: linkedmall_20180116_models.QueryUserAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUserAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryUserAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUserAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_account_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryUserAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUserAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryUserAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUserAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_account(
        self,
        request: linkedmall_20180116_models.QueryUserAccountRequest,
    ) -> linkedmall_20180116_models.QueryUserAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_account_with_options(request, runtime)

    async def query_user_account_async(
        self,
        request: linkedmall_20180116_models.QueryUserAccountRequest,
    ) -> linkedmall_20180116_models.QueryUserAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_account_with_options_async(request, runtime)

    def query_user_game_process_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryUserGameProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUserGameProcessResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUserGameProcessShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryUserGameProcess',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUserGameProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_game_process_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryUserGameProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUserGameProcessResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUserGameProcessShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.process_id):
            query['ProcessId'] = request.process_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryUserGameProcess',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUserGameProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_game_process(
        self,
        request: linkedmall_20180116_models.QueryUserGameProcessRequest,
    ) -> linkedmall_20180116_models.QueryUserGameProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_game_process_with_options(request, runtime)

    async def query_user_game_process_async(
        self,
        request: linkedmall_20180116_models.QueryUserGameProcessRequest,
    ) -> linkedmall_20180116_models.QueryUserGameProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_game_process_with_options_async(request, runtime)

    def query_user_point_with_options(
        self,
        tmp_req: linkedmall_20180116_models.QueryUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUserPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_point_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.QueryUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.QueryUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryUserPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_point(
        self,
        request: linkedmall_20180116_models.QueryUserPointRequest,
    ) -> linkedmall_20180116_models.QueryUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_user_point_with_options(request, runtime)

    async def query_user_point_async(
        self,
        request: linkedmall_20180116_models.QueryUserPointRequest,
    ) -> linkedmall_20180116_models.QueryUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_user_point_with_options_async(request, runtime)

    def query_withhold_trade_with_options(
        self,
        request: linkedmall_20180116_models.QueryWithholdTradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryWithholdTradeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.out_trade_no):
            body['OutTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.trade_no):
            body['TradeNo'] = request.trade_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryWithholdTrade',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryWithholdTradeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_withhold_trade_with_options_async(
        self,
        request: linkedmall_20180116_models.QueryWithholdTradeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.QueryWithholdTradeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.out_trade_no):
            body['OutTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.trade_no):
            body['TradeNo'] = request.trade_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryWithholdTrade',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.QueryWithholdTradeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_withhold_trade(
        self,
        request: linkedmall_20180116_models.QueryWithholdTradeRequest,
    ) -> linkedmall_20180116_models.QueryWithholdTradeResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_withhold_trade_with_options(request, runtime)

    async def query_withhold_trade_async(
        self,
        request: linkedmall_20180116_models.QueryWithholdTradeRequest,
    ) -> linkedmall_20180116_models.QueryWithholdTradeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_withhold_trade_with_options_async(request, runtime)

    def rebind_tb_account_with_options(
        self,
        request: linkedmall_20180116_models.RebindTbAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RebindTbAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RebindTbAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RebindTbAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebind_tb_account_with_options_async(
        self,
        request: linkedmall_20180116_models.RebindTbAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RebindTbAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RebindTbAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RebindTbAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebind_tb_account(
        self,
        request: linkedmall_20180116_models.RebindTbAccountRequest,
    ) -> linkedmall_20180116_models.RebindTbAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.rebind_tb_account_with_options(request, runtime)

    async def rebind_tb_account_async(
        self,
        request: linkedmall_20180116_models.RebindTbAccountRequest,
    ) -> linkedmall_20180116_models.RebindTbAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rebind_tb_account_with_options_async(request, runtime)

    def refresh_settlement_order_account_with_options(
        self,
        request: linkedmall_20180116_models.RefreshSettlementOrderAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefreshSettlementOrderAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshSettlementOrderAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefreshSettlementOrderAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_settlement_order_account_with_options_async(
        self,
        request: linkedmall_20180116_models.RefreshSettlementOrderAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefreshSettlementOrderAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_id):
            body['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshSettlementOrderAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefreshSettlementOrderAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_settlement_order_account(
        self,
        request: linkedmall_20180116_models.RefreshSettlementOrderAccountRequest,
    ) -> linkedmall_20180116_models.RefreshSettlementOrderAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_settlement_order_account_with_options(request, runtime)

    async def refresh_settlement_order_account_async(
        self,
        request: linkedmall_20180116_models.RefreshSettlementOrderAccountRequest,
    ) -> linkedmall_20180116_models.RefreshSettlementOrderAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_settlement_order_account_with_options_async(request, runtime)

    def refund_order_with_options(
        self,
        request: linkedmall_20180116_models.RefundOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefundOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.out_request_no):
            body['OutRequestNo'] = request.out_request_no
        if not UtilClient.is_unset(request.out_trade_no):
            body['OutTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.refund_amount):
            body['RefundAmount'] = request.refund_amount
        if not UtilClient.is_unset(request.refund_reason):
            body['RefundReason'] = request.refund_reason
        if not UtilClient.is_unset(request.refund_royalty_parameters):
            body['RefundRoyaltyParameters'] = request.refund_royalty_parameters
        if not UtilClient.is_unset(request.trade_no):
            body['TradeNo'] = request.trade_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefundOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefundOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_order_with_options_async(
        self,
        request: linkedmall_20180116_models.RefundOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefundOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.out_request_no):
            body['OutRequestNo'] = request.out_request_no
        if not UtilClient.is_unset(request.out_trade_no):
            body['OutTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.refund_amount):
            body['RefundAmount'] = request.refund_amount
        if not UtilClient.is_unset(request.refund_reason):
            body['RefundReason'] = request.refund_reason
        if not UtilClient.is_unset(request.refund_royalty_parameters):
            body['RefundRoyaltyParameters'] = request.refund_royalty_parameters
        if not UtilClient.is_unset(request.trade_no):
            body['TradeNo'] = request.trade_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefundOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefundOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_order(
        self,
        request: linkedmall_20180116_models.RefundOrderRequest,
    ) -> linkedmall_20180116_models.RefundOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_order_with_options(request, runtime)

    async def refund_order_async(
        self,
        request: linkedmall_20180116_models.RefundOrderRequest,
    ) -> linkedmall_20180116_models.RefundOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_order_with_options_async(request, runtime)

    def refund_point_with_options(
        self,
        request: linkedmall_20180116_models.RefundPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefundPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.seller_id):
            query['SellerId'] = request.seller_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefundPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_point_with_options_async(
        self,
        request: linkedmall_20180116_models.RefundPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefundPointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.seller_id):
            query['SellerId'] = request.seller_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefundPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefundPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_point(
        self,
        request: linkedmall_20180116_models.RefundPointRequest,
    ) -> linkedmall_20180116_models.RefundPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_point_with_options(request, runtime)

    async def refund_point_async(
        self,
        request: linkedmall_20180116_models.RefundPointRequest,
    ) -> linkedmall_20180116_models.RefundPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_point_with_options_async(request, runtime)

    def refund_user_point_with_options(
        self,
        tmp_req: linkedmall_20180116_models.RefundUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefundUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.RefundUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.origin_record_id):
            query['OriginRecordId'] = request.origin_record_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefundUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefundUserPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def refund_user_point_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.RefundUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefundUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.RefundUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.origin_record_id):
            query['OriginRecordId'] = request.origin_record_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefundUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefundUserPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refund_user_point(
        self,
        request: linkedmall_20180116_models.RefundUserPointRequest,
    ) -> linkedmall_20180116_models.RefundUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.refund_user_point_with_options(request, runtime)

    async def refund_user_point_async(
        self,
        request: linkedmall_20180116_models.RefundUserPointRequest,
    ) -> linkedmall_20180116_models.RefundUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refund_user_point_with_options_async(request, runtime)

    def refuse_merchant_sync_task_with_options(
        self,
        request: linkedmall_20180116_models.RefuseMerchantSyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefuseMerchantSyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.seller_nick):
            query['SellerNick'] = request.seller_nick
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefuseMerchantSyncTask',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefuseMerchantSyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def refuse_merchant_sync_task_with_options_async(
        self,
        request: linkedmall_20180116_models.RefuseMerchantSyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RefuseMerchantSyncTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.seller_nick):
            query['SellerNick'] = request.seller_nick
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefuseMerchantSyncTask',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RefuseMerchantSyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refuse_merchant_sync_task(
        self,
        request: linkedmall_20180116_models.RefuseMerchantSyncTaskRequest,
    ) -> linkedmall_20180116_models.RefuseMerchantSyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.refuse_merchant_sync_task_with_options(request, runtime)

    async def refuse_merchant_sync_task_async(
        self,
        request: linkedmall_20180116_models.RefuseMerchantSyncTaskRequest,
    ) -> linkedmall_20180116_models.RefuseMerchantSyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refuse_merchant_sync_task_with_options_async(request, runtime)

    def regist_anonymous_tb_account_with_options(
        self,
        request: linkedmall_20180116_models.RegistAnonymousTbAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RegistAnonymousTbAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegistAnonymousTbAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RegistAnonymousTbAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def regist_anonymous_tb_account_with_options_async(
        self,
        request: linkedmall_20180116_models.RegistAnonymousTbAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RegistAnonymousTbAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegistAnonymousTbAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RegistAnonymousTbAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def regist_anonymous_tb_account(
        self,
        request: linkedmall_20180116_models.RegistAnonymousTbAccountRequest,
    ) -> linkedmall_20180116_models.RegistAnonymousTbAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.regist_anonymous_tb_account_with_options(request, runtime)

    async def regist_anonymous_tb_account_async(
        self,
        request: linkedmall_20180116_models.RegistAnonymousTbAccountRequest,
    ) -> linkedmall_20180116_models.RegistAnonymousTbAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.regist_anonymous_tb_account_with_options_async(request, runtime)

    def register_settle_account_with_options(
        self,
        request: linkedmall_20180116_models.RegisterSettleAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RegisterSettleAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_channel):
            body['AccountChannel'] = request.account_channel
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_no):
            body['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.account_pay_type):
            body['AccountPayType'] = request.account_pay_type
        if not UtilClient.is_unset(request.account_type):
            body['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.country_or_area_code):
            body['CountryOrAreaCode'] = request.country_or_area_code
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.idempotent_id):
            body['IdempotentId'] = request.idempotent_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterSettleAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RegisterSettleAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_settle_account_with_options_async(
        self,
        request: linkedmall_20180116_models.RegisterSettleAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RegisterSettleAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_channel):
            body['AccountChannel'] = request.account_channel
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_no):
            body['AccountNo'] = request.account_no
        if not UtilClient.is_unset(request.account_pay_type):
            body['AccountPayType'] = request.account_pay_type
        if not UtilClient.is_unset(request.account_type):
            body['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.country_or_area_code):
            body['CountryOrAreaCode'] = request.country_or_area_code
        if not UtilClient.is_unset(request.currency):
            body['Currency'] = request.currency
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.idempotent_id):
            body['IdempotentId'] = request.idempotent_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterSettleAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RegisterSettleAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_settle_account(
        self,
        request: linkedmall_20180116_models.RegisterSettleAccountRequest,
    ) -> linkedmall_20180116_models.RegisterSettleAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_settle_account_with_options(request, runtime)

    async def register_settle_account_async(
        self,
        request: linkedmall_20180116_models.RegisterSettleAccountRequest,
    ) -> linkedmall_20180116_models.RegisterSettleAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_settle_account_with_options_async(request, runtime)

    def register_user_account_with_options(
        self,
        request: linkedmall_20180116_models.RegisterUserAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RegisterUserAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterUserAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RegisterUserAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_user_account_with_options_async(
        self,
        request: linkedmall_20180116_models.RegisterUserAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RegisterUserAccountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterUserAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RegisterUserAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_user_account(
        self,
        request: linkedmall_20180116_models.RegisterUserAccountRequest,
    ) -> linkedmall_20180116_models.RegisterUserAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_user_account_with_options(request, runtime)

    async def register_user_account_async(
        self,
        request: linkedmall_20180116_models.RegisterUserAccountRequest,
    ) -> linkedmall_20180116_models.RegisterUserAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_user_account_with_options_async(request, runtime)

    def release_movie_seat_with_options(
        self,
        request: linkedmall_20180116_models.ReleaseMovieSeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ReleaseMovieSeatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.lock_seat_apply_key):
            query['LockSeatApplyKey'] = request.lock_seat_apply_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseMovieSeat',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ReleaseMovieSeatResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_movie_seat_with_options_async(
        self,
        request: linkedmall_20180116_models.ReleaseMovieSeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ReleaseMovieSeatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.lock_seat_apply_key):
            query['LockSeatApplyKey'] = request.lock_seat_apply_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseMovieSeat',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ReleaseMovieSeatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_movie_seat(
        self,
        request: linkedmall_20180116_models.ReleaseMovieSeatRequest,
    ) -> linkedmall_20180116_models.ReleaseMovieSeatResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_movie_seat_with_options(request, runtime)

    async def release_movie_seat_async(
        self,
        request: linkedmall_20180116_models.ReleaseMovieSeatRequest,
    ) -> linkedmall_20180116_models.ReleaseMovieSeatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_movie_seat_with_options_async(request, runtime)

    def remove_address_with_options(
        self,
        request: linkedmall_20180116_models.RemoveAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RemoveAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.address_info):
            body['AddressInfo'] = request.address_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveAddress',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RemoveAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_address_with_options_async(
        self,
        request: linkedmall_20180116_models.RemoveAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RemoveAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.address_info):
            body['AddressInfo'] = request.address_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveAddress',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RemoveAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_address(
        self,
        request: linkedmall_20180116_models.RemoveAddressRequest,
    ) -> linkedmall_20180116_models.RemoveAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_address_with_options(request, runtime)

    async def remove_address_async(
        self,
        request: linkedmall_20180116_models.RemoveAddressRequest,
    ) -> linkedmall_20180116_models.RemoveAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_address_with_options_async(request, runtime)

    def remove_messages_with_options(
        self,
        request: linkedmall_20180116_models.RemoveMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RemoveMessagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.message_ids):
            query['MessageIds'] = request.message_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveMessages',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RemoveMessagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_messages_with_options_async(
        self,
        request: linkedmall_20180116_models.RemoveMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RemoveMessagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.message_ids):
            query['MessageIds'] = request.message_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveMessages',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RemoveMessagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_messages(
        self,
        request: linkedmall_20180116_models.RemoveMessagesRequest,
    ) -> linkedmall_20180116_models.RemoveMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_messages_with_options(request, runtime)

    async def remove_messages_async(
        self,
        request: linkedmall_20180116_models.RemoveMessagesRequest,
    ) -> linkedmall_20180116_models.RemoveMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_messages_with_options_async(request, runtime)

    def render_h5order_with_options(
        self,
        request: linkedmall_20180116_models.RenderH5OrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RenderH5OrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.buy_order_request_model):
            query['BuyOrderRequestModel'] = request.buy_order_request_model
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenderH5Order',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RenderH5OrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def render_h5order_with_options_async(
        self,
        request: linkedmall_20180116_models.RenderH5OrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RenderH5OrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.buy_order_request_model):
            query['BuyOrderRequestModel'] = request.buy_order_request_model
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenderH5Order',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RenderH5OrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def render_h5order(
        self,
        request: linkedmall_20180116_models.RenderH5OrderRequest,
    ) -> linkedmall_20180116_models.RenderH5OrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.render_h5order_with_options(request, runtime)

    async def render_h5order_async(
        self,
        request: linkedmall_20180116_models.RenderH5OrderRequest,
    ) -> linkedmall_20180116_models.RenderH5OrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.render_h5order_with_options_async(request, runtime)

    def render_order_with_options(
        self,
        request: linkedmall_20180116_models.RenderOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RenderOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.delivery_address):
            query['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenderOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RenderOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def render_order_with_options_async(
        self,
        request: linkedmall_20180116_models.RenderOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RenderOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.delivery_address):
            query['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.item_list):
            query['ItemList'] = request.item_list
        if not UtilClient.is_unset(request.lm_item_id):
            query['LmItemId'] = request.lm_item_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenderOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RenderOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def render_order(
        self,
        request: linkedmall_20180116_models.RenderOrderRequest,
    ) -> linkedmall_20180116_models.RenderOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.render_order_with_options(request, runtime)

    async def render_order_async(
        self,
        request: linkedmall_20180116_models.RenderOrderRequest,
    ) -> linkedmall_20180116_models.RenderOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.render_order_with_options_async(request, runtime)

    def render_order_with_designated_tb_uid_with_options(
        self,
        tmp_req: linkedmall_20180116_models.RenderOrderWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RenderOrderWithDesignatedTbUidResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.RenderOrderWithDesignatedTbUidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_list):
            request.item_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_list, 'ItemList', 'json')
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.delivery_address):
            body['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.item_list_shrink):
            body['ItemList'] = request.item_list_shrink
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenderOrderWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RenderOrderWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def render_order_with_designated_tb_uid_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.RenderOrderWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RenderOrderWithDesignatedTbUidResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.RenderOrderWithDesignatedTbUidShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.item_list):
            request.item_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.item_list, 'ItemList', 'json')
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.delivery_address):
            body['DeliveryAddress'] = request.delivery_address
        if not UtilClient.is_unset(request.item_list_shrink):
            body['ItemList'] = request.item_list_shrink
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RenderOrderWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RenderOrderWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def render_order_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.RenderOrderWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.RenderOrderWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.render_order_with_designated_tb_uid_with_options(request, runtime)

    async def render_order_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.RenderOrderWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.RenderOrderWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.render_order_with_designated_tb_uid_with_options_async(request, runtime)

    def repay_for_pay_url_with_options(
        self,
        request: linkedmall_20180116_models.RepayForPayUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RepayForPayUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RepayForPayUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RepayForPayUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def repay_for_pay_url_with_options_async(
        self,
        request: linkedmall_20180116_models.RepayForPayUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RepayForPayUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RepayForPayUrl',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RepayForPayUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def repay_for_pay_url(
        self,
        request: linkedmall_20180116_models.RepayForPayUrlRequest,
    ) -> linkedmall_20180116_models.RepayForPayUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.repay_for_pay_url_with_options(request, runtime)

    async def repay_for_pay_url_async(
        self,
        request: linkedmall_20180116_models.RepayForPayUrlRequest,
    ) -> linkedmall_20180116_models.RepayForPayUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.repay_for_pay_url_with_options_async(request, runtime)

    def repay_order_with_options(
        self,
        request: linkedmall_20180116_models.RepayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RepayOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RepayOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RepayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def repay_order_with_options_async(
        self,
        request: linkedmall_20180116_models.RepayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RepayOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.lm_order_id):
            query['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RepayOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RepayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def repay_order(
        self,
        request: linkedmall_20180116_models.RepayOrderRequest,
    ) -> linkedmall_20180116_models.RepayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.repay_order_with_options(request, runtime)

    async def repay_order_async(
        self,
        request: linkedmall_20180116_models.RepayOrderRequest,
    ) -> linkedmall_20180116_models.RepayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.repay_order_with_options_async(request, runtime)

    def repay_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.RepayWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RepayWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_json):
            body['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.lm_order_id):
            body['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RepayWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RepayWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def repay_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.RepayWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.RepayWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.ext_json):
            body['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.lm_order_id):
            body['LmOrderId'] = request.lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RepayWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.RepayWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def repay_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.RepayWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.RepayWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.repay_with_designated_tb_uid_with_options(request, runtime)

    async def repay_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.RepayWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.RepayWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.repay_with_designated_tb_uid_with_options_async(request, runtime)

    def reserve_movie_seat_with_options(
        self,
        request: linkedmall_20180116_models.ReserveMovieSeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ReserveMovieSeatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.schedule_id):
            query['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.seat_ids):
            query['SeatIds'] = request.seat_ids
        if not UtilClient.is_unset(request.seat_names):
            query['SeatNames'] = request.seat_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReserveMovieSeat',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ReserveMovieSeatResponse(),
            self.call_api(params, req, runtime)
        )

    async def reserve_movie_seat_with_options_async(
        self,
        request: linkedmall_20180116_models.ReserveMovieSeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ReserveMovieSeatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.schedule_id):
            query['ScheduleId'] = request.schedule_id
        if not UtilClient.is_unset(request.seat_ids):
            query['SeatIds'] = request.seat_ids
        if not UtilClient.is_unset(request.seat_names):
            query['SeatNames'] = request.seat_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReserveMovieSeat',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ReserveMovieSeatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reserve_movie_seat(
        self,
        request: linkedmall_20180116_models.ReserveMovieSeatRequest,
    ) -> linkedmall_20180116_models.ReserveMovieSeatResponse:
        runtime = util_models.RuntimeOptions()
        return self.reserve_movie_seat_with_options(request, runtime)

    async def reserve_movie_seat_async(
        self,
        request: linkedmall_20180116_models.ReserveMovieSeatRequest,
    ) -> linkedmall_20180116_models.ReserveMovieSeatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reserve_movie_seat_with_options_async(request, runtime)

    def settle_order_with_options(
        self,
        request: linkedmall_20180116_models.SettleOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SettleOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.out_request_no):
            body['OutRequestNo'] = request.out_request_no
        if not UtilClient.is_unset(request.out_trade_no):
            body['OutTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.royalty_parameters):
            body['RoyaltyParameters'] = request.royalty_parameters
        if not UtilClient.is_unset(request.trade_no):
            body['TradeNo'] = request.trade_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SettleOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SettleOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def settle_order_with_options_async(
        self,
        request: linkedmall_20180116_models.SettleOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SettleOrderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ext_info):
            body['ExtInfo'] = request.ext_info
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.out_request_no):
            body['OutRequestNo'] = request.out_request_no
        if not UtilClient.is_unset(request.out_trade_no):
            body['OutTradeNo'] = request.out_trade_no
        if not UtilClient.is_unset(request.royalty_parameters):
            body['RoyaltyParameters'] = request.royalty_parameters
        if not UtilClient.is_unset(request.trade_no):
            body['TradeNo'] = request.trade_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SettleOrder',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SettleOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def settle_order(
        self,
        request: linkedmall_20180116_models.SettleOrderRequest,
    ) -> linkedmall_20180116_models.SettleOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.settle_order_with_options(request, runtime)

    async def settle_order_async(
        self,
        request: linkedmall_20180116_models.SettleOrderRequest,
    ) -> linkedmall_20180116_models.SettleOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.settle_order_with_options_async(request, runtime)

    def start_user_game_with_options(
        self,
        tmp_req: linkedmall_20180116_models.StartUserGameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.StartUserGameResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.StartUserGameShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.game_id):
            query['GameId'] = request.game_id
        if not UtilClient.is_unset(request.route_id):
            query['RouteId'] = request.route_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.user_app):
            query['UserApp'] = request.user_app
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartUserGame',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.StartUserGameResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_user_game_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.StartUserGameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.StartUserGameResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.StartUserGameShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.activity_id):
            query['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.game_id):
            query['GameId'] = request.game_id
        if not UtilClient.is_unset(request.route_id):
            query['RouteId'] = request.route_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.user_app):
            query['UserApp'] = request.user_app
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartUserGame',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.StartUserGameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_user_game(
        self,
        request: linkedmall_20180116_models.StartUserGameRequest,
    ) -> linkedmall_20180116_models.StartUserGameResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_user_game_with_options(request, runtime)

    async def start_user_game_async(
        self,
        request: linkedmall_20180116_models.StartUserGameRequest,
    ) -> linkedmall_20180116_models.StartUserGameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_user_game_with_options_async(request, runtime)

    def submit_return_good_logistics_with_options(
        self,
        request: linkedmall_20180116_models.SubmitReturnGoodLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SubmitReturnGoodLogisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.cp_code):
            query['CpCode'] = request.cp_code
        if not UtilClient.is_unset(request.dispute_id):
            query['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.logistics_no):
            query['LogisticsNo'] = request.logistics_no
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitReturnGoodLogistics',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SubmitReturnGoodLogisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_return_good_logistics_with_options_async(
        self,
        request: linkedmall_20180116_models.SubmitReturnGoodLogisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SubmitReturnGoodLogisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.cp_code):
            query['CpCode'] = request.cp_code
        if not UtilClient.is_unset(request.dispute_id):
            query['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.logistics_no):
            query['LogisticsNo'] = request.logistics_no
        if not UtilClient.is_unset(request.sub_lm_order_id):
            query['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitReturnGoodLogistics',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SubmitReturnGoodLogisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_return_good_logistics(
        self,
        request: linkedmall_20180116_models.SubmitReturnGoodLogisticsRequest,
    ) -> linkedmall_20180116_models.SubmitReturnGoodLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_return_good_logistics_with_options(request, runtime)

    async def submit_return_good_logistics_async(
        self,
        request: linkedmall_20180116_models.SubmitReturnGoodLogisticsRequest,
    ) -> linkedmall_20180116_models.SubmitReturnGoodLogisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_return_good_logistics_with_options_async(request, runtime)

    def submit_return_good_logistics_with_designated_tb_uid_with_options(
        self,
        request: linkedmall_20180116_models.SubmitReturnGoodLogisticsWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SubmitReturnGoodLogisticsWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.cp_code):
            body['CpCode'] = request.cp_code
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.logistics_no):
            body['LogisticsNo'] = request.logistics_no
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitReturnGoodLogisticsWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SubmitReturnGoodLogisticsWithDesignatedTbUidResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_return_good_logistics_with_designated_tb_uid_with_options_async(
        self,
        request: linkedmall_20180116_models.SubmitReturnGoodLogisticsWithDesignatedTbUidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SubmitReturnGoodLogisticsWithDesignatedTbUidResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.cp_code):
            body['CpCode'] = request.cp_code
        if not UtilClient.is_unset(request.dispute_id):
            body['DisputeId'] = request.dispute_id
        if not UtilClient.is_unset(request.logistics_no):
            body['LogisticsNo'] = request.logistics_no
        if not UtilClient.is_unset(request.sub_lm_order_id):
            body['SubLmOrderId'] = request.sub_lm_order_id
        if not UtilClient.is_unset(request.tb_account_type):
            body['TbAccountType'] = request.tb_account_type
        if not UtilClient.is_unset(request.tb_user_id):
            body['TbUserId'] = request.tb_user_id
        if not UtilClient.is_unset(request.third_party_user_id):
            body['ThirdPartyUserId'] = request.third_party_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitReturnGoodLogisticsWithDesignatedTbUid',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SubmitReturnGoodLogisticsWithDesignatedTbUidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_return_good_logistics_with_designated_tb_uid(
        self,
        request: linkedmall_20180116_models.SubmitReturnGoodLogisticsWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.SubmitReturnGoodLogisticsWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_return_good_logistics_with_designated_tb_uid_with_options(request, runtime)

    async def submit_return_good_logistics_with_designated_tb_uid_async(
        self,
        request: linkedmall_20180116_models.SubmitReturnGoodLogisticsWithDesignatedTbUidRequest,
    ) -> linkedmall_20180116_models.SubmitReturnGoodLogisticsWithDesignatedTbUidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_return_good_logistics_with_designated_tb_uid_with_options_async(request, runtime)

    def sync_merchant_info_with_options(
        self,
        request: linkedmall_20180116_models.SyncMerchantInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SyncMerchantInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.seller_nick):
            query['SellerNick'] = request.seller_nick
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        body = {}
        if not UtilClient.is_unset(request.item_list):
            body['ItemList'] = request.item_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncMerchantInfo',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SyncMerchantInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_merchant_info_with_options_async(
        self,
        request: linkedmall_20180116_models.SyncMerchantInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.SyncMerchantInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.seller_nick):
            query['SellerNick'] = request.seller_nick
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.time_stamp):
            query['TimeStamp'] = request.time_stamp
        body = {}
        if not UtilClient.is_unset(request.item_list):
            body['ItemList'] = request.item_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncMerchantInfo',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.SyncMerchantInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_merchant_info(
        self,
        request: linkedmall_20180116_models.SyncMerchantInfoRequest,
    ) -> linkedmall_20180116_models.SyncMerchantInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_merchant_info_with_options(request, runtime)

    async def sync_merchant_info_async(
        self,
        request: linkedmall_20180116_models.SyncMerchantInfoRequest,
    ) -> linkedmall_20180116_models.SyncMerchantInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_merchant_info_with_options_async(request, runtime)

    def un_freeze_user_point_with_options(
        self,
        tmp_req: linkedmall_20180116_models.UnFreezeUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.UnFreezeUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.UnFreezeUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnFreezeUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.UnFreezeUserPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_freeze_user_point_with_options_async(
        self,
        tmp_req: linkedmall_20180116_models.UnFreezeUserPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.UnFreezeUserPointResponse:
        UtilClient.validate_model(tmp_req)
        request = linkedmall_20180116_models.UnFreezeUserPointShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ext_info):
            request.ext_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ext_info, 'ExtInfo', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.idempotent_id):
            query['IdempotentId'] = request.idempotent_id
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        body = {}
        if not UtilClient.is_unset(request.ext_info_shrink):
            body['ExtInfo'] = request.ext_info_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnFreezeUserPoint',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.UnFreezeUserPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_freeze_user_point(
        self,
        request: linkedmall_20180116_models.UnFreezeUserPointRequest,
    ) -> linkedmall_20180116_models.UnFreezeUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_freeze_user_point_with_options(request, runtime)

    async def un_freeze_user_point_async(
        self,
        request: linkedmall_20180116_models.UnFreezeUserPointRequest,
    ) -> linkedmall_20180116_models.UnFreezeUserPointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_freeze_user_point_with_options_async(request, runtime)

    def unsign_withhold_agreement_with_options(
        self,
        request: linkedmall_20180116_models.UnsignWithholdAgreementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.UnsignWithholdAgreementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agreement_no):
            body['AgreementNo'] = request.agreement_no
        if not UtilClient.is_unset(request.external_agreement_no):
            body['ExternalAgreementNo'] = request.external_agreement_no
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.out_request_no):
            body['OutRequestNo'] = request.out_request_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnsignWithholdAgreement',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.UnsignWithholdAgreementResponse(),
            self.call_api(params, req, runtime)
        )

    async def unsign_withhold_agreement_with_options_async(
        self,
        request: linkedmall_20180116_models.UnsignWithholdAgreementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.UnsignWithholdAgreementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agreement_no):
            body['AgreementNo'] = request.agreement_no
        if not UtilClient.is_unset(request.external_agreement_no):
            body['ExternalAgreementNo'] = request.external_agreement_no
        if not UtilClient.is_unset(request.merchant_id):
            body['MerchantId'] = request.merchant_id
        if not UtilClient.is_unset(request.out_request_no):
            body['OutRequestNo'] = request.out_request_no
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnsignWithholdAgreement',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.UnsignWithholdAgreementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unsign_withhold_agreement(
        self,
        request: linkedmall_20180116_models.UnsignWithholdAgreementRequest,
    ) -> linkedmall_20180116_models.UnsignWithholdAgreementResponse:
        runtime = util_models.RuntimeOptions()
        return self.unsign_withhold_agreement_with_options(request, runtime)

    async def unsign_withhold_agreement_async(
        self,
        request: linkedmall_20180116_models.UnsignWithholdAgreementRequest,
    ) -> linkedmall_20180116_models.UnsignWithholdAgreementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unsign_withhold_agreement_with_options_async(request, runtime)

    def update_address_with_options(
        self,
        request: linkedmall_20180116_models.UpdateAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.UpdateAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.address_info):
            body['AddressInfo'] = request.address_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAddress',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.UpdateAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_address_with_options_async(
        self,
        request: linkedmall_20180116_models.UpdateAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.UpdateAddressResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.third_party_user_id):
            query['ThirdPartyUserId'] = request.third_party_user_id
        if not UtilClient.is_unset(request.use_anonymous_tb_account):
            query['UseAnonymousTbAccount'] = request.use_anonymous_tb_account
        body = {}
        if not UtilClient.is_unset(request.address_info):
            body['AddressInfo'] = request.address_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAddress',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.UpdateAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_address(
        self,
        request: linkedmall_20180116_models.UpdateAddressRequest,
    ) -> linkedmall_20180116_models.UpdateAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_address_with_options(request, runtime)

    async def update_address_async(
        self,
        request: linkedmall_20180116_models.UpdateAddressRequest,
    ) -> linkedmall_20180116_models.UpdateAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_address_with_options_async(request, runtime)

    def validate_taobao_account_with_options(
        self,
        request: linkedmall_20180116_models.ValidateTaobaoAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ValidateTaobaoAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.mobile_no):
            query['MobileNo'] = request.mobile_no
        if not UtilClient.is_unset(request.tb_user_nick):
            query['TbUserNick'] = request.tb_user_nick
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateTaobaoAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ValidateTaobaoAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_taobao_account_with_options_async(
        self,
        request: linkedmall_20180116_models.ValidateTaobaoAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkedmall_20180116_models.ValidateTaobaoAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.biz_uid):
            query['BizUid'] = request.biz_uid
        if not UtilClient.is_unset(request.ext_json):
            query['ExtJson'] = request.ext_json
        if not UtilClient.is_unset(request.mobile_no):
            query['MobileNo'] = request.mobile_no
        if not UtilClient.is_unset(request.tb_user_nick):
            query['TbUserNick'] = request.tb_user_nick
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ValidateTaobaoAccount',
            version='2018-01-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkedmall_20180116_models.ValidateTaobaoAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_taobao_account(
        self,
        request: linkedmall_20180116_models.ValidateTaobaoAccountRequest,
    ) -> linkedmall_20180116_models.ValidateTaobaoAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_taobao_account_with_options(request, runtime)

    async def validate_taobao_account_async(
        self,
        request: linkedmall_20180116_models.ValidateTaobaoAccountRequest,
    ) -> linkedmall_20180116_models.ValidateTaobaoAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_taobao_account_with_options_async(request, runtime)
