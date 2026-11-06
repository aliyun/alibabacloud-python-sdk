# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ddosdiversion20230701 import models as main_models
from alibabacloud_gateway_pop.client import Client as GatewayClientClient
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
        self._product_id = 'DdosDiversion'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ddosdiversion', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def config_net_status_with_options(
        self,
        request: main_models.ConfigNetStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigNetStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.net):
            query['Net'] = request.net
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sub_nets):
            query['SubNets'] = request.sub_nets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigNetStatus',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigNetStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_net_status_with_options_async(
        self,
        request: main_models.ConfigNetStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigNetStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.net):
            query['Net'] = request.net
        if not DaraCore.is_null(request.regions):
            query['Regions'] = request.regions
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sub_nets):
            query['SubNets'] = request.sub_nets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigNetStatus',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigNetStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_net_status(
        self,
        request: main_models.ConfigNetStatusRequest,
    ) -> main_models.ConfigNetStatusResponse:
        runtime = RuntimeOptions()
        return self.config_net_status_with_options(request, runtime)

    async def config_net_status_async(
        self,
        request: main_models.ConfigNetStatusRequest,
    ) -> main_models.ConfigNetStatusResponse:
        runtime = RuntimeOptions()
        return await self.config_net_status_with_options_async(request, runtime)

    def list_instance_with_options(
        self,
        request: main_models.ListInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.num):
            query['Num'] = request.num
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstance',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: main_models.ListInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.num):
            query['Num'] = request.num
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstance',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: main_models.ListInstanceRequest,
    ) -> main_models.ListInstanceResponse:
        runtime = RuntimeOptions()
        return self.list_instance_with_options(request, runtime)

    async def list_instance_async(
        self,
        request: main_models.ListInstanceRequest,
    ) -> main_models.ListInstanceResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_with_options_async(request, runtime)

    def query_net_list_with_options(
        self,
        request: main_models.QueryNetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryNetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.main_net):
            query['MainNet'] = request.main_net
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.net):
            query['Net'] = request.net
        if not DaraCore.is_null(request.num):
            query['Num'] = request.num
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryNetList',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryNetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_net_list_with_options_async(
        self,
        request: main_models.QueryNetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryNetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.main_net):
            query['MainNet'] = request.main_net
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.net):
            query['Net'] = request.net
        if not DaraCore.is_null(request.num):
            query['Num'] = request.num
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.sale_id):
            query['SaleId'] = request.sale_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryNetList',
            version = '2023-07-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryNetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_net_list(
        self,
        request: main_models.QueryNetListRequest,
    ) -> main_models.QueryNetListResponse:
        runtime = RuntimeOptions()
        return self.query_net_list_with_options(request, runtime)

    async def query_net_list_async(
        self,
        request: main_models.QueryNetListRequest,
    ) -> main_models.QueryNetListResponse:
        runtime = RuntimeOptions()
        return await self.query_net_list_with_options_async(request, runtime)
