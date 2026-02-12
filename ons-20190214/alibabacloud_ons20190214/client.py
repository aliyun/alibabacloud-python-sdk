# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ons20190214 import models as main_models
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
            'ap-northeast-2-pop': 'ons.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'ons.aliyuncs.com',
            'cn-beijing-finance-pop': 'ons.aliyuncs.com',
            'cn-beijing-gov-1': 'ons.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ons.aliyuncs.com',
            'cn-edge-1': 'ons.aliyuncs.com',
            'cn-fujian': 'ons.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ons.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ons.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ons.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ons.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ons.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ons.aliyuncs.com',
            'cn-hangzhou-test-306': 'ons.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ons.aliyuncs.com',
            'cn-qingdao-nebula': 'ons.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ons.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ons.aliyuncs.com',
            'cn-shanghai-inner': 'ons.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ons.aliyuncs.com',
            'cn-shenzhen-inner': 'ons.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ons.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ons.aliyuncs.com',
            'cn-wuhan': 'ons.aliyuncs.com',
            'cn-yushanfang': 'ons.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ons.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ons.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ons.aliyuncs.com',
            'eu-west-1-oxs': 'ons.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'ons.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ons', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def ons_consumer_accumulate_with_options(
        self,
        request: main_models.OnsConsumerAccumulateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsConsumerAccumulateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.detail):
            query['Detail'] = request.detail
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsConsumerAccumulate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsConsumerAccumulateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_consumer_accumulate_with_options_async(
        self,
        request: main_models.OnsConsumerAccumulateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsConsumerAccumulateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.detail):
            query['Detail'] = request.detail
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsConsumerAccumulate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsConsumerAccumulateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_consumer_accumulate(
        self,
        request: main_models.OnsConsumerAccumulateRequest,
    ) -> main_models.OnsConsumerAccumulateResponse:
        runtime = RuntimeOptions()
        return self.ons_consumer_accumulate_with_options(request, runtime)

    async def ons_consumer_accumulate_async(
        self,
        request: main_models.OnsConsumerAccumulateRequest,
    ) -> main_models.OnsConsumerAccumulateResponse:
        runtime = RuntimeOptions()
        return await self.ons_consumer_accumulate_with_options_async(request, runtime)

    def ons_consumer_get_connection_with_options(
        self,
        request: main_models.OnsConsumerGetConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsConsumerGetConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsConsumerGetConnection',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsConsumerGetConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_consumer_get_connection_with_options_async(
        self,
        request: main_models.OnsConsumerGetConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsConsumerGetConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsConsumerGetConnection',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsConsumerGetConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_consumer_get_connection(
        self,
        request: main_models.OnsConsumerGetConnectionRequest,
    ) -> main_models.OnsConsumerGetConnectionResponse:
        runtime = RuntimeOptions()
        return self.ons_consumer_get_connection_with_options(request, runtime)

    async def ons_consumer_get_connection_async(
        self,
        request: main_models.OnsConsumerGetConnectionRequest,
    ) -> main_models.OnsConsumerGetConnectionResponse:
        runtime = RuntimeOptions()
        return await self.ons_consumer_get_connection_with_options_async(request, runtime)

    def ons_consumer_reset_offset_with_options(
        self,
        request: main_models.OnsConsumerResetOffsetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsConsumerResetOffsetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.reset_timestamp):
            query['ResetTimestamp'] = request.reset_timestamp
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsConsumerResetOffset',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsConsumerResetOffsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_consumer_reset_offset_with_options_async(
        self,
        request: main_models.OnsConsumerResetOffsetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsConsumerResetOffsetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.reset_timestamp):
            query['ResetTimestamp'] = request.reset_timestamp
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsConsumerResetOffset',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsConsumerResetOffsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_consumer_reset_offset(
        self,
        request: main_models.OnsConsumerResetOffsetRequest,
    ) -> main_models.OnsConsumerResetOffsetResponse:
        runtime = RuntimeOptions()
        return self.ons_consumer_reset_offset_with_options(request, runtime)

    async def ons_consumer_reset_offset_async(
        self,
        request: main_models.OnsConsumerResetOffsetRequest,
    ) -> main_models.OnsConsumerResetOffsetResponse:
        runtime = RuntimeOptions()
        return await self.ons_consumer_reset_offset_with_options_async(request, runtime)

    def ons_consumer_status_with_options(
        self,
        request: main_models.OnsConsumerStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsConsumerStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.detail):
            query['Detail'] = request.detail
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_jstack):
            query['NeedJstack'] = request.need_jstack
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsConsumerStatus',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsConsumerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_consumer_status_with_options_async(
        self,
        request: main_models.OnsConsumerStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsConsumerStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.detail):
            query['Detail'] = request.detail
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.need_jstack):
            query['NeedJstack'] = request.need_jstack
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsConsumerStatus',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsConsumerStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_consumer_status(
        self,
        request: main_models.OnsConsumerStatusRequest,
    ) -> main_models.OnsConsumerStatusResponse:
        runtime = RuntimeOptions()
        return self.ons_consumer_status_with_options(request, runtime)

    async def ons_consumer_status_async(
        self,
        request: main_models.OnsConsumerStatusRequest,
    ) -> main_models.OnsConsumerStatusResponse:
        runtime = RuntimeOptions()
        return await self.ons_consumer_status_with_options_async(request, runtime)

    def ons_consumer_time_span_with_options(
        self,
        request: main_models.OnsConsumerTimeSpanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsConsumerTimeSpanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsConsumerTimeSpan',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsConsumerTimeSpanResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_consumer_time_span_with_options_async(
        self,
        request: main_models.OnsConsumerTimeSpanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsConsumerTimeSpanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsConsumerTimeSpan',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsConsumerTimeSpanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_consumer_time_span(
        self,
        request: main_models.OnsConsumerTimeSpanRequest,
    ) -> main_models.OnsConsumerTimeSpanResponse:
        runtime = RuntimeOptions()
        return self.ons_consumer_time_span_with_options(request, runtime)

    async def ons_consumer_time_span_async(
        self,
        request: main_models.OnsConsumerTimeSpanRequest,
    ) -> main_models.OnsConsumerTimeSpanResponse:
        runtime = RuntimeOptions()
        return await self.ons_consumer_time_span_with_options_async(request, runtime)

    def ons_dlqmessage_get_by_id_with_options(
        self,
        request: main_models.OnsDLQMessageGetByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsDLQMessageGetByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsDLQMessageGetById',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsDLQMessageGetByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_dlqmessage_get_by_id_with_options_async(
        self,
        request: main_models.OnsDLQMessageGetByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsDLQMessageGetByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsDLQMessageGetById',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsDLQMessageGetByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_dlqmessage_get_by_id(
        self,
        request: main_models.OnsDLQMessageGetByIdRequest,
    ) -> main_models.OnsDLQMessageGetByIdResponse:
        runtime = RuntimeOptions()
        return self.ons_dlqmessage_get_by_id_with_options(request, runtime)

    async def ons_dlqmessage_get_by_id_async(
        self,
        request: main_models.OnsDLQMessageGetByIdRequest,
    ) -> main_models.OnsDLQMessageGetByIdResponse:
        runtime = RuntimeOptions()
        return await self.ons_dlqmessage_get_by_id_with_options_async(request, runtime)

    def ons_dlqmessage_page_query_by_group_id_with_options(
        self,
        request: main_models.OnsDLQMessagePageQueryByGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsDLQMessagePageQueryByGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsDLQMessagePageQueryByGroupId',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsDLQMessagePageQueryByGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_dlqmessage_page_query_by_group_id_with_options_async(
        self,
        request: main_models.OnsDLQMessagePageQueryByGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsDLQMessagePageQueryByGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsDLQMessagePageQueryByGroupId',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsDLQMessagePageQueryByGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_dlqmessage_page_query_by_group_id(
        self,
        request: main_models.OnsDLQMessagePageQueryByGroupIdRequest,
    ) -> main_models.OnsDLQMessagePageQueryByGroupIdResponse:
        runtime = RuntimeOptions()
        return self.ons_dlqmessage_page_query_by_group_id_with_options(request, runtime)

    async def ons_dlqmessage_page_query_by_group_id_async(
        self,
        request: main_models.OnsDLQMessagePageQueryByGroupIdRequest,
    ) -> main_models.OnsDLQMessagePageQueryByGroupIdResponse:
        runtime = RuntimeOptions()
        return await self.ons_dlqmessage_page_query_by_group_id_with_options_async(request, runtime)

    def ons_dlqmessage_resend_by_id_with_options(
        self,
        request: main_models.OnsDLQMessageResendByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsDLQMessageResendByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsDLQMessageResendById',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsDLQMessageResendByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_dlqmessage_resend_by_id_with_options_async(
        self,
        request: main_models.OnsDLQMessageResendByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsDLQMessageResendByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsDLQMessageResendById',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsDLQMessageResendByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_dlqmessage_resend_by_id(
        self,
        request: main_models.OnsDLQMessageResendByIdRequest,
    ) -> main_models.OnsDLQMessageResendByIdResponse:
        runtime = RuntimeOptions()
        return self.ons_dlqmessage_resend_by_id_with_options(request, runtime)

    async def ons_dlqmessage_resend_by_id_async(
        self,
        request: main_models.OnsDLQMessageResendByIdRequest,
    ) -> main_models.OnsDLQMessageResendByIdResponse:
        runtime = RuntimeOptions()
        return await self.ons_dlqmessage_resend_by_id_with_options_async(request, runtime)

    def ons_group_consumer_update_with_options(
        self,
        request: main_models.OnsGroupConsumerUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsGroupConsumerUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.read_enable):
            query['ReadEnable'] = request.read_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsGroupConsumerUpdate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsGroupConsumerUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_group_consumer_update_with_options_async(
        self,
        request: main_models.OnsGroupConsumerUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsGroupConsumerUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.read_enable):
            query['ReadEnable'] = request.read_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsGroupConsumerUpdate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsGroupConsumerUpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_group_consumer_update(
        self,
        request: main_models.OnsGroupConsumerUpdateRequest,
    ) -> main_models.OnsGroupConsumerUpdateResponse:
        runtime = RuntimeOptions()
        return self.ons_group_consumer_update_with_options(request, runtime)

    async def ons_group_consumer_update_async(
        self,
        request: main_models.OnsGroupConsumerUpdateRequest,
    ) -> main_models.OnsGroupConsumerUpdateResponse:
        runtime = RuntimeOptions()
        return await self.ons_group_consumer_update_with_options_async(request, runtime)

    def ons_group_create_with_options(
        self,
        request: main_models.OnsGroupCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsGroupCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsGroupCreate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsGroupCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_group_create_with_options_async(
        self,
        request: main_models.OnsGroupCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsGroupCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsGroupCreate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsGroupCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_group_create(
        self,
        request: main_models.OnsGroupCreateRequest,
    ) -> main_models.OnsGroupCreateResponse:
        runtime = RuntimeOptions()
        return self.ons_group_create_with_options(request, runtime)

    async def ons_group_create_async(
        self,
        request: main_models.OnsGroupCreateRequest,
    ) -> main_models.OnsGroupCreateResponse:
        runtime = RuntimeOptions()
        return await self.ons_group_create_with_options_async(request, runtime)

    def ons_group_delete_with_options(
        self,
        request: main_models.OnsGroupDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsGroupDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsGroupDelete',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsGroupDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_group_delete_with_options_async(
        self,
        request: main_models.OnsGroupDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsGroupDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsGroupDelete',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsGroupDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_group_delete(
        self,
        request: main_models.OnsGroupDeleteRequest,
    ) -> main_models.OnsGroupDeleteResponse:
        runtime = RuntimeOptions()
        return self.ons_group_delete_with_options(request, runtime)

    async def ons_group_delete_async(
        self,
        request: main_models.OnsGroupDeleteRequest,
    ) -> main_models.OnsGroupDeleteResponse:
        runtime = RuntimeOptions()
        return await self.ons_group_delete_with_options_async(request, runtime)

    def ons_group_list_with_options(
        self,
        request: main_models.OnsGroupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsGroupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsGroupList',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_group_list_with_options_async(
        self,
        request: main_models.OnsGroupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsGroupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsGroupList',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_group_list(
        self,
        request: main_models.OnsGroupListRequest,
    ) -> main_models.OnsGroupListResponse:
        runtime = RuntimeOptions()
        return self.ons_group_list_with_options(request, runtime)

    async def ons_group_list_async(
        self,
        request: main_models.OnsGroupListRequest,
    ) -> main_models.OnsGroupListResponse:
        runtime = RuntimeOptions()
        return await self.ons_group_list_with_options_async(request, runtime)

    def ons_group_sub_detail_with_options(
        self,
        request: main_models.OnsGroupSubDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsGroupSubDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsGroupSubDetail',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsGroupSubDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_group_sub_detail_with_options_async(
        self,
        request: main_models.OnsGroupSubDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsGroupSubDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsGroupSubDetail',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsGroupSubDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_group_sub_detail(
        self,
        request: main_models.OnsGroupSubDetailRequest,
    ) -> main_models.OnsGroupSubDetailResponse:
        runtime = RuntimeOptions()
        return self.ons_group_sub_detail_with_options(request, runtime)

    async def ons_group_sub_detail_async(
        self,
        request: main_models.OnsGroupSubDetailRequest,
    ) -> main_models.OnsGroupSubDetailResponse:
        runtime = RuntimeOptions()
        return await self.ons_group_sub_detail_with_options_async(request, runtime)

    def ons_instance_base_info_with_options(
        self,
        request: main_models.OnsInstanceBaseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsInstanceBaseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsInstanceBaseInfo',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsInstanceBaseInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_instance_base_info_with_options_async(
        self,
        request: main_models.OnsInstanceBaseInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsInstanceBaseInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsInstanceBaseInfo',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsInstanceBaseInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_instance_base_info(
        self,
        request: main_models.OnsInstanceBaseInfoRequest,
    ) -> main_models.OnsInstanceBaseInfoResponse:
        runtime = RuntimeOptions()
        return self.ons_instance_base_info_with_options(request, runtime)

    async def ons_instance_base_info_async(
        self,
        request: main_models.OnsInstanceBaseInfoRequest,
    ) -> main_models.OnsInstanceBaseInfoResponse:
        runtime = RuntimeOptions()
        return await self.ons_instance_base_info_with_options_async(request, runtime)

    def ons_instance_create_with_options(
        self,
        request: main_models.OnsInstanceCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsInstanceCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsInstanceCreate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsInstanceCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_instance_create_with_options_async(
        self,
        request: main_models.OnsInstanceCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsInstanceCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsInstanceCreate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsInstanceCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_instance_create(
        self,
        request: main_models.OnsInstanceCreateRequest,
    ) -> main_models.OnsInstanceCreateResponse:
        runtime = RuntimeOptions()
        return self.ons_instance_create_with_options(request, runtime)

    async def ons_instance_create_async(
        self,
        request: main_models.OnsInstanceCreateRequest,
    ) -> main_models.OnsInstanceCreateResponse:
        runtime = RuntimeOptions()
        return await self.ons_instance_create_with_options_async(request, runtime)

    def ons_instance_delete_with_options(
        self,
        request: main_models.OnsInstanceDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsInstanceDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsInstanceDelete',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsInstanceDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_instance_delete_with_options_async(
        self,
        request: main_models.OnsInstanceDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsInstanceDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsInstanceDelete',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsInstanceDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_instance_delete(
        self,
        request: main_models.OnsInstanceDeleteRequest,
    ) -> main_models.OnsInstanceDeleteResponse:
        runtime = RuntimeOptions()
        return self.ons_instance_delete_with_options(request, runtime)

    async def ons_instance_delete_async(
        self,
        request: main_models.OnsInstanceDeleteRequest,
    ) -> main_models.OnsInstanceDeleteResponse:
        runtime = RuntimeOptions()
        return await self.ons_instance_delete_with_options_async(request, runtime)

    def ons_instance_in_service_list_with_options(
        self,
        request: main_models.OnsInstanceInServiceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsInstanceInServiceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.need_resource_info):
            query['NeedResourceInfo'] = request.need_resource_info
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsInstanceInServiceList',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsInstanceInServiceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_instance_in_service_list_with_options_async(
        self,
        request: main_models.OnsInstanceInServiceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsInstanceInServiceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.need_resource_info):
            query['NeedResourceInfo'] = request.need_resource_info
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsInstanceInServiceList',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsInstanceInServiceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_instance_in_service_list(
        self,
        request: main_models.OnsInstanceInServiceListRequest,
    ) -> main_models.OnsInstanceInServiceListResponse:
        runtime = RuntimeOptions()
        return self.ons_instance_in_service_list_with_options(request, runtime)

    async def ons_instance_in_service_list_async(
        self,
        request: main_models.OnsInstanceInServiceListRequest,
    ) -> main_models.OnsInstanceInServiceListResponse:
        runtime = RuntimeOptions()
        return await self.ons_instance_in_service_list_with_options_async(request, runtime)

    def ons_instance_update_with_options(
        self,
        request: main_models.OnsInstanceUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsInstanceUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsInstanceUpdate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsInstanceUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_instance_update_with_options_async(
        self,
        request: main_models.OnsInstanceUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsInstanceUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsInstanceUpdate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsInstanceUpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_instance_update(
        self,
        request: main_models.OnsInstanceUpdateRequest,
    ) -> main_models.OnsInstanceUpdateResponse:
        runtime = RuntimeOptions()
        return self.ons_instance_update_with_options(request, runtime)

    async def ons_instance_update_async(
        self,
        request: main_models.OnsInstanceUpdateRequest,
    ) -> main_models.OnsInstanceUpdateResponse:
        runtime = RuntimeOptions()
        return await self.ons_instance_update_with_options_async(request, runtime)

    def ons_message_detail_with_options(
        self,
        request: main_models.OnsMessageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsMessageDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsMessageDetail',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsMessageDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_message_detail_with_options_async(
        self,
        request: main_models.OnsMessageDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsMessageDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsMessageDetail',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsMessageDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_message_detail(
        self,
        request: main_models.OnsMessageDetailRequest,
    ) -> main_models.OnsMessageDetailResponse:
        runtime = RuntimeOptions()
        return self.ons_message_detail_with_options(request, runtime)

    async def ons_message_detail_async(
        self,
        request: main_models.OnsMessageDetailRequest,
    ) -> main_models.OnsMessageDetailResponse:
        runtime = RuntimeOptions()
        return await self.ons_message_detail_with_options_async(request, runtime)

    def ons_message_get_by_key_with_options(
        self,
        request: main_models.OnsMessageGetByKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsMessageGetByKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsMessageGetByKey',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsMessageGetByKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_message_get_by_key_with_options_async(
        self,
        request: main_models.OnsMessageGetByKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsMessageGetByKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsMessageGetByKey',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsMessageGetByKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_message_get_by_key(
        self,
        request: main_models.OnsMessageGetByKeyRequest,
    ) -> main_models.OnsMessageGetByKeyResponse:
        runtime = RuntimeOptions()
        return self.ons_message_get_by_key_with_options(request, runtime)

    async def ons_message_get_by_key_async(
        self,
        request: main_models.OnsMessageGetByKeyRequest,
    ) -> main_models.OnsMessageGetByKeyResponse:
        runtime = RuntimeOptions()
        return await self.ons_message_get_by_key_with_options_async(request, runtime)

    def ons_message_get_by_msg_id_with_options(
        self,
        request: main_models.OnsMessageGetByMsgIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsMessageGetByMsgIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsMessageGetByMsgId',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsMessageGetByMsgIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_message_get_by_msg_id_with_options_async(
        self,
        request: main_models.OnsMessageGetByMsgIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsMessageGetByMsgIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsMessageGetByMsgId',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsMessageGetByMsgIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_message_get_by_msg_id(
        self,
        request: main_models.OnsMessageGetByMsgIdRequest,
    ) -> main_models.OnsMessageGetByMsgIdResponse:
        runtime = RuntimeOptions()
        return self.ons_message_get_by_msg_id_with_options(request, runtime)

    async def ons_message_get_by_msg_id_async(
        self,
        request: main_models.OnsMessageGetByMsgIdRequest,
    ) -> main_models.OnsMessageGetByMsgIdResponse:
        runtime = RuntimeOptions()
        return await self.ons_message_get_by_msg_id_with_options_async(request, runtime)

    def ons_message_page_query_by_topic_with_options(
        self,
        request: main_models.OnsMessagePageQueryByTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsMessagePageQueryByTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsMessagePageQueryByTopic',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsMessagePageQueryByTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_message_page_query_by_topic_with_options_async(
        self,
        request: main_models.OnsMessagePageQueryByTopicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsMessagePageQueryByTopicResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsMessagePageQueryByTopic',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsMessagePageQueryByTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_message_page_query_by_topic(
        self,
        request: main_models.OnsMessagePageQueryByTopicRequest,
    ) -> main_models.OnsMessagePageQueryByTopicResponse:
        runtime = RuntimeOptions()
        return self.ons_message_page_query_by_topic_with_options(request, runtime)

    async def ons_message_page_query_by_topic_async(
        self,
        request: main_models.OnsMessagePageQueryByTopicRequest,
    ) -> main_models.OnsMessagePageQueryByTopicResponse:
        runtime = RuntimeOptions()
        return await self.ons_message_page_query_by_topic_with_options_async(request, runtime)

    def ons_message_push_with_options(
        self,
        request: main_models.OnsMessagePushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsMessagePushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsMessagePush',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsMessagePushResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_message_push_with_options_async(
        self,
        request: main_models.OnsMessagePushRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsMessagePushResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsMessagePush',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsMessagePushResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_message_push(
        self,
        request: main_models.OnsMessagePushRequest,
    ) -> main_models.OnsMessagePushResponse:
        runtime = RuntimeOptions()
        return self.ons_message_push_with_options(request, runtime)

    async def ons_message_push_async(
        self,
        request: main_models.OnsMessagePushRequest,
    ) -> main_models.OnsMessagePushResponse:
        runtime = RuntimeOptions()
        return await self.ons_message_push_with_options_async(request, runtime)

    def ons_message_trace_with_options(
        self,
        request: main_models.OnsMessageTraceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsMessageTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsMessageTrace',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsMessageTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_message_trace_with_options_async(
        self,
        request: main_models.OnsMessageTraceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsMessageTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsMessageTrace',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsMessageTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_message_trace(
        self,
        request: main_models.OnsMessageTraceRequest,
    ) -> main_models.OnsMessageTraceResponse:
        runtime = RuntimeOptions()
        return self.ons_message_trace_with_options(request, runtime)

    async def ons_message_trace_async(
        self,
        request: main_models.OnsMessageTraceRequest,
    ) -> main_models.OnsMessageTraceResponse:
        runtime = RuntimeOptions()
        return await self.ons_message_trace_with_options_async(request, runtime)

    def ons_region_list_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OnsRegionListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OnsRegionList',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsRegionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_region_list_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OnsRegionListResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OnsRegionList',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsRegionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_region_list(self) -> main_models.OnsRegionListResponse:
        runtime = RuntimeOptions()
        return self.ons_region_list_with_options(runtime)

    async def ons_region_list_async(self) -> main_models.OnsRegionListResponse:
        runtime = RuntimeOptions()
        return await self.ons_region_list_with_options_async(runtime)

    def ons_topic_create_with_options(
        self,
        request: main_models.OnsTopicCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTopicCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTopicCreate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTopicCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_topic_create_with_options_async(
        self,
        request: main_models.OnsTopicCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTopicCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.message_type):
            query['MessageType'] = request.message_type
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTopicCreate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTopicCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_topic_create(
        self,
        request: main_models.OnsTopicCreateRequest,
    ) -> main_models.OnsTopicCreateResponse:
        runtime = RuntimeOptions()
        return self.ons_topic_create_with_options(request, runtime)

    async def ons_topic_create_async(
        self,
        request: main_models.OnsTopicCreateRequest,
    ) -> main_models.OnsTopicCreateResponse:
        runtime = RuntimeOptions()
        return await self.ons_topic_create_with_options_async(request, runtime)

    def ons_topic_delete_with_options(
        self,
        request: main_models.OnsTopicDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTopicDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTopicDelete',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTopicDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_topic_delete_with_options_async(
        self,
        request: main_models.OnsTopicDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTopicDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTopicDelete',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTopicDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_topic_delete(
        self,
        request: main_models.OnsTopicDeleteRequest,
    ) -> main_models.OnsTopicDeleteResponse:
        runtime = RuntimeOptions()
        return self.ons_topic_delete_with_options(request, runtime)

    async def ons_topic_delete_async(
        self,
        request: main_models.OnsTopicDeleteRequest,
    ) -> main_models.OnsTopicDeleteResponse:
        runtime = RuntimeOptions()
        return await self.ons_topic_delete_with_options_async(request, runtime)

    def ons_topic_list_with_options(
        self,
        request: main_models.OnsTopicListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTopicListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTopicList',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTopicListResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_topic_list_with_options_async(
        self,
        request: main_models.OnsTopicListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTopicListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTopicList',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTopicListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_topic_list(
        self,
        request: main_models.OnsTopicListRequest,
    ) -> main_models.OnsTopicListResponse:
        runtime = RuntimeOptions()
        return self.ons_topic_list_with_options(request, runtime)

    async def ons_topic_list_async(
        self,
        request: main_models.OnsTopicListRequest,
    ) -> main_models.OnsTopicListResponse:
        runtime = RuntimeOptions()
        return await self.ons_topic_list_with_options_async(request, runtime)

    def ons_topic_status_with_options(
        self,
        request: main_models.OnsTopicStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTopicStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTopicStatus',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTopicStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_topic_status_with_options_async(
        self,
        request: main_models.OnsTopicStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTopicStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTopicStatus',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTopicStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_topic_status(
        self,
        request: main_models.OnsTopicStatusRequest,
    ) -> main_models.OnsTopicStatusResponse:
        runtime = RuntimeOptions()
        return self.ons_topic_status_with_options(request, runtime)

    async def ons_topic_status_async(
        self,
        request: main_models.OnsTopicStatusRequest,
    ) -> main_models.OnsTopicStatusResponse:
        runtime = RuntimeOptions()
        return await self.ons_topic_status_with_options_async(request, runtime)

    def ons_topic_sub_detail_with_options(
        self,
        request: main_models.OnsTopicSubDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTopicSubDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTopicSubDetail',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTopicSubDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_topic_sub_detail_with_options_async(
        self,
        request: main_models.OnsTopicSubDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTopicSubDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTopicSubDetail',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTopicSubDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_topic_sub_detail(
        self,
        request: main_models.OnsTopicSubDetailRequest,
    ) -> main_models.OnsTopicSubDetailResponse:
        runtime = RuntimeOptions()
        return self.ons_topic_sub_detail_with_options(request, runtime)

    async def ons_topic_sub_detail_async(
        self,
        request: main_models.OnsTopicSubDetailRequest,
    ) -> main_models.OnsTopicSubDetailResponse:
        runtime = RuntimeOptions()
        return await self.ons_topic_sub_detail_with_options_async(request, runtime)

    def ons_topic_update_with_options(
        self,
        request: main_models.OnsTopicUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTopicUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.perm):
            query['Perm'] = request.perm
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTopicUpdate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTopicUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_topic_update_with_options_async(
        self,
        request: main_models.OnsTopicUpdateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTopicUpdateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.perm):
            query['Perm'] = request.perm
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTopicUpdate',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTopicUpdateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_topic_update(
        self,
        request: main_models.OnsTopicUpdateRequest,
    ) -> main_models.OnsTopicUpdateResponse:
        runtime = RuntimeOptions()
        return self.ons_topic_update_with_options(request, runtime)

    async def ons_topic_update_async(
        self,
        request: main_models.OnsTopicUpdateRequest,
    ) -> main_models.OnsTopicUpdateResponse:
        runtime = RuntimeOptions()
        return await self.ons_topic_update_with_options_async(request, runtime)

    def ons_trace_get_result_with_options(
        self,
        request: main_models.OnsTraceGetResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTraceGetResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.query_id):
            query['QueryId'] = request.query_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTraceGetResult',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTraceGetResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_trace_get_result_with_options_async(
        self,
        request: main_models.OnsTraceGetResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTraceGetResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.query_id):
            query['QueryId'] = request.query_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTraceGetResult',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTraceGetResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_trace_get_result(
        self,
        request: main_models.OnsTraceGetResultRequest,
    ) -> main_models.OnsTraceGetResultResponse:
        runtime = RuntimeOptions()
        return self.ons_trace_get_result_with_options(request, runtime)

    async def ons_trace_get_result_async(
        self,
        request: main_models.OnsTraceGetResultRequest,
    ) -> main_models.OnsTraceGetResultResponse:
        runtime = RuntimeOptions()
        return await self.ons_trace_get_result_with_options_async(request, runtime)

    def ons_trace_query_by_msg_id_with_options(
        self,
        request: main_models.OnsTraceQueryByMsgIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTraceQueryByMsgIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTraceQueryByMsgId',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTraceQueryByMsgIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_trace_query_by_msg_id_with_options_async(
        self,
        request: main_models.OnsTraceQueryByMsgIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTraceQueryByMsgIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_id):
            query['MsgId'] = request.msg_id
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTraceQueryByMsgId',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTraceQueryByMsgIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_trace_query_by_msg_id(
        self,
        request: main_models.OnsTraceQueryByMsgIdRequest,
    ) -> main_models.OnsTraceQueryByMsgIdResponse:
        runtime = RuntimeOptions()
        return self.ons_trace_query_by_msg_id_with_options(request, runtime)

    async def ons_trace_query_by_msg_id_async(
        self,
        request: main_models.OnsTraceQueryByMsgIdRequest,
    ) -> main_models.OnsTraceQueryByMsgIdResponse:
        runtime = RuntimeOptions()
        return await self.ons_trace_query_by_msg_id_with_options_async(request, runtime)

    def ons_trace_query_by_msg_key_with_options(
        self,
        request: main_models.OnsTraceQueryByMsgKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTraceQueryByMsgKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_key):
            query['MsgKey'] = request.msg_key
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTraceQueryByMsgKey',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTraceQueryByMsgKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_trace_query_by_msg_key_with_options_async(
        self,
        request: main_models.OnsTraceQueryByMsgKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTraceQueryByMsgKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.msg_key):
            query['MsgKey'] = request.msg_key
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTraceQueryByMsgKey',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTraceQueryByMsgKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_trace_query_by_msg_key(
        self,
        request: main_models.OnsTraceQueryByMsgKeyRequest,
    ) -> main_models.OnsTraceQueryByMsgKeyResponse:
        runtime = RuntimeOptions()
        return self.ons_trace_query_by_msg_key_with_options(request, runtime)

    async def ons_trace_query_by_msg_key_async(
        self,
        request: main_models.OnsTraceQueryByMsgKeyRequest,
    ) -> main_models.OnsTraceQueryByMsgKeyResponse:
        runtime = RuntimeOptions()
        return await self.ons_trace_query_by_msg_key_with_options_async(request, runtime)

    def ons_trend_group_output_tps_with_options(
        self,
        request: main_models.OnsTrendGroupOutputTpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTrendGroupOutputTpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTrendGroupOutputTps',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTrendGroupOutputTpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_trend_group_output_tps_with_options_async(
        self,
        request: main_models.OnsTrendGroupOutputTpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTrendGroupOutputTpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTrendGroupOutputTps',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTrendGroupOutputTpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_trend_group_output_tps(
        self,
        request: main_models.OnsTrendGroupOutputTpsRequest,
    ) -> main_models.OnsTrendGroupOutputTpsResponse:
        runtime = RuntimeOptions()
        return self.ons_trend_group_output_tps_with_options(request, runtime)

    async def ons_trend_group_output_tps_async(
        self,
        request: main_models.OnsTrendGroupOutputTpsRequest,
    ) -> main_models.OnsTrendGroupOutputTpsResponse:
        runtime = RuntimeOptions()
        return await self.ons_trend_group_output_tps_with_options_async(request, runtime)

    def ons_trend_topic_input_tps_with_options(
        self,
        request: main_models.OnsTrendTopicInputTpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTrendTopicInputTpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTrendTopicInputTps',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTrendTopicInputTpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def ons_trend_topic_input_tps_with_options_async(
        self,
        request: main_models.OnsTrendTopicInputTpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnsTrendTopicInputTpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.topic):
            query['Topic'] = request.topic
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnsTrendTopicInputTps',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnsTrendTopicInputTpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def ons_trend_topic_input_tps(
        self,
        request: main_models.OnsTrendTopicInputTpsRequest,
    ) -> main_models.OnsTrendTopicInputTpsResponse:
        runtime = RuntimeOptions()
        return self.ons_trend_topic_input_tps_with_options(request, runtime)

    async def ons_trend_topic_input_tps_async(
        self,
        request: main_models.OnsTrendTopicInputTpsRequest,
    ) -> main_models.OnsTrendTopicInputTpsResponse:
        runtime = RuntimeOptions()
        return await self.ons_trend_topic_input_tps_with_options_async(request, runtime)

    def open_ons_service_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OpenOnsServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OpenOnsService',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenOnsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_ons_service_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OpenOnsServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OpenOnsService',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenOnsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_ons_service(self) -> main_models.OpenOnsServiceResponse:
        runtime = RuntimeOptions()
        return self.open_ons_service_with_options(runtime)

    async def open_ons_service_async(self) -> main_models.OpenOnsServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_ons_service_with_options_async(runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-02-14',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
