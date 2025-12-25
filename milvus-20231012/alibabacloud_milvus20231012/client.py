# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_milvus20231012 import models as main_models
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
        self._endpoint = self.get_endpoint('milvus', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceGroup/change',
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
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/resourceGroup/change',
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

    def create_default_role_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDefaultRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateDefaultRole',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/user/create_default_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDefaultRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_default_role_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDefaultRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CreateDefaultRole',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/user/create_default_role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDefaultRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_default_role(self) -> main_models.CreateDefaultRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_default_role_with_options(headers, runtime)

    async def create_default_role_async(self) -> main_models.CreateDefaultRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_default_role_with_options_async(headers, runtime)

    def create_instance_with_options(
        self,
        request: main_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.auto_backup):
            body['autoBackup'] = request.auto_backup
        if not DaraCore.is_null(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.components):
            body['components'] = request.components
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.db_admin_password):
            body['dbAdminPassword'] = request.db_admin_password
        if not DaraCore.is_null(request.db_version):
            body['dbVersion'] = request.db_version
        if not DaraCore.is_null(request.encrypted):
            body['encrypted'] = request.encrypted
        if not DaraCore.is_null(request.ha):
            body['ha'] = request.ha
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.is_multi_az_storage):
            body['isMultiAzStorage'] = request.is_multi_az_storage
        if not DaraCore.is_null(request.kms_key_id):
            body['kmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.load_replicas):
            body['loadReplicas'] = request.load_replicas
        if not DaraCore.is_null(request.multi_zone_mode):
            body['multiZoneMode'] = request.multi_zone_mode
        if not DaraCore.is_null(request.payment_duration):
            body['paymentDuration'] = request.payment_duration
        if not DaraCore.is_null(request.payment_duration_unit):
            body['paymentDurationUnit'] = request.payment_duration_unit
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.promotion_no):
            body['promotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.v_switch_ids):
            body['vSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            body['zoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/instance/create',
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
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.auto_backup):
            body['autoBackup'] = request.auto_backup
        if not DaraCore.is_null(request.auto_renew):
            body['autoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.components):
            body['components'] = request.components
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.db_admin_password):
            body['dbAdminPassword'] = request.db_admin_password
        if not DaraCore.is_null(request.db_version):
            body['dbVersion'] = request.db_version
        if not DaraCore.is_null(request.encrypted):
            body['encrypted'] = request.encrypted
        if not DaraCore.is_null(request.ha):
            body['ha'] = request.ha
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.is_multi_az_storage):
            body['isMultiAzStorage'] = request.is_multi_az_storage
        if not DaraCore.is_null(request.kms_key_id):
            body['kmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.load_replicas):
            body['loadReplicas'] = request.load_replicas
        if not DaraCore.is_null(request.multi_zone_mode):
            body['multiZoneMode'] = request.multi_zone_mode
        if not DaraCore.is_null(request.payment_duration):
            body['paymentDuration'] = request.payment_duration
        if not DaraCore.is_null(request.payment_duration_unit):
            body['paymentDurationUnit'] = request.payment_duration_unit
        if not DaraCore.is_null(request.payment_type):
            body['paymentType'] = request.payment_type
        if not DaraCore.is_null(request.promotion_no):
            body['promotionNo'] = request.promotion_no
        if not DaraCore.is_null(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.v_switch_ids):
            body['vSwitchIds'] = request.v_switch_ids
        if not DaraCore.is_null(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not DaraCore.is_null(request.zone_id):
            body['zoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstance',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/instance/create',
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

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/instance/delete',
            method = 'DELETE',
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
        request: main_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/instance/delete',
            method = 'DELETE',
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
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(request, headers, runtime)

    async def delete_instance_async(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(request, headers, runtime)

    def describe_access_control_list_with_options(
        self,
        request: main_models.DescribeAccessControlListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessControlListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessControlList',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/milvus/describe_access_control_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_control_list_with_options_async(
        self,
        request: main_models.DescribeAccessControlListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccessControlListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccessControlList',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/milvus/describe_access_control_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccessControlListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_control_list(
        self,
        request: main_models.DescribeAccessControlListRequest,
    ) -> main_models.DescribeAccessControlListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_access_control_list_with_options(request, headers, runtime)

    async def describe_access_control_list_async(
        self,
        request: main_models.DescribeAccessControlListRequest,
    ) -> main_models.DescribeAccessControlListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_access_control_list_with_options_async(request, headers, runtime)

    def describe_instance_configs_with_options(
        self,
        request: main_models.DescribeInstanceConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceConfigs',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/describe_milvus_user_config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_configs_with_options_async(
        self,
        request: main_models.DescribeInstanceConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceConfigs',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/describe_milvus_user_config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_configs(
        self,
        request: main_models.DescribeInstanceConfigsRequest,
    ) -> main_models.DescribeInstanceConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_instance_configs_with_options(request, headers, runtime)

    async def describe_instance_configs_async(
        self,
        request: main_models.DescribeInstanceConfigsRequest,
    ) -> main_models.DescribeInstanceConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_instance_configs_with_options_async(request, headers, runtime)

    def get_instance_with_options(
        self,
        request: main_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/instance/get',
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
        request: main_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/instance/get',
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
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(request, headers, runtime)

    async def get_instance_async(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(request, headers, runtime)

    def get_instance_detail_with_options(
        self,
        request: main_models.GetInstanceDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceDetail',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/cluster/detail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_detail_with_options_async(
        self,
        request: main_models.GetInstanceDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceDetail',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/cluster/detail',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_detail(
        self,
        request: main_models.GetInstanceDetailRequest,
    ) -> main_models.GetInstanceDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_instance_detail_with_options(request, headers, runtime)

    async def get_instance_detail_async(
        self,
        request: main_models.GetInstanceDetailRequest,
    ) -> main_models.GetInstanceDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_instance_detail_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        tmp_req: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        tmp_req.validate()
        request = main_models.ListInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/order/list',
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
        tmp_req: main_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesResponse:
        tmp_req.validate()
        request = main_models.ListInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstances',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/order/list',
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

    def list_instances_v2with_options(
        self,
        tmp_req: main_models.ListInstancesV2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesV2Response:
        tmp_req.validate()
        request = main_models.ListInstancesV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancesV2',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/instance/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesV2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_v2with_options_async(
        self,
        tmp_req: main_models.ListInstancesV2Request,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancesV2Response:
        tmp_req.validate()
        request = main_models.ListInstancesV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.instance_id):
            query['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            query['instanceName'] = request.instance_name
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancesV2',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/instance/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancesV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_v2(
        self,
        request: main_models.ListInstancesV2Request,
    ) -> main_models.ListInstancesV2Response:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_instances_v2with_options(request, headers, runtime)

    async def list_instances_v2_async(
        self,
        request: main_models.ListInstancesV2Request,
    ) -> main_models.ListInstancesV2Response:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_instances_v2with_options_async(request, headers, runtime)

    def modify_instance_config_with_options(
        self,
        request: main_models.ModifyInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        if not DaraCore.is_null(request.user_config):
            query['UserConfig'] = request.user_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceConfig',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/modify_milvus_config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_config_with_options_async(
        self,
        request: main_models.ModifyInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        if not DaraCore.is_null(request.user_config):
            query['UserConfig'] = request.user_config
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceConfig',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/config/modify_milvus_config',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_config(
        self,
        request: main_models.ModifyInstanceConfigRequest,
    ) -> main_models.ModifyInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.modify_instance_config_with_options(request, headers, runtime)

    async def modify_instance_config_async(
        self,
        request: main_models.ModifyInstanceConfigRequest,
    ) -> main_models.ModifyInstanceConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.modify_instance_config_with_options_async(request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/tags',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def un_tag_resources_with_options(
        self,
        tmp_req: main_models.UnTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
        tmp_req.validate()
        request = main_models.UnTagResourcesShrinkRequest()
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
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagResources',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        tmp_req: main_models.UnTagResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
        tmp_req.validate()
        request = main_models.UnTagResourcesShrinkRequest()
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
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagResources',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/tags',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: main_models.UnTagResourcesRequest,
    ) -> main_models.UnTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.un_tag_resources_with_options(request, headers, runtime)

    async def un_tag_resources_async(
        self,
        request: main_models.UnTagResourcesRequest,
    ) -> main_models.UnTagResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.un_tag_resources_with_options_async(request, headers, runtime)

    def update_access_control_list_with_options(
        self,
        request: main_models.UpdateAccessControlListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccessControlListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccessControlList',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/milvus/update_access_control_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_access_control_list_with_options_async(
        self,
        request: main_models.UpdateAccessControlListRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccessControlListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.acl_id):
            query['AclId'] = request.acl_id
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccessControlList',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/milvus/update_access_control_list',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccessControlListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_access_control_list(
        self,
        request: main_models.UpdateAccessControlListRequest,
    ) -> main_models.UpdateAccessControlListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_access_control_list_with_options(request, headers, runtime)

    async def update_access_control_list_async(
        self,
        request: main_models.UpdateAccessControlListRequest,
    ) -> main_models.UpdateAccessControlListResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_access_control_list_with_options_async(request, headers, runtime)

    def update_instance_with_options(
        self,
        request: main_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.auto_backup):
            body['autoBackup'] = request.auto_backup
        if not DaraCore.is_null(request.components):
            body['components'] = request.components
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.ha):
            body['ha'] = request.ha
        if not DaraCore.is_null(request.instance_id):
            body['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/instance/update',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: main_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.auto_backup):
            body['autoBackup'] = request.auto_backup
        if not DaraCore.is_null(request.components):
            body['components'] = request.components
        if not DaraCore.is_null(request.configuration):
            body['configuration'] = request.configuration
        if not DaraCore.is_null(request.ha):
            body['ha'] = request.ha
        if not DaraCore.is_null(request.instance_id):
            body['instanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstance',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/instance/update',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(request, headers, runtime)

    async def update_instance_async(
        self,
        request: main_models.UpdateInstanceRequest,
    ) -> main_models.UpdateInstanceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(request, headers, runtime)

    def update_instance_name_with_options(
        self,
        request: main_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceName',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/cluster/update_name',
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
        request: main_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceName',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/cluster/update_name',
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
        request: main_models.UpdateInstanceNameRequest,
    ) -> main_models.UpdateInstanceNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_instance_name_with_options(request, headers, runtime)

    async def update_instance_name_async(
        self,
        request: main_models.UpdateInstanceNameRequest,
    ) -> main_models.UpdateInstanceNameResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_instance_name_with_options_async(request, headers, runtime)

    def update_public_network_status_with_options(
        self,
        request: main_models.UpdatePublicNetworkStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePublicNetworkStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.component_type):
            query['ComponentType'] = request.component_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.public_network_enabled):
            query['PublicNetworkEnabled'] = request.public_network_enabled
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePublicNetworkStatus',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/network/updatePublicNetworkStatus',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePublicNetworkStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_public_network_status_with_options_async(
        self,
        request: main_models.UpdatePublicNetworkStatusRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePublicNetworkStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cidr):
            query['Cidr'] = request.cidr
        if not DaraCore.is_null(request.component_type):
            query['ComponentType'] = request.component_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.public_network_enabled):
            query['PublicNetworkEnabled'] = request.public_network_enabled
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePublicNetworkStatus',
            version = '2023-10-12',
            protocol = 'HTTPS',
            pathname = f'/webapi/network/updatePublicNetworkStatus',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePublicNetworkStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_public_network_status(
        self,
        request: main_models.UpdatePublicNetworkStatusRequest,
    ) -> main_models.UpdatePublicNetworkStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_public_network_status_with_options(request, headers, runtime)

    async def update_public_network_status_async(
        self,
        request: main_models.UpdatePublicNetworkStatusRequest,
    ) -> main_models.UpdatePublicNetworkStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_public_network_status_with_options_async(request, headers, runtime)
