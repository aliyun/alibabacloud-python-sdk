# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_selectdb20230522 import models as main_models
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
        self._endpoint = self.get_endpoint('selectdb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allocate_instance_public_connection_with_options(
        self,
        request: main_models.AllocateInstancePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateInstancePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.net_type):
            query['NetType'] = request.net_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateInstancePublicConnection',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_instance_public_connection_with_options_async(
        self,
        request: main_models.AllocateInstancePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateInstancePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.net_type):
            query['NetType'] = request.net_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateInstancePublicConnection',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_instance_public_connection(
        self,
        request: main_models.AllocateInstancePublicConnectionRequest,
    ) -> main_models.AllocateInstancePublicConnectionResponse:
        runtime = RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    async def allocate_instance_public_connection_async(
        self,
        request: main_models.AllocateInstancePublicConnectionRequest,
    ) -> main_models.AllocateInstancePublicConnectionResponse:
        runtime = RuntimeOptions()
        return await self.allocate_instance_public_connection_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2023-05-22',
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

    def check_create_dbinstance_with_options(
        self,
        request: main_models.CheckCreateDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCreateDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
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
            action = 'CheckCreateDBInstance',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_create_dbinstance_with_options_async(
        self,
        request: main_models.CheckCreateDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCreateDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
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
            action = 'CheckCreateDBInstance',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCreateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_create_dbinstance(
        self,
        request: main_models.CheckCreateDBInstanceRequest,
    ) -> main_models.CheckCreateDBInstanceResponse:
        runtime = RuntimeOptions()
        return self.check_create_dbinstance_with_options(request, runtime)

    async def check_create_dbinstance_async(
        self,
        request: main_models.CheckCreateDBInstanceRequest,
    ) -> main_models.CheckCreateDBInstanceResponse:
        runtime = RuntimeOptions()
        return await self.check_create_dbinstance_with_options_async(request, runtime)

    def check_ip_exists_in_security_ip_list_with_options(
        self,
        request: main_models.CheckIpExistsInSecurityIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckIpExistsInSecurityIpListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckIpExistsInSecurityIpList',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckIpExistsInSecurityIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_ip_exists_in_security_ip_list_with_options_async(
        self,
        request: main_models.CheckIpExistsInSecurityIpListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckIpExistsInSecurityIpListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckIpExistsInSecurityIpList',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckIpExistsInSecurityIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_ip_exists_in_security_ip_list(
        self,
        request: main_models.CheckIpExistsInSecurityIpListRequest,
    ) -> main_models.CheckIpExistsInSecurityIpListResponse:
        runtime = RuntimeOptions()
        return self.check_ip_exists_in_security_ip_list_with_options(request, runtime)

    async def check_ip_exists_in_security_ip_list_async(
        self,
        request: main_models.CheckIpExistsInSecurityIpListRequest,
    ) -> main_models.CheckIpExistsInSecurityIpListResponse:
        runtime = RuntimeOptions()
        return await self.check_ip_exists_in_security_ip_list_with_options_async(request, runtime)

    def check_service_linked_role_with_options(
        self,
        request: main_models.CheckServiceLinkedRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceLinkedRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRole',
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRole',
            version = '2023-05-22',
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

    def create_dbcluster_with_options(
        self,
        request: main_models.CreateDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.cluster_node_count):
            query['ClusterNodeCount'] = request.cluster_node_count
        if not DaraCore.is_null(request.cluster_node_type):
            query['ClusterNodeType'] = request.cluster_node_type
        if not DaraCore.is_null(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not DaraCore.is_null(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        body = {}
        if not DaraCore.is_null(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBCluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbcluster_with_options_async(
        self,
        request: main_models.CreateDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.cluster_node_count):
            query['ClusterNodeCount'] = request.cluster_node_count
        if not DaraCore.is_null(request.cluster_node_type):
            query['ClusterNodeType'] = request.cluster_node_type
        if not DaraCore.is_null(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not DaraCore.is_null(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not DaraCore.is_null(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        body = {}
        if not DaraCore.is_null(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBCluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbcluster(
        self,
        request: main_models.CreateDBClusterRequest,
    ) -> main_models.CreateDBClusterResponse:
        runtime = RuntimeOptions()
        return self.create_dbcluster_with_options(request, runtime)

    async def create_dbcluster_async(
        self,
        request: main_models.CreateDBClusterRequest,
    ) -> main_models.CreateDBClusterResponse:
        runtime = RuntimeOptions()
        return await self.create_dbcluster_with_options_async(request, runtime)

    def create_dbcluster_binding_with_options(
        self,
        request: main_models.CreateDBClusterBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBClusterBindingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbcluster_id_bak):
            query['DBClusterIdBak'] = request.dbcluster_id_bak
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBClusterBinding',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBClusterBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbcluster_binding_with_options_async(
        self,
        request: main_models.CreateDBClusterBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBClusterBindingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbcluster_id_bak):
            query['DBClusterIdBak'] = request.dbcluster_id_bak
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBClusterBinding',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBClusterBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbcluster_binding(
        self,
        request: main_models.CreateDBClusterBindingRequest,
    ) -> main_models.CreateDBClusterBindingResponse:
        runtime = RuntimeOptions()
        return self.create_dbcluster_binding_with_options(request, runtime)

    async def create_dbcluster_binding_async(
        self,
        request: main_models.CreateDBClusterBindingRequest,
    ) -> main_models.CreateDBClusterBindingResponse:
        runtime = RuntimeOptions()
        return await self.create_dbcluster_binding_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        tmp_req: main_models.CreateDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateDBInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.multi_zone):
            request.multi_zone_shrink = Utils.array_to_string_with_specified_style(tmp_req.multi_zone, 'MultiZone', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.add_vpcips):
            query['AddVPCIPs'] = request.add_vpcips
        if not DaraCore.is_null(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_node_count):
            query['ClusterNodeCount'] = request.cluster_node_count
        if not DaraCore.is_null(request.cluster_node_type):
            query['ClusterNodeType'] = request.cluster_node_type
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.deploy_scheme):
            query['DeployScheme'] = request.deploy_scheme
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.multi_zone_shrink):
            query['MultiZone'] = request.multi_zone_shrink
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not DaraCore.is_null(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBInstance',
            version = '2023-05-22',
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
        tmp_req: main_models.CreateDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateDBInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.multi_zone):
            request.multi_zone_shrink = Utils.array_to_string_with_specified_style(tmp_req.multi_zone, 'MultiZone', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.add_vpcips):
            query['AddVPCIPs'] = request.add_vpcips
        if not DaraCore.is_null(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_node_count):
            query['ClusterNodeCount'] = request.cluster_node_count
        if not DaraCore.is_null(request.cluster_node_type):
            query['ClusterNodeType'] = request.cluster_node_type
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_class):
            query['DBInstanceClass'] = request.dbinstance_class
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.deploy_scheme):
            query['DeployScheme'] = request.deploy_scheme
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.multi_zone_shrink):
            query['MultiZone'] = request.multi_zone_shrink
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not DaraCore.is_null(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        body = {}
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBInstance',
            version = '2023-05-22',
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

    def create_elastic_rule_with_options(
        self,
        request: main_models.CreateElasticRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateElasticRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_class):
            query['ClusterClass'] = request.cluster_class
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not DaraCore.is_null(request.elastic_rule_start_time):
            query['ElasticRuleStartTime'] = request.elastic_rule_start_time
        if not DaraCore.is_null(request.execution_period):
            query['ExecutionPeriod'] = request.execution_period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateElasticRule',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateElasticRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_elastic_rule_with_options_async(
        self,
        request: main_models.CreateElasticRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateElasticRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_class):
            query['ClusterClass'] = request.cluster_class
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not DaraCore.is_null(request.elastic_rule_start_time):
            query['ElasticRuleStartTime'] = request.elastic_rule_start_time
        if not DaraCore.is_null(request.execution_period):
            query['ExecutionPeriod'] = request.execution_period
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateElasticRule',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateElasticRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_elastic_rule(
        self,
        request: main_models.CreateElasticRuleRequest,
    ) -> main_models.CreateElasticRuleResponse:
        runtime = RuntimeOptions()
        return self.create_elastic_rule_with_options(request, runtime)

    async def create_elastic_rule_async(
        self,
        request: main_models.CreateElasticRuleRequest,
    ) -> main_models.CreateElasticRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_elastic_rule_with_options_async(request, runtime)

    def create_service_linked_role_for_select_dbwith_options(
        self,
        request: main_models.CreateServiceLinkedRoleForSelectDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleForSelectDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRoleForSelectDB',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleForSelectDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_for_select_dbwith_options_async(
        self,
        request: main_models.CreateServiceLinkedRoleForSelectDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceLinkedRoleForSelectDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceLinkedRoleForSelectDB',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceLinkedRoleForSelectDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role_for_select_db(
        self,
        request: main_models.CreateServiceLinkedRoleForSelectDBRequest,
    ) -> main_models.CreateServiceLinkedRoleForSelectDBResponse:
        runtime = RuntimeOptions()
        return self.create_service_linked_role_for_select_dbwith_options(request, runtime)

    async def create_service_linked_role_for_select_db_async(
        self,
        request: main_models.CreateServiceLinkedRoleForSelectDBRequest,
    ) -> main_models.CreateServiceLinkedRoleForSelectDBResponse:
        runtime = RuntimeOptions()
        return await self.create_service_linked_role_for_select_dbwith_options_async(request, runtime)

    def create_virtual_cluster_with_options(
        self,
        request: main_models.CreateVirtualClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVirtualClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_cluster_id):
            query['ActiveClusterId'] = request.active_cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.standby_cluster_id):
            query['StandbyClusterId'] = request.standby_cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVirtualCluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVirtualClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_virtual_cluster_with_options_async(
        self,
        request: main_models.CreateVirtualClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVirtualClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_cluster_id):
            query['ActiveClusterId'] = request.active_cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.standby_cluster_id):
            query['StandbyClusterId'] = request.standby_cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVirtualCluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVirtualClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_virtual_cluster(
        self,
        request: main_models.CreateVirtualClusterRequest,
    ) -> main_models.CreateVirtualClusterResponse:
        runtime = RuntimeOptions()
        return self.create_virtual_cluster_with_options(request, runtime)

    async def create_virtual_cluster_async(
        self,
        request: main_models.CreateVirtualClusterRequest,
    ) -> main_models.CreateVirtualClusterResponse:
        runtime = RuntimeOptions()
        return await self.create_virtual_cluster_with_options_async(request, runtime)

    def delete_dbcluster_with_options(
        self,
        request: main_models.DeleteDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBCluster',
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBCluster',
            version = '2023-05-22',
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

    def delete_dbcluster_binding_with_options(
        self,
        request: main_models.DeleteDBClusterBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBClusterBindingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbcluster_id_bak):
            query['DBClusterIdBak'] = request.dbcluster_id_bak
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBClusterBinding',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBClusterBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbcluster_binding_with_options_async(
        self,
        request: main_models.DeleteDBClusterBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBClusterBindingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbcluster_id_bak):
            query['DBClusterIdBak'] = request.dbcluster_id_bak
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBClusterBinding',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBClusterBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbcluster_binding(
        self,
        request: main_models.DeleteDBClusterBindingRequest,
    ) -> main_models.DeleteDBClusterBindingResponse:
        runtime = RuntimeOptions()
        return self.delete_dbcluster_binding_with_options(request, runtime)

    async def delete_dbcluster_binding_async(
        self,
        request: main_models.DeleteDBClusterBindingRequest,
    ) -> main_models.DeleteDBClusterBindingResponse:
        runtime = RuntimeOptions()
        return await self.delete_dbcluster_binding_with_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: main_models.DeleteDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBInstance',
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBInstance',
            version = '2023-05-22',
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

    def delete_elastic_rule_with_options(
        self,
        request: main_models.DeleteElasticRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteElasticRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteElasticRule',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteElasticRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_elastic_rule_with_options_async(
        self,
        request: main_models.DeleteElasticRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteElasticRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteElasticRule',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteElasticRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_elastic_rule(
        self,
        request: main_models.DeleteElasticRuleRequest,
    ) -> main_models.DeleteElasticRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_elastic_rule_with_options(request, runtime)

    async def delete_elastic_rule_async(
        self,
        request: main_models.DeleteElasticRuleRequest,
    ) -> main_models.DeleteElasticRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_elastic_rule_with_options_async(request, runtime)

    def delete_virtual_cluster_with_options(
        self,
        request: main_models.DeleteVirtualClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVirtualClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVirtualCluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVirtualClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_virtual_cluster_with_options_async(
        self,
        request: main_models.DeleteVirtualClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVirtualClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVirtualCluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVirtualClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_virtual_cluster(
        self,
        request: main_models.DeleteVirtualClusterRequest,
    ) -> main_models.DeleteVirtualClusterResponse:
        runtime = RuntimeOptions()
        return self.delete_virtual_cluster_with_options(request, runtime)

    async def delete_virtual_cluster_async(
        self,
        request: main_models.DeleteVirtualClusterRequest,
    ) -> main_models.DeleteVirtualClusterResponse:
        runtime = RuntimeOptions()
        return await self.delete_virtual_cluster_with_options_async(request, runtime)

    def describe_all_dbinstance_class_with_options(
        self,
        request: main_models.DescribeAllDBInstanceClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllDBInstanceClassResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllDBInstanceClass',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllDBInstanceClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_dbinstance_class_with_options_async(
        self,
        request: main_models.DescribeAllDBInstanceClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAllDBInstanceClassResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAllDBInstanceClass',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAllDBInstanceClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_dbinstance_class(
        self,
        request: main_models.DescribeAllDBInstanceClassRequest,
    ) -> main_models.DescribeAllDBInstanceClassResponse:
        runtime = RuntimeOptions()
        return self.describe_all_dbinstance_class_with_options(request, runtime)

    async def describe_all_dbinstance_class_async(
        self,
        request: main_models.DescribeAllDBInstanceClassRequest,
    ) -> main_models.DescribeAllDBInstanceClassResponse:
        runtime = RuntimeOptions()
        return await self.describe_all_dbinstance_class_with_options_async(request, runtime)

    def describe_dbcluster_config_with_options(
        self,
        request: main_models.DescribeDBClusterConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterConfig',
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterConfig',
            version = '2023-05-22',
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

    def describe_dbcluster_config_change_logs_with_options(
        self,
        request: main_models.DescribeDBClusterConfigChangeLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterConfigChangeLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterConfigChangeLogs',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterConfigChangeLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_config_change_logs_with_options_async(
        self,
        request: main_models.DescribeDBClusterConfigChangeLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterConfigChangeLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterConfigChangeLogs',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterConfigChangeLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_config_change_logs(
        self,
        request: main_models.DescribeDBClusterConfigChangeLogsRequest,
    ) -> main_models.DescribeDBClusterConfigChangeLogsResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_config_change_logs_with_options(request, runtime)

    async def describe_dbcluster_config_change_logs_async(
        self,
        request: main_models.DescribeDBClusterConfigChangeLogsRequest,
    ) -> main_models.DescribeDBClusterConfigChangeLogsResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_config_change_logs_with_options_async(request, runtime)

    def describe_dbcluster_storage_limitation_with_options(
        self,
        request: main_models.DescribeDBClusterStorageLimitationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterStorageLimitationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterStorageLimitation',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterStorageLimitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_storage_limitation_with_options_async(
        self,
        request: main_models.DescribeDBClusterStorageLimitationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBClusterStorageLimitationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBClusterStorageLimitation',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBClusterStorageLimitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_storage_limitation(
        self,
        request: main_models.DescribeDBClusterStorageLimitationRequest,
    ) -> main_models.DescribeDBClusterStorageLimitationResponse:
        runtime = RuntimeOptions()
        return self.describe_dbcluster_storage_limitation_with_options(request, runtime)

    async def describe_dbcluster_storage_limitation_async(
        self,
        request: main_models.DescribeDBClusterStorageLimitationRequest,
    ) -> main_models.DescribeDBClusterStorageLimitationResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbcluster_storage_limitation_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: main_models.DescribeDBInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceAttribute',
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceAttribute',
            version = '2023-05-22',
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

    def describe_dbinstance_net_info_with_options(
        self,
        request: main_models.DescribeDBInstanceNetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceNetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceNetInfo',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_net_info_with_options_async(
        self,
        request: main_models.DescribeDBInstanceNetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceNetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceNetInfo',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceNetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_net_info(
        self,
        request: main_models.DescribeDBInstanceNetInfoRequest,
    ) -> main_models.DescribeDBInstanceNetInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    async def describe_dbinstance_net_info_async(
        self,
        request: main_models.DescribeDBInstanceNetInfoRequest,
    ) -> main_models.DescribeDBInstanceNetInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_net_info_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        tmp_req: main_models.DescribeDBInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancesResponse:
        tmp_req.validate()
        request = main_models.DescribeDBInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not DaraCore.is_null(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstances',
            version = '2023-05-22',
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
        tmp_req: main_models.DescribeDBInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancesResponse:
        tmp_req.validate()
        request = main_models.DescribeDBInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not DaraCore.is_null(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not DaraCore.is_null(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstances',
            version = '2023-05-22',
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

    def describe_elastic_rules_with_options(
        self,
        request: main_models.DescribeElasticRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticRulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticRules',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_elastic_rules_with_options_async(
        self,
        request: main_models.DescribeElasticRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeElasticRulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeElasticRules',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeElasticRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_elastic_rules(
        self,
        request: main_models.DescribeElasticRulesRequest,
    ) -> main_models.DescribeElasticRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_elastic_rules_with_options(request, runtime)

    async def describe_elastic_rules_async(
        self,
        request: main_models.DescribeElasticRulesRequest,
    ) -> main_models.DescribeElasticRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_elastic_rules_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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

    def describe_security_iplist_with_options(
        self,
        request: main_models.DescribeSecurityIPListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityIPListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityIPList',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityIPListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_iplist_with_options_async(
        self,
        request: main_models.DescribeSecurityIPListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityIPListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityIPList',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityIPListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_iplist(
        self,
        request: main_models.DescribeSecurityIPListRequest,
    ) -> main_models.DescribeSecurityIPListResponse:
        runtime = RuntimeOptions()
        return self.describe_security_iplist_with_options(request, runtime)

    async def describe_security_iplist_async(
        self,
        request: main_models.DescribeSecurityIPListRequest,
    ) -> main_models.DescribeSecurityIPListResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_iplist_with_options_async(request, runtime)

    def describe_vswitches_with_options(
        self,
        request: main_models.DescribeVSwitchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVSwitchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVSwitches',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVSwitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: main_models.DescribeVSwitchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVSwitchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVSwitches',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVSwitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vswitches(
        self,
        request: main_models.DescribeVSwitchesRequest,
    ) -> main_models.DescribeVSwitchesResponse:
        runtime = RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    async def describe_vswitches_async(
        self,
        request: main_models.DescribeVSwitchesRequest,
    ) -> main_models.DescribeVSwitchesResponse:
        runtime = RuntimeOptions()
        return await self.describe_vswitches_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2023-05-22',
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

    def en_disable_scaling_rules_with_options(
        self,
        request: main_models.EnDisableScalingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnDisableScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_rules_enable):
            query['ScalingRulesEnable'] = request.scaling_rules_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnDisableScalingRules',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnDisableScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def en_disable_scaling_rules_with_options_async(
        self,
        request: main_models.EnDisableScalingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnDisableScalingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scaling_rules_enable):
            query['ScalingRulesEnable'] = request.scaling_rules_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnDisableScalingRules',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnDisableScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def en_disable_scaling_rules(
        self,
        request: main_models.EnDisableScalingRulesRequest,
    ) -> main_models.EnDisableScalingRulesResponse:
        runtime = RuntimeOptions()
        return self.en_disable_scaling_rules_with_options(request, runtime)

    async def en_disable_scaling_rules_async(
        self,
        request: main_models.EnDisableScalingRulesRequest,
    ) -> main_models.EnDisableScalingRulesResponse:
        runtime = RuntimeOptions()
        return await self.en_disable_scaling_rules_with_options_async(request, runtime)

    def get_create_becluster_inquiry_with_options(
        self,
        request: main_models.GetCreateBEClusterInquiryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCreateBEClusterInquiryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCreateBEClusterInquiry',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCreateBEClusterInquiryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_create_becluster_inquiry_with_options_async(
        self,
        request: main_models.GetCreateBEClusterInquiryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCreateBEClusterInquiryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCreateBEClusterInquiry',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCreateBEClusterInquiryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_create_becluster_inquiry(
        self,
        request: main_models.GetCreateBEClusterInquiryRequest,
    ) -> main_models.GetCreateBEClusterInquiryResponse:
        runtime = RuntimeOptions()
        return self.get_create_becluster_inquiry_with_options(request, runtime)

    async def get_create_becluster_inquiry_async(
        self,
        request: main_models.GetCreateBEClusterInquiryRequest,
    ) -> main_models.GetCreateBEClusterInquiryResponse:
        runtime = RuntimeOptions()
        return await self.get_create_becluster_inquiry_with_options_async(request, runtime)

    def get_modify_becluster_inquiry_with_options(
        self,
        request: main_models.GetModifyBEClusterInquiryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetModifyBEClusterInquiryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetModifyBEClusterInquiry',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModifyBEClusterInquiryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_modify_becluster_inquiry_with_options_async(
        self,
        request: main_models.GetModifyBEClusterInquiryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetModifyBEClusterInquiryResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetModifyBEClusterInquiry',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModifyBEClusterInquiryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_modify_becluster_inquiry(
        self,
        request: main_models.GetModifyBEClusterInquiryRequest,
    ) -> main_models.GetModifyBEClusterInquiryResponse:
        runtime = RuntimeOptions()
        return self.get_modify_becluster_inquiry_with_options(request, runtime)

    async def get_modify_becluster_inquiry_async(
        self,
        request: main_models.GetModifyBEClusterInquiryRequest,
    ) -> main_models.GetModifyBEClusterInquiryResponse:
        runtime = RuntimeOptions()
        return await self.get_modify_becluster_inquiry_with_options_async(request, runtime)

    def modify_becluster_attribute_with_options(
        self,
        request: main_models.ModifyBEClusterAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBEClusterAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.instance_attribute_type):
            query['InstanceAttributeType'] = request.instance_attribute_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBEClusterAttribute',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBEClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_becluster_attribute_with_options_async(
        self,
        request: main_models.ModifyBEClusterAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBEClusterAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.instance_attribute_type):
            query['InstanceAttributeType'] = request.instance_attribute_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBEClusterAttribute',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBEClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_becluster_attribute(
        self,
        request: main_models.ModifyBEClusterAttributeRequest,
    ) -> main_models.ModifyBEClusterAttributeResponse:
        runtime = RuntimeOptions()
        return self.modify_becluster_attribute_with_options(request, runtime)

    async def modify_becluster_attribute_async(
        self,
        request: main_models.ModifyBEClusterAttributeRequest,
    ) -> main_models.ModifyBEClusterAttributeResponse:
        runtime = RuntimeOptions()
        return await self.modify_becluster_attribute_with_options_async(request, runtime)

    def modify_dbcluster_with_options(
        self,
        request: main_models.ModifyDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not DaraCore.is_null(request.cluster_node_count):
            query['ClusterNodeCount'] = request.cluster_node_count
        if not DaraCore.is_null(request.cluster_node_type):
            query['ClusterNodeType'] = request.cluster_node_type
        if not DaraCore.is_null(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not DaraCore.is_null(request.scale_min):
            query['ScaleMin'] = request.scale_min
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBCluster',
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.cache_size):
            query['CacheSize'] = request.cache_size
        if not DaraCore.is_null(request.cluster_node_count):
            query['ClusterNodeCount'] = request.cluster_node_count
        if not DaraCore.is_null(request.cluster_node_type):
            query['ClusterNodeType'] = request.cluster_node_type
        if not DaraCore.is_null(request.dbcluster_class):
            query['DBClusterClass'] = request.dbcluster_class
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not DaraCore.is_null(request.scale_min):
            query['ScaleMin'] = request.scale_min
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBCluster',
            version = '2023-05-22',
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

    def modify_dbcluster_config_with_options(
        self,
        request: main_models.ModifyDBClusterConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBClusterConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.parallel_operation):
            query['ParallelOperation'] = request.parallel_operation
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterConfig',
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.config_key):
            query['ConfigKey'] = request.config_key
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.parallel_operation):
            query['ParallelOperation'] = request.parallel_operation
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBClusterConfig',
            version = '2023-05-22',
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

    def modify_dbinstance_attribute_with_options(
        self,
        request: main_models.ModifyDBInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.instance_attribute_type):
            query['InstanceAttributeType'] = request.instance_attribute_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceAttribute',
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.instance_attribute_type):
            query['InstanceAttributeType'] = request.instance_attribute_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceAttribute',
            version = '2023-05-22',
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

    def modify_elastic_rule_with_options(
        self,
        request: main_models.ModifyElasticRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElasticRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_class):
            query['ClusterClass'] = request.cluster_class
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not DaraCore.is_null(request.elastic_rule_start_time):
            query['ElasticRuleStartTime'] = request.elastic_rule_start_time
        if not DaraCore.is_null(request.execution_period):
            query['ExecutionPeriod'] = request.execution_period
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticRule',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElasticRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_elastic_rule_with_options_async(
        self,
        request: main_models.ModifyElasticRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyElasticRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_class):
            query['ClusterClass'] = request.cluster_class
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.db_instance_id):
            query['DbInstanceId'] = request.db_instance_id
        if not DaraCore.is_null(request.elastic_rule_start_time):
            query['ElasticRuleStartTime'] = request.elastic_rule_start_time
        if not DaraCore.is_null(request.execution_period):
            query['ExecutionPeriod'] = request.execution_period
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyElasticRule',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyElasticRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_elastic_rule(
        self,
        request: main_models.ModifyElasticRuleRequest,
    ) -> main_models.ModifyElasticRuleResponse:
        runtime = RuntimeOptions()
        return self.modify_elastic_rule_with_options(request, runtime)

    async def modify_elastic_rule_async(
        self,
        request: main_models.ModifyElasticRuleRequest,
    ) -> main_models.ModifyElasticRuleResponse:
        runtime = RuntimeOptions()
        return await self.modify_elastic_rule_with_options_async(request, runtime)

    def modify_security_iplist_with_options(
        self,
        request: main_models.ModifySecurityIPListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityIPListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityIPList',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityIPListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_iplist_with_options_async(
        self,
        request: main_models.ModifySecurityIPListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityIPListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityIPList',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityIPListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_iplist(
        self,
        request: main_models.ModifySecurityIPListRequest,
    ) -> main_models.ModifySecurityIPListResponse:
        runtime = RuntimeOptions()
        return self.modify_security_iplist_with_options(request, runtime)

    async def modify_security_iplist_async(
        self,
        request: main_models.ModifySecurityIPListRequest,
    ) -> main_models.ModifySecurityIPListResponse:
        runtime = RuntimeOptions()
        return await self.modify_security_iplist_with_options_async(request, runtime)

    def modify_virtual_cluster_with_options(
        self,
        request: main_models.ModifyVirtualClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVirtualClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_cluster_id):
            query['ActiveClusterId'] = request.active_cluster_id
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.standby_cluster_id):
            query['StandbyClusterId'] = request.standby_cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVirtualCluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVirtualClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_virtual_cluster_with_options_async(
        self,
        request: main_models.ModifyVirtualClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyVirtualClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.active_cluster_id):
            query['ActiveClusterId'] = request.active_cluster_id
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.standby_cluster_id):
            query['StandbyClusterId'] = request.standby_cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyVirtualCluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyVirtualClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_virtual_cluster(
        self,
        request: main_models.ModifyVirtualClusterRequest,
    ) -> main_models.ModifyVirtualClusterResponse:
        runtime = RuntimeOptions()
        return self.modify_virtual_cluster_with_options(request, runtime)

    async def modify_virtual_cluster_async(
        self,
        request: main_models.ModifyVirtualClusterRequest,
    ) -> main_models.ModifyVirtualClusterResponse:
        runtime = RuntimeOptions()
        return await self.modify_virtual_cluster_with_options_async(request, runtime)

    def release_instance_public_connection_with_options(
        self,
        request: main_models.ReleaseInstancePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstancePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstancePublicConnection',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstancePublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_instance_public_connection_with_options_async(
        self,
        request: main_models.ReleaseInstancePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstancePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstancePublicConnection',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseInstancePublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_instance_public_connection(
        self,
        request: main_models.ReleaseInstancePublicConnectionRequest,
    ) -> main_models.ReleaseInstancePublicConnectionResponse:
        runtime = RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    async def release_instance_public_connection_async(
        self,
        request: main_models.ReleaseInstancePublicConnectionRequest,
    ) -> main_models.ReleaseInstancePublicConnectionResponse:
        runtime = RuntimeOptions()
        return await self.release_instance_public_connection_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: main_models.ResetAccountPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAccountPasswordResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPassword',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPassword',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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

    def restart_dbcluster_with_options(
        self,
        request: main_models.RestartDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.parallel_operation):
            query['ParallelOperation'] = request.parallel_operation
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartDBCluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dbcluster_with_options_async(
        self,
        request: main_models.RestartDBClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartDBClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.parallel_operation):
            query['ParallelOperation'] = request.parallel_operation
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        body = {}
        if not DaraCore.is_null(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartDBCluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dbcluster(
        self,
        request: main_models.RestartDBClusterRequest,
    ) -> main_models.RestartDBClusterResponse:
        runtime = RuntimeOptions()
        return self.restart_dbcluster_with_options(request, runtime)

    async def restart_dbcluster_async(
        self,
        request: main_models.RestartDBClusterRequest,
    ) -> main_models.RestartDBClusterResponse:
        runtime = RuntimeOptions()
        return await self.restart_dbcluster_with_options_async(request, runtime)

    def start_becluster_with_options(
        self,
        request: main_models.StartBEClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartBEClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartBECluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartBEClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_becluster_with_options_async(
        self,
        request: main_models.StartBEClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartBEClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartBECluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartBEClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_becluster(
        self,
        request: main_models.StartBEClusterRequest,
    ) -> main_models.StartBEClusterResponse:
        runtime = RuntimeOptions()
        return self.start_becluster_with_options(request, runtime)

    async def start_becluster_async(
        self,
        request: main_models.StartBEClusterRequest,
    ) -> main_models.StartBEClusterResponse:
        runtime = RuntimeOptions()
        return await self.start_becluster_with_options_async(request, runtime)

    def stop_becluster_with_options(
        self,
        request: main_models.StopBEClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopBEClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopBECluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopBEClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_becluster_with_options_async(
        self,
        request: main_models.StopBEClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopBEClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopBECluster',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopBEClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_becluster(
        self,
        request: main_models.StopBEClusterRequest,
    ) -> main_models.StopBEClusterResponse:
        runtime = RuntimeOptions()
        return self.stop_becluster_with_options(request, runtime)

    async def stop_becluster_async(
        self,
        request: main_models.StopBEClusterRequest,
    ) -> main_models.StopBEClusterResponse:
        runtime = RuntimeOptions()
        return await self.stop_becluster_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
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
            version = '2023-05-22',
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

    def upgrade_dbinstance_deploy_scheme_with_options(
        self,
        tmp_req: main_models.UpgradeDBInstanceDeploySchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeDBInstanceDeploySchemeResponse:
        tmp_req.validate()
        request = main_models.UpgradeDBInstanceDeploySchemeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.multi_zone):
            request.multi_zone_shrink = Utils.array_to_string_with_specified_style(tmp_req.multi_zone, 'MultiZone', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.multi_zone_shrink):
            query['MultiZone'] = request.multi_zone_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBInstanceDeployScheme',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeDBInstanceDeploySchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_dbinstance_deploy_scheme_with_options_async(
        self,
        tmp_req: main_models.UpgradeDBInstanceDeploySchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeDBInstanceDeploySchemeResponse:
        tmp_req.validate()
        request = main_models.UpgradeDBInstanceDeploySchemeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.multi_zone):
            request.multi_zone_shrink = Utils.array_to_string_with_specified_style(tmp_req.multi_zone, 'MultiZone', 'json')
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.multi_zone_shrink):
            query['MultiZone'] = request.multi_zone_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBInstanceDeployScheme',
            version = '2023-05-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeDBInstanceDeploySchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_dbinstance_deploy_scheme(
        self,
        request: main_models.UpgradeDBInstanceDeploySchemeRequest,
    ) -> main_models.UpgradeDBInstanceDeploySchemeResponse:
        runtime = RuntimeOptions()
        return self.upgrade_dbinstance_deploy_scheme_with_options(request, runtime)

    async def upgrade_dbinstance_deploy_scheme_async(
        self,
        request: main_models.UpgradeDBInstanceDeploySchemeRequest,
    ) -> main_models.UpgradeDBInstanceDeploySchemeResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_dbinstance_deploy_scheme_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.parallel_operation):
            query['ParallelOperation'] = request.parallel_operation
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBInstanceEngineVersion',
            version = '2023-05-22',
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
        if not DaraCore.is_null(request.parallel_operation):
            query['ParallelOperation'] = request.parallel_operation
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBInstanceEngineVersion',
            version = '2023-05-22',
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
