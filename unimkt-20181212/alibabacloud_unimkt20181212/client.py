# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_unimkt20181212 import models as main_models
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
            'cn-hangzhou': 'cloudcode.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'cloudcode.cn-shanghai.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('unimkt', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_proxy_brand_user_with_options(
        self,
        request: main_models.CreateProxyBrandUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProxyBrandUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_user_nick):
            query['BrandUserNick'] = request.brand_user_nick
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.company):
            query['Company'] = request.company
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.contact_phone):
            query['ContactPhone'] = request.contact_phone
        if not DaraCore.is_null(request.industry):
            query['Industry'] = request.industry
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProxyBrandUser',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProxyBrandUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_proxy_brand_user_with_options_async(
        self,
        request: main_models.CreateProxyBrandUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProxyBrandUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_user_nick):
            query['BrandUserNick'] = request.brand_user_nick
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.company):
            query['Company'] = request.company
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.contact_phone):
            query['ContactPhone'] = request.contact_phone
        if not DaraCore.is_null(request.industry):
            query['Industry'] = request.industry
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProxyBrandUser',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProxyBrandUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_proxy_brand_user(
        self,
        request: main_models.CreateProxyBrandUserRequest,
    ) -> main_models.CreateProxyBrandUserResponse:
        runtime = RuntimeOptions()
        return self.create_proxy_brand_user_with_options(request, runtime)

    async def create_proxy_brand_user_async(
        self,
        request: main_models.CreateProxyBrandUserRequest,
    ) -> main_models.CreateProxyBrandUserResponse:
        runtime = RuntimeOptions()
        return await self.create_proxy_brand_user_with_options_async(request, runtime)

    def create_union_task_with_options(
        self,
        tmp_req: main_models.CreateUnionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUnionTaskResponse:
        tmp_req.validate()
        request = main_models.CreateUnionTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.media_id_black_list):
            request.media_id_black_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.media_id_black_list, 'MediaIdBlackList', 'json')
        if not DaraCore.is_null(tmp_req.media_id_white_list):
            request.media_id_white_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.media_id_white_list, 'MediaIdWhiteList', 'json')
        query = {}
        if not DaraCore.is_null(request.anchor_id):
            query['AnchorId'] = request.anchor_id
        if not DaraCore.is_null(request.brand_user_id):
            query['BrandUserId'] = request.brand_user_id
        if not DaraCore.is_null(request.brand_user_nick):
            query['BrandUserNick'] = request.brand_user_nick
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.charge_ploy):
            query['ChargePloy'] = request.charge_ploy
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.content_id):
            query['ContentId'] = request.content_id
        if not DaraCore.is_null(request.content_url):
            query['ContentUrl'] = request.content_url
        if not DaraCore.is_null(request.custom_creative_type):
            query['CustomCreativeType'] = request.custom_creative_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.industry_label_bag_id):
            query['IndustryLabelBagId'] = request.industry_label_bag_id
        if not DaraCore.is_null(request.media_id_black_list_shrink):
            query['MediaIdBlackList'] = request.media_id_black_list_shrink
        if not DaraCore.is_null(request.media_id_white_list_shrink):
            query['MediaIdWhiteList'] = request.media_id_white_list_shrink
        if not DaraCore.is_null(request.media_industry):
            query['MediaIndustry'] = request.media_industry
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.optimization_switch):
            query['OptimizationSwitch'] = request.optimization_switch
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.quota):
            query['Quota'] = request.quota
        if not DaraCore.is_null(request.quota_day):
            query['QuotaDay'] = request.quota_day
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_biz_type):
            query['TaskBizType'] = request.task_biz_type
        if not DaraCore.is_null(request.task_rule_type):
            query['TaskRuleType'] = request.task_rule_type
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUnionTask',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUnionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_union_task_with_options_async(
        self,
        tmp_req: main_models.CreateUnionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUnionTaskResponse:
        tmp_req.validate()
        request = main_models.CreateUnionTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.media_id_black_list):
            request.media_id_black_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.media_id_black_list, 'MediaIdBlackList', 'json')
        if not DaraCore.is_null(tmp_req.media_id_white_list):
            request.media_id_white_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.media_id_white_list, 'MediaIdWhiteList', 'json')
        query = {}
        if not DaraCore.is_null(request.anchor_id):
            query['AnchorId'] = request.anchor_id
        if not DaraCore.is_null(request.brand_user_id):
            query['BrandUserId'] = request.brand_user_id
        if not DaraCore.is_null(request.brand_user_nick):
            query['BrandUserNick'] = request.brand_user_nick
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.charge_ploy):
            query['ChargePloy'] = request.charge_ploy
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.content_id):
            query['ContentId'] = request.content_id
        if not DaraCore.is_null(request.content_url):
            query['ContentUrl'] = request.content_url
        if not DaraCore.is_null(request.custom_creative_type):
            query['CustomCreativeType'] = request.custom_creative_type
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.industry_label_bag_id):
            query['IndustryLabelBagId'] = request.industry_label_bag_id
        if not DaraCore.is_null(request.media_id_black_list_shrink):
            query['MediaIdBlackList'] = request.media_id_black_list_shrink
        if not DaraCore.is_null(request.media_id_white_list_shrink):
            query['MediaIdWhiteList'] = request.media_id_white_list_shrink
        if not DaraCore.is_null(request.media_industry):
            query['MediaIndustry'] = request.media_industry
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.optimization_switch):
            query['OptimizationSwitch'] = request.optimization_switch
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.quota):
            query['Quota'] = request.quota
        if not DaraCore.is_null(request.quota_day):
            query['QuotaDay'] = request.quota_day
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_biz_type):
            query['TaskBizType'] = request.task_biz_type
        if not DaraCore.is_null(request.task_rule_type):
            query['TaskRuleType'] = request.task_rule_type
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUnionTask',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUnionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_union_task(
        self,
        request: main_models.CreateUnionTaskRequest,
    ) -> main_models.CreateUnionTaskResponse:
        runtime = RuntimeOptions()
        return self.create_union_task_with_options(request, runtime)

    async def create_union_task_async(
        self,
        request: main_models.CreateUnionTaskRequest,
    ) -> main_models.CreateUnionTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_union_task_with_options_async(request, runtime)

    def delete_union_brand_with_options(
        self,
        request: main_models.DeleteUnionBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUnionBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_main_id):
            query['BrandMainId'] = request.brand_main_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUnionBrand',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUnionBrandResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_union_brand_with_options_async(
        self,
        request: main_models.DeleteUnionBrandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUnionBrandResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_main_id):
            query['BrandMainId'] = request.brand_main_id
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUnionBrand',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUnionBrandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_union_brand(
        self,
        request: main_models.DeleteUnionBrandRequest,
    ) -> main_models.DeleteUnionBrandResponse:
        runtime = RuntimeOptions()
        return self.delete_union_brand_with_options(request, runtime)

    async def delete_union_brand_async(
        self,
        request: main_models.DeleteUnionBrandRequest,
    ) -> main_models.DeleteUnionBrandResponse:
        runtime = RuntimeOptions()
        return await self.delete_union_brand_with_options_async(request, runtime)

    def end_union_task_with_options(
        self,
        request: main_models.EndUnionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EndUnionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EndUnionTask',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EndUnionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def end_union_task_with_options_async(
        self,
        request: main_models.EndUnionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EndUnionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EndUnionTask',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EndUnionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def end_union_task(
        self,
        request: main_models.EndUnionTaskRequest,
    ) -> main_models.EndUnionTaskResponse:
        runtime = RuntimeOptions()
        return self.end_union_task_with_options(request, runtime)

    async def end_union_task_async(
        self,
        request: main_models.EndUnionTaskRequest,
    ) -> main_models.EndUnionTaskResponse:
        runtime = RuntimeOptions()
        return await self.end_union_task_with_options_async(request, runtime)

    def list_union_media_industry_with_options(
        self,
        request: main_models.ListUnionMediaIndustryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUnionMediaIndustryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUnionMediaIndustry',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUnionMediaIndustryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_union_media_industry_with_options_async(
        self,
        request: main_models.ListUnionMediaIndustryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUnionMediaIndustryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUnionMediaIndustry',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUnionMediaIndustryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_union_media_industry(
        self,
        request: main_models.ListUnionMediaIndustryRequest,
    ) -> main_models.ListUnionMediaIndustryResponse:
        runtime = RuntimeOptions()
        return self.list_union_media_industry_with_options(request, runtime)

    async def list_union_media_industry_async(
        self,
        request: main_models.ListUnionMediaIndustryRequest,
    ) -> main_models.ListUnionMediaIndustryResponse:
        runtime = RuntimeOptions()
        return await self.list_union_media_industry_with_options_async(request, runtime)

    def query_available_balance_with_options(
        self,
        request: main_models.QueryAvailableBalanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvailableBalanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAvailableBalance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvailableBalanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_available_balance_with_options_async(
        self,
        request: main_models.QueryAvailableBalanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAvailableBalanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAvailableBalance',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAvailableBalanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_available_balance(
        self,
        request: main_models.QueryAvailableBalanceRequest,
    ) -> main_models.QueryAvailableBalanceResponse:
        runtime = RuntimeOptions()
        return self.query_available_balance_with_options(request, runtime)

    async def query_available_balance_async(
        self,
        request: main_models.QueryAvailableBalanceRequest,
    ) -> main_models.QueryAvailableBalanceResponse:
        runtime = RuntimeOptions()
        return await self.query_available_balance_with_options_async(request, runtime)

    def query_content_list_with_options(
        self,
        request: main_models.QueryContentListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryContentListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_user_id):
            query['BrandUserId'] = request.brand_user_id
        if not DaraCore.is_null(request.brand_user_nick):
            query['BrandUserNick'] = request.brand_user_nick
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.task_biz_type):
            query['TaskBizType'] = request.task_biz_type
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryContentList',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryContentListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_content_list_with_options_async(
        self,
        request: main_models.QueryContentListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryContentListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_user_id):
            query['BrandUserId'] = request.brand_user_id
        if not DaraCore.is_null(request.brand_user_nick):
            query['BrandUserNick'] = request.brand_user_nick
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.task_biz_type):
            query['TaskBizType'] = request.task_biz_type
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryContentList',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryContentListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_content_list(
        self,
        request: main_models.QueryContentListRequest,
    ) -> main_models.QueryContentListResponse:
        runtime = RuntimeOptions()
        return self.query_content_list_with_options(request, runtime)

    async def query_content_list_async(
        self,
        request: main_models.QueryContentListRequest,
    ) -> main_models.QueryContentListResponse:
        runtime = RuntimeOptions()
        return await self.query_content_list_with_options_async(request, runtime)

    def query_industry_label_bag_with_options(
        self,
        request: main_models.QueryIndustryLabelBagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryIndustryLabelBagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryIndustryLabelBag',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryIndustryLabelBagResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_industry_label_bag_with_options_async(
        self,
        request: main_models.QueryIndustryLabelBagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryIndustryLabelBagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryIndustryLabelBag',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryIndustryLabelBagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_industry_label_bag(
        self,
        request: main_models.QueryIndustryLabelBagRequest,
    ) -> main_models.QueryIndustryLabelBagResponse:
        runtime = RuntimeOptions()
        return self.query_industry_label_bag_with_options(request, runtime)

    async def query_industry_label_bag_async(
        self,
        request: main_models.QueryIndustryLabelBagRequest,
    ) -> main_models.QueryIndustryLabelBagResponse:
        runtime = RuntimeOptions()
        return await self.query_industry_label_bag_with_options_async(request, runtime)

    def query_task_biz_type_with_options(
        self,
        request: main_models.QueryTaskBizTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskBizTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskBizType',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskBizTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_biz_type_with_options_async(
        self,
        request: main_models.QueryTaskBizTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskBizTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskBizType',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskBizTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_biz_type(
        self,
        request: main_models.QueryTaskBizTypeRequest,
    ) -> main_models.QueryTaskBizTypeResponse:
        runtime = RuntimeOptions()
        return self.query_task_biz_type_with_options(request, runtime)

    async def query_task_biz_type_async(
        self,
        request: main_models.QueryTaskBizTypeRequest,
    ) -> main_models.QueryTaskBizTypeResponse:
        runtime = RuntimeOptions()
        return await self.query_task_biz_type_with_options_async(request, runtime)

    def query_task_rule_limit_with_options(
        self,
        request: main_models.QueryTaskRuleLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskRuleLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskRuleLimit',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskRuleLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_task_rule_limit_with_options_async(
        self,
        request: main_models.QueryTaskRuleLimitRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryTaskRuleLimitResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryTaskRuleLimit',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryTaskRuleLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_task_rule_limit(
        self,
        request: main_models.QueryTaskRuleLimitRequest,
    ) -> main_models.QueryTaskRuleLimitResponse:
        runtime = RuntimeOptions()
        return self.query_task_rule_limit_with_options(request, runtime)

    async def query_task_rule_limit_async(
        self,
        request: main_models.QueryTaskRuleLimitRequest,
    ) -> main_models.QueryTaskRuleLimitResponse:
        runtime = RuntimeOptions()
        return await self.query_task_rule_limit_with_options_async(request, runtime)

    def query_union_channel_with_options(
        self,
        request: main_models.QueryUnionChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUnionChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUnionChannel',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUnionChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_union_channel_with_options_async(
        self,
        request: main_models.QueryUnionChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUnionChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUnionChannel',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUnionChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_union_channel(
        self,
        request: main_models.QueryUnionChannelRequest,
    ) -> main_models.QueryUnionChannelResponse:
        runtime = RuntimeOptions()
        return self.query_union_channel_with_options(request, runtime)

    async def query_union_channel_async(
        self,
        request: main_models.QueryUnionChannelRequest,
    ) -> main_models.QueryUnionChannelResponse:
        runtime = RuntimeOptions()
        return await self.query_union_channel_with_options_async(request, runtime)

    def query_union_content_info_with_options(
        self,
        request: main_models.QueryUnionContentInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUnionContentInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.content_id):
            query['ContentId'] = request.content_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUnionContentInfo',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUnionContentInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_union_content_info_with_options_async(
        self,
        request: main_models.QueryUnionContentInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUnionContentInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.content_id):
            query['ContentId'] = request.content_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUnionContentInfo',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUnionContentInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_union_content_info(
        self,
        request: main_models.QueryUnionContentInfoRequest,
    ) -> main_models.QueryUnionContentInfoResponse:
        runtime = RuntimeOptions()
        return self.query_union_content_info_with_options(request, runtime)

    async def query_union_content_info_async(
        self,
        request: main_models.QueryUnionContentInfoRequest,
    ) -> main_models.QueryUnionContentInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_union_content_info_with_options_async(request, runtime)

    def query_union_task_info_with_options(
        self,
        request: main_models.QueryUnionTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUnionTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUnionTaskInfo',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUnionTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_union_task_info_with_options_async(
        self,
        request: main_models.QueryUnionTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUnionTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUnionTaskInfo',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUnionTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_union_task_info(
        self,
        request: main_models.QueryUnionTaskInfoRequest,
    ) -> main_models.QueryUnionTaskInfoResponse:
        runtime = RuntimeOptions()
        return self.query_union_task_info_with_options(request, runtime)

    async def query_union_task_info_async(
        self,
        request: main_models.QueryUnionTaskInfoRequest,
    ) -> main_models.QueryUnionTaskInfoResponse:
        runtime = RuntimeOptions()
        return await self.query_union_task_info_with_options_async(request, runtime)

    def query_union_task_list_with_options(
        self,
        request: main_models.QueryUnionTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUnionTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_user_id):
            query['BrandUserId'] = request.brand_user_id
        if not DaraCore.is_null(request.brand_user_nick):
            query['BrandUserNick'] = request.brand_user_nick
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUnionTaskList',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUnionTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_union_task_list_with_options_async(
        self,
        request: main_models.QueryUnionTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryUnionTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.brand_user_id):
            query['BrandUserId'] = request.brand_user_id
        if not DaraCore.is_null(request.brand_user_nick):
            query['BrandUserNick'] = request.brand_user_nick
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryUnionTaskList',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryUnionTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_union_task_list(
        self,
        request: main_models.QueryUnionTaskListRequest,
    ) -> main_models.QueryUnionTaskListResponse:
        runtime = RuntimeOptions()
        return self.query_union_task_list_with_options(request, runtime)

    async def query_union_task_list_async(
        self,
        request: main_models.QueryUnionTaskListRequest,
    ) -> main_models.QueryUnionTaskListResponse:
        runtime = RuntimeOptions()
        return await self.query_union_task_list_with_options_async(request, runtime)

    def start_union_task_with_options(
        self,
        request: main_models.StartUnionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartUnionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartUnionTask',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartUnionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_union_task_with_options_async(
        self,
        request: main_models.StartUnionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartUnionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartUnionTask',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartUnionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_union_task(
        self,
        request: main_models.StartUnionTaskRequest,
    ) -> main_models.StartUnionTaskResponse:
        runtime = RuntimeOptions()
        return self.start_union_task_with_options(request, runtime)

    async def start_union_task_async(
        self,
        request: main_models.StartUnionTaskRequest,
    ) -> main_models.StartUnionTaskResponse:
        runtime = RuntimeOptions()
        return await self.start_union_task_with_options_async(request, runtime)

    def stop_union_task_with_options(
        self,
        request: main_models.StopUnionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopUnionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopUnionTask',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopUnionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_union_task_with_options_async(
        self,
        request: main_models.StopUnionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopUnionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopUnionTask',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopUnionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_union_task(
        self,
        request: main_models.StopUnionTaskRequest,
    ) -> main_models.StopUnionTaskResponse:
        runtime = RuntimeOptions()
        return self.stop_union_task_with_options(request, runtime)

    async def stop_union_task_async(
        self,
        request: main_models.StopUnionTaskRequest,
    ) -> main_models.StopUnionTaskResponse:
        runtime = RuntimeOptions()
        return await self.stop_union_task_with_options_async(request, runtime)

    def update_union_task_with_options(
        self,
        request: main_models.UpdateUnionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUnionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.charge_ploy):
            query['ChargePloy'] = request.charge_ploy
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.optimization_switch):
            query['OptimizationSwitch'] = request.optimization_switch
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.quota):
            query['Quota'] = request.quota
        if not DaraCore.is_null(request.quota_day):
            query['QuotaDay'] = request.quota_day
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUnionTask',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUnionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_union_task_with_options_async(
        self,
        request: main_models.UpdateUnionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUnionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not DaraCore.is_null(request.charge_ploy):
            query['ChargePloy'] = request.charge_ploy
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.optimization_switch):
            query['OptimizationSwitch'] = request.optimization_switch
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.quota):
            query['Quota'] = request.quota
        if not DaraCore.is_null(request.quota_day):
            query['QuotaDay'] = request.quota_day
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUnionTask',
            version = '2018-12-12',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUnionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_union_task(
        self,
        request: main_models.UpdateUnionTaskRequest,
    ) -> main_models.UpdateUnionTaskResponse:
        runtime = RuntimeOptions()
        return self.update_union_task_with_options(request, runtime)

    async def update_union_task_async(
        self,
        request: main_models.UpdateUnionTaskRequest,
    ) -> main_models.UpdateUnionTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_union_task_with_options_async(request, runtime)
