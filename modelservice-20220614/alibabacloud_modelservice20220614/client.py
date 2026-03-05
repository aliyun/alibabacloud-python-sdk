# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_modelservice20220614 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('modelservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_month_amount_with_options(
        self,
        request: main_models.GetMonthAmountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMonthAmountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMonthAmount',
            version = '2022-06-14',
            protocol = 'HTTPS',
            pathname = f'/api/v1/statistics/month/amount',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonthAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_month_amount_with_options_async(
        self,
        request: main_models.GetMonthAmountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMonthAmountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMonthAmount',
            version = '2022-06-14',
            protocol = 'HTTPS',
            pathname = f'/api/v1/statistics/month/amount',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonthAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_month_amount(
        self,
        request: main_models.GetMonthAmountRequest,
    ) -> main_models.GetMonthAmountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_month_amount_with_options(request, headers, runtime)

    async def get_month_amount_async(
        self,
        request: main_models.GetMonthAmountRequest,
    ) -> main_models.GetMonthAmountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_month_amount_with_options_async(request, headers, runtime)

    def get_user_with_options(
        self,
        request: main_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2022-06-14',
            protocol = 'HTTPS',
            pathname = f'/api/v1/user/info',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: main_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2022-06-14',
            protocol = 'HTTPS',
            pathname = f'/api/v1/user/info',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_with_options(request, headers, runtime)

    async def get_user_async(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(request, headers, runtime)

    def list_day_amount_with_options(
        self,
        request: main_models.ListDayAmountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDayAmountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.scene_type):
            query['SceneType'] = request.scene_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDayAmount',
            version = '2022-06-14',
            protocol = 'HTTPS',
            pathname = f'/api/v1/statistics/day/amount',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDayAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_day_amount_with_options_async(
        self,
        request: main_models.ListDayAmountRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDayAmountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.scene_type):
            query['SceneType'] = request.scene_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDayAmount',
            version = '2022-06-14',
            protocol = 'HTTPS',
            pathname = f'/api/v1/statistics/day/amount',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDayAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_day_amount(
        self,
        request: main_models.ListDayAmountRequest,
    ) -> main_models.ListDayAmountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_day_amount_with_options(request, headers, runtime)

    async def list_day_amount_async(
        self,
        request: main_models.ListDayAmountRequest,
    ) -> main_models.ListDayAmountResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_day_amount_with_options_async(request, headers, runtime)

    def list_recharge_bills_with_options(
        self,
        request: main_models.ListRechargeBillsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRechargeBillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRechargeBills',
            version = '2022-06-14',
            protocol = 'HTTPS',
            pathname = f'/api/v1/statistics/rechargebills',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRechargeBillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recharge_bills_with_options_async(
        self,
        request: main_models.ListRechargeBillsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRechargeBillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRechargeBills',
            version = '2022-06-14',
            protocol = 'HTTPS',
            pathname = f'/api/v1/statistics/rechargebills',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRechargeBillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recharge_bills(
        self,
        request: main_models.ListRechargeBillsRequest,
    ) -> main_models.ListRechargeBillsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_recharge_bills_with_options(request, headers, runtime)

    async def list_recharge_bills_async(
        self,
        request: main_models.ListRechargeBillsRequest,
    ) -> main_models.ListRechargeBillsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_recharge_bills_with_options_async(request, headers, runtime)
