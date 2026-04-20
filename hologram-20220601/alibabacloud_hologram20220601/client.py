# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_hologram20220601 import models as main_models
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
        self._endpoint = self.get_endpoint('hologram', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.new_resource_group_id):
            body['newResourceGroupId'] = request.new_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tag/changeResourceGroup',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_id):
            body['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.new_resource_group_id):
            body['newResourceGroupId'] = request.new_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/tag/changeResourceGroup',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def create_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: main_models.CreateHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_count):
            body['clusterCount'] = request.cluster_count
        if not DaraCore.is_null(request.cpu):
            body['cpu'] = request.cpu
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/createHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_count):
            body['clusterCount'] = request.cluster_count
        if not DaraCore.is_null(request.cpu):
            body['cpu'] = request.cpu
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/createHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_holo_warehouse(
        self,
        instance_id: str,
        request: main_models.CreateHoloWarehouseRequest,
    ) -> main_models.CreateHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def create_holo_warehouse_async(
        self,
        instance_id: str,
        request: main_models.CreateHoloWarehouseRequest,
    ) -> main_models.CreateHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_pay):
            body['autoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.charge_type):
            body['chargeType'] = request.charge_type
        if not DaraCore.is_null(request.cold_storage_size):
            body['coldStorageSize'] = request.cold_storage_size
        if not DaraCore.is_null(request.cpu):
            body['cpu'] = request.cpu
        if not DaraCore.is_null(request.duration):
            body['duration'] = request.duration
        if not DaraCore.is_null(request.enable_serverless_computing):
            body['enableServerlessComputing'] = request.enable_serverless_computing
        if not DaraCore.is_null(request.gateway_count):
            body['gatewayCount'] = request.gateway_count
        if not DaraCore.is_null(request.initial_databases):
            body['initialDatabases'] = request.initial_databases
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_type):
            body['instanceType'] = request.instance_type
        if not DaraCore.is_null(request.leader_instance_id):
            body['leaderInstanceId'] = request.leader_instance_id
        if not DaraCore.is_null(request.pricing_cycle):
            body['pricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.region_id):
            body['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.storage_size):
            body['storageSize'] = request.storage_size
        if not DaraCore.is_null(request.storage_type):
            body['storageType'] = request.storage_type
        if not DaraCore.is_null(request.v_switch_id):
            body['vSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            body['zoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_pay):
            body['autoPay'] = request.auto_pay
        if not DaraCore.is_null(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.charge_type):
            body['chargeType'] = request.charge_type
        if not DaraCore.is_null(request.cold_storage_size):
            body['coldStorageSize'] = request.cold_storage_size
        if not DaraCore.is_null(request.cpu):
            body['cpu'] = request.cpu
        if not DaraCore.is_null(request.duration):
            body['duration'] = request.duration
        if not DaraCore.is_null(request.enable_serverless_computing):
            body['enableServerlessComputing'] = request.enable_serverless_computing
        if not DaraCore.is_null(request.gateway_count):
            body['gatewayCount'] = request.gateway_count
        if not DaraCore.is_null(request.initial_databases):
            body['initialDatabases'] = request.initial_databases
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_type):
            body['instanceType'] = request.instance_type
        if not DaraCore.is_null(request.leader_instance_id):
            body['leaderInstanceId'] = request.leader_instance_id
        if not DaraCore.is_null(request.pricing_cycle):
            body['pricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.region_id):
            body['regionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.storage_size):
            body['storageSize'] = request.storage_size
        if not DaraCore.is_null(request.storage_type):
            body['storageType'] = request.storage_type
        if not DaraCore.is_null(request.v_switch_id):
            body['vSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            body['zoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/create',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: main_models.CreateInstanceRequest,
    ) -> main_models.CreateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def create_user_with_options(
        self,
        instance_id: str,
        request: main_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.super_user):
            body['superUser'] = request.super_user
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/createUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        instance_id: str,
        request: main_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.super_user):
            body['superUser'] = request.super_user
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/createUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        instance_id: str,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_user_with_options(instance_id, request, headers, runtime)

    async def create_user_async(
        self,
        instance_id: str,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_user_with_options_async(instance_id, request, headers, runtime)

    def delete_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: main_models.DeleteHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/deleteHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: main_models.DeleteHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/deleteHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_holo_warehouse(
        self,
        instance_id: str,
        request: main_models.DeleteHoloWarehouseRequest,
    ) -> main_models.DeleteHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def delete_holo_warehouse_async(
        self,
        instance_id: str,
        request: main_models.DeleteHoloWarehouseRequest,
    ) -> main_models.DeleteHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def delete_instance_with_options(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/delete',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(instance_id, request, headers, runtime)

    async def delete_instance_async(
        self,
        instance_id: str,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(instance_id, request, headers, runtime)

    def disable_hive_access_with_options(
        self,
        instance_id: str,
        request: main_models.DisableHiveAccessRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableHiveAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableHiveAccess',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/disableHiveAccess',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableHiveAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_hive_access_with_options_async(
        self,
        instance_id: str,
        request: main_models.DisableHiveAccessRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableHiveAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableHiveAccess',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/disableHiveAccess',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableHiveAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_hive_access(
        self,
        instance_id: str,
        request: main_models.DisableHiveAccessRequest,
    ) -> main_models.DisableHiveAccessResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_hive_access_with_options(instance_id, request, headers, runtime)

    async def disable_hive_access_async(
        self,
        instance_id: str,
        request: main_models.DisableHiveAccessRequest,
    ) -> main_models.DisableHiveAccessResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_hive_access_with_options_async(instance_id, request, headers, runtime)

    def disable_sslwith_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableSSLResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DisableSSL',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/disableSSL',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_sslwith_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DisableSSLResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DisableSSL',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/disableSSL',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_ssl(
        self,
        instance_id: str,
    ) -> main_models.DisableSSLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.disable_sslwith_options(instance_id, headers, runtime)

    async def disable_ssl_async(
        self,
        instance_id: str,
    ) -> main_models.DisableSSLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.disable_sslwith_options_async(instance_id, headers, runtime)

    def drop_user_with_options(
        self,
        instance_id: str,
        request: main_models.DropUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DropUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.super_user):
            body['superUser'] = request.super_user
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DropUser',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/dropUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DropUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_user_with_options_async(
        self,
        instance_id: str,
        request: main_models.DropUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DropUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.super_user):
            body['superUser'] = request.super_user
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DropUser',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/dropUser',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DropUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_user(
        self,
        instance_id: str,
        request: main_models.DropUserRequest,
    ) -> main_models.DropUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.drop_user_with_options(instance_id, request, headers, runtime)

    async def drop_user_async(
        self,
        instance_id: str,
        request: main_models.DropUserRequest,
    ) -> main_models.DropUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.drop_user_with_options_async(instance_id, request, headers, runtime)

    def enable_hive_access_with_options(
        self,
        instance_id: str,
        request: main_models.EnableHiveAccessRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableHiveAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHiveAccess',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/enableHiveAccess',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHiveAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_hive_access_with_options_async(
        self,
        instance_id: str,
        request: main_models.EnableHiveAccessRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableHiveAccessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHiveAccess',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/enableHiveAccess',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHiveAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_hive_access(
        self,
        instance_id: str,
        request: main_models.EnableHiveAccessRequest,
    ) -> main_models.EnableHiveAccessResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_hive_access_with_options(instance_id, request, headers, runtime)

    async def enable_hive_access_async(
        self,
        instance_id: str,
        request: main_models.EnableHiveAccessRequest,
    ) -> main_models.EnableHiveAccessResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_hive_access_with_options_async(instance_id, request, headers, runtime)

    def enable_sslwith_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableSSLResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'EnableSSL',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/enableSSL',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_sslwith_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.EnableSSLResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'EnableSSL',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/enableSSL',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_ssl(
        self,
        instance_id: str,
    ) -> main_models.EnableSSLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.enable_sslwith_options(instance_id, headers, runtime)

    async def enable_ssl_async(
        self,
        instance_id: str,
    ) -> main_models.EnableSSLResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.enable_sslwith_options_async(instance_id, headers, runtime)

    def get_certificate_attribute_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCertificateAttributeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCertificateAttribute',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/certificateAttribute',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCertificateAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_certificate_attribute_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCertificateAttributeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCertificateAttribute',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/certificateAttribute',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCertificateAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_certificate_attribute(
        self,
        instance_id: str,
    ) -> main_models.GetCertificateAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_certificate_attribute_with_options(instance_id, headers, runtime)

    async def get_certificate_attribute_async(
        self,
        instance_id: str,
    ) -> main_models.GetCertificateAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_certificate_attribute_with_options_async(instance_id, headers, runtime)

    def get_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        instance_id: str,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(instance_id, headers, runtime)

    async def get_instance_async(
        self,
        instance_id: str,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(instance_id, headers, runtime)

    def get_root_certificate_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRootCertificateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRootCertificate',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/rootCertificate',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRootCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_root_certificate_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRootCertificateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRootCertificate',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/rootCertificate',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRootCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_root_certificate(
        self,
        instance_id: str,
    ) -> main_models.GetRootCertificateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_root_certificate_with_options(instance_id, headers, runtime)

    async def get_root_certificate_async(
        self,
        instance_id: str,
    ) -> main_models.GetRootCertificateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_root_certificate_with_options_async(instance_id, headers, runtime)

    def get_warehouse_detail_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWarehouseDetailResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetWarehouseDetail',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/getWarehouseDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWarehouseDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_warehouse_detail_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetWarehouseDetailResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetWarehouseDetail',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/getWarehouseDetail',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWarehouseDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_warehouse_detail(
        self,
        instance_id: str,
    ) -> main_models.GetWarehouseDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_warehouse_detail_with_options(instance_id, headers, runtime)

    async def get_warehouse_detail_async(
        self,
        instance_id: str,
    ) -> main_models.GetWarehouseDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_warehouse_detail_with_options_async(instance_id, headers, runtime)

    def grant_database_permission_with_options(
        self,
        instance_id: str,
        request: main_models.GrantDatabasePermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantDatabasePermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.database_name):
            body['databaseName'] = request.database_name
        if not DaraCore.is_null(request.privileges):
            body['privileges'] = request.privileges
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantDatabasePermission',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/grantDatabasePermission',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantDatabasePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_database_permission_with_options_async(
        self,
        instance_id: str,
        request: main_models.GrantDatabasePermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantDatabasePermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.database_name):
            body['databaseName'] = request.database_name
        if not DaraCore.is_null(request.privileges):
            body['privileges'] = request.privileges
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantDatabasePermission',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/grantDatabasePermission',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantDatabasePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_database_permission(
        self,
        instance_id: str,
        request: main_models.GrantDatabasePermissionRequest,
    ) -> main_models.GrantDatabasePermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.grant_database_permission_with_options(instance_id, request, headers, runtime)

    async def grant_database_permission_async(
        self,
        instance_id: str,
        request: main_models.GrantDatabasePermissionRequest,
    ) -> main_models.GrantDatabasePermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.grant_database_permission_with_options_async(instance_id, request, headers, runtime)

    def grant_schema_permission_with_options(
        self,
        instance_id: str,
        request: main_models.GrantSchemaPermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantSchemaPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.database_name):
            body['databaseName'] = request.database_name
        if not DaraCore.is_null(request.privileges):
            body['privileges'] = request.privileges
        if not DaraCore.is_null(request.schema_name):
            body['schemaName'] = request.schema_name
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantSchemaPermission',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/grantSchemaPermission',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantSchemaPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_schema_permission_with_options_async(
        self,
        instance_id: str,
        request: main_models.GrantSchemaPermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantSchemaPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.database_name):
            body['databaseName'] = request.database_name
        if not DaraCore.is_null(request.privileges):
            body['privileges'] = request.privileges
        if not DaraCore.is_null(request.schema_name):
            body['schemaName'] = request.schema_name
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantSchemaPermission',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/grantSchemaPermission',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantSchemaPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_schema_permission(
        self,
        instance_id: str,
        request: main_models.GrantSchemaPermissionRequest,
    ) -> main_models.GrantSchemaPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.grant_schema_permission_with_options(instance_id, request, headers, runtime)

    async def grant_schema_permission_async(
        self,
        instance_id: str,
        request: main_models.GrantSchemaPermissionRequest,
    ) -> main_models.GrantSchemaPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.grant_schema_permission_with_options_async(instance_id, request, headers, runtime)

    def grant_table_permission_with_options(
        self,
        instance_id: str,
        request: main_models.GrantTablePermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantTablePermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.all_table):
            body['allTable'] = request.all_table
        if not DaraCore.is_null(request.database_name):
            body['databaseName'] = request.database_name
        if not DaraCore.is_null(request.privileges):
            body['privileges'] = request.privileges
        if not DaraCore.is_null(request.schema_name):
            body['schemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            body['tableName'] = request.table_name
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantTablePermission',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/grantTablePermission',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantTablePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_table_permission_with_options_async(
        self,
        instance_id: str,
        request: main_models.GrantTablePermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantTablePermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.all_table):
            body['allTable'] = request.all_table
        if not DaraCore.is_null(request.database_name):
            body['databaseName'] = request.database_name
        if not DaraCore.is_null(request.privileges):
            body['privileges'] = request.privileges
        if not DaraCore.is_null(request.schema_name):
            body['schemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            body['tableName'] = request.table_name
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantTablePermission',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/grantTablePermission',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantTablePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_table_permission(
        self,
        instance_id: str,
        request: main_models.GrantTablePermissionRequest,
    ) -> main_models.GrantTablePermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.grant_table_permission_with_options(instance_id, request, headers, runtime)

    async def grant_table_permission_async(
        self,
        instance_id: str,
        request: main_models.GrantTablePermissionRequest,
    ) -> main_models.GrantTablePermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.grant_table_permission_with_options_async(instance_id, request, headers, runtime)

    def list_backup_data_with_options(
        self,
        request: main_models.ListBackupDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBackupDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_type):
            query['backupType'] = request.backup_type
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBackupData',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/backups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBackupDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_backup_data_with_options_async(
        self,
        request: main_models.ListBackupDataRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBackupDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_type):
            query['backupType'] = request.backup_type
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBackupData',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/backups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBackupDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_backup_data(
        self,
        request: main_models.ListBackupDataRequest,
    ) -> main_models.ListBackupDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_backup_data_with_options(request, headers, runtime)

    async def list_backup_data_async(
        self,
        request: main_models.ListBackupDataRequest,
    ) -> main_models.ListBackupDataResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_backup_data_with_options_async(request, headers, runtime)

    def list_databases_with_options(
        self,
        instance_id: str,
        request: main_models.ListDatabasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.external):
            query['external'] = request.external
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabases',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/listDatabases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_databases_with_options_async(
        self,
        instance_id: str,
        request: main_models.ListDatabasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.external):
            query['external'] = request.external
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabases',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/listDatabases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_databases(
        self,
        instance_id: str,
        request: main_models.ListDatabasesRequest,
    ) -> main_models.ListDatabasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_databases_with_options(instance_id, request, headers, runtime)

    async def list_databases_async(
        self,
        instance_id: str,
        request: main_models.ListDatabasesRequest,
    ) -> main_models.ListDatabasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_databases_with_options_async(instance_id, request, headers, runtime)

    def list_instances_with_options(
        self,
        request: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cms_instance_type):
            body['cmsInstanceType'] = request.cms_instance_type
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cms_instance_type):
            body['cmsInstanceType'] = request.cms_instance_type
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: main_models.ListInstancesRequest,
    ) -> main_models.ListInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_warehouses_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWarehousesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListWarehouses',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/listWarehouses',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWarehousesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_warehouses_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWarehousesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListWarehouses',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/listWarehouses',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWarehousesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_warehouses(
        self,
        instance_id: str,
    ) -> main_models.ListWarehousesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_warehouses_with_options(instance_id, headers, runtime)

    async def list_warehouses_async(
        self,
        instance_id: str,
    ) -> main_models.ListWarehousesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_warehouses_with_options_async(instance_id, headers, runtime)

    def rebalance_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: main_models.RebalanceHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RebalanceHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RebalanceHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/rebalanceHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebalanceHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebalance_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: main_models.RebalanceHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RebalanceHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RebalanceHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/rebalanceHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebalanceHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebalance_holo_warehouse(
        self,
        instance_id: str,
        request: main_models.RebalanceHoloWarehouseRequest,
    ) -> main_models.RebalanceHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rebalance_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def rebalance_holo_warehouse_async(
        self,
        instance_id: str,
        request: main_models.RebalanceHoloWarehouseRequest,
    ) -> main_models.RebalanceHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rebalance_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def rename_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: main_models.RenameHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenameHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.new_warehouse_name):
            body['newWarehouseName'] = request.new_warehouse_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenameHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/renameHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def rename_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: main_models.RenameHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenameHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.new_warehouse_name):
            body['newWarehouseName'] = request.new_warehouse_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenameHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/renameHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenameHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rename_holo_warehouse(
        self,
        instance_id: str,
        request: main_models.RenameHoloWarehouseRequest,
    ) -> main_models.RenameHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rename_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def rename_holo_warehouse_async(
        self,
        instance_id: str,
        request: main_models.RenameHoloWarehouseRequest,
    ) -> main_models.RenameHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rename_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def renew_instance_with_options(
        self,
        instance_id: str,
        request: main_models.RenewInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.duration):
            body['duration'] = request.duration
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/renew',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        instance_id: str,
        request: main_models.RenewInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.duration):
            body['duration'] = request.duration
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/renew',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        instance_id: str,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.renew_instance_with_options(instance_id, request, headers, runtime)

    async def renew_instance_async(
        self,
        instance_id: str,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.renew_instance_with_options_async(instance_id, request, headers, runtime)

    def renew_sslcertificate_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenewSSLCertificateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RenewSSLCertificate',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/renewSSLCertificate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewSSLCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_sslcertificate_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RenewSSLCertificateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RenewSSLCertificate',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/renewSSLCertificate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewSSLCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_sslcertificate(
        self,
        instance_id: str,
    ) -> main_models.RenewSSLCertificateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.renew_sslcertificate_with_options(instance_id, headers, runtime)

    async def renew_sslcertificate_async(
        self,
        instance_id: str,
    ) -> main_models.RenewSSLCertificateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.renew_sslcertificate_with_options_async(instance_id, headers, runtime)

    def restart_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: main_models.RestartHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/restartHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: main_models.RestartHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RestartHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/restartHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_holo_warehouse(
        self,
        instance_id: str,
        request: main_models.RestartHoloWarehouseRequest,
    ) -> main_models.RestartHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def restart_holo_warehouse_async(
        self,
        instance_id: str,
        request: main_models.RestartHoloWarehouseRequest,
    ) -> main_models.RestartHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def restart_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RestartInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RestartInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/restart',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        instance_id: str,
    ) -> main_models.RestartInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.restart_instance_with_options(instance_id, headers, runtime)

    async def restart_instance_async(
        self,
        instance_id: str,
    ) -> main_models.RestartInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.restart_instance_with_options_async(instance_id, headers, runtime)

    def resume_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: main_models.ResumeHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResumeHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resumeHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: main_models.ResumeHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResumeHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resumeHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_holo_warehouse(
        self,
        instance_id: str,
        request: main_models.ResumeHoloWarehouseRequest,
    ) -> main_models.ResumeHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.resume_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def resume_holo_warehouse_async(
        self,
        instance_id: str,
        request: main_models.ResumeHoloWarehouseRequest,
    ) -> main_models.ResumeHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.resume_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def resume_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResumeInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ResumeInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ResumeInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/resume',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_instance(
        self,
        instance_id: str,
    ) -> main_models.ResumeInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.resume_instance_with_options(instance_id, headers, runtime)

    async def resume_instance_async(
        self,
        instance_id: str,
    ) -> main_models.ResumeInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.resume_instance_with_options_async(instance_id, headers, runtime)

    def revoke_database_permission_with_options(
        self,
        instance_id: str,
        request: main_models.RevokeDatabasePermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeDatabasePermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.database_name):
            body['databaseName'] = request.database_name
        if not DaraCore.is_null(request.privileges):
            body['privileges'] = request.privileges
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeDatabasePermission',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/revokeDatabasePermission',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeDatabasePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_database_permission_with_options_async(
        self,
        instance_id: str,
        request: main_models.RevokeDatabasePermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeDatabasePermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.database_name):
            body['databaseName'] = request.database_name
        if not DaraCore.is_null(request.privileges):
            body['privileges'] = request.privileges
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeDatabasePermission',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/revokeDatabasePermission',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeDatabasePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_database_permission(
        self,
        instance_id: str,
        request: main_models.RevokeDatabasePermissionRequest,
    ) -> main_models.RevokeDatabasePermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.revoke_database_permission_with_options(instance_id, request, headers, runtime)

    async def revoke_database_permission_async(
        self,
        instance_id: str,
        request: main_models.RevokeDatabasePermissionRequest,
    ) -> main_models.RevokeDatabasePermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.revoke_database_permission_with_options_async(instance_id, request, headers, runtime)

    def revoke_schema_permission_with_options(
        self,
        instance_id: str,
        request: main_models.RevokeSchemaPermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeSchemaPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.database_name):
            body['databaseName'] = request.database_name
        if not DaraCore.is_null(request.privileges):
            body['privileges'] = request.privileges
        if not DaraCore.is_null(request.schema_name):
            body['schemaName'] = request.schema_name
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeSchemaPermission',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/revokeSchemaPermission',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeSchemaPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_schema_permission_with_options_async(
        self,
        instance_id: str,
        request: main_models.RevokeSchemaPermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeSchemaPermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.database_name):
            body['databaseName'] = request.database_name
        if not DaraCore.is_null(request.privileges):
            body['privileges'] = request.privileges
        if not DaraCore.is_null(request.schema_name):
            body['schemaName'] = request.schema_name
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeSchemaPermission',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/revokeSchemaPermission',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeSchemaPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_schema_permission(
        self,
        instance_id: str,
        request: main_models.RevokeSchemaPermissionRequest,
    ) -> main_models.RevokeSchemaPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.revoke_schema_permission_with_options(instance_id, request, headers, runtime)

    async def revoke_schema_permission_async(
        self,
        instance_id: str,
        request: main_models.RevokeSchemaPermissionRequest,
    ) -> main_models.RevokeSchemaPermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.revoke_schema_permission_with_options_async(instance_id, request, headers, runtime)

    def revoke_table_permission_with_options(
        self,
        instance_id: str,
        request: main_models.RevokeTablePermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeTablePermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.all_table):
            body['allTable'] = request.all_table
        if not DaraCore.is_null(request.database_name):
            body['databaseName'] = request.database_name
        if not DaraCore.is_null(request.privileges):
            body['privileges'] = request.privileges
        if not DaraCore.is_null(request.schema_name):
            body['schemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            body['tableName'] = request.table_name
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeTablePermission',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/revokeTablePermission',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeTablePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_table_permission_with_options_async(
        self,
        instance_id: str,
        request: main_models.RevokeTablePermissionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeTablePermissionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.all_table):
            body['allTable'] = request.all_table
        if not DaraCore.is_null(request.database_name):
            body['databaseName'] = request.database_name
        if not DaraCore.is_null(request.privileges):
            body['privileges'] = request.privileges
        if not DaraCore.is_null(request.schema_name):
            body['schemaName'] = request.schema_name
        if not DaraCore.is_null(request.table_name):
            body['tableName'] = request.table_name
        if not DaraCore.is_null(request.user_name):
            body['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeTablePermission',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/revokeTablePermission',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeTablePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_table_permission(
        self,
        instance_id: str,
        request: main_models.RevokeTablePermissionRequest,
    ) -> main_models.RevokeTablePermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.revoke_table_permission_with_options(instance_id, request, headers, runtime)

    async def revoke_table_permission_async(
        self,
        instance_id: str,
        request: main_models.RevokeTablePermissionRequest,
    ) -> main_models.RevokeTablePermissionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.revoke_table_permission_with_options_async(instance_id, request, headers, runtime)

    def scale_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: main_models.ScaleHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_count):
            body['clusterCount'] = request.cluster_count
        if not DaraCore.is_null(request.cpu):
            body['cpu'] = request.cpu
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScaleHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/scaleHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: main_models.ScaleHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_count):
            body['clusterCount'] = request.cluster_count
        if not DaraCore.is_null(request.cpu):
            body['cpu'] = request.cpu
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScaleHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/scaleHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_holo_warehouse(
        self,
        instance_id: str,
        request: main_models.ScaleHoloWarehouseRequest,
    ) -> main_models.ScaleHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.scale_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def scale_holo_warehouse_async(
        self,
        instance_id: str,
        request: main_models.ScaleHoloWarehouseRequest,
    ) -> main_models.ScaleHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.scale_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def scale_instance_with_options(
        self,
        instance_id: str,
        request: main_models.ScaleInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cold_storage_size):
            body['coldStorageSize'] = request.cold_storage_size
        if not DaraCore.is_null(request.cpu):
            body['cpu'] = request.cpu
        if not DaraCore.is_null(request.enable_serverless_computing):
            body['enableServerlessComputing'] = request.enable_serverless_computing
        if not DaraCore.is_null(request.gateway_count):
            body['gatewayCount'] = request.gateway_count
        if not DaraCore.is_null(request.scale_type):
            body['scaleType'] = request.scale_type
        if not DaraCore.is_null(request.storage_size):
            body['storageSize'] = request.storage_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScaleInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/scale',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_instance_with_options_async(
        self,
        instance_id: str,
        request: main_models.ScaleInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ScaleInstanceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cold_storage_size):
            body['coldStorageSize'] = request.cold_storage_size
        if not DaraCore.is_null(request.cpu):
            body['cpu'] = request.cpu
        if not DaraCore.is_null(request.enable_serverless_computing):
            body['enableServerlessComputing'] = request.enable_serverless_computing
        if not DaraCore.is_null(request.gateway_count):
            body['gatewayCount'] = request.gateway_count
        if not DaraCore.is_null(request.scale_type):
            body['scaleType'] = request.scale_type
        if not DaraCore.is_null(request.storage_size):
            body['storageSize'] = request.storage_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ScaleInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/scale',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ScaleInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_instance(
        self,
        instance_id: str,
        request: main_models.ScaleInstanceRequest,
    ) -> main_models.ScaleInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.scale_instance_with_options(instance_id, request, headers, runtime)

    async def scale_instance_async(
        self,
        instance_id: str,
        request: main_models.ScaleInstanceRequest,
    ) -> main_models.ScaleInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.scale_instance_with_options_async(instance_id, request, headers, runtime)

    def stop_instance_with_options(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        instance_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.StopInstanceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'StopInstance',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/stop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_instance(
        self,
        instance_id: str,
    ) -> main_models.StopInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.stop_instance_with_options(instance_id, headers, runtime)

    async def stop_instance_async(
        self,
        instance_id: str,
    ) -> main_models.StopInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.stop_instance_with_options_async(instance_id, headers, runtime)

    def suspend_holo_warehouse_with_options(
        self,
        instance_id: str,
        request: main_models.SuspendHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SuspendHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SuspendHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/suspendHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendHoloWarehouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_holo_warehouse_with_options_async(
        self,
        instance_id: str,
        request: main_models.SuspendHoloWarehouseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SuspendHoloWarehouseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SuspendHoloWarehouse',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/suspendHoloWarehouse',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendHoloWarehouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_holo_warehouse(
        self,
        instance_id: str,
        request: main_models.SuspendHoloWarehouseRequest,
    ) -> main_models.SuspendHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.suspend_holo_warehouse_with_options(instance_id, request, headers, runtime)

    async def suspend_holo_warehouse_async(
        self,
        instance_id: str,
        request: main_models.SuspendHoloWarehouseRequest,
    ) -> main_models.SuspendHoloWarehouseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.suspend_holo_warehouse_with_options_async(instance_id, request, headers, runtime)

    def update_instance_name_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceNameResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceName',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/instanceName',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_name_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceNameResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceName',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/instanceName',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_name(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceNameRequest,
    ) -> main_models.UpdateInstanceNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_name_with_options(instance_id, request, headers, runtime)

    async def update_instance_name_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceNameRequest,
    ) -> main_models.UpdateInstanceNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_name_with_options_async(instance_id, request, headers, runtime)

    def update_instance_network_type_with_options(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceNetworkTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceNetworkTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.any_tunnel_to_single_tunnel):
            body['anyTunnelToSingleTunnel'] = request.any_tunnel_to_single_tunnel
        if not DaraCore.is_null(request.network_types):
            body['networkTypes'] = request.network_types
        if not DaraCore.is_null(request.v_switch_id):
            body['vSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_owner_id):
            body['vpcOwnerId'] = request.vpc_owner_id
        if not DaraCore.is_null(request.vpc_region_id):
            body['vpcRegionId'] = request.vpc_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceNetworkType',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/network',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceNetworkTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_network_type_with_options_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceNetworkTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceNetworkTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.any_tunnel_to_single_tunnel):
            body['anyTunnelToSingleTunnel'] = request.any_tunnel_to_single_tunnel
        if not DaraCore.is_null(request.network_types):
            body['networkTypes'] = request.network_types
        if not DaraCore.is_null(request.v_switch_id):
            body['vSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vpc_owner_id):
            body['vpcOwnerId'] = request.vpc_owner_id
        if not DaraCore.is_null(request.vpc_region_id):
            body['vpcRegionId'] = request.vpc_region_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceNetworkType',
            version = '2022-06-01',
            protocol = 'HTTPS',
            pathname = f'/api/v1/instances/{DaraURL.percent_encode(instance_id)}/network',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceNetworkTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_network_type(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceNetworkTypeRequest,
    ) -> main_models.UpdateInstanceNetworkTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_network_type_with_options(instance_id, request, headers, runtime)

    async def update_instance_network_type_async(
        self,
        instance_id: str,
        request: main_models.UpdateInstanceNetworkTypeRequest,
    ) -> main_models.UpdateInstanceNetworkTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_network_type_with_options_async(instance_id, request, headers, runtime)
