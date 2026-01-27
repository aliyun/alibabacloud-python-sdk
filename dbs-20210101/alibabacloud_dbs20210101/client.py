# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dbs20210101 import models as main_models
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
            'cn-qingdao': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-chengdu': 'dbs-api.cn-chengdu.aliyuncs.com',
            'cn-zhangjiakou': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-huhehaote': 'dbs-api.cn-huhehaote.aliyuncs.com',
            'cn-hangzhou': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'ap-southeast-1': 'dbs-api.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'dbs-api.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'dbs-api.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'dbs-api.ap-southeast-5.aliyuncs.com',
            'ap-northeast-1': 'dbs-api.ap-northeast-1.aliyuncs.com',
            'us-west-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'us-east-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'eu-central-1': 'dbs-api.eu-central-1.aliyuncs.com',
            'cn-hangzhou-finance': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shanghai-finance-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'ap-south-1': 'dbs-api.ap-south-1.aliyuncs.com',
            'eu-west-1': 'dbs-api.eu-west-1.aliyuncs.com',
            'me-east-1': 'dbs-api.me-east-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dbs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2021-01-01',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2021-01-01',
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

    def configure_backup_set_info_with_options(
        self,
        request: main_models.ConfigureBackupSetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureBackupSetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.backup_set_name):
            query['BackupSetName'] = request.backup_set_name
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.check_sum):
            query['CheckSum'] = request.check_sum
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.extra_meta):
            query['ExtraMeta'] = request.extra_meta
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.upload_status):
            query['UploadStatus'] = request.upload_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureBackupSetInfo',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureBackupSetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_backup_set_info_with_options_async(
        self,
        request: main_models.ConfigureBackupSetInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureBackupSetInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.backup_set_name):
            query['BackupSetName'] = request.backup_set_name
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.check_sum):
            query['CheckSum'] = request.check_sum
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.extra_meta):
            query['ExtraMeta'] = request.extra_meta
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.upload_status):
            query['UploadStatus'] = request.upload_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureBackupSetInfo',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureBackupSetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_backup_set_info(
        self,
        request: main_models.ConfigureBackupSetInfoRequest,
    ) -> main_models.ConfigureBackupSetInfoResponse:
        runtime = RuntimeOptions()
        return self.configure_backup_set_info_with_options(request, runtime)

    async def configure_backup_set_info_async(
        self,
        request: main_models.ConfigureBackupSetInfoRequest,
    ) -> main_models.ConfigureBackupSetInfoResponse:
        runtime = RuntimeOptions()
        return await self.configure_backup_set_info_with_options_async(request, runtime)

    def create_advanced_policy_with_options(
        self,
        request: main_models.CreateAdvancedPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAdvancedPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAdvancedPolicy',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAdvancedPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_advanced_policy_with_options_async(
        self,
        request: main_models.CreateAdvancedPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAdvancedPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAdvancedPolicy',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAdvancedPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_advanced_policy(
        self,
        request: main_models.CreateAdvancedPolicyRequest,
    ) -> main_models.CreateAdvancedPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_advanced_policy_with_options(request, runtime)

    async def create_advanced_policy_async(
        self,
        request: main_models.CreateAdvancedPolicyRequest,
    ) -> main_models.CreateAdvancedPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_advanced_policy_with_options_async(request, runtime)

    def create_download_with_options(
        self,
        request: main_models.CreateDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.admin_database):
            query['AdminDatabase'] = request.admin_database
        if not DaraCore.is_null(request.bak_set_id):
            query['BakSetId'] = request.bak_set_id
        if not DaraCore.is_null(request.bak_set_size):
            query['BakSetSize'] = request.bak_set_size
        if not DaraCore.is_null(request.bak_set_type):
            query['BakSetType'] = request.bak_set_type
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.download_point_in_time):
            query['DownloadPointInTime'] = request.download_point_in_time
        if not DaraCore.is_null(request.format_type):
            query['FormatType'] = request.format_type
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.is_cluster):
            query['IsCluster'] = request.is_cluster
        if not DaraCore.is_null(request.is_physical):
            query['IsPhysical'] = request.is_physical
        if not DaraCore.is_null(request.primary_key_type_only):
            query['PrimaryKeyTypeOnly'] = request.primary_key_type_only
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.target_bucket):
            query['TargetBucket'] = request.target_bucket
        if not DaraCore.is_null(request.target_oss_region):
            query['TargetOssRegion'] = request.target_oss_region
        if not DaraCore.is_null(request.target_path):
            query['TargetPath'] = request.target_path
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.use_zstd):
            query['UseZstd'] = request.use_zstd
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDownload',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_download_with_options_async(
        self,
        request: main_models.CreateDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.admin_database):
            query['AdminDatabase'] = request.admin_database
        if not DaraCore.is_null(request.bak_set_id):
            query['BakSetId'] = request.bak_set_id
        if not DaraCore.is_null(request.bak_set_size):
            query['BakSetSize'] = request.bak_set_size
        if not DaraCore.is_null(request.bak_set_type):
            query['BakSetType'] = request.bak_set_type
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.download_point_in_time):
            query['DownloadPointInTime'] = request.download_point_in_time
        if not DaraCore.is_null(request.format_type):
            query['FormatType'] = request.format_type
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.is_cluster):
            query['IsCluster'] = request.is_cluster
        if not DaraCore.is_null(request.is_physical):
            query['IsPhysical'] = request.is_physical
        if not DaraCore.is_null(request.primary_key_type_only):
            query['PrimaryKeyTypeOnly'] = request.primary_key_type_only
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.target_bucket):
            query['TargetBucket'] = request.target_bucket
        if not DaraCore.is_null(request.target_oss_region):
            query['TargetOssRegion'] = request.target_oss_region
        if not DaraCore.is_null(request.target_path):
            query['TargetPath'] = request.target_path
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.use_zstd):
            query['UseZstd'] = request.use_zstd
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDownload',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDownloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_download(
        self,
        request: main_models.CreateDownloadRequest,
    ) -> main_models.CreateDownloadResponse:
        runtime = RuntimeOptions()
        return self.create_download_with_options(request, runtime)

    async def create_download_async(
        self,
        request: main_models.CreateDownloadRequest,
    ) -> main_models.CreateDownloadResponse:
        runtime = RuntimeOptions()
        return await self.create_download_with_options_async(request, runtime)

    def delete_sandbox_instance_with_options(
        self,
        request: main_models.DeleteSandboxInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSandboxInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSandboxInstance',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSandboxInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sandbox_instance_with_options_async(
        self,
        request: main_models.DeleteSandboxInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSandboxInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSandboxInstance',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSandboxInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sandbox_instance(
        self,
        request: main_models.DeleteSandboxInstanceRequest,
    ) -> main_models.DeleteSandboxInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_sandbox_instance_with_options(request, runtime)

    async def delete_sandbox_instance_async(
        self,
        request: main_models.DeleteSandboxInstanceRequest,
    ) -> main_models.DeleteSandboxInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_sandbox_instance_with_options_async(request, runtime)

    def describe_backup_data_list_with_options(
        self,
        request: main_models.DescribeBackupDataListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupDataListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not DaraCore.is_null(request.backup_scale):
            query['BackupScale'] = request.backup_scale
        if not DaraCore.is_null(request.backup_status):
            query['BackupStatus'] = request.backup_status
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_is_deleted):
            query['InstanceIsDeleted'] = request.instance_is_deleted
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_region):
            query['InstanceRegion'] = request.instance_region
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.scene_type):
            query['SceneType'] = request.scene_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupDataList',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupDataListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_data_list_with_options_async(
        self,
        request: main_models.DescribeBackupDataListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupDataListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.backup_mode):
            query['BackupMode'] = request.backup_mode
        if not DaraCore.is_null(request.backup_scale):
            query['BackupScale'] = request.backup_scale
        if not DaraCore.is_null(request.backup_status):
            query['BackupStatus'] = request.backup_status
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_is_deleted):
            query['InstanceIsDeleted'] = request.instance_is_deleted
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_region):
            query['InstanceRegion'] = request.instance_region
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.scene_type):
            query['SceneType'] = request.scene_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupDataList',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupDataListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_data_list(
        self,
        request: main_models.DescribeBackupDataListRequest,
    ) -> main_models.DescribeBackupDataListResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_data_list_with_options(request, runtime)

    async def describe_backup_data_list_async(
        self,
        request: main_models.DescribeBackupDataListRequest,
    ) -> main_models.DescribeBackupDataListResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_data_list_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: main_models.DescribeBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2021-01-01',
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
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2021-01-01',
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

    def describe_bak_data_source_storage_access_info_with_options(
        self,
        request: main_models.DescribeBakDataSourceStorageAccessInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBakDataSourceStorageAccessInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.duration_seconds):
            query['DurationSeconds'] = request.duration_seconds
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBakDataSourceStorageAccessInfo',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBakDataSourceStorageAccessInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_bak_data_source_storage_access_info_with_options_async(
        self,
        request: main_models.DescribeBakDataSourceStorageAccessInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBakDataSourceStorageAccessInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.duration_seconds):
            query['DurationSeconds'] = request.duration_seconds
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBakDataSourceStorageAccessInfo',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBakDataSourceStorageAccessInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_bak_data_source_storage_access_info(
        self,
        request: main_models.DescribeBakDataSourceStorageAccessInfoRequest,
    ) -> main_models.DescribeBakDataSourceStorageAccessInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_bak_data_source_storage_access_info_with_options(request, runtime)

    async def describe_bak_data_source_storage_access_info_async(
        self,
        request: main_models.DescribeBakDataSourceStorageAccessInfoRequest,
    ) -> main_models.DescribeBakDataSourceStorageAccessInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_bak_data_source_storage_access_info_with_options_async(request, runtime)

    def describe_cost_info_by_dbs_instance_with_options(
        self,
        request: main_models.DescribeCostInfoByDbsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCostInfoByDbsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCostInfoByDbsInstance',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCostInfoByDbsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cost_info_by_dbs_instance_with_options_async(
        self,
        request: main_models.DescribeCostInfoByDbsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCostInfoByDbsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCostInfoByDbsInstance',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCostInfoByDbsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cost_info_by_dbs_instance(
        self,
        request: main_models.DescribeCostInfoByDbsInstanceRequest,
    ) -> main_models.DescribeCostInfoByDbsInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_cost_info_by_dbs_instance_with_options(request, runtime)

    async def describe_cost_info_by_dbs_instance_async(
        self,
        request: main_models.DescribeCostInfoByDbsInstanceRequest,
    ) -> main_models.DescribeCostInfoByDbsInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_cost_info_by_dbs_instance_with_options_async(request, runtime)

    def describe_dbtables_recovery_backup_set_with_options(
        self,
        request: main_models.DescribeDBTablesRecoveryBackupSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBTablesRecoveryBackupSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBTablesRecoveryBackupSet',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBTablesRecoveryBackupSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbtables_recovery_backup_set_with_options_async(
        self,
        request: main_models.DescribeDBTablesRecoveryBackupSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBTablesRecoveryBackupSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBTablesRecoveryBackupSet',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBTablesRecoveryBackupSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbtables_recovery_backup_set(
        self,
        request: main_models.DescribeDBTablesRecoveryBackupSetRequest,
    ) -> main_models.DescribeDBTablesRecoveryBackupSetResponse:
        runtime = RuntimeOptions()
        return self.describe_dbtables_recovery_backup_set_with_options(request, runtime)

    async def describe_dbtables_recovery_backup_set_async(
        self,
        request: main_models.DescribeDBTablesRecoveryBackupSetRequest,
    ) -> main_models.DescribeDBTablesRecoveryBackupSetResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbtables_recovery_backup_set_with_options_async(request, runtime)

    def describe_dbtables_recovery_state_with_options(
        self,
        request: main_models.DescribeDBTablesRecoveryStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBTablesRecoveryStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBTablesRecoveryState',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBTablesRecoveryStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbtables_recovery_state_with_options_async(
        self,
        request: main_models.DescribeDBTablesRecoveryStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBTablesRecoveryStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBTablesRecoveryState',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBTablesRecoveryStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbtables_recovery_state(
        self,
        request: main_models.DescribeDBTablesRecoveryStateRequest,
    ) -> main_models.DescribeDBTablesRecoveryStateResponse:
        runtime = RuntimeOptions()
        return self.describe_dbtables_recovery_state_with_options(request, runtime)

    async def describe_dbtables_recovery_state_async(
        self,
        request: main_models.DescribeDBTablesRecoveryStateRequest,
    ) -> main_models.DescribeDBTablesRecoveryStateResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbtables_recovery_state_with_options_async(request, runtime)

    def describe_dbtables_recovery_time_range_with_options(
        self,
        request: main_models.DescribeDBTablesRecoveryTimeRangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBTablesRecoveryTimeRangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBTablesRecoveryTimeRange',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBTablesRecoveryTimeRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbtables_recovery_time_range_with_options_async(
        self,
        request: main_models.DescribeDBTablesRecoveryTimeRangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBTablesRecoveryTimeRangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBTablesRecoveryTimeRange',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBTablesRecoveryTimeRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbtables_recovery_time_range(
        self,
        request: main_models.DescribeDBTablesRecoveryTimeRangeRequest,
    ) -> main_models.DescribeDBTablesRecoveryTimeRangeResponse:
        runtime = RuntimeOptions()
        return self.describe_dbtables_recovery_time_range_with_options(request, runtime)

    async def describe_dbtables_recovery_time_range_async(
        self,
        request: main_models.DescribeDBTablesRecoveryTimeRangeRequest,
    ) -> main_models.DescribeDBTablesRecoveryTimeRangeResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbtables_recovery_time_range_with_options_async(request, runtime)

    def describe_download_backup_set_storage_info_with_options(
        self,
        request: main_models.DescribeDownloadBackupSetStorageInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadBackupSetStorageInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadBackupSetStorageInfo',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadBackupSetStorageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_backup_set_storage_info_with_options_async(
        self,
        request: main_models.DescribeDownloadBackupSetStorageInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadBackupSetStorageInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadBackupSetStorageInfo',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadBackupSetStorageInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_backup_set_storage_info(
        self,
        request: main_models.DescribeDownloadBackupSetStorageInfoRequest,
    ) -> main_models.DescribeDownloadBackupSetStorageInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_download_backup_set_storage_info_with_options(request, runtime)

    async def describe_download_backup_set_storage_info_async(
        self,
        request: main_models.DescribeDownloadBackupSetStorageInfoRequest,
    ) -> main_models.DescribeDownloadBackupSetStorageInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_download_backup_set_storage_info_with_options_async(request, runtime)

    def describe_download_support_with_options(
        self,
        request: main_models.DescribeDownloadSupportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadSupportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadSupport',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadSupportResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_support_with_options_async(
        self,
        request: main_models.DescribeDownloadSupportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadSupportResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadSupport',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadSupportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_support(
        self,
        request: main_models.DescribeDownloadSupportRequest,
    ) -> main_models.DescribeDownloadSupportResponse:
        runtime = RuntimeOptions()
        return self.describe_download_support_with_options(request, runtime)

    async def describe_download_support_async(
        self,
        request: main_models.DescribeDownloadSupportRequest,
    ) -> main_models.DescribeDownloadSupportResponse:
        runtime = RuntimeOptions()
        return await self.describe_download_support_with_options_async(request, runtime)

    def describe_download_task_with_options(
        self,
        request: main_models.DescribeDownloadTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.datasource_id):
            query['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_direct):
            query['OrderDirect'] = request.order_direct
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadTask',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_task_with_options_async(
        self,
        request: main_models.DescribeDownloadTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDownloadTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.datasource_id):
            query['DatasourceId'] = request.datasource_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.order_column):
            query['OrderColumn'] = request.order_column
        if not DaraCore.is_null(request.order_direct):
            query['OrderDirect'] = request.order_direct
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDownloadTask',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDownloadTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_task(
        self,
        request: main_models.DescribeDownloadTaskRequest,
    ) -> main_models.DescribeDownloadTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_download_task_with_options(request, runtime)

    async def describe_download_task_async(
        self,
        request: main_models.DescribeDownloadTaskRequest,
    ) -> main_models.DescribeDownloadTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_download_task_with_options_async(request, runtime)

    def describe_sandbox_backup_sets_with_options(
        self,
        request: main_models.DescribeSandboxBackupSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSandboxBackupSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSandboxBackupSets',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSandboxBackupSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sandbox_backup_sets_with_options_async(
        self,
        request: main_models.DescribeSandboxBackupSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSandboxBackupSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSandboxBackupSets',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSandboxBackupSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sandbox_backup_sets(
        self,
        request: main_models.DescribeSandboxBackupSetsRequest,
    ) -> main_models.DescribeSandboxBackupSetsResponse:
        runtime = RuntimeOptions()
        return self.describe_sandbox_backup_sets_with_options(request, runtime)

    async def describe_sandbox_backup_sets_async(
        self,
        request: main_models.DescribeSandboxBackupSetsRequest,
    ) -> main_models.DescribeSandboxBackupSetsResponse:
        runtime = RuntimeOptions()
        return await self.describe_sandbox_backup_sets_with_options_async(request, runtime)

    def describe_sandbox_instances_with_options(
        self,
        request: main_models.DescribeSandboxInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSandboxInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSandboxInstances',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSandboxInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sandbox_instances_with_options_async(
        self,
        request: main_models.DescribeSandboxInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSandboxInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSandboxInstances',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSandboxInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sandbox_instances(
        self,
        request: main_models.DescribeSandboxInstancesRequest,
    ) -> main_models.DescribeSandboxInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_sandbox_instances_with_options(request, runtime)

    async def describe_sandbox_instances_async(
        self,
        request: main_models.DescribeSandboxInstancesRequest,
    ) -> main_models.DescribeSandboxInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_sandbox_instances_with_options_async(request, runtime)

    def describe_sandbox_recovery_time_with_options(
        self,
        request: main_models.DescribeSandboxRecoveryTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSandboxRecoveryTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSandboxRecoveryTime',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSandboxRecoveryTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sandbox_recovery_time_with_options_async(
        self,
        request: main_models.DescribeSandboxRecoveryTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSandboxRecoveryTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSandboxRecoveryTime',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSandboxRecoveryTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sandbox_recovery_time(
        self,
        request: main_models.DescribeSandboxRecoveryTimeRequest,
    ) -> main_models.DescribeSandboxRecoveryTimeResponse:
        runtime = RuntimeOptions()
        return self.describe_sandbox_recovery_time_with_options(request, runtime)

    async def describe_sandbox_recovery_time_async(
        self,
        request: main_models.DescribeSandboxRecoveryTimeRequest,
    ) -> main_models.DescribeSandboxRecoveryTimeResponse:
        runtime = RuntimeOptions()
        return await self.describe_sandbox_recovery_time_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        tmp_req: main_models.ModifyBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPolicyResponse:
        tmp_req.validate()
        request = main_models.ModifyBackupPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.advance_data_policies):
            request.advance_data_policies_shrink = Utils.array_to_string_with_specified_style(tmp_req.advance_data_policies, 'AdvanceDataPolicies', 'json')
        if not DaraCore.is_null(tmp_req.advance_inc_policies):
            request.advance_inc_policies_shrink = Utils.array_to_string_with_specified_style(tmp_req.advance_inc_policies, 'AdvanceIncPolicies', 'json')
        if not DaraCore.is_null(tmp_req.advance_log_policies):
            request.advance_log_policies_shrink = Utils.array_to_string_with_specified_style(tmp_req.advance_log_policies, 'AdvanceLogPolicies', 'json')
        query = {}
        if not DaraCore.is_null(request.advance_data_policies_shrink):
            query['AdvanceDataPolicies'] = request.advance_data_policies_shrink
        if not DaraCore.is_null(request.advance_inc_policies_shrink):
            query['AdvanceIncPolicies'] = request.advance_inc_policies_shrink
        if not DaraCore.is_null(request.advance_log_policies_shrink):
            query['AdvanceLogPolicies'] = request.advance_log_policies_shrink
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.backup_priority):
            query['BackupPriority'] = request.backup_priority
        if not DaraCore.is_null(request.backup_retention_policy_on_cluster_deletion):
            query['BackupRetentionPolicyOnClusterDeletion'] = request.backup_retention_policy_on_cluster_deletion
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.enable_inc_backup):
            query['EnableIncBackup'] = request.enable_inc_backup
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.preferred_backup_window_begin):
            query['PreferredBackupWindowBegin'] = request.preferred_backup_window_begin
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPolicy',
            version = '2021-01-01',
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
        tmp_req: main_models.ModifyBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPolicyResponse:
        tmp_req.validate()
        request = main_models.ModifyBackupPolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.advance_data_policies):
            request.advance_data_policies_shrink = Utils.array_to_string_with_specified_style(tmp_req.advance_data_policies, 'AdvanceDataPolicies', 'json')
        if not DaraCore.is_null(tmp_req.advance_inc_policies):
            request.advance_inc_policies_shrink = Utils.array_to_string_with_specified_style(tmp_req.advance_inc_policies, 'AdvanceIncPolicies', 'json')
        if not DaraCore.is_null(tmp_req.advance_log_policies):
            request.advance_log_policies_shrink = Utils.array_to_string_with_specified_style(tmp_req.advance_log_policies, 'AdvanceLogPolicies', 'json')
        query = {}
        if not DaraCore.is_null(request.advance_data_policies_shrink):
            query['AdvanceDataPolicies'] = request.advance_data_policies_shrink
        if not DaraCore.is_null(request.advance_inc_policies_shrink):
            query['AdvanceIncPolicies'] = request.advance_inc_policies_shrink
        if not DaraCore.is_null(request.advance_log_policies_shrink):
            query['AdvanceLogPolicies'] = request.advance_log_policies_shrink
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.backup_priority):
            query['BackupPriority'] = request.backup_priority
        if not DaraCore.is_null(request.backup_retention_policy_on_cluster_deletion):
            query['BackupRetentionPolicyOnClusterDeletion'] = request.backup_retention_policy_on_cluster_deletion
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.enable_inc_backup):
            query['EnableIncBackup'] = request.enable_inc_backup
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.preferred_backup_window_begin):
            query['PreferredBackupWindowBegin'] = request.preferred_backup_window_begin
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPolicy',
            version = '2021-01-01',
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

    def modify_dbtables_recovery_state_with_options(
        self,
        request: main_models.ModifyDBTablesRecoveryStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBTablesRecoveryStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.retention):
            query['Retention'] = request.retention
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBTablesRecoveryState',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBTablesRecoveryStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbtables_recovery_state_with_options_async(
        self,
        request: main_models.ModifyDBTablesRecoveryStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDBTablesRecoveryStateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.retention):
            query['Retention'] = request.retention
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDBTablesRecoveryState',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDBTablesRecoveryStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbtables_recovery_state(
        self,
        request: main_models.ModifyDBTablesRecoveryStateRequest,
    ) -> main_models.ModifyDBTablesRecoveryStateResponse:
        runtime = RuntimeOptions()
        return self.modify_dbtables_recovery_state_with_options(request, runtime)

    async def modify_dbtables_recovery_state_async(
        self,
        request: main_models.ModifyDBTablesRecoveryStateRequest,
    ) -> main_models.ModifyDBTablesRecoveryStateResponse:
        runtime = RuntimeOptions()
        return await self.modify_dbtables_recovery_state_with_options_async(request, runtime)

    def retry_download_task_with_options(
        self,
        request: main_models.RetryDownloadTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryDownloadTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryDownloadTask',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryDownloadTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_download_task_with_options_async(
        self,
        request: main_models.RetryDownloadTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RetryDownloadTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RetryDownloadTask',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RetryDownloadTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_download_task(
        self,
        request: main_models.RetryDownloadTaskRequest,
    ) -> main_models.RetryDownloadTaskResponse:
        runtime = RuntimeOptions()
        return self.retry_download_task_with_options(request, runtime)

    async def retry_download_task_async(
        self,
        request: main_models.RetryDownloadTaskRequest,
    ) -> main_models.RetryDownloadTaskResponse:
        runtime = RuntimeOptions()
        return await self.retry_download_task_with_options_async(request, runtime)

    def support_dbtable_recovery_with_options(
        self,
        request: main_models.SupportDBTableRecoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SupportDBTableRecoveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SupportDBTableRecovery',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SupportDBTableRecoveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def support_dbtable_recovery_with_options_async(
        self,
        request: main_models.SupportDBTableRecoveryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SupportDBTableRecoveryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.region_code):
            query['RegionCode'] = request.region_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SupportDBTableRecovery',
            version = '2021-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SupportDBTableRecoveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def support_dbtable_recovery(
        self,
        request: main_models.SupportDBTableRecoveryRequest,
    ) -> main_models.SupportDBTableRecoveryResponse:
        runtime = RuntimeOptions()
        return self.support_dbtable_recovery_with_options(request, runtime)

    async def support_dbtable_recovery_async(
        self,
        request: main_models.SupportDBTableRecoveryRequest,
    ) -> main_models.SupportDBTableRecoveryResponse:
        runtime = RuntimeOptions()
        return await self.support_dbtable_recovery_with_options_async(request, runtime)
