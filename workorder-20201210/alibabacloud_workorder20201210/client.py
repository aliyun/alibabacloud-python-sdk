# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from alibabacloud_workorder20201210 import models as main_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'ap-northeast-1': 'workorder.ap-northeast-1.aliyuncs.com',
            'ap-southeast-1': 'workorder.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('workorder', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_ticket_template_with_options(
        self,
        request: main_models.GetTicketTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTicketTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.cna):
            query['Cna'] = request.cna
        if not DaraCore.is_null(request.distribution_channel):
            query['DistributionChannel'] = request.distribution_channel
        if not DaraCore.is_null(request.referrer):
            query['Referrer'] = request.referrer
        if not DaraCore.is_null(request.sub_distribution_channel):
            query['SubDistributionChannel'] = request.sub_distribution_channel
        if not DaraCore.is_null(request.xgateway_extend_info):
            query['XGatewayExtendInfo'] = request.xgateway_extend_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTicketTemplate',
            version = '2020-12-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTicketTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ticket_template_with_options_async(
        self,
        request: main_models.GetTicketTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTicketTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category_id):
            query['CategoryId'] = request.category_id
        if not DaraCore.is_null(request.cna):
            query['Cna'] = request.cna
        if not DaraCore.is_null(request.distribution_channel):
            query['DistributionChannel'] = request.distribution_channel
        if not DaraCore.is_null(request.referrer):
            query['Referrer'] = request.referrer
        if not DaraCore.is_null(request.sub_distribution_channel):
            query['SubDistributionChannel'] = request.sub_distribution_channel
        if not DaraCore.is_null(request.xgateway_extend_info):
            query['XGatewayExtendInfo'] = request.xgateway_extend_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTicketTemplate',
            version = '2020-12-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTicketTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ticket_template(
        self,
        request: main_models.GetTicketTemplateRequest,
    ) -> main_models.GetTicketTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_ticket_template_with_options(request, runtime)

    async def get_ticket_template_async(
        self,
        request: main_models.GetTicketTemplateRequest,
    ) -> main_models.GetTicketTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_ticket_template_with_options_async(request, runtime)

    def is_first_bbs_ticket_with_options(
        self,
        request: main_models.IsFirstBbsTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IsFirstBbsTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cna):
            query['Cna'] = request.cna
        if not DaraCore.is_null(request.distribution_channel):
            query['DistributionChannel'] = request.distribution_channel
        if not DaraCore.is_null(request.referrer):
            query['Referrer'] = request.referrer
        if not DaraCore.is_null(request.sub_distribution_channel):
            query['SubDistributionChannel'] = request.sub_distribution_channel
        if not DaraCore.is_null(request.xgateway_extend_info):
            query['XGatewayExtendInfo'] = request.xgateway_extend_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IsFirstBbsTicket',
            version = '2020-12-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IsFirstBbsTicketResponse(),
            self.call_api(params, req, runtime)
        )

    async def is_first_bbs_ticket_with_options_async(
        self,
        request: main_models.IsFirstBbsTicketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IsFirstBbsTicketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cna):
            query['Cna'] = request.cna
        if not DaraCore.is_null(request.distribution_channel):
            query['DistributionChannel'] = request.distribution_channel
        if not DaraCore.is_null(request.referrer):
            query['Referrer'] = request.referrer
        if not DaraCore.is_null(request.sub_distribution_channel):
            query['SubDistributionChannel'] = request.sub_distribution_channel
        if not DaraCore.is_null(request.xgateway_extend_info):
            query['XGatewayExtendInfo'] = request.xgateway_extend_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IsFirstBbsTicket',
            version = '2020-12-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IsFirstBbsTicketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def is_first_bbs_ticket(
        self,
        request: main_models.IsFirstBbsTicketRequest,
    ) -> main_models.IsFirstBbsTicketResponse:
        runtime = RuntimeOptions()
        return self.is_first_bbs_ticket_with_options(request, runtime)

    async def is_first_bbs_ticket_async(
        self,
        request: main_models.IsFirstBbsTicketRequest,
    ) -> main_models.IsFirstBbsTicketResponse:
        runtime = RuntimeOptions()
        return await self.is_first_bbs_ticket_with_options_async(request, runtime)

    def suggest_category_with_options(
        self,
        request: main_models.SuggestCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuggestCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cna):
            query['Cna'] = request.cna
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.distribution_channel):
            query['DistributionChannel'] = request.distribution_channel
        if not DaraCore.is_null(request.referrer):
            query['Referrer'] = request.referrer
        if not DaraCore.is_null(request.sub_distribution_channel):
            query['SubDistributionChannel'] = request.sub_distribution_channel
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        if not DaraCore.is_null(request.use_hot_suggest_catch_all):
            query['UseHotSuggestCatchAll'] = request.use_hot_suggest_catch_all
        if not DaraCore.is_null(request.xgateway_extend_info):
            query['XGatewayExtendInfo'] = request.xgateway_extend_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuggestCategory',
            version = '2020-12-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuggestCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def suggest_category_with_options_async(
        self,
        request: main_models.SuggestCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuggestCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cna):
            query['Cna'] = request.cna
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.distribution_channel):
            query['DistributionChannel'] = request.distribution_channel
        if not DaraCore.is_null(request.referrer):
            query['Referrer'] = request.referrer
        if not DaraCore.is_null(request.sub_distribution_channel):
            query['SubDistributionChannel'] = request.sub_distribution_channel
        if not DaraCore.is_null(request.ticket_id):
            query['TicketId'] = request.ticket_id
        if not DaraCore.is_null(request.top_n):
            query['TopN'] = request.top_n
        if not DaraCore.is_null(request.use_hot_suggest_catch_all):
            query['UseHotSuggestCatchAll'] = request.use_hot_suggest_catch_all
        if not DaraCore.is_null(request.xgateway_extend_info):
            query['XGatewayExtendInfo'] = request.xgateway_extend_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SuggestCategory',
            version = '2020-12-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuggestCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suggest_category(
        self,
        request: main_models.SuggestCategoryRequest,
    ) -> main_models.SuggestCategoryResponse:
        runtime = RuntimeOptions()
        return self.suggest_category_with_options(request, runtime)

    async def suggest_category_async(
        self,
        request: main_models.SuggestCategoryRequest,
    ) -> main_models.SuggestCategoryResponse:
        runtime = RuntimeOptions()
        return await self.suggest_category_with_options_async(request, runtime)
