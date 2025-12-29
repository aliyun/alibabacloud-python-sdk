# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dds20151201 import models as main_models
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
            'cn-qingdao': 'mongodb.aliyuncs.com',
            'cn-beijing': 'mongodb.aliyuncs.com',
            'cn-zhangjiakou': 'mongodb.cn-zhangjiakou.aliyuncs.com',
            'cn-huhehaote': 'mongodb.cn-huhehaote.aliyuncs.com',
            'cn-wulanchabu': 'mongodb.aliyuncs.com',
            'cn-hangzhou': 'mongodb.aliyuncs.com',
            'cn-shanghai': 'mongodb.aliyuncs.com',
            'cn-shenzhen': 'mongodb.cn-shenzhen.aliyuncs.com',
            'cn-heyuan': 'mongodb.aliyuncs.com',
            'cn-guangzhou': 'mongodb.cn-guangzhou.aliyuncs.com',
            'cn-chengdu': 'mongodb.cn-chengdu.aliyuncs.com',
            'cn-hongkong': 'mongodb.cn-hongkong.aliyuncs.com',
            'ap-northeast-1': 'mongodb.ap-northeast-1.aliyuncs.com',
            'ap-southeast-1': 'mongodb.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'mongodb.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'mongodb.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'mongodb.ap-southeast-5.aliyuncs.com',
            'us-east-1': 'mongodb.us-east-1.aliyuncs.com',
            'us-west-1': 'mongodb.us-west-1.aliyuncs.com',
            'eu-west-1': 'mongodb.eu-west-1.aliyuncs.com',
            'eu-central-1': 'mongodb.eu-central-1.aliyuncs.com',
            'ap-south-1': 'mongodb.ap-south-1.aliyuncs.com',
            'me-east-1': 'mongodb.me-east-1.aliyuncs.com',
            'cn-hangzhou-finance': 'mongodb.aliyuncs.com',
            'cn-shanghai-finance-1': 'mongodb.cn-shanghai-finance-1.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mongodb.cn-shenzhen-finance-1.aliyuncs.com',
            'cn-north-2-gov-1': 'mongodb.cn-north-2-gov-1.aliyuncs.com',
            'ap-northeast-2-pop': 'mongodb.aliyuncs.com',
            'cn-beijing-finance-1': 'mongodb.aliyuncs.com',
            'cn-beijing-finance-pop': 'mongodb.aliyuncs.com',
            'cn-beijing-gov-1': 'mongodb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mongodb.aliyuncs.com',
            'cn-edge-1': 'mongodb.aliyuncs.com',
            'cn-fujian': 'mongodb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mongodb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mongodb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mongodb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mongodb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mongodb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mongodb.aliyuncs.com',
            'cn-hangzhou-test-306': 'mongodb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mongodb.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'mongodb.aliyuncs.com',
            'cn-qingdao-nebula': 'mongodb.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mongodb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mongodb.aliyuncs.com',
            'cn-shanghai-inner': 'mongodb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mongodb.aliyuncs.com',
            'cn-shenzhen-inner': 'mongodb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mongodb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mongodb.aliyuncs.com',
            'cn-wuhan': 'mongodb.aliyuncs.com',
            'cn-yushanfang': 'mongodb.aliyuncs.com',
            'cn-zhangbei': 'mongodb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mongodb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mongodb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mongodb.aliyuncs.com',
            'eu-west-1-oxs': 'mongodb.aliyuncs.com',
            'rus-west-1-pop': 'mongodb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dds', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allocate_dbinstance_srv_network_address_with_options(
        self,
        request: main_models.AllocateDBInstanceSrvNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateDBInstanceSrvNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.srv_connection_type):
            query['SrvConnectionType'] = request.srv_connection_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateDBInstanceSrvNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateDBInstanceSrvNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_dbinstance_srv_network_address_with_options_async(
        self,
        request: main_models.AllocateDBInstanceSrvNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateDBInstanceSrvNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.srv_connection_type):
            query['SrvConnectionType'] = request.srv_connection_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateDBInstanceSrvNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateDBInstanceSrvNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_dbinstance_srv_network_address(
        self,
        request: main_models.AllocateDBInstanceSrvNetworkAddressRequest,
    ) -> main_models.AllocateDBInstanceSrvNetworkAddressResponse:
        runtime = RuntimeOptions()
        return self.allocate_dbinstance_srv_network_address_with_options(request, runtime)

    async def allocate_dbinstance_srv_network_address_async(
        self,
        request: main_models.AllocateDBInstanceSrvNetworkAddressRequest,
    ) -> main_models.AllocateDBInstanceSrvNetworkAddressResponse:
        runtime = RuntimeOptions()
        return await self.allocate_dbinstance_srv_network_address_with_options_async(request, runtime)

    def allocate_node_private_network_address_with_options(
        self,
        request: main_models.AllocateNodePrivateNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateNodePrivateNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateNodePrivateNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateNodePrivateNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_node_private_network_address_with_options_async(
        self,
        request: main_models.AllocateNodePrivateNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateNodePrivateNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateNodePrivateNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateNodePrivateNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_node_private_network_address(
        self,
        request: main_models.AllocateNodePrivateNetworkAddressRequest,
    ) -> main_models.AllocateNodePrivateNetworkAddressResponse:
        runtime = RuntimeOptions()
        return self.allocate_node_private_network_address_with_options(request, runtime)

    async def allocate_node_private_network_address_async(
        self,
        request: main_models.AllocateNodePrivateNetworkAddressRequest,
    ) -> main_models.AllocateNodePrivateNetworkAddressResponse:
        runtime = RuntimeOptions()
        return await self.allocate_node_private_network_address_with_options_async(request, runtime)

    def allocate_public_network_address_with_options(
        self,
        request: main_models.AllocatePublicNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocatePublicNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'AllocatePublicNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocatePublicNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_public_network_address_with_options_async(
        self,
        request: main_models.AllocatePublicNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocatePublicNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'AllocatePublicNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocatePublicNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_public_network_address(
        self,
        request: main_models.AllocatePublicNetworkAddressRequest,
    ) -> main_models.AllocatePublicNetworkAddressResponse:
        runtime = RuntimeOptions()
        return self.allocate_public_network_address_with_options(request, runtime)

    async def allocate_public_network_address_async(
        self,
        request: main_models.AllocatePublicNetworkAddressRequest,
    ) -> main_models.AllocatePublicNetworkAddressResponse:
        runtime = RuntimeOptions()
        return await self.allocate_public_network_address_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelActiveOperationTasks',
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelActiveOperationTasks',
            version = '2015-12-01',
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

    def check_cloud_resource_authorized_with_options(
        self,
        request: main_models.CheckCloudResourceAuthorizedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCloudResourceAuthorizedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCloudResourceAuthorized',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCloudResourceAuthorizedResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_cloud_resource_authorized_with_options_async(
        self,
        request: main_models.CheckCloudResourceAuthorizedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCloudResourceAuthorizedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCloudResourceAuthorized',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCloudResourceAuthorizedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_cloud_resource_authorized(
        self,
        request: main_models.CheckCloudResourceAuthorizedRequest,
    ) -> main_models.CheckCloudResourceAuthorizedResponse:
        runtime = RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    async def check_cloud_resource_authorized_async(
        self,
        request: main_models.CheckCloudResourceAuthorizedRequest,
    ) -> main_models.CheckCloudResourceAuthorizedResponse:
        runtime = RuntimeOptions()
        return await self.check_cloud_resource_authorized_with_options_async(request, runtime)

    def check_recovery_condition_with_options(
        self,
        request: main_models.CheckRecoveryConditionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckRecoveryConditionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.database_names):
            query['DatabaseNames'] = request.database_names
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not DaraCore.is_null(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        if not DaraCore.is_null(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckRecoveryCondition',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckRecoveryConditionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_recovery_condition_with_options_async(
        self,
        request: main_models.CheckRecoveryConditionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckRecoveryConditionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.database_names):
            query['DatabaseNames'] = request.database_names
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not DaraCore.is_null(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        if not DaraCore.is_null(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckRecoveryCondition',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckRecoveryConditionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_recovery_condition(
        self,
        request: main_models.CheckRecoveryConditionRequest,
    ) -> main_models.CheckRecoveryConditionResponse:
        runtime = RuntimeOptions()
        return self.check_recovery_condition_with_options(request, runtime)

    async def check_recovery_condition_async(
        self,
        request: main_models.CheckRecoveryConditionRequest,
    ) -> main_models.CheckRecoveryConditionResponse:
        runtime = RuntimeOptions()
        return await self.check_recovery_condition_with_options_async(request, runtime)

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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRole',
            version = '2015-12-01',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRole',
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            version = '2015-12-01',
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

    def create_backup_with_options(
        self,
        request: main_models.CreateBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'CreateBackup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: main_models.CreateBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'CreateBackup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup(
        self,
        request: main_models.CreateBackupRequest,
    ) -> main_models.CreateBackupResponse:
        runtime = RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: main_models.CreateBackupRequest,
    ) -> main_models.CreateBackupResponse:
        runtime = RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: main_models.CreateDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not DaraCore.is_null(request.database_names):
            query['DatabaseNames'] = request.database_names
        if not DaraCore.is_null(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.global_security_group_ids):
            query['GlobalSecurityGroupIds'] = request.global_security_group_ids
        if not DaraCore.is_null(request.hidden_zone_id):
            query['HiddenZoneId'] = request.hidden_zone_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not DaraCore.is_null(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not DaraCore.is_null(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        if not DaraCore.is_null(request.storage_engine):
            query['StorageEngine'] = request.storage_engine
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
            action = 'CreateDBInstance',
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not DaraCore.is_null(request.database_names):
            query['DatabaseNames'] = request.database_names
        if not DaraCore.is_null(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.global_security_group_ids):
            query['GlobalSecurityGroupIds'] = request.global_security_group_ids
        if not DaraCore.is_null(request.hidden_zone_id):
            query['HiddenZoneId'] = request.hidden_zone_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not DaraCore.is_null(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not DaraCore.is_null(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        if not DaraCore.is_null(request.storage_engine):
            query['StorageEngine'] = request.storage_engine
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
            action = 'CreateDBInstance',
            version = '2015-12-01',
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

    def create_global_security_ipgroup_with_options(
        self,
        request: main_models.CreateGlobalSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGlobalSecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gip_list):
            query['GIpList'] = request.gip_list
        if not DaraCore.is_null(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGlobalSecurityIPGroup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_global_security_ipgroup_with_options_async(
        self,
        request: main_models.CreateGlobalSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGlobalSecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gip_list):
            query['GIpList'] = request.gip_list
        if not DaraCore.is_null(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGlobalSecurityIPGroup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_global_security_ipgroup(
        self,
        request: main_models.CreateGlobalSecurityIPGroupRequest,
    ) -> main_models.CreateGlobalSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return self.create_global_security_ipgroup_with_options(request, runtime)

    async def create_global_security_ipgroup_async(
        self,
        request: main_models.CreateGlobalSecurityIPGroupRequest,
    ) -> main_models.CreateGlobalSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_global_security_ipgroup_with_options_async(request, runtime)

    def create_node_with_options(
        self,
        request: main_models.CreateNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_class):
            query['NodeClass'] = request.node_class
        if not DaraCore.is_null(request.node_storage):
            query['NodeStorage'] = request.node_storage
        if not DaraCore.is_null(request.node_type):
            query['NodeType'] = request.node_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.shard_direct):
            query['ShardDirect'] = request.shard_direct
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNode',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_with_options_async(
        self,
        request: main_models.CreateNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_class):
            query['NodeClass'] = request.node_class
        if not DaraCore.is_null(request.node_storage):
            query['NodeStorage'] = request.node_storage
        if not DaraCore.is_null(request.node_type):
            query['NodeType'] = request.node_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.shard_direct):
            query['ShardDirect'] = request.shard_direct
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNode',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node(
        self,
        request: main_models.CreateNodeRequest,
    ) -> main_models.CreateNodeResponse:
        runtime = RuntimeOptions()
        return self.create_node_with_options(request, runtime)

    async def create_node_async(
        self,
        request: main_models.CreateNodeRequest,
    ) -> main_models.CreateNodeResponse:
        runtime = RuntimeOptions()
        return await self.create_node_with_options_async(request, runtime)

    def create_node_batch_with_options(
        self,
        request: main_models.CreateNodeBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.from_app):
            query['FromApp'] = request.from_app
        if not DaraCore.is_null(request.nodes_info):
            query['NodesInfo'] = request.nodes_info
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.shard_direct):
            query['ShardDirect'] = request.shard_direct
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNodeBatch',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodeBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_batch_with_options_async(
        self,
        request: main_models.CreateNodeBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.from_app):
            query['FromApp'] = request.from_app
        if not DaraCore.is_null(request.nodes_info):
            query['NodesInfo'] = request.nodes_info
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.shard_direct):
            query['ShardDirect'] = request.shard_direct
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNodeBatch',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodeBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node_batch(
        self,
        request: main_models.CreateNodeBatchRequest,
    ) -> main_models.CreateNodeBatchResponse:
        runtime = RuntimeOptions()
        return self.create_node_batch_with_options(request, runtime)

    async def create_node_batch_async(
        self,
        request: main_models.CreateNodeBatchRequest,
    ) -> main_models.CreateNodeBatchResponse:
        runtime = RuntimeOptions()
        return await self.create_node_batch_with_options_async(request, runtime)

    def create_node_role_tag_with_options(
        self,
        request: main_models.CreateNodeRoleTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeRoleTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.shard_list):
            query['ShardList'] = request.shard_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNodeRoleTag',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodeRoleTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_role_tag_with_options_async(
        self,
        request: main_models.CreateNodeRoleTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeRoleTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.shard_list):
            query['ShardList'] = request.shard_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNodeRoleTag',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodeRoleTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node_role_tag(
        self,
        request: main_models.CreateNodeRoleTagRequest,
    ) -> main_models.CreateNodeRoleTagResponse:
        runtime = RuntimeOptions()
        return self.create_node_role_tag_with_options(request, runtime)

    async def create_node_role_tag_async(
        self,
        request: main_models.CreateNodeRoleTagRequest,
    ) -> main_models.CreateNodeRoleTagResponse:
        runtime = RuntimeOptions()
        return await self.create_node_role_tag_with_options_async(request, runtime)

    def create_sharding_dbinstance_with_options(
        self,
        request: main_models.CreateShardingDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateShardingDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_server):
            query['ConfigServer'] = request.config_server
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.global_security_group_ids):
            query['GlobalSecurityGroupIds'] = request.global_security_group_ids
        if not DaraCore.is_null(request.hidden_zone_id):
            query['HiddenZoneId'] = request.hidden_zone_id
        if not DaraCore.is_null(request.mongos):
            query['Mongos'] = request.mongos
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_set):
            query['ReplicaSet'] = request.replica_set
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not DaraCore.is_null(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        if not DaraCore.is_null(request.storage_engine):
            query['StorageEngine'] = request.storage_engine
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
            action = 'CreateShardingDBInstance',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateShardingDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sharding_dbinstance_with_options_async(
        self,
        request: main_models.CreateShardingDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateShardingDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.config_server):
            query['ConfigServer'] = request.config_server
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.encrypted):
            query['Encrypted'] = request.encrypted
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.global_security_group_ids):
            query['GlobalSecurityGroupIds'] = request.global_security_group_ids
        if not DaraCore.is_null(request.hidden_zone_id):
            query['HiddenZoneId'] = request.hidden_zone_id
        if not DaraCore.is_null(request.mongos):
            query['Mongos'] = request.mongos
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not DaraCore.is_null(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replica_set):
            query['ReplicaSet'] = request.replica_set
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not DaraCore.is_null(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.src_dbinstance_id):
            query['SrcDBInstanceId'] = request.src_dbinstance_id
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        if not DaraCore.is_null(request.storage_engine):
            query['StorageEngine'] = request.storage_engine
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
            action = 'CreateShardingDBInstance',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateShardingDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sharding_dbinstance(
        self,
        request: main_models.CreateShardingDBInstanceRequest,
    ) -> main_models.CreateShardingDBInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_sharding_dbinstance_with_options(request, runtime)

    async def create_sharding_dbinstance_async(
        self,
        request: main_models.CreateShardingDBInstanceRequest,
    ) -> main_models.CreateShardingDBInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_sharding_dbinstance_with_options_async(request, runtime)

    def delete_backup_with_options(
        self,
        request: main_models.DeleteBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DeleteBackup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_with_options_async(
        self,
        request: main_models.DeleteBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DeleteBackup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup(
        self,
        request: main_models.DeleteBackupRequest,
    ) -> main_models.DeleteBackupResponse:
        runtime = RuntimeOptions()
        return self.delete_backup_with_options(request, runtime)

    async def delete_backup_async(
        self,
        request: main_models.DeleteBackupRequest,
    ) -> main_models.DeleteBackupResponse:
        runtime = RuntimeOptions()
        return await self.delete_backup_with_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: main_models.DeleteDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DeleteDBInstance',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: main_models.DeleteDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DeleteDBInstance',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbinstance(
        self,
        request: main_models.DeleteDBInstanceRequest,
    ) -> main_models.DeleteDBInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: main_models.DeleteDBInstanceRequest,
    ) -> main_models.DeleteDBInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def delete_global_security_ipgroup_with_options(
        self,
        request: main_models.DeleteGlobalSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGlobalSecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGlobalSecurityIPGroup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_global_security_ipgroup_with_options_async(
        self,
        request: main_models.DeleteGlobalSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGlobalSecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGlobalSecurityIPGroup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_global_security_ipgroup(
        self,
        request: main_models.DeleteGlobalSecurityIPGroupRequest,
    ) -> main_models.DeleteGlobalSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_global_security_ipgroup_with_options(request, runtime)

    async def delete_global_security_ipgroup_async(
        self,
        request: main_models.DeleteGlobalSecurityIPGroupRequest,
    ) -> main_models.DeleteGlobalSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_global_security_ipgroup_with_options_async(request, runtime)

    def delete_node_with_options(
        self,
        request: main_models.DeleteNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'DeleteNode',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_node_with_options_async(
        self,
        request: main_models.DeleteNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'DeleteNode',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_node(
        self,
        request: main_models.DeleteNodeRequest,
    ) -> main_models.DeleteNodeResponse:
        runtime = RuntimeOptions()
        return self.delete_node_with_options(request, runtime)

    async def delete_node_async(
        self,
        request: main_models.DeleteNodeRequest,
    ) -> main_models.DeleteNodeResponse:
        runtime = RuntimeOptions()
        return await self.delete_node_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: main_models.DescribeAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeAccounts',
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeAccounts',
            version = '2015-12-01',
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

    def describe_active_operation_maintenance_config_with_options(
        self,
        request: main_models.DescribeActiveOperationMaintenanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationMaintenanceConfigResponse:
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
            action = 'DescribeActiveOperationMaintenanceConfig',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationMaintenanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_maintenance_config_with_options_async(
        self,
        request: main_models.DescribeActiveOperationMaintenanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationMaintenanceConfigResponse:
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
            action = 'DescribeActiveOperationMaintenanceConfig',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationMaintenanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_maintenance_config(
        self,
        request: main_models.DescribeActiveOperationMaintenanceConfigRequest,
    ) -> main_models.DescribeActiveOperationMaintenanceConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_active_operation_maintenance_config_with_options(request, runtime)

    async def describe_active_operation_maintenance_config_async(
        self,
        request: main_models.DescribeActiveOperationMaintenanceConfigRequest,
    ) -> main_models.DescribeActiveOperationMaintenanceConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_active_operation_maintenance_config_with_options_async(request, runtime)

    def describe_active_operation_task_with_options(
        self,
        request: main_models.DescribeActiveOperationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_history):
            query['IsHistory'] = request.is_history
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
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTask',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_task_with_options_async(
        self,
        request: main_models.DescribeActiveOperationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_history):
            query['IsHistory'] = request.is_history
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
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTask',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_task(
        self,
        request: main_models.DescribeActiveOperationTaskRequest,
    ) -> main_models.DescribeActiveOperationTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_active_operation_task_with_options(request, runtime)

    async def describe_active_operation_task_async(
        self,
        request: main_models.DescribeActiveOperationTaskRequest,
    ) -> main_models.DescribeActiveOperationTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_active_operation_task_with_options_async(request, runtime)

    def describe_active_operation_task_count_with_options(
        self,
        request: main_models.DescribeActiveOperationTaskCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTaskCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTaskCount',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationTaskCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_task_count_with_options_async(
        self,
        request: main_models.DescribeActiveOperationTaskCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTaskCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTaskCount',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationTaskCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_task_count(
        self,
        request: main_models.DescribeActiveOperationTaskCountRequest,
    ) -> main_models.DescribeActiveOperationTaskCountResponse:
        runtime = RuntimeOptions()
        return self.describe_active_operation_task_count_with_options(request, runtime)

    async def describe_active_operation_task_count_async(
        self,
        request: main_models.DescribeActiveOperationTaskCountRequest,
    ) -> main_models.DescribeActiveOperationTaskCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_active_operation_task_count_with_options_async(request, runtime)

    def describe_active_operation_task_region_with_options(
        self,
        request: main_models.DescribeActiveOperationTaskRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTaskRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_history):
            query['IsHistory'] = request.is_history
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTaskRegion',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationTaskRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_task_region_with_options_async(
        self,
        request: main_models.DescribeActiveOperationTaskRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTaskRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_history):
            query['IsHistory'] = request.is_history
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTaskRegion',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationTaskRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_task_region(
        self,
        request: main_models.DescribeActiveOperationTaskRegionRequest,
    ) -> main_models.DescribeActiveOperationTaskRegionResponse:
        runtime = RuntimeOptions()
        return self.describe_active_operation_task_region_with_options(request, runtime)

    async def describe_active_operation_task_region_async(
        self,
        request: main_models.DescribeActiveOperationTaskRegionRequest,
    ) -> main_models.DescribeActiveOperationTaskRegionResponse:
        runtime = RuntimeOptions()
        return await self.describe_active_operation_task_region_with_options_async(request, runtime)

    def describe_active_operation_task_type_with_options(
        self,
        request: main_models.DescribeActiveOperationTaskTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTaskTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_history):
            query['IsHistory'] = request.is_history
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTaskType',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationTaskTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_operation_task_type_with_options_async(
        self,
        request: main_models.DescribeActiveOperationTaskTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTaskTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_history):
            query['IsHistory'] = request.is_history
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTaskType',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveOperationTaskTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_operation_task_type(
        self,
        request: main_models.DescribeActiveOperationTaskTypeRequest,
    ) -> main_models.DescribeActiveOperationTaskTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_active_operation_task_type_with_options(request, runtime)

    async def describe_active_operation_task_type_async(
        self,
        request: main_models.DescribeActiveOperationTaskTypeRequest,
    ) -> main_models.DescribeActiveOperationTaskTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_active_operation_task_type_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTasks',
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTasks',
            version = '2015-12-01',
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

    def describe_audit_log_filter_with_options(
        self,
        request: main_models.DescribeAuditLogFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditLogFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditLogFilter',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditLogFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_log_filter_with_options_async(
        self,
        request: main_models.DescribeAuditLogFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditLogFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditLogFilter',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditLogFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_log_filter(
        self,
        request: main_models.DescribeAuditLogFilterRequest,
    ) -> main_models.DescribeAuditLogFilterResponse:
        runtime = RuntimeOptions()
        return self.describe_audit_log_filter_with_options(request, runtime)

    async def describe_audit_log_filter_async(
        self,
        request: main_models.DescribeAuditLogFilterRequest,
    ) -> main_models.DescribeAuditLogFilterResponse:
        runtime = RuntimeOptions()
        return await self.describe_audit_log_filter_with_options_async(request, runtime)

    def describe_audit_policy_with_options(
        self,
        request: main_models.DescribeAuditPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeAuditPolicy',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_policy_with_options_async(
        self,
        request: main_models.DescribeAuditPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeAuditPolicy',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_policy(
        self,
        request: main_models.DescribeAuditPolicyRequest,
    ) -> main_models.DescribeAuditPolicyResponse:
        runtime = RuntimeOptions()
        return self.describe_audit_policy_with_options(request, runtime)

    async def describe_audit_policy_async(
        self,
        request: main_models.DescribeAuditPolicyRequest,
    ) -> main_models.DescribeAuditPolicyResponse:
        runtime = RuntimeOptions()
        return await self.describe_audit_policy_with_options_async(request, runtime)

    def describe_audit_records_with_options(
        self,
        request: main_models.DescribeAuditRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.form):
            query['Form'] = request.form
        if not DaraCore.is_null(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditRecords',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_records_with_options_async(
        self,
        request: main_models.DescribeAuditRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAuditRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.database):
            query['Database'] = request.database
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.form):
            query['Form'] = request.form
        if not DaraCore.is_null(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.user):
            query['User'] = request.user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAuditRecords',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAuditRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_records(
        self,
        request: main_models.DescribeAuditRecordsRequest,
    ) -> main_models.DescribeAuditRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_audit_records_with_options(request, runtime)

    async def describe_audit_records_async(
        self,
        request: main_models.DescribeAuditRecordsRequest,
    ) -> main_models.DescribeAuditRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_audit_records_with_options_async(request, runtime)

    def describe_availability_zones_with_options(
        self,
        request: main_models.DescribeAvailabilityZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailabilityZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.db_type):
            query['DbType'] = request.db_type
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.exclude_secondary_zone_id):
            query['ExcludeSecondaryZoneId'] = request.exclude_secondary_zone_id
        if not DaraCore.is_null(request.exclude_zone_id):
            query['ExcludeZoneId'] = request.exclude_zone_id
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.mongo_type):
            query['MongoType'] = request.mongo_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.storage_support):
            query['StorageSupport'] = request.storage_support
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailabilityZones',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailabilityZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_availability_zones_with_options_async(
        self,
        request: main_models.DescribeAvailabilityZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailabilityZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.db_type):
            query['DbType'] = request.db_type
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.exclude_secondary_zone_id):
            query['ExcludeSecondaryZoneId'] = request.exclude_secondary_zone_id
        if not DaraCore.is_null(request.exclude_zone_id):
            query['ExcludeZoneId'] = request.exclude_zone_id
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.mongo_type):
            query['MongoType'] = request.mongo_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.storage_support):
            query['StorageSupport'] = request.storage_support
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailabilityZones',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailabilityZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_availability_zones(
        self,
        request: main_models.DescribeAvailabilityZonesRequest,
    ) -> main_models.DescribeAvailabilityZonesResponse:
        runtime = RuntimeOptions()
        return self.describe_availability_zones_with_options(request, runtime)

    async def describe_availability_zones_async(
        self,
        request: main_models.DescribeAvailabilityZonesRequest,
    ) -> main_models.DescribeAvailabilityZonesResponse:
        runtime = RuntimeOptions()
        return await self.describe_availability_zones_with_options_async(request, runtime)

    def describe_available_engine_version_with_options(
        self,
        request: main_models.DescribeAvailableEngineVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableEngineVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeAvailableEngineVersion',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableEngineVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_engine_version_with_options_async(
        self,
        request: main_models.DescribeAvailableEngineVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableEngineVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeAvailableEngineVersion',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableEngineVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_engine_version(
        self,
        request: main_models.DescribeAvailableEngineVersionRequest,
    ) -> main_models.DescribeAvailableEngineVersionResponse:
        runtime = RuntimeOptions()
        return self.describe_available_engine_version_with_options(request, runtime)

    async def describe_available_engine_version_async(
        self,
        request: main_models.DescribeAvailableEngineVersionRequest,
    ) -> main_models.DescribeAvailableEngineVersionResponse:
        runtime = RuntimeOptions()
        return await self.describe_available_engine_version_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: main_models.DescribeAvailableResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.db_type):
            query['DbType'] = request.db_type
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableResource',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: main_models.DescribeAvailableResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.db_type):
            query['DbType'] = request.db_type
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableResource',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_resource(
        self,
        request: main_models.DescribeAvailableResourceRequest,
    ) -> main_models.DescribeAvailableResourceResponse:
        runtime = RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: main_models.DescribeAvailableResourceRequest,
    ) -> main_models.DescribeAvailableResourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_backup_dbs_with_options(
        self,
        request: main_models.DescribeBackupDBsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupDBsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not DaraCore.is_null(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        if not DaraCore.is_null(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupDBs',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupDBsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_dbs_with_options_async(
        self,
        request: main_models.DescribeBackupDBsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupDBsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not DaraCore.is_null(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        if not DaraCore.is_null(request.source_dbinstance):
            query['SourceDBInstance'] = request.source_dbinstance
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupDBs',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupDBsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_dbs(
        self,
        request: main_models.DescribeBackupDBsRequest,
    ) -> main_models.DescribeBackupDBsResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_dbs_with_options(request, runtime)

    async def describe_backup_dbs_async(
        self,
        request: main_models.DescribeBackupDBsRequest,
    ) -> main_models.DescribeBackupDBsResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_dbs_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: main_models.DescribeBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
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
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
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
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2015-12-01',
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

    def describe_backup_storage_with_options(
        self,
        request: main_models.DescribeBackupStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupStorageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'DescribeBackupStorage',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_storage_with_options_async(
        self,
        request: main_models.DescribeBackupStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupStorageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'DescribeBackupStorage',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_storage(
        self,
        request: main_models.DescribeBackupStorageRequest,
    ) -> main_models.DescribeBackupStorageResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_storage_with_options(request, runtime)

    async def describe_backup_storage_async(
        self,
        request: main_models.DescribeBackupStorageRequest,
    ) -> main_models.DescribeBackupStorageResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_storage_with_options_async(request, runtime)

    def describe_backup_tasks_with_options(
        self,
        request: main_models.DescribeBackupTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeBackupTasks',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_tasks_with_options_async(
        self,
        request: main_models.DescribeBackupTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeBackupTasks',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_tasks(
        self,
        request: main_models.DescribeBackupTasksRequest,
    ) -> main_models.DescribeBackupTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    async def describe_backup_tasks_async(
        self,
        request: main_models.DescribeBackupTasksRequest,
    ) -> main_models.DescribeBackupTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_tasks_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: main_models.DescribeBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackups',
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackups',
            version = '2015-12-01',
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

    def describe_cluster_backups_with_options(
        self,
        request: main_models.DescribeClusterBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_only_get_cluster_back_up):
            query['IsOnlyGetClusterBackUp'] = request.is_only_get_cluster_back_up
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterBackups',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_backups_with_options_async(
        self,
        request: main_models.DescribeClusterBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.backup_job_id):
            query['BackupJobId'] = request.backup_job_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_only_get_cluster_back_up):
            query['IsOnlyGetClusterBackUp'] = request.is_only_get_cluster_back_up
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterBackups',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_backups(
        self,
        request: main_models.DescribeClusterBackupsRequest,
    ) -> main_models.DescribeClusterBackupsResponse:
        runtime = RuntimeOptions()
        return self.describe_cluster_backups_with_options(request, runtime)

    async def describe_cluster_backups_async(
        self,
        request: main_models.DescribeClusterBackupsRequest,
    ) -> main_models.DescribeClusterBackupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cluster_backups_with_options_async(request, runtime)

    def describe_cluster_recover_time_with_options(
        self,
        request: main_models.DescribeClusterRecoverTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterRecoverTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterRecoverTime',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterRecoverTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_recover_time_with_options_async(
        self,
        request: main_models.DescribeClusterRecoverTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterRecoverTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterRecoverTime',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterRecoverTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_recover_time(
        self,
        request: main_models.DescribeClusterRecoverTimeRequest,
    ) -> main_models.DescribeClusterRecoverTimeResponse:
        runtime = RuntimeOptions()
        return self.describe_cluster_recover_time_with_options(request, runtime)

    async def describe_cluster_recover_time_async(
        self,
        request: main_models.DescribeClusterRecoverTimeRequest,
    ) -> main_models.DescribeClusterRecoverTimeResponse:
        runtime = RuntimeOptions()
        return await self.describe_cluster_recover_time_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: main_models.DescribeDBInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.is_delete):
            query['IsDelete'] = request.is_delete
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action = 'DescribeDBInstanceAttribute',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: main_models.DescribeDBInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.is_delete):
            query['IsDelete'] = request.is_delete
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            action = 'DescribeDBInstanceAttribute',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: main_models.DescribeDBInstanceAttributeRequest,
    ) -> main_models.DescribeDBInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: main_models.DescribeDBInstanceAttributeRequest,
    ) -> main_models.DescribeDBInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_encryption_key_with_options(
        self,
        request: main_models.DescribeDBInstanceEncryptionKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceEncryptionKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
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
            action = 'DescribeDBInstanceEncryptionKey',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceEncryptionKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_encryption_key_with_options_async(
        self,
        request: main_models.DescribeDBInstanceEncryptionKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceEncryptionKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
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
            action = 'DescribeDBInstanceEncryptionKey',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceEncryptionKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_encryption_key(
        self,
        request: main_models.DescribeDBInstanceEncryptionKeyRequest,
    ) -> main_models.DescribeDBInstanceEncryptionKeyResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_encryption_key_with_options(request, runtime)

    async def describe_dbinstance_encryption_key_async(
        self,
        request: main_models.DescribeDBInstanceEncryptionKeyRequest,
    ) -> main_models.DescribeDBInstanceEncryptionKeyResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_encryption_key_with_options_async(request, runtime)

    def describe_dbinstance_monitor_with_options(
        self,
        request: main_models.DescribeDBInstanceMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeDBInstanceMonitor',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_monitor_with_options_async(
        self,
        request: main_models.DescribeDBInstanceMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeDBInstanceMonitor',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_monitor(
        self,
        request: main_models.DescribeDBInstanceMonitorRequest,
    ) -> main_models.DescribeDBInstanceMonitorResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_monitor_with_options(request, runtime)

    async def describe_dbinstance_monitor_async(
        self,
        request: main_models.DescribeDBInstanceMonitorRequest,
    ) -> main_models.DescribeDBInstanceMonitorResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_monitor_with_options_async(request, runtime)

    def describe_dbinstance_performance_with_options(
        self,
        request: main_models.DescribeDBInstancePerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancePerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.replica_set_role):
            query['ReplicaSetRole'] = request.replica_set_role
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.search_id):
            query['SearchId'] = request.search_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstancePerformance',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstancePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_performance_with_options_async(
        self,
        request: main_models.DescribeDBInstancePerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancePerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.replica_set_role):
            query['ReplicaSetRole'] = request.replica_set_role
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.search_id):
            query['SearchId'] = request.search_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstancePerformance',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstancePerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_performance(
        self,
        request: main_models.DescribeDBInstancePerformanceRequest,
    ) -> main_models.DescribeDBInstancePerformanceResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    async def describe_dbinstance_performance_async(
        self,
        request: main_models.DescribeDBInstancePerformanceRequest,
    ) -> main_models.DescribeDBInstancePerformanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_performance_with_options_async(request, runtime)

    def describe_dbinstance_sslwith_options(
        self,
        request: main_models.DescribeDBInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeDBInstanceSSL',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_sslwith_options_async(
        self,
        request: main_models.DescribeDBInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeDBInstanceSSL',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_ssl(
        self,
        request: main_models.DescribeDBInstanceSSLRequest,
    ) -> main_models.DescribeDBInstanceSSLResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    async def describe_dbinstance_ssl_async(
        self,
        request: main_models.DescribeDBInstanceSSLRequest,
    ) -> main_models.DescribeDBInstanceSSLResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_sslwith_options_async(request, runtime)

    def describe_dbinstance_spec_info_with_options(
        self,
        request: main_models.DescribeDBInstanceSpecInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceSpecInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
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
            action = 'DescribeDBInstanceSpecInfo',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceSpecInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_spec_info_with_options_async(
        self,
        request: main_models.DescribeDBInstanceSpecInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceSpecInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
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
            action = 'DescribeDBInstanceSpecInfo',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceSpecInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_spec_info(
        self,
        request: main_models.DescribeDBInstanceSpecInfoRequest,
    ) -> main_models.DescribeDBInstanceSpecInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_spec_info_with_options(request, runtime)

    async def describe_dbinstance_spec_info_async(
        self,
        request: main_models.DescribeDBInstanceSpecInfoRequest,
    ) -> main_models.DescribeDBInstanceSpecInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_spec_info_with_options_async(request, runtime)

    def describe_dbinstance_switch_log_with_options(
        self,
        request: main_models.DescribeDBInstanceSwitchLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceSwitchLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceSwitchLog',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceSwitchLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_switch_log_with_options_async(
        self,
        request: main_models.DescribeDBInstanceSwitchLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceSwitchLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceSwitchLog',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceSwitchLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_switch_log(
        self,
        request: main_models.DescribeDBInstanceSwitchLogRequest,
    ) -> main_models.DescribeDBInstanceSwitchLogResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_switch_log_with_options(request, runtime)

    async def describe_dbinstance_switch_log_async(
        self,
        request: main_models.DescribeDBInstanceSwitchLogRequest,
    ) -> main_models.DescribeDBInstanceSwitchLogResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_switch_log_with_options_async(request, runtime)

    def describe_dbinstance_tdeinfo_with_options(
        self,
        request: main_models.DescribeDBInstanceTDEInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceTDEInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeDBInstanceTDEInfo',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceTDEInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_tdeinfo_with_options_async(
        self,
        request: main_models.DescribeDBInstanceTDEInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceTDEInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeDBInstanceTDEInfo',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceTDEInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_tdeinfo(
        self,
        request: main_models.DescribeDBInstanceTDEInfoRequest,
    ) -> main_models.DescribeDBInstanceTDEInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_tdeinfo_with_options(request, runtime)

    async def describe_dbinstance_tdeinfo_async(
        self,
        request: main_models.DescribeDBInstanceTDEInfoRequest,
    ) -> main_models.DescribeDBInstanceTDEInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_tdeinfo_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        request: main_models.DescribeDBInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.connection_domain):
            query['ConnectionDomain'] = request.connection_domain
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not DaraCore.is_null(request.dbinstance_type):
            query['DBInstanceType'] = request.dbinstance_type
        if not DaraCore.is_null(request.dbnode_type):
            query['DBNodeType'] = request.dbnode_type
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.expired):
            query['Expired'] = request.expired
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
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
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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
            action = 'DescribeDBInstances',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        request: main_models.DescribeDBInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.connection_domain):
            query['ConnectionDomain'] = request.connection_domain
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not DaraCore.is_null(request.dbinstance_type):
            query['DBInstanceType'] = request.dbinstance_type
        if not DaraCore.is_null(request.dbnode_type):
            query['DBNodeType'] = request.dbnode_type
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not DaraCore.is_null(request.expired):
            query['Expired'] = request.expired
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
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
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
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
            action = 'DescribeDBInstances',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances(
        self,
        request: main_models.DescribeDBInstancesRequest,
    ) -> main_models.DescribeDBInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: main_models.DescribeDBInstancesRequest,
    ) -> main_models.DescribeDBInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_dbinstances_overview_with_options(
        self,
        request: main_models.DescribeDBInstancesOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancesOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.show_tags):
            query['ShowTags'] = request.show_tags
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
            action = 'DescribeDBInstancesOverview',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstancesOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_overview_with_options_async(
        self,
        request: main_models.DescribeDBInstancesOverviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancesOverviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.show_tags):
            query['ShowTags'] = request.show_tags
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
            action = 'DescribeDBInstancesOverview',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstancesOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances_overview(
        self,
        request: main_models.DescribeDBInstancesOverviewRequest,
    ) -> main_models.DescribeDBInstancesOverviewResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstances_overview_with_options(request, runtime)

    async def describe_dbinstances_overview_async(
        self,
        request: main_models.DescribeDBInstancesOverviewRequest,
    ) -> main_models.DescribeDBInstancesOverviewResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstances_overview_with_options_async(request, runtime)

    def describe_error_log_records_with_options(
        self,
        request: main_models.DescribeErrorLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeErrorLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeErrorLogRecords',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeErrorLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_error_log_records_with_options_async(
        self,
        request: main_models.DescribeErrorLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeErrorLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeErrorLogRecords',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeErrorLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_error_log_records(
        self,
        request: main_models.DescribeErrorLogRecordsRequest,
    ) -> main_models.DescribeErrorLogRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_error_log_records_with_options(request, runtime)

    async def describe_error_log_records_async(
        self,
        request: main_models.DescribeErrorLogRecordsRequest,
    ) -> main_models.DescribeErrorLogRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_error_log_records_with_options_async(request, runtime)

    def describe_global_security_ipgroup_with_options(
        self,
        request: main_models.DescribeGlobalSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGlobalSecurityIPGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGlobalSecurityIPGroup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_security_ipgroup_with_options_async(
        self,
        request: main_models.DescribeGlobalSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGlobalSecurityIPGroupResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGlobalSecurityIPGroup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_security_ipgroup(
        self,
        request: main_models.DescribeGlobalSecurityIPGroupRequest,
    ) -> main_models.DescribeGlobalSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_global_security_ipgroup_with_options(request, runtime)

    async def describe_global_security_ipgroup_async(
        self,
        request: main_models.DescribeGlobalSecurityIPGroupRequest,
    ) -> main_models.DescribeGlobalSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_global_security_ipgroup_with_options_async(request, runtime)

    def describe_global_security_ipgroup_relation_with_options(
        self,
        request: main_models.DescribeGlobalSecurityIPGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGlobalSecurityIPGroupRelationResponse:
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
            action = 'DescribeGlobalSecurityIPGroupRelation',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGlobalSecurityIPGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_global_security_ipgroup_relation_with_options_async(
        self,
        request: main_models.DescribeGlobalSecurityIPGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGlobalSecurityIPGroupRelationResponse:
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
            action = 'DescribeGlobalSecurityIPGroupRelation',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGlobalSecurityIPGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_global_security_ipgroup_relation(
        self,
        request: main_models.DescribeGlobalSecurityIPGroupRelationRequest,
    ) -> main_models.DescribeGlobalSecurityIPGroupRelationResponse:
        runtime = RuntimeOptions()
        return self.describe_global_security_ipgroup_relation_with_options(request, runtime)

    async def describe_global_security_ipgroup_relation_async(
        self,
        request: main_models.DescribeGlobalSecurityIPGroupRelationRequest,
    ) -> main_models.DescribeGlobalSecurityIPGroupRelationResponse:
        runtime = RuntimeOptions()
        return await self.describe_global_security_ipgroup_relation_with_options_async(request, runtime)

    def describe_history_tasks_with_options(
        self,
        request: main_models.DescribeHistoryTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHistoryTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not DaraCore.is_null(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
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
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not DaraCore.is_null(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHistoryTasks',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHistoryTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_tasks_with_options_async(
        self,
        request: main_models.DescribeHistoryTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHistoryTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not DaraCore.is_null(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
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
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not DaraCore.is_null(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHistoryTasks',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHistoryTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_tasks(
        self,
        request: main_models.DescribeHistoryTasksRequest,
    ) -> main_models.DescribeHistoryTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_history_tasks_with_options(request, runtime)

    async def describe_history_tasks_async(
        self,
        request: main_models.DescribeHistoryTasksRequest,
    ) -> main_models.DescribeHistoryTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_history_tasks_with_options_async(request, runtime)

    def describe_history_tasks_stat_with_options(
        self,
        request: main_models.DescribeHistoryTasksStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHistoryTasksStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not DaraCore.is_null(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not DaraCore.is_null(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHistoryTasksStat',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHistoryTasksStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_history_tasks_stat_with_options_async(
        self,
        request: main_models.DescribeHistoryTasksStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHistoryTasksStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_exec_time):
            query['FromExecTime'] = request.from_exec_time
        if not DaraCore.is_null(request.from_start_time):
            query['FromStartTime'] = request.from_start_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.to_exec_time):
            query['ToExecTime'] = request.to_exec_time
        if not DaraCore.is_null(request.to_start_time):
            query['ToStartTime'] = request.to_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHistoryTasksStat',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHistoryTasksStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_history_tasks_stat(
        self,
        request: main_models.DescribeHistoryTasksStatRequest,
    ) -> main_models.DescribeHistoryTasksStatResponse:
        runtime = RuntimeOptions()
        return self.describe_history_tasks_stat_with_options(request, runtime)

    async def describe_history_tasks_stat_async(
        self,
        request: main_models.DescribeHistoryTasksStatRequest,
    ) -> main_models.DescribeHistoryTasksStatResponse:
        runtime = RuntimeOptions()
        return await self.describe_history_tasks_stat_with_options_async(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(
        self,
        request: main_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAutoRenewalAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbinstance_type):
            query['DBInstanceType'] = request.dbinstance_type
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
            action = 'DescribeInstanceAutoRenewalAttribute',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_auto_renewal_attribute_with_options_async(
        self,
        request: main_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceAutoRenewalAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbinstance_type):
            query['DBInstanceType'] = request.dbinstance_type
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
            action = 'DescribeInstanceAutoRenewalAttribute',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceAutoRenewalAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_auto_renewal_attribute(
        self,
        request: main_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> main_models.DescribeInstanceAutoRenewalAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    async def describe_instance_auto_renewal_attribute_async(
        self,
        request: main_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> main_models.DescribeInstanceAutoRenewalAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def describe_instance_recover_time_with_options(
        self,
        request: main_models.DescribeInstanceRecoverTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceRecoverTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceRecoverTime',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceRecoverTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_recover_time_with_options_async(
        self,
        request: main_models.DescribeInstanceRecoverTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceRecoverTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceRecoverTime',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceRecoverTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_recover_time(
        self,
        request: main_models.DescribeInstanceRecoverTimeRequest,
    ) -> main_models.DescribeInstanceRecoverTimeResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_recover_time_with_options(request, runtime)

    async def describe_instance_recover_time_async(
        self,
        request: main_models.DescribeInstanceRecoverTimeRequest,
    ) -> main_models.DescribeInstanceRecoverTimeResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_recover_time_with_options_async(request, runtime)

    def describe_kernel_release_notes_with_options(
        self,
        request: main_models.DescribeKernelReleaseNotesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKernelReleaseNotesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kernel_version):
            query['KernelVersion'] = request.kernel_version
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
            action = 'DescribeKernelReleaseNotes',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKernelReleaseNotesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kernel_release_notes_with_options_async(
        self,
        request: main_models.DescribeKernelReleaseNotesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKernelReleaseNotesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kernel_version):
            query['KernelVersion'] = request.kernel_version
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
            action = 'DescribeKernelReleaseNotes',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKernelReleaseNotesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kernel_release_notes(
        self,
        request: main_models.DescribeKernelReleaseNotesRequest,
    ) -> main_models.DescribeKernelReleaseNotesResponse:
        runtime = RuntimeOptions()
        return self.describe_kernel_release_notes_with_options(request, runtime)

    async def describe_kernel_release_notes_async(
        self,
        request: main_models.DescribeKernelReleaseNotesRequest,
    ) -> main_models.DescribeKernelReleaseNotesResponse:
        runtime = RuntimeOptions()
        return await self.describe_kernel_release_notes_with_options_async(request, runtime)

    def describe_kms_keys_with_options(
        self,
        request: main_models.DescribeKmsKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKmsKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
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
            action = 'DescribeKmsKeys',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKmsKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kms_keys_with_options_async(
        self,
        request: main_models.DescribeKmsKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeKmsKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
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
            action = 'DescribeKmsKeys',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeKmsKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kms_keys(
        self,
        request: main_models.DescribeKmsKeysRequest,
    ) -> main_models.DescribeKmsKeysResponse:
        runtime = RuntimeOptions()
        return self.describe_kms_keys_with_options(request, runtime)

    async def describe_kms_keys_async(
        self,
        request: main_models.DescribeKmsKeysRequest,
    ) -> main_models.DescribeKmsKeysResponse:
        runtime = RuntimeOptions()
        return await self.describe_kms_keys_with_options_async(request, runtime)

    def describe_mongo_dblog_config_with_options(
        self,
        request: main_models.DescribeMongoDBLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMongoDBLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeMongoDBLogConfig',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMongoDBLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mongo_dblog_config_with_options_async(
        self,
        request: main_models.DescribeMongoDBLogConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMongoDBLogConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeMongoDBLogConfig',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMongoDBLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mongo_dblog_config(
        self,
        request: main_models.DescribeMongoDBLogConfigRequest,
    ) -> main_models.DescribeMongoDBLogConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_mongo_dblog_config_with_options(request, runtime)

    async def describe_mongo_dblog_config_async(
        self,
        request: main_models.DescribeMongoDBLogConfigRequest,
    ) -> main_models.DescribeMongoDBLogConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_mongo_dblog_config_with_options_async(request, runtime)

    def describe_parameter_modification_history_with_options(
        self,
        request: main_models.DescribeParameterModificationHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParameterModificationHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'DescribeParameterModificationHistory',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParameterModificationHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_modification_history_with_options_async(
        self,
        request: main_models.DescribeParameterModificationHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParameterModificationHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'DescribeParameterModificationHistory',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParameterModificationHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_modification_history(
        self,
        request: main_models.DescribeParameterModificationHistoryRequest,
    ) -> main_models.DescribeParameterModificationHistoryResponse:
        runtime = RuntimeOptions()
        return self.describe_parameter_modification_history_with_options(request, runtime)

    async def describe_parameter_modification_history_async(
        self,
        request: main_models.DescribeParameterModificationHistoryRequest,
    ) -> main_models.DescribeParameterModificationHistoryResponse:
        runtime = RuntimeOptions()
        return await self.describe_parameter_modification_history_with_options_async(request, runtime)

    def describe_parameter_templates_with_options(
        self,
        request: main_models.DescribeParameterTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParameterTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
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
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParameterTemplates',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParameterTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_templates_with_options_async(
        self,
        request: main_models.DescribeParameterTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParameterTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
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
        if not DaraCore.is_null(request.role):
            query['Role'] = request.role
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParameterTemplates',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParameterTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_templates(
        self,
        request: main_models.DescribeParameterTemplatesRequest,
    ) -> main_models.DescribeParameterTemplatesResponse:
        runtime = RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    async def describe_parameter_templates_async(
        self,
        request: main_models.DescribeParameterTemplatesRequest,
    ) -> main_models.DescribeParameterTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.describe_parameter_templates_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: main_models.DescribeParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.extra_param):
            query['ExtraParam'] = request.extra_param
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'DescribeParameters',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: main_models.DescribeParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.extra_param):
            query['ExtraParam'] = request.extra_param
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'DescribeParameters',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameters(
        self,
        request: main_models.DescribeParametersRequest,
    ) -> main_models.DescribeParametersResponse:
        runtime = RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: main_models.DescribeParametersRequest,
    ) -> main_models.DescribeParametersResponse:
        runtime = RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: main_models.DescribePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not DaraCore.is_null(request.order_param_out):
            query['OrderParamOut'] = request.order_param_out
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrice',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: main_models.DescribePriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not DaraCore.is_null(request.order_param_out):
            query['OrderParamOut'] = request.order_param_out
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrice',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_price(
        self,
        request: main_models.DescribePriceRequest,
    ) -> main_models.DescribePriceResponse:
        runtime = RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: main_models.DescribePriceRequest,
    ) -> main_models.DescribePriceResponse:
        runtime = RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_rds_vswitchs_with_options(
        self,
        request: main_models.DescribeRdsVSwitchsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdsVSwitchsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdsVSwitchs',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdsVSwitchsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_vswitchs_with_options_async(
        self,
        request: main_models.DescribeRdsVSwitchsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdsVSwitchsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdsVSwitchs',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdsVSwitchsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_vswitchs(
        self,
        request: main_models.DescribeRdsVSwitchsRequest,
    ) -> main_models.DescribeRdsVSwitchsResponse:
        runtime = RuntimeOptions()
        return self.describe_rds_vswitchs_with_options(request, runtime)

    async def describe_rds_vswitchs_async(
        self,
        request: main_models.DescribeRdsVSwitchsRequest,
    ) -> main_models.DescribeRdsVSwitchsResponse:
        runtime = RuntimeOptions()
        return await self.describe_rds_vswitchs_with_options_async(request, runtime)

    def describe_rds_vpcs_with_options(
        self,
        request: main_models.DescribeRdsVpcsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdsVpcsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdsVpcs',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdsVpcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_vpcs_with_options_async(
        self,
        request: main_models.DescribeRdsVpcsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdsVpcsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdsVpcs',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdsVpcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_vpcs(
        self,
        request: main_models.DescribeRdsVpcsRequest,
    ) -> main_models.DescribeRdsVpcsResponse:
        runtime = RuntimeOptions()
        return self.describe_rds_vpcs_with_options(request, runtime)

    async def describe_rds_vpcs_async(
        self,
        request: main_models.DescribeRdsVpcsRequest,
    ) -> main_models.DescribeRdsVpcsResponse:
        runtime = RuntimeOptions()
        return await self.describe_rds_vpcs_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            action = 'DescribeRegions',
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
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
            action = 'DescribeRegions',
            version = '2015-12-01',
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

    def describe_renewal_price_with_options(
        self,
        request: main_models.DescribeRenewalPriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRenewalPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeRenewalPrice',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRenewalPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_renewal_price_with_options_async(
        self,
        request: main_models.DescribeRenewalPriceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRenewalPriceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeRenewalPrice',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRenewalPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_renewal_price(
        self,
        request: main_models.DescribeRenewalPriceRequest,
    ) -> main_models.DescribeRenewalPriceResponse:
        runtime = RuntimeOptions()
        return self.describe_renewal_price_with_options(request, runtime)

    async def describe_renewal_price_async(
        self,
        request: main_models.DescribeRenewalPriceRequest,
    ) -> main_models.DescribeRenewalPriceResponse:
        runtime = RuntimeOptions()
        return await self.describe_renewal_price_with_options_async(request, runtime)

    def describe_replica_set_role_with_options(
        self,
        request: main_models.DescribeReplicaSetRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeReplicaSetRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeReplicaSetRole',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeReplicaSetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_replica_set_role_with_options_async(
        self,
        request: main_models.DescribeReplicaSetRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeReplicaSetRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeReplicaSetRole',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeReplicaSetRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_replica_set_role(
        self,
        request: main_models.DescribeReplicaSetRoleRequest,
    ) -> main_models.DescribeReplicaSetRoleResponse:
        runtime = RuntimeOptions()
        return self.describe_replica_set_role_with_options(request, runtime)

    async def describe_replica_set_role_async(
        self,
        request: main_models.DescribeReplicaSetRoleRequest,
    ) -> main_models.DescribeReplicaSetRoleResponse:
        runtime = RuntimeOptions()
        return await self.describe_replica_set_role_with_options_async(request, runtime)

    def describe_restore_dbinstance_list_with_options(
        self,
        request: main_models.DescribeRestoreDBInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreDBInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creation_time_after):
            query['CreationTimeAfter'] = request.creation_time_after
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeRestoreDBInstanceList',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreDBInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_dbinstance_list_with_options_async(
        self,
        request: main_models.DescribeRestoreDBInstanceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreDBInstanceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.creation_time_after):
            query['CreationTimeAfter'] = request.creation_time_after
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeRestoreDBInstanceList',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreDBInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_dbinstance_list(
        self,
        request: main_models.DescribeRestoreDBInstanceListRequest,
    ) -> main_models.DescribeRestoreDBInstanceListResponse:
        runtime = RuntimeOptions()
        return self.describe_restore_dbinstance_list_with_options(request, runtime)

    async def describe_restore_dbinstance_list_async(
        self,
        request: main_models.DescribeRestoreDBInstanceListRequest,
    ) -> main_models.DescribeRestoreDBInstanceListResponse:
        runtime = RuntimeOptions()
        return await self.describe_restore_dbinstance_list_with_options_async(request, runtime)

    def describe_role_tag_status_with_options(
        self,
        request: main_models.DescribeRoleTagStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoleTagStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeRoleTagStatus',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoleTagStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_role_tag_status_with_options_async(
        self,
        request: main_models.DescribeRoleTagStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoleTagStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeRoleTagStatus',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoleTagStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_role_tag_status(
        self,
        request: main_models.DescribeRoleTagStatusRequest,
    ) -> main_models.DescribeRoleTagStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_role_tag_status_with_options(request, runtime)

    async def describe_role_tag_status_async(
        self,
        request: main_models.DescribeRoleTagStatusRequest,
    ) -> main_models.DescribeRoleTagStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_role_tag_status_with_options_async(request, runtime)

    def describe_role_zone_info_with_options(
        self,
        request: main_models.DescribeRoleZoneInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoleZoneInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeRoleZoneInfo',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoleZoneInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_role_zone_info_with_options_async(
        self,
        request: main_models.DescribeRoleZoneInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRoleZoneInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeRoleZoneInfo',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRoleZoneInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_role_zone_info(
        self,
        request: main_models.DescribeRoleZoneInfoRequest,
    ) -> main_models.DescribeRoleZoneInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_role_zone_info_with_options(request, runtime)

    async def describe_role_zone_info_async(
        self,
        request: main_models.DescribeRoleZoneInfoRequest,
    ) -> main_models.DescribeRoleZoneInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_role_zone_info_with_options_async(request, runtime)

    def describe_running_log_records_with_options(
        self,
        request: main_models.DescribeRunningLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRunningLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRunningLogRecords',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRunningLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_running_log_records_with_options_async(
        self,
        request: main_models.DescribeRunningLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRunningLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRunningLogRecords',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRunningLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_running_log_records(
        self,
        request: main_models.DescribeRunningLogRecordsRequest,
    ) -> main_models.DescribeRunningLogRecordsResponse:
        runtime = RuntimeOptions()
        return self.describe_running_log_records_with_options(request, runtime)

    async def describe_running_log_records_async(
        self,
        request: main_models.DescribeRunningLogRecordsRequest,
    ) -> main_models.DescribeRunningLogRecordsResponse:
        runtime = RuntimeOptions()
        return await self.describe_running_log_records_with_options_async(request, runtime)

    def describe_security_group_configuration_with_options(
        self,
        request: main_models.DescribeSecurityGroupConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityGroupConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeSecurityGroupConfiguration',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_group_configuration_with_options_async(
        self,
        request: main_models.DescribeSecurityGroupConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityGroupConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeSecurityGroupConfiguration',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityGroupConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_group_configuration(
        self,
        request: main_models.DescribeSecurityGroupConfigurationRequest,
    ) -> main_models.DescribeSecurityGroupConfigurationResponse:
        runtime = RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    async def describe_security_group_configuration_async(
        self,
        request: main_models.DescribeSecurityGroupConfigurationRequest,
    ) -> main_models.DescribeSecurityGroupConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_group_configuration_with_options_async(request, runtime)

    def describe_security_ips_with_options(
        self,
        request: main_models.DescribeSecurityIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.show_hdmips):
            query['ShowHDMIps'] = request.show_hdmips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityIps',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_ips_with_options_async(
        self,
        request: main_models.DescribeSecurityIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.show_hdmips):
            query['ShowHDMIps'] = request.show_hdmips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityIps',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_ips(
        self,
        request: main_models.DescribeSecurityIpsRequest,
    ) -> main_models.DescribeSecurityIpsResponse:
        runtime = RuntimeOptions()
        return self.describe_security_ips_with_options(request, runtime)

    async def describe_security_ips_async(
        self,
        request: main_models.DescribeSecurityIpsRequest,
    ) -> main_models.DescribeSecurityIpsResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_ips_with_options_async(request, runtime)

    def describe_sharding_network_address_with_options(
        self,
        request: main_models.DescribeShardingNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeShardingNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'DescribeShardingNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeShardingNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sharding_network_address_with_options_async(
        self,
        request: main_models.DescribeShardingNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeShardingNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'DescribeShardingNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeShardingNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sharding_network_address(
        self,
        request: main_models.DescribeShardingNetworkAddressRequest,
    ) -> main_models.DescribeShardingNetworkAddressResponse:
        runtime = RuntimeOptions()
        return self.describe_sharding_network_address_with_options(request, runtime)

    async def describe_sharding_network_address_async(
        self,
        request: main_models.DescribeShardingNetworkAddressRequest,
    ) -> main_models.DescribeShardingNetworkAddressResponse:
        runtime = RuntimeOptions()
        return await self.describe_sharding_network_address_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.logical_operator):
            query['LogicalOperator'] = request.logical_operator
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_keywords):
            query['QueryKeywords'] = request.query_keywords
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version = '2015-12-01',
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

    def describe_tags_with_options(
        self,
        request: main_models.DescribeTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsResponse:
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTags',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: main_models.DescribeTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsResponse:
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTags',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tags(
        self,
        request: main_models.DescribeTagsRequest,
    ) -> main_models.DescribeTagsResponse:
        runtime = RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: main_models.DescribeTagsRequest,
    ) -> main_models.DescribeTagsResponse:
        runtime = RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_user_encryption_key_list_with_options(
        self,
        request: main_models.DescribeUserEncryptionKeyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserEncryptionKeyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_arn):
            query['RoleARN'] = request.role_arn
        if not DaraCore.is_null(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserEncryptionKeyList',
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_arn):
            query['RoleARN'] = request.role_arn
        if not DaraCore.is_null(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserEncryptionKeyList',
            version = '2015-12-01',
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

    def describe_vpcs_for_mongo_dbwith_options(
        self,
        request: main_models.DescribeVpcsForMongoDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcsForMongoDBResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcsForMongoDB',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcsForMongoDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vpcs_for_mongo_dbwith_options_async(
        self,
        request: main_models.DescribeVpcsForMongoDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVpcsForMongoDBResponse:
        request.validate()
        query = {}
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
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVpcsForMongoDB',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVpcsForMongoDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vpcs_for_mongo_db(
        self,
        request: main_models.DescribeVpcsForMongoDBRequest,
    ) -> main_models.DescribeVpcsForMongoDBResponse:
        runtime = RuntimeOptions()
        return self.describe_vpcs_for_mongo_dbwith_options(request, runtime)

    async def describe_vpcs_for_mongo_db_async(
        self,
        request: main_models.DescribeVpcsForMongoDBRequest,
    ) -> main_models.DescribeVpcsForMongoDBResponse:
        runtime = RuntimeOptions()
        return await self.describe_vpcs_for_mongo_dbwith_options_async(request, runtime)

    def destroy_instance_with_options(
        self,
        request: main_models.DestroyInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DestroyInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DestroyInstance',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DestroyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def destroy_instance_with_options_async(
        self,
        request: main_models.DestroyInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DestroyInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DestroyInstance',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DestroyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def destroy_instance(
        self,
        request: main_models.DestroyInstanceRequest,
    ) -> main_models.DestroyInstanceResponse:
        runtime = RuntimeOptions()
        return self.destroy_instance_with_options(request, runtime)

    async def destroy_instance_async(
        self,
        request: main_models.DestroyInstanceRequest,
    ) -> main_models.DestroyInstanceResponse:
        runtime = RuntimeOptions()
        return await self.destroy_instance_with_options_async(request, runtime)

    def evaluate_resource_with_options(
        self,
        request: main_models.EvaluateResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EvaluateResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.shards_info):
            query['ShardsInfo'] = request.shards_info
        if not DaraCore.is_null(request.storage):
            query['Storage'] = request.storage
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EvaluateResource',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EvaluateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def evaluate_resource_with_options_async(
        self,
        request: main_models.EvaluateResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EvaluateResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.shards_info):
            query['ShardsInfo'] = request.shards_info
        if not DaraCore.is_null(request.storage):
            query['Storage'] = request.storage
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EvaluateResource',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EvaluateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def evaluate_resource(
        self,
        request: main_models.EvaluateResourceRequest,
    ) -> main_models.EvaluateResourceResponse:
        runtime = RuntimeOptions()
        return self.evaluate_resource_with_options(request, runtime)

    async def evaluate_resource_async(
        self,
        request: main_models.EvaluateResourceRequest,
    ) -> main_models.EvaluateResourceResponse:
        runtime = RuntimeOptions()
        return await self.evaluate_resource_with_options_async(request, runtime)

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
            version = '2015-12-01',
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
            version = '2015-12-01',
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

    def migrate_available_zone_with_options(
        self,
        request: main_models.MigrateAvailableZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MigrateAvailableZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.hidden_zone_id):
            query['HiddenZoneId'] = request.hidden_zone_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not DaraCore.is_null(request.vswitch):
            query['Vswitch'] = request.vswitch
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateAvailableZone',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateAvailableZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_available_zone_with_options_async(
        self,
        request: main_models.MigrateAvailableZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MigrateAvailableZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.hidden_zone_id):
            query['HiddenZoneId'] = request.hidden_zone_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not DaraCore.is_null(request.vswitch):
            query['Vswitch'] = request.vswitch
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateAvailableZone',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateAvailableZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_available_zone(
        self,
        request: main_models.MigrateAvailableZoneRequest,
    ) -> main_models.MigrateAvailableZoneResponse:
        runtime = RuntimeOptions()
        return self.migrate_available_zone_with_options(request, runtime)

    async def migrate_available_zone_async(
        self,
        request: main_models.MigrateAvailableZoneRequest,
    ) -> main_models.MigrateAvailableZoneResponse:
        runtime = RuntimeOptions()
        return await self.migrate_available_zone_with_options_async(request, runtime)

    def migrate_to_other_zone_with_options(
        self,
        request: main_models.MigrateToOtherZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MigrateToOtherZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateToOtherZone',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateToOtherZoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_to_other_zone_with_options_async(
        self,
        request: main_models.MigrateToOtherZoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MigrateToOtherZoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateToOtherZone',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateToOtherZoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_to_other_zone(
        self,
        request: main_models.MigrateToOtherZoneRequest,
    ) -> main_models.MigrateToOtherZoneResponse:
        runtime = RuntimeOptions()
        return self.migrate_to_other_zone_with_options(request, runtime)

    async def migrate_to_other_zone_async(
        self,
        request: main_models.MigrateToOtherZoneRequest,
    ) -> main_models.MigrateToOtherZoneResponse:
        runtime = RuntimeOptions()
        return await self.migrate_to_other_zone_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            version = '2015-12-01',
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

    def modify_active_operation_maintenance_config_with_options(
        self,
        request: main_models.ModifyActiveOperationMaintenanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyActiveOperationMaintenanceConfigResponse:
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
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationMaintenanceConfig',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyActiveOperationMaintenanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_active_operation_maintenance_config_with_options_async(
        self,
        request: main_models.ModifyActiveOperationMaintenanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyActiveOperationMaintenanceConfigResponse:
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
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationMaintenanceConfig',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyActiveOperationMaintenanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_active_operation_maintenance_config(
        self,
        request: main_models.ModifyActiveOperationMaintenanceConfigRequest,
    ) -> main_models.ModifyActiveOperationMaintenanceConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_active_operation_maintenance_config_with_options(request, runtime)

    async def modify_active_operation_maintenance_config_async(
        self,
        request: main_models.ModifyActiveOperationMaintenanceConfigRequest,
    ) -> main_models.ModifyActiveOperationMaintenanceConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_active_operation_maintenance_config_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationTasks',
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationTasks',
            version = '2015-12-01',
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

    def modify_audit_log_filter_with_options(
        self,
        request: main_models.ModifyAuditLogFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAuditLogFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAuditLogFilter',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAuditLogFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_audit_log_filter_with_options_async(
        self,
        request: main_models.ModifyAuditLogFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAuditLogFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_type):
            query['RoleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAuditLogFilter',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAuditLogFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_audit_log_filter(
        self,
        request: main_models.ModifyAuditLogFilterRequest,
    ) -> main_models.ModifyAuditLogFilterResponse:
        runtime = RuntimeOptions()
        return self.modify_audit_log_filter_with_options(request, runtime)

    async def modify_audit_log_filter_async(
        self,
        request: main_models.ModifyAuditLogFilterRequest,
    ) -> main_models.ModifyAuditLogFilterResponse:
        runtime = RuntimeOptions()
        return await self.modify_audit_log_filter_with_options_async(request, runtime)

    def modify_audit_policy_with_options(
        self,
        request: main_models.ModifyAuditPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAuditPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_log_switch_source):
            query['AuditLogSwitchSource'] = request.audit_log_switch_source
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.storage_period):
            query['StoragePeriod'] = request.storage_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAuditPolicy',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAuditPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_audit_policy_with_options_async(
        self,
        request: main_models.ModifyAuditPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAuditPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_log_switch_source):
            query['AuditLogSwitchSource'] = request.audit_log_switch_source
        if not DaraCore.is_null(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.storage_period):
            query['StoragePeriod'] = request.storage_period
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAuditPolicy',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAuditPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_audit_policy(
        self,
        request: main_models.ModifyAuditPolicyRequest,
    ) -> main_models.ModifyAuditPolicyResponse:
        runtime = RuntimeOptions()
        return self.modify_audit_policy_with_options(request, runtime)

    async def modify_audit_policy_async(
        self,
        request: main_models.ModifyAuditPolicyRequest,
    ) -> main_models.ModifyAuditPolicyResponse:
        runtime = RuntimeOptions()
        return await self.modify_audit_policy_with_options_async(request, runtime)

    def modify_backup_expire_time_with_options(
        self,
        request: main_models.ModifyBackupExpireTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupExpireTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_expire_time):
            query['BackupExpireTime'] = request.backup_expire_time
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'ModifyBackupExpireTime',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_expire_time_with_options_async(
        self,
        request: main_models.ModifyBackupExpireTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupExpireTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_expire_time):
            query['BackupExpireTime'] = request.backup_expire_time
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'ModifyBackupExpireTime',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupExpireTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_expire_time(
        self,
        request: main_models.ModifyBackupExpireTimeRequest,
    ) -> main_models.ModifyBackupExpireTimeResponse:
        runtime = RuntimeOptions()
        return self.modify_backup_expire_time_with_options(request, runtime)

    async def modify_backup_expire_time_async(
        self,
        request: main_models.ModifyBackupExpireTimeRequest,
    ) -> main_models.ModifyBackupExpireTimeResponse:
        runtime = RuntimeOptions()
        return await self.modify_backup_expire_time_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: main_models.ModifyBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_interval):
            query['BackupInterval'] = request.backup_interval
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.backup_retention_policy_on_cluster_deletion):
            query['BackupRetentionPolicyOnClusterDeletion'] = request.backup_retention_policy_on_cluster_deletion
        if not DaraCore.is_null(request.cross_backup_period):
            query['CrossBackupPeriod'] = request.cross_backup_period
        if not DaraCore.is_null(request.cross_backup_type):
            query['CrossBackupType'] = request.cross_backup_type
        if not DaraCore.is_null(request.cross_log_retention_type):
            query['CrossLogRetentionType'] = request.cross_log_retention_type
        if not DaraCore.is_null(request.cross_log_retention_value):
            query['CrossLogRetentionValue'] = request.cross_log_retention_value
        if not DaraCore.is_null(request.cross_retention_type):
            query['CrossRetentionType'] = request.cross_retention_type
        if not DaraCore.is_null(request.cross_retention_value):
            query['CrossRetentionValue'] = request.cross_retention_value
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not DaraCore.is_null(request.enable_cross_log_backup):
            query['EnableCrossLogBackup'] = request.enable_cross_log_backup
        if not DaraCore.is_null(request.high_frequency_backup_retention):
            query['HighFrequencyBackupRetention'] = request.high_frequency_backup_retention
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not DaraCore.is_null(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not DaraCore.is_null(request.preserve_one_each_hour):
            query['PreserveOneEachHour'] = request.preserve_one_each_hour
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.snapshot_backup_type):
            query['SnapshotBackupType'] = request.snapshot_backup_type
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPolicy',
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.backup_interval):
            query['BackupInterval'] = request.backup_interval
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.backup_retention_policy_on_cluster_deletion):
            query['BackupRetentionPolicyOnClusterDeletion'] = request.backup_retention_policy_on_cluster_deletion
        if not DaraCore.is_null(request.cross_backup_period):
            query['CrossBackupPeriod'] = request.cross_backup_period
        if not DaraCore.is_null(request.cross_backup_type):
            query['CrossBackupType'] = request.cross_backup_type
        if not DaraCore.is_null(request.cross_log_retention_type):
            query['CrossLogRetentionType'] = request.cross_log_retention_type
        if not DaraCore.is_null(request.cross_log_retention_value):
            query['CrossLogRetentionValue'] = request.cross_log_retention_value
        if not DaraCore.is_null(request.cross_retention_type):
            query['CrossRetentionType'] = request.cross_retention_type
        if not DaraCore.is_null(request.cross_retention_value):
            query['CrossRetentionValue'] = request.cross_retention_value
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not DaraCore.is_null(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not DaraCore.is_null(request.enable_cross_log_backup):
            query['EnableCrossLogBackup'] = request.enable_cross_log_backup
        if not DaraCore.is_null(request.high_frequency_backup_retention):
            query['HighFrequencyBackupRetention'] = request.high_frequency_backup_retention
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not DaraCore.is_null(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not DaraCore.is_null(request.preserve_one_each_hour):
            query['PreserveOneEachHour'] = request.preserve_one_each_hour
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.snapshot_backup_type):
            query['SnapshotBackupType'] = request.snapshot_backup_type
        if not DaraCore.is_null(request.src_region):
            query['SrcRegion'] = request.src_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPolicy',
            version = '2015-12-01',
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

    def modify_dbinstance_attribute_with_options(
        self,
        request: main_models.ModifyDBInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbinstance_release_protection):
            query['DBInstanceReleaseProtection'] = request.dbinstance_release_protection
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
            action = 'ModifyDBInstanceAttribute',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_attribute_with_options_async(
        self,
        request: main_models.ModifyDBInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbinstance_release_protection):
            query['DBInstanceReleaseProtection'] = request.dbinstance_release_protection
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
            action = 'ModifyDBInstanceAttribute',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_attribute(
        self,
        request: main_models.ModifyDBInstanceAttributeRequest,
    ) -> main_models.ModifyDBInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_attribute_with_options(request, runtime)

    async def modify_dbinstance_attribute_async(
        self,
        request: main_models.ModifyDBInstanceAttributeRequest,
    ) -> main_models.ModifyDBInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_attribute_with_options_async(request, runtime)

    def modify_dbinstance_config_with_options(
        self,
        request: main_models.ModifyDBInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.config_value):
            query['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'ModifyDBInstanceConfig',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_config_with_options_async(
        self,
        request: main_models.ModifyDBInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.config_value):
            query['ConfigValue'] = request.config_value
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'ModifyDBInstanceConfig',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_config(
        self,
        request: main_models.ModifyDBInstanceConfigRequest,
    ) -> main_models.ModifyDBInstanceConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_config_with_options(request, runtime)

    async def modify_dbinstance_config_async(
        self,
        request: main_models.ModifyDBInstanceConfigRequest,
    ) -> main_models.ModifyDBInstanceConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_config_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: main_models.ModifyDBInstanceConnectionStringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceConnectionStringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.new_connection_string):
            query['NewConnectionString'] = request.new_connection_string
        if not DaraCore.is_null(request.new_port):
            query['NewPort'] = request.new_port
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'ModifyDBInstanceConnectionString',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: main_models.ModifyDBInstanceConnectionStringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceConnectionStringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.new_connection_string):
            query['NewConnectionString'] = request.new_connection_string
        if not DaraCore.is_null(request.new_port):
            query['NewPort'] = request.new_port
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'ModifyDBInstanceConnectionString',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_connection_string(
        self,
        request: main_models.ModifyDBInstanceConnectionStringRequest,
    ) -> main_models.ModifyDBInstanceConnectionStringResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    async def modify_dbinstance_connection_string_async(
        self,
        request: main_models.ModifyDBInstanceConnectionStringRequest,
    ) -> main_models.ModifyDBInstanceConnectionStringResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_connection_string_with_options_async(request, runtime)

    def modify_dbinstance_description_with_options(
        self,
        request: main_models.ModifyDBInstanceDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'ModifyDBInstanceDescription',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_description_with_options_async(
        self,
        request: main_models.ModifyDBInstanceDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'ModifyDBInstanceDescription',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_description(
        self,
        request: main_models.ModifyDBInstanceDescriptionRequest,
    ) -> main_models.ModifyDBInstanceDescriptionResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    async def modify_dbinstance_description_async(
        self,
        request: main_models.ModifyDBInstanceDescriptionRequest,
    ) -> main_models.ModifyDBInstanceDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_description_with_options_async(request, runtime)

    def modify_dbinstance_disk_type_with_options(
        self,
        request: main_models.ModifyDBInstanceDiskTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceDiskTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.db_instance_storage_type):
            query['DbInstanceStorageType'] = request.db_instance_storage_type
        if not DaraCore.is_null(request.extra_param):
            query['ExtraParam'] = request.extra_param
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceDiskType',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceDiskTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_disk_type_with_options_async(
        self,
        request: main_models.ModifyDBInstanceDiskTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceDiskTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.db_instance_storage_type):
            query['DbInstanceStorageType'] = request.db_instance_storage_type
        if not DaraCore.is_null(request.extra_param):
            query['ExtraParam'] = request.extra_param
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.provisioned_iops):
            query['ProvisionedIops'] = request.provisioned_iops
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceDiskType',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceDiskTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_disk_type(
        self,
        request: main_models.ModifyDBInstanceDiskTypeRequest,
    ) -> main_models.ModifyDBInstanceDiskTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_disk_type_with_options(request, runtime)

    async def modify_dbinstance_disk_type_async(
        self,
        request: main_models.ModifyDBInstanceDiskTypeRequest,
    ) -> main_models.ModifyDBInstanceDiskTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_disk_type_with_options_async(request, runtime)

    def modify_dbinstance_maintain_time_with_options(
        self,
        request: main_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceMaintainTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceMaintainTime',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_maintain_time_with_options_async(
        self,
        request: main_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceMaintainTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceMaintainTime',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_maintain_time(
        self,
        request: main_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> main_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    async def modify_dbinstance_maintain_time_async(
        self,
        request: main_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> main_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_maintain_time_with_options_async(request, runtime)

    def modify_dbinstance_monitor_with_options(
        self,
        request: main_models.ModifyDBInstanceMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
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
            action = 'ModifyDBInstanceMonitor',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_monitor_with_options_async(
        self,
        request: main_models.ModifyDBInstanceMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
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
            action = 'ModifyDBInstanceMonitor',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_monitor(
        self,
        request: main_models.ModifyDBInstanceMonitorRequest,
    ) -> main_models.ModifyDBInstanceMonitorResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_monitor_with_options(request, runtime)

    async def modify_dbinstance_monitor_async(
        self,
        request: main_models.ModifyDBInstanceMonitorRequest,
    ) -> main_models.ModifyDBInstanceMonitorResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_monitor_with_options_async(request, runtime)

    def modify_dbinstance_net_expire_time_with_options(
        self,
        request: main_models.ModifyDBInstanceNetExpireTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceNetExpireTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.classic_expend_expired_days):
            query['ClassicExpendExpiredDays'] = request.classic_expend_expired_days
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'ModifyDBInstanceNetExpireTime',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceNetExpireTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_net_expire_time_with_options_async(
        self,
        request: main_models.ModifyDBInstanceNetExpireTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceNetExpireTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.classic_expend_expired_days):
            query['ClassicExpendExpiredDays'] = request.classic_expend_expired_days
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'ModifyDBInstanceNetExpireTime',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceNetExpireTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_net_expire_time(
        self,
        request: main_models.ModifyDBInstanceNetExpireTimeRequest,
    ) -> main_models.ModifyDBInstanceNetExpireTimeResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_net_expire_time_with_options(request, runtime)

    async def modify_dbinstance_net_expire_time_async(
        self,
        request: main_models.ModifyDBInstanceNetExpireTimeRequest,
    ) -> main_models.ModifyDBInstanceNetExpireTimeResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_net_expire_time_with_options_async(request, runtime)

    def modify_dbinstance_network_type_with_options(
        self,
        request: main_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceNetworkTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.retain_classic):
            query['RetainClassic'] = request.retain_classic
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
            action = 'ModifyDBInstanceNetworkType',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceNetworkTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_network_type_with_options_async(
        self,
        request: main_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceNetworkTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.classic_expired_days):
            query['ClassicExpiredDays'] = request.classic_expired_days
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.retain_classic):
            query['RetainClassic'] = request.retain_classic
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
            action = 'ModifyDBInstanceNetworkType',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceNetworkTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_network_type(
        self,
        request: main_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> main_models.ModifyDBInstanceNetworkTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_network_type_with_options(request, runtime)

    async def modify_dbinstance_network_type_async(
        self,
        request: main_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> main_models.ModifyDBInstanceNetworkTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_network_type_with_options_async(request, runtime)

    def modify_dbinstance_sslwith_options(
        self,
        request: main_models.ModifyDBInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.force_encryption):
            query['ForceEncryption'] = request.force_encryption
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sslaction):
            query['SSLAction'] = request.sslaction
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceSSL',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_sslwith_options_async(
        self,
        request: main_models.ModifyDBInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.force_encryption):
            query['ForceEncryption'] = request.force_encryption
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.sslaction):
            query['SSLAction'] = request.sslaction
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceSSL',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_ssl(
        self,
        request: main_models.ModifyDBInstanceSSLRequest,
    ) -> main_models.ModifyDBInstanceSSLResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_sslwith_options(request, runtime)

    async def modify_dbinstance_ssl_async(
        self,
        request: main_models.ModifyDBInstanceSSLRequest,
    ) -> main_models.ModifyDBInstanceSSLResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_sslwith_options_async(request, runtime)

    def modify_dbinstance_spec_with_options(
        self,
        request: main_models.ModifyDBInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.extra_param):
            query['ExtraParam'] = request.extra_param
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.search_node_class):
            query['SearchNodeClass'] = request.search_node_class
        if not DaraCore.is_null(request.search_node_count):
            query['SearchNodeCount'] = request.search_node_count
        if not DaraCore.is_null(request.search_node_storage):
            query['SearchNodeStorage'] = request.search_node_storage
        if not DaraCore.is_null(request.target_hidden_zone_id):
            query['TargetHiddenZoneId'] = request.target_hidden_zone_id
        if not DaraCore.is_null(request.target_secondary_zone_id):
            query['TargetSecondaryZoneId'] = request.target_secondary_zone_id
        if not DaraCore.is_null(request.target_vswitch_id):
            query['TargetVswitchId'] = request.target_vswitch_id
        if not DaraCore.is_null(request.target_zone_id):
            query['TargetZoneId'] = request.target_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceSpec',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_spec_with_options_async(
        self,
        request: main_models.ModifyDBInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.dbinstance_storage):
            query['DBInstanceStorage'] = request.dbinstance_storage
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.extra_param):
            query['ExtraParam'] = request.extra_param
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not DaraCore.is_null(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.search_node_class):
            query['SearchNodeClass'] = request.search_node_class
        if not DaraCore.is_null(request.search_node_count):
            query['SearchNodeCount'] = request.search_node_count
        if not DaraCore.is_null(request.search_node_storage):
            query['SearchNodeStorage'] = request.search_node_storage
        if not DaraCore.is_null(request.target_hidden_zone_id):
            query['TargetHiddenZoneId'] = request.target_hidden_zone_id
        if not DaraCore.is_null(request.target_secondary_zone_id):
            query['TargetSecondaryZoneId'] = request.target_secondary_zone_id
        if not DaraCore.is_null(request.target_vswitch_id):
            query['TargetVswitchId'] = request.target_vswitch_id
        if not DaraCore.is_null(request.target_zone_id):
            query['TargetZoneId'] = request.target_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceSpec',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_spec(
        self,
        request: main_models.ModifyDBInstanceSpecRequest,
    ) -> main_models.ModifyDBInstanceSpecResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_spec_with_options(request, runtime)

    async def modify_dbinstance_spec_async(
        self,
        request: main_models.ModifyDBInstanceSpecRequest,
    ) -> main_models.ModifyDBInstanceSpecResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_spec_with_options_async(request, runtime)

    def modify_dbinstance_tdewith_options(
        self,
        request: main_models.ModifyDBInstanceTDERequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceTDEResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.encryptor_name):
            query['EncryptorName'] = request.encryptor_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_arn):
            query['RoleARN'] = request.role_arn
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not DaraCore.is_null(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceTDE',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_tdewith_options_async(
        self,
        request: main_models.ModifyDBInstanceTDERequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceTDEResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.encryptor_name):
            query['EncryptorName'] = request.encryptor_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_arn):
            query['RoleARN'] = request.role_arn
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not DaraCore.is_null(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceTDE',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceTDEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_tde(
        self,
        request: main_models.ModifyDBInstanceTDERequest,
    ) -> main_models.ModifyDBInstanceTDEResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_tdewith_options(request, runtime)

    async def modify_dbinstance_tde_async(
        self,
        request: main_models.ModifyDBInstanceTDERequest,
    ) -> main_models.ModifyDBInstanceTDEResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_tdewith_options_async(request, runtime)

    def modify_global_security_ipgroup_with_options(
        self,
        request: main_models.ModifyGlobalSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGlobalSecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gip_list):
            query['GIpList'] = request.gip_list
        if not DaraCore.is_null(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action = 'ModifyGlobalSecurityIPGroup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGlobalSecurityIPGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_security_ipgroup_with_options_async(
        self,
        request: main_models.ModifyGlobalSecurityIPGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGlobalSecurityIPGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gip_list):
            query['GIpList'] = request.gip_list
        if not DaraCore.is_null(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action = 'ModifyGlobalSecurityIPGroup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGlobalSecurityIPGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_security_ipgroup(
        self,
        request: main_models.ModifyGlobalSecurityIPGroupRequest,
    ) -> main_models.ModifyGlobalSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_global_security_ipgroup_with_options(request, runtime)

    async def modify_global_security_ipgroup_async(
        self,
        request: main_models.ModifyGlobalSecurityIPGroupRequest,
    ) -> main_models.ModifyGlobalSecurityIPGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_global_security_ipgroup_with_options_async(request, runtime)

    def modify_global_security_ipgroup_name_with_options(
        self,
        request: main_models.ModifyGlobalSecurityIPGroupNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGlobalSecurityIPGroupNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action = 'ModifyGlobalSecurityIPGroupName',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGlobalSecurityIPGroupNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_security_ipgroup_name_with_options_async(
        self,
        request: main_models.ModifyGlobalSecurityIPGroupNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGlobalSecurityIPGroupNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_ig_name):
            query['GlobalIgName'] = request.global_ig_name
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action = 'ModifyGlobalSecurityIPGroupName',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGlobalSecurityIPGroupNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_security_ipgroup_name(
        self,
        request: main_models.ModifyGlobalSecurityIPGroupNameRequest,
    ) -> main_models.ModifyGlobalSecurityIPGroupNameResponse:
        runtime = RuntimeOptions()
        return self.modify_global_security_ipgroup_name_with_options(request, runtime)

    async def modify_global_security_ipgroup_name_async(
        self,
        request: main_models.ModifyGlobalSecurityIPGroupNameRequest,
    ) -> main_models.ModifyGlobalSecurityIPGroupNameResponse:
        runtime = RuntimeOptions()
        return await self.modify_global_security_ipgroup_name_with_options_async(request, runtime)

    def modify_global_security_ipgroup_relation_with_options(
        self,
        request: main_models.ModifyGlobalSecurityIPGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGlobalSecurityIPGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action = 'ModifyGlobalSecurityIPGroupRelation',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGlobalSecurityIPGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_global_security_ipgroup_relation_with_options_async(
        self,
        request: main_models.ModifyGlobalSecurityIPGroupRelationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGlobalSecurityIPGroupRelationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.global_security_group_id):
            query['GlobalSecurityGroupId'] = request.global_security_group_id
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
            action = 'ModifyGlobalSecurityIPGroupRelation',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGlobalSecurityIPGroupRelationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_global_security_ipgroup_relation(
        self,
        request: main_models.ModifyGlobalSecurityIPGroupRelationRequest,
    ) -> main_models.ModifyGlobalSecurityIPGroupRelationResponse:
        runtime = RuntimeOptions()
        return self.modify_global_security_ipgroup_relation_with_options(request, runtime)

    async def modify_global_security_ipgroup_relation_async(
        self,
        request: main_models.ModifyGlobalSecurityIPGroupRelationRequest,
    ) -> main_models.ModifyGlobalSecurityIPGroupRelationResponse:
        runtime = RuntimeOptions()
        return await self.modify_global_security_ipgroup_relation_with_options_async(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(
        self,
        request: main_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceAutoRenewalAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
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
            action = 'ModifyInstanceAutoRenewalAttribute',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceAutoRenewalAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_auto_renewal_attribute_with_options_async(
        self,
        request: main_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceAutoRenewalAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
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
            action = 'ModifyInstanceAutoRenewalAttribute',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceAutoRenewalAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_auto_renewal_attribute(
        self,
        request: main_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> main_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    async def modify_instance_auto_renewal_attribute_async(
        self,
        request: main_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> main_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def modify_instance_vpc_auth_mode_with_options(
        self,
        request: main_models.ModifyInstanceVpcAuthModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceVpcAuthModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vpc_auth_mode):
            query['VpcAuthMode'] = request.vpc_auth_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceVpcAuthMode',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceVpcAuthModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_vpc_auth_mode_with_options_async(
        self,
        request: main_models.ModifyInstanceVpcAuthModeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceVpcAuthModeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.vpc_auth_mode):
            query['VpcAuthMode'] = request.vpc_auth_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceVpcAuthMode',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceVpcAuthModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_vpc_auth_mode(
        self,
        request: main_models.ModifyInstanceVpcAuthModeRequest,
    ) -> main_models.ModifyInstanceVpcAuthModeResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_vpc_auth_mode_with_options(request, runtime)

    async def modify_instance_vpc_auth_mode_async(
        self,
        request: main_models.ModifyInstanceVpcAuthModeRequest,
    ) -> main_models.ModifyInstanceVpcAuthModeResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_vpc_auth_mode_with_options_async(request, runtime)

    def modify_node_spec_with_options(
        self,
        request: main_models.ModifyNodeSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodeSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.from_app):
            query['FromApp'] = request.from_app
        if not DaraCore.is_null(request.node_class):
            query['NodeClass'] = request.node_class
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.node_storage):
            query['NodeStorage'] = request.node_storage
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.target_hidden_zone_id):
            query['TargetHiddenZoneId'] = request.target_hidden_zone_id
        if not DaraCore.is_null(request.target_secondary_zone_id):
            query['TargetSecondaryZoneId'] = request.target_secondary_zone_id
        if not DaraCore.is_null(request.target_vswitch_id):
            query['TargetVswitchId'] = request.target_vswitch_id
        if not DaraCore.is_null(request.target_zone_id):
            query['TargetZoneId'] = request.target_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodeSpec',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodeSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_spec_with_options_async(
        self,
        request: main_models.ModifyNodeSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodeSpecResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.from_app):
            query['FromApp'] = request.from_app
        if not DaraCore.is_null(request.node_class):
            query['NodeClass'] = request.node_class
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.node_storage):
            query['NodeStorage'] = request.node_storage
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.readonly_replicas):
            query['ReadonlyReplicas'] = request.readonly_replicas
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.target_hidden_zone_id):
            query['TargetHiddenZoneId'] = request.target_hidden_zone_id
        if not DaraCore.is_null(request.target_secondary_zone_id):
            query['TargetSecondaryZoneId'] = request.target_secondary_zone_id
        if not DaraCore.is_null(request.target_vswitch_id):
            query['TargetVswitchId'] = request.target_vswitch_id
        if not DaraCore.is_null(request.target_zone_id):
            query['TargetZoneId'] = request.target_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodeSpec',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodeSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_spec(
        self,
        request: main_models.ModifyNodeSpecRequest,
    ) -> main_models.ModifyNodeSpecResponse:
        runtime = RuntimeOptions()
        return self.modify_node_spec_with_options(request, runtime)

    async def modify_node_spec_async(
        self,
        request: main_models.ModifyNodeSpecRequest,
    ) -> main_models.ModifyNodeSpecResponse:
        runtime = RuntimeOptions()
        return await self.modify_node_spec_with_options_async(request, runtime)

    def modify_node_spec_batch_with_options(
        self,
        request: main_models.ModifyNodeSpecBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodeSpecBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.nodes_info):
            query['NodesInfo'] = request.nodes_info
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
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
        if not DaraCore.is_null(request.target_hidden_zone_id):
            query['TargetHiddenZoneId'] = request.target_hidden_zone_id
        if not DaraCore.is_null(request.target_secondary_zone_id):
            query['TargetSecondaryZoneId'] = request.target_secondary_zone_id
        if not DaraCore.is_null(request.target_vswitch_id):
            query['TargetVswitchId'] = request.target_vswitch_id
        if not DaraCore.is_null(request.target_zone_id):
            query['TargetZoneId'] = request.target_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodeSpecBatch',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodeSpecBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_node_spec_batch_with_options_async(
        self,
        request: main_models.ModifyNodeSpecBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyNodeSpecBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.nodes_info):
            query['NodesInfo'] = request.nodes_info
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
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
        if not DaraCore.is_null(request.target_hidden_zone_id):
            query['TargetHiddenZoneId'] = request.target_hidden_zone_id
        if not DaraCore.is_null(request.target_secondary_zone_id):
            query['TargetSecondaryZoneId'] = request.target_secondary_zone_id
        if not DaraCore.is_null(request.target_vswitch_id):
            query['TargetVswitchId'] = request.target_vswitch_id
        if not DaraCore.is_null(request.target_zone_id):
            query['TargetZoneId'] = request.target_zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyNodeSpecBatch',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyNodeSpecBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_node_spec_batch(
        self,
        request: main_models.ModifyNodeSpecBatchRequest,
    ) -> main_models.ModifyNodeSpecBatchResponse:
        runtime = RuntimeOptions()
        return self.modify_node_spec_batch_with_options(request, runtime)

    async def modify_node_spec_batch_async(
        self,
        request: main_models.ModifyNodeSpecBatchRequest,
    ) -> main_models.ModifyNodeSpecBatchResponse:
        runtime = RuntimeOptions()
        return await self.modify_node_spec_batch_with_options_async(request, runtime)

    def modify_parameters_with_options(
        self,
        request: main_models.ModifyParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyParameters',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_parameters_with_options_async(
        self,
        request: main_models.ModifyParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyParameters',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_parameters(
        self,
        request: main_models.ModifyParametersRequest,
    ) -> main_models.ModifyParametersResponse:
        runtime = RuntimeOptions()
        return self.modify_parameters_with_options(request, runtime)

    async def modify_parameters_async(
        self,
        request: main_models.ModifyParametersRequest,
    ) -> main_models.ModifyParametersResponse:
        runtime = RuntimeOptions()
        return await self.modify_parameters_with_options_async(request, runtime)

    def modify_resource_group_with_options(
        self,
        request: main_models.ModifyResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyResourceGroup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_group_with_options_async(
        self,
        request: main_models.ModifyResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyResourceGroup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_resource_group(
        self,
        request: main_models.ModifyResourceGroupRequest,
    ) -> main_models.ModifyResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_resource_group_with_options(request, runtime)

    async def modify_resource_group_async(
        self,
        request: main_models.ModifyResourceGroupRequest,
    ) -> main_models.ModifyResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_resource_group_with_options_async(request, runtime)

    def modify_security_group_configuration_with_options(
        self,
        request: main_models.ModifySecurityGroupConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityGroupConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityGroupConfiguration',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityGroupConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_group_configuration_with_options_async(
        self,
        request: main_models.ModifySecurityGroupConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityGroupConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityGroupConfiguration',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityGroupConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_group_configuration(
        self,
        request: main_models.ModifySecurityGroupConfigurationRequest,
    ) -> main_models.ModifySecurityGroupConfigurationResponse:
        runtime = RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    async def modify_security_group_configuration_async(
        self,
        request: main_models.ModifySecurityGroupConfigurationRequest,
    ) -> main_models.ModifySecurityGroupConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.modify_security_group_configuration_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: main_models.ModifySecurityIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
        if not DaraCore.is_null(request.security_ip_group_attribute):
            query['SecurityIpGroupAttribute'] = request.security_ip_group_attribute
        if not DaraCore.is_null(request.security_ip_group_name):
            query['SecurityIpGroupName'] = request.security_ip_group_name
        if not DaraCore.is_null(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityIps',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityIpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: main_models.ModifySecurityIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
        if not DaraCore.is_null(request.security_ip_group_attribute):
            query['SecurityIpGroupAttribute'] = request.security_ip_group_attribute
        if not DaraCore.is_null(request.security_ip_group_name):
            query['SecurityIpGroupName'] = request.security_ip_group_name
        if not DaraCore.is_null(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityIps',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityIpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_ips(
        self,
        request: main_models.ModifySecurityIpsRequest,
    ) -> main_models.ModifySecurityIpsResponse:
        runtime = RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: main_models.ModifySecurityIpsRequest,
    ) -> main_models.ModifySecurityIpsResponse:
        runtime = RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def modify_srv_network_address_with_options(
        self,
        request: main_models.ModifySrvNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySrvNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.new_connection_string):
            query['NewConnectionString'] = request.new_connection_string
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
            action = 'ModifySrvNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySrvNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_srv_network_address_with_options_async(
        self,
        request: main_models.ModifySrvNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySrvNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.new_connection_string):
            query['NewConnectionString'] = request.new_connection_string
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
            action = 'ModifySrvNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySrvNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_srv_network_address(
        self,
        request: main_models.ModifySrvNetworkAddressRequest,
    ) -> main_models.ModifySrvNetworkAddressResponse:
        runtime = RuntimeOptions()
        return self.modify_srv_network_address_with_options(request, runtime)

    async def modify_srv_network_address_async(
        self,
        request: main_models.ModifySrvNetworkAddressRequest,
    ) -> main_models.ModifySrvNetworkAddressResponse:
        runtime = RuntimeOptions()
        return await self.modify_srv_network_address_with_options_async(request, runtime)

    def modify_task_info_with_options(
        self,
        request: main_models.ModifyTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_params):
            query['ActionParams'] = request.action_params
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.step_name):
            query['StepName'] = request.step_name
        if not DaraCore.is_null(request.task_action):
            query['TaskAction'] = request.task_action
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTaskInfo',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_task_info_with_options_async(
        self,
        request: main_models.ModifyTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_params):
            query['ActionParams'] = request.action_params
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.step_name):
            query['StepName'] = request.step_name
        if not DaraCore.is_null(request.task_action):
            query['TaskAction'] = request.task_action
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyTaskInfo',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_task_info(
        self,
        request: main_models.ModifyTaskInfoRequest,
    ) -> main_models.ModifyTaskInfoResponse:
        runtime = RuntimeOptions()
        return self.modify_task_info_with_options(request, runtime)

    async def modify_task_info_async(
        self,
        request: main_models.ModifyTaskInfoRequest,
    ) -> main_models.ModifyTaskInfoResponse:
        runtime = RuntimeOptions()
        return await self.modify_task_info_with_options_async(request, runtime)

    def release_node_private_network_address_with_options(
        self,
        request: main_models.ReleaseNodePrivateNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseNodePrivateNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'ReleaseNodePrivateNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseNodePrivateNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_node_private_network_address_with_options_async(
        self,
        request: main_models.ReleaseNodePrivateNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseNodePrivateNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'ReleaseNodePrivateNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseNodePrivateNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_node_private_network_address(
        self,
        request: main_models.ReleaseNodePrivateNetworkAddressRequest,
    ) -> main_models.ReleaseNodePrivateNetworkAddressResponse:
        runtime = RuntimeOptions()
        return self.release_node_private_network_address_with_options(request, runtime)

    async def release_node_private_network_address_async(
        self,
        request: main_models.ReleaseNodePrivateNetworkAddressRequest,
    ) -> main_models.ReleaseNodePrivateNetworkAddressResponse:
        runtime = RuntimeOptions()
        return await self.release_node_private_network_address_with_options_async(request, runtime)

    def release_public_network_address_with_options(
        self,
        request: main_models.ReleasePublicNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleasePublicNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'ReleasePublicNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleasePublicNetworkAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_public_network_address_with_options_async(
        self,
        request: main_models.ReleasePublicNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleasePublicNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_type):
            query['ConnectionType'] = request.connection_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
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
            action = 'ReleasePublicNetworkAddress',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleasePublicNetworkAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_public_network_address(
        self,
        request: main_models.ReleasePublicNetworkAddressRequest,
    ) -> main_models.ReleasePublicNetworkAddressResponse:
        runtime = RuntimeOptions()
        return self.release_public_network_address_with_options(request, runtime)

    async def release_public_network_address_async(
        self,
        request: main_models.ReleasePublicNetworkAddressRequest,
    ) -> main_models.ReleasePublicNetworkAddressResponse:
        runtime = RuntimeOptions()
        return await self.release_public_network_address_with_options_async(request, runtime)

    def renew_dbinstance_with_options(
        self,
        request: main_models.RenewDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewDBInstance',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_dbinstance_with_options_async(
        self,
        request: main_models.RenewDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewDBInstance',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_dbinstance(
        self,
        request: main_models.RenewDBInstanceRequest,
    ) -> main_models.RenewDBInstanceResponse:
        runtime = RuntimeOptions()
        return self.renew_dbinstance_with_options(request, runtime)

    async def renew_dbinstance_async(
        self,
        request: main_models.RenewDBInstanceRequest,
    ) -> main_models.RenewDBInstanceResponse:
        runtime = RuntimeOptions()
        return await self.renew_dbinstance_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            version = '2015-12-01',
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

    def restart_dbinstance_with_options(
        self,
        request: main_models.RestartDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartDBInstance',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dbinstance_with_options_async(
        self,
        request: main_models.RestartDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartDBInstance',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dbinstance(
        self,
        request: main_models.RestartDBInstanceRequest,
    ) -> main_models.RestartDBInstanceResponse:
        runtime = RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: main_models.RestartDBInstanceRequest,
    ) -> main_models.RestartDBInstanceResponse:
        runtime = RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def restart_node_with_options(
        self,
        request: main_models.RestartNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartNode',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_node_with_options_async(
        self,
        request: main_models.RestartNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_id):
            query['RoleId'] = request.role_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartNode',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_node(
        self,
        request: main_models.RestartNodeRequest,
    ) -> main_models.RestartNodeResponse:
        runtime = RuntimeOptions()
        return self.restart_node_with_options(request, runtime)

    async def restart_node_async(
        self,
        request: main_models.RestartNodeRequest,
    ) -> main_models.RestartNodeResponse:
        runtime = RuntimeOptions()
        return await self.restart_node_with_options_async(request, runtime)

    def switch_dbinstance_hawith_options(
        self,
        request: main_models.SwitchDBInstanceHARequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchDBInstanceHAResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_ids):
            query['RoleIds'] = request.role_ids
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchDBInstanceHA',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchDBInstanceHAResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_dbinstance_hawith_options_async(
        self,
        request: main_models.SwitchDBInstanceHARequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchDBInstanceHAResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.role_ids):
            query['RoleIds'] = request.role_ids
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchDBInstanceHA',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchDBInstanceHAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_dbinstance_ha(
        self,
        request: main_models.SwitchDBInstanceHARequest,
    ) -> main_models.SwitchDBInstanceHAResponse:
        runtime = RuntimeOptions()
        return self.switch_dbinstance_hawith_options(request, runtime)

    async def switch_dbinstance_ha_async(
        self,
        request: main_models.SwitchDBInstanceHARequest,
    ) -> main_models.SwitchDBInstanceHAResponse:
        runtime = RuntimeOptions()
        return await self.switch_dbinstance_hawith_options_async(request, runtime)

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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version = '2015-12-01',
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

    def transfer_cluster_backup_with_options(
        self,
        request: main_models.TransferClusterBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferClusterBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'TransferClusterBackup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferClusterBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_cluster_backup_with_options_async(
        self,
        request: main_models.TransferClusterBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransferClusterBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'TransferClusterBackup',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferClusterBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_cluster_backup(
        self,
        request: main_models.TransferClusterBackupRequest,
    ) -> main_models.TransferClusterBackupResponse:
        runtime = RuntimeOptions()
        return self.transfer_cluster_backup_with_options(request, runtime)

    async def transfer_cluster_backup_async(
        self,
        request: main_models.TransferClusterBackupRequest,
    ) -> main_models.TransferClusterBackupResponse:
        runtime = RuntimeOptions()
        return await self.transfer_cluster_backup_with_options_async(request, runtime)

    def transform_instance_charge_type_with_options(
        self,
        request: main_models.TransformInstanceChargeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransformInstanceChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransformInstanceChargeType',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransformInstanceChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def transform_instance_charge_type_with_options_async(
        self,
        request: main_models.TransformInstanceChargeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransformInstanceChargeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransformInstanceChargeType',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransformInstanceChargeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transform_instance_charge_type(
        self,
        request: main_models.TransformInstanceChargeTypeRequest,
    ) -> main_models.TransformInstanceChargeTypeResponse:
        runtime = RuntimeOptions()
        return self.transform_instance_charge_type_with_options(request, runtime)

    async def transform_instance_charge_type_async(
        self,
        request: main_models.TransformInstanceChargeTypeRequest,
    ) -> main_models.TransformInstanceChargeTypeResponse:
        runtime = RuntimeOptions()
        return await self.transform_instance_charge_type_with_options_async(request, runtime)

    def transform_to_pre_paid_with_options(
        self,
        request: main_models.TransformToPrePaidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransformToPrePaidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransformToPrePaid',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransformToPrePaidResponse(),
            self.call_api(params, req, runtime)
        )

    async def transform_to_pre_paid_with_options_async(
        self,
        request: main_models.TransformToPrePaidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TransformToPrePaidResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.business_info):
            query['BusinessInfo'] = request.business_info
        if not DaraCore.is_null(request.coupon_no):
            query['CouponNo'] = request.coupon_no
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TransformToPrePaid',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransformToPrePaidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transform_to_pre_paid(
        self,
        request: main_models.TransformToPrePaidRequest,
    ) -> main_models.TransformToPrePaidResponse:
        runtime = RuntimeOptions()
        return self.transform_to_pre_paid_with_options(request, runtime)

    async def transform_to_pre_paid_async(
        self,
        request: main_models.TransformToPrePaidRequest,
    ) -> main_models.TransformToPrePaidResponse:
        runtime = RuntimeOptions()
        return await self.transform_to_pre_paid_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version = '2015-12-01',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
            version = '2015-12-01',
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

    def upgrade_dbinstance_engine_version_with_options(
        self,
        request: main_models.UpgradeDBInstanceEngineVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeDBInstanceEngineVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBInstanceEngineVersion',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeDBInstanceEngineVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbinstance_engine_version_with_options_async(
        self,
        request: main_models.UpgradeDBInstanceEngineVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeDBInstanceEngineVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBInstanceEngineVersion',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeDBInstanceEngineVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbinstance_engine_version(
        self,
        request: main_models.UpgradeDBInstanceEngineVersionRequest,
    ) -> main_models.UpgradeDBInstanceEngineVersionResponse:
        runtime = RuntimeOptions()
        return self.upgrade_dbinstance_engine_version_with_options(request, runtime)

    async def upgrade_dbinstance_engine_version_async(
        self,
        request: main_models.UpgradeDBInstanceEngineVersionRequest,
    ) -> main_models.UpgradeDBInstanceEngineVersionResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_dbinstance_engine_version_with_options_async(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(
        self,
        request: main_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeDBInstanceKernelVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBInstanceKernelVersion',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeDBInstanceKernelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbinstance_kernel_version_with_options_async(
        self,
        request: main_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeDBInstanceKernelVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBInstanceKernelVersion',
            version = '2015-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeDBInstanceKernelVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbinstance_kernel_version(
        self,
        request: main_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> main_models.UpgradeDBInstanceKernelVersionResponse:
        runtime = RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)

    async def upgrade_dbinstance_kernel_version_async(
        self,
        request: main_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> main_models.UpgradeDBInstanceKernelVersionResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_dbinstance_kernel_version_with_options_async(request, runtime)
