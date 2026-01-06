# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_hbr20170908 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
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
            'ap-northeast-2-pop': 'hbr.aliyuncs.com',
            'cn-beijing-finance-pop': 'hbr.aliyuncs.com',
            'cn-beijing-gov-1': 'hbr.aliyuncs.com',
            'cn-beijing-nu16-b01': 'hbr.aliyuncs.com',
            'cn-edge-1': 'hbr.aliyuncs.com',
            'cn-fujian': 'hbr.aliyuncs.com',
            'cn-haidian-cm12-c01': 'hbr.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'hbr.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'hbr.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'hbr.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'hbr.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'hbr.aliyuncs.com',
            'cn-hangzhou-test-306': 'hbr.aliyuncs.com',
            'cn-hongkong-finance-pop': 'hbr.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'hbr.aliyuncs.com',
            'cn-qingdao-nebula': 'hbr.aliyuncs.com',
            'cn-shanghai-et15-b01': 'hbr.aliyuncs.com',
            'cn-shanghai-et2-b01': 'hbr.aliyuncs.com',
            'cn-shanghai-inner': 'hbr.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'hbr.aliyuncs.com',
            'cn-shenzhen-inner': 'hbr.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'hbr.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'hbr.aliyuncs.com',
            'cn-wuhan': 'hbr.aliyuncs.com',
            'cn-yushanfang': 'hbr.aliyuncs.com',
            'cn-zhangbei': 'hbr.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'hbr.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'hbr.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'hbr.aliyuncs.com',
            'eu-west-1-oxs': 'hbr.aliyuncs.com',
            'rus-west-1-pop': 'hbr.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('hbr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_container_cluster_with_options(
        self,
        request: main_models.AddContainerClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddContainerClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddContainerCluster',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddContainerClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_container_cluster_with_options_async(
        self,
        request: main_models.AddContainerClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddContainerClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddContainerCluster',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddContainerClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_container_cluster(
        self,
        request: main_models.AddContainerClusterRequest,
    ) -> main_models.AddContainerClusterResponse:
        runtime = RuntimeOptions()
        return self.add_container_cluster_with_options(request, runtime)

    async def add_container_cluster_async(
        self,
        request: main_models.AddContainerClusterRequest,
    ) -> main_models.AddContainerClusterResponse:
        runtime = RuntimeOptions()
        return await self.add_container_cluster_with_options_async(request, runtime)

    def cancel_backup_job_with_options(
        self,
        request: main_models.CancelBackupJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelBackupJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelBackupJob',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelBackupJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_backup_job_with_options_async(
        self,
        request: main_models.CancelBackupJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelBackupJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelBackupJob',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelBackupJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_backup_job(
        self,
        request: main_models.CancelBackupJobRequest,
    ) -> main_models.CancelBackupJobResponse:
        runtime = RuntimeOptions()
        return self.cancel_backup_job_with_options(request, runtime)

    async def cancel_backup_job_async(
        self,
        request: main_models.CancelBackupJobRequest,
    ) -> main_models.CancelBackupJobResponse:
        runtime = RuntimeOptions()
        return await self.cancel_backup_job_with_options_async(request, runtime)

    def cancel_restore_job_with_options(
        self,
        request: main_models.CancelRestoreJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRestoreJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.restore_id):
            query['RestoreId'] = request.restore_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelRestoreJob',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRestoreJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_restore_job_with_options_async(
        self,
        request: main_models.CancelRestoreJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRestoreJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.restore_id):
            query['RestoreId'] = request.restore_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelRestoreJob',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRestoreJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_restore_job(
        self,
        request: main_models.CancelRestoreJobRequest,
    ) -> main_models.CancelRestoreJobResponse:
        runtime = RuntimeOptions()
        return self.cancel_restore_job_with_options(request, runtime)

    async def cancel_restore_job_async(
        self,
        request: main_models.CancelRestoreJobRequest,
    ) -> main_models.CancelRestoreJobResponse:
        runtime = RuntimeOptions()
        return await self.cancel_restore_job_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2017-09-08',
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
        body = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2017-09-08',
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

    def check_role_with_options(
        self,
        request: main_models.CheckRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_role_type):
            query['CheckRoleType'] = request.check_role_type
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckRole',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_role_with_options_async(
        self,
        request: main_models.CheckRoleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.check_role_type):
            query['CheckRoleType'] = request.check_role_type
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckRole',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_role(
        self,
        request: main_models.CheckRoleRequest,
    ) -> main_models.CheckRoleResponse:
        runtime = RuntimeOptions()
        return self.check_role_with_options(request, runtime)

    async def check_role_async(
        self,
        request: main_models.CheckRoleRequest,
    ) -> main_models.CheckRoleResponse:
        runtime = RuntimeOptions()
        return await self.check_role_with_options_async(request, runtime)

    def create_backup_job_with_options(
        self,
        tmp_req: main_models.CreateBackupJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupJobResponse:
        tmp_req.validate()
        request = main_models.CreateBackupJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.detail):
            request.detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        query = {}
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.container_cluster_id):
            query['ContainerClusterId'] = request.container_cluster_id
        if not DaraCore.is_null(request.container_resources):
            query['ContainerResources'] = request.container_resources
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not DaraCore.is_null(request.exclude):
            query['Exclude'] = request.exclude
        if not DaraCore.is_null(request.include):
            query['Include'] = request.include
        if not DaraCore.is_null(request.initiated_by_ack):
            query['InitiatedByAck'] = request.initiated_by_ack
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        if not DaraCore.is_null(request.retention):
            query['Retention'] = request.retention
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackupJob',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_job_with_options_async(
        self,
        tmp_req: main_models.CreateBackupJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupJobResponse:
        tmp_req.validate()
        request = main_models.CreateBackupJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.detail):
            request.detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        query = {}
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.container_cluster_id):
            query['ContainerClusterId'] = request.container_cluster_id
        if not DaraCore.is_null(request.container_resources):
            query['ContainerResources'] = request.container_resources
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not DaraCore.is_null(request.exclude):
            query['Exclude'] = request.exclude
        if not DaraCore.is_null(request.include):
            query['Include'] = request.include
        if not DaraCore.is_null(request.initiated_by_ack):
            query['InitiatedByAck'] = request.initiated_by_ack
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        if not DaraCore.is_null(request.retention):
            query['Retention'] = request.retention
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackupJob',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup_job(
        self,
        request: main_models.CreateBackupJobRequest,
    ) -> main_models.CreateBackupJobResponse:
        runtime = RuntimeOptions()
        return self.create_backup_job_with_options(request, runtime)

    async def create_backup_job_async(
        self,
        request: main_models.CreateBackupJobRequest,
    ) -> main_models.CreateBackupJobResponse:
        runtime = RuntimeOptions()
        return await self.create_backup_job_with_options_async(request, runtime)

    def create_backup_plan_with_options(
        self,
        tmp_req: main_models.CreateBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupPlanResponse:
        tmp_req.validate()
        request = main_models.CreateBackupPlanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dest_data_source_detail):
            request.dest_data_source_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.dest_data_source_detail, 'DestDataSourceDetail', 'json')
        if not DaraCore.is_null(tmp_req.detail):
            request.detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        if not DaraCore.is_null(tmp_req.ots_detail):
            request.ots_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        query = {}
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.change_list_path):
            query['ChangeListPath'] = request.change_list_path
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.dest_data_source_detail_shrink):
            query['DestDataSourceDetail'] = request.dest_data_source_detail_shrink
        if not DaraCore.is_null(request.dest_data_source_id):
            query['DestDataSourceId'] = request.dest_data_source_id
        if not DaraCore.is_null(request.dest_source_type):
            query['DestSourceType'] = request.dest_source_type
        if not DaraCore.is_null(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.keep_latest_snapshots):
            query['KeepLatestSnapshots'] = request.keep_latest_snapshots
        if not DaraCore.is_null(request.plan_name):
            query['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.prefix):
            query['Prefix'] = request.prefix
        if not DaraCore.is_null(request.retention):
            query['Retention'] = request.retention
        if not DaraCore.is_null(request.schedule):
            query['Schedule'] = request.schedule
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.exclude):
            body['Exclude'] = request.exclude
        if not DaraCore.is_null(request.include):
            body['Include'] = request.include
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.rule):
            body['Rule'] = request.rule
        if not DaraCore.is_null(request.speed_limit):
            body['SpeedLimit'] = request.speed_limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_plan_with_options_async(
        self,
        tmp_req: main_models.CreateBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupPlanResponse:
        tmp_req.validate()
        request = main_models.CreateBackupPlanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dest_data_source_detail):
            request.dest_data_source_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.dest_data_source_detail, 'DestDataSourceDetail', 'json')
        if not DaraCore.is_null(tmp_req.detail):
            request.detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        if not DaraCore.is_null(tmp_req.ots_detail):
            request.ots_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        query = {}
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.change_list_path):
            query['ChangeListPath'] = request.change_list_path
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.dest_data_source_detail_shrink):
            query['DestDataSourceDetail'] = request.dest_data_source_detail_shrink
        if not DaraCore.is_null(request.dest_data_source_id):
            query['DestDataSourceId'] = request.dest_data_source_id
        if not DaraCore.is_null(request.dest_source_type):
            query['DestSourceType'] = request.dest_source_type
        if not DaraCore.is_null(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not DaraCore.is_null(request.keep_latest_snapshots):
            query['KeepLatestSnapshots'] = request.keep_latest_snapshots
        if not DaraCore.is_null(request.plan_name):
            query['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.prefix):
            query['Prefix'] = request.prefix
        if not DaraCore.is_null(request.retention):
            query['Retention'] = request.retention
        if not DaraCore.is_null(request.schedule):
            query['Schedule'] = request.schedule
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.exclude):
            body['Exclude'] = request.exclude
        if not DaraCore.is_null(request.include):
            body['Include'] = request.include
        if not DaraCore.is_null(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not DaraCore.is_null(request.path):
            body['Path'] = request.path
        if not DaraCore.is_null(request.rule):
            body['Rule'] = request.rule
        if not DaraCore.is_null(request.speed_limit):
            body['SpeedLimit'] = request.speed_limit
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup_plan(
        self,
        request: main_models.CreateBackupPlanRequest,
    ) -> main_models.CreateBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.create_backup_plan_with_options(request, runtime)

    async def create_backup_plan_async(
        self,
        request: main_models.CreateBackupPlanRequest,
    ) -> main_models.CreateBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.create_backup_plan_with_options_async(request, runtime)

    def create_clients_with_options(
        self,
        request: main_models.CreateClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not DaraCore.is_null(request.client_info):
            query['ClientInfo'] = request.client_info
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.use_https):
            query['UseHttps'] = request.use_https
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateClients',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_clients_with_options_async(
        self,
        request: main_models.CreateClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not DaraCore.is_null(request.client_info):
            query['ClientInfo'] = request.client_info
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.use_https):
            query['UseHttps'] = request.use_https
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateClients',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_clients(
        self,
        request: main_models.CreateClientsRequest,
    ) -> main_models.CreateClientsResponse:
        runtime = RuntimeOptions()
        return self.create_clients_with_options(request, runtime)

    async def create_clients_async(
        self,
        request: main_models.CreateClientsRequest,
    ) -> main_models.CreateClientsResponse:
        runtime = RuntimeOptions()
        return await self.create_clients_with_options_async(request, runtime)

    def create_hana_backup_plan_with_options(
        self,
        request: main_models.CreateHanaBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHanaBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.plan_name):
            query['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.schedule):
            query['Schedule'] = request.schedule
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHanaBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hana_backup_plan_with_options_async(
        self,
        request: main_models.CreateHanaBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHanaBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not DaraCore.is_null(request.backup_type):
            query['BackupType'] = request.backup_type
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.plan_name):
            query['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.schedule):
            query['Schedule'] = request.schedule
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHanaBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHanaBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hana_backup_plan(
        self,
        request: main_models.CreateHanaBackupPlanRequest,
    ) -> main_models.CreateHanaBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.create_hana_backup_plan_with_options(request, runtime)

    async def create_hana_backup_plan_async(
        self,
        request: main_models.CreateHanaBackupPlanRequest,
    ) -> main_models.CreateHanaBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.create_hana_backup_plan_with_options_async(request, runtime)

    def create_hana_instance_with_options(
        self,
        request: main_models.CreateHanaInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHanaInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not DaraCore.is_null(request.hana_name):
            query['HanaName'] = request.hana_name
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.instance_number):
            query['InstanceNumber'] = request.instance_number
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sid):
            query['Sid'] = request.sid
        if not DaraCore.is_null(request.use_ssl):
            query['UseSsl'] = request.use_ssl
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.validate_certificate):
            query['ValidateCertificate'] = request.validate_certificate
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHanaInstance',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHanaInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hana_instance_with_options_async(
        self,
        request: main_models.CreateHanaInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHanaInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not DaraCore.is_null(request.hana_name):
            query['HanaName'] = request.hana_name
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.instance_number):
            query['InstanceNumber'] = request.instance_number
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sid):
            query['Sid'] = request.sid
        if not DaraCore.is_null(request.use_ssl):
            query['UseSsl'] = request.use_ssl
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.validate_certificate):
            query['ValidateCertificate'] = request.validate_certificate
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHanaInstance',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHanaInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hana_instance(
        self,
        request: main_models.CreateHanaInstanceRequest,
    ) -> main_models.CreateHanaInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_hana_instance_with_options(request, runtime)

    async def create_hana_instance_async(
        self,
        request: main_models.CreateHanaInstanceRequest,
    ) -> main_models.CreateHanaInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_hana_instance_with_options_async(request, runtime)

    def create_hana_restore_with_options(
        self,
        request: main_models.CreateHanaRestoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHanaRestoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not DaraCore.is_null(request.check_access):
            query['CheckAccess'] = request.check_access
        if not DaraCore.is_null(request.clear_log):
            query['ClearLog'] = request.clear_log
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.log_position):
            query['LogPosition'] = request.log_position
        if not DaraCore.is_null(request.master_client_id):
            query['MasterClientId'] = request.master_client_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.recovery_point_in_time):
            query['RecoveryPointInTime'] = request.recovery_point_in_time
        if not DaraCore.is_null(request.sid_admin):
            query['SidAdmin'] = request.sid_admin
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_cluster_id):
            query['SourceClusterId'] = request.source_cluster_id
        if not DaraCore.is_null(request.system_copy):
            query['SystemCopy'] = request.system_copy
        if not DaraCore.is_null(request.use_catalog):
            query['UseCatalog'] = request.use_catalog
        if not DaraCore.is_null(request.use_delta):
            query['UseDelta'] = request.use_delta
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        if not DaraCore.is_null(request.volume_id):
            query['VolumeId'] = request.volume_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHanaRestore',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHanaRestoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hana_restore_with_options_async(
        self,
        request: main_models.CreateHanaRestoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHanaRestoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not DaraCore.is_null(request.check_access):
            query['CheckAccess'] = request.check_access
        if not DaraCore.is_null(request.clear_log):
            query['ClearLog'] = request.clear_log
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.log_position):
            query['LogPosition'] = request.log_position
        if not DaraCore.is_null(request.master_client_id):
            query['MasterClientId'] = request.master_client_id
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.recovery_point_in_time):
            query['RecoveryPointInTime'] = request.recovery_point_in_time
        if not DaraCore.is_null(request.sid_admin):
            query['SidAdmin'] = request.sid_admin
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_cluster_id):
            query['SourceClusterId'] = request.source_cluster_id
        if not DaraCore.is_null(request.system_copy):
            query['SystemCopy'] = request.system_copy
        if not DaraCore.is_null(request.use_catalog):
            query['UseCatalog'] = request.use_catalog
        if not DaraCore.is_null(request.use_delta):
            query['UseDelta'] = request.use_delta
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        if not DaraCore.is_null(request.volume_id):
            query['VolumeId'] = request.volume_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHanaRestore',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHanaRestoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hana_restore(
        self,
        request: main_models.CreateHanaRestoreRequest,
    ) -> main_models.CreateHanaRestoreResponse:
        runtime = RuntimeOptions()
        return self.create_hana_restore_with_options(request, runtime)

    async def create_hana_restore_async(
        self,
        request: main_models.CreateHanaRestoreRequest,
    ) -> main_models.CreateHanaRestoreResponse:
        runtime = RuntimeOptions()
        return await self.create_hana_restore_with_options_async(request, runtime)

    def create_policy_bindings_with_options(
        self,
        tmp_req: main_models.CreatePolicyBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyBindingsResponse:
        tmp_req.validate()
        request = main_models.CreatePolicyBindingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.policy_binding_list):
            request.policy_binding_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy_binding_list, 'PolicyBindingList', 'json')
        query = {}
        if not DaraCore.is_null(request.policy_binding_list_shrink):
            query['PolicyBindingList'] = request.policy_binding_list_shrink
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyBindings',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_bindings_with_options_async(
        self,
        tmp_req: main_models.CreatePolicyBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyBindingsResponse:
        tmp_req.validate()
        request = main_models.CreatePolicyBindingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.policy_binding_list):
            request.policy_binding_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.policy_binding_list, 'PolicyBindingList', 'json')
        query = {}
        if not DaraCore.is_null(request.policy_binding_list_shrink):
            query['PolicyBindingList'] = request.policy_binding_list_shrink
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyBindings',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_bindings(
        self,
        request: main_models.CreatePolicyBindingsRequest,
    ) -> main_models.CreatePolicyBindingsResponse:
        runtime = RuntimeOptions()
        return self.create_policy_bindings_with_options(request, runtime)

    async def create_policy_bindings_async(
        self,
        request: main_models.CreatePolicyBindingsRequest,
    ) -> main_models.CreatePolicyBindingsResponse:
        runtime = RuntimeOptions()
        return await self.create_policy_bindings_with_options_async(request, runtime)

    def create_policy_v2with_options(
        self,
        tmp_req: main_models.CreatePolicyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyV2Response:
        tmp_req.validate()
        request = main_models.CreatePolicyV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not DaraCore.is_null(request.policy_description):
            body['PolicyDescription'] = request.policy_description
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            body['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyV2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_v2with_options_async(
        self,
        tmp_req: main_models.CreatePolicyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePolicyV2Response:
        tmp_req.validate()
        request = main_models.CreatePolicyV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not DaraCore.is_null(request.policy_description):
            body['PolicyDescription'] = request.policy_description
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.policy_type):
            body['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePolicyV2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePolicyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy_v2(
        self,
        request: main_models.CreatePolicyV2Request,
    ) -> main_models.CreatePolicyV2Response:
        runtime = RuntimeOptions()
        return self.create_policy_v2with_options(request, runtime)

    async def create_policy_v2_async(
        self,
        request: main_models.CreatePolicyV2Request,
    ) -> main_models.CreatePolicyV2Response:
        runtime = RuntimeOptions()
        return await self.create_policy_v2with_options_async(request, runtime)

    def create_replication_vault_with_options(
        self,
        request: main_models.CreateReplicationVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateReplicationVaultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.redundancy_type):
            query['RedundancyType'] = request.redundancy_type
        if not DaraCore.is_null(request.replication_source_region_id):
            query['ReplicationSourceRegionId'] = request.replication_source_region_id
        if not DaraCore.is_null(request.replication_source_vault_id):
            query['ReplicationSourceVaultId'] = request.replication_source_vault_id
        if not DaraCore.is_null(request.vault_name):
            query['VaultName'] = request.vault_name
        if not DaraCore.is_null(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not DaraCore.is_null(request.vault_storage_class):
            query['VaultStorageClass'] = request.vault_storage_class
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateReplicationVault',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateReplicationVaultResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_replication_vault_with_options_async(
        self,
        request: main_models.CreateReplicationVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateReplicationVaultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.redundancy_type):
            query['RedundancyType'] = request.redundancy_type
        if not DaraCore.is_null(request.replication_source_region_id):
            query['ReplicationSourceRegionId'] = request.replication_source_region_id
        if not DaraCore.is_null(request.replication_source_vault_id):
            query['ReplicationSourceVaultId'] = request.replication_source_vault_id
        if not DaraCore.is_null(request.vault_name):
            query['VaultName'] = request.vault_name
        if not DaraCore.is_null(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not DaraCore.is_null(request.vault_storage_class):
            query['VaultStorageClass'] = request.vault_storage_class
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateReplicationVault',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateReplicationVaultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_replication_vault(
        self,
        request: main_models.CreateReplicationVaultRequest,
    ) -> main_models.CreateReplicationVaultResponse:
        runtime = RuntimeOptions()
        return self.create_replication_vault_with_options(request, runtime)

    async def create_replication_vault_async(
        self,
        request: main_models.CreateReplicationVaultRequest,
    ) -> main_models.CreateReplicationVaultResponse:
        runtime = RuntimeOptions()
        return await self.create_replication_vault_with_options_async(request, runtime)

    def create_restore_job_with_options(
        self,
        tmp_req: main_models.CreateRestoreJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRestoreJobResponse:
        tmp_req.validate()
        request = main_models.CreateRestoreJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.failback_detail):
            request.failback_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.failback_detail, 'FailbackDetail', 'json')
        if not DaraCore.is_null(tmp_req.ots_detail):
            request.ots_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        if not DaraCore.is_null(tmp_req.udm_detail):
            request.udm_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.udm_detail, 'UdmDetail', 'json')
        query = {}
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.failback_detail_shrink):
            query['FailbackDetail'] = request.failback_detail_shrink
        if not DaraCore.is_null(request.initiated_by_ack):
            query['InitiatedByAck'] = request.initiated_by_ack
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not DaraCore.is_null(request.snapshot_hash):
            query['SnapshotHash'] = request.snapshot_hash
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.target_bucket):
            query['TargetBucket'] = request.target_bucket
        if not DaraCore.is_null(request.target_container):
            query['TargetContainer'] = request.target_container
        if not DaraCore.is_null(request.target_container_cluster_id):
            query['TargetContainerClusterId'] = request.target_container_cluster_id
        if not DaraCore.is_null(request.target_create_time):
            query['TargetCreateTime'] = request.target_create_time
        if not DaraCore.is_null(request.target_file_system_id):
            query['TargetFileSystemId'] = request.target_file_system_id
        if not DaraCore.is_null(request.target_instance_name):
            query['TargetInstanceName'] = request.target_instance_name
        if not DaraCore.is_null(request.target_prefix):
            query['TargetPrefix'] = request.target_prefix
        if not DaraCore.is_null(request.target_table_name):
            query['TargetTableName'] = request.target_table_name
        if not DaraCore.is_null(request.target_time):
            query['TargetTime'] = request.target_time
        if not DaraCore.is_null(request.udm_detail_shrink):
            query['UdmDetail'] = request.udm_detail_shrink
        if not DaraCore.is_null(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not DaraCore.is_null(request.exclude):
            body['Exclude'] = request.exclude
        if not DaraCore.is_null(request.include):
            body['Include'] = request.include
        if not DaraCore.is_null(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not DaraCore.is_null(request.target_instance_id):
            body['TargetInstanceId'] = request.target_instance_id
        if not DaraCore.is_null(request.target_path):
            body['TargetPath'] = request.target_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRestoreJob',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRestoreJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_restore_job_with_options_async(
        self,
        tmp_req: main_models.CreateRestoreJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRestoreJobResponse:
        tmp_req.validate()
        request = main_models.CreateRestoreJobShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.failback_detail):
            request.failback_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.failback_detail, 'FailbackDetail', 'json')
        if not DaraCore.is_null(tmp_req.ots_detail):
            request.ots_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        if not DaraCore.is_null(tmp_req.udm_detail):
            request.udm_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.udm_detail, 'UdmDetail', 'json')
        query = {}
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.failback_detail_shrink):
            query['FailbackDetail'] = request.failback_detail_shrink
        if not DaraCore.is_null(request.initiated_by_ack):
            query['InitiatedByAck'] = request.initiated_by_ack
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        if not DaraCore.is_null(request.snapshot_hash):
            query['SnapshotHash'] = request.snapshot_hash
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.target_bucket):
            query['TargetBucket'] = request.target_bucket
        if not DaraCore.is_null(request.target_container):
            query['TargetContainer'] = request.target_container
        if not DaraCore.is_null(request.target_container_cluster_id):
            query['TargetContainerClusterId'] = request.target_container_cluster_id
        if not DaraCore.is_null(request.target_create_time):
            query['TargetCreateTime'] = request.target_create_time
        if not DaraCore.is_null(request.target_file_system_id):
            query['TargetFileSystemId'] = request.target_file_system_id
        if not DaraCore.is_null(request.target_instance_name):
            query['TargetInstanceName'] = request.target_instance_name
        if not DaraCore.is_null(request.target_prefix):
            query['TargetPrefix'] = request.target_prefix
        if not DaraCore.is_null(request.target_table_name):
            query['TargetTableName'] = request.target_table_name
        if not DaraCore.is_null(request.target_time):
            query['TargetTime'] = request.target_time
        if not DaraCore.is_null(request.udm_detail_shrink):
            query['UdmDetail'] = request.udm_detail_shrink
        if not DaraCore.is_null(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not DaraCore.is_null(request.exclude):
            body['Exclude'] = request.exclude
        if not DaraCore.is_null(request.include):
            body['Include'] = request.include
        if not DaraCore.is_null(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not DaraCore.is_null(request.target_instance_id):
            body['TargetInstanceId'] = request.target_instance_id
        if not DaraCore.is_null(request.target_path):
            body['TargetPath'] = request.target_path
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRestoreJob',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRestoreJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_restore_job(
        self,
        request: main_models.CreateRestoreJobRequest,
    ) -> main_models.CreateRestoreJobResponse:
        runtime = RuntimeOptions()
        return self.create_restore_job_with_options(request, runtime)

    async def create_restore_job_async(
        self,
        request: main_models.CreateRestoreJobRequest,
    ) -> main_models.CreateRestoreJobResponse:
        runtime = RuntimeOptions()
        return await self.create_restore_job_with_options_async(request, runtime)

    def create_temp_file_upload_url_with_options(
        self,
        request: main_models.CreateTempFileUploadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTempFileUploadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTempFileUploadUrl',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTempFileUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_temp_file_upload_url_with_options_async(
        self,
        request: main_models.CreateTempFileUploadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTempFileUploadUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTempFileUploadUrl',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTempFileUploadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_temp_file_upload_url(
        self,
        request: main_models.CreateTempFileUploadUrlRequest,
    ) -> main_models.CreateTempFileUploadUrlResponse:
        runtime = RuntimeOptions()
        return self.create_temp_file_upload_url_with_options(request, runtime)

    async def create_temp_file_upload_url_async(
        self,
        request: main_models.CreateTempFileUploadUrlRequest,
    ) -> main_models.CreateTempFileUploadUrlResponse:
        runtime = RuntimeOptions()
        return await self.create_temp_file_upload_url_with_options_async(request, runtime)

    def create_vault_with_options(
        self,
        request: main_models.CreateVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVaultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.replication):
            query['Replication'] = request.replication
        if not DaraCore.is_null(request.vault_name):
            query['VaultName'] = request.vault_name
        if not DaraCore.is_null(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not DaraCore.is_null(request.vault_storage_class):
            query['VaultStorageClass'] = request.vault_storage_class
        if not DaraCore.is_null(request.vault_type):
            query['VaultType'] = request.vault_type
        if not DaraCore.is_null(request.worm_enabled):
            query['WormEnabled'] = request.worm_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVault',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVaultResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vault_with_options_async(
        self,
        request: main_models.CreateVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVaultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not DaraCore.is_null(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not DaraCore.is_null(request.replication):
            query['Replication'] = request.replication
        if not DaraCore.is_null(request.vault_name):
            query['VaultName'] = request.vault_name
        if not DaraCore.is_null(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not DaraCore.is_null(request.vault_storage_class):
            query['VaultStorageClass'] = request.vault_storage_class
        if not DaraCore.is_null(request.vault_type):
            query['VaultType'] = request.vault_type
        if not DaraCore.is_null(request.worm_enabled):
            query['WormEnabled'] = request.worm_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVault',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVaultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vault(
        self,
        request: main_models.CreateVaultRequest,
    ) -> main_models.CreateVaultResponse:
        runtime = RuntimeOptions()
        return self.create_vault_with_options(request, runtime)

    async def create_vault_async(
        self,
        request: main_models.CreateVaultRequest,
    ) -> main_models.CreateVaultResponse:
        runtime = RuntimeOptions()
        return await self.create_vault_with_options_async(request, runtime)

    def create_vault_replication_with_options(
        self,
        request: main_models.CreateVaultReplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVaultReplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.replication_source_region_id):
            query['ReplicationSourceRegionId'] = request.replication_source_region_id
        if not DaraCore.is_null(request.replication_source_vault_id):
            query['ReplicationSourceVaultId'] = request.replication_source_vault_id
        if not DaraCore.is_null(request.replication_target_vault_id):
            query['ReplicationTargetVaultId'] = request.replication_target_vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVaultReplication',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVaultReplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vault_replication_with_options_async(
        self,
        request: main_models.CreateVaultReplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVaultReplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.replication_source_region_id):
            query['ReplicationSourceRegionId'] = request.replication_source_region_id
        if not DaraCore.is_null(request.replication_source_vault_id):
            query['ReplicationSourceVaultId'] = request.replication_source_vault_id
        if not DaraCore.is_null(request.replication_target_vault_id):
            query['ReplicationTargetVaultId'] = request.replication_target_vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVaultReplication',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVaultReplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vault_replication(
        self,
        request: main_models.CreateVaultReplicationRequest,
    ) -> main_models.CreateVaultReplicationResponse:
        runtime = RuntimeOptions()
        return self.create_vault_replication_with_options(request, runtime)

    async def create_vault_replication_async(
        self,
        request: main_models.CreateVaultReplicationRequest,
    ) -> main_models.CreateVaultReplicationResponse:
        runtime = RuntimeOptions()
        return await self.create_vault_replication_with_options_async(request, runtime)

    def delete_air_ecs_instance_with_options(
        self,
        tmp_req: main_models.DeleteAirEcsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAirEcsInstanceResponse:
        tmp_req.validate()
        request = main_models.DeleteAirEcsInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.uninstall_client_source_types):
            request.uninstall_client_source_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.uninstall_client_source_types, 'UninstallClientSourceTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not DaraCore.is_null(request.uninstall_client_source_types_shrink):
            query['UninstallClientSourceTypes'] = request.uninstall_client_source_types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAirEcsInstance',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAirEcsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_air_ecs_instance_with_options_async(
        self,
        tmp_req: main_models.DeleteAirEcsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAirEcsInstanceResponse:
        tmp_req.validate()
        request = main_models.DeleteAirEcsInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.uninstall_client_source_types):
            request.uninstall_client_source_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.uninstall_client_source_types, 'UninstallClientSourceTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.ecs_instance_id):
            query['EcsInstanceId'] = request.ecs_instance_id
        if not DaraCore.is_null(request.uninstall_client_source_types_shrink):
            query['UninstallClientSourceTypes'] = request.uninstall_client_source_types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAirEcsInstance',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAirEcsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_air_ecs_instance(
        self,
        request: main_models.DeleteAirEcsInstanceRequest,
    ) -> main_models.DeleteAirEcsInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_air_ecs_instance_with_options(request, runtime)

    async def delete_air_ecs_instance_async(
        self,
        request: main_models.DeleteAirEcsInstanceRequest,
    ) -> main_models.DeleteAirEcsInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_air_ecs_instance_with_options_async(request, runtime)

    def delete_backup_client_with_options(
        self,
        request: main_models.DeleteBackupClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackupClient',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_client_with_options_async(
        self,
        request: main_models.DeleteBackupClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackupClient',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup_client(
        self,
        request: main_models.DeleteBackupClientRequest,
    ) -> main_models.DeleteBackupClientResponse:
        runtime = RuntimeOptions()
        return self.delete_backup_client_with_options(request, runtime)

    async def delete_backup_client_async(
        self,
        request: main_models.DeleteBackupClientRequest,
    ) -> main_models.DeleteBackupClientResponse:
        runtime = RuntimeOptions()
        return await self.delete_backup_client_with_options_async(request, runtime)

    def delete_backup_client_resource_with_options(
        self,
        tmp_req: main_models.DeleteBackupClientResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupClientResourceResponse:
        tmp_req.validate()
        request = main_models.DeleteBackupClientResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_ids):
            request.client_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        query = {}
        if not DaraCore.is_null(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackupClientResource',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupClientResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_client_resource_with_options_async(
        self,
        tmp_req: main_models.DeleteBackupClientResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupClientResourceResponse:
        tmp_req.validate()
        request = main_models.DeleteBackupClientResourceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_ids):
            request.client_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        query = {}
        if not DaraCore.is_null(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackupClientResource',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupClientResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup_client_resource(
        self,
        request: main_models.DeleteBackupClientResourceRequest,
    ) -> main_models.DeleteBackupClientResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_backup_client_resource_with_options(request, runtime)

    async def delete_backup_client_resource_async(
        self,
        request: main_models.DeleteBackupClientResourceRequest,
    ) -> main_models.DeleteBackupClientResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_backup_client_resource_with_options_async(request, runtime)

    def delete_backup_plan_with_options(
        self,
        request: main_models.DeleteBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.require_no_running_jobs):
            query['RequireNoRunningJobs'] = request.require_no_running_jobs
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_plan_with_options_async(
        self,
        request: main_models.DeleteBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.require_no_running_jobs):
            query['RequireNoRunningJobs'] = request.require_no_running_jobs
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup_plan(
        self,
        request: main_models.DeleteBackupPlanRequest,
    ) -> main_models.DeleteBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.delete_backup_plan_with_options(request, runtime)

    async def delete_backup_plan_async(
        self,
        request: main_models.DeleteBackupPlanRequest,
    ) -> main_models.DeleteBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.delete_backup_plan_with_options_async(request, runtime)

    def delete_client_with_options(
        self,
        request: main_models.DeleteClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClient',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_client_with_options_async(
        self,
        request: main_models.DeleteClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteClient',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_client(
        self,
        request: main_models.DeleteClientRequest,
    ) -> main_models.DeleteClientResponse:
        runtime = RuntimeOptions()
        return self.delete_client_with_options(request, runtime)

    async def delete_client_async(
        self,
        request: main_models.DeleteClientRequest,
    ) -> main_models.DeleteClientResponse:
        runtime = RuntimeOptions()
        return await self.delete_client_with_options_async(request, runtime)

    def delete_hana_backup_plan_with_options(
        self,
        request: main_models.DeleteHanaBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHanaBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHanaBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hana_backup_plan_with_options_async(
        self,
        request: main_models.DeleteHanaBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHanaBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHanaBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHanaBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hana_backup_plan(
        self,
        request: main_models.DeleteHanaBackupPlanRequest,
    ) -> main_models.DeleteHanaBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.delete_hana_backup_plan_with_options(request, runtime)

    async def delete_hana_backup_plan_async(
        self,
        request: main_models.DeleteHanaBackupPlanRequest,
    ) -> main_models.DeleteHanaBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.delete_hana_backup_plan_with_options_async(request, runtime)

    def delete_hana_instance_with_options(
        self,
        request: main_models.DeleteHanaInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHanaInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sid):
            query['Sid'] = request.sid
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHanaInstance',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHanaInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hana_instance_with_options_async(
        self,
        request: main_models.DeleteHanaInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHanaInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sid):
            query['Sid'] = request.sid
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHanaInstance',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHanaInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hana_instance(
        self,
        request: main_models.DeleteHanaInstanceRequest,
    ) -> main_models.DeleteHanaInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_hana_instance_with_options(request, runtime)

    async def delete_hana_instance_async(
        self,
        request: main_models.DeleteHanaInstanceRequest,
    ) -> main_models.DeleteHanaInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_hana_instance_with_options_async(request, runtime)

    def delete_policy_binding_with_options(
        self,
        tmp_req: main_models.DeletePolicyBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyBindingResponse:
        tmp_req.validate()
        request = main_models.DeletePolicyBindingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source_ids):
            request.data_source_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not DaraCore.is_null(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyBinding',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_binding_with_options_async(
        self,
        tmp_req: main_models.DeletePolicyBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyBindingResponse:
        tmp_req.validate()
        request = main_models.DeletePolicyBindingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source_ids):
            request.data_source_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not DaraCore.is_null(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyBinding',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_binding(
        self,
        request: main_models.DeletePolicyBindingRequest,
    ) -> main_models.DeletePolicyBindingResponse:
        runtime = RuntimeOptions()
        return self.delete_policy_binding_with_options(request, runtime)

    async def delete_policy_binding_async(
        self,
        request: main_models.DeletePolicyBindingRequest,
    ) -> main_models.DeletePolicyBindingResponse:
        runtime = RuntimeOptions()
        return await self.delete_policy_binding_with_options_async(request, runtime)

    def delete_policy_v2with_options(
        self,
        request: main_models.DeletePolicyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyV2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyV2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_v2with_options_async(
        self,
        request: main_models.DeletePolicyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePolicyV2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePolicyV2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePolicyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_v2(
        self,
        request: main_models.DeletePolicyV2Request,
    ) -> main_models.DeletePolicyV2Response:
        runtime = RuntimeOptions()
        return self.delete_policy_v2with_options(request, runtime)

    async def delete_policy_v2_async(
        self,
        request: main_models.DeletePolicyV2Request,
    ) -> main_models.DeletePolicyV2Response:
        runtime = RuntimeOptions()
        return await self.delete_policy_v2with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: main_models.DeleteSnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSnapshot',
            version = '2017-09-08',
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
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSnapshot',
            version = '2017-09-08',
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

    def delete_udm_disk_with_options(
        self,
        request: main_models.DeleteUdmDiskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUdmDiskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUdmDisk',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUdmDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_udm_disk_with_options_async(
        self,
        request: main_models.DeleteUdmDiskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUdmDiskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUdmDisk',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUdmDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_udm_disk(
        self,
        request: main_models.DeleteUdmDiskRequest,
    ) -> main_models.DeleteUdmDiskResponse:
        runtime = RuntimeOptions()
        return self.delete_udm_disk_with_options(request, runtime)

    async def delete_udm_disk_async(
        self,
        request: main_models.DeleteUdmDiskRequest,
    ) -> main_models.DeleteUdmDiskResponse:
        runtime = RuntimeOptions()
        return await self.delete_udm_disk_with_options_async(request, runtime)

    def delete_udm_ecs_instance_with_options(
        self,
        request: main_models.DeleteUdmEcsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUdmEcsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUdmEcsInstance',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUdmEcsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_udm_ecs_instance_with_options_async(
        self,
        request: main_models.DeleteUdmEcsInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUdmEcsInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUdmEcsInstance',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUdmEcsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_udm_ecs_instance(
        self,
        request: main_models.DeleteUdmEcsInstanceRequest,
    ) -> main_models.DeleteUdmEcsInstanceResponse:
        runtime = RuntimeOptions()
        return self.delete_udm_ecs_instance_with_options(request, runtime)

    async def delete_udm_ecs_instance_async(
        self,
        request: main_models.DeleteUdmEcsInstanceRequest,
    ) -> main_models.DeleteUdmEcsInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_udm_ecs_instance_with_options_async(request, runtime)

    def delete_vault_with_options(
        self,
        request: main_models.DeleteVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVaultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVault',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVaultResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vault_with_options_async(
        self,
        request: main_models.DeleteVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVaultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVault',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVaultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vault(
        self,
        request: main_models.DeleteVaultRequest,
    ) -> main_models.DeleteVaultResponse:
        runtime = RuntimeOptions()
        return self.delete_vault_with_options(request, runtime)

    async def delete_vault_async(
        self,
        request: main_models.DeleteVaultRequest,
    ) -> main_models.DeleteVaultResponse:
        runtime = RuntimeOptions()
        return await self.delete_vault_with_options_async(request, runtime)

    def delete_vault_replication_with_options(
        self,
        request: main_models.DeleteVaultReplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVaultReplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.replication_source_region_id):
            query['ReplicationSourceRegionId'] = request.replication_source_region_id
        if not DaraCore.is_null(request.replication_source_vault_id):
            query['ReplicationSourceVaultId'] = request.replication_source_vault_id
        if not DaraCore.is_null(request.replication_target_vault_id):
            query['ReplicationTargetVaultId'] = request.replication_target_vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVaultReplication',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVaultReplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vault_replication_with_options_async(
        self,
        request: main_models.DeleteVaultReplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVaultReplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.replication_source_region_id):
            query['ReplicationSourceRegionId'] = request.replication_source_region_id
        if not DaraCore.is_null(request.replication_source_vault_id):
            query['ReplicationSourceVaultId'] = request.replication_source_vault_id
        if not DaraCore.is_null(request.replication_target_vault_id):
            query['ReplicationTargetVaultId'] = request.replication_target_vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVaultReplication',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVaultReplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vault_replication(
        self,
        request: main_models.DeleteVaultReplicationRequest,
    ) -> main_models.DeleteVaultReplicationResponse:
        runtime = RuntimeOptions()
        return self.delete_vault_replication_with_options(request, runtime)

    async def delete_vault_replication_async(
        self,
        request: main_models.DeleteVaultReplicationRequest,
    ) -> main_models.DeleteVaultReplicationResponse:
        runtime = RuntimeOptions()
        return await self.delete_vault_replication_with_options_async(request, runtime)

    def describe_backup_clients_with_options(
        self,
        tmp_req: main_models.DescribeBackupClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupClientsResponse:
        tmp_req.validate()
        request = main_models.DescribeBackupClientsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_ids):
            request.client_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.client_ids_shrink):
            body['ClientIds'] = request.client_ids_shrink
        if not DaraCore.is_null(request.instance_ids_shrink):
            body['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupClients',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_clients_with_options_async(
        self,
        tmp_req: main_models.DescribeBackupClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupClientsResponse:
        tmp_req.validate()
        request = main_models.DescribeBackupClientsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_ids):
            request.client_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not DaraCore.is_null(request.client_ids_shrink):
            body['ClientIds'] = request.client_ids_shrink
        if not DaraCore.is_null(request.instance_ids_shrink):
            body['InstanceIds'] = request.instance_ids_shrink
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupClients',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_clients(
        self,
        request: main_models.DescribeBackupClientsRequest,
    ) -> main_models.DescribeBackupClientsResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_clients_with_options(request, runtime)

    async def describe_backup_clients_async(
        self,
        request: main_models.DescribeBackupClientsRequest,
    ) -> main_models.DescribeBackupClientsResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_clients_with_options_async(request, runtime)

    def describe_backup_jobs_2with_options(
        self,
        request: main_models.DescribeBackupJobs2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupJobs2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupJobs2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupJobs2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_jobs_2with_options_async(
        self,
        request: main_models.DescribeBackupJobs2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupJobs2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupJobs2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupJobs2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_jobs_2(
        self,
        request: main_models.DescribeBackupJobs2Request,
    ) -> main_models.DescribeBackupJobs2Response:
        runtime = RuntimeOptions()
        return self.describe_backup_jobs_2with_options(request, runtime)

    async def describe_backup_jobs_2_async(
        self,
        request: main_models.DescribeBackupJobs2Request,
    ) -> main_models.DescribeBackupJobs2Response:
        runtime = RuntimeOptions()
        return await self.describe_backup_jobs_2with_options_async(request, runtime)

    def describe_backup_plans_with_options(
        self,
        request: main_models.DescribeBackupPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPlans',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_plans_with_options_async(
        self,
        request: main_models.DescribeBackupPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPlans',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_plans(
        self,
        request: main_models.DescribeBackupPlansRequest,
    ) -> main_models.DescribeBackupPlansResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_plans_with_options(request, runtime)

    async def describe_backup_plans_async(
        self,
        request: main_models.DescribeBackupPlansRequest,
    ) -> main_models.DescribeBackupPlansResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_plans_with_options_async(request, runtime)

    def describe_clients_with_options(
        self,
        request: main_models.DescribeClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClients',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_clients_with_options_async(
        self,
        request: main_models.DescribeClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClientsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClients',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_clients(
        self,
        request: main_models.DescribeClientsRequest,
    ) -> main_models.DescribeClientsResponse:
        runtime = RuntimeOptions()
        return self.describe_clients_with_options(request, runtime)

    async def describe_clients_async(
        self,
        request: main_models.DescribeClientsRequest,
    ) -> main_models.DescribeClientsResponse:
        runtime = RuntimeOptions()
        return await self.describe_clients_with_options_async(request, runtime)

    def describe_container_cluster_with_options(
        self,
        request: main_models.DescribeContainerClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeContainerClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeContainerCluster',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeContainerClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_container_cluster_with_options_async(
        self,
        request: main_models.DescribeContainerClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeContainerClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeContainerCluster',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeContainerClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_container_cluster(
        self,
        request: main_models.DescribeContainerClusterRequest,
    ) -> main_models.DescribeContainerClusterResponse:
        runtime = RuntimeOptions()
        return self.describe_container_cluster_with_options(request, runtime)

    async def describe_container_cluster_async(
        self,
        request: main_models.DescribeContainerClusterRequest,
    ) -> main_models.DescribeContainerClusterResponse:
        runtime = RuntimeOptions()
        return await self.describe_container_cluster_with_options_async(request, runtime)

    def describe_cross_accounts_with_options(
        self,
        request: main_models.DescribeCrossAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCrossAccountsResponse:
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
            action = 'DescribeCrossAccounts',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCrossAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cross_accounts_with_options_async(
        self,
        request: main_models.DescribeCrossAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCrossAccountsResponse:
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
            action = 'DescribeCrossAccounts',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCrossAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cross_accounts(
        self,
        request: main_models.DescribeCrossAccountsRequest,
    ) -> main_models.DescribeCrossAccountsResponse:
        runtime = RuntimeOptions()
        return self.describe_cross_accounts_with_options(request, runtime)

    async def describe_cross_accounts_async(
        self,
        request: main_models.DescribeCrossAccountsRequest,
    ) -> main_models.DescribeCrossAccountsResponse:
        runtime = RuntimeOptions()
        return await self.describe_cross_accounts_with_options_async(request, runtime)

    def describe_hana_backup_plans_with_options(
        self,
        request: main_models.DescribeHanaBackupPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaBackupPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaBackupPlans',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaBackupPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_backup_plans_with_options_async(
        self,
        request: main_models.DescribeHanaBackupPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaBackupPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaBackupPlans',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaBackupPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_backup_plans(
        self,
        request: main_models.DescribeHanaBackupPlansRequest,
    ) -> main_models.DescribeHanaBackupPlansResponse:
        runtime = RuntimeOptions()
        return self.describe_hana_backup_plans_with_options(request, runtime)

    async def describe_hana_backup_plans_async(
        self,
        request: main_models.DescribeHanaBackupPlansRequest,
    ) -> main_models.DescribeHanaBackupPlansResponse:
        runtime = RuntimeOptions()
        return await self.describe_hana_backup_plans_with_options_async(request, runtime)

    def describe_hana_backup_setting_with_options(
        self,
        request: main_models.DescribeHanaBackupSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaBackupSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaBackupSetting',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaBackupSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_backup_setting_with_options_async(
        self,
        request: main_models.DescribeHanaBackupSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaBackupSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaBackupSetting',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaBackupSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_backup_setting(
        self,
        request: main_models.DescribeHanaBackupSettingRequest,
    ) -> main_models.DescribeHanaBackupSettingResponse:
        runtime = RuntimeOptions()
        return self.describe_hana_backup_setting_with_options(request, runtime)

    async def describe_hana_backup_setting_async(
        self,
        request: main_models.DescribeHanaBackupSettingRequest,
    ) -> main_models.DescribeHanaBackupSettingResponse:
        runtime = RuntimeOptions()
        return await self.describe_hana_backup_setting_with_options_async(request, runtime)

    def describe_hana_backups_async_with_options(
        self,
        request: main_models.DescribeHanaBackupsAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaBackupsAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.include_differential):
            query['IncludeDifferential'] = request.include_differential
        if not DaraCore.is_null(request.include_incremental):
            query['IncludeIncremental'] = request.include_incremental
        if not DaraCore.is_null(request.include_log):
            query['IncludeLog'] = request.include_log
        if not DaraCore.is_null(request.log_position):
            query['LogPosition'] = request.log_position
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.recovery_point_in_time):
            query['RecoveryPointInTime'] = request.recovery_point_in_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_cluster_id):
            query['SourceClusterId'] = request.source_cluster_id
        if not DaraCore.is_null(request.system_copy):
            query['SystemCopy'] = request.system_copy
        if not DaraCore.is_null(request.use_backint):
            query['UseBackint'] = request.use_backint
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        if not DaraCore.is_null(request.volume_id):
            query['VolumeId'] = request.volume_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaBackupsAsync',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaBackupsAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_backups_async_with_options_async(
        self,
        request: main_models.DescribeHanaBackupsAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaBackupsAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.include_differential):
            query['IncludeDifferential'] = request.include_differential
        if not DaraCore.is_null(request.include_incremental):
            query['IncludeIncremental'] = request.include_incremental
        if not DaraCore.is_null(request.include_log):
            query['IncludeLog'] = request.include_log
        if not DaraCore.is_null(request.log_position):
            query['LogPosition'] = request.log_position
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.recovery_point_in_time):
            query['RecoveryPointInTime'] = request.recovery_point_in_time
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_cluster_id):
            query['SourceClusterId'] = request.source_cluster_id
        if not DaraCore.is_null(request.system_copy):
            query['SystemCopy'] = request.system_copy
        if not DaraCore.is_null(request.use_backint):
            query['UseBackint'] = request.use_backint
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        if not DaraCore.is_null(request.volume_id):
            query['VolumeId'] = request.volume_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaBackupsAsync',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaBackupsAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_backups_async(
        self,
        request: main_models.DescribeHanaBackupsAsyncRequest,
    ) -> main_models.DescribeHanaBackupsAsyncResponse:
        runtime = RuntimeOptions()
        return self.describe_hana_backups_async_with_options(request, runtime)

    async def describe_hana_backups_async_async(
        self,
        request: main_models.DescribeHanaBackupsAsyncRequest,
    ) -> main_models.DescribeHanaBackupsAsyncResponse:
        runtime = RuntimeOptions()
        return await self.describe_hana_backups_async_with_options_async(request, runtime)

    def describe_hana_databases_with_options(
        self,
        request: main_models.DescribeHanaDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaDatabases',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_databases_with_options_async(
        self,
        request: main_models.DescribeHanaDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaDatabases',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_databases(
        self,
        request: main_models.DescribeHanaDatabasesRequest,
    ) -> main_models.DescribeHanaDatabasesResponse:
        runtime = RuntimeOptions()
        return self.describe_hana_databases_with_options(request, runtime)

    async def describe_hana_databases_async(
        self,
        request: main_models.DescribeHanaDatabasesRequest,
    ) -> main_models.DescribeHanaDatabasesResponse:
        runtime = RuntimeOptions()
        return await self.describe_hana_databases_with_options_async(request, runtime)

    def describe_hana_instances_with_options(
        self,
        request: main_models.DescribeHanaInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaInstances',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_instances_with_options_async(
        self,
        request: main_models.DescribeHanaInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaInstances',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_instances(
        self,
        request: main_models.DescribeHanaInstancesRequest,
    ) -> main_models.DescribeHanaInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_hana_instances_with_options(request, runtime)

    async def describe_hana_instances_async(
        self,
        request: main_models.DescribeHanaInstancesRequest,
    ) -> main_models.DescribeHanaInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_hana_instances_with_options_async(request, runtime)

    def describe_hana_restores_with_options(
        self,
        request: main_models.DescribeHanaRestoresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaRestoresResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.restore_id):
            query['RestoreId'] = request.restore_id
        if not DaraCore.is_null(request.restore_status):
            query['RestoreStatus'] = request.restore_status
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaRestores',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaRestoresResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_restores_with_options_async(
        self,
        request: main_models.DescribeHanaRestoresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaRestoresResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.restore_id):
            query['RestoreId'] = request.restore_id
        if not DaraCore.is_null(request.restore_status):
            query['RestoreStatus'] = request.restore_status
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaRestores',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaRestoresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_restores(
        self,
        request: main_models.DescribeHanaRestoresRequest,
    ) -> main_models.DescribeHanaRestoresResponse:
        runtime = RuntimeOptions()
        return self.describe_hana_restores_with_options(request, runtime)

    async def describe_hana_restores_async(
        self,
        request: main_models.DescribeHanaRestoresRequest,
    ) -> main_models.DescribeHanaRestoresResponse:
        runtime = RuntimeOptions()
        return await self.describe_hana_restores_with_options_async(request, runtime)

    def describe_hana_retention_setting_with_options(
        self,
        request: main_models.DescribeHanaRetentionSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaRetentionSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaRetentionSetting',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaRetentionSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hana_retention_setting_with_options_async(
        self,
        request: main_models.DescribeHanaRetentionSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHanaRetentionSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHanaRetentionSetting',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHanaRetentionSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hana_retention_setting(
        self,
        request: main_models.DescribeHanaRetentionSettingRequest,
    ) -> main_models.DescribeHanaRetentionSettingResponse:
        runtime = RuntimeOptions()
        return self.describe_hana_retention_setting_with_options(request, runtime)

    async def describe_hana_retention_setting_async(
        self,
        request: main_models.DescribeHanaRetentionSettingRequest,
    ) -> main_models.DescribeHanaRetentionSettingResponse:
        runtime = RuntimeOptions()
        return await self.describe_hana_retention_setting_with_options_async(request, runtime)

    def describe_ots_table_snapshots_with_options(
        self,
        request: main_models.DescribeOtsTableSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOtsTableSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            body['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        body_flat = {}
        if not DaraCore.is_null(request.ots_instances):
            body_flat['OtsInstances'] = request.ots_instances
        if not DaraCore.is_null(request.snapshot_ids):
            body_flat['SnapshotIds'] = request.snapshot_ids
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOtsTableSnapshots',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOtsTableSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ots_table_snapshots_with_options_async(
        self,
        request: main_models.DescribeOtsTableSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOtsTableSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            body['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        body_flat = {}
        if not DaraCore.is_null(request.ots_instances):
            body_flat['OtsInstances'] = request.ots_instances
        if not DaraCore.is_null(request.snapshot_ids):
            body_flat['SnapshotIds'] = request.snapshot_ids
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOtsTableSnapshots',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOtsTableSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ots_table_snapshots(
        self,
        request: main_models.DescribeOtsTableSnapshotsRequest,
    ) -> main_models.DescribeOtsTableSnapshotsResponse:
        runtime = RuntimeOptions()
        return self.describe_ots_table_snapshots_with_options(request, runtime)

    async def describe_ots_table_snapshots_async(
        self,
        request: main_models.DescribeOtsTableSnapshotsRequest,
    ) -> main_models.DescribeOtsTableSnapshotsResponse:
        runtime = RuntimeOptions()
        return await self.describe_ots_table_snapshots_with_options_async(request, runtime)

    def describe_policies_v2with_options(
        self,
        request: main_models.DescribePoliciesV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePoliciesV2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribePoliciesV2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePoliciesV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_policies_v2with_options_async(
        self,
        request: main_models.DescribePoliciesV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePoliciesV2Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribePoliciesV2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePoliciesV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policies_v2(
        self,
        request: main_models.DescribePoliciesV2Request,
    ) -> main_models.DescribePoliciesV2Response:
        runtime = RuntimeOptions()
        return self.describe_policies_v2with_options(request, runtime)

    async def describe_policies_v2_async(
        self,
        request: main_models.DescribePoliciesV2Request,
    ) -> main_models.DescribePoliciesV2Response:
        runtime = RuntimeOptions()
        return await self.describe_policies_v2with_options_async(request, runtime)

    def describe_policy_bindings_with_options(
        self,
        tmp_req: main_models.DescribePolicyBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyBindingsResponse:
        tmp_req.validate()
        request = main_models.DescribePolicyBindingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source_ids):
            request.data_source_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not DaraCore.is_null(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyBindings',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_bindings_with_options_async(
        self,
        tmp_req: main_models.DescribePolicyBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePolicyBindingsResponse:
        tmp_req.validate()
        request = main_models.DescribePolicyBindingsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.data_source_ids):
            request.data_source_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.data_source_ids, 'DataSourceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not DaraCore.is_null(request.data_source_ids_shrink):
            body['DataSourceIds'] = request.data_source_ids_shrink
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribePolicyBindings',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePolicyBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_bindings(
        self,
        request: main_models.DescribePolicyBindingsRequest,
    ) -> main_models.DescribePolicyBindingsResponse:
        runtime = RuntimeOptions()
        return self.describe_policy_bindings_with_options(request, runtime)

    async def describe_policy_bindings_async(
        self,
        request: main_models.DescribePolicyBindingsRequest,
    ) -> main_models.DescribePolicyBindingsResponse:
        runtime = RuntimeOptions()
        return await self.describe_policy_bindings_with_options_async(request, runtime)

    def describe_recoverable_ots_instances_with_options(
        self,
        request: main_models.DescribeRecoverableOtsInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecoverableOtsInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecoverableOtsInstances',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecoverableOtsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recoverable_ots_instances_with_options_async(
        self,
        request: main_models.DescribeRecoverableOtsInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecoverableOtsInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecoverableOtsInstances',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecoverableOtsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recoverable_ots_instances(
        self,
        request: main_models.DescribeRecoverableOtsInstancesRequest,
    ) -> main_models.DescribeRecoverableOtsInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_recoverable_ots_instances_with_options(request, runtime)

    async def describe_recoverable_ots_instances_async(
        self,
        request: main_models.DescribeRecoverableOtsInstancesRequest,
    ) -> main_models.DescribeRecoverableOtsInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_recoverable_ots_instances_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2017-09-08',
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
            version = '2017-09-08',
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

    def describe_restore_jobs_2with_options(
        self,
        request: main_models.DescribeRestoreJobs2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreJobs2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreJobs2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreJobs2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_jobs_2with_options_async(
        self,
        request: main_models.DescribeRestoreJobs2Request,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreJobs2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.restore_type):
            query['RestoreType'] = request.restore_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreJobs2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreJobs2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_jobs_2(
        self,
        request: main_models.DescribeRestoreJobs2Request,
    ) -> main_models.DescribeRestoreJobs2Response:
        runtime = RuntimeOptions()
        return self.describe_restore_jobs_2with_options(request, runtime)

    async def describe_restore_jobs_2_async(
        self,
        request: main_models.DescribeRestoreJobs2Request,
    ) -> main_models.DescribeRestoreJobs2Response:
        runtime = RuntimeOptions()
        return await self.describe_restore_jobs_2with_options_async(request, runtime)

    def describe_task_with_options(
        self,
        request: main_models.DescribeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTask',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_with_options_async(
        self,
        request: main_models.DescribeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTask',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task(
        self,
        request: main_models.DescribeTaskRequest,
    ) -> main_models.DescribeTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_task_with_options(request, runtime)

    async def describe_task_async(
        self,
        request: main_models.DescribeTaskRequest,
    ) -> main_models.DescribeTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_task_with_options_async(request, runtime)

    def describe_udm_snapshots_with_options(
        self,
        tmp_req: main_models.DescribeUdmSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUdmSnapshotsResponse:
        tmp_req.validate()
        request = main_models.DescribeUdmSnapshotsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.snapshot_ids):
            request.snapshot_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.snapshot_ids, 'SnapshotIds', 'json')
        query = {}
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        body = {}
        if not DaraCore.is_null(request.snapshot_ids_shrink):
            body['SnapshotIds'] = request.snapshot_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUdmSnapshots',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUdmSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_udm_snapshots_with_options_async(
        self,
        tmp_req: main_models.DescribeUdmSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUdmSnapshotsResponse:
        tmp_req.validate()
        request = main_models.DescribeUdmSnapshotsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.snapshot_ids):
            request.snapshot_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.snapshot_ids, 'SnapshotIds', 'json')
        query = {}
        if not DaraCore.is_null(request.disk_id):
            query['DiskId'] = request.disk_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.job_id):
            query['JobId'] = request.job_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.udm_region_id):
            query['UdmRegionId'] = request.udm_region_id
        body = {}
        if not DaraCore.is_null(request.snapshot_ids_shrink):
            body['SnapshotIds'] = request.snapshot_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUdmSnapshots',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUdmSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_udm_snapshots(
        self,
        request: main_models.DescribeUdmSnapshotsRequest,
    ) -> main_models.DescribeUdmSnapshotsResponse:
        runtime = RuntimeOptions()
        return self.describe_udm_snapshots_with_options(request, runtime)

    async def describe_udm_snapshots_async(
        self,
        request: main_models.DescribeUdmSnapshotsRequest,
    ) -> main_models.DescribeUdmSnapshotsResponse:
        runtime = RuntimeOptions()
        return await self.describe_udm_snapshots_with_options_async(request, runtime)

    def describe_vault_replication_regions_with_options(
        self,
        request: main_models.DescribeVaultReplicationRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVaultReplicationRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVaultReplicationRegions',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVaultReplicationRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vault_replication_regions_with_options_async(
        self,
        request: main_models.DescribeVaultReplicationRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVaultReplicationRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVaultReplicationRegions',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVaultReplicationRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vault_replication_regions(
        self,
        request: main_models.DescribeVaultReplicationRegionsRequest,
    ) -> main_models.DescribeVaultReplicationRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_vault_replication_regions_with_options(request, runtime)

    async def describe_vault_replication_regions_async(
        self,
        request: main_models.DescribeVaultReplicationRegionsRequest,
    ) -> main_models.DescribeVaultReplicationRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_vault_replication_regions_with_options_async(request, runtime)

    def describe_vaults_with_options(
        self,
        request: main_models.DescribeVaultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVaultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.replication):
            query['Replication'] = request.replication
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        if not DaraCore.is_null(request.vault_name):
            query['VaultName'] = request.vault_name
        if not DaraCore.is_null(request.vault_owner_id):
            query['VaultOwnerId'] = request.vault_owner_id
        if not DaraCore.is_null(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not DaraCore.is_null(request.vault_type):
            query['VaultType'] = request.vault_type
        body = {}
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVaults',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVaultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vaults_with_options_async(
        self,
        request: main_models.DescribeVaultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVaultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.replication):
            query['Replication'] = request.replication
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        if not DaraCore.is_null(request.vault_name):
            query['VaultName'] = request.vault_name
        if not DaraCore.is_null(request.vault_owner_id):
            query['VaultOwnerId'] = request.vault_owner_id
        if not DaraCore.is_null(request.vault_region_id):
            query['VaultRegionId'] = request.vault_region_id
        if not DaraCore.is_null(request.vault_type):
            query['VaultType'] = request.vault_type
        body = {}
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVaults',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVaultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vaults(
        self,
        request: main_models.DescribeVaultsRequest,
    ) -> main_models.DescribeVaultsResponse:
        runtime = RuntimeOptions()
        return self.describe_vaults_with_options(request, runtime)

    async def describe_vaults_async(
        self,
        request: main_models.DescribeVaultsRequest,
    ) -> main_models.DescribeVaultsResponse:
        runtime = RuntimeOptions()
        return await self.describe_vaults_with_options_async(request, runtime)

    def detach_nas_file_system_with_options(
        self,
        request: main_models.DetachNasFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachNasFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachNasFileSystem',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachNasFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_nas_file_system_with_options_async(
        self,
        request: main_models.DetachNasFileSystemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachNasFileSystemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachNasFileSystem',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachNasFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_nas_file_system(
        self,
        request: main_models.DetachNasFileSystemRequest,
    ) -> main_models.DetachNasFileSystemResponse:
        runtime = RuntimeOptions()
        return self.detach_nas_file_system_with_options(request, runtime)

    async def detach_nas_file_system_async(
        self,
        request: main_models.DetachNasFileSystemRequest,
    ) -> main_models.DetachNasFileSystemResponse:
        runtime = RuntimeOptions()
        return await self.detach_nas_file_system_with_options_async(request, runtime)

    def disable_backup_plan_with_options(
        self,
        request: main_models.DisableBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_backup_plan_with_options_async(
        self,
        request: main_models.DisableBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_backup_plan(
        self,
        request: main_models.DisableBackupPlanRequest,
    ) -> main_models.DisableBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.disable_backup_plan_with_options(request, runtime)

    async def disable_backup_plan_async(
        self,
        request: main_models.DisableBackupPlanRequest,
    ) -> main_models.DisableBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.disable_backup_plan_with_options_async(request, runtime)

    def disable_hana_backup_plan_with_options(
        self,
        request: main_models.DisableHanaBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableHanaBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableHanaBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_hana_backup_plan_with_options_async(
        self,
        request: main_models.DisableHanaBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableHanaBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableHanaBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableHanaBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_hana_backup_plan(
        self,
        request: main_models.DisableHanaBackupPlanRequest,
    ) -> main_models.DisableHanaBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.disable_hana_backup_plan_with_options(request, runtime)

    async def disable_hana_backup_plan_async(
        self,
        request: main_models.DisableHanaBackupPlanRequest,
    ) -> main_models.DisableHanaBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.disable_hana_backup_plan_with_options_async(request, runtime)

    def enable_backup_plan_with_options(
        self,
        request: main_models.EnableBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_backup_plan_with_options_async(
        self,
        request: main_models.EnableBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_backup_plan(
        self,
        request: main_models.EnableBackupPlanRequest,
    ) -> main_models.EnableBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.enable_backup_plan_with_options(request, runtime)

    async def enable_backup_plan_async(
        self,
        request: main_models.EnableBackupPlanRequest,
    ) -> main_models.EnableBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.enable_backup_plan_with_options_async(request, runtime)

    def enable_hana_backup_plan_with_options(
        self,
        request: main_models.EnableHanaBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableHanaBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHanaBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_hana_backup_plan_with_options_async(
        self,
        request: main_models.EnableHanaBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableHanaBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHanaBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHanaBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_hana_backup_plan(
        self,
        request: main_models.EnableHanaBackupPlanRequest,
    ) -> main_models.EnableHanaBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.enable_hana_backup_plan_with_options(request, runtime)

    async def enable_hana_backup_plan_async(
        self,
        request: main_models.EnableHanaBackupPlanRequest,
    ) -> main_models.EnableHanaBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.enable_hana_backup_plan_with_options_async(request, runtime)

    def execute_backup_plan_with_options(
        self,
        request: main_models.ExecuteBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_backup_plan_with_options_async(
        self,
        request: main_models.ExecuteBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_backup_plan(
        self,
        request: main_models.ExecuteBackupPlanRequest,
    ) -> main_models.ExecuteBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.execute_backup_plan_with_options(request, runtime)

    async def execute_backup_plan_async(
        self,
        request: main_models.ExecuteBackupPlanRequest,
    ) -> main_models.ExecuteBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.execute_backup_plan_with_options_async(request, runtime)

    def execute_policy_v2with_options(
        self,
        request: main_models.ExecutePolicyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.ExecutePolicyV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecutePolicyV2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecutePolicyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def execute_policy_v2with_options_async(
        self,
        request: main_models.ExecutePolicyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.ExecutePolicyV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        body = {}
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecutePolicyV2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecutePolicyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_policy_v2(
        self,
        request: main_models.ExecutePolicyV2Request,
    ) -> main_models.ExecutePolicyV2Response:
        runtime = RuntimeOptions()
        return self.execute_policy_v2with_options(request, runtime)

    async def execute_policy_v2_async(
        self,
        request: main_models.ExecutePolicyV2Request,
    ) -> main_models.ExecutePolicyV2Response:
        runtime = RuntimeOptions()
        return await self.execute_policy_v2with_options_async(request, runtime)

    def generate_ram_policy_with_options(
        self,
        request: main_models.GenerateRamPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateRamPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.require_base_policy):
            query['RequireBasePolicy'] = request.require_base_policy
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateRamPolicy',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateRamPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_ram_policy_with_options_async(
        self,
        request: main_models.GenerateRamPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateRamPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_type):
            query['ActionType'] = request.action_type
        if not DaraCore.is_null(request.require_base_policy):
            query['RequireBasePolicy'] = request.require_base_policy
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateRamPolicy',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateRamPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_ram_policy(
        self,
        request: main_models.GenerateRamPolicyRequest,
    ) -> main_models.GenerateRamPolicyResponse:
        runtime = RuntimeOptions()
        return self.generate_ram_policy_with_options(request, runtime)

    async def generate_ram_policy_async(
        self,
        request: main_models.GenerateRamPolicyRequest,
    ) -> main_models.GenerateRamPolicyResponse:
        runtime = RuntimeOptions()
        return await self.generate_ram_policy_with_options_async(request, runtime)

    def get_temp_file_download_link_with_options(
        self,
        request: main_models.GetTempFileDownloadLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTempFileDownloadLinkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.temp_file_key):
            query['TempFileKey'] = request.temp_file_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTempFileDownloadLink',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTempFileDownloadLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_temp_file_download_link_with_options_async(
        self,
        request: main_models.GetTempFileDownloadLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTempFileDownloadLinkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.temp_file_key):
            query['TempFileKey'] = request.temp_file_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTempFileDownloadLink',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTempFileDownloadLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_temp_file_download_link(
        self,
        request: main_models.GetTempFileDownloadLinkRequest,
    ) -> main_models.GetTempFileDownloadLinkResponse:
        runtime = RuntimeOptions()
        return self.get_temp_file_download_link_with_options(request, runtime)

    async def get_temp_file_download_link_async(
        self,
        request: main_models.GetTempFileDownloadLinkRequest,
    ) -> main_models.GetTempFileDownloadLinkResponse:
        runtime = RuntimeOptions()
        return await self.get_temp_file_download_link_with_options_async(request, runtime)

    def install_backup_clients_with_options(
        self,
        tmp_req: main_models.InstallBackupClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallBackupClientsResponse:
        tmp_req.validate()
        request = main_models.InstallBackupClientsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallBackupClients',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_backup_clients_with_options_async(
        self,
        tmp_req: main_models.InstallBackupClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallBackupClientsResponse:
        tmp_req.validate()
        request = main_models.InstallBackupClientsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallBackupClients',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallBackupClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_backup_clients(
        self,
        request: main_models.InstallBackupClientsRequest,
    ) -> main_models.InstallBackupClientsResponse:
        runtime = RuntimeOptions()
        return self.install_backup_clients_with_options(request, runtime)

    async def install_backup_clients_async(
        self,
        request: main_models.InstallBackupClientsRequest,
    ) -> main_models.InstallBackupClientsResponse:
        runtime = RuntimeOptions()
        return await self.install_backup_clients_with_options_async(request, runtime)

    def list_protected_resources_with_options(
        self,
        request: main_models.ListProtectedResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProtectedResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.created_by_product):
            query['CreatedByProduct'] = request.created_by_product
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProtectedResources',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProtectedResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_protected_resources_with_options_async(
        self,
        request: main_models.ListProtectedResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProtectedResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.created_by_product):
            query['CreatedByProduct'] = request.created_by_product
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.skip):
            query['Skip'] = request.skip
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProtectedResources',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProtectedResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_protected_resources(
        self,
        request: main_models.ListProtectedResourcesRequest,
    ) -> main_models.ListProtectedResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_protected_resources_with_options(request, runtime)

    async def list_protected_resources_async(
        self,
        request: main_models.ListProtectedResourcesRequest,
    ) -> main_models.ListProtectedResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_protected_resources_with_options_async(request, runtime)

    def open_hbr_service_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OpenHbrServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OpenHbrService',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenHbrServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_hbr_service_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.OpenHbrServiceResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'OpenHbrService',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenHbrServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_hbr_service(self) -> main_models.OpenHbrServiceResponse:
        runtime = RuntimeOptions()
        return self.open_hbr_service_with_options(runtime)

    async def open_hbr_service_async(self) -> main_models.OpenHbrServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_hbr_service_with_options_async(runtime)

    def search_historical_snapshots_with_options(
        self,
        tmp_req: main_models.SearchHistoricalSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchHistoricalSnapshotsResponse:
        tmp_req.validate()
        request = main_models.SearchHistoricalSnapshotsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.query_shrink):
            query['Query'] = request.query_shrink
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchHistoricalSnapshots',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchHistoricalSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_historical_snapshots_with_options_async(
        self,
        tmp_req: main_models.SearchHistoricalSnapshotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchHistoricalSnapshotsResponse:
        tmp_req.validate()
        request = main_models.SearchHistoricalSnapshotsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.query_shrink):
            query['Query'] = request.query_shrink
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchHistoricalSnapshots',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchHistoricalSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_historical_snapshots(
        self,
        request: main_models.SearchHistoricalSnapshotsRequest,
    ) -> main_models.SearchHistoricalSnapshotsResponse:
        runtime = RuntimeOptions()
        return self.search_historical_snapshots_with_options(request, runtime)

    async def search_historical_snapshots_async(
        self,
        request: main_models.SearchHistoricalSnapshotsRequest,
    ) -> main_models.SearchHistoricalSnapshotsResponse:
        runtime = RuntimeOptions()
        return await self.search_historical_snapshots_with_options_async(request, runtime)

    def start_hana_database_async_with_options(
        self,
        request: main_models.StartHanaDatabaseAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartHanaDatabaseAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartHanaDatabaseAsync',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartHanaDatabaseAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_hana_database_async_with_options_async(
        self,
        request: main_models.StartHanaDatabaseAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartHanaDatabaseAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartHanaDatabaseAsync',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartHanaDatabaseAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_hana_database_async(
        self,
        request: main_models.StartHanaDatabaseAsyncRequest,
    ) -> main_models.StartHanaDatabaseAsyncResponse:
        runtime = RuntimeOptions()
        return self.start_hana_database_async_with_options(request, runtime)

    async def start_hana_database_async_async(
        self,
        request: main_models.StartHanaDatabaseAsyncRequest,
    ) -> main_models.StartHanaDatabaseAsyncResponse:
        runtime = RuntimeOptions()
        return await self.start_hana_database_async_with_options_async(request, runtime)

    def stop_hana_database_async_with_options(
        self,
        request: main_models.StopHanaDatabaseAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopHanaDatabaseAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopHanaDatabaseAsync',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopHanaDatabaseAsyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_hana_database_async_with_options_async(
        self,
        request: main_models.StopHanaDatabaseAsyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopHanaDatabaseAsyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopHanaDatabaseAsync',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopHanaDatabaseAsyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_hana_database_async(
        self,
        request: main_models.StopHanaDatabaseAsyncRequest,
    ) -> main_models.StopHanaDatabaseAsyncResponse:
        runtime = RuntimeOptions()
        return self.stop_hana_database_async_with_options(request, runtime)

    async def stop_hana_database_async_async(
        self,
        request: main_models.StopHanaDatabaseAsyncRequest,
    ) -> main_models.StopHanaDatabaseAsyncResponse:
        runtime = RuntimeOptions()
        return await self.stop_hana_database_async_with_options_async(request, runtime)

    def uninstall_backup_clients_with_options(
        self,
        tmp_req: main_models.UninstallBackupClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallBackupClientsResponse:
        tmp_req.validate()
        request = main_models.UninstallBackupClientsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_ids):
            request.client_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallBackupClients',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_backup_clients_with_options_async(
        self,
        tmp_req: main_models.UninstallBackupClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallBackupClientsResponse:
        tmp_req.validate()
        request = main_models.UninstallBackupClientsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_ids):
            request.client_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallBackupClients',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallBackupClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_backup_clients(
        self,
        request: main_models.UninstallBackupClientsRequest,
    ) -> main_models.UninstallBackupClientsResponse:
        runtime = RuntimeOptions()
        return self.uninstall_backup_clients_with_options(request, runtime)

    async def uninstall_backup_clients_async(
        self,
        request: main_models.UninstallBackupClientsRequest,
    ) -> main_models.UninstallBackupClientsResponse:
        runtime = RuntimeOptions()
        return await self.uninstall_backup_clients_with_options_async(request, runtime)

    def uninstall_client_with_options(
        self,
        request: main_models.UninstallClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallClient',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_client_with_options_async(
        self,
        request: main_models.UninstallClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallClient',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_client(
        self,
        request: main_models.UninstallClientRequest,
    ) -> main_models.UninstallClientResponse:
        runtime = RuntimeOptions()
        return self.uninstall_client_with_options(request, runtime)

    async def uninstall_client_async(
        self,
        request: main_models.UninstallClientRequest,
    ) -> main_models.UninstallClientResponse:
        runtime = RuntimeOptions()
        return await self.uninstall_client_with_options_async(request, runtime)

    def update_backup_plan_with_options(
        self,
        tmp_req: main_models.UpdateBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBackupPlanResponse:
        tmp_req.validate()
        request = main_models.UpdateBackupPlanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.detail):
            request.detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        if not DaraCore.is_null(tmp_req.ots_detail):
            request.ots_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        query = {}
        if not DaraCore.is_null(request.change_list_path):
            query['ChangeListPath'] = request.change_list_path
        if not DaraCore.is_null(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.keep_latest_snapshots):
            query['KeepLatestSnapshots'] = request.keep_latest_snapshots
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.plan_name):
            query['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.prefix):
            query['Prefix'] = request.prefix
        if not DaraCore.is_null(request.retention):
            query['Retention'] = request.retention
        if not DaraCore.is_null(request.schedule):
            query['Schedule'] = request.schedule
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        if not DaraCore.is_null(request.update_paths):
            query['UpdatePaths'] = request.update_paths
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not DaraCore.is_null(request.exclude):
            body['Exclude'] = request.exclude
        if not DaraCore.is_null(request.include):
            body['Include'] = request.include
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not DaraCore.is_null(request.rule):
            body['Rule'] = request.rule
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_backup_plan_with_options_async(
        self,
        tmp_req: main_models.UpdateBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBackupPlanResponse:
        tmp_req.validate()
        request = main_models.UpdateBackupPlanShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.detail):
            request.detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.detail, 'Detail', 'json')
        if not DaraCore.is_null(tmp_req.ots_detail):
            request.ots_detail_shrink = Utils.array_to_string_with_specified_style(tmp_req.ots_detail, 'OtsDetail', 'json')
        query = {}
        if not DaraCore.is_null(request.change_list_path):
            query['ChangeListPath'] = request.change_list_path
        if not DaraCore.is_null(request.detail_shrink):
            query['Detail'] = request.detail_shrink
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.keep_latest_snapshots):
            query['KeepLatestSnapshots'] = request.keep_latest_snapshots
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.plan_name):
            query['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.prefix):
            query['Prefix'] = request.prefix
        if not DaraCore.is_null(request.retention):
            query['Retention'] = request.retention
        if not DaraCore.is_null(request.schedule):
            query['Schedule'] = request.schedule
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        if not DaraCore.is_null(request.update_paths):
            query['UpdatePaths'] = request.update_paths
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        body = {}
        if not DaraCore.is_null(request.exclude):
            body['Exclude'] = request.exclude
        if not DaraCore.is_null(request.include):
            body['Include'] = request.include
        if not DaraCore.is_null(request.options):
            body['Options'] = request.options
        if not DaraCore.is_null(request.ots_detail_shrink):
            body['OtsDetail'] = request.ots_detail_shrink
        if not DaraCore.is_null(request.rule):
            body['Rule'] = request.rule
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_backup_plan(
        self,
        request: main_models.UpdateBackupPlanRequest,
    ) -> main_models.UpdateBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.update_backup_plan_with_options(request, runtime)

    async def update_backup_plan_async(
        self,
        request: main_models.UpdateBackupPlanRequest,
    ) -> main_models.UpdateBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.update_backup_plan_with_options_async(request, runtime)

    def update_client_settings_with_options(
        self,
        request: main_models.UpdateClientSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClientSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_on_partial_complete):
            query['AlertOnPartialComplete'] = request.alert_on_partial_complete
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.data_network_type):
            query['DataNetworkType'] = request.data_network_type
        if not DaraCore.is_null(request.data_proxy_setting):
            query['DataProxySetting'] = request.data_proxy_setting
        if not DaraCore.is_null(request.max_cpu_core):
            query['MaxCpuCore'] = request.max_cpu_core
        if not DaraCore.is_null(request.max_memory):
            query['MaxMemory'] = request.max_memory
        if not DaraCore.is_null(request.max_worker):
            query['MaxWorker'] = request.max_worker
        if not DaraCore.is_null(request.proxy_host):
            query['ProxyHost'] = request.proxy_host
        if not DaraCore.is_null(request.proxy_password):
            query['ProxyPassword'] = request.proxy_password
        if not DaraCore.is_null(request.proxy_port):
            query['ProxyPort'] = request.proxy_port
        if not DaraCore.is_null(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.use_https):
            query['UseHttps'] = request.use_https
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClientSettings',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClientSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_client_settings_with_options_async(
        self,
        request: main_models.UpdateClientSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClientSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_on_partial_complete):
            query['AlertOnPartialComplete'] = request.alert_on_partial_complete
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.data_network_type):
            query['DataNetworkType'] = request.data_network_type
        if not DaraCore.is_null(request.data_proxy_setting):
            query['DataProxySetting'] = request.data_proxy_setting
        if not DaraCore.is_null(request.max_cpu_core):
            query['MaxCpuCore'] = request.max_cpu_core
        if not DaraCore.is_null(request.max_memory):
            query['MaxMemory'] = request.max_memory
        if not DaraCore.is_null(request.max_worker):
            query['MaxWorker'] = request.max_worker
        if not DaraCore.is_null(request.proxy_host):
            query['ProxyHost'] = request.proxy_host
        if not DaraCore.is_null(request.proxy_password):
            query['ProxyPassword'] = request.proxy_password
        if not DaraCore.is_null(request.proxy_port):
            query['ProxyPort'] = request.proxy_port
        if not DaraCore.is_null(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.use_https):
            query['UseHttps'] = request.use_https
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClientSettings',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClientSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_client_settings(
        self,
        request: main_models.UpdateClientSettingsRequest,
    ) -> main_models.UpdateClientSettingsResponse:
        runtime = RuntimeOptions()
        return self.update_client_settings_with_options(request, runtime)

    async def update_client_settings_async(
        self,
        request: main_models.UpdateClientSettingsRequest,
    ) -> main_models.UpdateClientSettingsResponse:
        runtime = RuntimeOptions()
        return await self.update_client_settings_with_options_async(request, runtime)

    def update_container_cluster_with_options(
        self,
        request: main_models.UpdateContainerClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContainerClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.renew_token):
            query['RenewToken'] = request.renew_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContainerCluster',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContainerClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_container_cluster_with_options_async(
        self,
        request: main_models.UpdateContainerClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateContainerClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.network_type):
            query['NetworkType'] = request.network_type
        if not DaraCore.is_null(request.renew_token):
            query['RenewToken'] = request.renew_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateContainerCluster',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateContainerClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_container_cluster(
        self,
        request: main_models.UpdateContainerClusterRequest,
    ) -> main_models.UpdateContainerClusterResponse:
        runtime = RuntimeOptions()
        return self.update_container_cluster_with_options(request, runtime)

    async def update_container_cluster_async(
        self,
        request: main_models.UpdateContainerClusterRequest,
    ) -> main_models.UpdateContainerClusterResponse:
        runtime = RuntimeOptions()
        return await self.update_container_cluster_with_options_async(request, runtime)

    def update_hana_backup_plan_with_options(
        self,
        request: main_models.UpdateHanaBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHanaBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.plan_name):
            query['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.schedule):
            query['Schedule'] = request.schedule
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHanaBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHanaBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hana_backup_plan_with_options_async(
        self,
        request: main_models.UpdateHanaBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHanaBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_prefix):
            query['BackupPrefix'] = request.backup_prefix
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.plan_id):
            query['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.plan_name):
            query['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.schedule):
            query['Schedule'] = request.schedule
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHanaBackupPlan',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHanaBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hana_backup_plan(
        self,
        request: main_models.UpdateHanaBackupPlanRequest,
    ) -> main_models.UpdateHanaBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.update_hana_backup_plan_with_options(request, runtime)

    async def update_hana_backup_plan_async(
        self,
        request: main_models.UpdateHanaBackupPlanRequest,
    ) -> main_models.UpdateHanaBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.update_hana_backup_plan_with_options_async(request, runtime)

    def update_hana_backup_setting_with_options(
        self,
        request: main_models.UpdateHanaBackupSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHanaBackupSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_backup_parameter_file):
            query['CatalogBackupParameterFile'] = request.catalog_backup_parameter_file
        if not DaraCore.is_null(request.catalog_backup_using_backint):
            query['CatalogBackupUsingBackint'] = request.catalog_backup_using_backint
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data_backup_parameter_file):
            query['DataBackupParameterFile'] = request.data_backup_parameter_file
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.enable_auto_log_backup):
            query['EnableAutoLogBackup'] = request.enable_auto_log_backup
        if not DaraCore.is_null(request.log_backup_parameter_file):
            query['LogBackupParameterFile'] = request.log_backup_parameter_file
        if not DaraCore.is_null(request.log_backup_timeout):
            query['LogBackupTimeout'] = request.log_backup_timeout
        if not DaraCore.is_null(request.log_backup_using_backint):
            query['LogBackupUsingBackint'] = request.log_backup_using_backint
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHanaBackupSetting',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHanaBackupSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hana_backup_setting_with_options_async(
        self,
        request: main_models.UpdateHanaBackupSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHanaBackupSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_backup_parameter_file):
            query['CatalogBackupParameterFile'] = request.catalog_backup_parameter_file
        if not DaraCore.is_null(request.catalog_backup_using_backint):
            query['CatalogBackupUsingBackint'] = request.catalog_backup_using_backint
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data_backup_parameter_file):
            query['DataBackupParameterFile'] = request.data_backup_parameter_file
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.enable_auto_log_backup):
            query['EnableAutoLogBackup'] = request.enable_auto_log_backup
        if not DaraCore.is_null(request.log_backup_parameter_file):
            query['LogBackupParameterFile'] = request.log_backup_parameter_file
        if not DaraCore.is_null(request.log_backup_timeout):
            query['LogBackupTimeout'] = request.log_backup_timeout
        if not DaraCore.is_null(request.log_backup_using_backint):
            query['LogBackupUsingBackint'] = request.log_backup_using_backint
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHanaBackupSetting',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHanaBackupSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hana_backup_setting(
        self,
        request: main_models.UpdateHanaBackupSettingRequest,
    ) -> main_models.UpdateHanaBackupSettingResponse:
        runtime = RuntimeOptions()
        return self.update_hana_backup_setting_with_options(request, runtime)

    async def update_hana_backup_setting_async(
        self,
        request: main_models.UpdateHanaBackupSettingRequest,
    ) -> main_models.UpdateHanaBackupSettingResponse:
        runtime = RuntimeOptions()
        return await self.update_hana_backup_setting_with_options_async(request, runtime)

    def update_hana_instance_with_options(
        self,
        request: main_models.UpdateHanaInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHanaInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.hana_name):
            query['HanaName'] = request.hana_name
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.instance_number):
            query['InstanceNumber'] = request.instance_number
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.use_ssl):
            query['UseSsl'] = request.use_ssl
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.validate_certificate):
            query['ValidateCertificate'] = request.validate_certificate
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHanaInstance',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHanaInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hana_instance_with_options_async(
        self,
        request: main_models.UpdateHanaInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHanaInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_setting):
            query['AlertSetting'] = request.alert_setting
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.hana_name):
            query['HanaName'] = request.hana_name
        if not DaraCore.is_null(request.host):
            query['Host'] = request.host
        if not DaraCore.is_null(request.instance_number):
            query['InstanceNumber'] = request.instance_number
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.use_ssl):
            query['UseSsl'] = request.use_ssl
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.validate_certificate):
            query['ValidateCertificate'] = request.validate_certificate
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHanaInstance',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHanaInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hana_instance(
        self,
        request: main_models.UpdateHanaInstanceRequest,
    ) -> main_models.UpdateHanaInstanceResponse:
        runtime = RuntimeOptions()
        return self.update_hana_instance_with_options(request, runtime)

    async def update_hana_instance_async(
        self,
        request: main_models.UpdateHanaInstanceRequest,
    ) -> main_models.UpdateHanaInstanceResponse:
        runtime = RuntimeOptions()
        return await self.update_hana_instance_with_options_async(request, runtime)

    def update_hana_retention_setting_with_options(
        self,
        request: main_models.UpdateHanaRetentionSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHanaRetentionSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not DaraCore.is_null(request.schedule):
            query['Schedule'] = request.schedule
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHanaRetentionSetting',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHanaRetentionSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hana_retention_setting_with_options_async(
        self,
        request: main_models.UpdateHanaRetentionSettingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateHanaRetentionSettingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not DaraCore.is_null(request.schedule):
            query['Schedule'] = request.schedule
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateHanaRetentionSetting',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateHanaRetentionSettingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hana_retention_setting(
        self,
        request: main_models.UpdateHanaRetentionSettingRequest,
    ) -> main_models.UpdateHanaRetentionSettingResponse:
        runtime = RuntimeOptions()
        return self.update_hana_retention_setting_with_options(request, runtime)

    async def update_hana_retention_setting_async(
        self,
        request: main_models.UpdateHanaRetentionSettingRequest,
    ) -> main_models.UpdateHanaRetentionSettingResponse:
        runtime = RuntimeOptions()
        return await self.update_hana_retention_setting_with_options_async(request, runtime)

    def update_policy_binding_with_options(
        self,
        tmp_req: main_models.UpdatePolicyBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyBindingResponse:
        tmp_req.validate()
        request = main_models.UpdatePolicyBindingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.advanced_options):
            request.advanced_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.advanced_options, 'AdvancedOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.advanced_options_shrink):
            query['AdvancedOptions'] = request.advanced_options_shrink
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.exclude):
            query['Exclude'] = request.exclude
        if not DaraCore.is_null(request.include):
            query['Include'] = request.include
        if not DaraCore.is_null(request.policy_binding_description):
            query['PolicyBindingDescription'] = request.policy_binding_description
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        body = {}
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicyBinding',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolicyBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_policy_binding_with_options_async(
        self,
        tmp_req: main_models.UpdatePolicyBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyBindingResponse:
        tmp_req.validate()
        request = main_models.UpdatePolicyBindingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.advanced_options):
            request.advanced_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.advanced_options, 'AdvancedOptions', 'json')
        query = {}
        if not DaraCore.is_null(request.advanced_options_shrink):
            query['AdvancedOptions'] = request.advanced_options_shrink
        if not DaraCore.is_null(request.disabled):
            query['Disabled'] = request.disabled
        if not DaraCore.is_null(request.exclude):
            query['Exclude'] = request.exclude
        if not DaraCore.is_null(request.include):
            query['Include'] = request.include
        if not DaraCore.is_null(request.policy_binding_description):
            query['PolicyBindingDescription'] = request.policy_binding_description
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.speed_limit):
            query['SpeedLimit'] = request.speed_limit
        body = {}
        if not DaraCore.is_null(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicyBinding',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolicyBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_policy_binding(
        self,
        request: main_models.UpdatePolicyBindingRequest,
    ) -> main_models.UpdatePolicyBindingResponse:
        runtime = RuntimeOptions()
        return self.update_policy_binding_with_options(request, runtime)

    async def update_policy_binding_async(
        self,
        request: main_models.UpdatePolicyBindingRequest,
    ) -> main_models.UpdatePolicyBindingResponse:
        runtime = RuntimeOptions()
        return await self.update_policy_binding_with_options_async(request, runtime)

    def update_policy_v2with_options(
        self,
        tmp_req: main_models.UpdatePolicyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyV2Response:
        tmp_req.validate()
        request = main_models.UpdatePolicyV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not DaraCore.is_null(request.policy_description):
            body['PolicyDescription'] = request.policy_description
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicyV2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolicyV2Response(),
            self.call_api(params, req, runtime)
        )

    async def update_policy_v2with_options_async(
        self,
        tmp_req: main_models.UpdatePolicyV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePolicyV2Response:
        tmp_req.validate()
        request = main_models.UpdatePolicyV2ShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.rules):
            request.rules_shrink = Utils.array_to_string_with_specified_style(tmp_req.rules, 'Rules', 'json')
        body = {}
        if not DaraCore.is_null(request.policy_description):
            body['PolicyDescription'] = request.policy_description
        if not DaraCore.is_null(request.policy_id):
            body['PolicyId'] = request.policy_id
        if not DaraCore.is_null(request.policy_name):
            body['PolicyName'] = request.policy_name
        if not DaraCore.is_null(request.rules_shrink):
            body['Rules'] = request.rules_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePolicyV2',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePolicyV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def update_policy_v2(
        self,
        request: main_models.UpdatePolicyV2Request,
    ) -> main_models.UpdatePolicyV2Response:
        runtime = RuntimeOptions()
        return self.update_policy_v2with_options(request, runtime)

    async def update_policy_v2_async(
        self,
        request: main_models.UpdatePolicyV2Request,
    ) -> main_models.UpdatePolicyV2Response:
        runtime = RuntimeOptions()
        return await self.update_policy_v2with_options_async(request, runtime)

    def update_vault_with_options(
        self,
        request: main_models.UpdateVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVaultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        if not DaraCore.is_null(request.vault_name):
            query['VaultName'] = request.vault_name
        if not DaraCore.is_null(request.worm_enabled):
            query['WormEnabled'] = request.worm_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVault',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVaultResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_vault_with_options_async(
        self,
        request: main_models.UpdateVaultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateVaultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        if not DaraCore.is_null(request.vault_name):
            query['VaultName'] = request.vault_name
        if not DaraCore.is_null(request.worm_enabled):
            query['WormEnabled'] = request.worm_enabled
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateVault',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateVaultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_vault(
        self,
        request: main_models.UpdateVaultRequest,
    ) -> main_models.UpdateVaultResponse:
        runtime = RuntimeOptions()
        return self.update_vault_with_options(request, runtime)

    async def update_vault_async(
        self,
        request: main_models.UpdateVaultRequest,
    ) -> main_models.UpdateVaultResponse:
        runtime = RuntimeOptions()
        return await self.update_vault_with_options_async(request, runtime)

    def upgrade_backup_clients_with_options(
        self,
        tmp_req: main_models.UpgradeBackupClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeBackupClientsResponse:
        tmp_req.validate()
        request = main_models.UpgradeBackupClientsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_ids):
            request.client_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeBackupClients',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeBackupClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_backup_clients_with_options_async(
        self,
        tmp_req: main_models.UpgradeBackupClientsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeBackupClientsResponse:
        tmp_req.validate()
        request = main_models.UpgradeBackupClientsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.client_ids):
            request.client_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.client_ids, 'ClientIds', 'json')
        if not DaraCore.is_null(tmp_req.instance_ids):
            request.instance_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.client_ids_shrink):
            query['ClientIds'] = request.client_ids_shrink
        if not DaraCore.is_null(request.cross_account_role_name):
            query['CrossAccountRoleName'] = request.cross_account_role_name
        if not DaraCore.is_null(request.cross_account_type):
            query['CrossAccountType'] = request.cross_account_type
        if not DaraCore.is_null(request.cross_account_user_id):
            query['CrossAccountUserId'] = request.cross_account_user_id
        if not DaraCore.is_null(request.instance_ids_shrink):
            query['InstanceIds'] = request.instance_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeBackupClients',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeBackupClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_backup_clients(
        self,
        request: main_models.UpgradeBackupClientsRequest,
    ) -> main_models.UpgradeBackupClientsResponse:
        runtime = RuntimeOptions()
        return self.upgrade_backup_clients_with_options(request, runtime)

    async def upgrade_backup_clients_async(
        self,
        request: main_models.UpgradeBackupClientsRequest,
    ) -> main_models.UpgradeBackupClientsResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_backup_clients_with_options_async(request, runtime)

    def upgrade_client_with_options(
        self,
        request: main_models.UpgradeClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeClient',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeClientResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_client_with_options_async(
        self,
        request: main_models.UpgradeClientRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeClientResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_id):
            query['ClientId'] = request.client_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vault_id):
            query['VaultId'] = request.vault_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeClient',
            version = '2017-09-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeClientResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_client(
        self,
        request: main_models.UpgradeClientRequest,
    ) -> main_models.UpgradeClientResponse:
        runtime = RuntimeOptions()
        return self.upgrade_client_with_options(request, runtime)

    async def upgrade_client_async(
        self,
        request: main_models.UpgradeClientRequest,
    ) -> main_models.UpgradeClientResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_client_with_options_async(request, runtime)
