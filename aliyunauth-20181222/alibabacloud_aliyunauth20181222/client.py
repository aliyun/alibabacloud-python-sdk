# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aliyunauth20181222 import models as main_models
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
        self._endpoint = self.get_endpoint('aliyunauth', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def authenticate_with_options(
        self,
        request: main_models.AuthenticateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthenticateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Authenticate',
            version = '2018-12-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthenticateResponse(),
            self.call_api(params, req, runtime)
        )

    async def authenticate_with_options_async(
        self,
        request: main_models.AuthenticateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AuthenticateResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Authenticate',
            version = '2018-12-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthenticateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authenticate(
        self,
        request: main_models.AuthenticateRequest,
    ) -> main_models.AuthenticateResponse:
        runtime = RuntimeOptions()
        return self.authenticate_with_options(request, runtime)

    async def authenticate_async(
        self,
        request: main_models.AuthenticateRequest,
    ) -> main_models.AuthenticateResponse:
        runtime = RuntimeOptions()
        return await self.authenticate_with_options_async(request, runtime)

    def get_detail_by_order_with_options(
        self,
        request: main_models.GetDetailByOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDetailByOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acceptor):
            query['Acceptor'] = request.acceptor
        if not DaraCore.is_null(request.biz_no):
            query['BizNo'] = request.biz_no
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.check_auth_items):
            query['CheckAuthItems'] = request.check_auth_items
        if not DaraCore.is_null(request.emp_id):
            query['EmpId'] = request.emp_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.opt_source):
            query['OptSource'] = request.opt_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDetailByOrder',
            version = '2018-12-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDetailByOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_detail_by_order_with_options_async(
        self,
        request: main_models.GetDetailByOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDetailByOrderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acceptor):
            query['Acceptor'] = request.acceptor
        if not DaraCore.is_null(request.biz_no):
            query['BizNo'] = request.biz_no
        if not DaraCore.is_null(request.channel):
            query['Channel'] = request.channel
        if not DaraCore.is_null(request.check_auth_items):
            query['CheckAuthItems'] = request.check_auth_items
        if not DaraCore.is_null(request.emp_id):
            query['EmpId'] = request.emp_id
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.opt_source):
            query['OptSource'] = request.opt_source
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDetailByOrder',
            version = '2018-12-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDetailByOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_detail_by_order(
        self,
        request: main_models.GetDetailByOrderRequest,
    ) -> main_models.GetDetailByOrderResponse:
        runtime = RuntimeOptions()
        return self.get_detail_by_order_with_options(request, runtime)

    async def get_detail_by_order_async(
        self,
        request: main_models.GetDetailByOrderRequest,
    ) -> main_models.GetDetailByOrderResponse:
        runtime = RuntimeOptions()
        return await self.get_detail_by_order_with_options_async(request, runtime)

    def query_auth_with_options(
        self,
        request: main_models.QueryAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAuthResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAuth',
            version = '2018-12-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAuthResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_auth_with_options_async(
        self,
        request: main_models.QueryAuthRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAuthResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAuth',
            version = '2018-12-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAuthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_auth(
        self,
        request: main_models.QueryAuthRequest,
    ) -> main_models.QueryAuthResponse:
        runtime = RuntimeOptions()
        return self.query_auth_with_options(request, runtime)

    async def query_auth_async(
        self,
        request: main_models.QueryAuthRequest,
    ) -> main_models.QueryAuthResponse:
        runtime = RuntimeOptions()
        return await self.query_auth_with_options_async(request, runtime)

    def query_in_effect_quth_order_with_options(
        self,
        request: main_models.QueryInEffectQuthOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInEffectQuthOrderResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInEffectQuthOrder',
            version = '2018-12-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInEffectQuthOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_in_effect_quth_order_with_options_async(
        self,
        request: main_models.QueryInEffectQuthOrderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryInEffectQuthOrderResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryInEffectQuthOrder',
            version = '2018-12-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryInEffectQuthOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_in_effect_quth_order(
        self,
        request: main_models.QueryInEffectQuthOrderRequest,
    ) -> main_models.QueryInEffectQuthOrderResponse:
        runtime = RuntimeOptions()
        return self.query_in_effect_quth_order_with_options(request, runtime)

    async def query_in_effect_quth_order_async(
        self,
        request: main_models.QueryInEffectQuthOrderRequest,
    ) -> main_models.QueryInEffectQuthOrderResponse:
        runtime = RuntimeOptions()
        return await self.query_in_effect_quth_order_with_options_async(request, runtime)
