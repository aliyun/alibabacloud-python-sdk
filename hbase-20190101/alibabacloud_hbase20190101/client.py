# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_hbase20190101 import models as main_models
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
            'ap-northeast-2-pop': 'hbase.aliyuncs.com',
            'ap-south-1': 'hbase.aliyuncs.com',
            'ap-southeast-2': 'hbase.aliyuncs.com',
            'cn-beijing-finance-1': 'hbase.aliyuncs.com',
            'cn-beijing-finance-pop': 'hbase.aliyuncs.com',
            'cn-beijing-gov-1': 'hbase.aliyuncs.com',
            'cn-beijing-nu16-b01': 'hbase.aliyuncs.com',
            'cn-edge-1': 'hbase.aliyuncs.com',
            'cn-fujian': 'hbase.aliyuncs.com',
            'cn-haidian-cm12-c01': 'hbase.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'hbase.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'hbase.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'hbase.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'hbase.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'hbase.aliyuncs.com',
            'cn-hangzhou-test-306': 'hbase.aliyuncs.com',
            'cn-hongkong-finance-pop': 'hbase.aliyuncs.com',
            'cn-qingdao-nebula': 'hbase.aliyuncs.com',
            'cn-shanghai-et15-b01': 'hbase.aliyuncs.com',
            'cn-shanghai-et2-b01': 'hbase.aliyuncs.com',
            'cn-shanghai-inner': 'hbase.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'hbase.aliyuncs.com',
            'cn-shenzhen-inner': 'hbase.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'hbase.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'hbase.aliyuncs.com',
            'cn-wuhan': 'hbase.aliyuncs.com',
            'cn-wulanchabu': 'hbase.aliyuncs.com',
            'cn-yushanfang': 'hbase.aliyuncs.com',
            'cn-zhangbei': 'hbase.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'hbase.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'hbase.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'hbase.aliyuncs.com',
            'eu-west-1-oxs': 'hbase.aliyuncs.com',
            'rus-west-1-pop': 'hbase.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('hbase', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_user_hdfs_info_with_options(
        self,
        request: main_models.AddUserHdfsInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserHdfsInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ext_info):
            query['ExtInfo'] = request.ext_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserHdfsInfo',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserHdfsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_user_hdfs_info_with_options_async(
        self,
        request: main_models.AddUserHdfsInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddUserHdfsInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ext_info):
            query['ExtInfo'] = request.ext_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddUserHdfsInfo',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddUserHdfsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_user_hdfs_info(
        self,
        request: main_models.AddUserHdfsInfoRequest,
    ) -> main_models.AddUserHdfsInfoResponse:
        runtime = RuntimeOptions()
        return self.add_user_hdfs_info_with_options(request, runtime)

    async def add_user_hdfs_info_async(
        self,
        request: main_models.AddUserHdfsInfoRequest,
    ) -> main_models.AddUserHdfsInfoResponse:
        runtime = RuntimeOptions()
        return await self.add_user_hdfs_info_with_options_async(request, runtime)

    def allocate_public_network_address_with_options(
        self,
        request: main_models.AllocatePublicNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AllocatePublicNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocatePublicNetworkAddress',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AllocatePublicNetworkAddress',
            version = '2019-01-01',
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
            version = '2019-01-01',
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
            version = '2019-01-01',
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

    def check_components_version_with_options(
        self,
        request: main_models.CheckComponentsVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckComponentsVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.components):
            query['Components'] = request.components
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckComponentsVersion',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckComponentsVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_components_version_with_options_async(
        self,
        request: main_models.CheckComponentsVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckComponentsVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.components):
            query['Components'] = request.components
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckComponentsVersion',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckComponentsVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_components_version(
        self,
        request: main_models.CheckComponentsVersionRequest,
    ) -> main_models.CheckComponentsVersionResponse:
        runtime = RuntimeOptions()
        return self.check_components_version_with_options(request, runtime)

    async def check_components_version_async(
        self,
        request: main_models.CheckComponentsVersionRequest,
    ) -> main_models.CheckComponentsVersionResponse:
        runtime = RuntimeOptions()
        return await self.check_components_version_with_options_async(request, runtime)

    def close_backup_with_options(
        self,
        request: main_models.CloseBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseBackup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_backup_with_options_async(
        self,
        request: main_models.CloseBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseBackup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_backup(
        self,
        request: main_models.CloseBackupRequest,
    ) -> main_models.CloseBackupResponse:
        runtime = RuntimeOptions()
        return self.close_backup_with_options(request, runtime)

    async def close_backup_async(
        self,
        request: main_models.CloseBackupRequest,
    ) -> main_models.CloseBackupResponse:
        runtime = RuntimeOptions()
        return await self.close_backup_with_options_async(request, runtime)

    def convert_instance_with_options(
        self,
        request: main_models.ConvertInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConvertInstance',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_instance_with_options_async(
        self,
        request: main_models.ConvertInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConvertInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConvertInstance',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConvertInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_instance(
        self,
        request: main_models.ConvertInstanceRequest,
    ) -> main_models.ConvertInstanceResponse:
        runtime = RuntimeOptions()
        return self.convert_instance_with_options(request, runtime)

    async def convert_instance_async(
        self,
        request: main_models.ConvertInstanceRequest,
    ) -> main_models.ConvertInstanceResponse:
        runtime = RuntimeOptions()
        return await self.convert_instance_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccount',
            version = '2019-01-01',
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

    def create_backup_plan_with_options(
        self,
        request: main_models.CreateBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackupPlan',
            version = '2019-01-01',
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
        request: main_models.CreateBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackupPlan',
            version = '2019-01-01',
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

    def create_cluster_with_options(
        self,
        request: main_models.CreateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not DaraCore.is_null(request.node_count):
            query['NodeCount'] = request.node_count
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
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
            action = 'CreateCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: main_models.CreateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.encryption_key):
            query['EncryptionKey'] = request.encryption_key
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not DaraCore.is_null(request.node_count):
            query['NodeCount'] = request.node_count
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
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
            action = 'CreateCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: main_models.CreateClusterRequest,
    ) -> main_models.CreateClusterResponse:
        runtime = RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: main_models.CreateClusterRequest,
    ) -> main_models.CreateClusterResponse:
        runtime = RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_global_resource_with_options(
        self,
        request: main_models.CreateGlobalResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGlobalResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGlobalResource',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGlobalResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_global_resource_with_options_async(
        self,
        request: main_models.CreateGlobalResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGlobalResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGlobalResource',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGlobalResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_global_resource(
        self,
        request: main_models.CreateGlobalResourceRequest,
    ) -> main_models.CreateGlobalResourceResponse:
        runtime = RuntimeOptions()
        return self.create_global_resource_with_options(request, runtime)

    async def create_global_resource_async(
        self,
        request: main_models.CreateGlobalResourceRequest,
    ) -> main_models.CreateGlobalResourceResponse:
        runtime = RuntimeOptions()
        return await self.create_global_resource_with_options_async(request, runtime)

    def create_hbase_slb_server_with_options(
        self,
        request: main_models.CreateHBaseSlbServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHBaseSlbServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.slb_server):
            query['SlbServer'] = request.slb_server
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHBaseSlbServer',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHBaseSlbServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hbase_slb_server_with_options_async(
        self,
        request: main_models.CreateHBaseSlbServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHBaseSlbServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.slb_server):
            query['SlbServer'] = request.slb_server
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHBaseSlbServer',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHBaseSlbServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hbase_slb_server(
        self,
        request: main_models.CreateHBaseSlbServerRequest,
    ) -> main_models.CreateHBaseSlbServerResponse:
        runtime = RuntimeOptions()
        return self.create_hbase_slb_server_with_options(request, runtime)

    async def create_hbase_slb_server_async(
        self,
        request: main_models.CreateHBaseSlbServerRequest,
    ) -> main_models.CreateHBaseSlbServerResponse:
        runtime = RuntimeOptions()
        return await self.create_hbase_slb_server_with_options_async(request, runtime)

    def create_hbase_ha_slb_with_options(
        self,
        request: main_models.CreateHbaseHaSlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHbaseHaSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bds_id):
            query['BdsId'] = request.bds_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ha_id):
            query['HaId'] = request.ha_id
        if not DaraCore.is_null(request.ha_types):
            query['HaTypes'] = request.ha_types
        if not DaraCore.is_null(request.hbase_type):
            query['HbaseType'] = request.hbase_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHbaseHaSlb',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHbaseHaSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hbase_ha_slb_with_options_async(
        self,
        request: main_models.CreateHbaseHaSlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHbaseHaSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bds_id):
            query['BdsId'] = request.bds_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.ha_id):
            query['HaId'] = request.ha_id
        if not DaraCore.is_null(request.ha_types):
            query['HaTypes'] = request.ha_types
        if not DaraCore.is_null(request.hbase_type):
            query['HbaseType'] = request.hbase_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHbaseHaSlb',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHbaseHaSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hbase_ha_slb(
        self,
        request: main_models.CreateHbaseHaSlbRequest,
    ) -> main_models.CreateHbaseHaSlbResponse:
        runtime = RuntimeOptions()
        return self.create_hbase_ha_slb_with_options(request, runtime)

    async def create_hbase_ha_slb_async(
        self,
        request: main_models.CreateHbaseHaSlbRequest,
    ) -> main_models.CreateHbaseHaSlbResponse:
        runtime = RuntimeOptions()
        return await self.create_hbase_ha_slb_with_options_async(request, runtime)

    def create_multi_zone_cluster_with_options(
        self,
        request: main_models.CreateMultiZoneClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMultiZoneClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not DaraCore.is_null(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not DaraCore.is_null(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not DaraCore.is_null(request.core_disk_type):
            query['CoreDiskType'] = request.core_disk_type
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.core_node_count):
            query['CoreNodeCount'] = request.core_node_count
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.log_disk_size):
            query['LogDiskSize'] = request.log_disk_size
        if not DaraCore.is_null(request.log_disk_type):
            query['LogDiskType'] = request.log_disk_type
        if not DaraCore.is_null(request.log_instance_type):
            query['LogInstanceType'] = request.log_instance_type
        if not DaraCore.is_null(request.log_node_count):
            query['LogNodeCount'] = request.log_node_count
        if not DaraCore.is_null(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not DaraCore.is_null(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMultiZoneCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMultiZoneClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_multi_zone_cluster_with_options_async(
        self,
        request: main_models.CreateMultiZoneClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMultiZoneClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not DaraCore.is_null(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not DaraCore.is_null(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not DaraCore.is_null(request.core_disk_type):
            query['CoreDiskType'] = request.core_disk_type
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.core_node_count):
            query['CoreNodeCount'] = request.core_node_count
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.log_disk_size):
            query['LogDiskSize'] = request.log_disk_size
        if not DaraCore.is_null(request.log_disk_type):
            query['LogDiskType'] = request.log_disk_type
        if not DaraCore.is_null(request.log_instance_type):
            query['LogInstanceType'] = request.log_instance_type
        if not DaraCore.is_null(request.log_node_count):
            query['LogNodeCount'] = request.log_node_count
        if not DaraCore.is_null(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not DaraCore.is_null(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMultiZoneCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMultiZoneClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_multi_zone_cluster(
        self,
        request: main_models.CreateMultiZoneClusterRequest,
    ) -> main_models.CreateMultiZoneClusterResponse:
        runtime = RuntimeOptions()
        return self.create_multi_zone_cluster_with_options(request, runtime)

    async def create_multi_zone_cluster_async(
        self,
        request: main_models.CreateMultiZoneClusterRequest,
    ) -> main_models.CreateMultiZoneClusterResponse:
        runtime = RuntimeOptions()
        return await self.create_multi_zone_cluster_with_options_async(request, runtime)

    def create_restore_plan_with_options(
        self,
        request: main_models.CreateRestorePlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRestorePlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.restore_all_table):
            query['RestoreAllTable'] = request.restore_all_table
        if not DaraCore.is_null(request.restore_by_copy):
            query['RestoreByCopy'] = request.restore_by_copy
        if not DaraCore.is_null(request.restore_to_date):
            query['RestoreToDate'] = request.restore_to_date
        if not DaraCore.is_null(request.tables):
            query['Tables'] = request.tables
        if not DaraCore.is_null(request.target_cluster_id):
            query['TargetClusterId'] = request.target_cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRestorePlan',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRestorePlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_restore_plan_with_options_async(
        self,
        request: main_models.CreateRestorePlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRestorePlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.restore_all_table):
            query['RestoreAllTable'] = request.restore_all_table
        if not DaraCore.is_null(request.restore_by_copy):
            query['RestoreByCopy'] = request.restore_by_copy
        if not DaraCore.is_null(request.restore_to_date):
            query['RestoreToDate'] = request.restore_to_date
        if not DaraCore.is_null(request.tables):
            query['Tables'] = request.tables
        if not DaraCore.is_null(request.target_cluster_id):
            query['TargetClusterId'] = request.target_cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRestorePlan',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRestorePlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_restore_plan(
        self,
        request: main_models.CreateRestorePlanRequest,
    ) -> main_models.CreateRestorePlanResponse:
        runtime = RuntimeOptions()
        return self.create_restore_plan_with_options(request, runtime)

    async def create_restore_plan_async(
        self,
        request: main_models.CreateRestorePlanRequest,
    ) -> main_models.CreateRestorePlanResponse:
        runtime = RuntimeOptions()
        return await self.create_restore_plan_with_options_async(request, runtime)

    def create_serverless_cluster_with_options(
        self,
        request: main_models.CreateServerlessClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServerlessClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.serverless_capability):
            query['ServerlessCapability'] = request.serverless_capability
        if not DaraCore.is_null(request.serverless_spec):
            query['ServerlessSpec'] = request.serverless_spec
        if not DaraCore.is_null(request.serverless_storage):
            query['ServerlessStorage'] = request.serverless_storage
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
            action = 'CreateServerlessCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServerlessClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_serverless_cluster_with_options_async(
        self,
        request: main_models.CreateServerlessClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServerlessClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.client_type):
            query['ClientType'] = request.client_type
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.serverless_capability):
            query['ServerlessCapability'] = request.serverless_capability
        if not DaraCore.is_null(request.serverless_spec):
            query['ServerlessSpec'] = request.serverless_spec
        if not DaraCore.is_null(request.serverless_storage):
            query['ServerlessStorage'] = request.serverless_storage
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
            action = 'CreateServerlessCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServerlessClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_serverless_cluster(
        self,
        request: main_models.CreateServerlessClusterRequest,
    ) -> main_models.CreateServerlessClusterResponse:
        runtime = RuntimeOptions()
        return self.create_serverless_cluster_with_options(request, runtime)

    async def create_serverless_cluster_async(
        self,
        request: main_models.CreateServerlessClusterRequest,
    ) -> main_models.CreateServerlessClusterResponse:
        runtime = RuntimeOptions()
        return await self.create_serverless_cluster_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: main_models.DeleteAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccount',
            version = '2019-01-01',
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

    def delete_global_resource_with_options(
        self,
        request: main_models.DeleteGlobalResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGlobalResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGlobalResource',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGlobalResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_global_resource_with_options_async(
        self,
        request: main_models.DeleteGlobalResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGlobalResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGlobalResource',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGlobalResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_global_resource(
        self,
        request: main_models.DeleteGlobalResourceRequest,
    ) -> main_models.DeleteGlobalResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_global_resource_with_options(request, runtime)

    async def delete_global_resource_async(
        self,
        request: main_models.DeleteGlobalResourceRequest,
    ) -> main_models.DeleteGlobalResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_global_resource_with_options_async(request, runtime)

    def delete_hbase_ha_dbwith_options(
        self,
        request: main_models.DeleteHBaseHaDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHBaseHaDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bds_id):
            query['BdsId'] = request.bds_id
        if not DaraCore.is_null(request.ha_id):
            query['HaId'] = request.ha_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHBaseHaDB',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHBaseHaDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hbase_ha_dbwith_options_async(
        self,
        request: main_models.DeleteHBaseHaDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHBaseHaDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bds_id):
            query['BdsId'] = request.bds_id
        if not DaraCore.is_null(request.ha_id):
            query['HaId'] = request.ha_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHBaseHaDB',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHBaseHaDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hbase_ha_db(
        self,
        request: main_models.DeleteHBaseHaDBRequest,
    ) -> main_models.DeleteHBaseHaDBResponse:
        runtime = RuntimeOptions()
        return self.delete_hbase_ha_dbwith_options(request, runtime)

    async def delete_hbase_ha_db_async(
        self,
        request: main_models.DeleteHBaseHaDBRequest,
    ) -> main_models.DeleteHBaseHaDBResponse:
        runtime = RuntimeOptions()
        return await self.delete_hbase_ha_dbwith_options_async(request, runtime)

    def delete_hbase_slb_server_with_options(
        self,
        request: main_models.DeleteHBaseSlbServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHBaseSlbServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.slb_server):
            query['SlbServer'] = request.slb_server
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHBaseSlbServer',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHBaseSlbServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hbase_slb_server_with_options_async(
        self,
        request: main_models.DeleteHBaseSlbServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHBaseSlbServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.slb_server):
            query['SlbServer'] = request.slb_server
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHBaseSlbServer',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHBaseSlbServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hbase_slb_server(
        self,
        request: main_models.DeleteHBaseSlbServerRequest,
    ) -> main_models.DeleteHBaseSlbServerResponse:
        runtime = RuntimeOptions()
        return self.delete_hbase_slb_server_with_options(request, runtime)

    async def delete_hbase_slb_server_async(
        self,
        request: main_models.DeleteHBaseSlbServerRequest,
    ) -> main_models.DeleteHBaseSlbServerResponse:
        runtime = RuntimeOptions()
        return await self.delete_hbase_slb_server_with_options_async(request, runtime)

    def delete_hbase_ha_slb_with_options(
        self,
        request: main_models.DeleteHbaseHaSlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHbaseHaSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bds_id):
            query['BdsId'] = request.bds_id
        if not DaraCore.is_null(request.ha_id):
            query['HaId'] = request.ha_id
        if not DaraCore.is_null(request.ha_types):
            query['HaTypes'] = request.ha_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHbaseHaSlb',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHbaseHaSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hbase_ha_slb_with_options_async(
        self,
        request: main_models.DeleteHbaseHaSlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHbaseHaSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bds_id):
            query['BdsId'] = request.bds_id
        if not DaraCore.is_null(request.ha_id):
            query['HaId'] = request.ha_id
        if not DaraCore.is_null(request.ha_types):
            query['HaTypes'] = request.ha_types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHbaseHaSlb',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHbaseHaSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hbase_ha_slb(
        self,
        request: main_models.DeleteHbaseHaSlbRequest,
    ) -> main_models.DeleteHbaseHaSlbResponse:
        runtime = RuntimeOptions()
        return self.delete_hbase_ha_slb_with_options(request, runtime)

    async def delete_hbase_ha_slb_async(
        self,
        request: main_models.DeleteHbaseHaSlbRequest,
    ) -> main_models.DeleteHbaseHaSlbResponse:
        runtime = RuntimeOptions()
        return await self.delete_hbase_ha_slb_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.immediate_delete_flag):
            query['ImmediateDeleteFlag'] = request.immediate_delete_flag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: main_models.DeleteInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.immediate_delete_flag):
            query['ImmediateDeleteFlag'] = request.immediate_delete_flag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstance',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: main_models.DeleteInstanceRequest,
    ) -> main_models.DeleteInstanceResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_multi_zone_cluster_with_options(
        self,
        request: main_models.DeleteMultiZoneClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMultiZoneClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.immediate_delete_flag):
            query['ImmediateDeleteFlag'] = request.immediate_delete_flag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMultiZoneCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMultiZoneClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_multi_zone_cluster_with_options_async(
        self,
        request: main_models.DeleteMultiZoneClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMultiZoneClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.immediate_delete_flag):
            query['ImmediateDeleteFlag'] = request.immediate_delete_flag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMultiZoneCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMultiZoneClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_multi_zone_cluster(
        self,
        request: main_models.DeleteMultiZoneClusterRequest,
    ) -> main_models.DeleteMultiZoneClusterResponse:
        runtime = RuntimeOptions()
        return self.delete_multi_zone_cluster_with_options(request, runtime)

    async def delete_multi_zone_cluster_async(
        self,
        request: main_models.DeleteMultiZoneClusterRequest,
    ) -> main_models.DeleteMultiZoneClusterResponse:
        runtime = RuntimeOptions()
        return await self.delete_multi_zone_cluster_with_options_async(request, runtime)

    def delete_serverless_cluster_with_options(
        self,
        request: main_models.DeleteServerlessClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServerlessClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServerlessCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServerlessClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_serverless_cluster_with_options_async(
        self,
        request: main_models.DeleteServerlessClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServerlessClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServerlessCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServerlessClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_serverless_cluster(
        self,
        request: main_models.DeleteServerlessClusterRequest,
    ) -> main_models.DeleteServerlessClusterResponse:
        runtime = RuntimeOptions()
        return self.delete_serverless_cluster_with_options(request, runtime)

    async def delete_serverless_cluster_async(
        self,
        request: main_models.DeleteServerlessClusterRequest,
    ) -> main_models.DeleteServerlessClusterResponse:
        runtime = RuntimeOptions()
        return await self.delete_serverless_cluster_with_options_async(request, runtime)

    def delete_user_hdfs_info_with_options(
        self,
        request: main_models.DeleteUserHdfsInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserHdfsInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.name_service):
            query['NameService'] = request.name_service
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserHdfsInfo',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserHdfsInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_hdfs_info_with_options_async(
        self,
        request: main_models.DeleteUserHdfsInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUserHdfsInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.name_service):
            query['NameService'] = request.name_service
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUserHdfsInfo',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUserHdfsInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_hdfs_info(
        self,
        request: main_models.DeleteUserHdfsInfoRequest,
    ) -> main_models.DeleteUserHdfsInfoResponse:
        runtime = RuntimeOptions()
        return self.delete_user_hdfs_info_with_options(request, runtime)

    async def delete_user_hdfs_info_async(
        self,
        request: main_models.DeleteUserHdfsInfoRequest,
    ) -> main_models.DeleteUserHdfsInfoResponse:
        runtime = RuntimeOptions()
        return await self.delete_user_hdfs_info_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: main_models.DescribeAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccounts',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAccounts',
            version = '2019-01-01',
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
            action = 'DescribeActiveOperationTaskType',
            version = '2019-01-01',
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
            action = 'DescribeActiveOperationTaskType',
            version = '2019-01-01',
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
            version = '2019-01-01',
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
            version = '2019-01-01',
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

    def describe_available_resource_with_options(
        self,
        request: main_models.DescribeAvailableResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAvailableResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableResource',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAvailableResource',
            version = '2019-01-01',
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

    def describe_backup_plan_config_with_options(
        self,
        request: main_models.DescribeBackupPlanConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPlanConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPlanConfig',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPlanConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_plan_config_with_options_async(
        self,
        request: main_models.DescribeBackupPlanConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPlanConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPlanConfig',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPlanConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_plan_config(
        self,
        request: main_models.DescribeBackupPlanConfigRequest,
    ) -> main_models.DescribeBackupPlanConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_plan_config_with_options(request, runtime)

    async def describe_backup_plan_config_async(
        self,
        request: main_models.DescribeBackupPlanConfigRequest,
    ) -> main_models.DescribeBackupPlanConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_plan_config_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: main_models.DescribeBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPolicy',
            version = '2019-01-01',
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

    def describe_backup_status_with_options(
        self,
        request: main_models.DescribeBackupStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupStatus',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_status_with_options_async(
        self,
        request: main_models.DescribeBackupStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupStatus',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_status(
        self,
        request: main_models.DescribeBackupStatusRequest,
    ) -> main_models.DescribeBackupStatusResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_status_with_options(request, runtime)

    async def describe_backup_status_async(
        self,
        request: main_models.DescribeBackupStatusRequest,
    ) -> main_models.DescribeBackupStatusResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_status_with_options_async(request, runtime)

    def describe_backup_summary_with_options(
        self,
        request: main_models.DescribeBackupSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupSummary',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_summary_with_options_async(
        self,
        request: main_models.DescribeBackupSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupSummary',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_summary(
        self,
        request: main_models.DescribeBackupSummaryRequest,
    ) -> main_models.DescribeBackupSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_summary_with_options(request, runtime)

    async def describe_backup_summary_async(
        self,
        request: main_models.DescribeBackupSummaryRequest,
    ) -> main_models.DescribeBackupSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_summary_with_options_async(request, runtime)

    def describe_backup_tables_with_options(
        self,
        request: main_models.DescribeBackupTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_record_id):
            query['BackupRecordId'] = request.backup_record_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupTables',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_tables_with_options_async(
        self,
        request: main_models.DescribeBackupTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_record_id):
            query['BackupRecordId'] = request.backup_record_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupTables',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_tables(
        self,
        request: main_models.DescribeBackupTablesRequest,
    ) -> main_models.DescribeBackupTablesResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_tables_with_options(request, runtime)

    async def describe_backup_tables_async(
        self,
        request: main_models.DescribeBackupTablesRequest,
    ) -> main_models.DescribeBackupTablesResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_tables_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: main_models.DescribeBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.end_time_utc):
            query['EndTimeUTC'] = request.end_time_utc
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.start_time_utc):
            query['StartTimeUTC'] = request.start_time_utc
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackups',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.end_time_utc):
            query['EndTimeUTC'] = request.end_time_utc
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.start_time_utc):
            query['StartTimeUTC'] = request.start_time_utc
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackups',
            version = '2019-01-01',
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

    def describe_cluster_connection_with_options(
        self,
        request: main_models.DescribeClusterConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterConnection',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_connection_with_options_async(
        self,
        request: main_models.DescribeClusterConnectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterConnectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeClusterConnection',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_connection(
        self,
        request: main_models.DescribeClusterConnectionRequest,
    ) -> main_models.DescribeClusterConnectionResponse:
        runtime = RuntimeOptions()
        return self.describe_cluster_connection_with_options(request, runtime)

    async def describe_cluster_connection_async(
        self,
        request: main_models.DescribeClusterConnectionRequest,
    ) -> main_models.DescribeClusterConnectionResponse:
        runtime = RuntimeOptions()
        return await self.describe_cluster_connection_with_options_async(request, runtime)

    def describe_cold_storage_with_options(
        self,
        request: main_models.DescribeColdStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColdStorageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColdStorage',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColdStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cold_storage_with_options_async(
        self,
        request: main_models.DescribeColdStorageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeColdStorageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeColdStorage',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeColdStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cold_storage(
        self,
        request: main_models.DescribeColdStorageRequest,
    ) -> main_models.DescribeColdStorageResponse:
        runtime = RuntimeOptions()
        return self.describe_cold_storage_with_options(request, runtime)

    async def describe_cold_storage_async(
        self,
        request: main_models.DescribeColdStorageRequest,
    ) -> main_models.DescribeColdStorageResponse:
        runtime = RuntimeOptions()
        return await self.describe_cold_storage_with_options_async(request, runtime)

    def describe_dbinstance_usage_with_options(
        self,
        request: main_models.DescribeDBInstanceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceUsage',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_usage_with_options_async(
        self,
        request: main_models.DescribeDBInstanceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDBInstanceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDBInstanceUsage',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDBInstanceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_usage(
        self,
        request: main_models.DescribeDBInstanceUsageRequest,
    ) -> main_models.DescribeDBInstanceUsageResponse:
        runtime = RuntimeOptions()
        return self.describe_dbinstance_usage_with_options(request, runtime)

    async def describe_dbinstance_usage_async(
        self,
        request: main_models.DescribeDBInstanceUsageRequest,
    ) -> main_models.DescribeDBInstanceUsageResponse:
        runtime = RuntimeOptions()
        return await self.describe_dbinstance_usage_with_options_async(request, runtime)

    def describe_deleted_instances_with_options(
        self,
        request: main_models.DescribeDeletedInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeletedInstancesResponse:
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
            action = 'DescribeDeletedInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeletedInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deleted_instances_with_options_async(
        self,
        request: main_models.DescribeDeletedInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDeletedInstancesResponse:
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
            action = 'DescribeDeletedInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDeletedInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deleted_instances(
        self,
        request: main_models.DescribeDeletedInstancesRequest,
    ) -> main_models.DescribeDeletedInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_deleted_instances_with_options(request, runtime)

    async def describe_deleted_instances_async(
        self,
        request: main_models.DescribeDeletedInstancesRequest,
    ) -> main_models.DescribeDeletedInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_deleted_instances_with_options_async(request, runtime)

    def describe_disk_warning_line_with_options(
        self,
        request: main_models.DescribeDiskWarningLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskWarningLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskWarningLine',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskWarningLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_disk_warning_line_with_options_async(
        self,
        request: main_models.DescribeDiskWarningLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiskWarningLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiskWarningLine',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiskWarningLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_disk_warning_line(
        self,
        request: main_models.DescribeDiskWarningLineRequest,
    ) -> main_models.DescribeDiskWarningLineResponse:
        runtime = RuntimeOptions()
        return self.describe_disk_warning_line_with_options(request, runtime)

    async def describe_disk_warning_line_async(
        self,
        request: main_models.DescribeDiskWarningLineRequest,
    ) -> main_models.DescribeDiskWarningLineResponse:
        runtime = RuntimeOptions()
        return await self.describe_disk_warning_line_with_options_async(request, runtime)

    def describe_endpoints_with_options(
        self,
        request: main_models.DescribeEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEndpoints',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_endpoints_with_options_async(
        self,
        request: main_models.DescribeEndpointsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEndpointsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEndpoints',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_endpoints(
        self,
        request: main_models.DescribeEndpointsRequest,
    ) -> main_models.DescribeEndpointsResponse:
        runtime = RuntimeOptions()
        return self.describe_endpoints_with_options(request, runtime)

    async def describe_endpoints_async(
        self,
        request: main_models.DescribeEndpointsRequest,
    ) -> main_models.DescribeEndpointsResponse:
        runtime = RuntimeOptions()
        return await self.describe_endpoints_with_options_async(request, runtime)

    def describe_instance_with_options(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_with_options_async(
        self,
        request: main_models.DescribeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstance',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    async def describe_instance_async(
        self,
        request: main_models.DescribeInstanceRequest,
    ) -> main_models.DescribeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_with_options_async(request, runtime)

    def describe_instance_type_with_options(
        self,
        request: main_models.DescribeInstanceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceType',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_type_with_options_async(
        self,
        request: main_models.DescribeInstanceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstanceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstanceType',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstanceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_type(
        self,
        request: main_models.DescribeInstanceTypeRequest,
    ) -> main_models.DescribeInstanceTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_instance_type_with_options(request, runtime)

    async def describe_instance_type_async(
        self,
        request: main_models.DescribeInstanceTypeRequest,
    ) -> main_models.DescribeInstanceTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_instance_type_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.db_type):
            query['DbType'] = request.db_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: main_models.DescribeInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.db_type):
            query['DbType'] = request.db_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instances(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: main_models.DescribeInstancesRequest,
    ) -> main_models.DescribeInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_ip_whitelist_with_options(
        self,
        request: main_models.DescribeIpWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpWhitelist',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ip_whitelist_with_options_async(
        self,
        request: main_models.DescribeIpWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIpWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIpWhitelist',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ip_whitelist(
        self,
        request: main_models.DescribeIpWhitelistRequest,
    ) -> main_models.DescribeIpWhitelistResponse:
        runtime = RuntimeOptions()
        return self.describe_ip_whitelist_with_options(request, runtime)

    async def describe_ip_whitelist_async(
        self,
        request: main_models.DescribeIpWhitelistRequest,
    ) -> main_models.DescribeIpWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.describe_ip_whitelist_with_options_async(request, runtime)

    def describe_multi_zone_available_regions_with_options(
        self,
        request: main_models.DescribeMultiZoneAvailableRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMultiZoneAvailableRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMultiZoneAvailableRegions',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMultiZoneAvailableRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_multi_zone_available_regions_with_options_async(
        self,
        request: main_models.DescribeMultiZoneAvailableRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMultiZoneAvailableRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMultiZoneAvailableRegions',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMultiZoneAvailableRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_multi_zone_available_regions(
        self,
        request: main_models.DescribeMultiZoneAvailableRegionsRequest,
    ) -> main_models.DescribeMultiZoneAvailableRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_multi_zone_available_regions_with_options(request, runtime)

    async def describe_multi_zone_available_regions_async(
        self,
        request: main_models.DescribeMultiZoneAvailableRegionsRequest,
    ) -> main_models.DescribeMultiZoneAvailableRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_multi_zone_available_regions_with_options_async(request, runtime)

    def describe_multi_zone_available_resource_with_options(
        self,
        request: main_models.DescribeMultiZoneAvailableResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMultiZoneAvailableResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_combination):
            query['ZoneCombination'] = request.zone_combination
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMultiZoneAvailableResource',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMultiZoneAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_multi_zone_available_resource_with_options_async(
        self,
        request: main_models.DescribeMultiZoneAvailableResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMultiZoneAvailableResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_combination):
            query['ZoneCombination'] = request.zone_combination
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMultiZoneAvailableResource',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMultiZoneAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_multi_zone_available_resource(
        self,
        request: main_models.DescribeMultiZoneAvailableResourceRequest,
    ) -> main_models.DescribeMultiZoneAvailableResourceResponse:
        runtime = RuntimeOptions()
        return self.describe_multi_zone_available_resource_with_options(request, runtime)

    async def describe_multi_zone_available_resource_async(
        self,
        request: main_models.DescribeMultiZoneAvailableResourceRequest,
    ) -> main_models.DescribeMultiZoneAvailableResourceResponse:
        runtime = RuntimeOptions()
        return await self.describe_multi_zone_available_resource_with_options_async(request, runtime)

    def describe_multi_zone_cluster_with_options(
        self,
        request: main_models.DescribeMultiZoneClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMultiZoneClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMultiZoneCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMultiZoneClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_multi_zone_cluster_with_options_async(
        self,
        request: main_models.DescribeMultiZoneClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMultiZoneClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMultiZoneCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMultiZoneClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_multi_zone_cluster(
        self,
        request: main_models.DescribeMultiZoneClusterRequest,
    ) -> main_models.DescribeMultiZoneClusterResponse:
        runtime = RuntimeOptions()
        return self.describe_multi_zone_cluster_with_options(request, runtime)

    async def describe_multi_zone_cluster_async(
        self,
        request: main_models.DescribeMultiZoneClusterRequest,
    ) -> main_models.DescribeMultiZoneClusterResponse:
        runtime = RuntimeOptions()
        return await self.describe_multi_zone_cluster_with_options_async(request, runtime)

    def describe_recoverable_time_range_with_options(
        self,
        request: main_models.DescribeRecoverableTimeRangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecoverableTimeRangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecoverableTimeRange',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecoverableTimeRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_recoverable_time_range_with_options_async(
        self,
        request: main_models.DescribeRecoverableTimeRangeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRecoverableTimeRangeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRecoverableTimeRange',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRecoverableTimeRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_recoverable_time_range(
        self,
        request: main_models.DescribeRecoverableTimeRangeRequest,
    ) -> main_models.DescribeRecoverableTimeRangeResponse:
        runtime = RuntimeOptions()
        return self.describe_recoverable_time_range_with_options(request, runtime)

    async def describe_recoverable_time_range_async(
        self,
        request: main_models.DescribeRecoverableTimeRangeRequest,
    ) -> main_models.DescribeRecoverableTimeRangeResponse:
        runtime = RuntimeOptions()
        return await self.describe_recoverable_time_range_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-01-01',
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

    def describe_restore_full_details_with_options(
        self,
        request: main_models.DescribeRestoreFullDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreFullDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreFullDetails',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreFullDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_full_details_with_options_async(
        self,
        request: main_models.DescribeRestoreFullDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreFullDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreFullDetails',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreFullDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_full_details(
        self,
        request: main_models.DescribeRestoreFullDetailsRequest,
    ) -> main_models.DescribeRestoreFullDetailsResponse:
        runtime = RuntimeOptions()
        return self.describe_restore_full_details_with_options(request, runtime)

    async def describe_restore_full_details_async(
        self,
        request: main_models.DescribeRestoreFullDetailsRequest,
    ) -> main_models.DescribeRestoreFullDetailsResponse:
        runtime = RuntimeOptions()
        return await self.describe_restore_full_details_with_options_async(request, runtime)

    def describe_restore_incr_detail_with_options(
        self,
        request: main_models.DescribeRestoreIncrDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreIncrDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreIncrDetail',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreIncrDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_incr_detail_with_options_async(
        self,
        request: main_models.DescribeRestoreIncrDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreIncrDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreIncrDetail',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreIncrDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_incr_detail(
        self,
        request: main_models.DescribeRestoreIncrDetailRequest,
    ) -> main_models.DescribeRestoreIncrDetailResponse:
        runtime = RuntimeOptions()
        return self.describe_restore_incr_detail_with_options(request, runtime)

    async def describe_restore_incr_detail_async(
        self,
        request: main_models.DescribeRestoreIncrDetailRequest,
    ) -> main_models.DescribeRestoreIncrDetailResponse:
        runtime = RuntimeOptions()
        return await self.describe_restore_incr_detail_with_options_async(request, runtime)

    def describe_restore_schema_details_with_options(
        self,
        request: main_models.DescribeRestoreSchemaDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreSchemaDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreSchemaDetails',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreSchemaDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_schema_details_with_options_async(
        self,
        request: main_models.DescribeRestoreSchemaDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreSchemaDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreSchemaDetails',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreSchemaDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_schema_details(
        self,
        request: main_models.DescribeRestoreSchemaDetailsRequest,
    ) -> main_models.DescribeRestoreSchemaDetailsResponse:
        runtime = RuntimeOptions()
        return self.describe_restore_schema_details_with_options(request, runtime)

    async def describe_restore_schema_details_async(
        self,
        request: main_models.DescribeRestoreSchemaDetailsRequest,
    ) -> main_models.DescribeRestoreSchemaDetailsResponse:
        runtime = RuntimeOptions()
        return await self.describe_restore_schema_details_with_options_async(request, runtime)

    def describe_restore_summary_with_options(
        self,
        request: main_models.DescribeRestoreSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreSummary',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_summary_with_options_async(
        self,
        request: main_models.DescribeRestoreSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreSummary',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_summary(
        self,
        request: main_models.DescribeRestoreSummaryRequest,
    ) -> main_models.DescribeRestoreSummaryResponse:
        runtime = RuntimeOptions()
        return self.describe_restore_summary_with_options(request, runtime)

    async def describe_restore_summary_async(
        self,
        request: main_models.DescribeRestoreSummaryRequest,
    ) -> main_models.DescribeRestoreSummaryResponse:
        runtime = RuntimeOptions()
        return await self.describe_restore_summary_with_options_async(request, runtime)

    def describe_restore_tables_with_options(
        self,
        request: main_models.DescribeRestoreTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreTables',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_tables_with_options_async(
        self,
        request: main_models.DescribeRestoreTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.restore_record_id):
            query['RestoreRecordId'] = request.restore_record_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreTables',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_tables(
        self,
        request: main_models.DescribeRestoreTablesRequest,
    ) -> main_models.DescribeRestoreTablesResponse:
        runtime = RuntimeOptions()
        return self.describe_restore_tables_with_options(request, runtime)

    async def describe_restore_tables_async(
        self,
        request: main_models.DescribeRestoreTablesRequest,
    ) -> main_models.DescribeRestoreTablesResponse:
        runtime = RuntimeOptions()
        return await self.describe_restore_tables_with_options_async(request, runtime)

    def describe_security_groups_with_options(
        self,
        request: main_models.DescribeSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityGroups',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_groups_with_options_async(
        self,
        request: main_models.DescribeSecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSecurityGroups',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_groups(
        self,
        request: main_models.DescribeSecurityGroupsRequest,
    ) -> main_models.DescribeSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_security_groups_with_options(request, runtime)

    async def describe_security_groups_async(
        self,
        request: main_models.DescribeSecurityGroupsRequest,
    ) -> main_models.DescribeSecurityGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_security_groups_with_options_async(request, runtime)

    def describe_serverless_cluster_with_options(
        self,
        request: main_models.DescribeServerlessClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServerlessClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServerlessCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServerlessClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_serverless_cluster_with_options_async(
        self,
        request: main_models.DescribeServerlessClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeServerlessClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeServerlessCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeServerlessClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_serverless_cluster(
        self,
        request: main_models.DescribeServerlessClusterRequest,
    ) -> main_models.DescribeServerlessClusterResponse:
        runtime = RuntimeOptions()
        return self.describe_serverless_cluster_with_options(request, runtime)

    async def describe_serverless_cluster_async(
        self,
        request: main_models.DescribeServerlessClusterRequest,
    ) -> main_models.DescribeServerlessClusterResponse:
        runtime = RuntimeOptions()
        return await self.describe_serverless_cluster_with_options_async(request, runtime)

    def describe_sub_domain_with_options(
        self,
        request: main_models.DescribeSubDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubDomainResponse:
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
            action = 'DescribeSubDomain',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sub_domain_with_options_async(
        self,
        request: main_models.DescribeSubDomainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSubDomainResponse:
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
            action = 'DescribeSubDomain',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSubDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sub_domain(
        self,
        request: main_models.DescribeSubDomainRequest,
    ) -> main_models.DescribeSubDomainResponse:
        runtime = RuntimeOptions()
        return self.describe_sub_domain_with_options(request, runtime)

    async def describe_sub_domain_async(
        self,
        request: main_models.DescribeSubDomainRequest,
    ) -> main_models.DescribeSubDomainResponse:
        runtime = RuntimeOptions()
        return await self.describe_sub_domain_with_options_async(request, runtime)

    def enable_hbaseue_backup_with_options(
        self,
        request: main_models.EnableHBaseueBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableHBaseueBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        if not DaraCore.is_null(request.hbaseue_cluster_id):
            query['HbaseueClusterId'] = request.hbaseue_cluster_id
        if not DaraCore.is_null(request.node_count):
            query['NodeCount'] = request.node_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHBaseueBackup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHBaseueBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_hbaseue_backup_with_options_async(
        self,
        request: main_models.EnableHBaseueBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableHBaseueBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        if not DaraCore.is_null(request.hbaseue_cluster_id):
            query['HbaseueClusterId'] = request.hbaseue_cluster_id
        if not DaraCore.is_null(request.node_count):
            query['NodeCount'] = request.node_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHBaseueBackup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHBaseueBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_hbaseue_backup(
        self,
        request: main_models.EnableHBaseueBackupRequest,
    ) -> main_models.EnableHBaseueBackupResponse:
        runtime = RuntimeOptions()
        return self.enable_hbaseue_backup_with_options(request, runtime)

    async def enable_hbaseue_backup_async(
        self,
        request: main_models.EnableHBaseueBackupRequest,
    ) -> main_models.EnableHBaseueBackupResponse:
        runtime = RuntimeOptions()
        return await self.enable_hbaseue_backup_with_options_async(request, runtime)

    def enable_hbaseue_module_with_options(
        self,
        request: main_models.EnableHBaseueModuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableHBaseueModuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.bds_id):
            query['BdsId'] = request.bds_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.hbaseue_cluster_id):
            query['HbaseueClusterId'] = request.hbaseue_cluster_id
        if not DaraCore.is_null(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not DaraCore.is_null(request.module_cluster_name):
            query['ModuleClusterName'] = request.module_cluster_name
        if not DaraCore.is_null(request.module_type_name):
            query['ModuleTypeName'] = request.module_type_name
        if not DaraCore.is_null(request.node_count):
            query['NodeCount'] = request.node_count
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHBaseueModule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHBaseueModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_hbaseue_module_with_options_async(
        self,
        request: main_models.EnableHBaseueModuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableHBaseueModuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.bds_id):
            query['BdsId'] = request.bds_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not DaraCore.is_null(request.disk_type):
            query['DiskType'] = request.disk_type
        if not DaraCore.is_null(request.hbaseue_cluster_id):
            query['HbaseueClusterId'] = request.hbaseue_cluster_id
        if not DaraCore.is_null(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not DaraCore.is_null(request.module_cluster_name):
            query['ModuleClusterName'] = request.module_cluster_name
        if not DaraCore.is_null(request.module_type_name):
            query['ModuleTypeName'] = request.module_type_name
        if not DaraCore.is_null(request.node_count):
            query['NodeCount'] = request.node_count
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHBaseueModule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHBaseueModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_hbaseue_module(
        self,
        request: main_models.EnableHBaseueModuleRequest,
    ) -> main_models.EnableHBaseueModuleResponse:
        runtime = RuntimeOptions()
        return self.enable_hbaseue_module_with_options(request, runtime)

    async def enable_hbaseue_module_async(
        self,
        request: main_models.EnableHBaseueModuleRequest,
    ) -> main_models.EnableHBaseueModuleResponse:
        runtime = RuntimeOptions()
        return await self.enable_hbaseue_module_with_options_async(request, runtime)

    def evaluate_multi_zone_resource_with_options(
        self,
        request: main_models.EvaluateMultiZoneResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EvaluateMultiZoneResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not DaraCore.is_null(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not DaraCore.is_null(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not DaraCore.is_null(request.core_disk_type):
            query['CoreDiskType'] = request.core_disk_type
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.core_node_count):
            query['CoreNodeCount'] = request.core_node_count
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.log_disk_size):
            query['LogDiskSize'] = request.log_disk_size
        if not DaraCore.is_null(request.log_disk_type):
            query['LogDiskType'] = request.log_disk_type
        if not DaraCore.is_null(request.log_instance_type):
            query['LogInstanceType'] = request.log_instance_type
        if not DaraCore.is_null(request.log_node_count):
            query['LogNodeCount'] = request.log_node_count
        if not DaraCore.is_null(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not DaraCore.is_null(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EvaluateMultiZoneResource',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EvaluateMultiZoneResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def evaluate_multi_zone_resource_with_options_async(
        self,
        request: main_models.EvaluateMultiZoneResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EvaluateMultiZoneResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not DaraCore.is_null(request.arbiter_zone_id):
            query['ArbiterZoneId'] = request.arbiter_zone_id
        if not DaraCore.is_null(request.arch_version):
            query['ArchVersion'] = request.arch_version
        if not DaraCore.is_null(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not DaraCore.is_null(request.core_disk_type):
            query['CoreDiskType'] = request.core_disk_type
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.core_node_count):
            query['CoreNodeCount'] = request.core_node_count
        if not DaraCore.is_null(request.engine):
            query['Engine'] = request.engine
        if not DaraCore.is_null(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not DaraCore.is_null(request.log_disk_size):
            query['LogDiskSize'] = request.log_disk_size
        if not DaraCore.is_null(request.log_disk_type):
            query['LogDiskType'] = request.log_disk_type
        if not DaraCore.is_null(request.log_instance_type):
            query['LogInstanceType'] = request.log_instance_type
        if not DaraCore.is_null(request.log_node_count):
            query['LogNodeCount'] = request.log_node_count
        if not DaraCore.is_null(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        if not DaraCore.is_null(request.multi_zone_combination):
            query['MultiZoneCombination'] = request.multi_zone_combination
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.primary_zone_id):
            query['PrimaryZoneId'] = request.primary_zone_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        if not DaraCore.is_null(request.standby_zone_id):
            query['StandbyZoneId'] = request.standby_zone_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EvaluateMultiZoneResource',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EvaluateMultiZoneResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def evaluate_multi_zone_resource(
        self,
        request: main_models.EvaluateMultiZoneResourceRequest,
    ) -> main_models.EvaluateMultiZoneResourceResponse:
        runtime = RuntimeOptions()
        return self.evaluate_multi_zone_resource_with_options(request, runtime)

    async def evaluate_multi_zone_resource_async(
        self,
        request: main_models.EvaluateMultiZoneResourceRequest,
    ) -> main_models.EvaluateMultiZoneResourceResponse:
        runtime = RuntimeOptions()
        return await self.evaluate_multi_zone_resource_with_options_async(request, runtime)

    def get_multimode_cms_url_with_options(
        self,
        request: main_models.GetMultimodeCmsUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultimodeCmsUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultimodeCmsUrl',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultimodeCmsUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multimode_cms_url_with_options_async(
        self,
        request: main_models.GetMultimodeCmsUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultimodeCmsUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultimodeCmsUrl',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultimodeCmsUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multimode_cms_url(
        self,
        request: main_models.GetMultimodeCmsUrlRequest,
    ) -> main_models.GetMultimodeCmsUrlResponse:
        runtime = RuntimeOptions()
        return self.get_multimode_cms_url_with_options(request, runtime)

    async def get_multimode_cms_url_async(
        self,
        request: main_models.GetMultimodeCmsUrlRequest,
    ) -> main_models.GetMultimodeCmsUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_multimode_cms_url_with_options_async(request, runtime)

    def grant_with_options(
        self,
        request: main_models.GrantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.acl_actions):
            query['AclActions'] = request.acl_actions
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Grant',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_with_options_async(
        self,
        request: main_models.GrantRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GrantResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.acl_actions):
            query['AclActions'] = request.acl_actions
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Grant',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GrantResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant(
        self,
        request: main_models.GrantRequest,
    ) -> main_models.GrantResponse:
        runtime = RuntimeOptions()
        return self.grant_with_options(request, runtime)

    async def grant_async(
        self,
        request: main_models.GrantRequest,
    ) -> main_models.GrantResponse:
        runtime = RuntimeOptions()
        return await self.grant_with_options_async(request, runtime)

    def list_hbase_instances_with_options(
        self,
        request: main_models.ListHBaseInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHBaseInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHBaseInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHBaseInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hbase_instances_with_options_async(
        self,
        request: main_models.ListHBaseInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHBaseInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListHBaseInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHBaseInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hbase_instances(
        self,
        request: main_models.ListHBaseInstancesRequest,
    ) -> main_models.ListHBaseInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_hbase_instances_with_options(request, runtime)

    async def list_hbase_instances_async(
        self,
        request: main_models.ListHBaseInstancesRequest,
    ) -> main_models.ListHBaseInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_hbase_instances_with_options_async(request, runtime)

    def list_instance_service_config_histories_with_options(
        self,
        request: main_models.ListInstanceServiceConfigHistoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceServiceConfigHistoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceServiceConfigHistories',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceServiceConfigHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_service_config_histories_with_options_async(
        self,
        request: main_models.ListInstanceServiceConfigHistoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceServiceConfigHistoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceServiceConfigHistories',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceServiceConfigHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_service_config_histories(
        self,
        request: main_models.ListInstanceServiceConfigHistoriesRequest,
    ) -> main_models.ListInstanceServiceConfigHistoriesResponse:
        runtime = RuntimeOptions()
        return self.list_instance_service_config_histories_with_options(request, runtime)

    async def list_instance_service_config_histories_async(
        self,
        request: main_models.ListInstanceServiceConfigHistoriesRequest,
    ) -> main_models.ListInstanceServiceConfigHistoriesResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_service_config_histories_with_options_async(request, runtime)

    def list_instance_service_configurations_with_options(
        self,
        request: main_models.ListInstanceServiceConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceServiceConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceServiceConfigurations',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceServiceConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_service_configurations_with_options_async(
        self,
        request: main_models.ListInstanceServiceConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceServiceConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceServiceConfigurations',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceServiceConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_service_configurations(
        self,
        request: main_models.ListInstanceServiceConfigurationsRequest,
    ) -> main_models.ListInstanceServiceConfigurationsResponse:
        runtime = RuntimeOptions()
        return self.list_instance_service_configurations_with_options(request, runtime)

    async def list_instance_service_configurations_async(
        self,
        request: main_models.ListInstanceServiceConfigurationsRequest,
    ) -> main_models.ListInstanceServiceConfigurationsResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_service_configurations_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-01-01',
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

    def list_tags_with_options(
        self,
        request: main_models.ListTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTags',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tags_with_options_async(
        self,
        request: main_models.ListTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTags',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tags(
        self,
        request: main_models.ListTagsRequest,
    ) -> main_models.ListTagsResponse:
        runtime = RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    async def list_tags_async(
        self,
        request: main_models.ListTagsRequest,
    ) -> main_models.ListTagsResponse:
        runtime = RuntimeOptions()
        return await self.list_tags_with_options_async(request, runtime)

    def modify_account_password_with_options(
        self,
        request: main_models.ModifyAccountPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.new_account_password):
            query['NewAccountPassword'] = request.new_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountPassword',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_password_with_options_async(
        self,
        request: main_models.ModifyAccountPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAccountPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.new_account_password):
            query['NewAccountPassword'] = request.new_account_password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAccountPassword',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_password(
        self,
        request: main_models.ModifyAccountPasswordRequest,
    ) -> main_models.ModifyAccountPasswordResponse:
        runtime = RuntimeOptions()
        return self.modify_account_password_with_options(request, runtime)

    async def modify_account_password_async(
        self,
        request: main_models.ModifyAccountPasswordRequest,
    ) -> main_models.ModifyAccountPasswordResponse:
        runtime = RuntimeOptions()
        return await self.modify_account_password_with_options_async(request, runtime)

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
            version = '2019-01-01',
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
            version = '2019-01-01',
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

    def modify_backup_plan_config_with_options(
        self,
        request: main_models.ModifyBackupPlanConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPlanConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.full_backup_cycle):
            query['FullBackupCycle'] = request.full_backup_cycle
        if not DaraCore.is_null(request.min_hfile_backup_count):
            query['MinHFileBackupCount'] = request.min_hfile_backup_count
        if not DaraCore.is_null(request.next_full_backup_date):
            query['NextFullBackupDate'] = request.next_full_backup_date
        if not DaraCore.is_null(request.tables):
            query['Tables'] = request.tables
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPlanConfig',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupPlanConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_plan_config_with_options_async(
        self,
        request: main_models.ModifyBackupPlanConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPlanConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.full_backup_cycle):
            query['FullBackupCycle'] = request.full_backup_cycle
        if not DaraCore.is_null(request.min_hfile_backup_count):
            query['MinHFileBackupCount'] = request.min_hfile_backup_count
        if not DaraCore.is_null(request.next_full_backup_date):
            query['NextFullBackupDate'] = request.next_full_backup_date
        if not DaraCore.is_null(request.tables):
            query['Tables'] = request.tables
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPlanConfig',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupPlanConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_plan_config(
        self,
        request: main_models.ModifyBackupPlanConfigRequest,
    ) -> main_models.ModifyBackupPlanConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_backup_plan_config_with_options(request, runtime)

    async def modify_backup_plan_config_async(
        self,
        request: main_models.ModifyBackupPlanConfigRequest,
    ) -> main_models.ModifyBackupPlanConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_backup_plan_config_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: main_models.ModifyBackupPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.preferred_backup_end_time_utc):
            query['PreferredBackupEndTimeUTC'] = request.preferred_backup_end_time_utc
        if not DaraCore.is_null(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not DaraCore.is_null(request.preferred_backup_start_time_utc):
            query['PreferredBackupStartTimeUTC'] = request.preferred_backup_start_time_utc
        if not DaraCore.is_null(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPolicy',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.preferred_backup_end_time_utc):
            query['PreferredBackupEndTimeUTC'] = request.preferred_backup_end_time_utc
        if not DaraCore.is_null(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not DaraCore.is_null(request.preferred_backup_start_time_utc):
            query['PreferredBackupStartTimeUTC'] = request.preferred_backup_start_time_utc
        if not DaraCore.is_null(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPolicy',
            version = '2019-01-01',
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

    def modify_cluster_deletion_protection_with_options(
        self,
        request: main_models.ModifyClusterDeletionProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterDeletionProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.protection):
            query['Protection'] = request.protection
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterDeletionProtection',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_deletion_protection_with_options_async(
        self,
        request: main_models.ModifyClusterDeletionProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyClusterDeletionProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.protection):
            query['Protection'] = request.protection
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyClusterDeletionProtection',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyClusterDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_deletion_protection(
        self,
        request: main_models.ModifyClusterDeletionProtectionRequest,
    ) -> main_models.ModifyClusterDeletionProtectionResponse:
        runtime = RuntimeOptions()
        return self.modify_cluster_deletion_protection_with_options(request, runtime)

    async def modify_cluster_deletion_protection_async(
        self,
        request: main_models.ModifyClusterDeletionProtectionRequest,
    ) -> main_models.ModifyClusterDeletionProtectionResponse:
        runtime = RuntimeOptions()
        return await self.modify_cluster_deletion_protection_with_options_async(request, runtime)

    def modify_disk_warning_line_with_options(
        self,
        request: main_models.ModifyDiskWarningLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskWarningLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.warning_line):
            query['WarningLine'] = request.warning_line
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskWarningLine',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskWarningLineResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_disk_warning_line_with_options_async(
        self,
        request: main_models.ModifyDiskWarningLineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyDiskWarningLineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.warning_line):
            query['WarningLine'] = request.warning_line
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyDiskWarningLine',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyDiskWarningLineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_disk_warning_line(
        self,
        request: main_models.ModifyDiskWarningLineRequest,
    ) -> main_models.ModifyDiskWarningLineResponse:
        runtime = RuntimeOptions()
        return self.modify_disk_warning_line_with_options(request, runtime)

    async def modify_disk_warning_line_async(
        self,
        request: main_models.ModifyDiskWarningLineRequest,
    ) -> main_models.ModifyDiskWarningLineResponse:
        runtime = RuntimeOptions()
        return await self.modify_disk_warning_line_with_options_async(request, runtime)

    def modify_instance_maintain_time_with_options(
        self,
        request: main_models.ModifyInstanceMaintainTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceMaintainTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not DaraCore.is_null(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceMaintainTime',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_maintain_time_with_options_async(
        self,
        request: main_models.ModifyInstanceMaintainTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceMaintainTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.maintain_end_time):
            query['MaintainEndTime'] = request.maintain_end_time
        if not DaraCore.is_null(request.maintain_start_time):
            query['MaintainStartTime'] = request.maintain_start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceMaintainTime',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_maintain_time(
        self,
        request: main_models.ModifyInstanceMaintainTimeRequest,
    ) -> main_models.ModifyInstanceMaintainTimeResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_maintain_time_with_options(request, runtime)

    async def modify_instance_maintain_time_async(
        self,
        request: main_models.ModifyInstanceMaintainTimeRequest,
    ) -> main_models.ModifyInstanceMaintainTimeResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_maintain_time_with_options_async(request, runtime)

    def modify_instance_name_with_options(
        self,
        request: main_models.ModifyInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceName',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_name_with_options_async(
        self,
        request: main_models.ModifyInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceName',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_name(
        self,
        request: main_models.ModifyInstanceNameRequest,
    ) -> main_models.ModifyInstanceNameResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_name_with_options(request, runtime)

    async def modify_instance_name_async(
        self,
        request: main_models.ModifyInstanceNameRequest,
    ) -> main_models.ModifyInstanceNameResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_name_with_options_async(request, runtime)

    def modify_instance_service_config_with_options(
        self,
        request: main_models.ModifyInstanceServiceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceServiceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.configure_name):
            query['ConfigureName'] = request.configure_name
        if not DaraCore.is_null(request.configure_value):
            query['ConfigureValue'] = request.configure_value
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.restart):
            query['Restart'] = request.restart
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceServiceConfig',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceServiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_service_config_with_options_async(
        self,
        request: main_models.ModifyInstanceServiceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceServiceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.configure_name):
            query['ConfigureName'] = request.configure_name
        if not DaraCore.is_null(request.configure_value):
            query['ConfigureValue'] = request.configure_value
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.restart):
            query['Restart'] = request.restart
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceServiceConfig',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceServiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_service_config(
        self,
        request: main_models.ModifyInstanceServiceConfigRequest,
    ) -> main_models.ModifyInstanceServiceConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_service_config_with_options(request, runtime)

    async def modify_instance_service_config_async(
        self,
        request: main_models.ModifyInstanceServiceConfigRequest,
    ) -> main_models.ModifyInstanceServiceConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_service_config_with_options_async(request, runtime)

    def modify_instance_type_with_options(
        self,
        request: main_models.ModifyInstanceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceType',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_type_with_options_async(
        self,
        request: main_models.ModifyInstanceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyInstanceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyInstanceType',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyInstanceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_type(
        self,
        request: main_models.ModifyInstanceTypeRequest,
    ) -> main_models.ModifyInstanceTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_instance_type_with_options(request, runtime)

    async def modify_instance_type_async(
        self,
        request: main_models.ModifyInstanceTypeRequest,
    ) -> main_models.ModifyInstanceTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_instance_type_with_options_async(request, runtime)

    def modify_ip_whitelist_with_options(
        self,
        request: main_models.ModifyIpWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIpWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIpWhitelist',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIpWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ip_whitelist_with_options_async(
        self,
        request: main_models.ModifyIpWhitelistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyIpWhitelistResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.ip_list):
            query['IpList'] = request.ip_list
        if not DaraCore.is_null(request.ip_version):
            query['IpVersion'] = request.ip_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyIpWhitelist',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyIpWhitelistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ip_whitelist(
        self,
        request: main_models.ModifyIpWhitelistRequest,
    ) -> main_models.ModifyIpWhitelistResponse:
        runtime = RuntimeOptions()
        return self.modify_ip_whitelist_with_options(request, runtime)

    async def modify_ip_whitelist_async(
        self,
        request: main_models.ModifyIpWhitelistRequest,
    ) -> main_models.ModifyIpWhitelistResponse:
        runtime = RuntimeOptions()
        return await self.modify_ip_whitelist_with_options_async(request, runtime)

    def modify_multi_zone_cluster_node_type_with_options(
        self,
        request: main_models.ModifyMultiZoneClusterNodeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMultiZoneClusterNodeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.log_instance_type):
            query['LogInstanceType'] = request.log_instance_type
        if not DaraCore.is_null(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMultiZoneClusterNodeType',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMultiZoneClusterNodeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_multi_zone_cluster_node_type_with_options_async(
        self,
        request: main_models.ModifyMultiZoneClusterNodeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMultiZoneClusterNodeTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.core_instance_type):
            query['CoreInstanceType'] = request.core_instance_type
        if not DaraCore.is_null(request.log_instance_type):
            query['LogInstanceType'] = request.log_instance_type
        if not DaraCore.is_null(request.master_instance_type):
            query['MasterInstanceType'] = request.master_instance_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMultiZoneClusterNodeType',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMultiZoneClusterNodeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_multi_zone_cluster_node_type(
        self,
        request: main_models.ModifyMultiZoneClusterNodeTypeRequest,
    ) -> main_models.ModifyMultiZoneClusterNodeTypeResponse:
        runtime = RuntimeOptions()
        return self.modify_multi_zone_cluster_node_type_with_options(request, runtime)

    async def modify_multi_zone_cluster_node_type_async(
        self,
        request: main_models.ModifyMultiZoneClusterNodeTypeRequest,
    ) -> main_models.ModifyMultiZoneClusterNodeTypeResponse:
        runtime = RuntimeOptions()
        return await self.modify_multi_zone_cluster_node_type_with_options_async(request, runtime)

    def modify_security_groups_with_options(
        self,
        request: main_models.ModifySecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityGroups',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_groups_with_options_async(
        self,
        request: main_models.ModifySecurityGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySecurityGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySecurityGroups',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySecurityGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_groups(
        self,
        request: main_models.ModifySecurityGroupsRequest,
    ) -> main_models.ModifySecurityGroupsResponse:
        runtime = RuntimeOptions()
        return self.modify_security_groups_with_options(request, runtime)

    async def modify_security_groups_async(
        self,
        request: main_models.ModifySecurityGroupsRequest,
    ) -> main_models.ModifySecurityGroupsResponse:
        runtime = RuntimeOptions()
        return await self.modify_security_groups_with_options_async(request, runtime)

    def modify_uiaccount_password_with_options(
        self,
        request: main_models.ModifyUIAccountPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUIAccountPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUIAccountPassword',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUIAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_uiaccount_password_with_options_async(
        self,
        request: main_models.ModifyUIAccountPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyUIAccountPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.account_password):
            query['AccountPassword'] = request.account_password
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyUIAccountPassword',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyUIAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_uiaccount_password(
        self,
        request: main_models.ModifyUIAccountPasswordRequest,
    ) -> main_models.ModifyUIAccountPasswordResponse:
        runtime = RuntimeOptions()
        return self.modify_uiaccount_password_with_options(request, runtime)

    async def modify_uiaccount_password_async(
        self,
        request: main_models.ModifyUIAccountPasswordRequest,
    ) -> main_models.ModifyUIAccountPasswordResponse:
        runtime = RuntimeOptions()
        return await self.modify_uiaccount_password_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def open_backup_with_options(
        self,
        request: main_models.OpenBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenBackup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_backup_with_options_async(
        self,
        request: main_models.OpenBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenBackup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_backup(
        self,
        request: main_models.OpenBackupRequest,
    ) -> main_models.OpenBackupResponse:
        runtime = RuntimeOptions()
        return self.open_backup_with_options(request, runtime)

    async def open_backup_async(
        self,
        request: main_models.OpenBackupRequest,
    ) -> main_models.OpenBackupResponse:
        runtime = RuntimeOptions()
        return await self.open_backup_with_options_async(request, runtime)

    def purge_instance_with_options(
        self,
        request: main_models.PurgeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PurgeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PurgeInstance',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PurgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def purge_instance_with_options_async(
        self,
        request: main_models.PurgeInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PurgeInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PurgeInstance',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PurgeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def purge_instance(
        self,
        request: main_models.PurgeInstanceRequest,
    ) -> main_models.PurgeInstanceResponse:
        runtime = RuntimeOptions()
        return self.purge_instance_with_options(request, runtime)

    async def purge_instance_async(
        self,
        request: main_models.PurgeInstanceRequest,
    ) -> main_models.PurgeInstanceResponse:
        runtime = RuntimeOptions()
        return await self.purge_instance_with_options_async(request, runtime)

    def query_hbase_ha_dbwith_options(
        self,
        request: main_models.QueryHBaseHaDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryHBaseHaDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bds_id):
            query['BdsId'] = request.bds_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryHBaseHaDB',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryHBaseHaDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_hbase_ha_dbwith_options_async(
        self,
        request: main_models.QueryHBaseHaDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryHBaseHaDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bds_id):
            query['BdsId'] = request.bds_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryHBaseHaDB',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryHBaseHaDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_hbase_ha_db(
        self,
        request: main_models.QueryHBaseHaDBRequest,
    ) -> main_models.QueryHBaseHaDBResponse:
        runtime = RuntimeOptions()
        return self.query_hbase_ha_dbwith_options(request, runtime)

    async def query_hbase_ha_db_async(
        self,
        request: main_models.QueryHBaseHaDBRequest,
    ) -> main_models.QueryHBaseHaDBResponse:
        runtime = RuntimeOptions()
        return await self.query_hbase_ha_dbwith_options_async(request, runtime)

    def query_xpack_relate_dbwith_options(
        self,
        request: main_models.QueryXpackRelateDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryXpackRelateDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.has_single_node):
            query['HasSingleNode'] = request.has_single_node
        if not DaraCore.is_null(request.relate_db_type):
            query['RelateDbType'] = request.relate_db_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryXpackRelateDB',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryXpackRelateDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_xpack_relate_dbwith_options_async(
        self,
        request: main_models.QueryXpackRelateDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryXpackRelateDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.has_single_node):
            query['HasSingleNode'] = request.has_single_node
        if not DaraCore.is_null(request.relate_db_type):
            query['RelateDbType'] = request.relate_db_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryXpackRelateDB',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryXpackRelateDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_xpack_relate_db(
        self,
        request: main_models.QueryXpackRelateDBRequest,
    ) -> main_models.QueryXpackRelateDBResponse:
        runtime = RuntimeOptions()
        return self.query_xpack_relate_dbwith_options(request, runtime)

    async def query_xpack_relate_db_async(
        self,
        request: main_models.QueryXpackRelateDBRequest,
    ) -> main_models.QueryXpackRelateDBResponse:
        runtime = RuntimeOptions()
        return await self.query_xpack_relate_dbwith_options_async(request, runtime)

    def relate_db_for_hbase_ha_with_options(
        self,
        request: main_models.RelateDbForHBaseHaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RelateDbForHBaseHaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ha_active):
            query['HaActive'] = request.ha_active
        if not DaraCore.is_null(request.ha_active_cluster_key):
            query['HaActiveClusterKey'] = request.ha_active_cluster_key
        if not DaraCore.is_null(request.ha_active_dbtype):
            query['HaActiveDBType'] = request.ha_active_dbtype
        if not DaraCore.is_null(request.ha_active_hbase_fs_dir):
            query['HaActiveHbaseFsDir'] = request.ha_active_hbase_fs_dir
        if not DaraCore.is_null(request.ha_active_hdfs_uri):
            query['HaActiveHdfsUri'] = request.ha_active_hdfs_uri
        if not DaraCore.is_null(request.ha_active_password):
            query['HaActivePassword'] = request.ha_active_password
        if not DaraCore.is_null(request.ha_active_user):
            query['HaActiveUser'] = request.ha_active_user
        if not DaraCore.is_null(request.ha_active_version):
            query['HaActiveVersion'] = request.ha_active_version
        if not DaraCore.is_null(request.ha_migrate_type):
            query['HaMigrateType'] = request.ha_migrate_type
        if not DaraCore.is_null(request.ha_standby):
            query['HaStandby'] = request.ha_standby
        if not DaraCore.is_null(request.ha_standby_cluster_key):
            query['HaStandbyClusterKey'] = request.ha_standby_cluster_key
        if not DaraCore.is_null(request.ha_standby_dbtype):
            query['HaStandbyDBType'] = request.ha_standby_dbtype
        if not DaraCore.is_null(request.ha_standby_hbase_fs_dir):
            query['HaStandbyHbaseFsDir'] = request.ha_standby_hbase_fs_dir
        if not DaraCore.is_null(request.ha_standby_hdfs_uri):
            query['HaStandbyHdfsUri'] = request.ha_standby_hdfs_uri
        if not DaraCore.is_null(request.ha_standby_password):
            query['HaStandbyPassword'] = request.ha_standby_password
        if not DaraCore.is_null(request.ha_standby_user):
            query['HaStandbyUser'] = request.ha_standby_user
        if not DaraCore.is_null(request.ha_standby_version):
            query['HaStandbyVersion'] = request.ha_standby_version
        if not DaraCore.is_null(request.ha_tables):
            query['HaTables'] = request.ha_tables
        if not DaraCore.is_null(request.is_active_standard):
            query['IsActiveStandard'] = request.is_active_standard
        if not DaraCore.is_null(request.is_standby_standard):
            query['IsStandbyStandard'] = request.is_standby_standard
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RelateDbForHBaseHa',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RelateDbForHBaseHaResponse(),
            self.call_api(params, req, runtime)
        )

    async def relate_db_for_hbase_ha_with_options_async(
        self,
        request: main_models.RelateDbForHBaseHaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RelateDbForHBaseHaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ha_active):
            query['HaActive'] = request.ha_active
        if not DaraCore.is_null(request.ha_active_cluster_key):
            query['HaActiveClusterKey'] = request.ha_active_cluster_key
        if not DaraCore.is_null(request.ha_active_dbtype):
            query['HaActiveDBType'] = request.ha_active_dbtype
        if not DaraCore.is_null(request.ha_active_hbase_fs_dir):
            query['HaActiveHbaseFsDir'] = request.ha_active_hbase_fs_dir
        if not DaraCore.is_null(request.ha_active_hdfs_uri):
            query['HaActiveHdfsUri'] = request.ha_active_hdfs_uri
        if not DaraCore.is_null(request.ha_active_password):
            query['HaActivePassword'] = request.ha_active_password
        if not DaraCore.is_null(request.ha_active_user):
            query['HaActiveUser'] = request.ha_active_user
        if not DaraCore.is_null(request.ha_active_version):
            query['HaActiveVersion'] = request.ha_active_version
        if not DaraCore.is_null(request.ha_migrate_type):
            query['HaMigrateType'] = request.ha_migrate_type
        if not DaraCore.is_null(request.ha_standby):
            query['HaStandby'] = request.ha_standby
        if not DaraCore.is_null(request.ha_standby_cluster_key):
            query['HaStandbyClusterKey'] = request.ha_standby_cluster_key
        if not DaraCore.is_null(request.ha_standby_dbtype):
            query['HaStandbyDBType'] = request.ha_standby_dbtype
        if not DaraCore.is_null(request.ha_standby_hbase_fs_dir):
            query['HaStandbyHbaseFsDir'] = request.ha_standby_hbase_fs_dir
        if not DaraCore.is_null(request.ha_standby_hdfs_uri):
            query['HaStandbyHdfsUri'] = request.ha_standby_hdfs_uri
        if not DaraCore.is_null(request.ha_standby_password):
            query['HaStandbyPassword'] = request.ha_standby_password
        if not DaraCore.is_null(request.ha_standby_user):
            query['HaStandbyUser'] = request.ha_standby_user
        if not DaraCore.is_null(request.ha_standby_version):
            query['HaStandbyVersion'] = request.ha_standby_version
        if not DaraCore.is_null(request.ha_tables):
            query['HaTables'] = request.ha_tables
        if not DaraCore.is_null(request.is_active_standard):
            query['IsActiveStandard'] = request.is_active_standard
        if not DaraCore.is_null(request.is_standby_standard):
            query['IsStandbyStandard'] = request.is_standby_standard
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RelateDbForHBaseHa',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RelateDbForHBaseHaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def relate_db_for_hbase_ha(
        self,
        request: main_models.RelateDbForHBaseHaRequest,
    ) -> main_models.RelateDbForHBaseHaResponse:
        runtime = RuntimeOptions()
        return self.relate_db_for_hbase_ha_with_options(request, runtime)

    async def relate_db_for_hbase_ha_async(
        self,
        request: main_models.RelateDbForHBaseHaRequest,
    ) -> main_models.RelateDbForHBaseHaResponse:
        runtime = RuntimeOptions()
        return await self.relate_db_for_hbase_ha_with_options_async(request, runtime)

    def release_public_network_address_with_options(
        self,
        request: main_models.ReleasePublicNetworkAddressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleasePublicNetworkAddressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleasePublicNetworkAddress',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleasePublicNetworkAddress',
            version = '2019-01-01',
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

    def renew_instance_with_options(
        self,
        request: main_models.RenewInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: main_models.RenewInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewInstance',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: main_models.RenewInstanceRequest,
    ) -> main_models.RenewInstanceResponse:
        runtime = RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def resize_cold_storage_size_with_options(
        self,
        request: main_models.ResizeColdStorageSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResizeColdStorageSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResizeColdStorageSize',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResizeColdStorageSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_cold_storage_size_with_options_async(
        self,
        request: main_models.ResizeColdStorageSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResizeColdStorageSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cold_storage_size):
            query['ColdStorageSize'] = request.cold_storage_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResizeColdStorageSize',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResizeColdStorageSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_cold_storage_size(
        self,
        request: main_models.ResizeColdStorageSizeRequest,
    ) -> main_models.ResizeColdStorageSizeResponse:
        runtime = RuntimeOptions()
        return self.resize_cold_storage_size_with_options(request, runtime)

    async def resize_cold_storage_size_async(
        self,
        request: main_models.ResizeColdStorageSizeRequest,
    ) -> main_models.ResizeColdStorageSizeResponse:
        runtime = RuntimeOptions()
        return await self.resize_cold_storage_size_with_options_async(request, runtime)

    def resize_disk_size_with_options(
        self,
        request: main_models.ResizeDiskSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResizeDiskSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_disk_size):
            query['NodeDiskSize'] = request.node_disk_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResizeDiskSize',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResizeDiskSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_disk_size_with_options_async(
        self,
        request: main_models.ResizeDiskSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResizeDiskSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_disk_size):
            query['NodeDiskSize'] = request.node_disk_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResizeDiskSize',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResizeDiskSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_disk_size(
        self,
        request: main_models.ResizeDiskSizeRequest,
    ) -> main_models.ResizeDiskSizeResponse:
        runtime = RuntimeOptions()
        return self.resize_disk_size_with_options(request, runtime)

    async def resize_disk_size_async(
        self,
        request: main_models.ResizeDiskSizeRequest,
    ) -> main_models.ResizeDiskSizeResponse:
        runtime = RuntimeOptions()
        return await self.resize_disk_size_with_options_async(request, runtime)

    def resize_multi_zone_cluster_disk_size_with_options(
        self,
        request: main_models.ResizeMultiZoneClusterDiskSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResizeMultiZoneClusterDiskSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not DaraCore.is_null(request.log_disk_size):
            query['LogDiskSize'] = request.log_disk_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResizeMultiZoneClusterDiskSize',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResizeMultiZoneClusterDiskSizeResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_multi_zone_cluster_disk_size_with_options_async(
        self,
        request: main_models.ResizeMultiZoneClusterDiskSizeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResizeMultiZoneClusterDiskSizeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.core_disk_size):
            query['CoreDiskSize'] = request.core_disk_size
        if not DaraCore.is_null(request.log_disk_size):
            query['LogDiskSize'] = request.log_disk_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResizeMultiZoneClusterDiskSize',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResizeMultiZoneClusterDiskSizeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_multi_zone_cluster_disk_size(
        self,
        request: main_models.ResizeMultiZoneClusterDiskSizeRequest,
    ) -> main_models.ResizeMultiZoneClusterDiskSizeResponse:
        runtime = RuntimeOptions()
        return self.resize_multi_zone_cluster_disk_size_with_options(request, runtime)

    async def resize_multi_zone_cluster_disk_size_async(
        self,
        request: main_models.ResizeMultiZoneClusterDiskSizeRequest,
    ) -> main_models.ResizeMultiZoneClusterDiskSizeResponse:
        runtime = RuntimeOptions()
        return await self.resize_multi_zone_cluster_disk_size_with_options_async(request, runtime)

    def resize_multi_zone_cluster_node_count_with_options(
        self,
        request: main_models.ResizeMultiZoneClusterNodeCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResizeMultiZoneClusterNodeCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.core_node_count):
            query['CoreNodeCount'] = request.core_node_count
        if not DaraCore.is_null(request.log_node_count):
            query['LogNodeCount'] = request.log_node_count
        if not DaraCore.is_null(request.primary_core_node_count):
            query['PrimaryCoreNodeCount'] = request.primary_core_node_count
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.standby_core_node_count):
            query['StandbyCoreNodeCount'] = request.standby_core_node_count
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResizeMultiZoneClusterNodeCount',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResizeMultiZoneClusterNodeCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_multi_zone_cluster_node_count_with_options_async(
        self,
        request: main_models.ResizeMultiZoneClusterNodeCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResizeMultiZoneClusterNodeCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arbiter_vswitch_id):
            query['ArbiterVSwitchId'] = request.arbiter_vswitch_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.core_node_count):
            query['CoreNodeCount'] = request.core_node_count
        if not DaraCore.is_null(request.log_node_count):
            query['LogNodeCount'] = request.log_node_count
        if not DaraCore.is_null(request.primary_core_node_count):
            query['PrimaryCoreNodeCount'] = request.primary_core_node_count
        if not DaraCore.is_null(request.primary_vswitch_id):
            query['PrimaryVSwitchId'] = request.primary_vswitch_id
        if not DaraCore.is_null(request.standby_core_node_count):
            query['StandbyCoreNodeCount'] = request.standby_core_node_count
        if not DaraCore.is_null(request.standby_vswitch_id):
            query['StandbyVSwitchId'] = request.standby_vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResizeMultiZoneClusterNodeCount',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResizeMultiZoneClusterNodeCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_multi_zone_cluster_node_count(
        self,
        request: main_models.ResizeMultiZoneClusterNodeCountRequest,
    ) -> main_models.ResizeMultiZoneClusterNodeCountResponse:
        runtime = RuntimeOptions()
        return self.resize_multi_zone_cluster_node_count_with_options(request, runtime)

    async def resize_multi_zone_cluster_node_count_async(
        self,
        request: main_models.ResizeMultiZoneClusterNodeCountRequest,
    ) -> main_models.ResizeMultiZoneClusterNodeCountResponse:
        runtime = RuntimeOptions()
        return await self.resize_multi_zone_cluster_node_count_with_options_async(request, runtime)

    def resize_node_count_with_options(
        self,
        request: main_models.ResizeNodeCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResizeNodeCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_count):
            query['NodeCount'] = request.node_count
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResizeNodeCount',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResizeNodeCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def resize_node_count_with_options_async(
        self,
        request: main_models.ResizeNodeCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResizeNodeCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_count):
            query['NodeCount'] = request.node_count
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResizeNodeCount',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResizeNodeCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resize_node_count(
        self,
        request: main_models.ResizeNodeCountRequest,
    ) -> main_models.ResizeNodeCountResponse:
        runtime = RuntimeOptions()
        return self.resize_node_count_with_options(request, runtime)

    async def resize_node_count_async(
        self,
        request: main_models.ResizeNodeCountRequest,
    ) -> main_models.ResizeNodeCountResponse:
        runtime = RuntimeOptions()
        return await self.resize_node_count_with_options_async(request, runtime)

    def restart_instance_with_options(
        self,
        request: main_models.RestartInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.components):
            query['Components'] = request.components
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartInstance',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.components):
            query['Components'] = request.components
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartInstance',
            version = '2019-01-01',
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

    def revoke_with_options(
        self,
        request: main_models.RevokeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.acl_actions):
            query['AclActions'] = request.acl_actions
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Revoke',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_with_options_async(
        self,
        request: main_models.RevokeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevokeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_name):
            query['AccountName'] = request.account_name
        if not DaraCore.is_null(request.acl_actions):
            query['AclActions'] = request.acl_actions
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'Revoke',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke(
        self,
        request: main_models.RevokeRequest,
    ) -> main_models.RevokeResponse:
        runtime = RuntimeOptions()
        return self.revoke_with_options(request, runtime)

    async def revoke_async(
        self,
        request: main_models.RevokeRequest,
    ) -> main_models.RevokeResponse:
        runtime = RuntimeOptions()
        return await self.revoke_with_options_async(request, runtime)

    def switch_hbase_ha_slb_with_options(
        self,
        request: main_models.SwitchHbaseHaSlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchHbaseHaSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bds_id):
            query['BdsId'] = request.bds_id
        if not DaraCore.is_null(request.ha_id):
            query['HaId'] = request.ha_id
        if not DaraCore.is_null(request.ha_types):
            query['HaTypes'] = request.ha_types
        if not DaraCore.is_null(request.hbase_type):
            query['HbaseType'] = request.hbase_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchHbaseHaSlb',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchHbaseHaSlbResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_hbase_ha_slb_with_options_async(
        self,
        request: main_models.SwitchHbaseHaSlbRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchHbaseHaSlbResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bds_id):
            query['BdsId'] = request.bds_id
        if not DaraCore.is_null(request.ha_id):
            query['HaId'] = request.ha_id
        if not DaraCore.is_null(request.ha_types):
            query['HaTypes'] = request.ha_types
        if not DaraCore.is_null(request.hbase_type):
            query['HbaseType'] = request.hbase_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchHbaseHaSlb',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchHbaseHaSlbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_hbase_ha_slb(
        self,
        request: main_models.SwitchHbaseHaSlbRequest,
    ) -> main_models.SwitchHbaseHaSlbResponse:
        runtime = RuntimeOptions()
        return self.switch_hbase_ha_slb_with_options(request, runtime)

    async def switch_hbase_ha_slb_async(
        self,
        request: main_models.SwitchHbaseHaSlbRequest,
    ) -> main_models.SwitchHbaseHaSlbResponse:
        runtime = RuntimeOptions()
        return await self.switch_hbase_ha_slb_with_options_async(request, runtime)

    def switch_service_with_options(
        self,
        request: main_models.SwitchServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.operate):
            query['Operate'] = request.operate
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchService',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_service_with_options_async(
        self,
        request: main_models.SwitchServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.operate):
            query['Operate'] = request.operate
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchService',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_service(
        self,
        request: main_models.SwitchServiceRequest,
    ) -> main_models.SwitchServiceResponse:
        runtime = RuntimeOptions()
        return self.switch_service_with_options(request, runtime)

    async def switch_service_async(
        self,
        request: main_models.SwitchServiceRequest,
    ) -> main_models.SwitchServiceResponse:
        runtime = RuntimeOptions()
        return await self.switch_service_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-01-01',
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

    def un_tag_resources_with_options(
        self,
        request: main_models.UnTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagResources',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: main_models.UnTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UnTagResources',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
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
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: main_models.UnTagResourcesRequest,
    ) -> main_models.UnTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def upgrade_minor_version_with_options(
        self,
        request: main_models.UpgradeMinorVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeMinorVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.components):
            query['Components'] = request.components
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeMinorVersion',
            version = '2019-01-01',
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
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.components):
            query['Components'] = request.components
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeMinorVersion',
            version = '2019-01-01',
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

    def upgrade_multi_zone_cluster_with_options(
        self,
        request: main_models.UpgradeMultiZoneClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeMultiZoneClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.components):
            query['Components'] = request.components
        if not DaraCore.is_null(request.restart_components):
            query['RestartComponents'] = request.restart_components
        if not DaraCore.is_null(request.run_mode):
            query['RunMode'] = request.run_mode
        if not DaraCore.is_null(request.upgrade_ins_name):
            query['UpgradeInsName'] = request.upgrade_ins_name
        if not DaraCore.is_null(request.versions):
            query['Versions'] = request.versions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeMultiZoneCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeMultiZoneClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_multi_zone_cluster_with_options_async(
        self,
        request: main_models.UpgradeMultiZoneClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeMultiZoneClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.components):
            query['Components'] = request.components
        if not DaraCore.is_null(request.restart_components):
            query['RestartComponents'] = request.restart_components
        if not DaraCore.is_null(request.run_mode):
            query['RunMode'] = request.run_mode
        if not DaraCore.is_null(request.upgrade_ins_name):
            query['UpgradeInsName'] = request.upgrade_ins_name
        if not DaraCore.is_null(request.versions):
            query['Versions'] = request.versions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeMultiZoneCluster',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeMultiZoneClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_multi_zone_cluster(
        self,
        request: main_models.UpgradeMultiZoneClusterRequest,
    ) -> main_models.UpgradeMultiZoneClusterResponse:
        runtime = RuntimeOptions()
        return self.upgrade_multi_zone_cluster_with_options(request, runtime)

    async def upgrade_multi_zone_cluster_async(
        self,
        request: main_models.UpgradeMultiZoneClusterRequest,
    ) -> main_models.UpgradeMultiZoneClusterResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_multi_zone_cluster_with_options_async(request, runtime)

    def xpack_relate_dbwith_options(
        self,
        request: main_models.XpackRelateDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.XpackRelateDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.db_cluster_ids):
            query['DbClusterIds'] = request.db_cluster_ids
        if not DaraCore.is_null(request.relate_db_type):
            query['RelateDbType'] = request.relate_db_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'XpackRelateDB',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.XpackRelateDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def xpack_relate_dbwith_options_async(
        self,
        request: main_models.XpackRelateDBRequest,
        runtime: RuntimeOptions,
    ) -> main_models.XpackRelateDBResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.db_cluster_ids):
            query['DbClusterIds'] = request.db_cluster_ids
        if not DaraCore.is_null(request.relate_db_type):
            query['RelateDbType'] = request.relate_db_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'XpackRelateDB',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.XpackRelateDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def xpack_relate_db(
        self,
        request: main_models.XpackRelateDBRequest,
    ) -> main_models.XpackRelateDBResponse:
        runtime = RuntimeOptions()
        return self.xpack_relate_dbwith_options(request, runtime)

    async def xpack_relate_db_async(
        self,
        request: main_models.XpackRelateDBRequest,
    ) -> main_models.XpackRelateDBResponse:
        runtime = RuntimeOptions()
        return await self.xpack_relate_dbwith_options_async(request, runtime)
