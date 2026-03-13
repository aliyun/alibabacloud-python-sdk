# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_pai20240521 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
        self._endpoint = self.get_endpoint('pai', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_quota_with_options(
        self,
        quota_id: str,
        request: main_models.GetQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuota',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(quota_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quota_with_options_async(
        self,
        quota_id: str,
        request: main_models.GetQuotaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQuota',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/{DaraURL.percent_encode(quota_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quota(
        self,
        quota_id: str,
        request: main_models.GetQuotaRequest,
    ) -> main_models.GetQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_quota_with_options(quota_id, request, headers, runtime)

    async def get_quota_async(
        self,
        quota_id: str,
        request: main_models.GetQuotaRequest,
    ) -> main_models.GetQuotaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_quota_with_options_async(quota_id, request, headers, runtime)

    def get_resource_group_with_options(
        self,
        resource_group_id: str,
        tmp_req: main_models.GetResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupResponse:
        tmp_req.validate()
        request = main_models.GetResourceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.is_aiworkspace_data_enabled):
            query['IsAIWorkspaceDataEnabled'] = request.is_aiworkspace_data_enabled
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroup',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_with_options_async(
        self,
        resource_group_id: str,
        tmp_req: main_models.GetResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupResponse:
        tmp_req.validate()
        request = main_models.GetResourceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.is_aiworkspace_data_enabled):
            query['IsAIWorkspaceDataEnabled'] = request.is_aiworkspace_data_enabled
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroup',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group(
        self,
        resource_group_id: str,
        request: main_models.GetResourceGroupRequest,
    ) -> main_models.GetResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_group_with_options(resource_group_id, request, headers, runtime)

    async def get_resource_group_async(
        self,
        resource_group_id: str,
        request: main_models.GetResourceGroupRequest,
    ) -> main_models.GetResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_group_with_options_async(resource_group_id, request, headers, runtime)

    def get_resource_group_machine_group_with_options(
        self,
        machine_group_id: str,
        resource_group_id: str,
        tmp_req: main_models.GetResourceGroupMachineGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupMachineGroupResponse:
        tmp_req.validate()
        request = main_models.GetResourceGroupMachineGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupMachineGroup',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/machinegroups/{DaraURL.percent_encode(machine_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupMachineGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_machine_group_with_options_async(
        self,
        machine_group_id: str,
        resource_group_id: str,
        tmp_req: main_models.GetResourceGroupMachineGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupMachineGroupResponse:
        tmp_req.validate()
        request = main_models.GetResourceGroupMachineGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupMachineGroup',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/machinegroups/{DaraURL.percent_encode(machine_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupMachineGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_machine_group(
        self,
        machine_group_id: str,
        resource_group_id: str,
        request: main_models.GetResourceGroupMachineGroupRequest,
    ) -> main_models.GetResourceGroupMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_group_machine_group_with_options(machine_group_id, resource_group_id, request, headers, runtime)

    async def get_resource_group_machine_group_async(
        self,
        machine_group_id: str,
        resource_group_id: str,
        request: main_models.GetResourceGroupMachineGroupRequest,
    ) -> main_models.GetResourceGroupMachineGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_group_machine_group_with_options_async(machine_group_id, resource_group_id, request, headers, runtime)

    def get_resource_group_request_with_options(
        self,
        request: main_models.GetResourceGroupRequestRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pod_status):
            query['PodStatus'] = request.pod_status
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupID'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupRequest',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/data/request',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupRequestResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_request_with_options_async(
        self,
        request: main_models.GetResourceGroupRequestRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupRequestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pod_status):
            query['PodStatus'] = request.pod_status
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupID'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupRequest',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/data/request',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupRequestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_request(
        self,
        request: main_models.GetResourceGroupRequestRequest,
    ) -> main_models.GetResourceGroupRequestResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_group_request_with_options(request, headers, runtime)

    async def get_resource_group_request_async(
        self,
        request: main_models.GetResourceGroupRequestRequest,
    ) -> main_models.GetResourceGroupRequestResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_group_request_with_options_async(request, headers, runtime)

    def get_resource_group_total_with_options(
        self,
        request: main_models.GetResourceGroupTotalRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupTotalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupID'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupTotal',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/data/total',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupTotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_group_total_with_options_async(
        self,
        request: main_models.GetResourceGroupTotalRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceGroupTotalResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupID'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceGroupTotal',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/data/total',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceGroupTotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_group_total(
        self,
        request: main_models.GetResourceGroupTotalRequest,
    ) -> main_models.GetResourceGroupTotalResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_group_total_with_options(request, headers, runtime)

    async def get_resource_group_total_async(
        self,
        request: main_models.GetResourceGroupTotalRequest,
    ) -> main_models.GetResourceGroupTotalResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_group_total_with_options_async(request, headers, runtime)

    def get_user_ali_uid_by_instance_id_with_options(
        self,
        resource_instance_id: str,
        request: main_models.GetUserAliUidByInstanceIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAliUidByInstanceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_uid):
            query['ResourceOwnerUid'] = request.resource_owner_uid
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserAliUidByInstanceId',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/inner/pods/{DaraURL.percent_encode(resource_instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAliUidByInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_ali_uid_by_instance_id_with_options_async(
        self,
        resource_instance_id: str,
        request: main_models.GetUserAliUidByInstanceIdRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserAliUidByInstanceIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_uid):
            query['ResourceOwnerUid'] = request.resource_owner_uid
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserAliUidByInstanceId',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/inner/pods/{DaraURL.percent_encode(resource_instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserAliUidByInstanceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_ali_uid_by_instance_id(
        self,
        resource_instance_id: str,
        request: main_models.GetUserAliUidByInstanceIdRequest,
    ) -> main_models.GetUserAliUidByInstanceIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_ali_uid_by_instance_id_with_options(resource_instance_id, request, headers, runtime)

    async def get_user_ali_uid_by_instance_id_async(
        self,
        resource_instance_id: str,
        request: main_models.GetUserAliUidByInstanceIdRequest,
    ) -> main_models.GetUserAliUidByInstanceIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_ali_uid_by_instance_id_with_options_async(resource_instance_id, request, headers, runtime)

    def get_user_view_metrics_with_options(
        self,
        resource_group_id: str,
        request: main_models.GetUserViewMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserViewMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserViewMetrics',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/usermetrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserViewMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_view_metrics_with_options_async(
        self,
        resource_group_id: str,
        request: main_models.GetUserViewMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserViewMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.time_step):
            query['TimeStep'] = request.time_step
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserViewMetrics',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/usermetrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserViewMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_view_metrics(
        self,
        resource_group_id: str,
        request: main_models.GetUserViewMetricsRequest,
    ) -> main_models.GetUserViewMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_view_metrics_with_options(resource_group_id, request, headers, runtime)

    async def get_user_view_metrics_async(
        self,
        resource_group_id: str,
        request: main_models.GetUserViewMetricsRequest,
    ) -> main_models.GetUserViewMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_view_metrics_with_options_async(resource_group_id, request, headers, runtime)

    def list_data_cache_services_with_options(
        self,
        request: main_models.ListDataCacheServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCacheServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCacheServices',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/caches',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCacheServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_cache_services_with_options_async(
        self,
        request: main_models.ListDataCacheServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDataCacheServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataCacheServices',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/caches',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataCacheServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_cache_services(
        self,
        request: main_models.ListDataCacheServicesRequest,
    ) -> main_models.ListDataCacheServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_data_cache_services_with_options(request, headers, runtime)

    async def list_data_cache_services_async(
        self,
        request: main_models.ListDataCacheServicesRequest,
    ) -> main_models.ListDataCacheServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_data_cache_services_with_options_async(request, headers, runtime)

    def list_nodes_with_options(
        self,
        tmp_req: main_models.ListNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        tmp_req.validate()
        request = main_models.ListNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.health_count):
            request.health_count_shrink = Utils.array_to_string_with_specified_style(tmp_req.health_count, 'HealthCount', 'json')
        if not DaraCore.is_null(tmp_req.health_rate):
            request.health_rate_shrink = Utils.array_to_string_with_specified_style(tmp_req.health_rate, 'HealthRate', 'json')
        query = {}
        if not DaraCore.is_null(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not DaraCore.is_null(request.availability_zone):
            query['AvailabilityZone'] = request.availability_zone
        if not DaraCore.is_null(request.clique_id):
            query['CliqueID'] = request.clique_id
        if not DaraCore.is_null(request.filter_by_quota_id):
            query['FilterByQuotaId'] = request.filter_by_quota_id
        if not DaraCore.is_null(request.filter_by_resource_group_ids):
            query['FilterByResourceGroupIds'] = request.filter_by_resource_group_ids
        if not DaraCore.is_null(request.gputype):
            query['GPUType'] = request.gputype
        if not DaraCore.is_null(request.health_count_shrink):
            query['HealthCount'] = request.health_count_shrink
        if not DaraCore.is_null(request.health_rate_shrink):
            query['HealthRate'] = request.health_rate_shrink
        if not DaraCore.is_null(request.hyper_node):
            query['HyperNode'] = request.hyper_node
        if not DaraCore.is_null(request.hyper_zone):
            query['HyperZone'] = request.hyper_zone
        if not DaraCore.is_null(request.layout_mode):
            query['LayoutMode'] = request.layout_mode
        if not DaraCore.is_null(request.machine_group_ids):
            query['MachineGroupIds'] = request.machine_group_ids
        if not DaraCore.is_null(request.node_names):
            query['NodeNames'] = request.node_names
        if not DaraCore.is_null(request.node_statuses):
            query['NodeStatuses'] = request.node_statuses
        if not DaraCore.is_null(request.node_types):
            query['NodeTypes'] = request.node_types
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_instance_ids):
            query['OrderInstanceIds'] = request.order_instance_ids
        if not DaraCore.is_null(request.order_statuses):
            query['OrderStatuses'] = request.order_statuses
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.reason_codes):
            query['ReasonCodes'] = request.reason_codes
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        tmp_req: main_models.ListNodesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        tmp_req.validate()
        request = main_models.ListNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.health_count):
            request.health_count_shrink = Utils.array_to_string_with_specified_style(tmp_req.health_count, 'HealthCount', 'json')
        if not DaraCore.is_null(tmp_req.health_rate):
            request.health_rate_shrink = Utils.array_to_string_with_specified_style(tmp_req.health_rate, 'HealthRate', 'json')
        query = {}
        if not DaraCore.is_null(request.accelerator_type):
            query['AcceleratorType'] = request.accelerator_type
        if not DaraCore.is_null(request.availability_zone):
            query['AvailabilityZone'] = request.availability_zone
        if not DaraCore.is_null(request.clique_id):
            query['CliqueID'] = request.clique_id
        if not DaraCore.is_null(request.filter_by_quota_id):
            query['FilterByQuotaId'] = request.filter_by_quota_id
        if not DaraCore.is_null(request.filter_by_resource_group_ids):
            query['FilterByResourceGroupIds'] = request.filter_by_resource_group_ids
        if not DaraCore.is_null(request.gputype):
            query['GPUType'] = request.gputype
        if not DaraCore.is_null(request.health_count_shrink):
            query['HealthCount'] = request.health_count_shrink
        if not DaraCore.is_null(request.health_rate_shrink):
            query['HealthRate'] = request.health_rate_shrink
        if not DaraCore.is_null(request.hyper_node):
            query['HyperNode'] = request.hyper_node
        if not DaraCore.is_null(request.hyper_zone):
            query['HyperZone'] = request.hyper_zone
        if not DaraCore.is_null(request.layout_mode):
            query['LayoutMode'] = request.layout_mode
        if not DaraCore.is_null(request.machine_group_ids):
            query['MachineGroupIds'] = request.machine_group_ids
        if not DaraCore.is_null(request.node_names):
            query['NodeNames'] = request.node_names
        if not DaraCore.is_null(request.node_statuses):
            query['NodeStatuses'] = request.node_statuses
        if not DaraCore.is_null(request.node_types):
            query['NodeTypes'] = request.node_types
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_instance_ids):
            query['OrderInstanceIds'] = request.order_instance_ids
        if not DaraCore.is_null(request.order_statuses):
            query['OrderStatuses'] = request.order_statuses
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.quota_id):
            query['QuotaId'] = request.quota_id
        if not DaraCore.is_null(request.reason_codes):
            query['ReasonCodes'] = request.reason_codes
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/nodes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_nodes_with_options(request, headers, runtime)

    async def list_nodes_async(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_nodes_with_options_async(request, headers, runtime)

    def list_quotas_with_options(
        self,
        request: main_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.layout_mode):
            query['LayoutMode'] = request.layout_mode
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_quota_id):
            query['ParentQuotaId'] = request.parent_quota_id
        if not DaraCore.is_null(request.quota_ids):
            query['QuotaIds'] = request.quota_ids
        if not DaraCore.is_null(request.quota_name):
            query['QuotaName'] = request.quota_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.statuses):
            query['Statuses'] = request.statuses
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotas',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quotas_with_options_async(
        self,
        request: main_models.ListQuotasRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListQuotasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.layout_mode):
            query['LayoutMode'] = request.layout_mode
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_quota_id):
            query['ParentQuotaId'] = request.parent_quota_id
        if not DaraCore.is_null(request.quota_ids):
            query['QuotaIds'] = request.quota_ids
        if not DaraCore.is_null(request.quota_name):
            query['QuotaName'] = request.quota_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.statuses):
            query['Statuses'] = request.statuses
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        if not DaraCore.is_null(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        if not DaraCore.is_null(request.workspace_name):
            query['WorkspaceName'] = request.workspace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQuotas',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/quotas/',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quotas(
        self,
        request: main_models.ListQuotasRequest,
    ) -> main_models.ListQuotasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_quotas_with_options(request, headers, runtime)

    async def list_quotas_async(
        self,
        request: main_models.ListQuotasRequest,
    ) -> main_models.ListQuotasResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_quotas_with_options_async(request, headers, runtime)

    def list_resource_group_machine_groups_with_options(
        self,
        resource_group_id: str,
        request: main_models.ListResourceGroupMachineGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupMachineGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator_id):
            query['CreatorID'] = request.creator_id
        if not DaraCore.is_null(request.ecs_spec):
            query['EcsSpec'] = request.ecs_spec
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_instance_id):
            query['OrderInstanceId'] = request.order_instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_duration):
            query['PaymentDuration'] = request.payment_duration
        if not DaraCore.is_null(request.payment_duration_unit):
            query['PaymentDurationUnit'] = request.payment_duration_unit
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroupMachineGroups',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/machinegroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupMachineGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_group_machine_groups_with_options_async(
        self,
        resource_group_id: str,
        request: main_models.ListResourceGroupMachineGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupMachineGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creator_id):
            query['CreatorID'] = request.creator_id
        if not DaraCore.is_null(request.ecs_spec):
            query['EcsSpec'] = request.ecs_spec
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_instance_id):
            query['OrderInstanceId'] = request.order_instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.payment_duration):
            query['PaymentDuration'] = request.payment_duration
        if not DaraCore.is_null(request.payment_duration_unit):
            query['PaymentDurationUnit'] = request.payment_duration_unit
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroupMachineGroups',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources/{DaraURL.percent_encode(resource_group_id)}/machinegroups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupMachineGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_group_machine_groups(
        self,
        resource_group_id: str,
        request: main_models.ListResourceGroupMachineGroupsRequest,
    ) -> main_models.ListResourceGroupMachineGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resource_group_machine_groups_with_options(resource_group_id, request, headers, runtime)

    async def list_resource_group_machine_groups_async(
        self,
        resource_group_id: str,
        request: main_models.ListResourceGroupMachineGroupsRequest,
    ) -> main_models.ListResourceGroupMachineGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resource_group_machine_groups_with_options_async(resource_group_id, request, headers, runtime)

    def list_resource_groups_with_options(
        self,
        request: main_models.ListResourceGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.computing_resource_provider):
            query['ComputingResourceProvider'] = request.computing_resource_provider
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.show_all):
            query['ShowAll'] = request.show_all
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroups',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_groups_with_options_async(
        self,
        request: main_models.ListResourceGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.computing_resource_provider):
            query['ComputingResourceProvider'] = request.computing_resource_provider
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.show_all):
            query['ShowAll'] = request.show_all
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceGroups',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_groups(
        self,
        request: main_models.ListResourceGroupsRequest,
    ) -> main_models.ListResourceGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resource_groups_with_options(request, headers, runtime)

    async def list_resource_groups_async(
        self,
        request: main_models.ListResourceGroupsRequest,
    ) -> main_models.ListResourceGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resource_groups_with_options_async(request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/inner/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/inner/tags',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def tag_resources_system_tags_with_options(
        self,
        request: main_models.TagResourcesSystemTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesSystemTagsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scope):
            body['Scope'] = request.scope
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.tag_owner_uid):
            body['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResourcesSystemTags',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/inner/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesSystemTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_system_tags_with_options_async(
        self,
        request: main_models.TagResourcesSystemTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesSystemTagsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scope):
            body['Scope'] = request.scope
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.tag_owner_uid):
            body['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResourcesSystemTags',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/inner/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesSystemTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources_system_tags(
        self,
        request: main_models.TagResourcesSystemTagsRequest,
    ) -> main_models.TagResourcesSystemTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.tag_resources_system_tags_with_options(request, headers, runtime)

    async def tag_resources_system_tags_async(
        self,
        request: main_models.TagResourcesSystemTagsRequest,
    ) -> main_models.TagResourcesSystemTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.tag_resources_system_tags_with_options_async(request, headers, runtime)

    def untag_resources_system_tags_with_options(
        self,
        tmp_req: main_models.UntagResourcesSystemTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesSystemTagsResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesSystemTagsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        if not DaraCore.is_null(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResourcesSystemTags',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/inner/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesSystemTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_system_tags_with_options_async(
        self,
        tmp_req: main_models.UntagResourcesSystemTagsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesSystemTagsResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesSystemTagsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_id):
            request.resource_id_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not DaraCore.is_null(tmp_req.tag_key):
            request.tag_key_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        if not DaraCore.is_null(request.tag_owner_uid):
            query['TagOwnerUid'] = request.tag_owner_uid
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResourcesSystemTags',
            version = '2024-05-21',
            protocol = 'HTTPS',
            pathname = f'/api/v1/inner/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesSystemTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources_system_tags(
        self,
        request: main_models.UntagResourcesSystemTagsRequest,
    ) -> main_models.UntagResourcesSystemTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.untag_resources_system_tags_with_options(request, headers, runtime)

    async def untag_resources_system_tags_async(
        self,
        request: main_models.UntagResourcesSystemTagsRequest,
    ) -> main_models.UntagResourcesSystemTagsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.untag_resources_system_tags_with_options_async(request, headers, runtime)
