# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_nas20170626 import models as main_models
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
            'cn-hangzhou-finance': 'nas.cn-hangzhou-dg-a01.aliyuncs.com',
            'ap-northeast-2-pop': 'nas.aliyuncs.com',
            'ap-southeast-2': 'nas.aliyuncs.com',
            'cn-beijing-finance-pop': 'nas.aliyuncs.com',
            'cn-beijing-gov-1': 'nas.aliyuncs.com',
            'cn-beijing-nu16-b01': 'nas.aliyuncs.com',
            'cn-edge-1': 'nas.aliyuncs.com',
            'cn-fujian': 'nas.aliyuncs.com',
            'cn-haidian-cm12-c01': 'nas.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'nas.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'nas.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'nas.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'nas.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'nas.aliyuncs.com',
            'cn-hangzhou-test-306': 'nas.aliyuncs.com',
            'cn-hongkong-finance-pop': 'nas.aliyuncs.com',
            'cn-qingdao-nebula': 'nas.aliyuncs.com',
            'cn-shanghai-et15-b01': 'nas.aliyuncs.com',
            'cn-shanghai-et2-b01': 'nas.aliyuncs.com',
            'cn-shanghai-inner': 'nas.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'nas.aliyuncs.com',
            'cn-shenzhen-inner': 'nas.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'nas.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'nas.aliyuncs.com',
            'cn-wuhan': 'nas.aliyuncs.com',
            'cn-yushanfang': 'nas.aliyuncs.com',
            'cn-zhangbei': 'nas.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'nas.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'nas.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'nas.aliyuncs.com',
            'eu-west-1-oxs': 'nas.aliyuncs.com',
            'rus-west-1-pop': 'nas.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('nas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_client_to_black_list_with_options(
        self,
        request: main_models.AddClientToBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddClientToBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddClientToBlackList',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddClientToBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_client_to_black_list_with_options_async(
        self,
        request: main_models.AddClientToBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddClientToBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddClientToBlackList',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddClientToBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_client_to_black_list(
        self,
        request: main_models.AddClientToBlackListRequest,
    ) -> main_models.AddClientToBlackListResponse:
        runtime = RuntimeOptions()
        return self.add_client_to_black_list_with_options(request, runtime)

    async def add_client_to_black_list_async(
        self,
        request: main_models.AddClientToBlackListRequest,
    ) -> main_models.AddClientToBlackListResponse:
        runtime = RuntimeOptions()
        return await self.add_client_to_black_list_with_options_async(request, runtime)

    def apply_auto_snapshot_policy_with_options(
        self,
        request: main_models.ApplyAutoSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyAutoSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not DaraCore.is_null(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyAutoSnapshotPolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_auto_snapshot_policy_with_options_async(
        self,
        request: main_models.ApplyAutoSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyAutoSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not DaraCore.is_null(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyAutoSnapshotPolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_auto_snapshot_policy(
        self,
        request: main_models.ApplyAutoSnapshotPolicyRequest,
    ) -> main_models.ApplyAutoSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return self.apply_auto_snapshot_policy_with_options(request, runtime)

    async def apply_auto_snapshot_policy_async(
        self,
        request: main_models.ApplyAutoSnapshotPolicyRequest,
    ) -> main_models.ApplyAutoSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return await self.apply_auto_snapshot_policy_with_options_async(request, runtime)

    def apply_data_flow_auto_refresh_with_options(
        self,
        request: main_models.ApplyDataFlowAutoRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyDataFlowAutoRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not DaraCore.is_null(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not DaraCore.is_null(request.auto_refreshs):
            query['AutoRefreshs'] = request.auto_refreshs
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyDataFlowAutoRefresh',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyDataFlowAutoRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_data_flow_auto_refresh_with_options_async(
        self,
        request: main_models.ApplyDataFlowAutoRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyDataFlowAutoRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not DaraCore.is_null(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not DaraCore.is_null(request.auto_refreshs):
            query['AutoRefreshs'] = request.auto_refreshs
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyDataFlowAutoRefresh',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyDataFlowAutoRefreshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_data_flow_auto_refresh(
        self,
        request: main_models.ApplyDataFlowAutoRefreshRequest,
    ) -> main_models.ApplyDataFlowAutoRefreshResponse:
        runtime = RuntimeOptions()
        return self.apply_data_flow_auto_refresh_with_options(request, runtime)

    async def apply_data_flow_auto_refresh_async(
        self,
        request: main_models.ApplyDataFlowAutoRefreshRequest,
    ) -> main_models.ApplyDataFlowAutoRefreshResponse:
        runtime = RuntimeOptions()
        return await self.apply_data_flow_auto_refresh_with_options_async(request, runtime)

    def attach_vsc_to_filesystems_with_options(
        self,
        request: main_models.AttachVscToFilesystemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachVscToFilesystemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachVscToFilesystems',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachVscToFilesystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_vsc_to_filesystems_with_options_async(
        self,
        request: main_models.AttachVscToFilesystemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachVscToFilesystemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachVscToFilesystems',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachVscToFilesystemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_vsc_to_filesystems(
        self,
        request: main_models.AttachVscToFilesystemsRequest,
    ) -> main_models.AttachVscToFilesystemsResponse:
        runtime = RuntimeOptions()
        return self.attach_vsc_to_filesystems_with_options(request, runtime)

    async def attach_vsc_to_filesystems_async(
        self,
        request: main_models.AttachVscToFilesystemsRequest,
    ) -> main_models.AttachVscToFilesystemsResponse:
        runtime = RuntimeOptions()
        return await self.attach_vsc_to_filesystems_with_options_async(request, runtime)

    def cancel_auto_snapshot_policy_with_options(
        self,
        request: main_models.CancelAutoSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAutoSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAutoSnapshotPolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_auto_snapshot_policy_with_options_async(
        self,
        request: main_models.CancelAutoSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAutoSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAutoSnapshotPolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_auto_snapshot_policy(
        self,
        request: main_models.CancelAutoSnapshotPolicyRequest,
    ) -> main_models.CancelAutoSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return self.cancel_auto_snapshot_policy_with_options(request, runtime)

    async def cancel_auto_snapshot_policy_async(
        self,
        request: main_models.CancelAutoSnapshotPolicyRequest,
    ) -> main_models.CancelAutoSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return await self.cancel_auto_snapshot_policy_with_options_async(request, runtime)

    def cancel_data_flow_auto_refresh_with_options(
        self,
        request: main_models.CancelDataFlowAutoRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelDataFlowAutoRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.refresh_path):
            query['RefreshPath'] = request.refresh_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelDataFlowAutoRefresh',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDataFlowAutoRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_data_flow_auto_refresh_with_options_async(
        self,
        request: main_models.CancelDataFlowAutoRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelDataFlowAutoRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.refresh_path):
            query['RefreshPath'] = request.refresh_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelDataFlowAutoRefresh',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDataFlowAutoRefreshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_data_flow_auto_refresh(
        self,
        request: main_models.CancelDataFlowAutoRefreshRequest,
    ) -> main_models.CancelDataFlowAutoRefreshResponse:
        runtime = RuntimeOptions()
        return self.cancel_data_flow_auto_refresh_with_options(request, runtime)

    async def cancel_data_flow_auto_refresh_async(
        self,
        request: main_models.CancelDataFlowAutoRefreshRequest,
    ) -> main_models.CancelDataFlowAutoRefreshResponse:
        runtime = RuntimeOptions()
        return await self.cancel_data_flow_auto_refresh_with_options_async(request, runtime)

    def cancel_data_flow_sub_task_with_options(
        self,
        request: main_models.CancelDataFlowSubTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelDataFlowSubTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.data_flow_sub_task_id):
            query['DataFlowSubTaskId'] = request.data_flow_sub_task_id
        if not DaraCore.is_null(request.data_flow_task_id):
            query['DataFlowTaskId'] = request.data_flow_task_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelDataFlowSubTask',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDataFlowSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_data_flow_sub_task_with_options_async(
        self,
        request: main_models.CancelDataFlowSubTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelDataFlowSubTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.data_flow_sub_task_id):
            query['DataFlowSubTaskId'] = request.data_flow_sub_task_id
        if not DaraCore.is_null(request.data_flow_task_id):
            query['DataFlowTaskId'] = request.data_flow_task_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelDataFlowSubTask',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDataFlowSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_data_flow_sub_task(
        self,
        request: main_models.CancelDataFlowSubTaskRequest,
    ) -> main_models.CancelDataFlowSubTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_data_flow_sub_task_with_options(request, runtime)

    async def cancel_data_flow_sub_task_async(
        self,
        request: main_models.CancelDataFlowSubTaskRequest,
    ) -> main_models.CancelDataFlowSubTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_data_flow_sub_task_with_options_async(request, runtime)

    def cancel_data_flow_task_with_options(
        self,
        request: main_models.CancelDataFlowTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelDataFlowTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelDataFlowTask',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDataFlowTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_data_flow_task_with_options_async(
        self,
        request: main_models.CancelDataFlowTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelDataFlowTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelDataFlowTask',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDataFlowTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_data_flow_task(
        self,
        request: main_models.CancelDataFlowTaskRequest,
    ) -> main_models.CancelDataFlowTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_data_flow_task_with_options(request, runtime)

    async def cancel_data_flow_task_async(
        self,
        request: main_models.CancelDataFlowTaskRequest,
    ) -> main_models.CancelDataFlowTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_data_flow_task_with_options_async(request, runtime)

    def cancel_dir_quota_with_options(
        self,
        request: main_models.CancelDirQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelDirQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelDirQuota',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDirQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_dir_quota_with_options_async(
        self,
        request: main_models.CancelDirQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelDirQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelDirQuota',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelDirQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_dir_quota(
        self,
        request: main_models.CancelDirQuotaRequest,
    ) -> main_models.CancelDirQuotaResponse:
        runtime = RuntimeOptions()
        return self.cancel_dir_quota_with_options(request, runtime)

    async def cancel_dir_quota_async(
        self,
        request: main_models.CancelDirQuotaRequest,
    ) -> main_models.CancelDirQuotaResponse:
        runtime = RuntimeOptions()
        return await self.cancel_dir_quota_with_options_async(request, runtime)

    def cancel_fileset_quota_with_options(
        self,
        request: main_models.CancelFilesetQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelFilesetQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelFilesetQuota',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelFilesetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_fileset_quota_with_options_async(
        self,
        request: main_models.CancelFilesetQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelFilesetQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelFilesetQuota',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelFilesetQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_fileset_quota(
        self,
        request: main_models.CancelFilesetQuotaRequest,
    ) -> main_models.CancelFilesetQuotaResponse:
        runtime = RuntimeOptions()
        return self.cancel_fileset_quota_with_options(request, runtime)

    async def cancel_fileset_quota_async(
        self,
        request: main_models.CancelFilesetQuotaRequest,
    ) -> main_models.CancelFilesetQuotaResponse:
        runtime = RuntimeOptions()
        return await self.cancel_fileset_quota_with_options_async(request, runtime)

    def cancel_lifecycle_retrieve_job_with_options(
        self,
        request: main_models.CancelLifecycleRetrieveJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelLifecycleRetrieveJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelLifecycleRetrieveJob',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelLifecycleRetrieveJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_lifecycle_retrieve_job_with_options_async(
        self,
        request: main_models.CancelLifecycleRetrieveJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelLifecycleRetrieveJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelLifecycleRetrieveJob',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelLifecycleRetrieveJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_lifecycle_retrieve_job(
        self,
        request: main_models.CancelLifecycleRetrieveJobRequest,
    ) -> main_models.CancelLifecycleRetrieveJobResponse:
        runtime = RuntimeOptions()
        return self.cancel_lifecycle_retrieve_job_with_options(request, runtime)

    async def cancel_lifecycle_retrieve_job_async(
        self,
        request: main_models.CancelLifecycleRetrieveJobRequest,
    ) -> main_models.CancelLifecycleRetrieveJobResponse:
        runtime = RuntimeOptions()
        return await self.cancel_lifecycle_retrieve_job_with_options_async(request, runtime)

    def cancel_recycle_bin_job_with_options(
        self,
        request: main_models.CancelRecycleBinJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRecycleBinJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelRecycleBinJob',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRecycleBinJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_recycle_bin_job_with_options_async(
        self,
        request: main_models.CancelRecycleBinJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRecycleBinJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelRecycleBinJob',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRecycleBinJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_recycle_bin_job(
        self,
        request: main_models.CancelRecycleBinJobRequest,
    ) -> main_models.CancelRecycleBinJobResponse:
        runtime = RuntimeOptions()
        return self.cancel_recycle_bin_job_with_options(request, runtime)

    async def cancel_recycle_bin_job_async(
        self,
        request: main_models.CancelRecycleBinJobRequest,
    ) -> main_models.CancelRecycleBinJobResponse:
        runtime = RuntimeOptions()
        return await self.cancel_recycle_bin_job_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_access_group_with_options(
        self,
        request: main_models.CreateAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.access_group_type):
            query['AccessGroupType'] = request.access_group_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessGroup',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_group_with_options_async(
        self,
        request: main_models.CreateAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.access_group_type):
            query['AccessGroupType'] = request.access_group_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessGroup',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_group(
        self,
        request: main_models.CreateAccessGroupRequest,
    ) -> main_models.CreateAccessGroupResponse:
        runtime = RuntimeOptions()
        return self.create_access_group_with_options(request, runtime)

    async def create_access_group_async(
        self,
        request: main_models.CreateAccessGroupRequest,
    ) -> main_models.CreateAccessGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_access_group_with_options_async(request, runtime)

    def create_access_point_with_options(
        self,
        request: main_models.CreateAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group):
            query['AccessGroup'] = request.access_group
        if not DaraCore.is_null(request.access_point_name):
            query['AccessPointName'] = request.access_point_name
        if not DaraCore.is_null(request.enabled_ram):
            query['EnabledRam'] = request.enabled_ram
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.owner_group_id):
            query['OwnerGroupId'] = request.owner_group_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not DaraCore.is_null(request.permission):
            query['Permission'] = request.permission
        if not DaraCore.is_null(request.posix_group_id):
            query['PosixGroupId'] = request.posix_group_id
        if not DaraCore.is_null(request.posix_secondary_group_ids):
            query['PosixSecondaryGroupIds'] = request.posix_secondary_group_ids
        if not DaraCore.is_null(request.posix_user_id):
            query['PosixUserId'] = request.posix_user_id
        if not DaraCore.is_null(request.root_directory):
            query['RootDirectory'] = request.root_directory
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vsw_id):
            query['VswId'] = request.vsw_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessPoint',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_point_with_options_async(
        self,
        request: main_models.CreateAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group):
            query['AccessGroup'] = request.access_group
        if not DaraCore.is_null(request.access_point_name):
            query['AccessPointName'] = request.access_point_name
        if not DaraCore.is_null(request.enabled_ram):
            query['EnabledRam'] = request.enabled_ram
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.owner_group_id):
            query['OwnerGroupId'] = request.owner_group_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not DaraCore.is_null(request.permission):
            query['Permission'] = request.permission
        if not DaraCore.is_null(request.posix_group_id):
            query['PosixGroupId'] = request.posix_group_id
        if not DaraCore.is_null(request.posix_secondary_group_ids):
            query['PosixSecondaryGroupIds'] = request.posix_secondary_group_ids
        if not DaraCore.is_null(request.posix_user_id):
            query['PosixUserId'] = request.posix_user_id
        if not DaraCore.is_null(request.root_directory):
            query['RootDirectory'] = request.root_directory
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vsw_id):
            query['VswId'] = request.vsw_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessPoint',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_point(
        self,
        request: main_models.CreateAccessPointRequest,
    ) -> main_models.CreateAccessPointResponse:
        runtime = RuntimeOptions()
        return self.create_access_point_with_options(request, runtime)

    async def create_access_point_async(
        self,
        request: main_models.CreateAccessPointRequest,
    ) -> main_models.CreateAccessPointResponse:
        runtime = RuntimeOptions()
        return await self.create_access_point_with_options_async(request, runtime)

    def create_access_rule_with_options(
        self,
        request: main_models.CreateAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        if not DaraCore.is_null(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not DaraCore.is_null(request.user_access_type):
            query['UserAccessType'] = request.user_access_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessRule',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_rule_with_options_async(
        self,
        request: main_models.CreateAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        if not DaraCore.is_null(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not DaraCore.is_null(request.user_access_type):
            query['UserAccessType'] = request.user_access_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccessRule',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_rule(
        self,
        request: main_models.CreateAccessRuleRequest,
    ) -> main_models.CreateAccessRuleResponse:
        runtime = RuntimeOptions()
        return self.create_access_rule_with_options(request, runtime)

    async def create_access_rule_async(
        self,
        request: main_models.CreateAccessRuleRequest,
    ) -> main_models.CreateAccessRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_access_rule_with_options_async(request, runtime)

    def create_auto_snapshot_policy_with_options(
        self,
        request: main_models.CreateAutoSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAutoSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_snapshot_policy_name):
            query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.repeat_weekdays):
            query['RepeatWeekdays'] = request.repeat_weekdays
        if not DaraCore.is_null(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not DaraCore.is_null(request.time_points):
            query['TimePoints'] = request.time_points
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAutoSnapshotPolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auto_snapshot_policy_with_options_async(
        self,
        request: main_models.CreateAutoSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAutoSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_snapshot_policy_name):
            query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.repeat_weekdays):
            query['RepeatWeekdays'] = request.repeat_weekdays
        if not DaraCore.is_null(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not DaraCore.is_null(request.time_points):
            query['TimePoints'] = request.time_points
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAutoSnapshotPolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_auto_snapshot_policy(
        self,
        request: main_models.CreateAutoSnapshotPolicyRequest,
    ) -> main_models.CreateAutoSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_auto_snapshot_policy_with_options(request, runtime)

    async def create_auto_snapshot_policy_async(
        self,
        request: main_models.CreateAutoSnapshotPolicyRequest,
    ) -> main_models.CreateAutoSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_auto_snapshot_policy_with_options_async(request, runtime)

    def create_data_flow_with_options(
        self,
        request: main_models.CreateDataFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not DaraCore.is_null(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not DaraCore.is_null(request.auto_refreshs):
            query['AutoRefreshs'] = request.auto_refreshs
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.file_system_path):
            query['FileSystemPath'] = request.file_system_path
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        if not DaraCore.is_null(request.source_security_type):
            query['SourceSecurityType'] = request.source_security_type
        if not DaraCore.is_null(request.source_storage):
            query['SourceStorage'] = request.source_storage
        if not DaraCore.is_null(request.source_storage_path):
            query['SourceStoragePath'] = request.source_storage_path
        if not DaraCore.is_null(request.throughput):
            query['Throughput'] = request.throughput
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataFlow',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_flow_with_options_async(
        self,
        request: main_models.CreateDataFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not DaraCore.is_null(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not DaraCore.is_null(request.auto_refreshs):
            query['AutoRefreshs'] = request.auto_refreshs
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.file_system_path):
            query['FileSystemPath'] = request.file_system_path
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        if not DaraCore.is_null(request.source_security_type):
            query['SourceSecurityType'] = request.source_security_type
        if not DaraCore.is_null(request.source_storage):
            query['SourceStorage'] = request.source_storage
        if not DaraCore.is_null(request.source_storage_path):
            query['SourceStoragePath'] = request.source_storage_path
        if not DaraCore.is_null(request.throughput):
            query['Throughput'] = request.throughput
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataFlow',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_flow(
        self,
        request: main_models.CreateDataFlowRequest,
    ) -> main_models.CreateDataFlowResponse:
        runtime = RuntimeOptions()
        return self.create_data_flow_with_options(request, runtime)

    async def create_data_flow_async(
        self,
        request: main_models.CreateDataFlowRequest,
    ) -> main_models.CreateDataFlowResponse:
        runtime = RuntimeOptions()
        return await self.create_data_flow_with_options_async(request, runtime)

    def create_data_flow_sub_task_with_options(
        self,
        request: main_models.CreateDataFlowSubTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataFlowSubTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.condition):
            query['Condition'] = request.condition
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.data_flow_task_id):
            query['DataFlowTaskId'] = request.data_flow_task_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.dst_file_path):
            query['DstFilePath'] = request.dst_file_path
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.src_file_path):
            query['SrcFilePath'] = request.src_file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataFlowSubTask',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataFlowSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_flow_sub_task_with_options_async(
        self,
        request: main_models.CreateDataFlowSubTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataFlowSubTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.condition):
            query['Condition'] = request.condition
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.data_flow_task_id):
            query['DataFlowTaskId'] = request.data_flow_task_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.dst_file_path):
            query['DstFilePath'] = request.dst_file_path
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.src_file_path):
            query['SrcFilePath'] = request.src_file_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataFlowSubTask',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataFlowSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_flow_sub_task(
        self,
        request: main_models.CreateDataFlowSubTaskRequest,
    ) -> main_models.CreateDataFlowSubTaskResponse:
        runtime = RuntimeOptions()
        return self.create_data_flow_sub_task_with_options(request, runtime)

    async def create_data_flow_sub_task_async(
        self,
        request: main_models.CreateDataFlowSubTaskRequest,
    ) -> main_models.CreateDataFlowSubTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_data_flow_sub_task_with_options_async(request, runtime)

    def create_data_flow_task_with_options(
        self,
        request: main_models.CreateDataFlowTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataFlowTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.conflict_policy):
            query['ConflictPolicy'] = request.conflict_policy
        if not DaraCore.is_null(request.create_dir_if_not_exist):
            query['CreateDirIfNotExist'] = request.create_dir_if_not_exist
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.directory):
            query['Directory'] = request.directory
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.dst_directory):
            query['DstDirectory'] = request.dst_directory
        if not DaraCore.is_null(request.entry_list):
            query['EntryList'] = request.entry_list
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.includes):
            query['Includes'] = request.includes
        if not DaraCore.is_null(request.src_task_id):
            query['SrcTaskId'] = request.src_task_id
        if not DaraCore.is_null(request.task_action):
            query['TaskAction'] = request.task_action
        if not DaraCore.is_null(request.transfer_file_list_path):
            query['TransferFileListPath'] = request.transfer_file_list_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataFlowTask',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataFlowTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_flow_task_with_options_async(
        self,
        request: main_models.CreateDataFlowTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataFlowTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.conflict_policy):
            query['ConflictPolicy'] = request.conflict_policy
        if not DaraCore.is_null(request.create_dir_if_not_exist):
            query['CreateDirIfNotExist'] = request.create_dir_if_not_exist
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.data_type):
            query['DataType'] = request.data_type
        if not DaraCore.is_null(request.directory):
            query['Directory'] = request.directory
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.dst_directory):
            query['DstDirectory'] = request.dst_directory
        if not DaraCore.is_null(request.entry_list):
            query['EntryList'] = request.entry_list
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.includes):
            query['Includes'] = request.includes
        if not DaraCore.is_null(request.src_task_id):
            query['SrcTaskId'] = request.src_task_id
        if not DaraCore.is_null(request.task_action):
            query['TaskAction'] = request.task_action
        if not DaraCore.is_null(request.transfer_file_list_path):
            query['TransferFileListPath'] = request.transfer_file_list_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataFlowTask',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataFlowTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_flow_task(
        self,
        request: main_models.CreateDataFlowTaskRequest,
    ) -> main_models.CreateDataFlowTaskResponse:
        runtime = RuntimeOptions()
        return self.create_data_flow_task_with_options(request, runtime)

    async def create_data_flow_task_async(
        self,
        request: main_models.CreateDataFlowTaskRequest,
    ) -> main_models.CreateDataFlowTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_data_flow_task_with_options_async(request, runtime)

    def create_dir_with_options(
        self,
        request: main_models.CreateDirRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDirResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.owner_group_id):
            query['OwnerGroupId'] = request.owner_group_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not DaraCore.is_null(request.permission):
            query['Permission'] = request.permission
        if not DaraCore.is_null(request.recursion):
            query['Recursion'] = request.recursion
        if not DaraCore.is_null(request.root_directory):
            query['RootDirectory'] = request.root_directory
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDir',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDirResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dir_with_options_async(
        self,
        request: main_models.CreateDirRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDirResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.owner_group_id):
            query['OwnerGroupId'] = request.owner_group_id
        if not DaraCore.is_null(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not DaraCore.is_null(request.permission):
            query['Permission'] = request.permission
        if not DaraCore.is_null(request.recursion):
            query['Recursion'] = request.recursion
        if not DaraCore.is_null(request.root_directory):
            query['RootDirectory'] = request.root_directory
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDir',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDirResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dir(
        self,
        request: main_models.CreateDirRequest,
    ) -> main_models.CreateDirResponse:
        runtime = RuntimeOptions()
        return self.create_dir_with_options(request, runtime)

    async def create_dir_async(
        self,
        request: main_models.CreateDirRequest,
    ) -> main_models.CreateDirResponse:
        runtime = RuntimeOptions()
        return await self.create_dir_with_options_async(request, runtime)

    def create_file_with_options(
        self,
        request: main_models.CreateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.owner_access_inheritable):
            query['OwnerAccessInheritable'] = request.owner_access_inheritable
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFile',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_with_options_async(
        self,
        request: main_models.CreateFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.owner_access_inheritable):
            query['OwnerAccessInheritable'] = request.owner_access_inheritable
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFile',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file(
        self,
        request: main_models.CreateFileRequest,
    ) -> main_models.CreateFileResponse:
        runtime = RuntimeOptions()
        return self.create_file_with_options(request, runtime)

    async def create_file_async(
        self,
        request: main_models.CreateFileRequest,
    ) -> main_models.CreateFileResponse:
        runtime = RuntimeOptions()
        return await self.create_file_with_options_async(request, runtime)

    def create_file_system_with_options(
        self,
        request: main_models.CreateFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.capacity):
            query['Capacity'] = request.capacity
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.redundancy_type):
            query['RedundancyType'] = request.redundancy_type
        if not DaraCore.is_null(request.redundancy_vswitch_ids):
            query['RedundancyVSwitchIds'] = request.redundancy_vswitch_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFileSystem',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_system_with_options_async(
        self,
        request: main_models.CreateFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not DaraCore.is_null(request.capacity):
            query['Capacity'] = request.capacity
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.redundancy_type):
            query['RedundancyType'] = request.redundancy_type
        if not DaraCore.is_null(request.redundancy_vswitch_ids):
            query['RedundancyVSwitchIds'] = request.redundancy_vswitch_ids
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFileSystem',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file_system(
        self,
        request: main_models.CreateFileSystemRequest,
    ) -> main_models.CreateFileSystemResponse:
        runtime = RuntimeOptions()
        return self.create_file_system_with_options(request, runtime)

    async def create_file_system_async(
        self,
        request: main_models.CreateFileSystemRequest,
    ) -> main_models.CreateFileSystemResponse:
        runtime = RuntimeOptions()
        return await self.create_file_system_with_options_async(request, runtime)

    def create_fileset_with_options(
        self,
        request: main_models.CreateFilesetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFilesetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.file_system_path):
            query['FileSystemPath'] = request.file_system_path
        if not DaraCore.is_null(request.quota):
            query['Quota'] = request.quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFileset',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFilesetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fileset_with_options_async(
        self,
        request: main_models.CreateFilesetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFilesetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.file_system_path):
            query['FileSystemPath'] = request.file_system_path
        if not DaraCore.is_null(request.quota):
            query['Quota'] = request.quota
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFileset',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFilesetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fileset(
        self,
        request: main_models.CreateFilesetRequest,
    ) -> main_models.CreateFilesetResponse:
        runtime = RuntimeOptions()
        return self.create_fileset_with_options(request, runtime)

    async def create_fileset_async(
        self,
        request: main_models.CreateFilesetRequest,
    ) -> main_models.CreateFilesetResponse:
        runtime = RuntimeOptions()
        return await self.create_fileset_with_options_async(request, runtime)

    def create_ldapconfig_with_options(
        self,
        request: main_models.CreateLDAPConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLDAPConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_dn):
            query['BindDN'] = request.bind_dn
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.search_base):
            query['SearchBase'] = request.search_base
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLDAPConfig',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLDAPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ldapconfig_with_options_async(
        self,
        request: main_models.CreateLDAPConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLDAPConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_dn):
            query['BindDN'] = request.bind_dn
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.search_base):
            query['SearchBase'] = request.search_base
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLDAPConfig',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLDAPConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ldapconfig(
        self,
        request: main_models.CreateLDAPConfigRequest,
    ) -> main_models.CreateLDAPConfigResponse:
        runtime = RuntimeOptions()
        return self.create_ldapconfig_with_options(request, runtime)

    async def create_ldapconfig_async(
        self,
        request: main_models.CreateLDAPConfigRequest,
    ) -> main_models.CreateLDAPConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_ldapconfig_with_options_async(request, runtime)

    def create_lifecycle_policy_with_options(
        self,
        request: main_models.CreateLifecyclePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLifecyclePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        if not DaraCore.is_null(request.lifecycle_policy_type):
            query['LifecyclePolicyType'] = request.lifecycle_policy_type
        if not DaraCore.is_null(request.lifecycle_rule_name):
            query['LifecycleRuleName'] = request.lifecycle_rule_name
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.paths):
            query['Paths'] = request.paths
        if not DaraCore.is_null(request.retrieve_rules):
            query['RetrieveRules'] = request.retrieve_rules
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.transit_rules):
            query['TransitRules'] = request.transit_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLifecyclePolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLifecyclePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lifecycle_policy_with_options_async(
        self,
        request: main_models.CreateLifecyclePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLifecyclePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        if not DaraCore.is_null(request.lifecycle_policy_type):
            query['LifecyclePolicyType'] = request.lifecycle_policy_type
        if not DaraCore.is_null(request.lifecycle_rule_name):
            query['LifecycleRuleName'] = request.lifecycle_rule_name
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.paths):
            query['Paths'] = request.paths
        if not DaraCore.is_null(request.retrieve_rules):
            query['RetrieveRules'] = request.retrieve_rules
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.transit_rules):
            query['TransitRules'] = request.transit_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLifecyclePolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLifecyclePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lifecycle_policy(
        self,
        request: main_models.CreateLifecyclePolicyRequest,
    ) -> main_models.CreateLifecyclePolicyResponse:
        runtime = RuntimeOptions()
        return self.create_lifecycle_policy_with_options(request, runtime)

    async def create_lifecycle_policy_async(
        self,
        request: main_models.CreateLifecyclePolicyRequest,
    ) -> main_models.CreateLifecyclePolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_lifecycle_policy_with_options_async(request, runtime)

    def create_lifecycle_retrieve_job_with_options(
        self,
        request: main_models.CreateLifecycleRetrieveJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLifecycleRetrieveJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.paths):
            query['Paths'] = request.paths
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLifecycleRetrieveJob',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLifecycleRetrieveJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lifecycle_retrieve_job_with_options_async(
        self,
        request: main_models.CreateLifecycleRetrieveJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLifecycleRetrieveJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.paths):
            query['Paths'] = request.paths
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLifecycleRetrieveJob',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLifecycleRetrieveJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lifecycle_retrieve_job(
        self,
        request: main_models.CreateLifecycleRetrieveJobRequest,
    ) -> main_models.CreateLifecycleRetrieveJobResponse:
        runtime = RuntimeOptions()
        return self.create_lifecycle_retrieve_job_with_options(request, runtime)

    async def create_lifecycle_retrieve_job_async(
        self,
        request: main_models.CreateLifecycleRetrieveJobRequest,
    ) -> main_models.CreateLifecycleRetrieveJobResponse:
        runtime = RuntimeOptions()
        return await self.create_lifecycle_retrieve_job_with_options_async(request, runtime)

    def create_log_analysis_with_options(
        self,
        request: main_models.CreateLogAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogAnalysisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogAnalysis',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_log_analysis_with_options_async(
        self,
        request: main_models.CreateLogAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLogAnalysisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLogAnalysis',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLogAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_log_analysis(
        self,
        request: main_models.CreateLogAnalysisRequest,
    ) -> main_models.CreateLogAnalysisResponse:
        runtime = RuntimeOptions()
        return self.create_log_analysis_with_options(request, runtime)

    async def create_log_analysis_async(
        self,
        request: main_models.CreateLogAnalysisRequest,
    ) -> main_models.CreateLogAnalysisResponse:
        runtime = RuntimeOptions()
        return await self.create_log_analysis_with_options_async(request, runtime)

    def create_mount_target_with_options(
        self,
        request: main_models.CreateMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_ipv_6):
            query['EnableIpv6'] = request.enable_ipv_6
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mount_target_with_options_async(
        self,
        request: main_models.CreateMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_ipv_6):
            query['EnableIpv6'] = request.enable_ipv_6
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mount_target(
        self,
        request: main_models.CreateMountTargetRequest,
    ) -> main_models.CreateMountTargetResponse:
        runtime = RuntimeOptions()
        return self.create_mount_target_with_options(request, runtime)

    async def create_mount_target_async(
        self,
        request: main_models.CreateMountTargetRequest,
    ) -> main_models.CreateMountTargetResponse:
        runtime = RuntimeOptions()
        return await self.create_mount_target_with_options_async(request, runtime)

    def create_protocol_mount_target_with_options(
        self,
        request: main_models.CreateProtocolMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProtocolMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProtocolMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProtocolMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_protocol_mount_target_with_options_async(
        self,
        request: main_models.CreateProtocolMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProtocolMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProtocolMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProtocolMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_protocol_mount_target(
        self,
        request: main_models.CreateProtocolMountTargetRequest,
    ) -> main_models.CreateProtocolMountTargetResponse:
        runtime = RuntimeOptions()
        return self.create_protocol_mount_target_with_options(request, runtime)

    async def create_protocol_mount_target_async(
        self,
        request: main_models.CreateProtocolMountTargetRequest,
    ) -> main_models.CreateProtocolMountTargetResponse:
        runtime = RuntimeOptions()
        return await self.create_protocol_mount_target_with_options_async(request, runtime)

    def create_protocol_service_with_options(
        self,
        request: main_models.CreateProtocolServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProtocolServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.protocol_spec):
            query['ProtocolSpec'] = request.protocol_spec
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.throughput):
            query['Throughput'] = request.throughput
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProtocolService',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProtocolServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_protocol_service_with_options_async(
        self,
        request: main_models.CreateProtocolServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProtocolServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.protocol_spec):
            query['ProtocolSpec'] = request.protocol_spec
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.throughput):
            query['Throughput'] = request.throughput
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProtocolService',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProtocolServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_protocol_service(
        self,
        request: main_models.CreateProtocolServiceRequest,
    ) -> main_models.CreateProtocolServiceResponse:
        runtime = RuntimeOptions()
        return self.create_protocol_service_with_options(request, runtime)

    async def create_protocol_service_async(
        self,
        request: main_models.CreateProtocolServiceRequest,
    ) -> main_models.CreateProtocolServiceResponse:
        runtime = RuntimeOptions()
        return await self.create_protocol_service_with_options_async(request, runtime)

    def create_recycle_bin_delete_job_with_options(
        self,
        request: main_models.CreateRecycleBinDeleteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecycleBinDeleteJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecycleBinDeleteJob',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecycleBinDeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_recycle_bin_delete_job_with_options_async(
        self,
        request: main_models.CreateRecycleBinDeleteJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecycleBinDeleteJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecycleBinDeleteJob',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecycleBinDeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_recycle_bin_delete_job(
        self,
        request: main_models.CreateRecycleBinDeleteJobRequest,
    ) -> main_models.CreateRecycleBinDeleteJobResponse:
        runtime = RuntimeOptions()
        return self.create_recycle_bin_delete_job_with_options(request, runtime)

    async def create_recycle_bin_delete_job_async(
        self,
        request: main_models.CreateRecycleBinDeleteJobRequest,
    ) -> main_models.CreateRecycleBinDeleteJobResponse:
        runtime = RuntimeOptions()
        return await self.create_recycle_bin_delete_job_with_options_async(request, runtime)

    def create_recycle_bin_restore_job_with_options(
        self,
        request: main_models.CreateRecycleBinRestoreJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecycleBinRestoreJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecycleBinRestoreJob',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecycleBinRestoreJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_recycle_bin_restore_job_with_options_async(
        self,
        request: main_models.CreateRecycleBinRestoreJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRecycleBinRestoreJobResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRecycleBinRestoreJob',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRecycleBinRestoreJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_recycle_bin_restore_job(
        self,
        request: main_models.CreateRecycleBinRestoreJobRequest,
    ) -> main_models.CreateRecycleBinRestoreJobResponse:
        runtime = RuntimeOptions()
        return self.create_recycle_bin_restore_job_with_options(request, runtime)

    async def create_recycle_bin_restore_job_async(
        self,
        request: main_models.CreateRecycleBinRestoreJobRequest,
    ) -> main_models.CreateRecycleBinRestoreJobResponse:
        runtime = RuntimeOptions()
        return await self.create_recycle_bin_restore_job_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: main_models.CreateSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not DaraCore.is_null(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSnapshot',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: main_models.CreateSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not DaraCore.is_null(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSnapshot',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_snapshot(
        self,
        request: main_models.CreateSnapshotRequest,
    ) -> main_models.CreateSnapshotResponse:
        runtime = RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    async def create_snapshot_async(
        self,
        request: main_models.CreateSnapshotRequest,
    ) -> main_models.CreateSnapshotResponse:
        runtime = RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def delete_access_group_with_options(
        self,
        request: main_models.DeleteAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessGroup',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_group_with_options_async(
        self,
        request: main_models.DeleteAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessGroup',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_group(
        self,
        request: main_models.DeleteAccessGroupRequest,
    ) -> main_models.DeleteAccessGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_access_group_with_options(request, runtime)

    async def delete_access_group_async(
        self,
        request: main_models.DeleteAccessGroupRequest,
    ) -> main_models.DeleteAccessGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_access_group_with_options_async(request, runtime)

    def delete_access_point_with_options(
        self,
        request: main_models.DeleteAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessPoint',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_point_with_options_async(
        self,
        request: main_models.DeleteAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessPoint',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_point(
        self,
        request: main_models.DeleteAccessPointRequest,
    ) -> main_models.DeleteAccessPointResponse:
        runtime = RuntimeOptions()
        return self.delete_access_point_with_options(request, runtime)

    async def delete_access_point_async(
        self,
        request: main_models.DeleteAccessPointRequest,
    ) -> main_models.DeleteAccessPointResponse:
        runtime = RuntimeOptions()
        return await self.delete_access_point_with_options_async(request, runtime)

    def delete_access_rule_with_options(
        self,
        request: main_models.DeleteAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessRule',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_rule_with_options_async(
        self,
        request: main_models.DeleteAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccessRule',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_rule(
        self,
        request: main_models.DeleteAccessRuleRequest,
    ) -> main_models.DeleteAccessRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_access_rule_with_options(request, runtime)

    async def delete_access_rule_async(
        self,
        request: main_models.DeleteAccessRuleRequest,
    ) -> main_models.DeleteAccessRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_access_rule_with_options_async(request, runtime)

    def delete_auto_snapshot_policy_with_options(
        self,
        request: main_models.DeleteAutoSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoSnapshotPolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_snapshot_policy_with_options_async(
        self,
        request: main_models.DeleteAutoSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAutoSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAutoSnapshotPolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_auto_snapshot_policy(
        self,
        request: main_models.DeleteAutoSnapshotPolicyRequest,
    ) -> main_models.DeleteAutoSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_auto_snapshot_policy_with_options(request, runtime)

    async def delete_auto_snapshot_policy_async(
        self,
        request: main_models.DeleteAutoSnapshotPolicyRequest,
    ) -> main_models.DeleteAutoSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_auto_snapshot_policy_with_options_async(request, runtime)

    def delete_data_flow_with_options(
        self,
        request: main_models.DeleteDataFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataFlow',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_flow_with_options_async(
        self,
        request: main_models.DeleteDataFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataFlow',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_flow(
        self,
        request: main_models.DeleteDataFlowRequest,
    ) -> main_models.DeleteDataFlowResponse:
        runtime = RuntimeOptions()
        return self.delete_data_flow_with_options(request, runtime)

    async def delete_data_flow_async(
        self,
        request: main_models.DeleteDataFlowRequest,
    ) -> main_models.DeleteDataFlowResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_flow_with_options_async(request, runtime)

    def delete_file_system_with_options(
        self,
        request: main_models.DeleteFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFileSystem',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_system_with_options_async(
        self,
        request: main_models.DeleteFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFileSystem',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file_system(
        self,
        request: main_models.DeleteFileSystemRequest,
    ) -> main_models.DeleteFileSystemResponse:
        runtime = RuntimeOptions()
        return self.delete_file_system_with_options(request, runtime)

    async def delete_file_system_async(
        self,
        request: main_models.DeleteFileSystemRequest,
    ) -> main_models.DeleteFileSystemResponse:
        runtime = RuntimeOptions()
        return await self.delete_file_system_with_options_async(request, runtime)

    def delete_fileset_with_options(
        self,
        request: main_models.DeleteFilesetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFilesetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFileset',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFilesetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_fileset_with_options_async(
        self,
        request: main_models.DeleteFilesetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFilesetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFileset',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFilesetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_fileset(
        self,
        request: main_models.DeleteFilesetRequest,
    ) -> main_models.DeleteFilesetResponse:
        runtime = RuntimeOptions()
        return self.delete_fileset_with_options(request, runtime)

    async def delete_fileset_async(
        self,
        request: main_models.DeleteFilesetRequest,
    ) -> main_models.DeleteFilesetResponse:
        runtime = RuntimeOptions()
        return await self.delete_fileset_with_options_async(request, runtime)

    def delete_ldapconfig_with_options(
        self,
        request: main_models.DeleteLDAPConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLDAPConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLDAPConfig',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLDAPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ldapconfig_with_options_async(
        self,
        request: main_models.DeleteLDAPConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLDAPConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLDAPConfig',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLDAPConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ldapconfig(
        self,
        request: main_models.DeleteLDAPConfigRequest,
    ) -> main_models.DeleteLDAPConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_ldapconfig_with_options(request, runtime)

    async def delete_ldapconfig_async(
        self,
        request: main_models.DeleteLDAPConfigRequest,
    ) -> main_models.DeleteLDAPConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_ldapconfig_with_options_async(request, runtime)

    def delete_lifecycle_policy_with_options(
        self,
        request: main_models.DeleteLifecyclePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLifecyclePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.lifecycle_policy_id):
            query['LifecyclePolicyId'] = request.lifecycle_policy_id
        if not DaraCore.is_null(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLifecyclePolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLifecyclePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_lifecycle_policy_with_options_async(
        self,
        request: main_models.DeleteLifecyclePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLifecyclePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.lifecycle_policy_id):
            query['LifecyclePolicyId'] = request.lifecycle_policy_id
        if not DaraCore.is_null(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLifecyclePolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLifecyclePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_lifecycle_policy(
        self,
        request: main_models.DeleteLifecyclePolicyRequest,
    ) -> main_models.DeleteLifecyclePolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_lifecycle_policy_with_options(request, runtime)

    async def delete_lifecycle_policy_async(
        self,
        request: main_models.DeleteLifecyclePolicyRequest,
    ) -> main_models.DeleteLifecyclePolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_lifecycle_policy_with_options_async(request, runtime)

    def delete_log_analysis_with_options(
        self,
        request: main_models.DeleteLogAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogAnalysisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogAnalysis',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_log_analysis_with_options_async(
        self,
        request: main_models.DeleteLogAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogAnalysisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogAnalysis',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_log_analysis(
        self,
        request: main_models.DeleteLogAnalysisRequest,
    ) -> main_models.DeleteLogAnalysisResponse:
        runtime = RuntimeOptions()
        return self.delete_log_analysis_with_options(request, runtime)

    async def delete_log_analysis_async(
        self,
        request: main_models.DeleteLogAnalysisRequest,
    ) -> main_models.DeleteLogAnalysisResponse:
        runtime = RuntimeOptions()
        return await self.delete_log_analysis_with_options_async(request, runtime)

    def delete_mount_target_with_options(
        self,
        request: main_models.DeleteMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mount_target_with_options_async(
        self,
        request: main_models.DeleteMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mount_target(
        self,
        request: main_models.DeleteMountTargetRequest,
    ) -> main_models.DeleteMountTargetResponse:
        runtime = RuntimeOptions()
        return self.delete_mount_target_with_options(request, runtime)

    async def delete_mount_target_async(
        self,
        request: main_models.DeleteMountTargetRequest,
    ) -> main_models.DeleteMountTargetResponse:
        runtime = RuntimeOptions()
        return await self.delete_mount_target_with_options_async(request, runtime)

    def delete_protocol_mount_target_with_options(
        self,
        request: main_models.DeleteProtocolMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProtocolMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.export_id):
            query['ExportId'] = request.export_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProtocolMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProtocolMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_protocol_mount_target_with_options_async(
        self,
        request: main_models.DeleteProtocolMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProtocolMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.export_id):
            query['ExportId'] = request.export_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProtocolMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProtocolMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_protocol_mount_target(
        self,
        request: main_models.DeleteProtocolMountTargetRequest,
    ) -> main_models.DeleteProtocolMountTargetResponse:
        runtime = RuntimeOptions()
        return self.delete_protocol_mount_target_with_options(request, runtime)

    async def delete_protocol_mount_target_async(
        self,
        request: main_models.DeleteProtocolMountTargetRequest,
    ) -> main_models.DeleteProtocolMountTargetResponse:
        runtime = RuntimeOptions()
        return await self.delete_protocol_mount_target_with_options_async(request, runtime)

    def delete_protocol_service_with_options(
        self,
        request: main_models.DeleteProtocolServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProtocolServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProtocolService',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProtocolServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_protocol_service_with_options_async(
        self,
        request: main_models.DeleteProtocolServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProtocolServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProtocolService',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProtocolServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_protocol_service(
        self,
        request: main_models.DeleteProtocolServiceRequest,
    ) -> main_models.DeleteProtocolServiceResponse:
        runtime = RuntimeOptions()
        return self.delete_protocol_service_with_options(request, runtime)

    async def delete_protocol_service_async(
        self,
        request: main_models.DeleteProtocolServiceRequest,
    ) -> main_models.DeleteProtocolServiceResponse:
        runtime = RuntimeOptions()
        return await self.delete_protocol_service_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: main_models.DeleteSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSnapshot',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: main_models.DeleteSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSnapshot',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshot(
        self,
        request: main_models.DeleteSnapshotRequest,
    ) -> main_models.DeleteSnapshotResponse:
        runtime = RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: main_models.DeleteSnapshotRequest,
    ) -> main_models.DeleteSnapshotResponse:
        runtime = RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def describe_access_groups_with_options(
        self,
        request: main_models.DescribeAccessGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.use_utcdate_time):
            query['UseUTCDateTime'] = request.use_utcdate_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessGroups',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_groups_with_options_async(
        self,
        request: main_models.DescribeAccessGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.use_utcdate_time):
            query['UseUTCDateTime'] = request.use_utcdate_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessGroups',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_groups(
        self,
        request: main_models.DescribeAccessGroupsRequest,
    ) -> main_models.DescribeAccessGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_access_groups_with_options(request, runtime)

    async def describe_access_groups_async(
        self,
        request: main_models.DescribeAccessGroupsRequest,
    ) -> main_models.DescribeAccessGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_groups_with_options_async(request, runtime)

    def describe_access_point_with_options(
        self,
        request: main_models.DescribeAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessPoint',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_point_with_options_async(
        self,
        request: main_models.DescribeAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessPoint',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_point(
        self,
        request: main_models.DescribeAccessPointRequest,
    ) -> main_models.DescribeAccessPointResponse:
        runtime = RuntimeOptions()
        return self.describe_access_point_with_options(request, runtime)

    async def describe_access_point_async(
        self,
        request: main_models.DescribeAccessPointRequest,
    ) -> main_models.DescribeAccessPointResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_point_with_options_async(request, runtime)

    def describe_access_points_with_options(
        self,
        request: main_models.DescribeAccessPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group):
            query['AccessGroup'] = request.access_group
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessPoints',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_points_with_options_async(
        self,
        request: main_models.DescribeAccessPointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessPointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group):
            query['AccessGroup'] = request.access_group
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessPoints',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_points(
        self,
        request: main_models.DescribeAccessPointsRequest,
    ) -> main_models.DescribeAccessPointsResponse:
        runtime = RuntimeOptions()
        return self.describe_access_points_with_options(request, runtime)

    async def describe_access_points_async(
        self,
        request: main_models.DescribeAccessPointsRequest,
    ) -> main_models.DescribeAccessPointsResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_points_with_options_async(request, runtime)

    def describe_access_rules_with_options(
        self,
        request: main_models.DescribeAccessRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessRules',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_rules_with_options_async(
        self,
        request: main_models.DescribeAccessRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessRules',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_rules(
        self,
        request: main_models.DescribeAccessRulesRequest,
    ) -> main_models.DescribeAccessRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_access_rules_with_options(request, runtime)

    async def describe_access_rules_async(
        self,
        request: main_models.DescribeAccessRulesRequest,
    ) -> main_models.DescribeAccessRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_access_rules_with_options_async(request, runtime)

    def describe_auto_snapshot_policies_with_options(
        self,
        request: main_models.DescribeAutoSnapshotPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoSnapshotPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoSnapshotPolicies',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoSnapshotPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_snapshot_policies_with_options_async(
        self,
        request: main_models.DescribeAutoSnapshotPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoSnapshotPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoSnapshotPolicies',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoSnapshotPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_snapshot_policies(
        self,
        request: main_models.DescribeAutoSnapshotPoliciesRequest,
    ) -> main_models.DescribeAutoSnapshotPoliciesResponse:
        runtime = RuntimeOptions()
        return self.describe_auto_snapshot_policies_with_options(request, runtime)

    async def describe_auto_snapshot_policies_async(
        self,
        request: main_models.DescribeAutoSnapshotPoliciesRequest,
    ) -> main_models.DescribeAutoSnapshotPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.describe_auto_snapshot_policies_with_options_async(request, runtime)

    def describe_auto_snapshot_tasks_with_options(
        self,
        request: main_models.DescribeAutoSnapshotTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoSnapshotTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_snapshot_policy_ids):
            query['AutoSnapshotPolicyIds'] = request.auto_snapshot_policy_ids
        if not DaraCore.is_null(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoSnapshotTasks',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoSnapshotTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_snapshot_tasks_with_options_async(
        self,
        request: main_models.DescribeAutoSnapshotTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoSnapshotTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_snapshot_policy_ids):
            query['AutoSnapshotPolicyIds'] = request.auto_snapshot_policy_ids
        if not DaraCore.is_null(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoSnapshotTasks',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoSnapshotTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_snapshot_tasks(
        self,
        request: main_models.DescribeAutoSnapshotTasksRequest,
    ) -> main_models.DescribeAutoSnapshotTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_auto_snapshot_tasks_with_options(request, runtime)

    async def describe_auto_snapshot_tasks_async(
        self,
        request: main_models.DescribeAutoSnapshotTasksRequest,
    ) -> main_models.DescribeAutoSnapshotTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_auto_snapshot_tasks_with_options_async(request, runtime)

    def describe_black_list_clients_with_options(
        self,
        request: main_models.DescribeBlackListClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBlackListClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBlackListClients',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBlackListClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_black_list_clients_with_options_async(
        self,
        request: main_models.DescribeBlackListClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBlackListClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBlackListClients',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBlackListClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_black_list_clients(
        self,
        request: main_models.DescribeBlackListClientsRequest,
    ) -> main_models.DescribeBlackListClientsResponse:
        runtime = RuntimeOptions()
        return self.describe_black_list_clients_with_options(request, runtime)

    async def describe_black_list_clients_async(
        self,
        request: main_models.DescribeBlackListClientsRequest,
    ) -> main_models.DescribeBlackListClientsResponse:
        runtime = RuntimeOptions()
        return await self.describe_black_list_clients_with_options_async(request, runtime)

    def describe_data_flow_sub_tasks_with_options(
        self,
        request: main_models.DescribeDataFlowSubTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataFlowSubTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataFlowSubTasks',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataFlowSubTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_flow_sub_tasks_with_options_async(
        self,
        request: main_models.DescribeDataFlowSubTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataFlowSubTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataFlowSubTasks',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataFlowSubTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_flow_sub_tasks(
        self,
        request: main_models.DescribeDataFlowSubTasksRequest,
    ) -> main_models.DescribeDataFlowSubTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_data_flow_sub_tasks_with_options(request, runtime)

    async def describe_data_flow_sub_tasks_async(
        self,
        request: main_models.DescribeDataFlowSubTasksRequest,
    ) -> main_models.DescribeDataFlowSubTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_flow_sub_tasks_with_options_async(request, runtime)

    def describe_data_flow_tasks_with_options(
        self,
        request: main_models.DescribeDataFlowTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataFlowTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.with_reports):
            query['WithReports'] = request.with_reports
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataFlowTasks',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataFlowTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_flow_tasks_with_options_async(
        self,
        request: main_models.DescribeDataFlowTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataFlowTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.with_reports):
            query['WithReports'] = request.with_reports
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataFlowTasks',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataFlowTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_flow_tasks(
        self,
        request: main_models.DescribeDataFlowTasksRequest,
    ) -> main_models.DescribeDataFlowTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_data_flow_tasks_with_options(request, runtime)

    async def describe_data_flow_tasks_async(
        self,
        request: main_models.DescribeDataFlowTasksRequest,
    ) -> main_models.DescribeDataFlowTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_flow_tasks_with_options_async(request, runtime)

    def describe_data_flows_with_options(
        self,
        request: main_models.DescribeDataFlowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataFlowsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataFlows',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_flows_with_options_async(
        self,
        request: main_models.DescribeDataFlowsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataFlowsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataFlows',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_flows(
        self,
        request: main_models.DescribeDataFlowsRequest,
    ) -> main_models.DescribeDataFlowsResponse:
        runtime = RuntimeOptions()
        return self.describe_data_flows_with_options(request, runtime)

    async def describe_data_flows_async(
        self,
        request: main_models.DescribeDataFlowsRequest,
    ) -> main_models.DescribeDataFlowsResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_flows_with_options_async(request, runtime)

    def describe_dir_quotas_with_options(
        self,
        request: main_models.DescribeDirQuotasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDirQuotasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDirQuotas',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDirQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dir_quotas_with_options_async(
        self,
        request: main_models.DescribeDirQuotasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDirQuotasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDirQuotas',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDirQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dir_quotas(
        self,
        request: main_models.DescribeDirQuotasRequest,
    ) -> main_models.DescribeDirQuotasResponse:
        runtime = RuntimeOptions()
        return self.describe_dir_quotas_with_options(request, runtime)

    async def describe_dir_quotas_async(
        self,
        request: main_models.DescribeDirQuotasRequest,
    ) -> main_models.DescribeDirQuotasResponse:
        runtime = RuntimeOptions()
        return await self.describe_dir_quotas_with_options_async(request, runtime)

    def describe_file_system_statistics_with_options(
        self,
        request: main_models.DescribeFileSystemStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFileSystemStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFileSystemStatistics',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFileSystemStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_system_statistics_with_options_async(
        self,
        request: main_models.DescribeFileSystemStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFileSystemStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFileSystemStatistics',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFileSystemStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_file_system_statistics(
        self,
        request: main_models.DescribeFileSystemStatisticsRequest,
    ) -> main_models.DescribeFileSystemStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_file_system_statistics_with_options(request, runtime)

    async def describe_file_system_statistics_async(
        self,
        request: main_models.DescribeFileSystemStatisticsRequest,
    ) -> main_models.DescribeFileSystemStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_file_system_statistics_with_options_async(request, runtime)

    def describe_file_systems_with_options(
        self,
        request: main_models.DescribeFileSystemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFileSystemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFileSystems',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_systems_with_options_async(
        self,
        request: main_models.DescribeFileSystemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFileSystemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFileSystems',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFileSystemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_file_systems(
        self,
        request: main_models.DescribeFileSystemsRequest,
    ) -> main_models.DescribeFileSystemsResponse:
        runtime = RuntimeOptions()
        return self.describe_file_systems_with_options(request, runtime)

    async def describe_file_systems_async(
        self,
        request: main_models.DescribeFileSystemsRequest,
    ) -> main_models.DescribeFileSystemsResponse:
        runtime = RuntimeOptions()
        return await self.describe_file_systems_with_options_async(request, runtime)

    def describe_filesets_with_options(
        self,
        request: main_models.DescribeFilesetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFilesetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFilesets',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFilesetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_filesets_with_options_async(
        self,
        request: main_models.DescribeFilesetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFilesetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFilesets',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFilesetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_filesets(
        self,
        request: main_models.DescribeFilesetsRequest,
    ) -> main_models.DescribeFilesetsResponse:
        runtime = RuntimeOptions()
        return self.describe_filesets_with_options(request, runtime)

    async def describe_filesets_async(
        self,
        request: main_models.DescribeFilesetsRequest,
    ) -> main_models.DescribeFilesetsResponse:
        runtime = RuntimeOptions()
        return await self.describe_filesets_with_options_async(request, runtime)

    def describe_filesystems_vsc_attach_info_with_options(
        self,
        request: main_models.DescribeFilesystemsVscAttachInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFilesystemsVscAttachInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFilesystemsVscAttachInfo',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFilesystemsVscAttachInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_filesystems_vsc_attach_info_with_options_async(
        self,
        request: main_models.DescribeFilesystemsVscAttachInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFilesystemsVscAttachInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFilesystemsVscAttachInfo',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFilesystemsVscAttachInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_filesystems_vsc_attach_info(
        self,
        request: main_models.DescribeFilesystemsVscAttachInfoRequest,
    ) -> main_models.DescribeFilesystemsVscAttachInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_filesystems_vsc_attach_info_with_options(request, runtime)

    async def describe_filesystems_vsc_attach_info_async(
        self,
        request: main_models.DescribeFilesystemsVscAttachInfoRequest,
    ) -> main_models.DescribeFilesystemsVscAttachInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_filesystems_vsc_attach_info_with_options_async(request, runtime)

    def describe_lifecycle_policies_with_options(
        self,
        request: main_models.DescribeLifecyclePoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLifecyclePoliciesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLifecyclePolicies',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLifecyclePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lifecycle_policies_with_options_async(
        self,
        request: main_models.DescribeLifecyclePoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLifecyclePoliciesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLifecyclePolicies',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLifecyclePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lifecycle_policies(
        self,
        request: main_models.DescribeLifecyclePoliciesRequest,
    ) -> main_models.DescribeLifecyclePoliciesResponse:
        runtime = RuntimeOptions()
        return self.describe_lifecycle_policies_with_options(request, runtime)

    async def describe_lifecycle_policies_async(
        self,
        request: main_models.DescribeLifecyclePoliciesRequest,
    ) -> main_models.DescribeLifecyclePoliciesResponse:
        runtime = RuntimeOptions()
        return await self.describe_lifecycle_policies_with_options_async(request, runtime)

    def describe_log_analysis_with_options(
        self,
        request: main_models.DescribeLogAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogAnalysisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogAnalysis',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_analysis_with_options_async(
        self,
        request: main_models.DescribeLogAnalysisRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogAnalysisResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogAnalysis',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_analysis(
        self,
        request: main_models.DescribeLogAnalysisRequest,
    ) -> main_models.DescribeLogAnalysisResponse:
        runtime = RuntimeOptions()
        return self.describe_log_analysis_with_options(request, runtime)

    async def describe_log_analysis_async(
        self,
        request: main_models.DescribeLogAnalysisRequest,
    ) -> main_models.DescribeLogAnalysisResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_analysis_with_options_async(request, runtime)

    def describe_mount_targets_with_options(
        self,
        request: main_models.DescribeMountTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMountTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dual_stack_mount_target_domain):
            query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMountTargets',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMountTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mount_targets_with_options_async(
        self,
        request: main_models.DescribeMountTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMountTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dual_stack_mount_target_domain):
            query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMountTargets',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMountTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mount_targets(
        self,
        request: main_models.DescribeMountTargetsRequest,
    ) -> main_models.DescribeMountTargetsResponse:
        runtime = RuntimeOptions()
        return self.describe_mount_targets_with_options(request, runtime)

    async def describe_mount_targets_async(
        self,
        request: main_models.DescribeMountTargetsRequest,
    ) -> main_models.DescribeMountTargetsResponse:
        runtime = RuntimeOptions()
        return await self.describe_mount_targets_with_options_async(request, runtime)

    def describe_mounted_clients_with_options(
        self,
        request: main_models.DescribeMountedClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMountedClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMountedClients',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMountedClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mounted_clients_with_options_async(
        self,
        request: main_models.DescribeMountedClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMountedClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMountedClients',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMountedClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mounted_clients(
        self,
        request: main_models.DescribeMountedClientsRequest,
    ) -> main_models.DescribeMountedClientsResponse:
        runtime = RuntimeOptions()
        return self.describe_mounted_clients_with_options(request, runtime)

    async def describe_mounted_clients_async(
        self,
        request: main_models.DescribeMountedClientsRequest,
    ) -> main_models.DescribeMountedClientsResponse:
        runtime = RuntimeOptions()
        return await self.describe_mounted_clients_with_options_async(request, runtime)

    def describe_nfs_acl_with_options(
        self,
        request: main_models.DescribeNfsAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNfsAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNfsAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNfsAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nfs_acl_with_options_async(
        self,
        request: main_models.DescribeNfsAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNfsAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNfsAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNfsAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nfs_acl(
        self,
        request: main_models.DescribeNfsAclRequest,
    ) -> main_models.DescribeNfsAclResponse:
        runtime = RuntimeOptions()
        return self.describe_nfs_acl_with_options(request, runtime)

    async def describe_nfs_acl_async(
        self,
        request: main_models.DescribeNfsAclRequest,
    ) -> main_models.DescribeNfsAclResponse:
        runtime = RuntimeOptions()
        return await self.describe_nfs_acl_with_options_async(request, runtime)

    def describe_protocol_mount_target_with_options(
        self,
        request: main_models.DescribeProtocolMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProtocolMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.protocol_service_ids):
            query['ProtocolServiceIds'] = request.protocol_service_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProtocolMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProtocolMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_protocol_mount_target_with_options_async(
        self,
        request: main_models.DescribeProtocolMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProtocolMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.protocol_service_ids):
            query['ProtocolServiceIds'] = request.protocol_service_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProtocolMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProtocolMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_protocol_mount_target(
        self,
        request: main_models.DescribeProtocolMountTargetRequest,
    ) -> main_models.DescribeProtocolMountTargetResponse:
        runtime = RuntimeOptions()
        return self.describe_protocol_mount_target_with_options(request, runtime)

    async def describe_protocol_mount_target_async(
        self,
        request: main_models.DescribeProtocolMountTargetRequest,
    ) -> main_models.DescribeProtocolMountTargetResponse:
        runtime = RuntimeOptions()
        return await self.describe_protocol_mount_target_with_options_async(request, runtime)

    def describe_protocol_service_with_options(
        self,
        request: main_models.DescribeProtocolServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProtocolServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.protocol_service_ids):
            query['ProtocolServiceIds'] = request.protocol_service_ids
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProtocolService',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProtocolServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_protocol_service_with_options_async(
        self,
        request: main_models.DescribeProtocolServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProtocolServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.protocol_service_ids):
            query['ProtocolServiceIds'] = request.protocol_service_ids
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProtocolService',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProtocolServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_protocol_service(
        self,
        request: main_models.DescribeProtocolServiceRequest,
    ) -> main_models.DescribeProtocolServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_protocol_service_with_options(request, runtime)

    async def describe_protocol_service_async(
        self,
        request: main_models.DescribeProtocolServiceRequest,
    ) -> main_models.DescribeProtocolServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_protocol_service_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_smb_acl_with_options(
        self,
        request: main_models.DescribeSmbAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmbAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmbAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmbAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smb_acl_with_options_async(
        self,
        request: main_models.DescribeSmbAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSmbAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSmbAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSmbAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smb_acl(
        self,
        request: main_models.DescribeSmbAclRequest,
    ) -> main_models.DescribeSmbAclResponse:
        runtime = RuntimeOptions()
        return self.describe_smb_acl_with_options(request, runtime)

    async def describe_smb_acl_async(
        self,
        request: main_models.DescribeSmbAclRequest,
    ) -> main_models.DescribeSmbAclResponse:
        runtime = RuntimeOptions()
        return await self.describe_smb_acl_with_options_async(request, runtime)

    def describe_snapshots_with_options(
        self,
        request: main_models.DescribeSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not DaraCore.is_null(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not DaraCore.is_null(request.snapshot_type):
            query['SnapshotType'] = request.snapshot_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSnapshots',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_snapshots_with_options_async(
        self,
        request: main_models.DescribeSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not DaraCore.is_null(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not DaraCore.is_null(request.snapshot_type):
            query['SnapshotType'] = request.snapshot_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSnapshots',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_snapshots(
        self,
        request: main_models.DescribeSnapshotsRequest,
    ) -> main_models.DescribeSnapshotsResponse:
        runtime = RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    async def describe_snapshots_async(
        self,
        request: main_models.DescribeSnapshotsRequest,
    ) -> main_models.DescribeSnapshotsResponse:
        runtime = RuntimeOptions()
        return await self.describe_snapshots_with_options_async(request, runtime)

    def describe_storage_packages_with_options(
        self,
        request: main_models.DescribeStoragePackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStoragePackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.use_utcdate_time):
            query['UseUTCDateTime'] = request.use_utcdate_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStoragePackages',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStoragePackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_packages_with_options_async(
        self,
        request: main_models.DescribeStoragePackagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStoragePackagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.use_utcdate_time):
            query['UseUTCDateTime'] = request.use_utcdate_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStoragePackages',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStoragePackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage_packages(
        self,
        request: main_models.DescribeStoragePackagesRequest,
    ) -> main_models.DescribeStoragePackagesResponse:
        runtime = RuntimeOptions()
        return self.describe_storage_packages_with_options(request, runtime)

    async def describe_storage_packages_async(
        self,
        request: main_models.DescribeStoragePackagesRequest,
    ) -> main_models.DescribeStoragePackagesResponse:
        runtime = RuntimeOptions()
        return await self.describe_storage_packages_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_vsc_from_filesystems_with_options(
        self,
        request: main_models.DetachVscFromFilesystemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachVscFromFilesystemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachVscFromFilesystems',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachVscFromFilesystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_vsc_from_filesystems_with_options_async(
        self,
        request: main_models.DetachVscFromFilesystemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachVscFromFilesystemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachVscFromFilesystems',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachVscFromFilesystemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_vsc_from_filesystems(
        self,
        request: main_models.DetachVscFromFilesystemsRequest,
    ) -> main_models.DetachVscFromFilesystemsResponse:
        runtime = RuntimeOptions()
        return self.detach_vsc_from_filesystems_with_options(request, runtime)

    async def detach_vsc_from_filesystems_async(
        self,
        request: main_models.DetachVscFromFilesystemsRequest,
    ) -> main_models.DetachVscFromFilesystemsResponse:
        runtime = RuntimeOptions()
        return await self.detach_vsc_from_filesystems_with_options_async(request, runtime)

    def disable_and_clean_recycle_bin_with_options(
        self,
        request: main_models.DisableAndCleanRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAndCleanRecycleBinResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAndCleanRecycleBin',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAndCleanRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_and_clean_recycle_bin_with_options_async(
        self,
        request: main_models.DisableAndCleanRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAndCleanRecycleBinResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAndCleanRecycleBin',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAndCleanRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_and_clean_recycle_bin(
        self,
        request: main_models.DisableAndCleanRecycleBinRequest,
    ) -> main_models.DisableAndCleanRecycleBinResponse:
        runtime = RuntimeOptions()
        return self.disable_and_clean_recycle_bin_with_options(request, runtime)

    async def disable_and_clean_recycle_bin_async(
        self,
        request: main_models.DisableAndCleanRecycleBinRequest,
    ) -> main_models.DisableAndCleanRecycleBinResponse:
        runtime = RuntimeOptions()
        return await self.disable_and_clean_recycle_bin_with_options_async(request, runtime)

    def disable_nfs_acl_with_options(
        self,
        request: main_models.DisableNfsAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableNfsAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableNfsAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableNfsAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_nfs_acl_with_options_async(
        self,
        request: main_models.DisableNfsAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableNfsAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableNfsAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableNfsAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_nfs_acl(
        self,
        request: main_models.DisableNfsAclRequest,
    ) -> main_models.DisableNfsAclResponse:
        runtime = RuntimeOptions()
        return self.disable_nfs_acl_with_options(request, runtime)

    async def disable_nfs_acl_async(
        self,
        request: main_models.DisableNfsAclRequest,
    ) -> main_models.DisableNfsAclResponse:
        runtime = RuntimeOptions()
        return await self.disable_nfs_acl_with_options_async(request, runtime)

    def disable_smb_acl_with_options(
        self,
        request: main_models.DisableSmbAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSmbAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSmbAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSmbAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_smb_acl_with_options_async(
        self,
        request: main_models.DisableSmbAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSmbAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSmbAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSmbAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_smb_acl(
        self,
        request: main_models.DisableSmbAclRequest,
    ) -> main_models.DisableSmbAclResponse:
        runtime = RuntimeOptions()
        return self.disable_smb_acl_with_options(request, runtime)

    async def disable_smb_acl_async(
        self,
        request: main_models.DisableSmbAclRequest,
    ) -> main_models.DisableSmbAclResponse:
        runtime = RuntimeOptions()
        return await self.disable_smb_acl_with_options_async(request, runtime)

    def enable_nfs_acl_with_options(
        self,
        request: main_models.EnableNfsAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableNfsAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableNfsAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableNfsAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_nfs_acl_with_options_async(
        self,
        request: main_models.EnableNfsAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableNfsAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableNfsAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableNfsAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_nfs_acl(
        self,
        request: main_models.EnableNfsAclRequest,
    ) -> main_models.EnableNfsAclResponse:
        runtime = RuntimeOptions()
        return self.enable_nfs_acl_with_options(request, runtime)

    async def enable_nfs_acl_async(
        self,
        request: main_models.EnableNfsAclRequest,
    ) -> main_models.EnableNfsAclResponse:
        runtime = RuntimeOptions()
        return await self.enable_nfs_acl_with_options_async(request, runtime)

    def enable_recycle_bin_with_options(
        self,
        request: main_models.EnableRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.reserved_days):
            query['ReservedDays'] = request.reserved_days
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableRecycleBin',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_recycle_bin_with_options_async(
        self,
        request: main_models.EnableRecycleBinRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableRecycleBinResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.reserved_days):
            query['ReservedDays'] = request.reserved_days
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableRecycleBin',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_recycle_bin(
        self,
        request: main_models.EnableRecycleBinRequest,
    ) -> main_models.EnableRecycleBinResponse:
        runtime = RuntimeOptions()
        return self.enable_recycle_bin_with_options(request, runtime)

    async def enable_recycle_bin_async(
        self,
        request: main_models.EnableRecycleBinRequest,
    ) -> main_models.EnableRecycleBinResponse:
        runtime = RuntimeOptions()
        return await self.enable_recycle_bin_with_options_async(request, runtime)

    def enable_smb_acl_with_options(
        self,
        request: main_models.EnableSmbAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSmbAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.keytab):
            query['Keytab'] = request.keytab
        if not DaraCore.is_null(request.keytab_md_5):
            query['KeytabMd5'] = request.keytab_md_5
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSmbAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSmbAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_smb_acl_with_options_async(
        self,
        request: main_models.EnableSmbAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSmbAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.keytab):
            query['Keytab'] = request.keytab
        if not DaraCore.is_null(request.keytab_md_5):
            query['KeytabMd5'] = request.keytab_md_5
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSmbAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSmbAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_smb_acl(
        self,
        request: main_models.EnableSmbAclRequest,
    ) -> main_models.EnableSmbAclResponse:
        runtime = RuntimeOptions()
        return self.enable_smb_acl_with_options(request, runtime)

    async def enable_smb_acl_async(
        self,
        request: main_models.EnableSmbAclRequest,
    ) -> main_models.EnableSmbAclResponse:
        runtime = RuntimeOptions()
        return await self.enable_smb_acl_with_options_async(request, runtime)

    def get_directory_or_file_properties_with_options(
        self,
        request: main_models.GetDirectoryOrFilePropertiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDirectoryOrFilePropertiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDirectoryOrFileProperties',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDirectoryOrFilePropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_directory_or_file_properties_with_options_async(
        self,
        request: main_models.GetDirectoryOrFilePropertiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDirectoryOrFilePropertiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDirectoryOrFileProperties',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDirectoryOrFilePropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_directory_or_file_properties(
        self,
        request: main_models.GetDirectoryOrFilePropertiesRequest,
    ) -> main_models.GetDirectoryOrFilePropertiesResponse:
        runtime = RuntimeOptions()
        return self.get_directory_or_file_properties_with_options(request, runtime)

    async def get_directory_or_file_properties_async(
        self,
        request: main_models.GetDirectoryOrFilePropertiesRequest,
    ) -> main_models.GetDirectoryOrFilePropertiesResponse:
        runtime = RuntimeOptions()
        return await self.get_directory_or_file_properties_with_options_async(request, runtime)

    def get_fileset_with_options(
        self,
        request: main_models.GetFilesetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFilesetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFileset',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFilesetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fileset_with_options_async(
        self,
        request: main_models.GetFilesetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFilesetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFileset',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFilesetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fileset(
        self,
        request: main_models.GetFilesetRequest,
    ) -> main_models.GetFilesetResponse:
        runtime = RuntimeOptions()
        return self.get_fileset_with_options(request, runtime)

    async def get_fileset_async(
        self,
        request: main_models.GetFilesetRequest,
    ) -> main_models.GetFilesetResponse:
        runtime = RuntimeOptions()
        return await self.get_fileset_with_options_async(request, runtime)

    def get_protocol_mount_target_with_options(
        self,
        request: main_models.GetProtocolMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProtocolMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.export_id):
            query['ExportId'] = request.export_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProtocolMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProtocolMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_protocol_mount_target_with_options_async(
        self,
        request: main_models.GetProtocolMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProtocolMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.export_id):
            query['ExportId'] = request.export_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProtocolMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProtocolMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_protocol_mount_target(
        self,
        request: main_models.GetProtocolMountTargetRequest,
    ) -> main_models.GetProtocolMountTargetResponse:
        runtime = RuntimeOptions()
        return self.get_protocol_mount_target_with_options(request, runtime)

    async def get_protocol_mount_target_async(
        self,
        request: main_models.GetProtocolMountTargetRequest,
    ) -> main_models.GetProtocolMountTargetResponse:
        runtime = RuntimeOptions()
        return await self.get_protocol_mount_target_with_options_async(request, runtime)

    def get_recycle_bin_attribute_with_options(
        self,
        request: main_models.GetRecycleBinAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRecycleBinAttributeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecycleBinAttribute',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecycleBinAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_recycle_bin_attribute_with_options_async(
        self,
        request: main_models.GetRecycleBinAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRecycleBinAttributeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRecycleBinAttribute',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecycleBinAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_recycle_bin_attribute(
        self,
        request: main_models.GetRecycleBinAttributeRequest,
    ) -> main_models.GetRecycleBinAttributeResponse:
        runtime = RuntimeOptions()
        return self.get_recycle_bin_attribute_with_options(request, runtime)

    async def get_recycle_bin_attribute_async(
        self,
        request: main_models.GetRecycleBinAttributeRequest,
    ) -> main_models.GetRecycleBinAttributeResponse:
        runtime = RuntimeOptions()
        return await self.get_recycle_bin_attribute_with_options_async(request, runtime)

    def list_directories_and_files_with_options(
        self,
        request: main_models.ListDirectoriesAndFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDirectoriesAndFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_only):
            query['DirectoryOnly'] = request.directory_only
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDirectoriesAndFiles',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDirectoriesAndFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_directories_and_files_with_options_async(
        self,
        request: main_models.ListDirectoriesAndFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDirectoriesAndFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directory_only):
            query['DirectoryOnly'] = request.directory_only
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDirectoriesAndFiles',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDirectoriesAndFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_directories_and_files(
        self,
        request: main_models.ListDirectoriesAndFilesRequest,
    ) -> main_models.ListDirectoriesAndFilesResponse:
        runtime = RuntimeOptions()
        return self.list_directories_and_files_with_options(request, runtime)

    async def list_directories_and_files_async(
        self,
        request: main_models.ListDirectoriesAndFilesRequest,
    ) -> main_models.ListDirectoriesAndFilesResponse:
        runtime = RuntimeOptions()
        return await self.list_directories_and_files_with_options_async(request, runtime)

    def list_lifecycle_retrieve_jobs_with_options(
        self,
        request: main_models.ListLifecycleRetrieveJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLifecycleRetrieveJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLifecycleRetrieveJobs',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLifecycleRetrieveJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lifecycle_retrieve_jobs_with_options_async(
        self,
        request: main_models.ListLifecycleRetrieveJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLifecycleRetrieveJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLifecycleRetrieveJobs',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLifecycleRetrieveJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lifecycle_retrieve_jobs(
        self,
        request: main_models.ListLifecycleRetrieveJobsRequest,
    ) -> main_models.ListLifecycleRetrieveJobsResponse:
        runtime = RuntimeOptions()
        return self.list_lifecycle_retrieve_jobs_with_options(request, runtime)

    async def list_lifecycle_retrieve_jobs_async(
        self,
        request: main_models.ListLifecycleRetrieveJobsRequest,
    ) -> main_models.ListLifecycleRetrieveJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_lifecycle_retrieve_jobs_with_options_async(request, runtime)

    def list_recently_recycled_directories_with_options(
        self,
        request: main_models.ListRecentlyRecycledDirectoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecentlyRecycledDirectoriesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecentlyRecycledDirectories',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecentlyRecycledDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recently_recycled_directories_with_options_async(
        self,
        request: main_models.ListRecentlyRecycledDirectoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecentlyRecycledDirectoriesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecentlyRecycledDirectories',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecentlyRecycledDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recently_recycled_directories(
        self,
        request: main_models.ListRecentlyRecycledDirectoriesRequest,
    ) -> main_models.ListRecentlyRecycledDirectoriesResponse:
        runtime = RuntimeOptions()
        return self.list_recently_recycled_directories_with_options(request, runtime)

    async def list_recently_recycled_directories_async(
        self,
        request: main_models.ListRecentlyRecycledDirectoriesRequest,
    ) -> main_models.ListRecentlyRecycledDirectoriesResponse:
        runtime = RuntimeOptions()
        return await self.list_recently_recycled_directories_with_options_async(request, runtime)

    def list_recycle_bin_jobs_with_options(
        self,
        request: main_models.ListRecycleBinJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecycleBinJobsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecycleBinJobs',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecycleBinJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recycle_bin_jobs_with_options_async(
        self,
        request: main_models.ListRecycleBinJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecycleBinJobsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecycleBinJobs',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecycleBinJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recycle_bin_jobs(
        self,
        request: main_models.ListRecycleBinJobsRequest,
    ) -> main_models.ListRecycleBinJobsResponse:
        runtime = RuntimeOptions()
        return self.list_recycle_bin_jobs_with_options(request, runtime)

    async def list_recycle_bin_jobs_async(
        self,
        request: main_models.ListRecycleBinJobsRequest,
    ) -> main_models.ListRecycleBinJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_recycle_bin_jobs_with_options_async(request, runtime)

    def list_recycled_directories_and_files_with_options(
        self,
        request: main_models.ListRecycledDirectoriesAndFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecycledDirectoriesAndFilesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecycledDirectoriesAndFiles',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecycledDirectoriesAndFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recycled_directories_and_files_with_options_async(
        self,
        request: main_models.ListRecycledDirectoriesAndFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRecycledDirectoriesAndFilesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRecycledDirectoriesAndFiles',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRecycledDirectoriesAndFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recycled_directories_and_files(
        self,
        request: main_models.ListRecycledDirectoriesAndFilesRequest,
    ) -> main_models.ListRecycledDirectoriesAndFilesResponse:
        runtime = RuntimeOptions()
        return self.list_recycled_directories_and_files_with_options(request, runtime)

    async def list_recycled_directories_and_files_async(
        self,
        request: main_models.ListRecycledDirectoriesAndFilesRequest,
    ) -> main_models.ListRecycledDirectoriesAndFilesResponse:
        runtime = RuntimeOptions()
        return await self.list_recycled_directories_and_files_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
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
            version = '2017-06-26',
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
            version = '2017-06-26',
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

    def modify_access_group_with_options(
        self,
        request: main_models.ModifyAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccessGroup',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_access_group_with_options_async(
        self,
        request: main_models.ModifyAccessGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccessGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccessGroup',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_access_group(
        self,
        request: main_models.ModifyAccessGroupRequest,
    ) -> main_models.ModifyAccessGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_access_group_with_options(request, runtime)

    async def modify_access_group_async(
        self,
        request: main_models.ModifyAccessGroupRequest,
    ) -> main_models.ModifyAccessGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_access_group_with_options_async(request, runtime)

    def modify_access_point_with_options(
        self,
        request: main_models.ModifyAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group):
            query['AccessGroup'] = request.access_group
        if not DaraCore.is_null(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not DaraCore.is_null(request.access_point_name):
            query['AccessPointName'] = request.access_point_name
        if not DaraCore.is_null(request.enabled_ram):
            query['EnabledRam'] = request.enabled_ram
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccessPoint',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_access_point_with_options_async(
        self,
        request: main_models.ModifyAccessPointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccessPointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group):
            query['AccessGroup'] = request.access_group
        if not DaraCore.is_null(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not DaraCore.is_null(request.access_point_name):
            query['AccessPointName'] = request.access_point_name
        if not DaraCore.is_null(request.enabled_ram):
            query['EnabledRam'] = request.enabled_ram
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccessPoint',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_access_point(
        self,
        request: main_models.ModifyAccessPointRequest,
    ) -> main_models.ModifyAccessPointResponse:
        runtime = RuntimeOptions()
        return self.modify_access_point_with_options(request, runtime)

    async def modify_access_point_async(
        self,
        request: main_models.ModifyAccessPointRequest,
    ) -> main_models.ModifyAccessPointResponse:
        runtime = RuntimeOptions()
        return await self.modify_access_point_with_options_async(request, runtime)

    def modify_access_rule_with_options(
        self,
        request: main_models.ModifyAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        if not DaraCore.is_null(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not DaraCore.is_null(request.user_access_type):
            query['UserAccessType'] = request.user_access_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccessRule',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_access_rule_with_options_async(
        self,
        request: main_models.ModifyAccessRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccessRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not DaraCore.is_null(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not DaraCore.is_null(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        if not DaraCore.is_null(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not DaraCore.is_null(request.user_access_type):
            query['UserAccessType'] = request.user_access_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccessRule',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_access_rule(
        self,
        request: main_models.ModifyAccessRuleRequest,
    ) -> main_models.ModifyAccessRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_access_rule_with_options(request, runtime)

    async def modify_access_rule_async(
        self,
        request: main_models.ModifyAccessRuleRequest,
    ) -> main_models.ModifyAccessRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_access_rule_with_options_async(request, runtime)

    def modify_auto_snapshot_policy_with_options(
        self,
        request: main_models.ModifyAutoSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not DaraCore.is_null(request.auto_snapshot_policy_name):
            query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        if not DaraCore.is_null(request.repeat_weekdays):
            query['RepeatWeekdays'] = request.repeat_weekdays
        if not DaraCore.is_null(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not DaraCore.is_null(request.time_points):
            query['TimePoints'] = request.time_points
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAutoSnapshotPolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_auto_snapshot_policy_with_options_async(
        self,
        request: main_models.ModifyAutoSnapshotPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoSnapshotPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not DaraCore.is_null(request.auto_snapshot_policy_name):
            query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        if not DaraCore.is_null(request.repeat_weekdays):
            query['RepeatWeekdays'] = request.repeat_weekdays
        if not DaraCore.is_null(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not DaraCore.is_null(request.time_points):
            query['TimePoints'] = request.time_points
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAutoSnapshotPolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_auto_snapshot_policy(
        self,
        request: main_models.ModifyAutoSnapshotPolicyRequest,
    ) -> main_models.ModifyAutoSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_auto_snapshot_policy_with_options(request, runtime)

    async def modify_auto_snapshot_policy_async(
        self,
        request: main_models.ModifyAutoSnapshotPolicyRequest,
    ) -> main_models.ModifyAutoSnapshotPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_auto_snapshot_policy_with_options_async(request, runtime)

    def modify_data_flow_with_options(
        self,
        request: main_models.ModifyDataFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.throughput):
            query['Throughput'] = request.throughput
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataFlow',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_flow_with_options_async(
        self,
        request: main_models.ModifyDataFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.throughput):
            query['Throughput'] = request.throughput
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataFlow',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_flow(
        self,
        request: main_models.ModifyDataFlowRequest,
    ) -> main_models.ModifyDataFlowResponse:
        runtime = RuntimeOptions()
        return self.modify_data_flow_with_options(request, runtime)

    async def modify_data_flow_async(
        self,
        request: main_models.ModifyDataFlowRequest,
    ) -> main_models.ModifyDataFlowResponse:
        runtime = RuntimeOptions()
        return await self.modify_data_flow_with_options_async(request, runtime)

    def modify_data_flow_auto_refresh_with_options(
        self,
        request: main_models.ModifyDataFlowAutoRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataFlowAutoRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not DaraCore.is_null(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataFlowAutoRefresh',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataFlowAutoRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_flow_auto_refresh_with_options_async(
        self,
        request: main_models.ModifyDataFlowAutoRefreshRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDataFlowAutoRefreshResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not DaraCore.is_null(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDataFlowAutoRefresh',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDataFlowAutoRefreshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_flow_auto_refresh(
        self,
        request: main_models.ModifyDataFlowAutoRefreshRequest,
    ) -> main_models.ModifyDataFlowAutoRefreshResponse:
        runtime = RuntimeOptions()
        return self.modify_data_flow_auto_refresh_with_options(request, runtime)

    async def modify_data_flow_auto_refresh_async(
        self,
        request: main_models.ModifyDataFlowAutoRefreshRequest,
    ) -> main_models.ModifyDataFlowAutoRefreshResponse:
        runtime = RuntimeOptions()
        return await self.modify_data_flow_auto_refresh_with_options_async(request, runtime)

    def modify_file_system_with_options(
        self,
        tmp_req: main_models.ModifyFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFileSystemResponse:
        tmp_req.validate()
        request = main_models.ModifyFileSystemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.options):
            request.options_shrink = Utils.array_to_string_with_specified_style(tmp_req.options, 'Options', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.options_shrink):
            query['Options'] = request.options_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFileSystem',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_file_system_with_options_async(
        self,
        tmp_req: main_models.ModifyFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFileSystemResponse:
        tmp_req.validate()
        request = main_models.ModifyFileSystemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.options):
            request.options_shrink = Utils.array_to_string_with_specified_style(tmp_req.options, 'Options', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.options_shrink):
            query['Options'] = request.options_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFileSystem',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_file_system(
        self,
        request: main_models.ModifyFileSystemRequest,
    ) -> main_models.ModifyFileSystemResponse:
        runtime = RuntimeOptions()
        return self.modify_file_system_with_options(request, runtime)

    async def modify_file_system_async(
        self,
        request: main_models.ModifyFileSystemRequest,
    ) -> main_models.ModifyFileSystemResponse:
        runtime = RuntimeOptions()
        return await self.modify_file_system_with_options_async(request, runtime)

    def modify_fileset_with_options(
        self,
        request: main_models.ModifyFilesetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFilesetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFileset',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFilesetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_fileset_with_options_async(
        self,
        request: main_models.ModifyFilesetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFilesetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFileset',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFilesetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_fileset(
        self,
        request: main_models.ModifyFilesetRequest,
    ) -> main_models.ModifyFilesetResponse:
        runtime = RuntimeOptions()
        return self.modify_fileset_with_options(request, runtime)

    async def modify_fileset_async(
        self,
        request: main_models.ModifyFilesetRequest,
    ) -> main_models.ModifyFilesetResponse:
        runtime = RuntimeOptions()
        return await self.modify_fileset_with_options_async(request, runtime)

    def modify_ldapconfig_with_options(
        self,
        request: main_models.ModifyLDAPConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLDAPConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_dn):
            query['BindDN'] = request.bind_dn
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.search_base):
            query['SearchBase'] = request.search_base
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLDAPConfig',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLDAPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ldapconfig_with_options_async(
        self,
        request: main_models.ModifyLDAPConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLDAPConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_dn):
            query['BindDN'] = request.bind_dn
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.search_base):
            query['SearchBase'] = request.search_base
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLDAPConfig',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLDAPConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ldapconfig(
        self,
        request: main_models.ModifyLDAPConfigRequest,
    ) -> main_models.ModifyLDAPConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_ldapconfig_with_options(request, runtime)

    async def modify_ldapconfig_async(
        self,
        request: main_models.ModifyLDAPConfigRequest,
    ) -> main_models.ModifyLDAPConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_ldapconfig_with_options_async(request, runtime)

    def modify_lifecycle_policy_with_options(
        self,
        request: main_models.ModifyLifecyclePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLifecyclePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.lifecycle_policy_id):
            query['LifecyclePolicyId'] = request.lifecycle_policy_id
        if not DaraCore.is_null(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        if not DaraCore.is_null(request.lifecycle_rule_name):
            query['LifecycleRuleName'] = request.lifecycle_rule_name
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLifecyclePolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLifecyclePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_lifecycle_policy_with_options_async(
        self,
        request: main_models.ModifyLifecyclePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyLifecyclePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.lifecycle_policy_id):
            query['LifecyclePolicyId'] = request.lifecycle_policy_id
        if not DaraCore.is_null(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        if not DaraCore.is_null(request.lifecycle_rule_name):
            query['LifecycleRuleName'] = request.lifecycle_rule_name
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyLifecyclePolicy',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyLifecyclePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_lifecycle_policy(
        self,
        request: main_models.ModifyLifecyclePolicyRequest,
    ) -> main_models.ModifyLifecyclePolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_lifecycle_policy_with_options(request, runtime)

    async def modify_lifecycle_policy_async(
        self,
        request: main_models.ModifyLifecyclePolicyRequest,
    ) -> main_models.ModifyLifecyclePolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_lifecycle_policy_with_options_async(request, runtime)

    def modify_mount_target_with_options(
        self,
        request: main_models.ModifyMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.dual_stack_mount_target_domain):
            query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_mount_target_with_options_async(
        self,
        request: main_models.ModifyMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not DaraCore.is_null(request.dual_stack_mount_target_domain):
            query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_mount_target(
        self,
        request: main_models.ModifyMountTargetRequest,
    ) -> main_models.ModifyMountTargetResponse:
        runtime = RuntimeOptions()
        return self.modify_mount_target_with_options(request, runtime)

    async def modify_mount_target_async(
        self,
        request: main_models.ModifyMountTargetRequest,
    ) -> main_models.ModifyMountTargetResponse:
        runtime = RuntimeOptions()
        return await self.modify_mount_target_with_options_async(request, runtime)

    def modify_protocol_mount_target_with_options(
        self,
        request: main_models.ModifyProtocolMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyProtocolMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.export_id):
            query['ExportId'] = request.export_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyProtocolMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyProtocolMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_protocol_mount_target_with_options_async(
        self,
        request: main_models.ModifyProtocolMountTargetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyProtocolMountTargetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.export_id):
            query['ExportId'] = request.export_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyProtocolMountTarget',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyProtocolMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_protocol_mount_target(
        self,
        request: main_models.ModifyProtocolMountTargetRequest,
    ) -> main_models.ModifyProtocolMountTargetResponse:
        runtime = RuntimeOptions()
        return self.modify_protocol_mount_target_with_options(request, runtime)

    async def modify_protocol_mount_target_async(
        self,
        request: main_models.ModifyProtocolMountTargetRequest,
    ) -> main_models.ModifyProtocolMountTargetResponse:
        runtime = RuntimeOptions()
        return await self.modify_protocol_mount_target_with_options_async(request, runtime)

    def modify_protocol_service_with_options(
        self,
        request: main_models.ModifyProtocolServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyProtocolServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyProtocolService',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyProtocolServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_protocol_service_with_options_async(
        self,
        request: main_models.ModifyProtocolServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyProtocolServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyProtocolService',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyProtocolServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_protocol_service(
        self,
        request: main_models.ModifyProtocolServiceRequest,
    ) -> main_models.ModifyProtocolServiceResponse:
        runtime = RuntimeOptions()
        return self.modify_protocol_service_with_options(request, runtime)

    async def modify_protocol_service_async(
        self,
        request: main_models.ModifyProtocolServiceRequest,
    ) -> main_models.ModifyProtocolServiceResponse:
        runtime = RuntimeOptions()
        return await self.modify_protocol_service_with_options_async(request, runtime)

    def modify_smb_acl_with_options(
        self,
        request: main_models.ModifySmbAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySmbAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_anonymous_access):
            query['EnableAnonymousAccess'] = request.enable_anonymous_access
        if not DaraCore.is_null(request.encrypt_data):
            query['EncryptData'] = request.encrypt_data
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.home_dir_path):
            query['HomeDirPath'] = request.home_dir_path
        if not DaraCore.is_null(request.keytab):
            query['Keytab'] = request.keytab
        if not DaraCore.is_null(request.keytab_md_5):
            query['KeytabMd5'] = request.keytab_md_5
        if not DaraCore.is_null(request.reject_unencrypted_access):
            query['RejectUnencryptedAccess'] = request.reject_unencrypted_access
        if not DaraCore.is_null(request.super_admin_sid):
            query['SuperAdminSid'] = request.super_admin_sid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySmbAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySmbAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_smb_acl_with_options_async(
        self,
        request: main_models.ModifySmbAclRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySmbAclResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_anonymous_access):
            query['EnableAnonymousAccess'] = request.enable_anonymous_access
        if not DaraCore.is_null(request.encrypt_data):
            query['EncryptData'] = request.encrypt_data
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.home_dir_path):
            query['HomeDirPath'] = request.home_dir_path
        if not DaraCore.is_null(request.keytab):
            query['Keytab'] = request.keytab
        if not DaraCore.is_null(request.keytab_md_5):
            query['KeytabMd5'] = request.keytab_md_5
        if not DaraCore.is_null(request.reject_unencrypted_access):
            query['RejectUnencryptedAccess'] = request.reject_unencrypted_access
        if not DaraCore.is_null(request.super_admin_sid):
            query['SuperAdminSid'] = request.super_admin_sid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySmbAcl',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySmbAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_smb_acl(
        self,
        request: main_models.ModifySmbAclRequest,
    ) -> main_models.ModifySmbAclResponse:
        runtime = RuntimeOptions()
        return self.modify_smb_acl_with_options(request, runtime)

    async def modify_smb_acl_async(
        self,
        request: main_models.ModifySmbAclRequest,
    ) -> main_models.ModifySmbAclResponse:
        runtime = RuntimeOptions()
        return await self.modify_smb_acl_with_options_async(request, runtime)

    def open_nasservice_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OpenNASServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OpenNASService',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenNASServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_nasservice_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OpenNASServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OpenNASService',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenNASServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_nasservice(self) -> main_models.OpenNASServiceResponse:
        runtime = RuntimeOptions()
        return self.open_nasservice_with_options(runtime)

    async def open_nasservice_async(self) -> main_models.OpenNASServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_nasservice_with_options_async(runtime)

    def remove_client_from_black_list_with_options(
        self,
        request: main_models.RemoveClientFromBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveClientFromBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveClientFromBlackList',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveClientFromBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_client_from_black_list_with_options_async(
        self,
        request: main_models.RemoveClientFromBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveClientFromBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveClientFromBlackList',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveClientFromBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_client_from_black_list(
        self,
        request: main_models.RemoveClientFromBlackListRequest,
    ) -> main_models.RemoveClientFromBlackListResponse:
        runtime = RuntimeOptions()
        return self.remove_client_from_black_list_with_options(request, runtime)

    async def remove_client_from_black_list_async(
        self,
        request: main_models.RemoveClientFromBlackListRequest,
    ) -> main_models.RemoveClientFromBlackListResponse:
        runtime = RuntimeOptions()
        return await self.remove_client_from_black_list_with_options_async(request, runtime)

    def reset_file_system_with_options(
        self,
        request: main_models.ResetFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetFileSystem',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_file_system_with_options_async(
        self,
        request: main_models.ResetFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetFileSystem',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_file_system(
        self,
        request: main_models.ResetFileSystemRequest,
    ) -> main_models.ResetFileSystemResponse:
        runtime = RuntimeOptions()
        return self.reset_file_system_with_options(request, runtime)

    async def reset_file_system_async(
        self,
        request: main_models.ResetFileSystemRequest,
    ) -> main_models.ResetFileSystemResponse:
        runtime = RuntimeOptions()
        return await self.reset_file_system_with_options_async(request, runtime)

    def retry_lifecycle_retrieve_job_with_options(
        self,
        request: main_models.RetryLifecycleRetrieveJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryLifecycleRetrieveJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryLifecycleRetrieveJob',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryLifecycleRetrieveJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_lifecycle_retrieve_job_with_options_async(
        self,
        request: main_models.RetryLifecycleRetrieveJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryLifecycleRetrieveJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryLifecycleRetrieveJob',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryLifecycleRetrieveJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_lifecycle_retrieve_job(
        self,
        request: main_models.RetryLifecycleRetrieveJobRequest,
    ) -> main_models.RetryLifecycleRetrieveJobResponse:
        runtime = RuntimeOptions()
        return self.retry_lifecycle_retrieve_job_with_options(request, runtime)

    async def retry_lifecycle_retrieve_job_async(
        self,
        request: main_models.RetryLifecycleRetrieveJobRequest,
    ) -> main_models.RetryLifecycleRetrieveJobResponse:
        runtime = RuntimeOptions()
        return await self.retry_lifecycle_retrieve_job_with_options_async(request, runtime)

    def set_dir_quota_with_options(
        self,
        request: main_models.SetDirQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDirQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_count_limit):
            query['FileCountLimit'] = request.file_count_limit
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.quota_type):
            query['QuotaType'] = request.quota_type
        if not DaraCore.is_null(request.size_limit):
            query['SizeLimit'] = request.size_limit
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDirQuota',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDirQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dir_quota_with_options_async(
        self,
        request: main_models.SetDirQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDirQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_count_limit):
            query['FileCountLimit'] = request.file_count_limit
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.quota_type):
            query['QuotaType'] = request.quota_type
        if not DaraCore.is_null(request.size_limit):
            query['SizeLimit'] = request.size_limit
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDirQuota',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDirQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dir_quota(
        self,
        request: main_models.SetDirQuotaRequest,
    ) -> main_models.SetDirQuotaResponse:
        runtime = RuntimeOptions()
        return self.set_dir_quota_with_options(request, runtime)

    async def set_dir_quota_async(
        self,
        request: main_models.SetDirQuotaRequest,
    ) -> main_models.SetDirQuotaResponse:
        runtime = RuntimeOptions()
        return await self.set_dir_quota_with_options_async(request, runtime)

    def set_fileset_quota_with_options(
        self,
        request: main_models.SetFilesetQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetFilesetQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_count_limit):
            query['FileCountLimit'] = request.file_count_limit
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        if not DaraCore.is_null(request.size_limit):
            query['SizeLimit'] = request.size_limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetFilesetQuota',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetFilesetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_fileset_quota_with_options_async(
        self,
        request: main_models.SetFilesetQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetFilesetQuotaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_count_limit):
            query['FileCountLimit'] = request.file_count_limit
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.fset_id):
            query['FsetId'] = request.fset_id
        if not DaraCore.is_null(request.size_limit):
            query['SizeLimit'] = request.size_limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetFilesetQuota',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetFilesetQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_fileset_quota(
        self,
        request: main_models.SetFilesetQuotaRequest,
    ) -> main_models.SetFilesetQuotaResponse:
        runtime = RuntimeOptions()
        return self.set_fileset_quota_with_options(request, runtime)

    async def set_fileset_quota_async(
        self,
        request: main_models.SetFilesetQuotaRequest,
    ) -> main_models.SetFilesetQuotaResponse:
        runtime = RuntimeOptions()
        return await self.set_fileset_quota_with_options_async(request, runtime)

    def start_data_flow_with_options(
        self,
        request: main_models.StartDataFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDataFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDataFlow',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_data_flow_with_options_async(
        self,
        request: main_models.StartDataFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDataFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDataFlow',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDataFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_data_flow(
        self,
        request: main_models.StartDataFlowRequest,
    ) -> main_models.StartDataFlowResponse:
        runtime = RuntimeOptions()
        return self.start_data_flow_with_options(request, runtime)

    async def start_data_flow_async(
        self,
        request: main_models.StartDataFlowRequest,
    ) -> main_models.StartDataFlowResponse:
        runtime = RuntimeOptions()
        return await self.start_data_flow_with_options_async(request, runtime)

    def stop_data_flow_with_options(
        self,
        request: main_models.StopDataFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDataFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDataFlow',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_data_flow_with_options_async(
        self,
        request: main_models.StopDataFlowRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDataFlowResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDataFlow',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDataFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_data_flow(
        self,
        request: main_models.StopDataFlowRequest,
    ) -> main_models.StopDataFlowResponse:
        runtime = RuntimeOptions()
        return self.stop_data_flow_with_options(request, runtime)

    async def stop_data_flow_async(
        self,
        request: main_models.StopDataFlowRequest,
    ) -> main_models.StopDataFlowResponse:
        runtime = RuntimeOptions()
        return await self.stop_data_flow_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
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
            version = '2017-06-26',
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
            version = '2017-06-26',
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
            version = '2017-06-26',
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
            version = '2017-06-26',
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

    def update_recycle_bin_attribute_with_options(
        self,
        request: main_models.UpdateRecycleBinAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecycleBinAttributeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecycleBinAttribute',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecycleBinAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recycle_bin_attribute_with_options_async(
        self,
        request: main_models.UpdateRecycleBinAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRecycleBinAttributeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRecycleBinAttribute',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRecycleBinAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recycle_bin_attribute(
        self,
        request: main_models.UpdateRecycleBinAttributeRequest,
    ) -> main_models.UpdateRecycleBinAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_recycle_bin_attribute_with_options(request, runtime)

    async def update_recycle_bin_attribute_async(
        self,
        request: main_models.UpdateRecycleBinAttributeRequest,
    ) -> main_models.UpdateRecycleBinAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_recycle_bin_attribute_with_options_async(request, runtime)

    def upgrade_file_system_with_options(
        self,
        request: main_models.UpgradeFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.capacity):
            query['Capacity'] = request.capacity
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeFileSystem',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_file_system_with_options_async(
        self,
        request: main_models.UpgradeFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.capacity):
            query['Capacity'] = request.capacity
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeFileSystem',
            version = '2017-06-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_file_system(
        self,
        request: main_models.UpgradeFileSystemRequest,
    ) -> main_models.UpgradeFileSystemResponse:
        runtime = RuntimeOptions()
        return self.upgrade_file_system_with_options(request, runtime)

    async def upgrade_file_system_async(
        self,
        request: main_models.UpgradeFileSystemRequest,
    ) -> main_models.UpgradeFileSystemResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_file_system_with_options_async(request, runtime)
