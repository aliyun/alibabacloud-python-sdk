# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_csasedr20241122 import models as main_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('csasedr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def describe_nsas_susp_event_type_with_options(
        self,
        request: main_models.DescribeNsasSuspEventTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNsasSuspEventTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not DaraCore.is_null(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNsasSuspEventType',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNsasSuspEventTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nsas_susp_event_type_with_options_async(
        self,
        request: main_models.DescribeNsasSuspEventTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNsasSuspEventTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not DaraCore.is_null(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.uuids):
            query['Uuids'] = request.uuids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNsasSuspEventType',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNsasSuspEventTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nsas_susp_event_type(
        self,
        request: main_models.DescribeNsasSuspEventTypeRequest,
    ) -> main_models.DescribeNsasSuspEventTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_nsas_susp_event_type_with_options(request, runtime)

    async def describe_nsas_susp_event_type_async(
        self,
        request: main_models.DescribeNsasSuspEventTypeRequest,
    ) -> main_models.DescribeNsasSuspEventTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_nsas_susp_event_type_with_options_async(request, runtime)

    def describe_security_event_operations_with_options(
        self,
        request: main_models.DescribeSecurityEventOperationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventOperations',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_event_operations_with_options_async(
        self,
        request: main_models.DescribeSecurityEventOperationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityEventOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.security_event_id):
            query['SecurityEventId'] = request.security_event_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityEventOperations',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityEventOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_event_operations(
        self,
        request: main_models.DescribeSecurityEventOperationsRequest,
    ) -> main_models.DescribeSecurityEventOperationsResponse:
        runtime = RuntimeOptions()
        return self.describe_security_event_operations_with_options(request, runtime)

    async def describe_security_event_operations_async(
        self,
        request: main_models.DescribeSecurityEventOperationsRequest,
    ) -> main_models.DescribeSecurityEventOperationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_event_operations_with_options_async(request, runtime)

    def describe_susp_events_with_options(
        self,
        request: main_models.DescribeSuspEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSuspEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_event_name):
            query['AlarmEventName'] = request.alarm_event_name
        if not DaraCore.is_null(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not DaraCore.is_null(request.assets_type_list):
            query['AssetsTypeList'] = request.assets_type_list
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not DaraCore.is_null(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dealed):
            query['Dealed'] = request.dealed
        if not DaraCore.is_null(request.department):
            query['Department'] = request.department
        if not DaraCore.is_null(request.event_names):
            query['EventNames'] = request.event_names
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.inner_ip):
            query['InnerIp'] = request.inner_ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.levels):
            query['Levels'] = request.levels
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.operate_error_code_list):
            query['OperateErrorCodeList'] = request.operate_error_code_list
        if not DaraCore.is_null(request.operate_time_end):
            query['OperateTimeEnd'] = request.operate_time_end
        if not DaraCore.is_null(request.operate_time_start):
            query['OperateTimeStart'] = request.operate_time_start
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_event_types):
            query['ParentEventTypes'] = request.parent_event_types
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.sort_column):
            query['SortColumn'] = request.sort_column
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.strict_mode):
            query['StrictMode'] = request.strict_mode
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.time_end):
            query['TimeEnd'] = request.time_end
        if not DaraCore.is_null(request.time_start):
            query['TimeStart'] = request.time_start
        if not DaraCore.is_null(request.unique_info):
            query['UniqueInfo'] = request.unique_info
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.uuids):
            query['Uuids'] = request.uuids
        body = {}
        if not DaraCore.is_null(request.tactic_id):
            body['TacticId'] = request.tactic_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSuspEvents',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSuspEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_susp_events_with_options_async(
        self,
        request: main_models.DescribeSuspEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSuspEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_event_name):
            query['AlarmEventName'] = request.alarm_event_name
        if not DaraCore.is_null(request.alarm_unique_info):
            query['AlarmUniqueInfo'] = request.alarm_unique_info
        if not DaraCore.is_null(request.assets_type_list):
            query['AssetsTypeList'] = request.assets_type_list
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.container_field_name):
            query['ContainerFieldName'] = request.container_field_name
        if not DaraCore.is_null(request.container_field_value):
            query['ContainerFieldValue'] = request.container_field_value
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.dealed):
            query['Dealed'] = request.dealed
        if not DaraCore.is_null(request.department):
            query['Department'] = request.department
        if not DaraCore.is_null(request.event_names):
            query['EventNames'] = request.event_names
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.inner_ip):
            query['InnerIp'] = request.inner_ip
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.levels):
            query['Levels'] = request.levels
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.operate_error_code_list):
            query['OperateErrorCodeList'] = request.operate_error_code_list
        if not DaraCore.is_null(request.operate_time_end):
            query['OperateTimeEnd'] = request.operate_time_end
        if not DaraCore.is_null(request.operate_time_start):
            query['OperateTimeStart'] = request.operate_time_start
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_event_types):
            query['ParentEventTypes'] = request.parent_event_types
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.sort_column):
            query['SortColumn'] = request.sort_column
        if not DaraCore.is_null(request.sort_type):
            query['SortType'] = request.sort_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not DaraCore.is_null(request.src_ip):
            query['SrcIp'] = request.src_ip
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.strict_mode):
            query['StrictMode'] = request.strict_mode
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.time_end):
            query['TimeEnd'] = request.time_end
        if not DaraCore.is_null(request.time_start):
            query['TimeStart'] = request.time_start
        if not DaraCore.is_null(request.unique_info):
            query['UniqueInfo'] = request.unique_info
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.uuids):
            query['Uuids'] = request.uuids
        body = {}
        if not DaraCore.is_null(request.tactic_id):
            body['TacticId'] = request.tactic_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSuspEvents',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSuspEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_susp_events(
        self,
        request: main_models.DescribeSuspEventsRequest,
    ) -> main_models.DescribeSuspEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_susp_events_with_options(request, runtime)

    async def describe_susp_events_async(
        self,
        request: main_models.DescribeSuspEventsRequest,
    ) -> main_models.DescribeSuspEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_susp_events_with_options_async(request, runtime)

    def handle_security_events_with_options(
        self,
        request: main_models.HandleSecurityEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HandleSecurityEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mark_batch):
            query['MarkBatch'] = request.mark_batch
        if not DaraCore.is_null(request.mark_miss_param):
            query['MarkMissParam'] = request.mark_miss_param
        if not DaraCore.is_null(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not DaraCore.is_null(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HandleSecurityEvents',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HandleSecurityEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def handle_security_events_with_options_async(
        self,
        request: main_models.HandleSecurityEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HandleSecurityEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.mark_batch):
            query['MarkBatch'] = request.mark_batch
        if not DaraCore.is_null(request.mark_miss_param):
            query['MarkMissParam'] = request.mark_miss_param
        if not DaraCore.is_null(request.operation_code):
            query['OperationCode'] = request.operation_code
        if not DaraCore.is_null(request.operation_params):
            query['OperationParams'] = request.operation_params
        if not DaraCore.is_null(request.remark):
            query['Remark'] = request.remark
        if not DaraCore.is_null(request.security_event_ids):
            query['SecurityEventIds'] = request.security_event_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HandleSecurityEvents',
            version = '2024-11-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HandleSecurityEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def handle_security_events(
        self,
        request: main_models.HandleSecurityEventsRequest,
    ) -> main_models.HandleSecurityEventsResponse:
        runtime = RuntimeOptions()
        return self.handle_security_events_with_options(request, runtime)

    async def handle_security_events_async(
        self,
        request: main_models.HandleSecurityEventsRequest,
    ) -> main_models.HandleSecurityEventsResponse:
        runtime = RuntimeOptions()
        return await self.handle_security_events_with_options_async(request, runtime)
