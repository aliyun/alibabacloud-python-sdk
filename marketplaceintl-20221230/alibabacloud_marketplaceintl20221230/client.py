# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_marketplaceintl20221230 import models as main_models
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
        self._product_id = 'marketplaceIntl'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('marketplaceintl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_push_metering_data_with_options(
        self,
        request: main_models.DescribePushMeteringDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePushMeteringDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.push_order_biz_id):
            query['PushOrderBizId'] = request.push_order_biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePushMeteringData',
            version = '2022-12-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePushMeteringDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_push_metering_data_with_options_async(
        self,
        request: main_models.DescribePushMeteringDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePushMeteringDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.push_order_biz_id):
            query['PushOrderBizId'] = request.push_order_biz_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePushMeteringData',
            version = '2022-12-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePushMeteringDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_push_metering_data(
        self,
        request: main_models.DescribePushMeteringDataRequest,
    ) -> main_models.DescribePushMeteringDataResponse:
        runtime = RuntimeOptions()
        return self.describe_push_metering_data_with_options(request, runtime)

    async def describe_push_metering_data_async(
        self,
        request: main_models.DescribePushMeteringDataRequest,
    ) -> main_models.DescribePushMeteringDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_push_metering_data_with_options_async(request, runtime)

    def describe_seller_instances_with_options(
        self,
        request: main_models.DescribeSellerInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSellerInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSellerInstances',
            version = '2022-12-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSellerInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_seller_instances_with_options_async(
        self,
        request: main_models.DescribeSellerInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSellerInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSellerInstances',
            version = '2022-12-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSellerInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_seller_instances(
        self,
        request: main_models.DescribeSellerInstancesRequest,
    ) -> main_models.DescribeSellerInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_seller_instances_with_options(request, runtime)

    async def describe_seller_instances_async(
        self,
        request: main_models.DescribeSellerInstancesRequest,
    ) -> main_models.DescribeSellerInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_seller_instances_with_options_async(request, runtime)

    def notice_instance_user_with_options(
        self,
        request: main_models.NoticeInstanceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NoticeInstanceUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.notice_param):
            body['NoticeParam'] = request.notice_param
        if not DaraCore.is_null(request.notice_type):
            body['NoticeType'] = request.notice_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'NoticeInstanceUser',
            version = '2022-12-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NoticeInstanceUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def notice_instance_user_with_options_async(
        self,
        request: main_models.NoticeInstanceUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NoticeInstanceUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.notice_param):
            body['NoticeParam'] = request.notice_param
        if not DaraCore.is_null(request.notice_type):
            body['NoticeType'] = request.notice_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'NoticeInstanceUser',
            version = '2022-12-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NoticeInstanceUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def notice_instance_user(
        self,
        request: main_models.NoticeInstanceUserRequest,
    ) -> main_models.NoticeInstanceUserResponse:
        runtime = RuntimeOptions()
        return self.notice_instance_user_with_options(request, runtime)

    async def notice_instance_user_async(
        self,
        request: main_models.NoticeInstanceUserRequest,
    ) -> main_models.NoticeInstanceUserResponse:
        runtime = RuntimeOptions()
        return await self.notice_instance_user_with_options_async(request, runtime)

    def push_metering_data_with_options(
        self,
        request: main_models.PushMeteringDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushMeteringDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.metering):
            query['Metering'] = request.metering
        body = {}
        if not DaraCore.is_null(request.gmt_create):
            body['GmtCreate'] = request.gmt_create
        if not DaraCore.is_null(request.metering_data):
            body['MeteringData'] = request.metering_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushMeteringData',
            version = '2022-12-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushMeteringDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_metering_data_with_options_async(
        self,
        request: main_models.PushMeteringDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushMeteringDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.metering):
            query['Metering'] = request.metering
        body = {}
        if not DaraCore.is_null(request.gmt_create):
            body['GmtCreate'] = request.gmt_create
        if not DaraCore.is_null(request.metering_data):
            body['MeteringData'] = request.metering_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PushMeteringData',
            version = '2022-12-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushMeteringDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_metering_data(
        self,
        request: main_models.PushMeteringDataRequest,
    ) -> main_models.PushMeteringDataResponse:
        runtime = RuntimeOptions()
        return self.push_metering_data_with_options(request, runtime)

    async def push_metering_data_async(
        self,
        request: main_models.PushMeteringDataRequest,
    ) -> main_models.PushMeteringDataResponse:
        runtime = RuntimeOptions()
        return await self.push_metering_data_with_options_async(request, runtime)
