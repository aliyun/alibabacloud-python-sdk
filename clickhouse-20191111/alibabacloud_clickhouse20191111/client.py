# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_clickhouse20191111 import models as main_models
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
            'ap-northeast-2-pop': 'clickhouse.aliyuncs.com',
            'ap-southeast-1': 'clickhouse.aliyuncs.com',
            'cn-beijing': 'clickhouse.aliyuncs.com',
            'cn-beijing-finance-1': 'clickhouse.aliyuncs.com',
            'cn-beijing-finance-pop': 'clickhouse.aliyuncs.com',
            'cn-beijing-gov-1': 'clickhouse.aliyuncs.com',
            'cn-beijing-nu16-b01': 'clickhouse.aliyuncs.com',
            'cn-edge-1': 'clickhouse.aliyuncs.com',
            'cn-fujian': 'clickhouse.aliyuncs.com',
            'cn-haidian-cm12-c01': 'clickhouse.aliyuncs.com',
            'cn-hangzhou': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-finance': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-test-306': 'clickhouse.aliyuncs.com',
            'cn-hongkong': 'clickhouse.aliyuncs.com',
            'cn-hongkong-finance-pop': 'clickhouse.aliyuncs.com',
            'cn-north-2-gov-1': 'clickhouse.aliyuncs.com',
            'cn-qingdao': 'clickhouse.aliyuncs.com',
            'cn-qingdao-nebula': 'clickhouse.aliyuncs.com',
            'cn-shanghai': 'clickhouse.aliyuncs.com',
            'cn-shanghai-et15-b01': 'clickhouse.aliyuncs.com',
            'cn-shanghai-et2-b01': 'clickhouse.aliyuncs.com',
            'cn-shanghai-finance-1': 'clickhouse.aliyuncs.com',
            'cn-shanghai-inner': 'clickhouse.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'clickhouse.aliyuncs.com',
            'cn-shenzhen': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-finance-1': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-inner': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'clickhouse.aliyuncs.com',
            'cn-wuhan': 'clickhouse.aliyuncs.com',
            'cn-yushanfang': 'clickhouse.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'clickhouse.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'clickhouse.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'clickhouse.aliyuncs.com',
            'eu-west-1-oxs': 'clickhouse.aliyuncs.com',
            'me-east-1': 'clickhouse.aliyuncs.com',
            'rus-west-1-pop': 'clickhouse.aliyuncs.com',
            'us-east-1': 'clickhouse.aliyuncs.com',
            'us-west-1': 'clickhouse.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('clickhouse', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allocate_cluster_public_connection_with_options(
        self,
        request: main_models.AllocateClusterPublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateClusterPublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateClusterPublicConnection',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_cluster_public_connection_with_options_async(
        self,
        request: main_models.AllocateClusterPublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateClusterPublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateClusterPublicConnection',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_cluster_public_connection(
        self,
        request: main_models.AllocateClusterPublicConnectionRequest,
    ) -> main_models.AllocateClusterPublicConnectionResponse:
        runtime = RuntimeOptions()
        return self.allocate_cluster_public_connection_with_options(request, runtime)

    async def allocate_cluster_public_connection_async(
        self,
        request: main_models.AllocateClusterPublicConnectionRequest,
    ) -> main_models.AllocateClusterPublicConnectionResponse:
        runtime = RuntimeOptions()
        return await self.allocate_cluster_public_connection_with_options_async(request, runtime)

    def cancel_active_operation_tasks_with_options(
        self,
        request: main_models.CancelActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelActiveOperationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelActiveOperationTasks',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_active_operation_tasks_with_options_async(
        self,
        request: main_models.CancelActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelActiveOperationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelActiveOperationTasks',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_active_operation_tasks(
        self,
        request: main_models.CancelActiveOperationTasksRequest,
    ) -> main_models.CancelActiveOperationTasksResponse:
        runtime = RuntimeOptions()
        return self.cancel_active_operation_tasks_with_options(request, runtime)

    async def cancel_active_operation_tasks_async(
        self,
        request: main_models.CancelActiveOperationTasksRequest,
    ) -> main_models.CancelActiveOperationTasksResponse:
        runtime = RuntimeOptions()
        return await self.cancel_active_operation_tasks_with_options_async(request, runtime)

    def cancel_appointment_elect_zookeeper_leader_with_options(
        self,
        request: main_models.CancelAppointmentElectZookeeperLeaderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAppointmentElectZookeeperLeaderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAppointmentElectZookeeperLeader',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAppointmentElectZookeeperLeaderResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_appointment_elect_zookeeper_leader_with_options_async(
        self,
        request: main_models.CancelAppointmentElectZookeeperLeaderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAppointmentElectZookeeperLeaderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAppointmentElectZookeeperLeader',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAppointmentElectZookeeperLeaderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_appointment_elect_zookeeper_leader(
        self,
        request: main_models.CancelAppointmentElectZookeeperLeaderRequest,
    ) -> main_models.CancelAppointmentElectZookeeperLeaderResponse:
        runtime = RuntimeOptions()
        return self.cancel_appointment_elect_zookeeper_leader_with_options(request, runtime)

    async def cancel_appointment_elect_zookeeper_leader_async(
        self,
        request: main_models.CancelAppointmentElectZookeeperLeaderRequest,
    ) -> main_models.CancelAppointmentElectZookeeperLeaderResponse:
        runtime = RuntimeOptions()
        return await self.cancel_appointment_elect_zookeeper_leader_with_options_async(request, runtime)

    def cancel_appointment_restart_instance_node_list_with_options(
        self,
        request: main_models.CancelAppointmentRestartInstanceNodeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAppointmentRestartInstanceNodeListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAppointmentRestartInstanceNodeList',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAppointmentRestartInstanceNodeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_appointment_restart_instance_node_list_with_options_async(
        self,
        request: main_models.CancelAppointmentRestartInstanceNodeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelAppointmentRestartInstanceNodeListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelAppointmentRestartInstanceNodeList',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelAppointmentRestartInstanceNodeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_appointment_restart_instance_node_list(
        self,
        request: main_models.CancelAppointmentRestartInstanceNodeListRequest,
    ) -> main_models.CancelAppointmentRestartInstanceNodeListResponse:
        runtime = RuntimeOptions()
        return self.cancel_appointment_restart_instance_node_list_with_options(request, runtime)

    async def cancel_appointment_restart_instance_node_list_async(
        self,
        request: main_models.CancelAppointmentRestartInstanceNodeListRequest,
    ) -> main_models.CancelAppointmentRestartInstanceNodeListResponse:
        runtime = RuntimeOptions()
        return await self.cancel_appointment_restart_instance_node_list_with_options_async(request, runtime)

    def cancel_restart_instance_with_options(
        self,
        request: main_models.CancelRestartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRestartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restart_time):
            query['RestartTime'] = request.restart_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelRestartInstance',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_restart_instance_with_options_async(
        self,
        request: main_models.CancelRestartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRestartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restart_time):
            query['RestartTime'] = request.restart_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelRestartInstance',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_restart_instance(
        self,
        request: main_models.CancelRestartInstanceRequest,
    ) -> main_models.CancelRestartInstanceResponse:
        runtime = RuntimeOptions()
        return self.cancel_restart_instance_with_options(request, runtime)

    async def cancel_restart_instance_async(
        self,
        request: main_models.CancelRestartInstanceRequest,
    ) -> main_models.CancelRestartInstanceResponse:
        runtime = RuntimeOptions()
        return await self.cancel_restart_instance_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2019-11-11',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2019-11-11',
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

    def check_clickhouse_to_rdswith_options(
        self,
        request: main_models.CheckClickhouseToRDSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckClickhouseToRDSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ck_password):
            query['CkPassword'] = request.ck_password
        if not DaraCore.is_null(request.ck_user_name):
            query['CkUserName'] = request.ck_user_name
        if not DaraCore.is_null(request.clickhouse_port):
            query['ClickhousePort'] = request.clickhouse_port
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rds_id):
            query['RdsId'] = request.rds_id
        if not DaraCore.is_null(request.rds_password):
            query['RdsPassword'] = request.rds_password
        if not DaraCore.is_null(request.rds_port):
            query['RdsPort'] = request.rds_port
        if not DaraCore.is_null(request.rds_user_name):
            query['RdsUserName'] = request.rds_user_name
        if not DaraCore.is_null(request.rds_vpc_id):
            query['RdsVpcId'] = request.rds_vpc_id
        if not DaraCore.is_null(request.rds_vpc_url):
            query['RdsVpcUrl'] = request.rds_vpc_url
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckClickhouseToRDS',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckClickhouseToRDSResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_clickhouse_to_rdswith_options_async(
        self,
        request: main_models.CheckClickhouseToRDSRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckClickhouseToRDSResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ck_password):
            query['CkPassword'] = request.ck_password
        if not DaraCore.is_null(request.ck_user_name):
            query['CkUserName'] = request.ck_user_name
        if not DaraCore.is_null(request.clickhouse_port):
            query['ClickhousePort'] = request.clickhouse_port
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rds_id):
            query['RdsId'] = request.rds_id
        if not DaraCore.is_null(request.rds_password):
            query['RdsPassword'] = request.rds_password
        if not DaraCore.is_null(request.rds_port):
            query['RdsPort'] = request.rds_port
        if not DaraCore.is_null(request.rds_user_name):
            query['RdsUserName'] = request.rds_user_name
        if not DaraCore.is_null(request.rds_vpc_id):
            query['RdsVpcId'] = request.rds_vpc_id
        if not DaraCore.is_null(request.rds_vpc_url):
            query['RdsVpcUrl'] = request.rds_vpc_url
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckClickhouseToRDS',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckClickhouseToRDSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_clickhouse_to_rds(
        self,
        request: main_models.CheckClickhouseToRDSRequest,
    ) -> main_models.CheckClickhouseToRDSResponse:
        runtime = RuntimeOptions()
        return self.check_clickhouse_to_rdswith_options(request, runtime)

    async def check_clickhouse_to_rds_async(
        self,
        request: main_models.CheckClickhouseToRDSRequest,
    ) -> main_models.CheckClickhouseToRDSResponse:
        runtime = RuntimeOptions()
        return await self.check_clickhouse_to_rdswith_options_async(request, runtime)

    def check_modify_config_need_restart_with_options(
        self,
        request: main_models.CheckModifyConfigNeedRestartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckModifyConfigNeedRestartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckModifyConfigNeedRestart',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckModifyConfigNeedRestartResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_modify_config_need_restart_with_options_async(
        self,
        request: main_models.CheckModifyConfigNeedRestartRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckModifyConfigNeedRestartResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckModifyConfigNeedRestart',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckModifyConfigNeedRestartResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_modify_config_need_restart(
        self,
        request: main_models.CheckModifyConfigNeedRestartRequest,
    ) -> main_models.CheckModifyConfigNeedRestartResponse:
        runtime = RuntimeOptions()
        return self.check_modify_config_need_restart_with_options(request, runtime)

    async def check_modify_config_need_restart_async(
        self,
        request: main_models.CheckModifyConfigNeedRestartRequest,
    ) -> main_models.CheckModifyConfigNeedRestartResponse:
        runtime = RuntimeOptions()
        return await self.check_modify_config_need_restart_with_options_async(request, runtime)

    def check_monitor_alert_with_options(
        self,
        request: main_models.CheckMonitorAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckMonitorAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckMonitorAlert',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckMonitorAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_monitor_alert_with_options_async(
        self,
        request: main_models.CheckMonitorAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckMonitorAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckMonitorAlert',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckMonitorAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_monitor_alert(
        self,
        request: main_models.CheckMonitorAlertRequest,
    ) -> main_models.CheckMonitorAlertResponse:
        runtime = RuntimeOptions()
        return self.check_monitor_alert_with_options(request, runtime)

    async def check_monitor_alert_async(
        self,
        request: main_models.CheckMonitorAlertRequest,
    ) -> main_models.CheckMonitorAlertResponse:
        runtime = RuntimeOptions()
        return await self.check_monitor_alert_with_options_async(request, runtime)

    def check_scale_out_balanced_with_options(
        self,
        request: main_models.CheckScaleOutBalancedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckScaleOutBalancedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckScaleOutBalanced',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckScaleOutBalancedResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_scale_out_balanced_with_options_async(
        self,
        request: main_models.CheckScaleOutBalancedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckScaleOutBalancedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckScaleOutBalanced',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckScaleOutBalancedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_scale_out_balanced(
        self,
        request: main_models.CheckScaleOutBalancedRequest,
    ) -> main_models.CheckScaleOutBalancedResponse:
        runtime = RuntimeOptions()
        return self.check_scale_out_balanced_with_options(request, runtime)

    async def check_scale_out_balanced_async(
        self,
        request: main_models.CheckScaleOutBalancedRequest,
    ) -> main_models.CheckScaleOutBalancedResponse:
        runtime = RuntimeOptions()
        return await self.check_scale_out_balanced_with_options_async(request, runtime)

    def check_service_linked_role_with_options(
        self,
        request: main_models.CheckServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceLinkedRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRole',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_with_options_async(
        self,
        request: main_models.CheckServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceLinkedRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRole',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role(
        self,
        request: main_models.CheckServiceLinkedRoleRequest,
    ) -> main_models.CheckServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    async def check_service_linked_role_async(
        self,
        request: main_models.CheckServiceLinkedRoleRequest,
    ) -> main_models.CheckServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return await self.check_service_linked_role_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: main_models.CreateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: main_models.CreateAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: main_models.CreateAccountRequest,
    ) -> main_models.CreateAccountResponse:
        runtime = RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: main_models.CreateAccountRequest,
    ) -> main_models.CreateAccountResponse:
        runtime = RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_account_and_authority_with_options(
        self,
        request: main_models.CreateAccountAndAuthorityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountAndAuthorityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.allow_databases):
            query['AllowDatabases'] = request.allow_databases
        if not DaraCore.is_null(request.allow_dictionaries):
            query['AllowDictionaries'] = request.allow_dictionaries
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.ddl_authority):
            query['DdlAuthority'] = request.ddl_authority
        if not DaraCore.is_null(request.dml_authority):
            query['DmlAuthority'] = request.dml_authority
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.total_databases):
            query['TotalDatabases'] = request.total_databases
        if not DaraCore.is_null(request.total_dictionaries):
            query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccountAndAuthority',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountAndAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_and_authority_with_options_async(
        self,
        request: main_models.CreateAccountAndAuthorityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountAndAuthorityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.allow_databases):
            query['AllowDatabases'] = request.allow_databases
        if not DaraCore.is_null(request.allow_dictionaries):
            query['AllowDictionaries'] = request.allow_dictionaries
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.ddl_authority):
            query['DdlAuthority'] = request.ddl_authority
        if not DaraCore.is_null(request.dml_authority):
            query['DmlAuthority'] = request.dml_authority
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.total_databases):
            query['TotalDatabases'] = request.total_databases
        if not DaraCore.is_null(request.total_dictionaries):
            query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccountAndAuthority',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountAndAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account_and_authority(
        self,
        request: main_models.CreateAccountAndAuthorityRequest,
    ) -> main_models.CreateAccountAndAuthorityResponse:
        runtime = RuntimeOptions()
        return self.create_account_and_authority_with_options(request, runtime)

    async def create_account_and_authority_async(
        self,
        request: main_models.CreateAccountAndAuthorityRequest,
    ) -> main_models.CreateAccountAndAuthorityResponse:
        runtime = RuntimeOptions()
        return await self.create_account_and_authority_with_options_async(request, runtime)

    def create_backup_policy_with_options(
        self,
        request: main_models.CreateBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not DaraCore.is_null(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackupPolicy',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_policy_with_options_async(
        self,
        request: main_models.CreateBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not DaraCore.is_null(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackupPolicy',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup_policy(
        self,
        request: main_models.CreateBackupPolicyRequest,
    ) -> main_models.CreateBackupPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_backup_policy_with_options(request, runtime)

    async def create_backup_policy_async(
        self,
        request: main_models.CreateBackupPolicyRequest,
    ) -> main_models.CreateBackupPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_backup_policy_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: main_models.CreateDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetID'] = request.backup_set_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbcluster_category):
            query['DBClusterCategory'] = request.dbcluster_category
        if not DaraCore.is_null(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not DaraCore.is_null(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not DaraCore.is_null(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not DaraCore.is_null(request.db_node_storage_type):
            query['DbNodeStorageType'] = request.db_node_storage_type
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.encryption_type):
            query['EncryptionType'] = request.encryption_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_dbcluster_id):
            query['SourceDBClusterId'] = request.source_dbcluster_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_bak):
            query['VSwitchBak'] = request.v_switch_bak
        if not DaraCore.is_null(request.v_switch_bak_2):
            query['VSwitchBak2'] = request.v_switch_bak_2
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zond_id_bak_2):
            query['ZondIdBak2'] = request.zond_id_bak_2
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not DaraCore.is_null(request.zone_id_bak):
            query['ZoneIdBak'] = request.zone_id_bak
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBInstance',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        request: main_models.CreateDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetID'] = request.backup_set_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbcluster_category):
            query['DBClusterCategory'] = request.dbcluster_category
        if not DaraCore.is_null(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not DaraCore.is_null(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not DaraCore.is_null(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not DaraCore.is_null(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not DaraCore.is_null(request.db_node_storage_type):
            query['DbNodeStorageType'] = request.db_node_storage_type
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.encryption_type):
            query['EncryptionType'] = request.encryption_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_dbcluster_id):
            query['SourceDBClusterId'] = request.source_dbcluster_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_bak):
            query['VSwitchBak'] = request.v_switch_bak
        if not DaraCore.is_null(request.v_switch_bak_2):
            query['VSwitchBak2'] = request.v_switch_bak_2
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zond_id_bak_2):
            query['ZondIdBak2'] = request.zond_id_bak_2
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not DaraCore.is_null(request.zone_id_bak):
            query['ZoneIdBak'] = request.zone_id_bak
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBInstance',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance(
        self,
        request: main_models.CreateDBInstanceRequest,
    ) -> main_models.CreateDBInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: main_models.CreateDBInstanceRequest,
    ) -> main_models.CreateDBInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_monitor_data_report_with_options(
        self,
        request: main_models.CreateMonitorDataReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorDataReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorDataReport',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorDataReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_data_report_with_options_async(
        self,
        request: main_models.CreateMonitorDataReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorDataReportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorDataReport',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorDataReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_data_report(
        self,
        request: main_models.CreateMonitorDataReportRequest,
    ) -> main_models.CreateMonitorDataReportResponse:
        runtime = RuntimeOptions()
        return self.create_monitor_data_report_with_options(request, runtime)

    async def create_monitor_data_report_async(
        self,
        request: main_models.CreateMonitorDataReportRequest,
    ) -> main_models.CreateMonitorDataReportResponse:
        runtime = RuntimeOptions()
        return await self.create_monitor_data_report_with_options_async(request, runtime)

    def create_ossstorage_with_options(
        self,
        request: main_models.CreateOSSStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOSSStorageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOSSStorage',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOSSStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ossstorage_with_options_async(
        self,
        request: main_models.CreateOSSStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOSSStorageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOSSStorage',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOSSStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ossstorage(
        self,
        request: main_models.CreateOSSStorageRequest,
    ) -> main_models.CreateOSSStorageResponse:
        runtime = RuntimeOptions()
        return self.create_ossstorage_with_options(request, runtime)

    async def create_ossstorage_async(
        self,
        request: main_models.CreateOSSStorageRequest,
    ) -> main_models.CreateOSSStorageResponse:
        runtime = RuntimeOptions()
        return await self.create_ossstorage_with_options_async(request, runtime)

    def create_ports_for_click_house_with_options(
        self,
        request: main_models.CreatePortsForClickHouseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePortsForClickHouseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_type):
            query['PortType'] = request.port_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePortsForClickHouse',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePortsForClickHouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ports_for_click_house_with_options_async(
        self,
        request: main_models.CreatePortsForClickHouseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePortsForClickHouseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port_type):
            query['PortType'] = request.port_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePortsForClickHouse',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePortsForClickHouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ports_for_click_house(
        self,
        request: main_models.CreatePortsForClickHouseRequest,
    ) -> main_models.CreatePortsForClickHouseResponse:
        runtime = RuntimeOptions()
        return self.create_ports_for_click_house_with_options(request, runtime)

    async def create_ports_for_click_house_async(
        self,
        request: main_models.CreatePortsForClickHouseRequest,
    ) -> main_models.CreatePortsForClickHouseResponse:
        runtime = RuntimeOptions()
        return await self.create_ports_for_click_house_with_options_async(request, runtime)

    def create_rdsto_clickhouse_db_with_options(
        self,
        request: main_models.CreateRDSToClickhouseDbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRDSToClickhouseDbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ck_password):
            query['CkPassword'] = request.ck_password
        if not DaraCore.is_null(request.ck_user_name):
            query['CkUserName'] = request.ck_user_name
        if not DaraCore.is_null(request.clickhouse_port):
            query['ClickhousePort'] = request.clickhouse_port
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.limit_upper):
            query['LimitUpper'] = request.limit_upper
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rds_id):
            query['RdsId'] = request.rds_id
        if not DaraCore.is_null(request.rds_password):
            query['RdsPassword'] = request.rds_password
        if not DaraCore.is_null(request.rds_port):
            query['RdsPort'] = request.rds_port
        if not DaraCore.is_null(request.rds_user_name):
            query['RdsUserName'] = request.rds_user_name
        if not DaraCore.is_null(request.rds_vpc_id):
            query['RdsVpcId'] = request.rds_vpc_id
        if not DaraCore.is_null(request.rds_vpc_url):
            query['RdsVpcUrl'] = request.rds_vpc_url
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.skip_unsupported):
            query['SkipUnsupported'] = request.skip_unsupported
        if not DaraCore.is_null(request.syn_db_tables):
            query['SynDbTables'] = request.syn_db_tables
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRDSToClickhouseDb',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRDSToClickhouseDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rdsto_clickhouse_db_with_options_async(
        self,
        request: main_models.CreateRDSToClickhouseDbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRDSToClickhouseDbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ck_password):
            query['CkPassword'] = request.ck_password
        if not DaraCore.is_null(request.ck_user_name):
            query['CkUserName'] = request.ck_user_name
        if not DaraCore.is_null(request.clickhouse_port):
            query['ClickhousePort'] = request.clickhouse_port
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.limit_upper):
            query['LimitUpper'] = request.limit_upper
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rds_id):
            query['RdsId'] = request.rds_id
        if not DaraCore.is_null(request.rds_password):
            query['RdsPassword'] = request.rds_password
        if not DaraCore.is_null(request.rds_port):
            query['RdsPort'] = request.rds_port
        if not DaraCore.is_null(request.rds_user_name):
            query['RdsUserName'] = request.rds_user_name
        if not DaraCore.is_null(request.rds_vpc_id):
            query['RdsVpcId'] = request.rds_vpc_id
        if not DaraCore.is_null(request.rds_vpc_url):
            query['RdsVpcUrl'] = request.rds_vpc_url
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.skip_unsupported):
            query['SkipUnsupported'] = request.skip_unsupported
        if not DaraCore.is_null(request.syn_db_tables):
            query['SynDbTables'] = request.syn_db_tables
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRDSToClickhouseDb',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRDSToClickhouseDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rdsto_clickhouse_db(
        self,
        request: main_models.CreateRDSToClickhouseDbRequest,
    ) -> main_models.CreateRDSToClickhouseDbResponse:
        runtime = RuntimeOptions()
        return self.create_rdsto_clickhouse_db_with_options(request, runtime)

    async def create_rdsto_clickhouse_db_async(
        self,
        request: main_models.CreateRDSToClickhouseDbRequest,
    ) -> main_models.CreateRDSToClickhouseDbResponse:
        runtime = RuntimeOptions()
        return await self.create_rdsto_clickhouse_db_with_options_async(request, runtime)

    def create_slbwith_options(
        self,
        request: main_models.CreateSLBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSLBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSLB',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSLBResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_slbwith_options_async(
        self,
        request: main_models.CreateSLBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSLBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSLB',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSLBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_slb(
        self,
        request: main_models.CreateSLBRequest,
    ) -> main_models.CreateSLBResponse:
        runtime = RuntimeOptions()
        return self.create_slbwith_options(request, runtime)

    async def create_slb_async(
        self,
        request: main_models.CreateSLBRequest,
    ) -> main_models.CreateSLBResponse:
        runtime = RuntimeOptions()
        return await self.create_slbwith_options_async(request, runtime)

    def create_sqlaccount_with_options(
        self,
        request: main_models.CreateSQLAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSQLAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSQLAccount',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSQLAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sqlaccount_with_options_async(
        self,
        request: main_models.CreateSQLAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSQLAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSQLAccount',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSQLAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sqlaccount(
        self,
        request: main_models.CreateSQLAccountRequest,
    ) -> main_models.CreateSQLAccountResponse:
        runtime = RuntimeOptions()
        return self.create_sqlaccount_with_options(request, runtime)

    async def create_sqlaccount_async(
        self,
        request: main_models.CreateSQLAccountRequest,
    ) -> main_models.CreateSQLAccountResponse:
        runtime = RuntimeOptions()
        return await self.create_sqlaccount_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRole',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRole',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: main_models.CreateServiceLinkedRoleRequest,
    ) -> main_models.CreateServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: main_models.DeleteAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: main_models.DeleteAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: main_models.DeleteAccountRequest,
    ) -> main_models.DeleteAccountResponse:
        runtime = RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: main_models.DeleteAccountRequest,
    ) -> main_models.DeleteAccountResponse:
        runtime = RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_backup_policy_with_options(
        self,
        request: main_models.DeleteBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackupPolicy',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_policy_with_options_async(
        self,
        request: main_models.DeleteBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackupPolicy',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup_policy(
        self,
        request: main_models.DeleteBackupPolicyRequest,
    ) -> main_models.DeleteBackupPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_backup_policy_with_options(request, runtime)

    async def delete_backup_policy_async(
        self,
        request: main_models.DeleteBackupPolicyRequest,
    ) -> main_models.DeleteBackupPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_backup_policy_with_options_async(request, runtime)

    def delete_dbcluster_with_options(
        self,
        request: main_models.DeleteDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBCluster',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbcluster_with_options_async(
        self,
        request: main_models.DeleteDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBCluster',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbcluster(
        self,
        request: main_models.DeleteDBClusterRequest,
    ) -> main_models.DeleteDBClusterResponse:
        runtime = RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    async def delete_dbcluster_async(
        self,
        request: main_models.DeleteDBClusterRequest,
    ) -> main_models.DeleteDBClusterResponse:
        runtime = RuntimeOptions()
        return await self.delete_dbcluster_with_options_async(request, runtime)

    def delete_slbwith_options(
        self,
        request: main_models.DeleteSLBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSLBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSLB',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSLBResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_slbwith_options_async(
        self,
        request: main_models.DeleteSLBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSLBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSLB',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSLBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_slb(
        self,
        request: main_models.DeleteSLBRequest,
    ) -> main_models.DeleteSLBResponse:
        runtime = RuntimeOptions()
        return self.delete_slbwith_options(request, runtime)

    async def delete_slb_async(
        self,
        request: main_models.DeleteSLBRequest,
    ) -> main_models.DeleteSLBResponse:
        runtime = RuntimeOptions()
        return await self.delete_slbwith_options_async(request, runtime)

    def delete_syndb_with_options(
        self,
        request: main_models.DeleteSyndbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSyndbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.syn_db):
            query['SynDb'] = request.syn_db
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSyndb',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSyndbResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_syndb_with_options_async(
        self,
        request: main_models.DeleteSyndbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSyndbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.syn_db):
            query['SynDb'] = request.syn_db
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSyndb',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSyndbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_syndb(
        self,
        request: main_models.DeleteSyndbRequest,
    ) -> main_models.DeleteSyndbResponse:
        runtime = RuntimeOptions()
        return self.delete_syndb_with_options(request, runtime)

    async def delete_syndb_async(
        self,
        request: main_models.DeleteSyndbRequest,
    ) -> main_models.DeleteSyndbResponse:
        runtime = RuntimeOptions()
        return await self.delete_syndb_with_options_async(request, runtime)

    def describe_account_authority_with_options(
        self,
        request: main_models.DescribeAccountAuthorityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountAuthorityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountAuthority',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_authority_with_options_async(
        self,
        request: main_models.DescribeAccountAuthorityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountAuthorityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountAuthority',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_authority(
        self,
        request: main_models.DescribeAccountAuthorityRequest,
    ) -> main_models.DescribeAccountAuthorityResponse:
        runtime = RuntimeOptions()
        return self.describe_account_authority_with_options(request, runtime)

    async def describe_account_authority_async(
        self,
        request: main_models.DescribeAccountAuthorityRequest,
    ) -> main_models.DescribeAccountAuthorityResponse:
        runtime = RuntimeOptions()
        return await self.describe_account_authority_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: main_models.DescribeAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccounts',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: main_models.DescribeAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccounts',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: main_models.DescribeAccountsRequest,
    ) -> main_models.DescribeAccountsResponse:
        runtime = RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: main_models.DescribeAccountsRequest,
    ) -> main_models.DescribeAccountsResponse:
        runtime = RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_active_operation_maintain_conf_with_options(
        self,
        request: main_models.DescribeActiveOperationMaintainConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationMaintainConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationMaintainConf',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationMaintainConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_maintain_conf_with_options_async(
        self,
        request: main_models.DescribeActiveOperationMaintainConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationMaintainConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationMaintainConf',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationMaintainConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_maintain_conf(
        self,
        request: main_models.DescribeActiveOperationMaintainConfRequest,
    ) -> main_models.DescribeActiveOperationMaintainConfResponse:
        runtime = RuntimeOptions()
        return self.describe_active_operation_maintain_conf_with_options(request, runtime)

    async def describe_active_operation_maintain_conf_async(
        self,
        request: main_models.DescribeActiveOperationMaintainConfRequest,
    ) -> main_models.DescribeActiveOperationMaintainConfResponse:
        runtime = RuntimeOptions()
        return await self.describe_active_operation_maintain_conf_with_options_async(request, runtime)

    def describe_active_operation_tasks_with_options(
        self,
        request: main_models.DescribeActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_cancel):
            query['AllowCancel'] = request.allow_cancel
        if not DaraCore.is_null(request.allow_change):
            query['AllowChange'] = request.allow_change
        if not DaraCore.is_null(request.change_level):
            query['ChangeLevel'] = request.change_level
        if not DaraCore.is_null(request.db_type):
            query['DbType'] = request.db_type
        if not DaraCore.is_null(request.ins_name):
            query['InsName'] = request.ins_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTasks',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_tasks_with_options_async(
        self,
        request: main_models.DescribeActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allow_cancel):
            query['AllowCancel'] = request.allow_cancel
        if not DaraCore.is_null(request.allow_change):
            query['AllowChange'] = request.allow_change
        if not DaraCore.is_null(request.change_level):
            query['ChangeLevel'] = request.change_level
        if not DaraCore.is_null(request.db_type):
            query['DbType'] = request.db_type
        if not DaraCore.is_null(request.ins_name):
            query['InsName'] = request.ins_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTasks',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_tasks(
        self,
        request: main_models.DescribeActiveOperationTasksRequest,
    ) -> main_models.DescribeActiveOperationTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_active_operation_tasks_with_options(request, runtime)

    async def describe_active_operation_tasks_async(
        self,
        request: main_models.DescribeActiveOperationTasksRequest,
    ) -> main_models.DescribeActiveOperationTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_active_operation_tasks_with_options_async(request, runtime)

    def describe_all_data_source_with_options(
        self,
        request: main_models.DescribeAllDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllDataSource',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_data_source_with_options_async(
        self,
        request: main_models.DescribeAllDataSourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllDataSourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllDataSource',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_data_source(
        self,
        request: main_models.DescribeAllDataSourceRequest,
    ) -> main_models.DescribeAllDataSourceResponse:
        runtime = RuntimeOptions()
        return self.describe_all_data_source_with_options(request, runtime)

    async def describe_all_data_source_async(
        self,
        request: main_models.DescribeAllDataSourceRequest,
    ) -> main_models.DescribeAllDataSourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_all_data_source_with_options_async(request, runtime)

    def describe_all_data_sources_with_options(
        self,
        request: main_models.DescribeAllDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllDataSources',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_data_sources_with_options_async(
        self,
        request: main_models.DescribeAllDataSourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllDataSourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllDataSources',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_data_sources(
        self,
        request: main_models.DescribeAllDataSourcesRequest,
    ) -> main_models.DescribeAllDataSourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_all_data_sources_with_options(request, runtime)

    async def describe_all_data_sources_async(
        self,
        request: main_models.DescribeAllDataSourcesRequest,
    ) -> main_models.DescribeAllDataSourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_all_data_sources_with_options_async(request, runtime)

    def describe_auto_renew_attribute_with_options(
        self,
        request: main_models.DescribeAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoRenewAttribute',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_renew_attribute_with_options_async(
        self,
        request: main_models.DescribeAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAutoRenewAttribute',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_renew_attribute(
        self,
        request: main_models.DescribeAutoRenewAttributeRequest,
    ) -> main_models.DescribeAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_auto_renew_attribute_with_options(request, runtime)

    async def describe_auto_renew_attribute_async(
        self,
        request: main_models.DescribeAutoRenewAttributeRequest,
    ) -> main_models.DescribeAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_auto_renew_attribute_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: main_models.DescribeBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: main_models.DescribeBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: main_models.DescribeBackupPolicyRequest,
    ) -> main_models.DescribeBackupPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: main_models.DescribeBackupPolicyRequest,
    ) -> main_models.DescribeBackupPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: main_models.DescribeBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackups',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: main_models.DescribeBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackups',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: main_models.DescribeBackupsRequest,
    ) -> main_models.DescribeBackupsResponse:
        runtime = RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: main_models.DescribeBackupsRequest,
    ) -> main_models.DescribeBackupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_columns_with_options(
        self,
        request: main_models.DescribeColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumns',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columns_with_options_async(
        self,
        request: main_models.DescribeColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumns',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columns(
        self,
        request: main_models.DescribeColumnsRequest,
    ) -> main_models.DescribeColumnsResponse:
        runtime = RuntimeOptions()
        return self.describe_columns_with_options(request, runtime)

    async def describe_columns_async(
        self,
        request: main_models.DescribeColumnsRequest,
    ) -> main_models.DescribeColumnsResponse:
        runtime = RuntimeOptions()
        return await self.describe_columns_with_options_async(request, runtime)

    def describe_config_history_with_options(
        self,
        request: main_models.DescribeConfigHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfigHistoryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfigHistory',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfigHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_config_history_with_options_async(
        self,
        request: main_models.DescribeConfigHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfigHistoryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfigHistory',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfigHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_config_history(
        self,
        request: main_models.DescribeConfigHistoryRequest,
    ) -> main_models.DescribeConfigHistoryResponse:
        runtime = RuntimeOptions()
        return self.describe_config_history_with_options(request, runtime)

    async def describe_config_history_async(
        self,
        request: main_models.DescribeConfigHistoryRequest,
    ) -> main_models.DescribeConfigHistoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_config_history_with_options_async(request, runtime)

    def describe_config_version_difference_with_options(
        self,
        request: main_models.DescribeConfigVersionDifferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfigVersionDifferenceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfigVersionDifference',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfigVersionDifferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_config_version_difference_with_options_async(
        self,
        request: main_models.DescribeConfigVersionDifferenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeConfigVersionDifferenceResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeConfigVersionDifference',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeConfigVersionDifferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_config_version_difference(
        self,
        request: main_models.DescribeConfigVersionDifferenceRequest,
    ) -> main_models.DescribeConfigVersionDifferenceResponse:
        runtime = RuntimeOptions()
        return self.describe_config_version_difference_with_options(request, runtime)

    async def describe_config_version_difference_async(
        self,
        request: main_models.DescribeConfigVersionDifferenceRequest,
    ) -> main_models.DescribeConfigVersionDifferenceResponse:
        runtime = RuntimeOptions()
        return await self.describe_config_version_difference_with_options_async(request, runtime)

    def describe_dbcluster_access_white_list_with_options(
        self,
        request: main_models.DescribeDBClusterAccessWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterAccessWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterAccessWhiteList',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_access_white_list_with_options_async(
        self,
        request: main_models.DescribeDBClusterAccessWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterAccessWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterAccessWhiteList',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_access_white_list(
        self,
        request: main_models.DescribeDBClusterAccessWhiteListRequest,
    ) -> main_models.DescribeDBClusterAccessWhiteListResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_access_white_list_with_options(request, runtime)

    async def describe_dbcluster_access_white_list_async(
        self,
        request: main_models.DescribeDBClusterAccessWhiteListRequest,
    ) -> main_models.DescribeDBClusterAccessWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_access_white_list_with_options_async(request, runtime)

    def describe_dbcluster_attribute_with_options(
        self,
        request: main_models.DescribeDBClusterAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterAttribute',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_attribute_with_options_async(
        self,
        request: main_models.DescribeDBClusterAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterAttribute',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_attribute(
        self,
        request: main_models.DescribeDBClusterAttributeRequest,
    ) -> main_models.DescribeDBClusterAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_attribute_with_options(request, runtime)

    async def describe_dbcluster_attribute_async(
        self,
        request: main_models.DescribeDBClusterAttributeRequest,
    ) -> main_models.DescribeDBClusterAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_attribute_with_options_async(request, runtime)

    def describe_dbcluster_config_with_options(
        self,
        request: main_models.DescribeDBClusterConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterConfig',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_config_with_options_async(
        self,
        request: main_models.DescribeDBClusterConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterConfig',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_config(
        self,
        request: main_models.DescribeDBClusterConfigRequest,
    ) -> main_models.DescribeDBClusterConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_config_with_options(request, runtime)

    async def describe_dbcluster_config_async(
        self,
        request: main_models.DescribeDBClusterConfigRequest,
    ) -> main_models.DescribeDBClusterConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_config_with_options_async(request, runtime)

    def describe_dbcluster_config_in_xmlwith_options(
        self,
        request: main_models.DescribeDBClusterConfigInXMLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterConfigInXMLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterConfigInXML',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterConfigInXMLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_config_in_xmlwith_options_async(
        self,
        request: main_models.DescribeDBClusterConfigInXMLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterConfigInXMLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterConfigInXML',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterConfigInXMLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_config_in_xml(
        self,
        request: main_models.DescribeDBClusterConfigInXMLRequest,
    ) -> main_models.DescribeDBClusterConfigInXMLResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_config_in_xmlwith_options(request, runtime)

    async def describe_dbcluster_config_in_xml_async(
        self,
        request: main_models.DescribeDBClusterConfigInXMLRequest,
    ) -> main_models.DescribeDBClusterConfigInXMLResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_config_in_xmlwith_options_async(request, runtime)

    def describe_dbcluster_net_info_items_with_options(
        self,
        request: main_models.DescribeDBClusterNetInfoItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterNetInfoItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterNetInfoItems',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterNetInfoItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_net_info_items_with_options_async(
        self,
        request: main_models.DescribeDBClusterNetInfoItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterNetInfoItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterNetInfoItems',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterNetInfoItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_net_info_items(
        self,
        request: main_models.DescribeDBClusterNetInfoItemsRequest,
    ) -> main_models.DescribeDBClusterNetInfoItemsResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_net_info_items_with_options(request, runtime)

    async def describe_dbcluster_net_info_items_async(
        self,
        request: main_models.DescribeDBClusterNetInfoItemsRequest,
    ) -> main_models.DescribeDBClusterNetInfoItemsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_net_info_items_with_options_async(request, runtime)

    def describe_dbcluster_node_infos_with_options(
        self,
        request: main_models.DescribeDBClusterNodeInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterNodeInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterNodeInfos',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterNodeInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_node_infos_with_options_async(
        self,
        request: main_models.DescribeDBClusterNodeInfosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterNodeInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterNodeInfos',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterNodeInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_node_infos(
        self,
        request: main_models.DescribeDBClusterNodeInfosRequest,
    ) -> main_models.DescribeDBClusterNodeInfosResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_node_infos_with_options(request, runtime)

    async def describe_dbcluster_node_infos_async(
        self,
        request: main_models.DescribeDBClusterNodeInfosRequest,
    ) -> main_models.DescribeDBClusterNodeInfosResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_node_infos_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: main_models.DescribeDBClusterPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterPerformance',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: main_models.DescribeDBClusterPerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterPerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterPerformance',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_performance(
        self,
        request: main_models.DescribeDBClusterPerformanceRequest,
    ) -> main_models.DescribeDBClusterPerformanceResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: main_models.DescribeDBClusterPerformanceRequest,
    ) -> main_models.DescribeDBClusterPerformanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def describe_dbcluster_status_set_with_options(
        self,
        request: main_models.DescribeDBClusterStatusSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterStatusSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterStatusSet',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterStatusSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_status_set_with_options_async(
        self,
        request: main_models.DescribeDBClusterStatusSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterStatusSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterStatusSet',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterStatusSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_status_set(
        self,
        request: main_models.DescribeDBClusterStatusSetRequest,
    ) -> main_models.DescribeDBClusterStatusSetResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_status_set_with_options(request, runtime)

    async def describe_dbcluster_status_set_async(
        self,
        request: main_models.DescribeDBClusterStatusSetRequest,
    ) -> main_models.DescribeDBClusterStatusSetResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_status_set_with_options_async(request, runtime)

    def describe_dbclusters_with_options(
        self,
        request: main_models.DescribeDBClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not DaraCore.is_null(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusters',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbclusters_with_options_async(
        self,
        request: main_models.DescribeDBClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not DaraCore.is_null(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusters',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbclusters(
        self,
        request: main_models.DescribeDBClustersRequest,
    ) -> main_models.DescribeDBClustersResponse:
        runtime = RuntimeOptions()
        return self.describe_dbclusters_with_options(request, runtime)

    async def describe_dbclusters_async(
        self,
        request: main_models.DescribeDBClustersRequest,
    ) -> main_models.DescribeDBClustersResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbclusters_with_options_async(request, runtime)

    def describe_dbconfig_with_options(
        self,
        request: main_models.DescribeDBConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBConfig',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbconfig_with_options_async(
        self,
        request: main_models.DescribeDBConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBConfig',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbconfig(
        self,
        request: main_models.DescribeDBConfigRequest,
    ) -> main_models.DescribeDBConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_dbconfig_with_options(request, runtime)

    async def describe_dbconfig_async(
        self,
        request: main_models.DescribeDBConfigRequest,
    ) -> main_models.DescribeDBConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbconfig_with_options_async(request, runtime)

    def describe_event_meta_info_with_options(
        self,
        request: main_models.DescribeEventMetaInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventMetaInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventMetaInfo',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventMetaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_meta_info_with_options_async(
        self,
        request: main_models.DescribeEventMetaInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventMetaInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.source_code):
            query['SourceCode'] = request.source_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventMetaInfo',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventMetaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_meta_info(
        self,
        request: main_models.DescribeEventMetaInfoRequest,
    ) -> main_models.DescribeEventMetaInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_event_meta_info_with_options(request, runtime)

    async def describe_event_meta_info_async(
        self,
        request: main_models.DescribeEventMetaInfoRequest,
    ) -> main_models.DescribeEventMetaInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_meta_info_with_options_async(request, runtime)

    def describe_ossstorage_with_options(
        self,
        request: main_models.DescribeOSSStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOSSStorageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOSSStorage',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOSSStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ossstorage_with_options_async(
        self,
        request: main_models.DescribeOSSStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOSSStorageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOSSStorage',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOSSStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ossstorage(
        self,
        request: main_models.DescribeOSSStorageRequest,
    ) -> main_models.DescribeOSSStorageResponse:
        runtime = RuntimeOptions()
        return self.describe_ossstorage_with_options(request, runtime)

    async def describe_ossstorage_async(
        self,
        request: main_models.DescribeOSSStorageRequest,
    ) -> main_models.DescribeOSSStorageResponse:
        runtime = RuntimeOptions()
        return await self.describe_ossstorage_with_options_async(request, runtime)

    def describe_process_list_with_options(
        self,
        request: main_models.DescribeProcessListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProcessListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not DaraCore.is_null(request.initial_user):
            query['InitialUser'] = request.initial_user
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProcessList',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProcessListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_process_list_with_options_async(
        self,
        request: main_models.DescribeProcessListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProcessListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not DaraCore.is_null(request.initial_user):
            query['InitialUser'] = request.initial_user
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProcessList',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProcessListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_process_list(
        self,
        request: main_models.DescribeProcessListRequest,
    ) -> main_models.DescribeProcessListResponse:
        runtime = RuntimeOptions()
        return self.describe_process_list_with_options(request, runtime)

    async def describe_process_list_async(
        self,
        request: main_models.DescribeProcessListRequest,
    ) -> main_models.DescribeProcessListResponse:
        runtime = RuntimeOptions()
        return await self.describe_process_list_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-11-11',
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
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-11-11',
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

    def describe_schemas_with_options(
        self,
        request: main_models.DescribeSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSchemasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSchemas',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_schemas_with_options_async(
        self,
        request: main_models.DescribeSchemasRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSchemasResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSchemas',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_schemas(
        self,
        request: main_models.DescribeSchemasRequest,
    ) -> main_models.DescribeSchemasResponse:
        runtime = RuntimeOptions()
        return self.describe_schemas_with_options(request, runtime)

    async def describe_schemas_async(
        self,
        request: main_models.DescribeSchemasRequest,
    ) -> main_models.DescribeSchemasResponse:
        runtime = RuntimeOptions()
        return await self.describe_schemas_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogRecords',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogRecords',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_slow_log_trend_with_options(
        self,
        request: main_models.DescribeSlowLogTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogTrend',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowLogTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_trend_with_options_async(
        self,
        request: main_models.DescribeSlowLogTrendRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogTrend',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSlowLogTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_trend(
        self,
        request: main_models.DescribeSlowLogTrendRequest,
    ) -> main_models.DescribeSlowLogTrendResponse:
        runtime = RuntimeOptions()
        return self.describe_slow_log_trend_with_options(request, runtime)

    async def describe_slow_log_trend_async(
        self,
        request: main_models.DescribeSlowLogTrendRequest,
    ) -> main_models.DescribeSlowLogTrendResponse:
        runtime = RuntimeOptions()
        return await self.describe_slow_log_trend_with_options_async(request, runtime)

    def describe_syn_db_tables_with_options(
        self,
        request: main_models.DescribeSynDbTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynDbTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.syn_db):
            query['SynDb'] = request.syn_db
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynDbTables',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynDbTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_syn_db_tables_with_options_async(
        self,
        request: main_models.DescribeSynDbTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynDbTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.syn_db):
            query['SynDb'] = request.syn_db
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynDbTables',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynDbTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_syn_db_tables(
        self,
        request: main_models.DescribeSynDbTablesRequest,
    ) -> main_models.DescribeSynDbTablesResponse:
        runtime = RuntimeOptions()
        return self.describe_syn_db_tables_with_options(request, runtime)

    async def describe_syn_db_tables_async(
        self,
        request: main_models.DescribeSynDbTablesRequest,
    ) -> main_models.DescribeSynDbTablesResponse:
        runtime = RuntimeOptions()
        return await self.describe_syn_db_tables_with_options_async(request, runtime)

    def describe_syn_dbs_with_options(
        self,
        request: main_models.DescribeSynDbsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynDbsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynDbs',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynDbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_syn_dbs_with_options_async(
        self,
        request: main_models.DescribeSynDbsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSynDbsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSynDbs',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSynDbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_syn_dbs(
        self,
        request: main_models.DescribeSynDbsRequest,
    ) -> main_models.DescribeSynDbsResponse:
        runtime = RuntimeOptions()
        return self.describe_syn_dbs_with_options(request, runtime)

    async def describe_syn_dbs_async(
        self,
        request: main_models.DescribeSynDbsRequest,
    ) -> main_models.DescribeSynDbsResponse:
        runtime = RuntimeOptions()
        return await self.describe_syn_dbs_with_options_async(request, runtime)

    def describe_tables_with_options(
        self,
        request: main_models.DescribeTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTables',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tables_with_options_async(
        self,
        request: main_models.DescribeTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTables',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tables(
        self,
        request: main_models.DescribeTablesRequest,
    ) -> main_models.DescribeTablesResponse:
        runtime = RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    async def describe_tables_async(
        self,
        request: main_models.DescribeTablesRequest,
    ) -> main_models.DescribeTablesResponse:
        runtime = RuntimeOptions()
        return await self.describe_tables_with_options_async(request, runtime)

    def describe_transfer_history_with_options(
        self,
        request: main_models.DescribeTransferHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTransferHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTransferHistory',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTransferHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transfer_history_with_options_async(
        self,
        request: main_models.DescribeTransferHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTransferHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTransferHistory',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTransferHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transfer_history(
        self,
        request: main_models.DescribeTransferHistoryRequest,
    ) -> main_models.DescribeTransferHistoryResponse:
        runtime = RuntimeOptions()
        return self.describe_transfer_history_with_options(request, runtime)

    async def describe_transfer_history_async(
        self,
        request: main_models.DescribeTransferHistoryRequest,
    ) -> main_models.DescribeTransferHistoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_transfer_history_with_options_async(request, runtime)

    def describe_user_encryption_key_list_with_options(
        self,
        request: main_models.DescribeUserEncryptionKeyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserEncryptionKeyListResponse:
        request.validate()
        query = {}
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
            action = 'DescribeUserEncryptionKeyList',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserEncryptionKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_encryption_key_list_with_options_async(
        self,
        request: main_models.DescribeUserEncryptionKeyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserEncryptionKeyListResponse:
        request.validate()
        query = {}
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
            action = 'DescribeUserEncryptionKeyList',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUserEncryptionKeyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_encryption_key_list(
        self,
        request: main_models.DescribeUserEncryptionKeyListRequest,
    ) -> main_models.DescribeUserEncryptionKeyListResponse:
        runtime = RuntimeOptions()
        return self.describe_user_encryption_key_list_with_options(request, runtime)

    async def describe_user_encryption_key_list_async(
        self,
        request: main_models.DescribeUserEncryptionKeyListRequest,
    ) -> main_models.DescribeUserEncryptionKeyListResponse:
        runtime = RuntimeOptions()
        return await self.describe_user_encryption_key_list_with_options_async(request, runtime)

    def elect_zookeeper_leader_with_options(
        self,
        request: main_models.ElectZookeeperLeaderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ElectZookeeperLeaderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.disable_write):
            query['DisableWrite'] = request.disable_write
        if not DaraCore.is_null(request.elect_time):
            query['ElectTime'] = request.elect_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ElectZookeeperLeader',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ElectZookeeperLeaderResponse(),
            self.call_api(params, req, runtime)
        )

    async def elect_zookeeper_leader_with_options_async(
        self,
        request: main_models.ElectZookeeperLeaderRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ElectZookeeperLeaderResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.disable_write):
            query['DisableWrite'] = request.disable_write
        if not DaraCore.is_null(request.elect_time):
            query['ElectTime'] = request.elect_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ElectZookeeperLeader',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ElectZookeeperLeaderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def elect_zookeeper_leader(
        self,
        request: main_models.ElectZookeeperLeaderRequest,
    ) -> main_models.ElectZookeeperLeaderResponse:
        runtime = RuntimeOptions()
        return self.elect_zookeeper_leader_with_options(request, runtime)

    async def elect_zookeeper_leader_async(
        self,
        request: main_models.ElectZookeeperLeaderRequest,
    ) -> main_models.ElectZookeeperLeaderResponse:
        runtime = RuntimeOptions()
        return await self.elect_zookeeper_leader_with_options_async(request, runtime)

    def kill_process_with_options(
        self,
        request: main_models.KillProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KillProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KillProcess',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_process_with_options_async(
        self,
        request: main_models.KillProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.KillProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'KillProcess',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.KillProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_process(
        self,
        request: main_models.KillProcessRequest,
    ) -> main_models.KillProcessResponse:
        runtime = RuntimeOptions()
        return self.kill_process_with_options(request, runtime)

    async def kill_process_async(
        self,
        request: main_models.KillProcessRequest,
    ) -> main_models.KillProcessResponse:
        runtime = RuntimeOptions()
        return await self.kill_process_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-11-11',
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
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-11-11',
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

    def modify_account_authority_with_options(
        self,
        request: main_models.ModifyAccountAuthorityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountAuthorityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.allow_databases):
            query['AllowDatabases'] = request.allow_databases
        if not DaraCore.is_null(request.allow_dictionaries):
            query['AllowDictionaries'] = request.allow_dictionaries
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.ddl_authority):
            query['DdlAuthority'] = request.ddl_authority
        if not DaraCore.is_null(request.dml_authority):
            query['DmlAuthority'] = request.dml_authority
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.total_databases):
            query['TotalDatabases'] = request.total_databases
        if not DaraCore.is_null(request.total_dictionaries):
            query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountAuthority',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_authority_with_options_async(
        self,
        request: main_models.ModifyAccountAuthorityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountAuthorityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.allow_databases):
            query['AllowDatabases'] = request.allow_databases
        if not DaraCore.is_null(request.allow_dictionaries):
            query['AllowDictionaries'] = request.allow_dictionaries
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.ddl_authority):
            query['DdlAuthority'] = request.ddl_authority
        if not DaraCore.is_null(request.dml_authority):
            query['DmlAuthority'] = request.dml_authority
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.total_databases):
            query['TotalDatabases'] = request.total_databases
        if not DaraCore.is_null(request.total_dictionaries):
            query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountAuthority',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_authority(
        self,
        request: main_models.ModifyAccountAuthorityRequest,
    ) -> main_models.ModifyAccountAuthorityResponse:
        runtime = RuntimeOptions()
        return self.modify_account_authority_with_options(request, runtime)

    async def modify_account_authority_async(
        self,
        request: main_models.ModifyAccountAuthorityRequest,
    ) -> main_models.ModifyAccountAuthorityResponse:
        runtime = RuntimeOptions()
        return await self.modify_account_authority_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: main_models.ModifyAccountDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountDescription',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: main_models.ModifyAccountDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountDescription',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: main_models.ModifyAccountDescriptionRequest,
    ) -> main_models.ModifyAccountDescriptionResponse:
        runtime = RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: main_models.ModifyAccountDescriptionRequest,
    ) -> main_models.ModifyAccountDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_active_operation_maintain_conf_with_options(
        self,
        request: main_models.ModifyActiveOperationMaintainConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyActiveOperationMaintainConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cycle_time):
            query['CycleTime'] = request.cycle_time
        if not DaraCore.is_null(request.cycle_type):
            query['CycleType'] = request.cycle_type
        if not DaraCore.is_null(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not DaraCore.is_null(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationMaintainConf',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyActiveOperationMaintainConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_active_operation_maintain_conf_with_options_async(
        self,
        request: main_models.ModifyActiveOperationMaintainConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyActiveOperationMaintainConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cycle_time):
            query['CycleTime'] = request.cycle_time
        if not DaraCore.is_null(request.cycle_type):
            query['CycleType'] = request.cycle_type
        if not DaraCore.is_null(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not DaraCore.is_null(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationMaintainConf',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyActiveOperationMaintainConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_active_operation_maintain_conf(
        self,
        request: main_models.ModifyActiveOperationMaintainConfRequest,
    ) -> main_models.ModifyActiveOperationMaintainConfResponse:
        runtime = RuntimeOptions()
        return self.modify_active_operation_maintain_conf_with_options(request, runtime)

    async def modify_active_operation_maintain_conf_async(
        self,
        request: main_models.ModifyActiveOperationMaintainConfRequest,
    ) -> main_models.ModifyActiveOperationMaintainConfResponse:
        runtime = RuntimeOptions()
        return await self.modify_active_operation_maintain_conf_with_options_async(request, runtime)

    def modify_active_operation_tasks_with_options(
        self,
        request: main_models.ModifyActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyActiveOperationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.immediate_start):
            query['ImmediateStart'] = request.immediate_start
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationTasks',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyActiveOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_active_operation_tasks_with_options_async(
        self,
        request: main_models.ModifyActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyActiveOperationTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.immediate_start):
            query['ImmediateStart'] = request.immediate_start
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationTasks',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyActiveOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_active_operation_tasks(
        self,
        request: main_models.ModifyActiveOperationTasksRequest,
    ) -> main_models.ModifyActiveOperationTasksResponse:
        runtime = RuntimeOptions()
        return self.modify_active_operation_tasks_with_options(request, runtime)

    async def modify_active_operation_tasks_async(
        self,
        request: main_models.ModifyActiveOperationTasksRequest,
    ) -> main_models.ModifyActiveOperationTasksResponse:
        runtime = RuntimeOptions()
        return await self.modify_active_operation_tasks_with_options_async(request, runtime)

    def modify_auto_renew_attribute_with_options(
        self,
        request: main_models.ModifyAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAutoRenewAttribute',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoRenewAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_auto_renew_attribute_with_options_async(
        self,
        request: main_models.ModifyAutoRenewAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAutoRenewAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.renewal_status):
            query['RenewalStatus'] = request.renewal_status
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAutoRenewAttribute',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAutoRenewAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_auto_renew_attribute(
        self,
        request: main_models.ModifyAutoRenewAttributeRequest,
    ) -> main_models.ModifyAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_auto_renew_attribute_with_options(request, runtime)

    async def modify_auto_renew_attribute_async(
        self,
        request: main_models.ModifyAutoRenewAttributeRequest,
    ) -> main_models.ModifyAutoRenewAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_auto_renew_attribute_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: main_models.ModifyBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not DaraCore.is_null(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPolicy',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: main_models.ModifyBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not DaraCore.is_null(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPolicy',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: main_models.ModifyBackupPolicyRequest,
    ) -> main_models.ModifyBackupPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: main_models.ModifyBackupPolicyRequest,
    ) -> main_models.ModifyBackupPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_dbcluster_with_options(
        self,
        request: main_models.ModifyDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not DaraCore.is_null(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not DaraCore.is_null(request.db_node_storage_type):
            query['DbNodeStorageType'] = request.db_node_storage_type
        if not DaraCore.is_null(request.disable_write_windows):
            query['DisableWriteWindows'] = request.disable_write_windows
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBCluster',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_with_options_async(
        self,
        request: main_models.ModifyDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbnode_group_count):
            query['DBNodeGroupCount'] = request.dbnode_group_count
        if not DaraCore.is_null(request.dbnode_storage):
            query['DBNodeStorage'] = request.dbnode_storage
        if not DaraCore.is_null(request.db_node_storage_type):
            query['DbNodeStorageType'] = request.db_node_storage_type
        if not DaraCore.is_null(request.disable_write_windows):
            query['DisableWriteWindows'] = request.disable_write_windows
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBCluster',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster(
        self,
        request: main_models.ModifyDBClusterRequest,
    ) -> main_models.ModifyDBClusterResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_with_options(request, runtime)

    async def modify_dbcluster_async(
        self,
        request: main_models.ModifyDBClusterRequest,
    ) -> main_models.ModifyDBClusterResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_with_options_async(request, runtime)

    def modify_dbcluster_access_white_list_with_options(
        self,
        request: main_models.ModifyDBClusterAccessWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterAccessWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_iparray_attribute):
            query['DBClusterIPArrayAttribute'] = request.dbcluster_iparray_attribute
        if not DaraCore.is_null(request.dbcluster_iparray_name):
            query['DBClusterIPArrayName'] = request.dbcluster_iparray_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterAccessWhiteList',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_access_white_list_with_options_async(
        self,
        request: main_models.ModifyDBClusterAccessWhiteListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterAccessWhiteListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_iparray_attribute):
            query['DBClusterIPArrayAttribute'] = request.dbcluster_iparray_attribute
        if not DaraCore.is_null(request.dbcluster_iparray_name):
            query['DBClusterIPArrayName'] = request.dbcluster_iparray_name
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterAccessWhiteList',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_access_white_list(
        self,
        request: main_models.ModifyDBClusterAccessWhiteListRequest,
    ) -> main_models.ModifyDBClusterAccessWhiteListResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_access_white_list_with_options(request, runtime)

    async def modify_dbcluster_access_white_list_async(
        self,
        request: main_models.ModifyDBClusterAccessWhiteListRequest,
    ) -> main_models.ModifyDBClusterAccessWhiteListResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_access_white_list_with_options_async(request, runtime)

    def modify_dbcluster_config_with_options(
        self,
        request: main_models.ModifyDBClusterConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_config):
            query['UserConfig'] = request.user_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterConfig',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_config_with_options_async(
        self,
        request: main_models.ModifyDBClusterConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.user_config):
            query['UserConfig'] = request.user_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterConfig',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_config(
        self,
        request: main_models.ModifyDBClusterConfigRequest,
    ) -> main_models.ModifyDBClusterConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_config_with_options(request, runtime)

    async def modify_dbcluster_config_async(
        self,
        request: main_models.ModifyDBClusterConfigRequest,
    ) -> main_models.ModifyDBClusterConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_config_with_options_async(request, runtime)

    def modify_dbcluster_config_in_xmlwith_options(
        self,
        request: main_models.ModifyDBClusterConfigInXMLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterConfigInXMLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterConfigInXML',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterConfigInXMLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_config_in_xmlwith_options_async(
        self,
        request: main_models.ModifyDBClusterConfigInXMLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterConfigInXMLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterConfigInXML',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterConfigInXMLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_config_in_xml(
        self,
        request: main_models.ModifyDBClusterConfigInXMLRequest,
    ) -> main_models.ModifyDBClusterConfigInXMLResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_config_in_xmlwith_options(request, runtime)

    async def modify_dbcluster_config_in_xml_async(
        self,
        request: main_models.ModifyDBClusterConfigInXMLRequest,
    ) -> main_models.ModifyDBClusterConfigInXMLResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_config_in_xmlwith_options_async(request, runtime)

    def modify_dbcluster_description_with_options(
        self,
        request: main_models.ModifyDBClusterDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterDescription',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_description_with_options_async(
        self,
        request: main_models.ModifyDBClusterDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterDescription',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_description(
        self,
        request: main_models.ModifyDBClusterDescriptionRequest,
    ) -> main_models.ModifyDBClusterDescriptionResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_description_with_options(request, runtime)

    async def modify_dbcluster_description_async(
        self,
        request: main_models.ModifyDBClusterDescriptionRequest,
    ) -> main_models.ModifyDBClusterDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_description_with_options_async(request, runtime)

    def modify_dbcluster_maintain_time_with_options(
        self,
        request: main_models.ModifyDBClusterMaintainTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterMaintainTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterMaintainTime',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_maintain_time_with_options_async(
        self,
        request: main_models.ModifyDBClusterMaintainTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterMaintainTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterMaintainTime',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBClusterMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_maintain_time(
        self,
        request: main_models.ModifyDBClusterMaintainTimeRequest,
    ) -> main_models.ModifyDBClusterMaintainTimeResponse:
        runtime = RuntimeOptions()
        return self.modify_dbcluster_maintain_time_with_options(request, runtime)

    async def modify_dbcluster_maintain_time_async(
        self,
        request: main_models.ModifyDBClusterMaintainTimeRequest,
    ) -> main_models.ModifyDBClusterMaintainTimeResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbcluster_maintain_time_with_options_async(request, runtime)

    def modify_dbconfig_with_options(
        self,
        request: main_models.ModifyDBConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBConfig',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbconfig_with_options_async(
        self,
        request: main_models.ModifyDBConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBConfig',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbconfig(
        self,
        request: main_models.ModifyDBConfigRequest,
    ) -> main_models.ModifyDBConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_dbconfig_with_options(request, runtime)

    async def modify_dbconfig_async(
        self,
        request: main_models.ModifyDBConfigRequest,
    ) -> main_models.ModifyDBConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbconfig_with_options_async(request, runtime)

    def modify_minor_version_greade_type_with_options(
        self,
        request: main_models.ModifyMinorVersionGreadeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMinorVersionGreadeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.maintain_auto_type):
            query['MaintainAutoType'] = request.maintain_auto_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMinorVersionGreadeType',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMinorVersionGreadeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_minor_version_greade_type_with_options_async(
        self,
        request: main_models.ModifyMinorVersionGreadeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMinorVersionGreadeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.maintain_auto_type):
            query['MaintainAutoType'] = request.maintain_auto_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMinorVersionGreadeType',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMinorVersionGreadeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_minor_version_greade_type(
        self,
        request: main_models.ModifyMinorVersionGreadeTypeRequest,
    ) -> main_models.ModifyMinorVersionGreadeTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_minor_version_greade_type_with_options(request, runtime)

    async def modify_minor_version_greade_type_async(
        self,
        request: main_models.ModifyMinorVersionGreadeTypeRequest,
    ) -> main_models.ModifyMinorVersionGreadeTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_minor_version_greade_type_with_options_async(request, runtime)

    def modify_rdsto_clickhouse_db_with_options(
        self,
        request: main_models.ModifyRDSToClickhouseDbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRDSToClickhouseDbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ck_password):
            query['CkPassword'] = request.ck_password
        if not DaraCore.is_null(request.ck_user_name):
            query['CkUserName'] = request.ck_user_name
        if not DaraCore.is_null(request.clickhouse_port):
            query['ClickhousePort'] = request.clickhouse_port
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.limit_upper):
            query['LimitUpper'] = request.limit_upper
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rds_id):
            query['RdsId'] = request.rds_id
        if not DaraCore.is_null(request.rds_password):
            query['RdsPassword'] = request.rds_password
        if not DaraCore.is_null(request.rds_port):
            query['RdsPort'] = request.rds_port
        if not DaraCore.is_null(request.rds_syn_db):
            query['RdsSynDb'] = request.rds_syn_db
        if not DaraCore.is_null(request.rds_syn_tables):
            query['RdsSynTables'] = request.rds_syn_tables
        if not DaraCore.is_null(request.rds_user_name):
            query['RdsUserName'] = request.rds_user_name
        if not DaraCore.is_null(request.rds_vpc_id):
            query['RdsVpcId'] = request.rds_vpc_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.skip_unsupported):
            query['SkipUnsupported'] = request.skip_unsupported
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRDSToClickhouseDb',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRDSToClickhouseDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rdsto_clickhouse_db_with_options_async(
        self,
        request: main_models.ModifyRDSToClickhouseDbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyRDSToClickhouseDbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ck_password):
            query['CkPassword'] = request.ck_password
        if not DaraCore.is_null(request.ck_user_name):
            query['CkUserName'] = request.ck_user_name
        if not DaraCore.is_null(request.clickhouse_port):
            query['ClickhousePort'] = request.clickhouse_port
        if not DaraCore.is_null(request.db_cluster_id):
            query['DbClusterId'] = request.db_cluster_id
        if not DaraCore.is_null(request.limit_upper):
            query['LimitUpper'] = request.limit_upper
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.rds_id):
            query['RdsId'] = request.rds_id
        if not DaraCore.is_null(request.rds_password):
            query['RdsPassword'] = request.rds_password
        if not DaraCore.is_null(request.rds_port):
            query['RdsPort'] = request.rds_port
        if not DaraCore.is_null(request.rds_syn_db):
            query['RdsSynDb'] = request.rds_syn_db
        if not DaraCore.is_null(request.rds_syn_tables):
            query['RdsSynTables'] = request.rds_syn_tables
        if not DaraCore.is_null(request.rds_user_name):
            query['RdsUserName'] = request.rds_user_name
        if not DaraCore.is_null(request.rds_vpc_id):
            query['RdsVpcId'] = request.rds_vpc_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.skip_unsupported):
            query['SkipUnsupported'] = request.skip_unsupported
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyRDSToClickhouseDb',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyRDSToClickhouseDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rdsto_clickhouse_db(
        self,
        request: main_models.ModifyRDSToClickhouseDbRequest,
    ) -> main_models.ModifyRDSToClickhouseDbResponse:
        runtime = RuntimeOptions()
        return self.modify_rdsto_clickhouse_db_with_options(request, runtime)

    async def modify_rdsto_clickhouse_db_async(
        self,
        request: main_models.ModifyRDSToClickhouseDbRequest,
    ) -> main_models.ModifyRDSToClickhouseDbResponse:
        runtime = RuntimeOptions()
        return await self.modify_rdsto_clickhouse_db_with_options_async(request, runtime)

    def release_cluster_public_connection_with_options(
        self,
        request: main_models.ReleaseClusterPublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseClusterPublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseClusterPublicConnection',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cluster_public_connection_with_options_async(
        self,
        request: main_models.ReleaseClusterPublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseClusterPublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseClusterPublicConnection',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_cluster_public_connection(
        self,
        request: main_models.ReleaseClusterPublicConnectionRequest,
    ) -> main_models.ReleaseClusterPublicConnectionResponse:
        runtime = RuntimeOptions()
        return self.release_cluster_public_connection_with_options(request, runtime)

    async def release_cluster_public_connection_async(
        self,
        request: main_models.ReleaseClusterPublicConnectionRequest,
    ) -> main_models.ReleaseClusterPublicConnectionResponse:
        runtime = RuntimeOptions()
        return await self.release_cluster_public_connection_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: main_models.ResetAccountPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAccountPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPassword',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: main_models.ResetAccountPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAccountPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPassword',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: main_models.ResetAccountPasswordRequest,
    ) -> main_models.ResetAccountPasswordResponse:
        runtime = RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: main_models.ResetAccountPasswordRequest,
    ) -> main_models.ResetAccountPasswordResponse:
        runtime = RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_instance_with_options(
        self,
        request: main_models.RestartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restart_time):
            query['RestartTime'] = request.restart_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartInstance',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: main_models.RestartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restart_time):
            query['RestartTime'] = request.restart_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartInstance',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        request: main_models.RestartInstanceRequest,
    ) -> main_models.RestartInstanceResponse:
        runtime = RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    async def restart_instance_async(
        self,
        request: main_models.RestartInstanceRequest,
    ) -> main_models.RestartInstanceResponse:
        runtime = RuntimeOptions()
        return await self.restart_instance_with_options_async(request, runtime)

    def restart_instance_node_list_with_options(
        self,
        tmp_req: main_models.RestartInstanceNodeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstanceNodeListResponse:
        tmp_req.validate()
        request = main_models.RestartInstanceNodeListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_list):
            request.node_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_list, 'NodeList', 'json')
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.node_list_shrink):
            query['NodeList'] = request.node_list_shrink
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restart_time):
            query['RestartTime'] = request.restart_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartInstanceNodeList',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstanceNodeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_node_list_with_options_async(
        self,
        tmp_req: main_models.RestartInstanceNodeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstanceNodeListResponse:
        tmp_req.validate()
        request = main_models.RestartInstanceNodeListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_list):
            request.node_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_list, 'NodeList', 'json')
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.node_list_shrink):
            query['NodeList'] = request.node_list_shrink
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restart_time):
            query['RestartTime'] = request.restart_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartInstanceNodeList',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstanceNodeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance_node_list(
        self,
        request: main_models.RestartInstanceNodeListRequest,
    ) -> main_models.RestartInstanceNodeListResponse:
        runtime = RuntimeOptions()
        return self.restart_instance_node_list_with_options(request, runtime)

    async def restart_instance_node_list_async(
        self,
        request: main_models.RestartInstanceNodeListRequest,
    ) -> main_models.RestartInstanceNodeListResponse:
        runtime = RuntimeOptions()
        return await self.restart_instance_node_list_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-11-11',
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
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-11-11',
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

    def transfer_version_with_options(
        self,
        request: main_models.TransferVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.disable_write_windows):
            query['DisableWriteWindows'] = request.disable_write_windows
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_account):
            query['SourceAccount'] = request.source_account
        if not DaraCore.is_null(request.source_cluster_name):
            query['SourceClusterName'] = request.source_cluster_name
        if not DaraCore.is_null(request.source_password):
            query['SourcePassword'] = request.source_password
        if not DaraCore.is_null(request.source_shards):
            query['SourceShards'] = request.source_shards
        if not DaraCore.is_null(request.target_account):
            query['TargetAccount'] = request.target_account
        if not DaraCore.is_null(request.target_db_cluster_id):
            query['TargetDbClusterId'] = request.target_db_cluster_id
        if not DaraCore.is_null(request.target_password):
            query['TargetPassword'] = request.target_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferVersion',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_version_with_options_async(
        self,
        request: main_models.TransferVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.disable_write_windows):
            query['DisableWriteWindows'] = request.disable_write_windows
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.source_account):
            query['SourceAccount'] = request.source_account
        if not DaraCore.is_null(request.source_cluster_name):
            query['SourceClusterName'] = request.source_cluster_name
        if not DaraCore.is_null(request.source_password):
            query['SourcePassword'] = request.source_password
        if not DaraCore.is_null(request.source_shards):
            query['SourceShards'] = request.source_shards
        if not DaraCore.is_null(request.target_account):
            query['TargetAccount'] = request.target_account
        if not DaraCore.is_null(request.target_db_cluster_id):
            query['TargetDbClusterId'] = request.target_db_cluster_id
        if not DaraCore.is_null(request.target_password):
            query['TargetPassword'] = request.target_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransferVersion',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_version(
        self,
        request: main_models.TransferVersionRequest,
    ) -> main_models.TransferVersionResponse:
        runtime = RuntimeOptions()
        return self.transfer_version_with_options(request, runtime)

    async def transfer_version_async(
        self,
        request: main_models.TransferVersionRequest,
    ) -> main_models.TransferVersionResponse:
        runtime = RuntimeOptions()
        return await self.transfer_version_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-11-11',
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
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-11-11',
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

    def upgrade_minor_version_with_options(
        self,
        request: main_models.UpgradeMinorVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeMinorVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.upgrade_immediately):
            query['UpgradeImmediately'] = request.upgrade_immediately
        if not DaraCore.is_null(request.upgrade_time):
            query['UpgradeTime'] = request.upgrade_time
        if not DaraCore.is_null(request.upgrade_version):
            query['UpgradeVersion'] = request.upgrade_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeMinorVersion',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeMinorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_minor_version_with_options_async(
        self,
        request: main_models.UpgradeMinorVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeMinorVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.upgrade_immediately):
            query['UpgradeImmediately'] = request.upgrade_immediately
        if not DaraCore.is_null(request.upgrade_time):
            query['UpgradeTime'] = request.upgrade_time
        if not DaraCore.is_null(request.upgrade_version):
            query['UpgradeVersion'] = request.upgrade_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeMinorVersion',
            version = '2019-11-11',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeMinorVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_minor_version(
        self,
        request: main_models.UpgradeMinorVersionRequest,
    ) -> main_models.UpgradeMinorVersionResponse:
        runtime = RuntimeOptions()
        return self.upgrade_minor_version_with_options(request, runtime)

    async def upgrade_minor_version_async(
        self,
        request: main_models.UpgradeMinorVersionRequest,
    ) -> main_models.UpgradeMinorVersionResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_minor_version_with_options_async(request, runtime)
