# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_arms20181015 import models as main_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'arms.aliyuncs.com',
            'cn-beijing-finance-1': 'arms.aliyuncs.com',
            'cn-beijing-finance-pop': 'arms.aliyuncs.com',
            'cn-beijing-gov-1': 'arms.aliyuncs.com',
            'cn-beijing-nu16-b01': 'arms.aliyuncs.com',
            'cn-edge-1': 'arms.aliyuncs.com',
            'cn-fujian': 'arms.aliyuncs.com',
            'cn-haidian-cm12-c01': 'arms.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'arms.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'arms.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'arms.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'arms.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'arms.aliyuncs.com',
            'cn-hangzhou-test-306': 'arms.aliyuncs.com',
            'cn-hongkong-finance-pop': 'arms.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'arms.aliyuncs.com',
            'cn-qingdao-nebula': 'arms.aliyuncs.com',
            'cn-shanghai-et15-b01': 'arms.aliyuncs.com',
            'cn-shanghai-et2-b01': 'arms.aliyuncs.com',
            'cn-shanghai-inner': 'arms.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'arms.aliyuncs.com',
            'cn-shenzhen-inner': 'arms.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'arms.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'arms.aliyuncs.com',
            'cn-wuhan': 'arms.aliyuncs.com',
            'cn-yushanfang': 'arms.aliyuncs.com',
            'cn-zhangbei': 'arms.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'arms.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'arms.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'arms.aliyuncs.com',
            'eu-west-1-oxs': 'arms.aliyuncs.com',
            'me-east-1': 'arms.aliyuncs.com',
            'rus-west-1-pop': 'arms.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('arms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def a_rmsquery_data_set_with_options(
        self,
        request: main_models.ARMSQueryDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ARMSQueryDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.date_str):
            query['DateStr'] = request.date_str
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.hacker_user_id):
            query['HackerUserId'] = request.hacker_user_id
        if not DaraCore.is_null(request.hungry_mode):
            query['HungryMode'] = request.hungry_mode
        if not DaraCore.is_null(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not DaraCore.is_null(request.is_drill_down):
            query['IsDrillDown'] = request.is_drill_down
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.max_time):
            query['MaxTime'] = request.max_time
        if not DaraCore.is_null(request.measures):
            query['Measures'] = request.measures
        if not DaraCore.is_null(request.min_time):
            query['MinTime'] = request.min_time
        if not DaraCore.is_null(request.optional_dims):
            query['OptionalDims'] = request.optional_dims
        if not DaraCore.is_null(request.order_by_key):
            query['OrderByKey'] = request.order_by_key
        if not DaraCore.is_null(request.reduce_tail):
            query['ReduceTail'] = request.reduce_tail
        if not DaraCore.is_null(request.required_dims):
            query['RequiredDims'] = request.required_dims
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ARMSQueryDataSet',
            version = '2018-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ARMSQueryDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def a_rmsquery_data_set_with_options_async(
        self,
        request: main_models.ARMSQueryDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ARMSQueryDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.date_str):
            query['DateStr'] = request.date_str
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.hacker_user_id):
            query['HackerUserId'] = request.hacker_user_id
        if not DaraCore.is_null(request.hungry_mode):
            query['HungryMode'] = request.hungry_mode
        if not DaraCore.is_null(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not DaraCore.is_null(request.is_drill_down):
            query['IsDrillDown'] = request.is_drill_down
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.max_time):
            query['MaxTime'] = request.max_time
        if not DaraCore.is_null(request.measures):
            query['Measures'] = request.measures
        if not DaraCore.is_null(request.min_time):
            query['MinTime'] = request.min_time
        if not DaraCore.is_null(request.optional_dims):
            query['OptionalDims'] = request.optional_dims
        if not DaraCore.is_null(request.order_by_key):
            query['OrderByKey'] = request.order_by_key
        if not DaraCore.is_null(request.reduce_tail):
            query['ReduceTail'] = request.reduce_tail
        if not DaraCore.is_null(request.required_dims):
            query['RequiredDims'] = request.required_dims
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ARMSQueryDataSet',
            version = '2018-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ARMSQueryDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def a_rmsquery_data_set(
        self,
        request: main_models.ARMSQueryDataSetRequest,
    ) -> main_models.ARMSQueryDataSetResponse:
        runtime = RuntimeOptions()
        return self.a_rmsquery_data_set_with_options(request, runtime)

    async def a_rmsquery_data_set_async(
        self,
        request: main_models.ARMSQueryDataSetRequest,
    ) -> main_models.ARMSQueryDataSetResponse:
        runtime = RuntimeOptions()
        return await self.a_rmsquery_data_set_with_options_async(request, runtime)

    def metric_query_with_options(
        self,
        request: main_models.MetricQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MetricQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.hacker_user_id):
            query['HackerUserId'] = request.hacker_user_id
        if not DaraCore.is_null(request.iinterval_in_sec):
            query['IintervalInSec'] = request.iinterval_in_sec
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.measures):
            query['Measures'] = request.measures
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MetricQuery',
            version = '2018-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MetricQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def metric_query_with_options_async(
        self,
        request: main_models.MetricQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MetricQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.hacker_user_id):
            query['HackerUserId'] = request.hacker_user_id
        if not DaraCore.is_null(request.iinterval_in_sec):
            query['IintervalInSec'] = request.iinterval_in_sec
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.measures):
            query['Measures'] = request.measures
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MetricQuery',
            version = '2018-10-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MetricQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def metric_query(
        self,
        request: main_models.MetricQueryRequest,
    ) -> main_models.MetricQueryResponse:
        runtime = RuntimeOptions()
        return self.metric_query_with_options(request, runtime)

    async def metric_query_async(
        self,
        request: main_models.MetricQueryRequest,
    ) -> main_models.MetricQueryResponse:
        runtime = RuntimeOptions()
        return await self.metric_query_with_options_async(request, runtime)
