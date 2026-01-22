# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_polardbx20200202 import models as main_models
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
            'ap-northeast-1': 'polardbx.aliyuncs.com',
            'ap-northeast-2-pop': 'polardbx.aliyuncs.com',
            'ap-south-1': 'polardbx.aliyuncs.com',
            'ap-southeast-2': 'polardbx.aliyuncs.com',
            'ap-southeast-3': 'polardbx.aliyuncs.com',
            'ap-southeast-5': 'polardbx.aliyuncs.com',
            'cn-beijing-finance-1': 'polardbx.aliyuncs.com',
            'cn-beijing-finance-pop': 'polardbx.aliyuncs.com',
            'cn-beijing-gov-1': 'polardbx.aliyuncs.com',
            'cn-beijing-nu16-b01': 'polardbx.aliyuncs.com',
            'cn-edge-1': 'polardbx.aliyuncs.com',
            'cn-fujian': 'polardbx.aliyuncs.com',
            'cn-haidian-cm12-c01': 'polardbx.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'polardbx.aliyuncs.com',
            'cn-hangzhou-finance': 'polardbx.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'polardbx.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'polardbx.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'polardbx.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'polardbx.aliyuncs.com',
            'cn-hangzhou-test-306': 'polardbx.aliyuncs.com',
            'cn-hongkong-finance-pop': 'polardbx.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'polardbx.aliyuncs.com',
            'cn-north-2-gov-1': 'polardbx.aliyuncs.com',
            'cn-qingdao-nebula': 'polardbx.aliyuncs.com',
            'cn-shanghai-et15-b01': 'polardbx.aliyuncs.com',
            'cn-shanghai-et2-b01': 'polardbx.aliyuncs.com',
            'cn-shanghai-finance-1': 'polardbx.aliyuncs.com',
            'cn-shanghai-inner': 'polardbx.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'polardbx.aliyuncs.com',
            'cn-shenzhen-finance-1': 'polardbx.aliyuncs.com',
            'cn-shenzhen-inner': 'polardbx.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'polardbx.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'polardbx.aliyuncs.com',
            'cn-wuhan': 'polardbx.aliyuncs.com',
            'cn-wulanchabu': 'polardbx.aliyuncs.com',
            'cn-yushanfang': 'polardbx.aliyuncs.com',
            'cn-zhangbei': 'polardbx.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'polardbx.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'polardbx.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'polardbx.aliyuncs.com',
            'eu-central-1': 'polardbx.aliyuncs.com',
            'eu-west-1': 'polardbx.aliyuncs.com',
            'eu-west-1-oxs': 'polardbx.aliyuncs.com',
            'me-east-1': 'polardbx.aliyuncs.com',
            'rus-west-1-pop': 'polardbx.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('polardbx', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def align_storage_primary_azone_with_options(
        self,
        request: main_models.AlignStoragePrimaryAzoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AlignStoragePrimaryAzoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.storage_instance_name):
            query['StorageInstanceName'] = request.storage_instance_name
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AlignStoragePrimaryAzone',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AlignStoragePrimaryAzoneResponse(),
            self.call_api(params, req, runtime)
        )

    async def align_storage_primary_azone_with_options_async(
        self,
        request: main_models.AlignStoragePrimaryAzoneRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AlignStoragePrimaryAzoneResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.storage_instance_name):
            query['StorageInstanceName'] = request.storage_instance_name
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AlignStoragePrimaryAzone',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AlignStoragePrimaryAzoneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def align_storage_primary_azone(
        self,
        request: main_models.AlignStoragePrimaryAzoneRequest,
    ) -> main_models.AlignStoragePrimaryAzoneResponse:
        runtime = RuntimeOptions()
        return self.align_storage_primary_azone_with_options(request, runtime)

    async def align_storage_primary_azone_async(
        self,
        request: main_models.AlignStoragePrimaryAzoneRequest,
    ) -> main_models.AlignStoragePrimaryAzoneResponse:
        runtime = RuntimeOptions()
        return await self.align_storage_primary_azone_with_options_async(request, runtime)

    def allocate_cold_data_volume_with_options(
        self,
        request: main_models.AllocateColdDataVolumeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateColdDataVolumeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateColdDataVolume',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateColdDataVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_cold_data_volume_with_options_async(
        self,
        request: main_models.AllocateColdDataVolumeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateColdDataVolumeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocateColdDataVolume',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AllocateColdDataVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_cold_data_volume(
        self,
        request: main_models.AllocateColdDataVolumeRequest,
    ) -> main_models.AllocateColdDataVolumeResponse:
        runtime = RuntimeOptions()
        return self.allocate_cold_data_volume_with_options(request, runtime)

    async def allocate_cold_data_volume_async(
        self,
        request: main_models.AllocateColdDataVolumeRequest,
    ) -> main_models.AllocateColdDataVolumeResponse:
        runtime = RuntimeOptions()
        return await self.allocate_cold_data_volume_with_options_async(request, runtime)

    def allocate_instance_public_connection_with_options(
        self,
        request: main_models.AllocateInstancePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocateInstancePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
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
            action = 'AllocateInstancePublicConnection',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
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
            action = 'AllocateInstancePublicConnection',
            version = '2020-02-02',
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

    def attach_columnar_instance_with_options(
        self,
        request: main_models.AttachColumnarInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachColumnarInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachColumnarInstance',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachColumnarInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_columnar_instance_with_options_async(
        self,
        request: main_models.AttachColumnarInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachColumnarInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachColumnarInstance',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachColumnarInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_columnar_instance(
        self,
        request: main_models.AttachColumnarInstanceRequest,
    ) -> main_models.AttachColumnarInstanceResponse:
        runtime = RuntimeOptions()
        return self.attach_columnar_instance_with_options(request, runtime)

    async def attach_columnar_instance_async(
        self,
        request: main_models.AttachColumnarInstanceRequest,
    ) -> main_models.AttachColumnarInstanceResponse:
        runtime = RuntimeOptions()
        return await self.attach_columnar_instance_with_options_async(request, runtime)

    def cancel_active_operation_tasks_with_options(
        self,
        request: main_models.CancelActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelActiveOperationTasksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelActiveOperationTasks',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelActiveOperationTasks',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
            version = '2020-02-02',
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
            version = '2020-02-02',
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

    def check_cloud_resource_authorized_with_options(
        self,
        request: main_models.CheckCloudResourceAuthorizedRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCloudResourceAuthorizedResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCloudResourceAuthorized',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_arn):
            query['RoleArn'] = request.role_arn
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCloudResourceAuthorized',
            version = '2020-02-02',
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

    def check_sql_audit_sls_status_with_options(
        self,
        request: main_models.CheckSqlAuditSlsStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckSqlAuditSlsStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckSqlAuditSlsStatus',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckSqlAuditSlsStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_sql_audit_sls_status_with_options_async(
        self,
        request: main_models.CheckSqlAuditSlsStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckSqlAuditSlsStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckSqlAuditSlsStatus',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckSqlAuditSlsStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_sql_audit_sls_status(
        self,
        request: main_models.CheckSqlAuditSlsStatusRequest,
    ) -> main_models.CheckSqlAuditSlsStatusResponse:
        runtime = RuntimeOptions()
        return self.check_sql_audit_sls_status_with_options(request, runtime)

    async def check_sql_audit_sls_status_async(
        self,
        request: main_models.CheckSqlAuditSlsStatusRequest,
    ) -> main_models.CheckSqlAuditSlsStatusResponse:
        runtime = RuntimeOptions()
        return await self.check_sql_audit_sls_status_with_options_async(request, runtime)

    def close_engine_migration_with_options(
        self,
        request: main_models.CloseEngineMigrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseEngineMigrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.continue_enable_binlog):
            query['ContinueEnableBinlog'] = request.continue_enable_binlog
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseEngineMigration',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseEngineMigrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_engine_migration_with_options_async(
        self,
        request: main_models.CloseEngineMigrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseEngineMigrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.continue_enable_binlog):
            query['ContinueEnableBinlog'] = request.continue_enable_binlog
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseEngineMigration',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseEngineMigrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_engine_migration(
        self,
        request: main_models.CloseEngineMigrationRequest,
    ) -> main_models.CloseEngineMigrationResponse:
        runtime = RuntimeOptions()
        return self.close_engine_migration_with_options(request, runtime)

    async def close_engine_migration_async(
        self,
        request: main_models.CloseEngineMigrationRequest,
    ) -> main_models.CloseEngineMigrationResponse:
        runtime = RuntimeOptions()
        return await self.close_engine_migration_with_options_async(request, runtime)

    def confirm_no_connection_with_options(
        self,
        request: main_models.ConfirmNoConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmNoConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmNoConnection',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmNoConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_no_connection_with_options_async(
        self,
        request: main_models.ConfirmNoConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfirmNoConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfirmNoConnection',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfirmNoConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_no_connection(
        self,
        request: main_models.ConfirmNoConnectionRequest,
    ) -> main_models.ConfirmNoConnectionResponse:
        runtime = RuntimeOptions()
        return self.confirm_no_connection_with_options(request, runtime)

    async def confirm_no_connection_async(
        self,
        request: main_models.ConfirmNoConnectionRequest,
    ) -> main_models.ConfirmNoConnectionResponse:
        runtime = RuntimeOptions()
        return await self.confirm_no_connection_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackup',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackup',
            version = '2020-02-02',
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

    def create_custom_endpoint_with_options(
        self,
        request: main_models.CreateCustomEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.node_auto_enter):
            query['NodeAutoEnter'] = request.node_auto_enter
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.node_role):
            query['NodeRole'] = request.node_role
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomEndpoint',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_endpoint_with_options_async(
        self,
        request: main_models.CreateCustomEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.node_auto_enter):
            query['NodeAutoEnter'] = request.node_auto_enter
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.node_role):
            query['NodeRole'] = request.node_role
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomEndpoint',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_endpoint(
        self,
        request: main_models.CreateCustomEndpointRequest,
    ) -> main_models.CreateCustomEndpointResponse:
        runtime = RuntimeOptions()
        return self.create_custom_endpoint_with_options(request, runtime)

    async def create_custom_endpoint_async(
        self,
        request: main_models.CreateCustomEndpointRequest,
    ) -> main_models.CreateCustomEndpointResponse:
        runtime = RuntimeOptions()
        return await self.create_custom_endpoint_with_options_async(request, runtime)

    def create_dbwith_options(
        self,
        request: main_models.CreateDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not DaraCore.is_null(request.charset):
            query['Charset'] = request.charset
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.db_description):
            query['DbDescription'] = request.db_description
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        if not DaraCore.is_null(request.storage_pool_name):
            query['StoragePoolName'] = request.storage_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDB',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbwith_options_async(
        self,
        request: main_models.CreateDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not DaraCore.is_null(request.charset):
            query['Charset'] = request.charset
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.db_description):
            query['DbDescription'] = request.db_description
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        if not DaraCore.is_null(request.storage_pool_name):
            query['StoragePoolName'] = request.storage_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDB',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_db(
        self,
        request: main_models.CreateDBRequest,
    ) -> main_models.CreateDBResponse:
        runtime = RuntimeOptions()
        return self.create_dbwith_options(request, runtime)

    async def create_db_async(
        self,
        request: main_models.CreateDBRequest,
    ) -> main_models.CreateDBResponse:
        runtime = RuntimeOptions()
        return await self.create_dbwith_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        tmp_req: main_models.CreateDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDBInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateDBInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.extra_params):
            request.extra_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra_params, 'ExtraParams', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.cnnode_count):
            query['CNNodeCount'] = request.cnnode_count
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cn_class):
            query['CnClass'] = request.cn_class
        if not DaraCore.is_null(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not DaraCore.is_null(request.dbnode_count):
            query['DBNodeCount'] = request.dbnode_count
        if not DaraCore.is_null(request.dnnode_count):
            query['DNNodeCount'] = request.dnnode_count
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dn_class):
            query['DnClass'] = request.dn_class
        if not DaraCore.is_null(request.dn_storage_space):
            query['DnStorageSpace'] = request.dn_storage_space
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.extra_params_shrink):
            query['ExtraParams'] = request.extra_params_shrink
        if not DaraCore.is_null(request.is_columnar_read_dbinstance):
            query['IsColumnarReadDBInstance'] = request.is_columnar_read_dbinstance
        if not DaraCore.is_null(request.is_read_dbinstance):
            query['IsReadDBInstance'] = request.is_read_dbinstance
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.primary_dbinstance_name):
            query['PrimaryDBInstanceName'] = request.primary_dbinstance_name
        if not DaraCore.is_null(request.primary_zone):
            query['PrimaryZone'] = request.primary_zone
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.secondary_zone):
            query['SecondaryZone'] = request.secondary_zone
        if not DaraCore.is_null(request.series):
            query['Series'] = request.series
        if not DaraCore.is_null(request.tertiary_zone):
            query['TertiaryZone'] = request.tertiary_zone
        if not DaraCore.is_null(request.topology_type):
            query['TopologyType'] = request.topology_type
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBInstance',
            version = '2020-02-02',
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
        if not DaraCore.is_null(tmp_req.extra_params):
            request.extra_params_shrink = Utils.array_to_string_with_specified_style(tmp_req.extra_params, 'ExtraParams', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.cnnode_count):
            query['CNNodeCount'] = request.cnnode_count
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cn_class):
            query['CnClass'] = request.cn_class
        if not DaraCore.is_null(request.dbnode_class):
            query['DBNodeClass'] = request.dbnode_class
        if not DaraCore.is_null(request.dbnode_count):
            query['DBNodeCount'] = request.dbnode_count
        if not DaraCore.is_null(request.dnnode_count):
            query['DNNodeCount'] = request.dnnode_count
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.dn_class):
            query['DnClass'] = request.dn_class
        if not DaraCore.is_null(request.dn_storage_space):
            query['DnStorageSpace'] = request.dn_storage_space
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.extra_params_shrink):
            query['ExtraParams'] = request.extra_params_shrink
        if not DaraCore.is_null(request.is_columnar_read_dbinstance):
            query['IsColumnarReadDBInstance'] = request.is_columnar_read_dbinstance
        if not DaraCore.is_null(request.is_read_dbinstance):
            query['IsReadDBInstance'] = request.is_read_dbinstance
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.primary_dbinstance_name):
            query['PrimaryDBInstanceName'] = request.primary_dbinstance_name
        if not DaraCore.is_null(request.primary_zone):
            query['PrimaryZone'] = request.primary_zone
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.secondary_zone):
            query['SecondaryZone'] = request.secondary_zone
        if not DaraCore.is_null(request.series):
            query['Series'] = request.series
        if not DaraCore.is_null(request.tertiary_zone):
            query['TertiaryZone'] = request.tertiary_zone
        if not DaraCore.is_null(request.topology_type):
            query['TopologyType'] = request.topology_type
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        if not DaraCore.is_null(request.vpcid):
            query['VPCId'] = request.vpcid
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDBInstance',
            version = '2020-02-02',
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

    def create_data_import_task_with_options(
        self,
        request: main_models.CreateDataImportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataImportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dst_db):
            query['DstDb'] = request.dst_db
        if not DaraCore.is_null(request.dst_password):
            query['DstPassword'] = request.dst_password
        if not DaraCore.is_null(request.dst_res_id):
            query['DstResId'] = request.dst_res_id
        if not DaraCore.is_null(request.dst_user_name):
            query['DstUserName'] = request.dst_user_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not DaraCore.is_null(request.src_db):
            query['SrcDb'] = request.src_db
        if not DaraCore.is_null(request.src_password):
            query['SrcPassword'] = request.src_password
        if not DaraCore.is_null(request.src_res_id):
            query['SrcResId'] = request.src_res_id
        if not DaraCore.is_null(request.src_user_name):
            query['SrcUserName'] = request.src_user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataImportTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_import_task_with_options_async(
        self,
        request: main_models.CreateDataImportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDataImportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dst_db):
            query['DstDb'] = request.dst_db
        if not DaraCore.is_null(request.dst_password):
            query['DstPassword'] = request.dst_password
        if not DaraCore.is_null(request.dst_res_id):
            query['DstResId'] = request.dst_res_id
        if not DaraCore.is_null(request.dst_user_name):
            query['DstUserName'] = request.dst_user_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not DaraCore.is_null(request.src_db):
            query['SrcDb'] = request.src_db
        if not DaraCore.is_null(request.src_password):
            query['SrcPassword'] = request.src_password
        if not DaraCore.is_null(request.src_res_id):
            query['SrcResId'] = request.src_res_id
        if not DaraCore.is_null(request.src_user_name):
            query['SrcUserName'] = request.src_user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataImportTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDataImportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_import_task(
        self,
        request: main_models.CreateDataImportTaskRequest,
    ) -> main_models.CreateDataImportTaskResponse:
        runtime = RuntimeOptions()
        return self.create_data_import_task_with_options(request, runtime)

    async def create_data_import_task_async(
        self,
        request: main_models.CreateDataImportTaskRequest,
    ) -> main_models.CreateDataImportTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_data_import_task_with_options_async(request, runtime)

    def create_gdn_instance_with_options(
        self,
        request: main_models.CreateGdnInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGdnInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.gdn_mode):
            query['GdnMode'] = request.gdn_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rpl_conflict_strategy):
            query['RplConflictStrategy'] = request.rpl_conflict_strategy
        if not DaraCore.is_null(request.rpl_dml_strategy):
            query['RplDmlStrategy'] = request.rpl_dml_strategy
        if not DaraCore.is_null(request.rpl_sync_ddl):
            query['RplSyncDdl'] = request.rpl_sync_ddl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGdnInstance',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGdnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_gdn_instance_with_options_async(
        self,
        request: main_models.CreateGdnInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGdnInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.gdn_mode):
            query['GdnMode'] = request.gdn_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rpl_conflict_strategy):
            query['RplConflictStrategy'] = request.rpl_conflict_strategy
        if not DaraCore.is_null(request.rpl_dml_strategy):
            query['RplDmlStrategy'] = request.rpl_dml_strategy
        if not DaraCore.is_null(request.rpl_sync_ddl):
            query['RplSyncDdl'] = request.rpl_sync_ddl
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGdnInstance',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGdnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_gdn_instance(
        self,
        request: main_models.CreateGdnInstanceRequest,
    ) -> main_models.CreateGdnInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_gdn_instance_with_options(request, runtime)

    async def create_gdn_instance_async(
        self,
        request: main_models.CreateGdnInstanceRequest,
    ) -> main_models.CreateGdnInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_gdn_instance_with_options_async(request, runtime)

    def create_rpl_inspection_task_with_options(
        self,
        request: main_models.CreateRplInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRplInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dst_db):
            query['DstDb'] = request.dst_db
        if not DaraCore.is_null(request.dst_password):
            query['DstPassword'] = request.dst_password
        if not DaraCore.is_null(request.dst_res_id):
            query['DstResId'] = request.dst_res_id
        if not DaraCore.is_null(request.dst_user_name):
            query['DstUserName'] = request.dst_user_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not DaraCore.is_null(request.src_password):
            query['SrcPassword'] = request.src_password
        if not DaraCore.is_null(request.src_user_name):
            query['SrcUserName'] = request.src_user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRplInspectionTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRplInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rpl_inspection_task_with_options_async(
        self,
        request: main_models.CreateRplInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRplInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dst_db):
            query['DstDb'] = request.dst_db
        if not DaraCore.is_null(request.dst_password):
            query['DstPassword'] = request.dst_password
        if not DaraCore.is_null(request.dst_res_id):
            query['DstResId'] = request.dst_res_id
        if not DaraCore.is_null(request.dst_user_name):
            query['DstUserName'] = request.dst_user_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not DaraCore.is_null(request.src_password):
            query['SrcPassword'] = request.src_password
        if not DaraCore.is_null(request.src_user_name):
            query['SrcUserName'] = request.src_user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRplInspectionTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRplInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rpl_inspection_task(
        self,
        request: main_models.CreateRplInspectionTaskRequest,
    ) -> main_models.CreateRplInspectionTaskResponse:
        runtime = RuntimeOptions()
        return self.create_rpl_inspection_task_with_options(request, runtime)

    async def create_rpl_inspection_task_async(
        self,
        request: main_models.CreateRplInspectionTaskRequest,
    ) -> main_models.CreateRplInspectionTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_rpl_inspection_task_with_options_async(request, runtime)

    def create_sqlevaluate_task_with_options(
        self,
        request: main_models.CreateSQLEvaluateTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSQLEvaluateTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dst_db):
            query['DstDb'] = request.dst_db
        if not DaraCore.is_null(request.dst_password):
            query['DstPassword'] = request.dst_password
        if not DaraCore.is_null(request.dst_res_id):
            query['DstResId'] = request.dst_res_id
        if not DaraCore.is_null(request.dst_user_name):
            query['DstUserName'] = request.dst_user_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_desc):
            query['SlinkTaskDesc'] = request.slink_task_desc
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not DaraCore.is_null(request.src_db):
            query['SrcDb'] = request.src_db
        if not DaraCore.is_null(request.src_password):
            query['SrcPassword'] = request.src_password
        if not DaraCore.is_null(request.src_res_id):
            query['SrcResId'] = request.src_res_id
        if not DaraCore.is_null(request.src_res_type):
            query['SrcResType'] = request.src_res_type
        if not DaraCore.is_null(request.src_user_name):
            query['SrcUserName'] = request.src_user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSQLEvaluateTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSQLEvaluateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sqlevaluate_task_with_options_async(
        self,
        request: main_models.CreateSQLEvaluateTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSQLEvaluateTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dst_db):
            query['DstDb'] = request.dst_db
        if not DaraCore.is_null(request.dst_password):
            query['DstPassword'] = request.dst_password
        if not DaraCore.is_null(request.dst_res_id):
            query['DstResId'] = request.dst_res_id
        if not DaraCore.is_null(request.dst_user_name):
            query['DstUserName'] = request.dst_user_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_desc):
            query['SlinkTaskDesc'] = request.slink_task_desc
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not DaraCore.is_null(request.src_db):
            query['SrcDb'] = request.src_db
        if not DaraCore.is_null(request.src_password):
            query['SrcPassword'] = request.src_password
        if not DaraCore.is_null(request.src_res_id):
            query['SrcResId'] = request.src_res_id
        if not DaraCore.is_null(request.src_res_type):
            query['SrcResType'] = request.src_res_type
        if not DaraCore.is_null(request.src_user_name):
            query['SrcUserName'] = request.src_user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSQLEvaluateTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSQLEvaluateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sqlevaluate_task(
        self,
        request: main_models.CreateSQLEvaluateTaskRequest,
    ) -> main_models.CreateSQLEvaluateTaskResponse:
        runtime = RuntimeOptions()
        return self.create_sqlevaluate_task_with_options(request, runtime)

    async def create_sqlevaluate_task_async(
        self,
        request: main_models.CreateSQLEvaluateTaskRequest,
    ) -> main_models.CreateSQLEvaluateTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_sqlevaluate_task_with_options_async(request, runtime)

    def create_storage_pool_with_options(
        self,
        request: main_models.CreateStoragePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStoragePoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.storage_pool_dnlist):
            query['StoragePoolDNList'] = request.storage_pool_dnlist
        if not DaraCore.is_null(request.storage_pool_name):
            query['StoragePoolName'] = request.storage_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStoragePool',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStoragePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_storage_pool_with_options_async(
        self,
        request: main_models.CreateStoragePoolRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStoragePoolResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.storage_pool_dnlist):
            query['StoragePoolDNList'] = request.storage_pool_dnlist
        if not DaraCore.is_null(request.storage_pool_name):
            query['StoragePoolName'] = request.storage_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStoragePool',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStoragePoolResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_storage_pool(
        self,
        request: main_models.CreateStoragePoolRequest,
    ) -> main_models.CreateStoragePoolResponse:
        runtime = RuntimeOptions()
        return self.create_storage_pool_with_options(request, runtime)

    async def create_storage_pool_async(
        self,
        request: main_models.CreateStoragePoolRequest,
    ) -> main_models.CreateStoragePoolResponse:
        runtime = RuntimeOptions()
        return await self.create_storage_pool_with_options_async(request, runtime)

    def create_structure_import_task_with_options(
        self,
        request: main_models.CreateStructureImportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStructureImportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStructureImportTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStructureImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_structure_import_task_with_options_async(
        self,
        request: main_models.CreateStructureImportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStructureImportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStructureImportTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStructureImportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_structure_import_task(
        self,
        request: main_models.CreateStructureImportTaskRequest,
    ) -> main_models.CreateStructureImportTaskResponse:
        runtime = RuntimeOptions()
        return self.create_structure_import_task_with_options(request, runtime)

    async def create_structure_import_task_async(
        self,
        request: main_models.CreateStructureImportTaskRequest,
    ) -> main_models.CreateStructureImportTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_structure_import_task_with_options_async(request, runtime)

    def create_super_account_with_options(
        self,
        request: main_models.CreateSuperAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSuperAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSuperAccount',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSuperAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_super_account_with_options_async(
        self,
        request: main_models.CreateSuperAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSuperAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_description):
            query['AccountDescription'] = request.account_description
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSuperAccount',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSuperAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_super_account(
        self,
        request: main_models.CreateSuperAccountRequest,
    ) -> main_models.CreateSuperAccountResponse:
        runtime = RuntimeOptions()
        return self.create_super_account_with_options(request, runtime)

    async def create_super_account_async(
        self,
        request: main_models.CreateSuperAccountRequest,
    ) -> main_models.CreateSuperAccountResponse:
        runtime = RuntimeOptions()
        return await self.create_super_account_with_options_async(request, runtime)

    def create_transform_operation_with_options(
        self,
        request: main_models.CreateTransformOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransformOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.operation):
            query['Operation'] = request.operation
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransformOperation',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransformOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_transform_operation_with_options_async(
        self,
        request: main_models.CreateTransformOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTransformOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.operation):
            query['Operation'] = request.operation
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTransformOperation',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTransformOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_transform_operation(
        self,
        request: main_models.CreateTransformOperationRequest,
    ) -> main_models.CreateTransformOperationResponse:
        runtime = RuntimeOptions()
        return self.create_transform_operation_with_options(request, runtime)

    async def create_transform_operation_async(
        self,
        request: main_models.CreateTransformOperationRequest,
    ) -> main_models.CreateTransformOperationResponse:
        runtime = RuntimeOptions()
        return await self.create_transform_operation_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: main_models.DeleteAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2020-02-02',
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

    def delete_custom_endpoint_with_options(
        self,
        request: main_models.DeleteCustomEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_endpoint_id):
            query['CustomEndpointId'] = request.custom_endpoint_id
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomEndpoint',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_endpoint_with_options_async(
        self,
        request: main_models.DeleteCustomEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_endpoint_id):
            query['CustomEndpointId'] = request.custom_endpoint_id
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomEndpoint',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_endpoint(
        self,
        request: main_models.DeleteCustomEndpointRequest,
    ) -> main_models.DeleteCustomEndpointResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_endpoint_with_options(request, runtime)

    async def delete_custom_endpoint_async(
        self,
        request: main_models.DeleteCustomEndpointRequest,
    ) -> main_models.DeleteCustomEndpointResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_endpoint_with_options_async(request, runtime)

    def delete_dbwith_options(
        self,
        request: main_models.DeleteDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDB',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbwith_options_async(
        self,
        request: main_models.DeleteDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDB',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_db(
        self,
        request: main_models.DeleteDBRequest,
    ) -> main_models.DeleteDBResponse:
        runtime = RuntimeOptions()
        return self.delete_dbwith_options(request, runtime)

    async def delete_db_async(
        self,
        request: main_models.DeleteDBRequest,
    ) -> main_models.DeleteDBResponse:
        runtime = RuntimeOptions()
        return await self.delete_dbwith_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: main_models.DeleteDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBInstance',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDBInstance',
            version = '2020-02-02',
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

    def delete_evaluate_and_import_task_with_options(
        self,
        request: main_models.DeleteEvaluateAndImportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEvaluateAndImportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEvaluateAndImportTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEvaluateAndImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_evaluate_and_import_task_with_options_async(
        self,
        request: main_models.DeleteEvaluateAndImportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEvaluateAndImportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEvaluateAndImportTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEvaluateAndImportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_evaluate_and_import_task(
        self,
        request: main_models.DeleteEvaluateAndImportTaskRequest,
    ) -> main_models.DeleteEvaluateAndImportTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_evaluate_and_import_task_with_options(request, runtime)

    async def delete_evaluate_and_import_task_async(
        self,
        request: main_models.DeleteEvaluateAndImportTaskRequest,
    ) -> main_models.DeleteEvaluateAndImportTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_evaluate_and_import_task_with_options_async(request, runtime)

    def delete_gdn_instance_with_options(
        self,
        request: main_models.DeleteGdnInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGdnInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gdn_instance_name):
            query['GdnInstanceName'] = request.gdn_instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGdnInstance',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGdnInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_gdn_instance_with_options_async(
        self,
        request: main_models.DeleteGdnInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGdnInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.gdn_instance_name):
            query['GdnInstanceName'] = request.gdn_instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGdnInstance',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGdnInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_gdn_instance(
        self,
        request: main_models.DeleteGdnInstanceRequest,
    ) -> main_models.DeleteGdnInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_gdn_instance_with_options(request, runtime)

    async def delete_gdn_instance_async(
        self,
        request: main_models.DeleteGdnInstanceRequest,
    ) -> main_models.DeleteGdnInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_gdn_instance_with_options_async(request, runtime)

    def describe_account_list_with_options(
        self,
        request: main_models.DescribeAccountListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_list_with_options_async(
        self,
        request: main_models.DescribeAccountListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_type):
            query['AccountType'] = request.account_type
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccountList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAccountListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_list(
        self,
        request: main_models.DescribeAccountListRequest,
    ) -> main_models.DescribeAccountListResponse:
        runtime = RuntimeOptions()
        return self.describe_account_list_with_options(request, runtime)

    async def describe_account_list_async(
        self,
        request: main_models.DescribeAccountListRequest,
    ) -> main_models.DescribeAccountListResponse:
        runtime = RuntimeOptions()
        return await self.describe_account_list_with_options_async(request, runtime)

    def describe_active_operation_maintain_conf_with_options(
        self,
        request: main_models.DescribeActiveOperationMaintainConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationMaintainConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationMaintainConf',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationMaintainConf',
            version = '2020-02-02',
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

    def describe_active_operation_task_count_with_options(
        self,
        request: main_models.DescribeActiveOperationTaskCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTaskCountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTaskCount',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTaskCount',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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

    def describe_active_operation_tasks_with_options(
        self,
        request: main_models.DescribeActiveOperationTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveOperationTasksResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTasks',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveOperationTasks',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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

    def describe_archive_table_list_with_options(
        self,
        request: main_models.DescribeArchiveTableListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeArchiveTableListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeArchiveTableList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeArchiveTableListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_archive_table_list_with_options_async(
        self,
        request: main_models.DescribeArchiveTableListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeArchiveTableListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.page_index):
            query['PageIndex'] = request.page_index
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeArchiveTableList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeArchiveTableListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_archive_table_list(
        self,
        request: main_models.DescribeArchiveTableListRequest,
    ) -> main_models.DescribeArchiveTableListResponse:
        runtime = RuntimeOptions()
        return self.describe_archive_table_list_with_options(request, runtime)

    async def describe_archive_table_list_async(
        self,
        request: main_models.DescribeArchiveTableListRequest,
    ) -> main_models.DescribeArchiveTableListResponse:
        runtime = RuntimeOptions()
        return await self.describe_archive_table_list_with_options_async(request, runtime)

    def describe_available_cross_regions_with_options(
        self,
        request: main_models.DescribeAvailableCrossRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableCrossRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableCrossRegions',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableCrossRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_cross_regions_with_options_async(
        self,
        request: main_models.DescribeAvailableCrossRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableCrossRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableCrossRegions',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAvailableCrossRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_cross_regions(
        self,
        request: main_models.DescribeAvailableCrossRegionsRequest,
    ) -> main_models.DescribeAvailableCrossRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_available_cross_regions_with_options(request, runtime)

    async def describe_available_cross_regions_async(
        self,
        request: main_models.DescribeAvailableCrossRegionsRequest,
    ) -> main_models.DescribeAvailableCrossRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_available_cross_regions_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: main_models.DescribeBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2020-02-02',
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

    def describe_backup_set_with_options(
        self,
        request: main_models.DescribeBackupSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dest_cross_region):
            query['DestCrossRegion'] = request.dest_cross_region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupSet',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_set_with_options_async(
        self,
        request: main_models.DescribeBackupSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dest_cross_region):
            query['DestCrossRegion'] = request.dest_cross_region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupSet',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_set(
        self,
        request: main_models.DescribeBackupSetRequest,
    ) -> main_models.DescribeBackupSetResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_set_with_options(request, runtime)

    async def describe_backup_set_async(
        self,
        request: main_models.DescribeBackupSetRequest,
    ) -> main_models.DescribeBackupSetResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_set_with_options_async(request, runtime)

    def describe_backup_set_list_with_options(
        self,
        request: main_models.DescribeBackupSetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupSetListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupSetList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupSetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_set_list_with_options_async(
        self,
        request: main_models.DescribeBackupSetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupSetListResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupSetList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupSetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_set_list(
        self,
        request: main_models.DescribeBackupSetListRequest,
    ) -> main_models.DescribeBackupSetListResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_set_list_with_options(request, runtime)

    async def describe_backup_set_list_async(
        self,
        request: main_models.DescribeBackupSetListRequest,
    ) -> main_models.DescribeBackupSetListResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_set_list_with_options_async(request, runtime)

    def describe_binary_log_list_with_options(
        self,
        request: main_models.DescribeBinaryLogListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBinaryLogListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBinaryLogList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBinaryLogListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_binary_log_list_with_options_async(
        self,
        request: main_models.DescribeBinaryLogListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBinaryLogListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBinaryLogList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBinaryLogListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_binary_log_list(
        self,
        request: main_models.DescribeBinaryLogListRequest,
    ) -> main_models.DescribeBinaryLogListResponse:
        runtime = RuntimeOptions()
        return self.describe_binary_log_list_with_options(request, runtime)

    async def describe_binary_log_list_async(
        self,
        request: main_models.DescribeBinaryLogListRequest,
    ) -> main_models.DescribeBinaryLogListResponse:
        runtime = RuntimeOptions()
        return await self.describe_binary_log_list_with_options_async(request, runtime)

    def describe_cdc_class_list_with_options(
        self,
        request: main_models.DescribeCdcClassListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdcClassListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdcClassList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdcClassListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdc_class_list_with_options_async(
        self,
        request: main_models.DescribeCdcClassListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdcClassListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdcClassList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdcClassListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdc_class_list(
        self,
        request: main_models.DescribeCdcClassListRequest,
    ) -> main_models.DescribeCdcClassListResponse:
        runtime = RuntimeOptions()
        return self.describe_cdc_class_list_with_options(request, runtime)

    async def describe_cdc_class_list_async(
        self,
        request: main_models.DescribeCdcClassListRequest,
    ) -> main_models.DescribeCdcClassListResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdc_class_list_with_options_async(request, runtime)

    def describe_cdc_info_with_options(
        self,
        request: main_models.DescribeCdcInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdcInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdcInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdcInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdc_info_with_options_async(
        self,
        request: main_models.DescribeCdcInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdcInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdcInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdcInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdc_info(
        self,
        request: main_models.DescribeCdcInfoRequest,
    ) -> main_models.DescribeCdcInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_cdc_info_with_options(request, runtime)

    async def describe_cdc_info_async(
        self,
        request: main_models.DescribeCdcInfoRequest,
    ) -> main_models.DescribeCdcInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdc_info_with_options_async(request, runtime)

    def describe_cdc_version_list_with_options(
        self,
        request: main_models.DescribeCdcVersionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdcVersionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdcVersionList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdcVersionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cdc_version_list_with_options_async(
        self,
        request: main_models.DescribeCdcVersionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCdcVersionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCdcVersionList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCdcVersionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cdc_version_list(
        self,
        request: main_models.DescribeCdcVersionListRequest,
    ) -> main_models.DescribeCdcVersionListResponse:
        runtime = RuntimeOptions()
        return self.describe_cdc_version_list_with_options(request, runtime)

    async def describe_cdc_version_list_async(
        self,
        request: main_models.DescribeCdcVersionListRequest,
    ) -> main_models.DescribeCdcVersionListResponse:
        runtime = RuntimeOptions()
        return await self.describe_cdc_version_list_with_options_async(request, runtime)

    def describe_character_set_with_options(
        self,
        request: main_models.DescribeCharacterSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCharacterSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCharacterSet',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCharacterSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_character_set_with_options_async(
        self,
        request: main_models.DescribeCharacterSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCharacterSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCharacterSet',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCharacterSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_character_set(
        self,
        request: main_models.DescribeCharacterSetRequest,
    ) -> main_models.DescribeCharacterSetResponse:
        runtime = RuntimeOptions()
        return self.describe_character_set_with_options(request, runtime)

    async def describe_character_set_async(
        self,
        request: main_models.DescribeCharacterSetRequest,
    ) -> main_models.DescribeCharacterSetResponse:
        runtime = RuntimeOptions()
        return await self.describe_character_set_with_options_async(request, runtime)

    def describe_cold_data_basic_info_with_options(
        self,
        request: main_models.DescribeColdDataBasicInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColdDataBasicInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColdDataBasicInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColdDataBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cold_data_basic_info_with_options_async(
        self,
        request: main_models.DescribeColdDataBasicInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColdDataBasicInfoResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColdDataBasicInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColdDataBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cold_data_basic_info(
        self,
        request: main_models.DescribeColdDataBasicInfoRequest,
    ) -> main_models.DescribeColdDataBasicInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_cold_data_basic_info_with_options(request, runtime)

    async def describe_cold_data_basic_info_async(
        self,
        request: main_models.DescribeColdDataBasicInfoRequest,
    ) -> main_models.DescribeColdDataBasicInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_cold_data_basic_info_with_options_async(request, runtime)

    def describe_columnar_class_list_with_options(
        self,
        request: main_models.DescribeColumnarClassListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnarClassListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumnarClassList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnarClassListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columnar_class_list_with_options_async(
        self,
        request: main_models.DescribeColumnarClassListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnarClassListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumnarClassList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnarClassListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columnar_class_list(
        self,
        request: main_models.DescribeColumnarClassListRequest,
    ) -> main_models.DescribeColumnarClassListResponse:
        runtime = RuntimeOptions()
        return self.describe_columnar_class_list_with_options(request, runtime)

    async def describe_columnar_class_list_async(
        self,
        request: main_models.DescribeColumnarClassListRequest,
    ) -> main_models.DescribeColumnarClassListResponse:
        runtime = RuntimeOptions()
        return await self.describe_columnar_class_list_with_options_async(request, runtime)

    def describe_columnar_info_with_options(
        self,
        request: main_models.DescribeColumnarInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnarInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumnarInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnarInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columnar_info_with_options_async(
        self,
        request: main_models.DescribeColumnarInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnarInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumnarInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnarInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columnar_info(
        self,
        request: main_models.DescribeColumnarInfoRequest,
    ) -> main_models.DescribeColumnarInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_columnar_info_with_options(request, runtime)

    async def describe_columnar_info_async(
        self,
        request: main_models.DescribeColumnarInfoRequest,
    ) -> main_models.DescribeColumnarInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_columnar_info_with_options_async(request, runtime)

    def describe_columnar_version_list_with_options(
        self,
        request: main_models.DescribeColumnarVersionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnarVersionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumnarVersionList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnarVersionListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columnar_version_list_with_options_async(
        self,
        request: main_models.DescribeColumnarVersionListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColumnarVersionListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColumnarVersionList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColumnarVersionListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columnar_version_list(
        self,
        request: main_models.DescribeColumnarVersionListRequest,
    ) -> main_models.DescribeColumnarVersionListResponse:
        runtime = RuntimeOptions()
        return self.describe_columnar_version_list_with_options(request, runtime)

    async def describe_columnar_version_list_async(
        self,
        request: main_models.DescribeColumnarVersionListRequest,
    ) -> main_models.DescribeColumnarVersionListResponse:
        runtime = RuntimeOptions()
        return await self.describe_columnar_version_list_with_options_async(request, runtime)

    def describe_component_propeties_with_options(
        self,
        request: main_models.DescribeComponentPropetiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentPropetiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.component_name):
            query['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentPropeties',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentPropetiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_component_propeties_with_options_async(
        self,
        request: main_models.DescribeComponentPropetiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeComponentPropetiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.component_name):
            query['ComponentName'] = request.component_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeComponentPropeties',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeComponentPropetiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_component_propeties(
        self,
        request: main_models.DescribeComponentPropetiesRequest,
    ) -> main_models.DescribeComponentPropetiesResponse:
        runtime = RuntimeOptions()
        return self.describe_component_propeties_with_options(request, runtime)

    async def describe_component_propeties_async(
        self,
        request: main_models.DescribeComponentPropetiesRequest,
    ) -> main_models.DescribeComponentPropetiesResponse:
        runtime = RuntimeOptions()
        return await self.describe_component_propeties_with_options_async(request, runtime)

    def describe_custom_endpoint_list_with_options(
        self,
        request: main_models.DescribeCustomEndpointListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomEndpointListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_delete_cn):
            query['CheckDeleteCN'] = request.check_delete_cn
        if not DaraCore.is_null(request.custom_endpoint_ids):
            query['CustomEndpointIds'] = request.custom_endpoint_ids
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomEndpointList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomEndpointListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_endpoint_list_with_options_async(
        self,
        request: main_models.DescribeCustomEndpointListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomEndpointListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_delete_cn):
            query['CheckDeleteCN'] = request.check_delete_cn
        if not DaraCore.is_null(request.custom_endpoint_ids):
            query['CustomEndpointIds'] = request.custom_endpoint_ids
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomEndpointList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomEndpointListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_endpoint_list(
        self,
        request: main_models.DescribeCustomEndpointListRequest,
    ) -> main_models.DescribeCustomEndpointListResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_endpoint_list_with_options(request, runtime)

    async def describe_custom_endpoint_list_async(
        self,
        request: main_models.DescribeCustomEndpointListRequest,
    ) -> main_models.DescribeCustomEndpointListResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_endpoint_list_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: main_models.DescribeDBInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceAttribute',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceAttribute',
            version = '2020-02-02',
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

    def describe_dbinstance_config_with_options(
        self,
        request: main_models.DescribeDBInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceConfig',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_config_with_options_async(
        self,
        request: main_models.DescribeDBInstanceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_name):
            query['ConfigName'] = request.config_name
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceConfig',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_config(
        self,
        request: main_models.DescribeDBInstanceConfigRequest,
    ) -> main_models.DescribeDBInstanceConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_config_with_options(request, runtime)

    async def describe_dbinstance_config_async(
        self,
        request: main_models.DescribeDBInstanceConfigRequest,
    ) -> main_models.DescribeDBInstanceConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_config_with_options_async(request, runtime)

    def describe_dbinstance_hawith_options(
        self,
        request: main_models.DescribeDBInstanceHARequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceHAResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceHA',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceHAResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_hawith_options_async(
        self,
        request: main_models.DescribeDBInstanceHARequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceHAResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceHA',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceHAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_ha(
        self,
        request: main_models.DescribeDBInstanceHARequest,
    ) -> main_models.DescribeDBInstanceHAResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_hawith_options(request, runtime)

    async def describe_dbinstance_ha_async(
        self,
        request: main_models.DescribeDBInstanceHARequest,
    ) -> main_models.DescribeDBInstanceHAResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_hawith_options_async(request, runtime)

    def describe_dbinstance_sslwith_options(
        self,
        request: main_models.DescribeDBInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceSSL',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceSSL',
            version = '2020-02-02',
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

    def describe_dbinstance_tdewith_options(
        self,
        request: main_models.DescribeDBInstanceTDERequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceTDEResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceTDE',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_tdewith_options_async(
        self,
        request: main_models.DescribeDBInstanceTDERequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceTDEResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceTDE',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceTDEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_tde(
        self,
        request: main_models.DescribeDBInstanceTDERequest,
    ) -> main_models.DescribeDBInstanceTDEResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_tdewith_options(request, runtime)

    async def describe_dbinstance_tde_async(
        self,
        request: main_models.DescribeDBInstanceTDERequest,
    ) -> main_models.DescribeDBInstanceTDEResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_tdewith_options_async(request, runtime)

    def describe_dbinstance_topology_with_options(
        self,
        request: main_models.DescribeDBInstanceTopologyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceTopologyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.minute_simple):
            query['MinuteSimple'] = request.minute_simple
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceTopology',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_topology_with_options_async(
        self,
        request: main_models.DescribeDBInstanceTopologyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceTopologyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.minute_simple):
            query['MinuteSimple'] = request.minute_simple
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceTopology',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_topology(
        self,
        request: main_models.DescribeDBInstanceTopologyRequest,
    ) -> main_models.DescribeDBInstanceTopologyResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_topology_with_options(request, runtime)

    async def describe_dbinstance_topology_async(
        self,
        request: main_models.DescribeDBInstanceTopologyRequest,
    ) -> main_models.DescribeDBInstanceTopologyResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_topology_with_options_async(request, runtime)

    def describe_dbinstance_via_endpoint_with_options(
        self,
        request: main_models.DescribeDBInstanceViaEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceViaEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceViaEndpoint',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceViaEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_via_endpoint_with_options_async(
        self,
        request: main_models.DescribeDBInstanceViaEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceViaEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceViaEndpoint',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceViaEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_via_endpoint(
        self,
        request: main_models.DescribeDBInstanceViaEndpointRequest,
    ) -> main_models.DescribeDBInstanceViaEndpointResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_via_endpoint_with_options(request, runtime)

    async def describe_dbinstance_via_endpoint_async(
        self,
        request: main_models.DescribeDBInstanceViaEndpointRequest,
    ) -> main_models.DescribeDBInstanceViaEndpointResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_via_endpoint_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        request: main_models.DescribeDBInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_version):
            query['DbVersion'] = request.db_version
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.must_has_cdc):
            query['MustHasCdc'] = request.must_has_cdc
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.series):
            query['Series'] = request.series
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstances',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.db_version):
            query['DbVersion'] = request.db_version
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.must_has_cdc):
            query['MustHasCdc'] = request.must_has_cdc
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.series):
            query['Series'] = request.series
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstances',
            version = '2020-02-02',
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

    def describe_dbnode_performance_with_options(
        self,
        request: main_models.DescribeDBNodePerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBNodePerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not DaraCore.is_null(request.dbnode_role):
            query['DBNodeRole'] = request.dbnode_role
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBNodePerformance',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBNodePerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbnode_performance_with_options_async(
        self,
        request: main_models.DescribeDBNodePerformanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBNodePerformanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not DaraCore.is_null(request.dbnode_role):
            query['DBNodeRole'] = request.dbnode_role
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBNodePerformance',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBNodePerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbnode_performance(
        self,
        request: main_models.DescribeDBNodePerformanceRequest,
    ) -> main_models.DescribeDBNodePerformanceResponse:
        runtime = RuntimeOptions()
        return self.describe_dbnode_performance_with_options(request, runtime)

    async def describe_dbnode_performance_async(
        self,
        request: main_models.DescribeDBNodePerformanceRequest,
    ) -> main_models.DescribeDBNodePerformanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbnode_performance_with_options_async(request, runtime)

    def describe_data_import_task_info_with_options(
        self,
        request: main_models.DescribeDataImportTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataImportTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fail_page_number):
            query['FailPageNumber'] = request.fail_page_number
        if not DaraCore.is_null(request.fail_page_size):
            query['FailPageSize'] = request.fail_page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not DaraCore.is_null(request.success_page_number):
            query['SuccessPageNumber'] = request.success_page_number
        if not DaraCore.is_null(request.success_page_size):
            query['SuccessPageSize'] = request.success_page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataImportTaskInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataImportTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_import_task_info_with_options_async(
        self,
        request: main_models.DescribeDataImportTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDataImportTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fail_page_number):
            query['FailPageNumber'] = request.fail_page_number
        if not DaraCore.is_null(request.fail_page_size):
            query['FailPageSize'] = request.fail_page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not DaraCore.is_null(request.success_page_number):
            query['SuccessPageNumber'] = request.success_page_number
        if not DaraCore.is_null(request.success_page_size):
            query['SuccessPageSize'] = request.success_page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDataImportTaskInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDataImportTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_import_task_info(
        self,
        request: main_models.DescribeDataImportTaskInfoRequest,
    ) -> main_models.DescribeDataImportTaskInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_data_import_task_info_with_options(request, runtime)

    async def describe_data_import_task_info_async(
        self,
        request: main_models.DescribeDataImportTaskInfoRequest,
    ) -> main_models.DescribeDataImportTaskInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_data_import_task_info_with_options_async(request, runtime)

    def describe_db_list_with_options(
        self,
        request: main_models.DescribeDbListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDbListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDbList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDbListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_db_list_with_options_async(
        self,
        request: main_models.DescribeDbListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDbListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDbList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDbListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_db_list(
        self,
        request: main_models.DescribeDbListRequest,
    ) -> main_models.DescribeDbListResponse:
        runtime = RuntimeOptions()
        return self.describe_db_list_with_options(request, runtime)

    async def describe_db_list_async(
        self,
        request: main_models.DescribeDbListRequest,
    ) -> main_models.DescribeDbListResponse:
        runtime = RuntimeOptions()
        return await self.describe_db_list_with_options_async(request, runtime)

    def describe_distribute_table_list_with_options(
        self,
        request: main_models.DescribeDistributeTableListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDistributeTableListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDistributeTableList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDistributeTableListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_distribute_table_list_with_options_async(
        self,
        request: main_models.DescribeDistributeTableListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDistributeTableListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDistributeTableList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDistributeTableListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_distribute_table_list(
        self,
        request: main_models.DescribeDistributeTableListRequest,
    ) -> main_models.DescribeDistributeTableListResponse:
        runtime = RuntimeOptions()
        return self.describe_distribute_table_list_with_options(request, runtime)

    async def describe_distribute_table_list_async(
        self,
        request: main_models.DescribeDistributeTableListRequest,
    ) -> main_models.DescribeDistributeTableListResponse:
        runtime = RuntimeOptions()
        return await self.describe_distribute_table_list_with_options_async(request, runtime)

    def describe_enabled_cross_regions_with_options(
        self,
        request: main_models.DescribeEnabledCrossRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnabledCrossRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnabledCrossRegions',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnabledCrossRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_enabled_cross_regions_with_options_async(
        self,
        request: main_models.DescribeEnabledCrossRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnabledCrossRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnabledCrossRegions',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnabledCrossRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_enabled_cross_regions(
        self,
        request: main_models.DescribeEnabledCrossRegionsRequest,
    ) -> main_models.DescribeEnabledCrossRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_enabled_cross_regions_with_options(request, runtime)

    async def describe_enabled_cross_regions_async(
        self,
        request: main_models.DescribeEnabledCrossRegionsRequest,
    ) -> main_models.DescribeEnabledCrossRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_enabled_cross_regions_with_options_async(request, runtime)

    def describe_evaluate_and_import_task_with_options(
        self,
        request: main_models.DescribeEvaluateAndImportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEvaluateAndImportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEvaluateAndImportTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEvaluateAndImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_evaluate_and_import_task_with_options_async(
        self,
        request: main_models.DescribeEvaluateAndImportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEvaluateAndImportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEvaluateAndImportTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEvaluateAndImportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_evaluate_and_import_task(
        self,
        request: main_models.DescribeEvaluateAndImportTaskRequest,
    ) -> main_models.DescribeEvaluateAndImportTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_evaluate_and_import_task_with_options(request, runtime)

    async def describe_evaluate_and_import_task_async(
        self,
        request: main_models.DescribeEvaluateAndImportTaskRequest,
    ) -> main_models.DescribeEvaluateAndImportTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_evaluate_and_import_task_with_options_async(request, runtime)

    def describe_evaluate_and_import_tasks_with_options(
        self,
        request: main_models.DescribeEvaluateAndImportTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEvaluateAndImportTasksResponse:
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
            action = 'DescribeEvaluateAndImportTasks',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEvaluateAndImportTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_evaluate_and_import_tasks_with_options_async(
        self,
        request: main_models.DescribeEvaluateAndImportTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEvaluateAndImportTasksResponse:
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
            action = 'DescribeEvaluateAndImportTasks',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEvaluateAndImportTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_evaluate_and_import_tasks(
        self,
        request: main_models.DescribeEvaluateAndImportTasksRequest,
    ) -> main_models.DescribeEvaluateAndImportTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_evaluate_and_import_tasks_with_options(request, runtime)

    async def describe_evaluate_and_import_tasks_async(
        self,
        request: main_models.DescribeEvaluateAndImportTasksRequest,
    ) -> main_models.DescribeEvaluateAndImportTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_evaluate_and_import_tasks_with_options_async(request, runtime)

    def describe_events_with_options(
        self,
        request: main_models.DescribeEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEvents',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_events_with_options_async(
        self,
        request: main_models.DescribeEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEvents',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_events(
        self,
        request: main_models.DescribeEventsRequest,
    ) -> main_models.DescribeEventsResponse:
        runtime = RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    async def describe_events_async(
        self,
        request: main_models.DescribeEventsRequest,
    ) -> main_models.DescribeEventsResponse:
        runtime = RuntimeOptions()
        return await self.describe_events_with_options_async(request, runtime)

    def describe_gdn_instances_with_options(
        self,
        request: main_models.DescribeGdnInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGdnInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_type):
            query['FilterType'] = request.filter_type
        if not DaraCore.is_null(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not DaraCore.is_null(request.gdnid):
            query['GDNId'] = request.gdnid
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGdnInstances',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGdnInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_gdn_instances_with_options_async(
        self,
        request: main_models.DescribeGdnInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGdnInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_type):
            query['FilterType'] = request.filter_type
        if not DaraCore.is_null(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not DaraCore.is_null(request.gdnid):
            query['GDNId'] = request.gdnid
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGdnInstances',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGdnInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_gdn_instances(
        self,
        request: main_models.DescribeGdnInstancesRequest,
    ) -> main_models.DescribeGdnInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_gdn_instances_with_options(request, runtime)

    async def describe_gdn_instances_async(
        self,
        request: main_models.DescribeGdnInstancesRequest,
    ) -> main_models.DescribeGdnInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_gdn_instances_with_options_async(request, runtime)

    def describe_open_backup_set_with_options(
        self,
        request: main_models.DescribeOpenBackupSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOpenBackupSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpenBackupSet',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOpenBackupSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_open_backup_set_with_options_async(
        self,
        request: main_models.DescribeOpenBackupSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOpenBackupSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOpenBackupSet',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOpenBackupSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_open_backup_set(
        self,
        request: main_models.DescribeOpenBackupSetRequest,
    ) -> main_models.DescribeOpenBackupSetResponse:
        runtime = RuntimeOptions()
        return self.describe_open_backup_set_with_options(request, runtime)

    async def describe_open_backup_set_async(
        self,
        request: main_models.DescribeOpenBackupSetRequest,
    ) -> main_models.DescribeOpenBackupSetResponse:
        runtime = RuntimeOptions()
        return await self.describe_open_backup_set_with_options_async(request, runtime)

    def describe_parameter_groups_with_options(
        self,
        request: main_models.DescribeParameterGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParameterGroupsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParameterGroups',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParameterGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_parameter_groups_with_options_async(
        self,
        request: main_models.DescribeParameterGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParameterGroupsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParameterGroups',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeParameterGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_parameter_groups(
        self,
        request: main_models.DescribeParameterGroupsRequest,
    ) -> main_models.DescribeParameterGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_parameter_groups_with_options(request, runtime)

    async def describe_parameter_groups_async(
        self,
        request: main_models.DescribeParameterGroupsRequest,
    ) -> main_models.DescribeParameterGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_parameter_groups_with_options_async(request, runtime)

    def describe_parameter_templates_with_options(
        self,
        request: main_models.DescribeParameterTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeParameterTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.param_level):
            query['ParamLevel'] = request.param_level
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParameterTemplates',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.param_level):
            query['ParamLevel'] = request.param_level
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParameterTemplates',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.param_level):
            query['ParamLevel'] = request.param_level
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParameters',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.param_level):
            query['ParamLevel'] = request.param_level
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeParameters',
            version = '2020-02-02',
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

    def describe_polarx_data_nodes_with_options(
        self,
        request: main_models.DescribePolarxDataNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolarxDataNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.node_type):
            query['NodeType'] = request.node_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePolarxDataNodes',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolarxDataNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_polarx_data_nodes_with_options_async(
        self,
        request: main_models.DescribePolarxDataNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolarxDataNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.node_type):
            query['NodeType'] = request.node_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePolarxDataNodes',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolarxDataNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_polarx_data_nodes(
        self,
        request: main_models.DescribePolarxDataNodesRequest,
    ) -> main_models.DescribePolarxDataNodesResponse:
        runtime = RuntimeOptions()
        return self.describe_polarx_data_nodes_with_options(request, runtime)

    async def describe_polarx_data_nodes_async(
        self,
        request: main_models.DescribePolarxDataNodesRequest,
    ) -> main_models.DescribePolarxDataNodesResponse:
        runtime = RuntimeOptions()
        return await self.describe_polarx_data_nodes_with_options_async(request, runtime)

    def describe_rds_vpcs_with_options(
        self,
        request: main_models.DescribeRdsVpcsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdsVpcsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdsVpcs',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRdsVpcs',
            version = '2020-02-02',
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

    def describe_rds_vswitches_with_options(
        self,
        request: main_models.DescribeRdsVswitchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdsVswitchesResponse:
        request.validate()
        query = {}
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
            action = 'DescribeRdsVswitches',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdsVswitchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_vswitches_with_options_async(
        self,
        request: main_models.DescribeRdsVswitchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRdsVswitchesResponse:
        request.validate()
        query = {}
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
            action = 'DescribeRdsVswitches',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRdsVswitchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_vswitches(
        self,
        request: main_models.DescribeRdsVswitchesRequest,
    ) -> main_models.DescribeRdsVswitchesResponse:
        runtime = RuntimeOptions()
        return self.describe_rds_vswitches_with_options(request, runtime)

    async def describe_rds_vswitches_async(
        self,
        request: main_models.DescribeRdsVswitchesRequest,
    ) -> main_models.DescribeRdsVswitchesResponse:
        runtime = RuntimeOptions()
        return await self.describe_rds_vswitches_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-02-02',
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
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2020-02-02',
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

    def describe_regions(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def describe_rpl_inspection_task_with_options(
        self,
        request: main_models.DescribeRplInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRplInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fail_page_number):
            query['FailPageNumber'] = request.fail_page_number
        if not DaraCore.is_null(request.fail_page_size):
            query['FailPageSize'] = request.fail_page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not DaraCore.is_null(request.success_page_number):
            query['SuccessPageNumber'] = request.success_page_number
        if not DaraCore.is_null(request.success_page_size):
            query['SuccessPageSize'] = request.success_page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRplInspectionTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRplInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rpl_inspection_task_with_options_async(
        self,
        request: main_models.DescribeRplInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRplInspectionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.fail_page_number):
            query['FailPageNumber'] = request.fail_page_number
        if not DaraCore.is_null(request.fail_page_size):
            query['FailPageSize'] = request.fail_page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not DaraCore.is_null(request.success_page_number):
            query['SuccessPageNumber'] = request.success_page_number
        if not DaraCore.is_null(request.success_page_size):
            query['SuccessPageSize'] = request.success_page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRplInspectionTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRplInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rpl_inspection_task(
        self,
        request: main_models.DescribeRplInspectionTaskRequest,
    ) -> main_models.DescribeRplInspectionTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_rpl_inspection_task_with_options(request, runtime)

    async def describe_rpl_inspection_task_async(
        self,
        request: main_models.DescribeRplInspectionTaskRequest,
    ) -> main_models.DescribeRplInspectionTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_rpl_inspection_task_with_options_async(request, runtime)

    def describe_scale_out_migrate_task_list_with_options(
        self,
        request: main_models.DescribeScaleOutMigrateTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScaleOutMigrateTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
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
            action = 'DescribeScaleOutMigrateTaskList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScaleOutMigrateTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scale_out_migrate_task_list_with_options_async(
        self,
        request: main_models.DescribeScaleOutMigrateTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeScaleOutMigrateTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
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
            action = 'DescribeScaleOutMigrateTaskList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeScaleOutMigrateTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scale_out_migrate_task_list(
        self,
        request: main_models.DescribeScaleOutMigrateTaskListRequest,
    ) -> main_models.DescribeScaleOutMigrateTaskListResponse:
        runtime = RuntimeOptions()
        return self.describe_scale_out_migrate_task_list_with_options(request, runtime)

    async def describe_scale_out_migrate_task_list_async(
        self,
        request: main_models.DescribeScaleOutMigrateTaskListRequest,
    ) -> main_models.DescribeScaleOutMigrateTaskListResponse:
        runtime = RuntimeOptions()
        return await self.describe_scale_out_migrate_task_list_with_options_async(request, runtime)

    def describe_security_ips_with_options(
        self,
        request: main_models.DescribeSecurityIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityIps',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityIps',
            version = '2020-02-02',
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

    def describe_show_storage_info_with_options(
        self,
        request: main_models.DescribeShowStorageInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeShowStorageInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeShowStorageInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeShowStorageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_show_storage_info_with_options_async(
        self,
        request: main_models.DescribeShowStorageInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeShowStorageInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeShowStorageInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeShowStorageInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_show_storage_info(
        self,
        request: main_models.DescribeShowStorageInfoRequest,
    ) -> main_models.DescribeShowStorageInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_show_storage_info_with_options(request, runtime)

    async def describe_show_storage_info_async(
        self,
        request: main_models.DescribeShowStorageInfoRequest,
    ) -> main_models.DescribeShowStorageInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_show_storage_info_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: main_models.DescribeSlowLogRecordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSlowLogRecordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogRecords',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.character_type):
            query['CharacterType'] = request.character_type
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        if not DaraCore.is_null(request.dbnode_ids):
            query['DBNodeIds'] = request.dbnode_ids
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSlowLogRecords',
            version = '2020-02-02',
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

    def describe_sql_audit_info_with_options(
        self,
        request: main_models.DescribeSqlAuditInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlAuditInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not DaraCore.is_null(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlAuditInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlAuditInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_audit_info_with_options_async(
        self,
        request: main_models.DescribeSqlAuditInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlAuditInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not DaraCore.is_null(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlAuditInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlAuditInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_audit_info(
        self,
        request: main_models.DescribeSqlAuditInfoRequest,
    ) -> main_models.DescribeSqlAuditInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_sql_audit_info_with_options(request, runtime)

    async def describe_sql_audit_info_async(
        self,
        request: main_models.DescribeSqlAuditInfoRequest,
    ) -> main_models.DescribeSqlAuditInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_sql_audit_info_with_options_async(request, runtime)

    def describe_sql_flashback_task_list_with_options(
        self,
        request: main_models.DescribeSqlFlashbackTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlFlashbackTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.polardbx_instance_id):
            query['PolardbxInstanceId'] = request.polardbx_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlFlashbackTaskList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlFlashbackTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_flashback_task_list_with_options_async(
        self,
        request: main_models.DescribeSqlFlashbackTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSqlFlashbackTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.polardbx_instance_id):
            query['PolardbxInstanceId'] = request.polardbx_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSqlFlashbackTaskList',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSqlFlashbackTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_flashback_task_list(
        self,
        request: main_models.DescribeSqlFlashbackTaskListRequest,
    ) -> main_models.DescribeSqlFlashbackTaskListResponse:
        runtime = RuntimeOptions()
        return self.describe_sql_flashback_task_list_with_options(request, runtime)

    async def describe_sql_flashback_task_list_async(
        self,
        request: main_models.DescribeSqlFlashbackTaskListRequest,
    ) -> main_models.DescribeSqlFlashbackTaskListResponse:
        runtime = RuntimeOptions()
        return await self.describe_sql_flashback_task_list_with_options_async(request, runtime)

    def describe_storage_pool_info_with_options(
        self,
        request: main_models.DescribeStoragePoolInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStoragePoolInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStoragePoolInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStoragePoolInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_pool_info_with_options_async(
        self,
        request: main_models.DescribeStoragePoolInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStoragePoolInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStoragePoolInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStoragePoolInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage_pool_info(
        self,
        request: main_models.DescribeStoragePoolInfoRequest,
    ) -> main_models.DescribeStoragePoolInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_storage_pool_info_with_options(request, runtime)

    async def describe_storage_pool_info_async(
        self,
        request: main_models.DescribeStoragePoolInfoRequest,
    ) -> main_models.DescribeStoragePoolInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_storage_pool_info_with_options_async(request, runtime)

    def describe_structure_import_task_info_with_options(
        self,
        request: main_models.DescribeStructureImportTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStructureImportTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStructureImportTaskInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStructureImportTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_structure_import_task_info_with_options_async(
        self,
        request: main_models.DescribeStructureImportTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeStructureImportTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeStructureImportTaskInfo',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeStructureImportTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_structure_import_task_info(
        self,
        request: main_models.DescribeStructureImportTaskInfoRequest,
    ) -> main_models.DescribeStructureImportTaskInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_structure_import_task_info_with_options(request, runtime)

    async def describe_structure_import_task_info_async(
        self,
        request: main_models.DescribeStructureImportTaskInfoRequest,
    ) -> main_models.DescribeStructureImportTaskInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_structure_import_task_info_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: main_models.DescribeTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTags',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTags',
            version = '2020-02-02',
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

    def describe_tasks_with_options(
        self,
        request: main_models.DescribeTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeTasks',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: main_models.DescribeTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
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
            action = 'DescribeTasks',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tasks(
        self,
        request: main_models.DescribeTasksRequest,
    ) -> main_models.DescribeTasksResponse:
        runtime = RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: main_models.DescribeTasksRequest,
    ) -> main_models.DescribeTasksResponse:
        runtime = RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def describe_transform_status_with_options(
        self,
        request: main_models.DescribeTransformStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTransformStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.query_report):
            query['QueryReport'] = request.query_report
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTransformStatus',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTransformStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transform_status_with_options_async(
        self,
        request: main_models.DescribeTransformStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTransformStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.query_report):
            query['QueryReport'] = request.query_report
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTransformStatus',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTransformStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transform_status(
        self,
        request: main_models.DescribeTransformStatusRequest,
    ) -> main_models.DescribeTransformStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_transform_status_with_options(request, runtime)

    async def describe_transform_status_async(
        self,
        request: main_models.DescribeTransformStatusRequest,
    ) -> main_models.DescribeTransformStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_transform_status_with_options_async(request, runtime)

    def describe_user_encryption_key_list_with_options(
        self,
        request: main_models.DescribeUserEncryptionKeyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUserEncryptionKeyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserEncryptionKeyList',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUserEncryptionKeyList',
            version = '2020-02-02',
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

    def disable_rights_separation_with_options(
        self,
        request: main_models.DisableRightsSeparationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableRightsSeparationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dba_account_name):
            query['DbaAccountName'] = request.dba_account_name
        if not DaraCore.is_null(request.dba_account_password):
            query['DbaAccountPassword'] = request.dba_account_password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableRightsSeparation',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableRightsSeparationResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_rights_separation_with_options_async(
        self,
        request: main_models.DisableRightsSeparationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableRightsSeparationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dba_account_name):
            query['DbaAccountName'] = request.dba_account_name
        if not DaraCore.is_null(request.dba_account_password):
            query['DbaAccountPassword'] = request.dba_account_password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableRightsSeparation',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableRightsSeparationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_rights_separation(
        self,
        request: main_models.DisableRightsSeparationRequest,
    ) -> main_models.DisableRightsSeparationResponse:
        runtime = RuntimeOptions()
        return self.disable_rights_separation_with_options(request, runtime)

    async def disable_rights_separation_async(
        self,
        request: main_models.DisableRightsSeparationRequest,
    ) -> main_models.DisableRightsSeparationResponse:
        runtime = RuntimeOptions()
        return await self.disable_rights_separation_with_options_async(request, runtime)

    def disable_sql_audit_with_options(
        self,
        request: main_models.DisableSqlAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSqlAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not DaraCore.is_null(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSqlAudit',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSqlAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_sql_audit_with_options_async(
        self,
        request: main_models.DisableSqlAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSqlAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not DaraCore.is_null(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSqlAudit',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSqlAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_sql_audit(
        self,
        request: main_models.DisableSqlAuditRequest,
    ) -> main_models.DisableSqlAuditResponse:
        runtime = RuntimeOptions()
        return self.disable_sql_audit_with_options(request, runtime)

    async def disable_sql_audit_async(
        self,
        request: main_models.DisableSqlAuditRequest,
    ) -> main_models.DisableSqlAuditResponse:
        runtime = RuntimeOptions()
        return await self.disable_sql_audit_with_options_async(request, runtime)

    def enable_rights_separation_with_options(
        self,
        request: main_models.EnableRightsSeparationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableRightsSeparationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_account_description):
            query['AuditAccountDescription'] = request.audit_account_description
        if not DaraCore.is_null(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not DaraCore.is_null(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_description):
            query['SecurityAccountDescription'] = request.security_account_description
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableRightsSeparation',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableRightsSeparationResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_rights_separation_with_options_async(
        self,
        request: main_models.EnableRightsSeparationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableRightsSeparationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_account_description):
            query['AuditAccountDescription'] = request.audit_account_description
        if not DaraCore.is_null(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not DaraCore.is_null(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_description):
            query['SecurityAccountDescription'] = request.security_account_description
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableRightsSeparation',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableRightsSeparationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_rights_separation(
        self,
        request: main_models.EnableRightsSeparationRequest,
    ) -> main_models.EnableRightsSeparationResponse:
        runtime = RuntimeOptions()
        return self.enable_rights_separation_with_options(request, runtime)

    async def enable_rights_separation_async(
        self,
        request: main_models.EnableRightsSeparationRequest,
    ) -> main_models.EnableRightsSeparationResponse:
        runtime = RuntimeOptions()
        return await self.enable_rights_separation_with_options_async(request, runtime)

    def enable_sql_audit_with_options(
        self,
        request: main_models.EnableSqlAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSqlAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not DaraCore.is_null(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.expire_after_days):
            query['ExpireAfterDays'] = request.expire_after_days
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSqlAudit',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSqlAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_sql_audit_with_options_async(
        self,
        request: main_models.EnableSqlAuditRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSqlAuditResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.audit_account_name):
            query['AuditAccountName'] = request.audit_account_name
        if not DaraCore.is_null(request.audit_account_password):
            query['AuditAccountPassword'] = request.audit_account_password
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.expire_after_days):
            query['ExpireAfterDays'] = request.expire_after_days
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSqlAudit',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSqlAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_sql_audit(
        self,
        request: main_models.EnableSqlAuditRequest,
    ) -> main_models.EnableSqlAuditResponse:
        runtime = RuntimeOptions()
        return self.enable_sql_audit_with_options(request, runtime)

    async def enable_sql_audit_async(
        self,
        request: main_models.EnableSqlAuditRequest,
    ) -> main_models.EnableSqlAuditResponse:
        runtime = RuntimeOptions()
        return await self.enable_sql_audit_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
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
            action = 'ListTagResources',
            version = '2020-02-02',
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
            action = 'ListTagResources',
            version = '2020-02-02',
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

    def migrate_dbinstance_with_options(
        self,
        request: main_models.MigrateDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MigrateDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not DaraCore.is_null(request.tertiary_zone_id):
            query['TertiaryZoneId'] = request.tertiary_zone_id
        if not DaraCore.is_null(request.topology_type):
            query['TopologyType'] = request.topology_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateDBInstance',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def migrate_dbinstance_with_options_async(
        self,
        request: main_models.MigrateDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MigrateDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.secondary_zone_id):
            query['SecondaryZoneId'] = request.secondary_zone_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not DaraCore.is_null(request.tertiary_zone_id):
            query['TertiaryZoneId'] = request.tertiary_zone_id
        if not DaraCore.is_null(request.topology_type):
            query['TopologyType'] = request.topology_type
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MigrateDBInstance',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MigrateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def migrate_dbinstance(
        self,
        request: main_models.MigrateDBInstanceRequest,
    ) -> main_models.MigrateDBInstanceResponse:
        runtime = RuntimeOptions()
        return self.migrate_dbinstance_with_options(request, runtime)

    async def migrate_dbinstance_async(
        self,
        request: main_models.MigrateDBInstanceRequest,
    ) -> main_models.MigrateDBInstanceResponse:
        runtime = RuntimeOptions()
        return await self.migrate_dbinstance_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountDescription',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountDescription',
            version = '2020-02-02',
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

    def modify_account_privilege_with_options(
        self,
        request: main_models.ModifyAccountPrivilegeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountPrivilegeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountPrivilege',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountPrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_privilege_with_options_async(
        self,
        request: main_models.ModifyAccountPrivilegeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountPrivilegeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_privilege):
            query['AccountPrivilege'] = request.account_privilege
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountPrivilege',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountPrivilegeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_privilege(
        self,
        request: main_models.ModifyAccountPrivilegeRequest,
    ) -> main_models.ModifyAccountPrivilegeResponse:
        runtime = RuntimeOptions()
        return self.modify_account_privilege_with_options(request, runtime)

    async def modify_account_privilege_async(
        self,
        request: main_models.ModifyAccountPrivilegeRequest,
    ) -> main_models.ModifyAccountPrivilegeResponse:
        runtime = RuntimeOptions()
        return await self.modify_account_privilege_with_options_async(request, runtime)

    def modify_active_operation_maintain_conf_with_options(
        self,
        request: main_models.ModifyActiveOperationMaintainConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyActiveOperationMaintainConfResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationMaintainConf',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationMaintainConf',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationTasks',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyActiveOperationTasks',
            version = '2020-02-02',
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

    def modify_cdc_class_with_options(
        self,
        request: main_models.ModifyCdcClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCdcClassResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cdcnode_count):
            query['CDCNodeCount'] = request.cdcnode_count
        if not DaraCore.is_null(request.cdc_class):
            query['CdcClass'] = request.cdc_class
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCdcClass',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCdcClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cdc_class_with_options_async(
        self,
        request: main_models.ModifyCdcClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCdcClassResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cdcnode_count):
            query['CDCNodeCount'] = request.cdcnode_count
        if not DaraCore.is_null(request.cdc_class):
            query['CdcClass'] = request.cdc_class
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCdcClass',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCdcClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cdc_class(
        self,
        request: main_models.ModifyCdcClassRequest,
    ) -> main_models.ModifyCdcClassResponse:
        runtime = RuntimeOptions()
        return self.modify_cdc_class_with_options(request, runtime)

    async def modify_cdc_class_async(
        self,
        request: main_models.ModifyCdcClassRequest,
    ) -> main_models.ModifyCdcClassResponse:
        runtime = RuntimeOptions()
        return await self.modify_cdc_class_with_options_async(request, runtime)

    def modify_columnar_class_with_options(
        self,
        request: main_models.ModifyColumnarClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyColumnarClassResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.columnar_class):
            query['ColumnarClass'] = request.columnar_class
        if not DaraCore.is_null(request.columnar_node_count):
            query['ColumnarNodeCount'] = request.columnar_node_count
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyColumnarClass',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyColumnarClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_columnar_class_with_options_async(
        self,
        request: main_models.ModifyColumnarClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyColumnarClassResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.columnar_class):
            query['ColumnarClass'] = request.columnar_class
        if not DaraCore.is_null(request.columnar_node_count):
            query['ColumnarNodeCount'] = request.columnar_node_count
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyColumnarClass',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyColumnarClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_columnar_class(
        self,
        request: main_models.ModifyColumnarClassRequest,
    ) -> main_models.ModifyColumnarClassResponse:
        runtime = RuntimeOptions()
        return self.modify_columnar_class_with_options(request, runtime)

    async def modify_columnar_class_async(
        self,
        request: main_models.ModifyColumnarClassRequest,
    ) -> main_models.ModifyColumnarClassResponse:
        runtime = RuntimeOptions()
        return await self.modify_columnar_class_with_options_async(request, runtime)

    def modify_custom_endpoint_with_options(
        self,
        request: main_models.ModifyCustomEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_endpoint_id):
            query['CustomEndpointId'] = request.custom_endpoint_id
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.node_auto_enter):
            query['NodeAutoEnter'] = request.node_auto_enter
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.node_role):
            query['NodeRole'] = request.node_role
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomEndpoint',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_custom_endpoint_with_options_async(
        self,
        request: main_models.ModifyCustomEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_endpoint_id):
            query['CustomEndpointId'] = request.custom_endpoint_id
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.node_auto_enter):
            query['NodeAutoEnter'] = request.node_auto_enter
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.node_role):
            query['NodeRole'] = request.node_role
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomEndpoint',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_custom_endpoint(
        self,
        request: main_models.ModifyCustomEndpointRequest,
    ) -> main_models.ModifyCustomEndpointResponse:
        runtime = RuntimeOptions()
        return self.modify_custom_endpoint_with_options(request, runtime)

    async def modify_custom_endpoint_async(
        self,
        request: main_models.ModifyCustomEndpointRequest,
    ) -> main_models.ModifyCustomEndpointResponse:
        runtime = RuntimeOptions()
        return await self.modify_custom_endpoint_with_options_async(request, runtime)

    def modify_custom_endpoint_net_with_options(
        self,
        request: main_models.ModifyCustomEndpointNetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomEndpointNetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conn_prefix):
            query['ConnPrefix'] = request.conn_prefix
        if not DaraCore.is_null(request.custom_endpoint_id):
            query['CustomEndpointId'] = request.custom_endpoint_id
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomEndpointNet',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomEndpointNetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_custom_endpoint_net_with_options_async(
        self,
        request: main_models.ModifyCustomEndpointNetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCustomEndpointNetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.conn_prefix):
            query['ConnPrefix'] = request.conn_prefix
        if not DaraCore.is_null(request.custom_endpoint_id):
            query['CustomEndpointId'] = request.custom_endpoint_id
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.port):
            query['Port'] = request.port
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCustomEndpointNet',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCustomEndpointNetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_custom_endpoint_net(
        self,
        request: main_models.ModifyCustomEndpointNetRequest,
    ) -> main_models.ModifyCustomEndpointNetResponse:
        runtime = RuntimeOptions()
        return self.modify_custom_endpoint_net_with_options(request, runtime)

    async def modify_custom_endpoint_net_async(
        self,
        request: main_models.ModifyCustomEndpointNetRequest,
    ) -> main_models.ModifyCustomEndpointNetResponse:
        runtime = RuntimeOptions()
        return await self.modify_custom_endpoint_net_with_options_async(request, runtime)

    def modify_dbinstance_class_with_options(
        self,
        request: main_models.ModifyDBInstanceClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceClassResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cn_class):
            query['CnClass'] = request.cn_class
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dn_class):
            query['DnClass'] = request.dn_class
        if not DaraCore.is_null(request.dn_storage_space):
            query['DnStorageSpace'] = request.dn_storage_space
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.specified_dnscale):
            query['SpecifiedDNScale'] = request.specified_dnscale
        if not DaraCore.is_null(request.specified_dnspec_map_json):
            query['SpecifiedDNSpecMapJson'] = request.specified_dnspec_map_json
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not DaraCore.is_null(request.target_dbinstance_class):
            query['TargetDBInstanceClass'] = request.target_dbinstance_class
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceClass',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_class_with_options_async(
        self,
        request: main_models.ModifyDBInstanceClassRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceClassResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cn_class):
            query['CnClass'] = request.cn_class
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dn_class):
            query['DnClass'] = request.dn_class
        if not DaraCore.is_null(request.dn_storage_space):
            query['DnStorageSpace'] = request.dn_storage_space
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.specified_dnscale):
            query['SpecifiedDNScale'] = request.specified_dnscale
        if not DaraCore.is_null(request.specified_dnspec_map_json):
            query['SpecifiedDNSpecMapJson'] = request.specified_dnspec_map_json
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not DaraCore.is_null(request.target_dbinstance_class):
            query['TargetDBInstanceClass'] = request.target_dbinstance_class
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceClass',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_class(
        self,
        request: main_models.ModifyDBInstanceClassRequest,
    ) -> main_models.ModifyDBInstanceClassResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_class_with_options(request, runtime)

    async def modify_dbinstance_class_async(
        self,
        request: main_models.ModifyDBInstanceClassRequest,
    ) -> main_models.ModifyDBInstanceClassResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_class_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceConfig',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceConfig',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.new_port):
            query['NewPort'] = request.new_port
        if not DaraCore.is_null(request.new_prefix):
            query['NewPrefix'] = request.new_prefix
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceConnectionString',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.new_port):
            query['NewPort'] = request.new_port
        if not DaraCore.is_null(request.new_prefix):
            query['NewPrefix'] = request.new_prefix
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceConnectionString',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceDescription',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceDescription',
            version = '2020-02-02',
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

    def modify_dbinstance_maintain_time_with_options(
        self,
        request: main_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceMaintainTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceMaintainTime',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceMaintainTime',
            version = '2020-02-02',
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

    def modify_dbinstance_vip_with_options(
        self,
        request: main_models.ModifyDBInstanceVipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceVipResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceVip',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceVipResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_vip_with_options_async(
        self,
        request: main_models.ModifyDBInstanceVipRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBInstanceVipResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBInstanceVip',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBInstanceVipResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_vip(
        self,
        request: main_models.ModifyDBInstanceVipRequest,
    ) -> main_models.ModifyDBInstanceVipResponse:
        runtime = RuntimeOptions()
        return self.modify_dbinstance_vip_with_options(request, runtime)

    async def modify_dbinstance_vip_async(
        self,
        request: main_models.ModifyDBInstanceVipRequest,
    ) -> main_models.ModifyDBInstanceVipResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbinstance_vip_with_options_async(request, runtime)

    def modify_database_description_with_options(
        self,
        request: main_models.ModifyDatabaseDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatabaseDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.db_description):
            query['DbDescription'] = request.db_description
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDatabaseDescription',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatabaseDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_database_description_with_options_async(
        self,
        request: main_models.ModifyDatabaseDescriptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDatabaseDescriptionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.db_description):
            query['DbDescription'] = request.db_description
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDatabaseDescription',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDatabaseDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_database_description(
        self,
        request: main_models.ModifyDatabaseDescriptionRequest,
    ) -> main_models.ModifyDatabaseDescriptionResponse:
        runtime = RuntimeOptions()
        return self.modify_database_description_with_options(request, runtime)

    async def modify_database_description_async(
        self,
        request: main_models.ModifyDatabaseDescriptionRequest,
    ) -> main_models.ModifyDatabaseDescriptionResponse:
        runtime = RuntimeOptions()
        return await self.modify_database_description_with_options_async(request, runtime)

    def modify_engine_migration_with_options(
        self,
        request: main_models.ModifyEngineMigrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEngineMigrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_strings):
            query['ConnectionStrings'] = request.connection_strings
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.new_master_dbinstance_name):
            query['NewMasterDBInstanceName'] = request.new_master_dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_dbinstance_name):
            query['SourceDBInstanceName'] = request.source_dbinstance_name
        if not DaraCore.is_null(request.swap_connection_string):
            query['SwapConnectionString'] = request.swap_connection_string
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEngineMigration',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEngineMigrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_engine_migration_with_options_async(
        self,
        request: main_models.ModifyEngineMigrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyEngineMigrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.connection_strings):
            query['ConnectionStrings'] = request.connection_strings
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.new_master_dbinstance_name):
            query['NewMasterDBInstanceName'] = request.new_master_dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_dbinstance_name):
            query['SourceDBInstanceName'] = request.source_dbinstance_name
        if not DaraCore.is_null(request.swap_connection_string):
            query['SwapConnectionString'] = request.swap_connection_string
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyEngineMigration',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyEngineMigrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_engine_migration(
        self,
        request: main_models.ModifyEngineMigrationRequest,
    ) -> main_models.ModifyEngineMigrationResponse:
        runtime = RuntimeOptions()
        return self.modify_engine_migration_with_options(request, runtime)

    async def modify_engine_migration_async(
        self,
        request: main_models.ModifyEngineMigrationRequest,
    ) -> main_models.ModifyEngineMigrationResponse:
        runtime = RuntimeOptions()
        return await self.modify_engine_migration_with_options_async(request, runtime)

    def modify_parameter_with_options(
        self,
        request: main_models.ModifyParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.param_level):
            query['ParamLevel'] = request.param_level
        if not DaraCore.is_null(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyParameter',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_parameter_with_options_async(
        self,
        request: main_models.ModifyParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not DaraCore.is_null(request.param_level):
            query['ParamLevel'] = request.param_level
        if not DaraCore.is_null(request.parameter_group_id):
            query['ParameterGroupId'] = request.parameter_group_id
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyParameter',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_parameter(
        self,
        request: main_models.ModifyParameterRequest,
    ) -> main_models.ModifyParameterResponse:
        runtime = RuntimeOptions()
        return self.modify_parameter_with_options(request, runtime)

    async def modify_parameter_async(
        self,
        request: main_models.ModifyParameterRequest,
    ) -> main_models.ModifyParameterResponse:
        runtime = RuntimeOptions()
        return await self.modify_parameter_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: main_models.ModifySecurityIpsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityIpsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityIps',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityIps',
            version = '2020-02-02',
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

    def pre_check_sql_flashback_task_with_options(
        self,
        request: main_models.PreCheckSqlFlashbackTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreCheckSqlFlashbackTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.polardbx_instance_id):
            query['PolardbxInstanceId'] = request.polardbx_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreCheckSqlFlashbackTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreCheckSqlFlashbackTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def pre_check_sql_flashback_task_with_options_async(
        self,
        request: main_models.PreCheckSqlFlashbackTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreCheckSqlFlashbackTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.polardbx_instance_id):
            query['PolardbxInstanceId'] = request.polardbx_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreCheckSqlFlashbackTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreCheckSqlFlashbackTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pre_check_sql_flashback_task(
        self,
        request: main_models.PreCheckSqlFlashbackTaskRequest,
    ) -> main_models.PreCheckSqlFlashbackTaskResponse:
        runtime = RuntimeOptions()
        return self.pre_check_sql_flashback_task_with_options(request, runtime)

    async def pre_check_sql_flashback_task_async(
        self,
        request: main_models.PreCheckSqlFlashbackTaskRequest,
    ) -> main_models.PreCheckSqlFlashbackTaskResponse:
        runtime = RuntimeOptions()
        return await self.pre_check_sql_flashback_task_with_options_async(request, runtime)

    def refresh_import_meta_with_options(
        self,
        request: main_models.RefreshImportMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshImportMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshImportMeta',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshImportMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_import_meta_with_options_async(
        self,
        request: main_models.RefreshImportMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshImportMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshImportMeta',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshImportMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_import_meta(
        self,
        request: main_models.RefreshImportMetaRequest,
    ) -> main_models.RefreshImportMetaResponse:
        runtime = RuntimeOptions()
        return self.refresh_import_meta_with_options(request, runtime)

    async def refresh_import_meta_async(
        self,
        request: main_models.RefreshImportMetaRequest,
    ) -> main_models.RefreshImportMetaResponse:
        runtime = RuntimeOptions()
        return await self.refresh_import_meta_with_options_async(request, runtime)

    def release_cold_data_volume_with_options(
        self,
        request: main_models.ReleaseColdDataVolumeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseColdDataVolumeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseColdDataVolume',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseColdDataVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cold_data_volume_with_options_async(
        self,
        request: main_models.ReleaseColdDataVolumeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseColdDataVolumeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseColdDataVolume',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseColdDataVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_cold_data_volume(
        self,
        request: main_models.ReleaseColdDataVolumeRequest,
    ) -> main_models.ReleaseColdDataVolumeResponse:
        runtime = RuntimeOptions()
        return self.release_cold_data_volume_with_options(request, runtime)

    async def release_cold_data_volume_async(
        self,
        request: main_models.ReleaseColdDataVolumeRequest,
    ) -> main_models.ReleaseColdDataVolumeResponse:
        runtime = RuntimeOptions()
        return await self.release_cold_data_volume_with_options_async(request, runtime)

    def release_instance_public_connection_with_options(
        self,
        request: main_models.ReleaseInstancePublicConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseInstancePublicConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstancePublicConnection',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseInstancePublicConnection',
            version = '2020-02-02',
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
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPassword',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPassword',
            version = '2020-02-02',
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

    def reset_account_password_restrict_with_options(
        self,
        request: main_models.ResetAccountPasswordRestrictRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAccountPasswordRestrictResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPasswordRestrict',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAccountPasswordRestrictResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_restrict_with_options_async(
        self,
        request: main_models.ResetAccountPasswordRestrictRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetAccountPasswordRestrictResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_account_name):
            query['SecurityAccountName'] = request.security_account_name
        if not DaraCore.is_null(request.security_account_password):
            query['SecurityAccountPassword'] = request.security_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetAccountPasswordRestrict',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetAccountPasswordRestrictResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password_restrict(
        self,
        request: main_models.ResetAccountPasswordRestrictRequest,
    ) -> main_models.ResetAccountPasswordRestrictResponse:
        runtime = RuntimeOptions()
        return self.reset_account_password_restrict_with_options(request, runtime)

    async def reset_account_password_restrict_async(
        self,
        request: main_models.ResetAccountPasswordRestrictRequest,
    ) -> main_models.ResetAccountPasswordRestrictResponse:
        runtime = RuntimeOptions()
        return await self.reset_account_password_restrict_with_options_async(request, runtime)

    def restart_dbinstance_with_options(
        self,
        request: main_models.RestartDBInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartDBInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartDBInstance',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartDBInstance',
            version = '2020-02-02',
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

    def restart_data_import_task_with_options(
        self,
        request: main_models.RestartDataImportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartDataImportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartDataImportTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartDataImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_data_import_task_with_options_async(
        self,
        request: main_models.RestartDataImportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartDataImportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartDataImportTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartDataImportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_data_import_task(
        self,
        request: main_models.RestartDataImportTaskRequest,
    ) -> main_models.RestartDataImportTaskResponse:
        runtime = RuntimeOptions()
        return self.restart_data_import_task_with_options(request, runtime)

    async def restart_data_import_task_async(
        self,
        request: main_models.RestartDataImportTaskRequest,
    ) -> main_models.RestartDataImportTaskResponse:
        runtime = RuntimeOptions()
        return await self.restart_data_import_task_with_options_async(request, runtime)

    def skip_current_step_with_options(
        self,
        request: main_models.SkipCurrentStepRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SkipCurrentStepResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_step):
            query['CurrentStep'] = request.current_step
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SkipCurrentStep',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SkipCurrentStepResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_current_step_with_options_async(
        self,
        request: main_models.SkipCurrentStepRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SkipCurrentStepResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_step):
            query['CurrentStep'] = request.current_step
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SkipCurrentStep',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SkipCurrentStepResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_current_step(
        self,
        request: main_models.SkipCurrentStepRequest,
    ) -> main_models.SkipCurrentStepResponse:
        runtime = RuntimeOptions()
        return self.skip_current_step_with_options(request, runtime)

    async def skip_current_step_async(
        self,
        request: main_models.SkipCurrentStepRequest,
    ) -> main_models.SkipCurrentStepResponse:
        runtime = RuntimeOptions()
        return await self.skip_current_step_with_options_async(request, runtime)

    def start_switch_database_with_options(
        self,
        request: main_models.StartSwitchDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSwitchDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dst_main_connect_string):
            query['DstMainConnectString'] = request.dst_main_connect_string
        if not DaraCore.is_null(request.dst_main_port):
            query['DstMainPort'] = request.dst_main_port
        if not DaraCore.is_null(request.is_modify_endpoint):
            query['IsModifyEndpoint'] = request.is_modify_endpoint
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not DaraCore.is_null(request.src_main_connect_string):
            query['SrcMainConnectString'] = request.src_main_connect_string
        if not DaraCore.is_null(request.src_main_port):
            query['SrcMainPort'] = request.src_main_port
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartSwitchDatabase',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSwitchDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_switch_database_with_options_async(
        self,
        request: main_models.StartSwitchDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartSwitchDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dst_main_connect_string):
            query['DstMainConnectString'] = request.dst_main_connect_string
        if not DaraCore.is_null(request.dst_main_port):
            query['DstMainPort'] = request.dst_main_port
        if not DaraCore.is_null(request.is_modify_endpoint):
            query['IsModifyEndpoint'] = request.is_modify_endpoint
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        if not DaraCore.is_null(request.src_main_connect_string):
            query['SrcMainConnectString'] = request.src_main_connect_string
        if not DaraCore.is_null(request.src_main_port):
            query['SrcMainPort'] = request.src_main_port
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartSwitchDatabase',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartSwitchDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_switch_database(
        self,
        request: main_models.StartSwitchDatabaseRequest,
    ) -> main_models.StartSwitchDatabaseResponse:
        runtime = RuntimeOptions()
        return self.start_switch_database_with_options(request, runtime)

    async def start_switch_database_async(
        self,
        request: main_models.StartSwitchDatabaseRequest,
    ) -> main_models.StartSwitchDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.start_switch_database_with_options_async(request, runtime)

    def stop_data_import_task_with_options(
        self,
        request: main_models.StopDataImportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDataImportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDataImportTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDataImportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_data_import_task_with_options_async(
        self,
        request: main_models.StopDataImportTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopDataImportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.slink_task_id):
            query['SlinkTaskId'] = request.slink_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopDataImportTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopDataImportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_data_import_task(
        self,
        request: main_models.StopDataImportTaskRequest,
    ) -> main_models.StopDataImportTaskResponse:
        runtime = RuntimeOptions()
        return self.stop_data_import_task_with_options(request, runtime)

    async def stop_data_import_task_async(
        self,
        request: main_models.StopDataImportTaskRequest,
    ) -> main_models.StopDataImportTaskResponse:
        runtime = RuntimeOptions()
        return await self.stop_data_import_task_with_options_async(request, runtime)

    def submit_sql_flashback_task_with_options(
        self,
        request: main_models.SubmitSqlFlashbackTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSqlFlashbackTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.polardbx_instance_id):
            query['PolardbxInstanceId'] = request.polardbx_instance_id
        if not DaraCore.is_null(request.recall_restore_type):
            query['RecallRestoreType'] = request.recall_restore_type
        if not DaraCore.is_null(request.recall_type):
            query['RecallType'] = request.recall_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sql_pk):
            query['SqlPk'] = request.sql_pk
        if not DaraCore.is_null(request.sql_type):
            query['SqlType'] = request.sql_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSqlFlashbackTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSqlFlashbackTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_sql_flashback_task_with_options_async(
        self,
        request: main_models.SubmitSqlFlashbackTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSqlFlashbackTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.polardbx_instance_id):
            query['PolardbxInstanceId'] = request.polardbx_instance_id
        if not DaraCore.is_null(request.recall_restore_type):
            query['RecallRestoreType'] = request.recall_restore_type
        if not DaraCore.is_null(request.recall_type):
            query['RecallType'] = request.recall_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sql_pk):
            query['SqlPk'] = request.sql_pk
        if not DaraCore.is_null(request.sql_type):
            query['SqlType'] = request.sql_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSqlFlashbackTask',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSqlFlashbackTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_sql_flashback_task(
        self,
        request: main_models.SubmitSqlFlashbackTaskRequest,
    ) -> main_models.SubmitSqlFlashbackTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_sql_flashback_task_with_options(request, runtime)

    async def submit_sql_flashback_task_async(
        self,
        request: main_models.SubmitSqlFlashbackTaskRequest,
    ) -> main_models.SubmitSqlFlashbackTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_sql_flashback_task_with_options_async(request, runtime)

    def switch_dbinstance_hawith_options(
        self,
        request: main_models.SwitchDBInstanceHARequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchDBInstanceHAResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not DaraCore.is_null(request.target_primary_azone_id):
            query['TargetPrimaryAzoneId'] = request.target_primary_azone_id
        if not DaraCore.is_null(request.target_primary_region_id):
            query['TargetPrimaryRegionId'] = request.target_primary_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchDBInstanceHA',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not DaraCore.is_null(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not DaraCore.is_null(request.target_primary_azone_id):
            query['TargetPrimaryAzoneId'] = request.target_primary_azone_id
        if not DaraCore.is_null(request.target_primary_region_id):
            query['TargetPrimaryRegionId'] = request.target_primary_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchDBInstanceHA',
            version = '2020-02-02',
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

    def switch_gdn_member_role_with_options(
        self,
        request: main_models.SwitchGdnMemberRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchGdnMemberRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not DaraCore.is_null(request.task_timeout):
            query['TaskTimeout'] = request.task_timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchGdnMemberRole',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchGdnMemberRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_gdn_member_role_with_options_async(
        self,
        request: main_models.SwitchGdnMemberRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchGdnMemberRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        if not DaraCore.is_null(request.task_timeout):
            query['TaskTimeout'] = request.task_timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchGdnMemberRole',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchGdnMemberRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_gdn_member_role(
        self,
        request: main_models.SwitchGdnMemberRoleRequest,
    ) -> main_models.SwitchGdnMemberRoleResponse:
        runtime = RuntimeOptions()
        return self.switch_gdn_member_role_with_options(request, runtime)

    async def switch_gdn_member_role_async(
        self,
        request: main_models.SwitchGdnMemberRoleRequest,
    ) -> main_models.SwitchGdnMemberRoleResponse:
        runtime = RuntimeOptions()
        return await self.switch_gdn_member_role_with_options_async(request, runtime)

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
            version = '2020-02-02',
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
            version = '2020-02-02',
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
            version = '2020-02-02',
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
            version = '2020-02-02',
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

    def update_backup_policy_with_options(
        self,
        request: main_models.UpdateBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not DaraCore.is_null(request.backup_plan_begin):
            query['BackupPlanBegin'] = request.backup_plan_begin
        if not DaraCore.is_null(request.backup_set_retention):
            query['BackupSetRetention'] = request.backup_set_retention
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.backup_way):
            query['BackupWay'] = request.backup_way
        if not DaraCore.is_null(request.cold_data_backup_interval):
            query['ColdDataBackupInterval'] = request.cold_data_backup_interval
        if not DaraCore.is_null(request.cold_data_backup_retention):
            query['ColdDataBackupRetention'] = request.cold_data_backup_retention
        if not DaraCore.is_null(request.cross_region_data_backup_retention):
            query['CrossRegionDataBackupRetention'] = request.cross_region_data_backup_retention
        if not DaraCore.is_null(request.cross_region_log_backup_retention):
            query['CrossRegionLogBackupRetention'] = request.cross_region_log_backup_retention
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dest_cross_region):
            query['DestCrossRegion'] = request.dest_cross_region
        if not DaraCore.is_null(request.force_clean_on_high_space_usage):
            query['ForceCleanOnHighSpaceUsage'] = request.force_clean_on_high_space_usage
        if not DaraCore.is_null(request.is_cross_region_data_backup_enabled):
            query['IsCrossRegionDataBackupEnabled'] = request.is_cross_region_data_backup_enabled
        if not DaraCore.is_null(request.is_cross_region_log_backup_enabled):
            query['IsCrossRegionLogBackupEnabled'] = request.is_cross_region_log_backup_enabled
        if not DaraCore.is_null(request.is_enabled):
            query['IsEnabled'] = request.is_enabled
        if not DaraCore.is_null(request.local_log_retention):
            query['LocalLogRetention'] = request.local_log_retention
        if not DaraCore.is_null(request.local_log_retention_number):
            query['LocalLogRetentionNumber'] = request.local_log_retention_number
        if not DaraCore.is_null(request.log_local_retention_space):
            query['LogLocalRetentionSpace'] = request.log_local_retention_space
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remove_log_retention):
            query['RemoveLogRetention'] = request.remove_log_retention
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBackupPolicy',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_backup_policy_with_options_async(
        self,
        request: main_models.UpdateBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not DaraCore.is_null(request.backup_plan_begin):
            query['BackupPlanBegin'] = request.backup_plan_begin
        if not DaraCore.is_null(request.backup_set_retention):
            query['BackupSetRetention'] = request.backup_set_retention
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.backup_way):
            query['BackupWay'] = request.backup_way
        if not DaraCore.is_null(request.cold_data_backup_interval):
            query['ColdDataBackupInterval'] = request.cold_data_backup_interval
        if not DaraCore.is_null(request.cold_data_backup_retention):
            query['ColdDataBackupRetention'] = request.cold_data_backup_retention
        if not DaraCore.is_null(request.cross_region_data_backup_retention):
            query['CrossRegionDataBackupRetention'] = request.cross_region_data_backup_retention
        if not DaraCore.is_null(request.cross_region_log_backup_retention):
            query['CrossRegionLogBackupRetention'] = request.cross_region_log_backup_retention
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dest_cross_region):
            query['DestCrossRegion'] = request.dest_cross_region
        if not DaraCore.is_null(request.force_clean_on_high_space_usage):
            query['ForceCleanOnHighSpaceUsage'] = request.force_clean_on_high_space_usage
        if not DaraCore.is_null(request.is_cross_region_data_backup_enabled):
            query['IsCrossRegionDataBackupEnabled'] = request.is_cross_region_data_backup_enabled
        if not DaraCore.is_null(request.is_cross_region_log_backup_enabled):
            query['IsCrossRegionLogBackupEnabled'] = request.is_cross_region_log_backup_enabled
        if not DaraCore.is_null(request.is_enabled):
            query['IsEnabled'] = request.is_enabled
        if not DaraCore.is_null(request.local_log_retention):
            query['LocalLogRetention'] = request.local_log_retention
        if not DaraCore.is_null(request.local_log_retention_number):
            query['LocalLogRetentionNumber'] = request.local_log_retention_number
        if not DaraCore.is_null(request.log_local_retention_space):
            query['LogLocalRetentionSpace'] = request.log_local_retention_space
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.remove_log_retention):
            query['RemoveLogRetention'] = request.remove_log_retention
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBackupPolicy',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_backup_policy(
        self,
        request: main_models.UpdateBackupPolicyRequest,
    ) -> main_models.UpdateBackupPolicyResponse:
        runtime = RuntimeOptions()
        return self.update_backup_policy_with_options(request, runtime)

    async def update_backup_policy_async(
        self,
        request: main_models.UpdateBackupPolicyRequest,
    ) -> main_models.UpdateBackupPolicyResponse:
        runtime = RuntimeOptions()
        return await self.update_backup_policy_with_options_async(request, runtime)

    def update_dbinstance_sslwith_options(
        self,
        request: main_models.UpdateDBInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDBInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_common_name):
            query['CertCommonName'] = request.cert_common_name
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDBInstanceSSL',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDBInstanceSSLResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dbinstance_sslwith_options_async(
        self,
        request: main_models.UpdateDBInstanceSSLRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDBInstanceSSLResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cert_common_name):
            query['CertCommonName'] = request.cert_common_name
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.enable_ssl):
            query['EnableSSL'] = request.enable_ssl
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDBInstanceSSL',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDBInstanceSSLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dbinstance_ssl(
        self,
        request: main_models.UpdateDBInstanceSSLRequest,
    ) -> main_models.UpdateDBInstanceSSLResponse:
        runtime = RuntimeOptions()
        return self.update_dbinstance_sslwith_options(request, runtime)

    async def update_dbinstance_ssl_async(
        self,
        request: main_models.UpdateDBInstanceSSLRequest,
    ) -> main_models.UpdateDBInstanceSSLResponse:
        runtime = RuntimeOptions()
        return await self.update_dbinstance_sslwith_options_async(request, runtime)

    def update_dbinstance_tdewith_options(
        self,
        request: main_models.UpdateDBInstanceTDERequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDBInstanceTDEResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDBInstanceTDE',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDBInstanceTDEResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dbinstance_tdewith_options_async(
        self,
        request: main_models.UpdateDBInstanceTDERequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDBInstanceTDEResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.tdestatus):
            query['TDEStatus'] = request.tdestatus
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDBInstanceTDE',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDBInstanceTDEResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dbinstance_tde(
        self,
        request: main_models.UpdateDBInstanceTDERequest,
    ) -> main_models.UpdateDBInstanceTDEResponse:
        runtime = RuntimeOptions()
        return self.update_dbinstance_tdewith_options(request, runtime)

    async def update_dbinstance_tde_async(
        self,
        request: main_models.UpdateDBInstanceTDERequest,
    ) -> main_models.UpdateDBInstanceTDEResponse:
        runtime = RuntimeOptions()
        return await self.update_dbinstance_tdewith_options_async(request, runtime)

    def update_polar_dbxinstance_node_with_options(
        self,
        request: main_models.UpdatePolarDBXInstanceNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolarDBXInstanceNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_dnspec):
            query['AddDNSpec'] = request.add_dnspec
        if not DaraCore.is_null(request.cnnode_count):
            query['CNNodeCount'] = request.cnnode_count
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dnnode_count):
            query['DNNodeCount'] = request.dnnode_count
        if not DaraCore.is_null(request.db_instance_node_count):
            query['DbInstanceNodeCount'] = request.db_instance_node_count
        if not DaraCore.is_null(request.delete_dnids):
            query['DeleteDNIds'] = request.delete_dnids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.storage_pool_name):
            query['StoragePoolName'] = request.storage_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolarDBXInstanceNode',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolarDBXInstanceNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_polar_dbxinstance_node_with_options_async(
        self,
        request: main_models.UpdatePolarDBXInstanceNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolarDBXInstanceNodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.add_dnspec):
            query['AddDNSpec'] = request.add_dnspec
        if not DaraCore.is_null(request.cnnode_count):
            query['CNNodeCount'] = request.cnnode_count
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.dnnode_count):
            query['DNNodeCount'] = request.dnnode_count
        if not DaraCore.is_null(request.db_instance_node_count):
            query['DbInstanceNodeCount'] = request.db_instance_node_count
        if not DaraCore.is_null(request.delete_dnids):
            query['DeleteDNIds'] = request.delete_dnids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.storage_pool_name):
            query['StoragePoolName'] = request.storage_pool_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolarDBXInstanceNode',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolarDBXInstanceNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_polar_dbxinstance_node(
        self,
        request: main_models.UpdatePolarDBXInstanceNodeRequest,
    ) -> main_models.UpdatePolarDBXInstanceNodeResponse:
        runtime = RuntimeOptions()
        return self.update_polar_dbxinstance_node_with_options(request, runtime)

    async def update_polar_dbxinstance_node_async(
        self,
        request: main_models.UpdatePolarDBXInstanceNodeRequest,
    ) -> main_models.UpdatePolarDBXInstanceNodeResponse:
        runtime = RuntimeOptions()
        return await self.update_polar_dbxinstance_node_with_options_async(request, runtime)

    def upgrade_cdcversion_with_options(
        self,
        request: main_models.UpgradeCDCVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeCDCVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cdc_db_version):
            query['CdcDbVersion'] = request.cdc_db_version
        if not DaraCore.is_null(request.cdc_minor_version):
            query['CdcMinorVersion'] = request.cdc_minor_version
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeCDCVersion',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeCDCVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_cdcversion_with_options_async(
        self,
        request: main_models.UpgradeCDCVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeCDCVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cdc_db_version):
            query['CdcDbVersion'] = request.cdc_db_version
        if not DaraCore.is_null(request.cdc_minor_version):
            query['CdcMinorVersion'] = request.cdc_minor_version
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeCDCVersion',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeCDCVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_cdcversion(
        self,
        request: main_models.UpgradeCDCVersionRequest,
    ) -> main_models.UpgradeCDCVersionResponse:
        runtime = RuntimeOptions()
        return self.upgrade_cdcversion_with_options(request, runtime)

    async def upgrade_cdcversion_async(
        self,
        request: main_models.UpgradeCDCVersionRequest,
    ) -> main_models.UpgradeCDCVersionResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_cdcversion_with_options_async(request, runtime)

    def upgrade_columnar_version_with_options(
        self,
        request: main_models.UpgradeColumnarVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeColumnarVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.columnar_version):
            query['ColumnarVersion'] = request.columnar_version
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeColumnarVersion',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeColumnarVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_columnar_version_with_options_async(
        self,
        request: main_models.UpgradeColumnarVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeColumnarVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.columnar_version):
            query['ColumnarVersion'] = request.columnar_version
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeColumnarVersion',
            version = '2020-02-02',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeColumnarVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_columnar_version(
        self,
        request: main_models.UpgradeColumnarVersionRequest,
    ) -> main_models.UpgradeColumnarVersionResponse:
        runtime = RuntimeOptions()
        return self.upgrade_columnar_version_with_options(request, runtime)

    async def upgrade_columnar_version_async(
        self,
        request: main_models.UpgradeColumnarVersionRequest,
    ) -> main_models.UpgradeColumnarVersionResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_columnar_version_with_options_async(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(
        self,
        request: main_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeDBInstanceKernelVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.minor_version):
            query['MinorVersion'] = request.minor_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBInstanceKernelVersion',
            version = '2020-02-02',
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
        if not DaraCore.is_null(request.dbinstance_name):
            query['DBInstanceName'] = request.dbinstance_name
        if not DaraCore.is_null(request.minor_version):
            query['MinorVersion'] = request.minor_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.switch_mode):
            query['SwitchMode'] = request.switch_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeDBInstanceKernelVersion',
            version = '2020-02-02',
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
