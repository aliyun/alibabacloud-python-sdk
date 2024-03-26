# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_resellertrade20191227 import models as reseller_trade_20191227_models
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
            'ap-northeast-1': 'resellertrade.aliyuncs.com',
            'ap-northeast-2-pop': 'resellertrade.aliyuncs.com',
            'ap-south-1': 'resellertrade.aliyuncs.com',
            'ap-southeast-1': 'resellertrade.aliyuncs.com',
            'ap-southeast-2': 'resellertrade.aliyuncs.com',
            'ap-southeast-3': 'resellertrade.aliyuncs.com',
            'ap-southeast-5': 'resellertrade.aliyuncs.com',
            'cn-beijing': 'resellertrade.aliyuncs.com',
            'cn-beijing-finance-1': 'resellertrade.aliyuncs.com',
            'cn-beijing-finance-pop': 'resellertrade.aliyuncs.com',
            'cn-beijing-gov-1': 'resellertrade.aliyuncs.com',
            'cn-beijing-nu16-b01': 'resellertrade.aliyuncs.com',
            'cn-chengdu': 'resellertrade.aliyuncs.com',
            'cn-edge-1': 'resellertrade.aliyuncs.com',
            'cn-fujian': 'resellertrade.aliyuncs.com',
            'cn-haidian-cm12-c01': 'resellertrade.aliyuncs.com',
            'cn-hangzhou': 'resellertrade.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'resellertrade.aliyuncs.com',
            'cn-hangzhou-finance': 'resellertrade.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'resellertrade.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'resellertrade.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'resellertrade.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'resellertrade.aliyuncs.com',
            'cn-hangzhou-test-306': 'resellertrade.aliyuncs.com',
            'cn-hongkong': 'resellertrade.aliyuncs.com',
            'cn-hongkong-finance-pop': 'resellertrade.aliyuncs.com',
            'cn-huhehaote': 'resellertrade.aliyuncs.com',
            'cn-north-2-gov-1': 'resellertrade.aliyuncs.com',
            'cn-qingdao': 'resellertrade.aliyuncs.com',
            'cn-qingdao-nebula': 'resellertrade.aliyuncs.com',
            'cn-shanghai': 'resellertrade.aliyuncs.com',
            'cn-shanghai-et15-b01': 'resellertrade.aliyuncs.com',
            'cn-shanghai-et2-b01': 'resellertrade.aliyuncs.com',
            'cn-shanghai-finance-1': 'resellertrade.aliyuncs.com',
            'cn-shanghai-inner': 'resellertrade.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'resellertrade.aliyuncs.com',
            'cn-shenzhen': 'resellertrade.aliyuncs.com',
            'cn-shenzhen-finance-1': 'resellertrade.aliyuncs.com',
            'cn-shenzhen-inner': 'resellertrade.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'resellertrade.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'resellertrade.aliyuncs.com',
            'cn-wuhan': 'resellertrade.aliyuncs.com',
            'cn-yushanfang': 'resellertrade.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'resellertrade.aliyuncs.com',
            'cn-zhangjiakou': 'resellertrade.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'resellertrade.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'resellertrade.aliyuncs.com',
            'eu-central-1': 'resellertrade.aliyuncs.com',
            'eu-west-1': 'resellertrade.aliyuncs.com',
            'eu-west-1-oxs': 'resellertrade.aliyuncs.com',
            'me-east-1': 'resellertrade.aliyuncs.com',
            'rus-west-1-pop': 'resellertrade.aliyuncs.com',
            'us-east-1': 'resellertrade.aliyuncs.com',
            'us-west-1': 'resellertrade.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('resellertrade', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_coupon_template_with_options(
        self,
        request: reseller_trade_20191227_models.CreateCouponTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.CreateCouponTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.activity_site):
            body['ActivitySite'] = request.activity_site
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.certain_money):
            body['CertainMoney'] = request.certain_money
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.commodity_type):
            body['CommodityType'] = request.commodity_type
        if not UtilClient.is_unset(request.control_type):
            body['ControlType'] = request.control_type
        if not UtilClient.is_unset(request.coupon_amount):
            body['CouponAmount'] = request.coupon_amount
        if not UtilClient.is_unset(request.coupon_end_time):
            body['CouponEndTime'] = request.coupon_end_time
        if not UtilClient.is_unset(request.coupon_fixed_type):
            body['CouponFixedType'] = request.coupon_fixed_type
        if not UtilClient.is_unset(request.coupon_start_time):
            body['CouponStartTime'] = request.coupon_start_time
        if not UtilClient.is_unset(request.coupon_type):
            body['CouponType'] = request.coupon_type
        body_flat = {}
        if not UtilClient.is_unset(request.currency):
            body_flat['Currency'] = request.currency
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.discount_rate):
            body['DiscountRate'] = request.discount_rate
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.extends_map):
            body_flat['ExtendsMap'] = request.extends_map
        if not UtilClient.is_unset(request.from_app):
            body['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.item_code_set):
            body['ItemCodeSet'] = request.item_code_set
        if not UtilClient.is_unset(request.market):
            body['Market'] = request.market
        if not UtilClient.is_unset(request.market_type):
            body['MarketType'] = request.market_type
        if not UtilClient.is_unset(request.max_release):
            body['MaxRelease'] = request.max_release
        if not UtilClient.is_unset(request.message_id):
            body['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.order_type_set):
            body['OrderTypeSet'] = request.order_type_set
        if not UtilClient.is_unset(request.per_limit_num):
            body['PerLimitNum'] = request.per_limit_num
        if not UtilClient.is_unset(request.promotion_id):
            body['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.relative_second):
            body['RelativeSecond'] = request.relative_second
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.selection_id_set):
            body['SelectionIdSet'] = request.selection_id_set
        if not UtilClient.is_unset(request.seller_id):
            body['SellerId'] = request.seller_id
        if not UtilClient.is_unset(request.site):
            body['Site'] = request.site
        if not UtilClient.is_unset(request.sp_id):
            body['SpId'] = request.sp_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.universal_type):
            body['UniversalType'] = request.universal_type
        if not UtilClient.is_unset(request.upper_limit):
            body['UpperLimit'] = request.upper_limit
        if not UtilClient.is_unset(request.usage_count):
            body['UsageCount'] = request.usage_count
        if not UtilClient.is_unset(request.use_scene):
            body['UseScene'] = request.use_scene
        if not UtilClient.is_unset(request.user_pk_amount):
            body['UserPkAmount'] = request.user_pk_amount
        if not UtilClient.is_unset(request.validity_type):
            body['ValidityType'] = request.validity_type
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCouponTemplate',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.CreateCouponTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_coupon_template_with_options_async(
        self,
        request: reseller_trade_20191227_models.CreateCouponTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.CreateCouponTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.activity_site):
            body['ActivitySite'] = request.activity_site
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.certain_money):
            body['CertainMoney'] = request.certain_money
        if not UtilClient.is_unset(request.client_type):
            body['ClientType'] = request.client_type
        if not UtilClient.is_unset(request.commodity_type):
            body['CommodityType'] = request.commodity_type
        if not UtilClient.is_unset(request.control_type):
            body['ControlType'] = request.control_type
        if not UtilClient.is_unset(request.coupon_amount):
            body['CouponAmount'] = request.coupon_amount
        if not UtilClient.is_unset(request.coupon_end_time):
            body['CouponEndTime'] = request.coupon_end_time
        if not UtilClient.is_unset(request.coupon_fixed_type):
            body['CouponFixedType'] = request.coupon_fixed_type
        if not UtilClient.is_unset(request.coupon_start_time):
            body['CouponStartTime'] = request.coupon_start_time
        if not UtilClient.is_unset(request.coupon_type):
            body['CouponType'] = request.coupon_type
        body_flat = {}
        if not UtilClient.is_unset(request.currency):
            body_flat['Currency'] = request.currency
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.discount_rate):
            body['DiscountRate'] = request.discount_rate
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.extends_map):
            body_flat['ExtendsMap'] = request.extends_map
        if not UtilClient.is_unset(request.from_app):
            body['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.item_code_set):
            body['ItemCodeSet'] = request.item_code_set
        if not UtilClient.is_unset(request.market):
            body['Market'] = request.market
        if not UtilClient.is_unset(request.market_type):
            body['MarketType'] = request.market_type
        if not UtilClient.is_unset(request.max_release):
            body['MaxRelease'] = request.max_release
        if not UtilClient.is_unset(request.message_id):
            body['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.order_type_set):
            body['OrderTypeSet'] = request.order_type_set
        if not UtilClient.is_unset(request.per_limit_num):
            body['PerLimitNum'] = request.per_limit_num
        if not UtilClient.is_unset(request.promotion_id):
            body['PromotionId'] = request.promotion_id
        if not UtilClient.is_unset(request.reason):
            body['Reason'] = request.reason
        if not UtilClient.is_unset(request.relative_second):
            body['RelativeSecond'] = request.relative_second
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.selection_id_set):
            body['SelectionIdSet'] = request.selection_id_set
        if not UtilClient.is_unset(request.seller_id):
            body['SellerId'] = request.seller_id
        if not UtilClient.is_unset(request.site):
            body['Site'] = request.site
        if not UtilClient.is_unset(request.sp_id):
            body['SpId'] = request.sp_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.universal_type):
            body['UniversalType'] = request.universal_type
        if not UtilClient.is_unset(request.upper_limit):
            body['UpperLimit'] = request.upper_limit
        if not UtilClient.is_unset(request.usage_count):
            body['UsageCount'] = request.usage_count
        if not UtilClient.is_unset(request.use_scene):
            body['UseScene'] = request.use_scene
        if not UtilClient.is_unset(request.user_pk_amount):
            body['UserPkAmount'] = request.user_pk_amount
        if not UtilClient.is_unset(request.validity_type):
            body['ValidityType'] = request.validity_type
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCouponTemplate',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.CreateCouponTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_coupon_template(
        self,
        request: reseller_trade_20191227_models.CreateCouponTemplateRequest,
    ) -> reseller_trade_20191227_models.CreateCouponTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_coupon_template_with_options(request, runtime)

    async def create_coupon_template_async(
        self,
        request: reseller_trade_20191227_models.CreateCouponTemplateRequest,
    ) -> reseller_trade_20191227_models.CreateCouponTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_coupon_template_with_options_async(request, runtime)

    def discard_coupon_list_with_options(
        self,
        request: reseller_trade_20191227_models.DiscardCouponListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.DiscardCouponListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.coupon_list):
            body['CouponList'] = request.coupon_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DiscardCouponList',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.DiscardCouponListResponse(),
            self.call_api(params, req, runtime)
        )

    async def discard_coupon_list_with_options_async(
        self,
        request: reseller_trade_20191227_models.DiscardCouponListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.DiscardCouponListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.coupon_list):
            body['CouponList'] = request.coupon_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DiscardCouponList',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.DiscardCouponListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def discard_coupon_list(
        self,
        request: reseller_trade_20191227_models.DiscardCouponListRequest,
    ) -> reseller_trade_20191227_models.DiscardCouponListResponse:
        runtime = util_models.RuntimeOptions()
        return self.discard_coupon_list_with_options(request, runtime)

    async def discard_coupon_list_async(
        self,
        request: reseller_trade_20191227_models.DiscardCouponListRequest,
    ) -> reseller_trade_20191227_models.DiscardCouponListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.discard_coupon_list_with_options_async(request, runtime)

    def get_coupon_page_with_options(
        self,
        request: reseller_trade_20191227_models.GetCouponPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.GetCouponPageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCouponPage',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.GetCouponPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_coupon_page_with_options_async(
        self,
        request: reseller_trade_20191227_models.GetCouponPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.GetCouponPageResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCouponPage',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.GetCouponPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_coupon_page(
        self,
        request: reseller_trade_20191227_models.GetCouponPageRequest,
    ) -> reseller_trade_20191227_models.GetCouponPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_coupon_page_with_options(request, runtime)

    async def get_coupon_page_async(
        self,
        request: reseller_trade_20191227_models.GetCouponPageRequest,
    ) -> reseller_trade_20191227_models.GetCouponPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_coupon_page_with_options_async(request, runtime)

    def get_customer_list_with_options(
        self,
        request: reseller_trade_20191227_models.GetCustomerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.GetCustomerListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomerList',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.GetCustomerListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customer_list_with_options_async(
        self,
        request: reseller_trade_20191227_models.GetCustomerListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.GetCustomerListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomerList',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.GetCustomerListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customer_list(
        self,
        request: reseller_trade_20191227_models.GetCustomerListRequest,
    ) -> reseller_trade_20191227_models.GetCustomerListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_customer_list_with_options(request, runtime)

    async def get_customer_list_async(
        self,
        request: reseller_trade_20191227_models.GetCustomerListRequest,
    ) -> reseller_trade_20191227_models.GetCustomerListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_customer_list_with_options_async(request, runtime)

    def get_relation_with_options(
        self,
        request: reseller_trade_20191227_models.GetRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.GetRelationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRelation',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.GetRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_relation_with_options_async(
        self,
        request: reseller_trade_20191227_models.GetRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.GetRelationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRelation',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.GetRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_relation(
        self,
        request: reseller_trade_20191227_models.GetRelationRequest,
    ) -> reseller_trade_20191227_models.GetRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_relation_with_options(request, runtime)

    async def get_relation_async(
        self,
        request: reseller_trade_20191227_models.GetRelationRequest,
    ) -> reseller_trade_20191227_models.GetRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_relation_with_options_async(request, runtime)

    def get_reseller_pay_order_with_options(
        self,
        request: reseller_trade_20191227_models.GetResellerPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.GetResellerPayOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResellerPayOrder',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.GetResellerPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_reseller_pay_order_with_options_async(
        self,
        request: reseller_trade_20191227_models.GetResellerPayOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.GetResellerPayOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResellerPayOrder',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.GetResellerPayOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_reseller_pay_order(
        self,
        request: reseller_trade_20191227_models.GetResellerPayOrderRequest,
    ) -> reseller_trade_20191227_models.GetResellerPayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_reseller_pay_order_with_options(request, runtime)

    async def get_reseller_pay_order_async(
        self,
        request: reseller_trade_20191227_models.GetResellerPayOrderRequest,
    ) -> reseller_trade_20191227_models.GetResellerPayOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_reseller_pay_order_with_options_async(request, runtime)

    def label_partner_user_with_options(
        self,
        request: reseller_trade_20191227_models.LabelPartnerUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.LabelPartnerUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_pk):
            body['UserPK'] = request.user_pk
        if not UtilClient.is_unset(request.user_tag):
            body['UserTag'] = request.user_tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LabelPartnerUser',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.LabelPartnerUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def label_partner_user_with_options_async(
        self,
        request: reseller_trade_20191227_models.LabelPartnerUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.LabelPartnerUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.user_pk):
            body['UserPK'] = request.user_pk
        if not UtilClient.is_unset(request.user_tag):
            body['UserTag'] = request.user_tag
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LabelPartnerUser',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.LabelPartnerUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def label_partner_user(
        self,
        request: reseller_trade_20191227_models.LabelPartnerUserRequest,
    ) -> reseller_trade_20191227_models.LabelPartnerUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.label_partner_user_with_options(request, runtime)

    async def label_partner_user_async(
        self,
        request: reseller_trade_20191227_models.LabelPartnerUserRequest,
    ) -> reseller_trade_20191227_models.LabelPartnerUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.label_partner_user_with_options_async(request, runtime)

    def migrate_resource_with_options(
        self,
        request: reseller_trade_20191227_models.MigrateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.MigrateResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_code):
            body['ActionCode'] = request.action_code
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MigrateResource',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.MigrateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_resource_with_options_async(
        self,
        request: reseller_trade_20191227_models.MigrateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.MigrateResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_code):
            body['ActionCode'] = request.action_code
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MigrateResource',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.MigrateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_resource(
        self,
        request: reseller_trade_20191227_models.MigrateResourceRequest,
    ) -> reseller_trade_20191227_models.MigrateResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_resource_with_options(request, runtime)

    async def migrate_resource_async(
        self,
        request: reseller_trade_20191227_models.MigrateResourceRequest,
    ) -> reseller_trade_20191227_models.MigrateResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_resource_with_options_async(request, runtime)

    def offline_activity_with_options(
        self,
        request: reseller_trade_20191227_models.OfflineActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.OfflineActivityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.activity_list):
            body['ActivityList'] = request.activity_list
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineActivity',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.OfflineActivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_activity_with_options_async(
        self,
        request: reseller_trade_20191227_models.OfflineActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.OfflineActivityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.activity_list):
            body['ActivityList'] = request.activity_list
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OfflineActivity',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.OfflineActivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_activity(
        self,
        request: reseller_trade_20191227_models.OfflineActivityRequest,
    ) -> reseller_trade_20191227_models.OfflineActivityResponse:
        runtime = util_models.RuntimeOptions()
        return self.offline_activity_with_options(request, runtime)

    async def offline_activity_async(
        self,
        request: reseller_trade_20191227_models.OfflineActivityRequest,
    ) -> reseller_trade_20191227_models.OfflineActivityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.offline_activity_with_options_async(request, runtime)

    def pay_result_callback_with_options(
        self,
        request: reseller_trade_20191227_models.PayResultCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.PayResultCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.pay_status):
            query['PayStatus'] = request.pay_status
        if not UtilClient.is_unset(request.pay_time):
            query['PayTime'] = request.pay_time
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PayResultCallback',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.PayResultCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def pay_result_callback_with_options_async(
        self,
        request: reseller_trade_20191227_models.PayResultCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.PayResultCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.pay_status):
            query['PayStatus'] = request.pay_status
        if not UtilClient.is_unset(request.pay_time):
            query['PayTime'] = request.pay_time
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PayResultCallback',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.PayResultCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pay_result_callback(
        self,
        request: reseller_trade_20191227_models.PayResultCallbackRequest,
    ) -> reseller_trade_20191227_models.PayResultCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.pay_result_callback_with_options(request, runtime)

    async def pay_result_callback_async(
        self,
        request: reseller_trade_20191227_models.PayResultCallbackRequest,
    ) -> reseller_trade_20191227_models.PayResultCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pay_result_callback_with_options_async(request, runtime)

    def public_activity_with_options(
        self,
        request: reseller_trade_20191227_models.PublicActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.PublicActivityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.activity_list):
            body['ActivityList'] = request.activity_list
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.snap_type):
            body['SnapType'] = request.snap_type
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublicActivity',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.PublicActivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def public_activity_with_options_async(
        self,
        request: reseller_trade_20191227_models.PublicActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.PublicActivityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.activity_list):
            body['ActivityList'] = request.activity_list
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.snap_type):
            body['SnapType'] = request.snap_type
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublicActivity',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.PublicActivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def public_activity(
        self,
        request: reseller_trade_20191227_models.PublicActivityRequest,
    ) -> reseller_trade_20191227_models.PublicActivityResponse:
        runtime = util_models.RuntimeOptions()
        return self.public_activity_with_options(request, runtime)

    async def public_activity_async(
        self,
        request: reseller_trade_20191227_models.PublicActivityRequest,
    ) -> reseller_trade_20191227_models.PublicActivityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.public_activity_with_options_async(request, runtime)

    def query_activity_with_options(
        self,
        request: reseller_trade_20191227_models.QueryActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.QueryActivityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.activity_id):
            body['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.snap_type):
            body['SnapType'] = request.snap_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryActivity',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.QueryActivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_activity_with_options_async(
        self,
        request: reseller_trade_20191227_models.QueryActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.QueryActivityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.activity_id):
            body['ActivityId'] = request.activity_id
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.snap_type):
            body['SnapType'] = request.snap_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryActivity',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.QueryActivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_activity(
        self,
        request: reseller_trade_20191227_models.QueryActivityRequest,
    ) -> reseller_trade_20191227_models.QueryActivityResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_activity_with_options(request, runtime)

    async def query_activity_async(
        self,
        request: reseller_trade_20191227_models.QueryActivityRequest,
    ) -> reseller_trade_20191227_models.QueryActivityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_activity_with_options_async(request, runtime)

    def query_eco_relation_with_options(
        self,
        request: reseller_trade_20191227_models.QueryEcoRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.QueryEcoRelationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.relation_time):
            body['RelationTime'] = request.relation_time
        if not UtilClient.is_unset(request.uid):
            body['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryEcoRelation',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.QueryEcoRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_eco_relation_with_options_async(
        self,
        request: reseller_trade_20191227_models.QueryEcoRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.QueryEcoRelationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.relation_time):
            body['RelationTime'] = request.relation_time
        if not UtilClient.is_unset(request.uid):
            body['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryEcoRelation',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.QueryEcoRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_eco_relation(
        self,
        request: reseller_trade_20191227_models.QueryEcoRelationRequest,
    ) -> reseller_trade_20191227_models.QueryEcoRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_eco_relation_with_options(request, runtime)

    async def query_eco_relation_async(
        self,
        request: reseller_trade_20191227_models.QueryEcoRelationRequest,
    ) -> reseller_trade_20191227_models.QueryEcoRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_eco_relation_with_options_async(request, runtime)

    def save_activity_with_options(
        self,
        tmp_req: reseller_trade_20191227_models.SaveActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.SaveActivityResponse:
        UtilClient.validate_model(tmp_req)
        request = reseller_trade_20191227_models.SaveActivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_map):
            request.extend_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_map, 'ExtendMap', 'json')
        body = {}
        if not UtilClient.is_unset(request.activity_name):
            body['ActivityName'] = request.activity_name
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.black_uid_list):
            body['BlackUidList'] = request.black_uid_list
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.extend_map_shrink):
            body['ExtendMap'] = request.extend_map_shrink
        if not UtilClient.is_unset(request.fusion_promotion_param_list):
            body['FusionPromotionParamList'] = request.fusion_promotion_param_list
        if not UtilClient.is_unset(request.publish_tag):
            body['PublishTag'] = request.publish_tag
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.test_account_uid_list):
            body['TestAccountUidList'] = request.test_account_uid_list
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.white_uid_list):
            body['WhiteUidList'] = request.white_uid_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveActivity',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.SaveActivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_activity_with_options_async(
        self,
        tmp_req: reseller_trade_20191227_models.SaveActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.SaveActivityResponse:
        UtilClient.validate_model(tmp_req)
        request = reseller_trade_20191227_models.SaveActivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extend_map):
            request.extend_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_map, 'ExtendMap', 'json')
        body = {}
        if not UtilClient.is_unset(request.activity_name):
            body['ActivityName'] = request.activity_name
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.black_uid_list):
            body['BlackUidList'] = request.black_uid_list
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.extend_map_shrink):
            body['ExtendMap'] = request.extend_map_shrink
        if not UtilClient.is_unset(request.fusion_promotion_param_list):
            body['FusionPromotionParamList'] = request.fusion_promotion_param_list
        if not UtilClient.is_unset(request.publish_tag):
            body['PublishTag'] = request.publish_tag
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.test_account_uid_list):
            body['TestAccountUidList'] = request.test_account_uid_list
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.white_uid_list):
            body['WhiteUidList'] = request.white_uid_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveActivity',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.SaveActivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_activity(
        self,
        request: reseller_trade_20191227_models.SaveActivityRequest,
    ) -> reseller_trade_20191227_models.SaveActivityResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_activity_with_options(request, runtime)

    async def save_activity_async(
        self,
        request: reseller_trade_20191227_models.SaveActivityRequest,
    ) -> reseller_trade_20191227_models.SaveActivityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_activity_with_options_async(request, runtime)

    def send_coupon_with_options(
        self,
        request: reseller_trade_20191227_models.SendCouponRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.SendCouponResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.from_app):
            body['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.seller_id):
            body['SellerId'] = request.seller_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_amount_model_list):
            body['UserAmountModelList'] = request.user_amount_model_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCoupon',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.SendCouponResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_coupon_with_options_async(
        self,
        request: reseller_trade_20191227_models.SendCouponRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.SendCouponResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bid):
            body['Bid'] = request.bid
        if not UtilClient.is_unset(request.from_app):
            body['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.operator):
            body['Operator'] = request.operator
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.seller_id):
            body['SellerId'] = request.seller_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_amount_model_list):
            body['UserAmountModelList'] = request.user_amount_model_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendCoupon',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.SendCouponResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_coupon(
        self,
        request: reseller_trade_20191227_models.SendCouponRequest,
    ) -> reseller_trade_20191227_models.SendCouponResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_coupon_with_options(request, runtime)

    async def send_coupon_async(
        self,
        request: reseller_trade_20191227_models.SendCouponRequest,
    ) -> reseller_trade_20191227_models.SendCouponResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_coupon_with_options_async(request, runtime)

    def transfer_resource_with_options(
        self,
        request: reseller_trade_20191227_models.TransferResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.TransferResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_code):
            body['ActionCode'] = request.action_code
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TransferResource',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.TransferResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_resource_with_options_async(
        self,
        request: reseller_trade_20191227_models.TransferResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> reseller_trade_20191227_models.TransferResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.action_code):
            body['ActionCode'] = request.action_code
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TransferResource',
            version='2019-12-27',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            reseller_trade_20191227_models.TransferResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_resource(
        self,
        request: reseller_trade_20191227_models.TransferResourceRequest,
    ) -> reseller_trade_20191227_models.TransferResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.transfer_resource_with_options(request, runtime)

    async def transfer_resource_async(
        self,
        request: reseller_trade_20191227_models.TransferResourceRequest,
    ) -> reseller_trade_20191227_models.TransferResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_resource_with_options_async(request, runtime)
