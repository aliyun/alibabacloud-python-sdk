# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_modelservice20220614 import models as model_service_20220614_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def get_month_amount_with_options(
        self,
        request: model_service_20220614_models.GetMonthAmountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> model_service_20220614_models.GetMonthAmountResponse:
        """
        @summary 获取当月的使用量
        
        @param request: GetMonthAmountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMonthAmountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonthAmount',
            version='2022-06-14',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/month/amount',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            model_service_20220614_models.GetMonthAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_month_amount_with_options_async(
        self,
        request: model_service_20220614_models.GetMonthAmountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> model_service_20220614_models.GetMonthAmountResponse:
        """
        @summary 获取当月的使用量
        
        @param request: GetMonthAmountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetMonthAmountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMonthAmount',
            version='2022-06-14',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/month/amount',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            model_service_20220614_models.GetMonthAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_month_amount(
        self,
        request: model_service_20220614_models.GetMonthAmountRequest,
    ) -> model_service_20220614_models.GetMonthAmountResponse:
        """
        @summary 获取当月的使用量
        
        @param request: GetMonthAmountRequest
        @return: GetMonthAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_month_amount_with_options(request, headers, runtime)

    async def get_month_amount_async(
        self,
        request: model_service_20220614_models.GetMonthAmountRequest,
    ) -> model_service_20220614_models.GetMonthAmountResponse:
        """
        @summary 获取当月的使用量
        
        @param request: GetMonthAmountRequest
        @return: GetMonthAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_month_amount_with_options_async(request, headers, runtime)

    def get_user_with_options(
        self,
        request: model_service_20220614_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> model_service_20220614_models.GetUserResponse:
        """
        @summary 获取user相关的appid, token等信息
        
        @param request: GetUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-06-14',
            protocol='HTTPS',
            pathname=f'/api/v1/user/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            model_service_20220614_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: model_service_20220614_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> model_service_20220614_models.GetUserResponse:
        """
        @summary 获取user相关的appid, token等信息
        
        @param request: GetUserRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2022-06-14',
            protocol='HTTPS',
            pathname=f'/api/v1/user/info',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            model_service_20220614_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: model_service_20220614_models.GetUserRequest,
    ) -> model_service_20220614_models.GetUserResponse:
        """
        @summary 获取user相关的appid, token等信息
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_with_options(request, headers, runtime)

    async def get_user_async(
        self,
        request: model_service_20220614_models.GetUserRequest,
    ) -> model_service_20220614_models.GetUserResponse:
        """
        @summary 获取user相关的appid, token等信息
        
        @param request: GetUserRequest
        @return: GetUserResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(request, headers, runtime)

    def list_day_amount_with_options(
        self,
        request: model_service_20220614_models.ListDayAmountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> model_service_20220614_models.ListDayAmountResponse:
        """
        @summary 每天的调用量列表
        
        @param request: ListDayAmountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDayAmountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDayAmount',
            version='2022-06-14',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/day/amount',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            model_service_20220614_models.ListDayAmountResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_day_amount_with_options_async(
        self,
        request: model_service_20220614_models.ListDayAmountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> model_service_20220614_models.ListDayAmountResponse:
        """
        @summary 每天的调用量列表
        
        @param request: ListDayAmountRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDayAmountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDayAmount',
            version='2022-06-14',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/day/amount',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            model_service_20220614_models.ListDayAmountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_day_amount(
        self,
        request: model_service_20220614_models.ListDayAmountRequest,
    ) -> model_service_20220614_models.ListDayAmountResponse:
        """
        @summary 每天的调用量列表
        
        @param request: ListDayAmountRequest
        @return: ListDayAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_day_amount_with_options(request, headers, runtime)

    async def list_day_amount_async(
        self,
        request: model_service_20220614_models.ListDayAmountRequest,
    ) -> model_service_20220614_models.ListDayAmountResponse:
        """
        @summary 每天的调用量列表
        
        @param request: ListDayAmountRequest
        @return: ListDayAmountResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_day_amount_with_options_async(request, headers, runtime)

    def list_recharge_bills_with_options(
        self,
        request: model_service_20220614_models.ListRechargeBillsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> model_service_20220614_models.ListRechargeBillsResponse:
        """
        @summary 用户充值列表
        
        @param request: ListRechargeBillsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRechargeBillsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRechargeBills',
            version='2022-06-14',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/rechargebills',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            model_service_20220614_models.ListRechargeBillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recharge_bills_with_options_async(
        self,
        request: model_service_20220614_models.ListRechargeBillsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> model_service_20220614_models.ListRechargeBillsResponse:
        """
        @summary 用户充值列表
        
        @param request: ListRechargeBillsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRechargeBillsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRechargeBills',
            version='2022-06-14',
            protocol='HTTPS',
            pathname=f'/api/v1/statistics/rechargebills',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            model_service_20220614_models.ListRechargeBillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recharge_bills(
        self,
        request: model_service_20220614_models.ListRechargeBillsRequest,
    ) -> model_service_20220614_models.ListRechargeBillsResponse:
        """
        @summary 用户充值列表
        
        @param request: ListRechargeBillsRequest
        @return: ListRechargeBillsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_recharge_bills_with_options(request, headers, runtime)

    async def list_recharge_bills_async(
        self,
        request: model_service_20220614_models.ListRechargeBillsRequest,
    ) -> model_service_20220614_models.ListRechargeBillsResponse:
        """
        @summary 用户充值列表
        
        @param request: ListRechargeBillsRequest
        @return: ListRechargeBillsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_recharge_bills_with_options_async(request, headers, runtime)
