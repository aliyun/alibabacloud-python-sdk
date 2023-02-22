# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_adb20211201 import models as adb_20211201_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'adb.aliyuncs.com',
            'cn-beijing': 'adb.aliyuncs.com',
            'cn-hangzhou': 'adb.aliyuncs.com',
            'cn-shanghai': 'adb.aliyuncs.com',
            'cn-shenzhen': 'adb.aliyuncs.com',
            'cn-hongkong': 'adb.aliyuncs.com',
            'ap-southeast-1': 'adb.aliyuncs.com',
            'us-west-1': 'adb.aliyuncs.com',
            'us-east-1': 'adb.aliyuncs.com',
            'cn-hangzhou-finance': 'adb.aliyuncs.com',
            'cn-north-2-gov-1': 'adb.aliyuncs.com',
            'ap-northeast-2-pop': 'adb.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'adb.aliyuncs.com',
            'cn-beijing-finance-pop': 'adb.aliyuncs.com',
            'cn-beijing-gov-1': 'adb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'adb.aliyuncs.com',
            'cn-edge-1': 'adb.aliyuncs.com',
            'cn-fujian': 'adb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'adb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'adb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'adb.aliyuncs.com',
            'cn-hangzhou-test-306': 'adb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'adb.aliyuncs.com',
            'cn-qingdao-nebula': 'adb.aliyuncs.com',
            'cn-shanghai-et15-b01': 'adb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'adb.aliyuncs.com',
            'cn-shanghai-finance-1': 'adb.aliyuncs.com',
            'cn-shanghai-inner': 'adb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'adb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'adb.aliyuncs.com',
            'cn-shenzhen-inner': 'adb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'adb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'adb.aliyuncs.com',
            'cn-wuhan': 'adb.aliyuncs.com',
            'cn-yushanfang': 'adb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'adb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'adb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'adb.aliyuncs.com',
            'eu-west-1-oxs': 'adb.ap-northeast-1.aliyuncs.com',
            'me-east-1': 'adb.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'adb.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('adb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def allocate_cluster_public_connection_with_options(
        self,
        request: adb_20211201_models.AllocateClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.AllocateClusterPublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateClusterPublicConnection',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.AllocateClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_cluster_public_connection_with_options_async(
        self,
        request: adb_20211201_models.AllocateClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.AllocateClusterPublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocateClusterPublicConnection',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.AllocateClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_cluster_public_connection(
        self,
        request: adb_20211201_models.AllocateClusterPublicConnectionRequest,
    ) -> adb_20211201_models.AllocateClusterPublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_cluster_public_connection_with_options(request, runtime)

    async def allocate_cluster_public_connection_async(
        self,
        request: adb_20211201_models.AllocateClusterPublicConnectionRequest,
    ) -> adb_20211201_models.AllocateClusterPublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_cluster_public_connection_with_options_async(request, runtime)

    def bind_account_with_options(
        self,
        request: adb_20211201_models.BindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.BindAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ram_user):
            query['RamUser'] = request.ram_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.BindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_account_with_options_async(
        self,
        request: adb_20211201_models.BindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.BindAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.ram_user):
            query['RamUser'] = request.ram_user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.BindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_account(
        self,
        request: adb_20211201_models.BindAccountRequest,
    ) -> adb_20211201_models.BindAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_account_with_options(request, runtime)

    async def bind_account_async(
        self,
        request: adb_20211201_models.BindAccountRequest,
    ) -> adb_20211201_models.BindAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_account_with_options_async(request, runtime)

    def check_bind_ram_user_with_options(
        self,
        request: adb_20211201_models.CheckBindRamUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CheckBindRamUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckBindRamUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CheckBindRamUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_bind_ram_user_with_options_async(
        self,
        request: adb_20211201_models.CheckBindRamUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CheckBindRamUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckBindRamUser',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CheckBindRamUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_bind_ram_user(
        self,
        request: adb_20211201_models.CheckBindRamUserRequest,
    ) -> adb_20211201_models.CheckBindRamUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_bind_ram_user_with_options(request, runtime)

    async def check_bind_ram_user_async(
        self,
        request: adb_20211201_models.CheckBindRamUserRequest,
    ) -> adb_20211201_models.CheckBindRamUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_bind_ram_user_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: adb_20211201_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: adb_20211201_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: adb_20211201_models.CreateAccountRequest,
    ) -> adb_20211201_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: adb_20211201_models.CreateAccountRequest,
    ) -> adb_20211201_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_dbcluster_with_options(
        self,
        request: adb_20211201_models.CreateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateDBClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.enable_default_resource_pool):
            query['EnableDefaultResourcePool'] = request.enable_default_resource_pool
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBCluster',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbcluster_with_options_async(
        self,
        request: adb_20211201_models.CreateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateDBClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_network_type):
            query['DBClusterNetworkType'] = request.dbcluster_network_type
        if not UtilClient.is_unset(request.dbcluster_version):
            query['DBClusterVersion'] = request.dbcluster_version
        if not UtilClient.is_unset(request.enable_default_resource_pool):
            query['EnableDefaultResourcePool'] = request.enable_default_resource_pool
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.vpcid):
            query['VPCId'] = request.vpcid
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBCluster',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbcluster(
        self,
        request: adb_20211201_models.CreateDBClusterRequest,
    ) -> adb_20211201_models.CreateDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbcluster_with_options(request, runtime)

    async def create_dbcluster_async(
        self,
        request: adb_20211201_models.CreateDBClusterRequest,
    ) -> adb_20211201_models.CreateDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbcluster_with_options_async(request, runtime)

    def create_dbresource_group_with_options(
        self,
        request: adb_20211201_models.CreateDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateDBResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not UtilClient.is_unset(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbresource_group_with_options_async(
        self,
        request: adb_20211201_models.CreateDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateDBResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not UtilClient.is_unset(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbresource_group(
        self,
        request: adb_20211201_models.CreateDBResourceGroupRequest,
    ) -> adb_20211201_models.CreateDBResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbresource_group_with_options(request, runtime)

    async def create_dbresource_group_async(
        self,
        request: adb_20211201_models.CreateDBResourceGroupRequest,
    ) -> adb_20211201_models.CreateDBResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbresource_group_with_options_async(request, runtime)

    def create_oss_sub_directory_with_options(
        self,
        request: adb_20211201_models.CreateOssSubDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateOssSubDirectoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOssSubDirectory',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateOssSubDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_oss_sub_directory_with_options_async(
        self,
        request: adb_20211201_models.CreateOssSubDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateOssSubDirectoryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.path):
            body['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOssSubDirectory',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateOssSubDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_oss_sub_directory(
        self,
        request: adb_20211201_models.CreateOssSubDirectoryRequest,
    ) -> adb_20211201_models.CreateOssSubDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_oss_sub_directory_with_options(request, runtime)

    async def create_oss_sub_directory_async(
        self,
        request: adb_20211201_models.CreateOssSubDirectoryRequest,
    ) -> adb_20211201_models.CreateOssSubDirectoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_oss_sub_directory_with_options_async(request, runtime)

    def create_spark_template_with_options(
        self,
        request: adb_20211201_models.CreateSparkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateSparkTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            body['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSparkTemplate',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateSparkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_spark_template_with_options_async(
        self,
        request: adb_20211201_models.CreateSparkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.CreateSparkTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            body['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSparkTemplate',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.CreateSparkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_spark_template(
        self,
        request: adb_20211201_models.CreateSparkTemplateRequest,
    ) -> adb_20211201_models.CreateSparkTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_spark_template_with_options(request, runtime)

    async def create_spark_template_async(
        self,
        request: adb_20211201_models.CreateSparkTemplateRequest,
    ) -> adb_20211201_models.CreateSparkTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_spark_template_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: adb_20211201_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: adb_20211201_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: adb_20211201_models.DeleteAccountRequest,
    ) -> adb_20211201_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: adb_20211201_models.DeleteAccountRequest,
    ) -> adb_20211201_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_dbcluster_with_options(
        self,
        request: adb_20211201_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteDBClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbcluster_with_options_async(
        self,
        request: adb_20211201_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteDBClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbcluster(
        self,
        request: adb_20211201_models.DeleteDBClusterRequest,
    ) -> adb_20211201_models.DeleteDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    async def delete_dbcluster_async(
        self,
        request: adb_20211201_models.DeleteDBClusterRequest,
    ) -> adb_20211201_models.DeleteDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbcluster_with_options_async(request, runtime)

    def delete_dbresource_group_with_options(
        self,
        request: adb_20211201_models.DeleteDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteDBResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbresource_group_with_options_async(
        self,
        request: adb_20211201_models.DeleteDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteDBResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbresource_group(
        self,
        request: adb_20211201_models.DeleteDBResourceGroupRequest,
    ) -> adb_20211201_models.DeleteDBResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbresource_group_with_options(request, runtime)

    async def delete_dbresource_group_async(
        self,
        request: adb_20211201_models.DeleteDBResourceGroupRequest,
    ) -> adb_20211201_models.DeleteDBResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbresource_group_with_options_async(request, runtime)

    def delete_process_instance_with_options(
        self,
        request: adb_20211201_models.DeleteProcessInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteProcessInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.process_instance_id):
            query['ProcessInstanceId'] = request.process_instance_id
        if not UtilClient.is_unset(request.project_code):
            query['ProjectCode'] = request.project_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProcessInstance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteProcessInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_process_instance_with_options_async(
        self,
        request: adb_20211201_models.DeleteProcessInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteProcessInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.process_instance_id):
            query['ProcessInstanceId'] = request.process_instance_id
        if not UtilClient.is_unset(request.project_code):
            query['ProjectCode'] = request.project_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProcessInstance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteProcessInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_process_instance(
        self,
        request: adb_20211201_models.DeleteProcessInstanceRequest,
    ) -> adb_20211201_models.DeleteProcessInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_process_instance_with_options(request, runtime)

    async def delete_process_instance_async(
        self,
        request: adb_20211201_models.DeleteProcessInstanceRequest,
    ) -> adb_20211201_models.DeleteProcessInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_process_instance_with_options_async(request, runtime)

    def delete_spark_template_with_options(
        self,
        request: adb_20211201_models.DeleteSparkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteSparkTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSparkTemplate',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteSparkTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_spark_template_with_options_async(
        self,
        request: adb_20211201_models.DeleteSparkTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteSparkTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSparkTemplate',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteSparkTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_spark_template(
        self,
        request: adb_20211201_models.DeleteSparkTemplateRequest,
    ) -> adb_20211201_models.DeleteSparkTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_spark_template_with_options(request, runtime)

    async def delete_spark_template_async(
        self,
        request: adb_20211201_models.DeleteSparkTemplateRequest,
    ) -> adb_20211201_models.DeleteSparkTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_spark_template_with_options_async(request, runtime)

    def delete_spark_template_file_with_options(
        self,
        request: adb_20211201_models.DeleteSparkTemplateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteSparkTemplateFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSparkTemplateFile',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteSparkTemplateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_spark_template_file_with_options_async(
        self,
        request: adb_20211201_models.DeleteSparkTemplateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DeleteSparkTemplateFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSparkTemplateFile',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DeleteSparkTemplateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_spark_template_file(
        self,
        request: adb_20211201_models.DeleteSparkTemplateFileRequest,
    ) -> adb_20211201_models.DeleteSparkTemplateFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_spark_template_file_with_options(request, runtime)

    async def delete_spark_template_file_async(
        self,
        request: adb_20211201_models.DeleteSparkTemplateFileRequest,
    ) -> adb_20211201_models.DeleteSparkTemplateFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_spark_template_file_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: adb_20211201_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: adb_20211201_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: adb_20211201_models.DescribeAccountsRequest,
    ) -> adb_20211201_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: adb_20211201_models.DescribeAccountsRequest,
    ) -> adb_20211201_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_adb_my_sql_columns_with_options(
        self,
        request: adb_20211201_models.DescribeAdbMySqlColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAdbMySqlColumnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdbMySqlColumns',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAdbMySqlColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_adb_my_sql_columns_with_options_async(
        self,
        request: adb_20211201_models.DescribeAdbMySqlColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAdbMySqlColumnsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdbMySqlColumns',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAdbMySqlColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_adb_my_sql_columns(
        self,
        request: adb_20211201_models.DescribeAdbMySqlColumnsRequest,
    ) -> adb_20211201_models.DescribeAdbMySqlColumnsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_adb_my_sql_columns_with_options(request, runtime)

    async def describe_adb_my_sql_columns_async(
        self,
        request: adb_20211201_models.DescribeAdbMySqlColumnsRequest,
    ) -> adb_20211201_models.DescribeAdbMySqlColumnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_adb_my_sql_columns_with_options_async(request, runtime)

    def describe_adb_my_sql_schemas_with_options(
        self,
        request: adb_20211201_models.DescribeAdbMySqlSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAdbMySqlSchemasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdbMySqlSchemas',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAdbMySqlSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_adb_my_sql_schemas_with_options_async(
        self,
        request: adb_20211201_models.DescribeAdbMySqlSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAdbMySqlSchemasResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdbMySqlSchemas',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAdbMySqlSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_adb_my_sql_schemas(
        self,
        request: adb_20211201_models.DescribeAdbMySqlSchemasRequest,
    ) -> adb_20211201_models.DescribeAdbMySqlSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_adb_my_sql_schemas_with_options(request, runtime)

    async def describe_adb_my_sql_schemas_async(
        self,
        request: adb_20211201_models.DescribeAdbMySqlSchemasRequest,
    ) -> adb_20211201_models.DescribeAdbMySqlSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_adb_my_sql_schemas_with_options_async(request, runtime)

    def describe_adb_my_sql_tables_with_options(
        self,
        request: adb_20211201_models.DescribeAdbMySqlTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAdbMySqlTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdbMySqlTables',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAdbMySqlTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_adb_my_sql_tables_with_options_async(
        self,
        request: adb_20211201_models.DescribeAdbMySqlTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAdbMySqlTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema):
            query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAdbMySqlTables',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAdbMySqlTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_adb_my_sql_tables(
        self,
        request: adb_20211201_models.DescribeAdbMySqlTablesRequest,
    ) -> adb_20211201_models.DescribeAdbMySqlTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_adb_my_sql_tables_with_options(request, runtime)

    async def describe_adb_my_sql_tables_async(
        self,
        request: adb_20211201_models.DescribeAdbMySqlTablesRequest,
    ) -> adb_20211201_models.DescribeAdbMySqlTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_adb_my_sql_tables_with_options_async(request, runtime)

    def describe_aps_action_logs_with_options(
        self,
        request: adb_20211201_models.DescribeApsActionLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeApsActionLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.stage):
            query['Stage'] = request.stage
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.workload_id):
            query['WorkloadId'] = request.workload_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApsActionLogs',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeApsActionLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aps_action_logs_with_options_async(
        self,
        request: adb_20211201_models.DescribeApsActionLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeApsActionLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.stage):
            query['Stage'] = request.stage
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.workload_id):
            query['WorkloadId'] = request.workload_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApsActionLogs',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeApsActionLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aps_action_logs(
        self,
        request: adb_20211201_models.DescribeApsActionLogsRequest,
    ) -> adb_20211201_models.DescribeApsActionLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_aps_action_logs_with_options(request, runtime)

    async def describe_aps_action_logs_async(
        self,
        request: adb_20211201_models.DescribeApsActionLogsRequest,
    ) -> adb_20211201_models.DescribeApsActionLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_aps_action_logs_with_options_async(request, runtime)

    def describe_aps_resource_groups_with_options(
        self,
        request: adb_20211201_models.DescribeApsResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeApsResourceGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeApsResourceGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeApsResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_aps_resource_groups_with_options_async(
        self,
        request: adb_20211201_models.DescribeApsResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeApsResourceGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeApsResourceGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeApsResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_aps_resource_groups(
        self,
        request: adb_20211201_models.DescribeApsResourceGroupsRequest,
    ) -> adb_20211201_models.DescribeApsResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_aps_resource_groups_with_options(request, runtime)

    async def describe_aps_resource_groups_async(
        self,
        request: adb_20211201_models.DescribeApsResourceGroupsRequest,
    ) -> adb_20211201_models.DescribeApsResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_aps_resource_groups_with_options_async(request, runtime)

    def describe_audit_log_config_with_options(
        self,
        request: adb_20211201_models.DescribeAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAuditLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditLogConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAuditLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_log_config_with_options_async(
        self,
        request: adb_20211201_models.DescribeAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAuditLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditLogConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAuditLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_log_config(
        self,
        request: adb_20211201_models.DescribeAuditLogConfigRequest,
    ) -> adb_20211201_models.DescribeAuditLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_log_config_with_options(request, runtime)

    async def describe_audit_log_config_async(
        self,
        request: adb_20211201_models.DescribeAuditLogConfigRequest,
    ) -> adb_20211201_models.DescribeAuditLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_log_config_with_options_async(request, runtime)

    def describe_audit_log_records_with_options(
        self,
        request: adb_20211201_models.DescribeAuditLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAuditLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.succeed):
            query['Succeed'] = request.succeed
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditLogRecords',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAuditLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_audit_log_records_with_options_async(
        self,
        request: adb_20211201_models.DescribeAuditLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeAuditLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.proxy_user):
            query['ProxyUser'] = request.proxy_user
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.sql_type):
            query['SqlType'] = request.sql_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.succeed):
            query['Succeed'] = request.succeed
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAuditLogRecords',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeAuditLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_audit_log_records(
        self,
        request: adb_20211201_models.DescribeAuditLogRecordsRequest,
    ) -> adb_20211201_models.DescribeAuditLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_audit_log_records_with_options(request, runtime)

    async def describe_audit_log_records_async(
        self,
        request: adb_20211201_models.DescribeAuditLogRecordsRequest,
    ) -> adb_20211201_models.DescribeAuditLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_audit_log_records_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: adb_20211201_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: adb_20211201_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: adb_20211201_models.DescribeBackupPolicyRequest,
    ) -> adb_20211201_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: adb_20211201_models.DescribeBackupPolicyRequest,
    ) -> adb_20211201_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: adb_20211201_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: adb_20211201_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: adb_20211201_models.DescribeBackupsRequest,
    ) -> adb_20211201_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: adb_20211201_models.DescribeBackupsRequest,
    ) -> adb_20211201_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_cluster_access_white_list_with_options(
        self,
        request: adb_20211201_models.DescribeClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeClusterAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterAccessWhiteList',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_access_white_list_with_options_async(
        self,
        request: adb_20211201_models.DescribeClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeClusterAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterAccessWhiteList',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_access_white_list(
        self,
        request: adb_20211201_models.DescribeClusterAccessWhiteListRequest,
    ) -> adb_20211201_models.DescribeClusterAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_access_white_list_with_options(request, runtime)

    async def describe_cluster_access_white_list_async(
        self,
        request: adb_20211201_models.DescribeClusterAccessWhiteListRequest,
    ) -> adb_20211201_models.DescribeClusterAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_access_white_list_with_options_async(request, runtime)

    def describe_cluster_net_info_with_options(
        self,
        request: adb_20211201_models.DescribeClusterNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeClusterNetInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterNetInfo',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeClusterNetInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_net_info_with_options_async(
        self,
        request: adb_20211201_models.DescribeClusterNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeClusterNetInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterNetInfo',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeClusterNetInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_net_info(
        self,
        request: adb_20211201_models.DescribeClusterNetInfoRequest,
    ) -> adb_20211201_models.DescribeClusterNetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_net_info_with_options(request, runtime)

    async def describe_cluster_net_info_async(
        self,
        request: adb_20211201_models.DescribeClusterNetInfoRequest,
    ) -> adb_20211201_models.DescribeClusterNetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_net_info_with_options_async(request, runtime)

    def describe_dbcluster_attribute_with_options(
        self,
        request: adb_20211201_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAttribute',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_attribute_with_options_async(
        self,
        request: adb_20211201_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAttribute',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_attribute(
        self,
        request: adb_20211201_models.DescribeDBClusterAttributeRequest,
    ) -> adb_20211201_models.DescribeDBClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_attribute_with_options(request, runtime)

    async def describe_dbcluster_attribute_async(
        self,
        request: adb_20211201_models.DescribeDBClusterAttributeRequest,
    ) -> adb_20211201_models.DescribeDBClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_attribute_with_options_async(request, runtime)

    def describe_dbcluster_forecast_with_options(
        self,
        request: adb_20211201_models.DescribeDBClusterForecastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterForecastResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterForecast',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterForecastResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_forecast_with_options_async(
        self,
        request: adb_20211201_models.DescribeDBClusterForecastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterForecastResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterForecast',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterForecastResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_forecast(
        self,
        request: adb_20211201_models.DescribeDBClusterForecastRequest,
    ) -> adb_20211201_models.DescribeDBClusterForecastResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_forecast_with_options(request, runtime)

    async def describe_dbcluster_forecast_async(
        self,
        request: adb_20211201_models.DescribeDBClusterForecastRequest,
    ) -> adb_20211201_models.DescribeDBClusterForecastResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_forecast_with_options_async(request, runtime)

    def describe_dbcluster_health_status_with_options(
        self,
        request: adb_20211201_models.DescribeDBClusterHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterHealthStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterHealthStatus',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_health_status_with_options_async(
        self,
        request: adb_20211201_models.DescribeDBClusterHealthStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterHealthStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterHealthStatus',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterHealthStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_health_status(
        self,
        request: adb_20211201_models.DescribeDBClusterHealthStatusRequest,
    ) -> adb_20211201_models.DescribeDBClusterHealthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_health_status_with_options(request, runtime)

    async def describe_dbcluster_health_status_async(
        self,
        request: adb_20211201_models.DescribeDBClusterHealthStatusRequest,
    ) -> adb_20211201_models.DescribeDBClusterHealthStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_health_status_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: adb_20211201_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: adb_20211201_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClusterPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_pools):
            query['ResourcePools'] = request.resource_pools
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClusterPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_performance(
        self,
        request: adb_20211201_models.DescribeDBClusterPerformanceRequest,
    ) -> adb_20211201_models.DescribeDBClusterPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: adb_20211201_models.DescribeDBClusterPerformanceRequest,
    ) -> adb_20211201_models.DescribeDBClusterPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def describe_dbclusters_with_options(
        self,
        request: adb_20211201_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusters',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbclusters_with_options_async(
        self,
        request: adb_20211201_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_ids):
            query['DBClusterIds'] = request.dbcluster_ids
        if not UtilClient.is_unset(request.dbcluster_status):
            query['DBClusterStatus'] = request.dbcluster_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBClusters',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbclusters(
        self,
        request: adb_20211201_models.DescribeDBClustersRequest,
    ) -> adb_20211201_models.DescribeDBClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbclusters_with_options(request, runtime)

    async def describe_dbclusters_async(
        self,
        request: adb_20211201_models.DescribeDBClustersRequest,
    ) -> adb_20211201_models.DescribeDBClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbclusters_with_options_async(request, runtime)

    def describe_dbresource_group_with_options(
        self,
        request: adb_20211201_models.DescribeDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbresource_group_with_options_async(
        self,
        request: adb_20211201_models.DescribeDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDBResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbresource_group(
        self,
        request: adb_20211201_models.DescribeDBResourceGroupRequest,
    ) -> adb_20211201_models.DescribeDBResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbresource_group_with_options(request, runtime)

    async def describe_dbresource_group_async(
        self,
        request: adb_20211201_models.DescribeDBResourceGroupRequest,
    ) -> adb_20211201_models.DescribeDBResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbresource_group_with_options_async(request, runtime)

    def describe_diagnosis_dimensions_with_options(
        self,
        request: adb_20211201_models.DescribeDiagnosisDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDiagnosisDimensionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisDimensions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDiagnosisDimensionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_dimensions_with_options_async(
        self,
        request: adb_20211201_models.DescribeDiagnosisDimensionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDiagnosisDimensionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisDimensions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDiagnosisDimensionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_dimensions(
        self,
        request: adb_20211201_models.DescribeDiagnosisDimensionsRequest,
    ) -> adb_20211201_models.DescribeDiagnosisDimensionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_dimensions_with_options(request, runtime)

    async def describe_diagnosis_dimensions_async(
        self,
        request: adb_20211201_models.DescribeDiagnosisDimensionsRequest,
    ) -> adb_20211201_models.DescribeDiagnosisDimensionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_dimensions_with_options_async(request, runtime)

    def describe_diagnosis_records_with_options(
        self,
        request: adb_20211201_models.DescribeDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDiagnosisRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_peak_memory):
            query['MaxPeakMemory'] = request.max_peak_memory
        if not UtilClient.is_unset(request.max_scan_size):
            query['MaxScanSize'] = request.max_scan_size
        if not UtilClient.is_unset(request.min_peak_memory):
            query['MinPeakMemory'] = request.min_peak_memory
        if not UtilClient.is_unset(request.min_scan_size):
            query['MinScanSize'] = request.min_scan_size
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisRecords',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_records_with_options_async(
        self,
        request: adb_20211201_models.DescribeDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDiagnosisRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_peak_memory):
            query['MaxPeakMemory'] = request.max_peak_memory
        if not UtilClient.is_unset(request.max_scan_size):
            query['MaxScanSize'] = request.max_scan_size
        if not UtilClient.is_unset(request.min_peak_memory):
            query['MinPeakMemory'] = request.min_peak_memory
        if not UtilClient.is_unset(request.min_scan_size):
            query['MinScanSize'] = request.min_scan_size
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisRecords',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDiagnosisRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_records(
        self,
        request: adb_20211201_models.DescribeDiagnosisRecordsRequest,
    ) -> adb_20211201_models.DescribeDiagnosisRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_records_with_options(request, runtime)

    async def describe_diagnosis_records_async(
        self,
        request: adb_20211201_models.DescribeDiagnosisRecordsRequest,
    ) -> adb_20211201_models.DescribeDiagnosisRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_records_with_options_async(request, runtime)

    def describe_diagnosis_sqlinfo_with_options(
        self,
        request: adb_20211201_models.DescribeDiagnosisSQLInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDiagnosisSQLInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisSQLInfo',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDiagnosisSQLInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnosis_sqlinfo_with_options_async(
        self,
        request: adb_20211201_models.DescribeDiagnosisSQLInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDiagnosisSQLInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosisSQLInfo',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDiagnosisSQLInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnosis_sqlinfo(
        self,
        request: adb_20211201_models.DescribeDiagnosisSQLInfoRequest,
    ) -> adb_20211201_models.DescribeDiagnosisSQLInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnosis_sqlinfo_with_options(request, runtime)

    async def describe_diagnosis_sqlinfo_async(
        self,
        request: adb_20211201_models.DescribeDiagnosisSQLInfoRequest,
    ) -> adb_20211201_models.DescribeDiagnosisSQLInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnosis_sqlinfo_with_options_async(request, runtime)

    def describe_download_records_with_options(
        self,
        request: adb_20211201_models.DescribeDownloadRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDownloadRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadRecords',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDownloadRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_download_records_with_options_async(
        self,
        request: adb_20211201_models.DescribeDownloadRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeDownloadRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDownloadRecords',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeDownloadRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_download_records(
        self,
        request: adb_20211201_models.DescribeDownloadRecordsRequest,
    ) -> adb_20211201_models.DescribeDownloadRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_download_records_with_options(request, runtime)

    async def describe_download_records_async(
        self,
        request: adb_20211201_models.DescribeDownloadRecordsRequest,
    ) -> adb_20211201_models.DescribeDownloadRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_download_records_with_options_async(request, runtime)

    def describe_pattern_performance_with_options(
        self,
        request: adb_20211201_models.DescribePatternPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribePatternPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePatternPerformance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribePatternPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pattern_performance_with_options_async(
        self,
        request: adb_20211201_models.DescribePatternPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribePatternPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePatternPerformance',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribePatternPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pattern_performance(
        self,
        request: adb_20211201_models.DescribePatternPerformanceRequest,
    ) -> adb_20211201_models.DescribePatternPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pattern_performance_with_options(request, runtime)

    async def describe_pattern_performance_async(
        self,
        request: adb_20211201_models.DescribePatternPerformanceRequest,
    ) -> adb_20211201_models.DescribePatternPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pattern_performance_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: adb_20211201_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: adb_20211201_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: adb_20211201_models.DescribeRegionsRequest,
    ) -> adb_20211201_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: adb_20211201_models.DescribeRegionsRequest,
    ) -> adb_20211201_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_sqlpattern_attribute_with_options(
        self,
        request: adb_20211201_models.DescribeSQLPatternAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSQLPatternAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLPatternAttribute',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSQLPatternAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlpattern_attribute_with_options_async(
        self,
        request: adb_20211201_models.DescribeSQLPatternAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSQLPatternAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.pattern_id):
            query['PatternId'] = request.pattern_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLPatternAttribute',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSQLPatternAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlpattern_attribute(
        self,
        request: adb_20211201_models.DescribeSQLPatternAttributeRequest,
    ) -> adb_20211201_models.DescribeSQLPatternAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlpattern_attribute_with_options(request, runtime)

    async def describe_sqlpattern_attribute_async(
        self,
        request: adb_20211201_models.DescribeSQLPatternAttributeRequest,
    ) -> adb_20211201_models.DescribeSQLPatternAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlpattern_attribute_with_options_async(request, runtime)

    def describe_sqlpatterns_with_options(
        self,
        request: adb_20211201_models.DescribeSQLPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSQLPatternsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLPatterns',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSQLPatternsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sqlpatterns_with_options_async(
        self,
        request: adb_20211201_models.DescribeSQLPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSQLPatternsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSQLPatterns',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSQLPatternsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sqlpatterns(
        self,
        request: adb_20211201_models.DescribeSQLPatternsRequest,
    ) -> adb_20211201_models.DescribeSQLPatternsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlpatterns_with_options(request, runtime)

    async def describe_sqlpatterns_async(
        self,
        request: adb_20211201_models.DescribeSQLPatternsRequest,
    ) -> adb_20211201_models.DescribeSQLPatternsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlpatterns_with_options_async(request, runtime)

    def describe_spark_code_log_with_options(
        self,
        request: adb_20211201_models.DescribeSparkCodeLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSparkCodeLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSparkCodeLog',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSparkCodeLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_code_log_with_options_async(
        self,
        request: adb_20211201_models.DescribeSparkCodeLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSparkCodeLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSparkCodeLog',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSparkCodeLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_code_log(
        self,
        request: adb_20211201_models.DescribeSparkCodeLogRequest,
    ) -> adb_20211201_models.DescribeSparkCodeLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_spark_code_log_with_options(request, runtime)

    async def describe_spark_code_log_async(
        self,
        request: adb_20211201_models.DescribeSparkCodeLogRequest,
    ) -> adb_20211201_models.DescribeSparkCodeLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_spark_code_log_with_options_async(request, runtime)

    def describe_spark_code_output_with_options(
        self,
        request: adb_20211201_models.DescribeSparkCodeOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSparkCodeOutputResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSparkCodeOutput',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSparkCodeOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_code_output_with_options_async(
        self,
        request: adb_20211201_models.DescribeSparkCodeOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSparkCodeOutputResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSparkCodeOutput',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSparkCodeOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_code_output(
        self,
        request: adb_20211201_models.DescribeSparkCodeOutputRequest,
    ) -> adb_20211201_models.DescribeSparkCodeOutputResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_spark_code_output_with_options(request, runtime)

    async def describe_spark_code_output_async(
        self,
        request: adb_20211201_models.DescribeSparkCodeOutputRequest,
    ) -> adb_20211201_models.DescribeSparkCodeOutputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_spark_code_output_with_options_async(request, runtime)

    def describe_spark_code_web_ui_with_options(
        self,
        request: adb_20211201_models.DescribeSparkCodeWebUiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSparkCodeWebUiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSparkCodeWebUi',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSparkCodeWebUiResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_spark_code_web_ui_with_options_async(
        self,
        request: adb_20211201_models.DescribeSparkCodeWebUiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSparkCodeWebUiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSparkCodeWebUi',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSparkCodeWebUiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_spark_code_web_ui(
        self,
        request: adb_20211201_models.DescribeSparkCodeWebUiRequest,
    ) -> adb_20211201_models.DescribeSparkCodeWebUiResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_spark_code_web_ui_with_options(request, runtime)

    async def describe_spark_code_web_ui_async(
        self,
        request: adb_20211201_models.DescribeSparkCodeWebUiRequest,
    ) -> adb_20211201_models.DescribeSparkCodeWebUiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_spark_code_web_ui_with_options_async(request, runtime)

    def describe_sql_pattern_with_options(
        self,
        request: adb_20211201_models.DescribeSqlPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSqlPatternResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sql_pattern):
            query['SqlPattern'] = request.sql_pattern
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSqlPattern',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSqlPatternResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_sql_pattern_with_options_async(
        self,
        request: adb_20211201_models.DescribeSqlPatternRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeSqlPatternResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sql_pattern):
            query['SqlPattern'] = request.sql_pattern
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSqlPattern',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeSqlPatternResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_sql_pattern(
        self,
        request: adb_20211201_models.DescribeSqlPatternRequest,
    ) -> adb_20211201_models.DescribeSqlPatternResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_pattern_with_options(request, runtime)

    async def describe_sql_pattern_async(
        self,
        request: adb_20211201_models.DescribeSqlPatternRequest,
    ) -> adb_20211201_models.DescribeSqlPatternResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sql_pattern_with_options_async(request, runtime)

    def describe_table_access_count_with_options(
        self,
        request: adb_20211201_models.DescribeTableAccessCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeTableAccessCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTableAccessCount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeTableAccessCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_table_access_count_with_options_async(
        self,
        request: adb_20211201_models.DescribeTableAccessCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DescribeTableAccessCountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTableAccessCount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DescribeTableAccessCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_table_access_count(
        self,
        request: adb_20211201_models.DescribeTableAccessCountRequest,
    ) -> adb_20211201_models.DescribeTableAccessCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_table_access_count_with_options(request, runtime)

    async def describe_table_access_count_async(
        self,
        request: adb_20211201_models.DescribeTableAccessCountRequest,
    ) -> adb_20211201_models.DescribeTableAccessCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_table_access_count_with_options_async(request, runtime)

    def download_diagnosis_records_with_options(
        self,
        request: adb_20211201_models.DownloadDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DownloadDiagnosisRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_peak_memory):
            query['MaxPeakMemory'] = request.max_peak_memory
        if not UtilClient.is_unset(request.max_scan_size):
            query['MaxScanSize'] = request.max_scan_size
        if not UtilClient.is_unset(request.min_peak_memory):
            query['MinPeakMemory'] = request.min_peak_memory
        if not UtilClient.is_unset(request.min_scan_size):
            query['MinScanSize'] = request.min_scan_size
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadDiagnosisRecords',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DownloadDiagnosisRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_diagnosis_records_with_options_async(
        self,
        request: adb_20211201_models.DownloadDiagnosisRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.DownloadDiagnosisRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.database):
            query['Database'] = request.database
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.max_peak_memory):
            query['MaxPeakMemory'] = request.max_peak_memory
        if not UtilClient.is_unset(request.max_scan_size):
            query['MaxScanSize'] = request.max_scan_size
        if not UtilClient.is_unset(request.min_peak_memory):
            query['MinPeakMemory'] = request.min_peak_memory
        if not UtilClient.is_unset(request.min_scan_size):
            query['MinScanSize'] = request.min_scan_size
        if not UtilClient.is_unset(request.query_condition):
            query['QueryCondition'] = request.query_condition
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group):
            query['ResourceGroup'] = request.resource_group
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DownloadDiagnosisRecords',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.DownloadDiagnosisRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_diagnosis_records(
        self,
        request: adb_20211201_models.DownloadDiagnosisRecordsRequest,
    ) -> adb_20211201_models.DownloadDiagnosisRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_diagnosis_records_with_options(request, runtime)

    async def download_diagnosis_records_async(
        self,
        request: adb_20211201_models.DownloadDiagnosisRecordsRequest,
    ) -> adb_20211201_models.DownloadDiagnosisRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_diagnosis_records_with_options_async(request, runtime)

    def get_lakehouse_valid_resource_groups_with_options(
        self,
        request: adb_20211201_models.GetLakehouseValidResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetLakehouseValidResourceGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.groups_info):
            query['GroupsInfo'] = request.groups_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLakehouseValidResourceGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetLakehouseValidResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_lakehouse_valid_resource_groups_with_options_async(
        self,
        request: adb_20211201_models.GetLakehouseValidResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetLakehouseValidResourceGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.groups_info):
            query['GroupsInfo'] = request.groups_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLakehouseValidResourceGroups',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetLakehouseValidResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_lakehouse_valid_resource_groups(
        self,
        request: adb_20211201_models.GetLakehouseValidResourceGroupsRequest,
    ) -> adb_20211201_models.GetLakehouseValidResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_lakehouse_valid_resource_groups_with_options(request, runtime)

    async def get_lakehouse_valid_resource_groups_async(
        self,
        request: adb_20211201_models.GetLakehouseValidResourceGroupsRequest,
    ) -> adb_20211201_models.GetLakehouseValidResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_lakehouse_valid_resource_groups_with_options_async(request, runtime)

    def get_spark_app_attempt_log_with_options(
        self,
        request: adb_20211201_models.GetSparkAppAttemptLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppAttemptLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attempt_id):
            body['AttemptId'] = request.attempt_id
        if not UtilClient.is_unset(request.log_length):
            body['LogLength'] = request.log_length
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppAttemptLog',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppAttemptLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_attempt_log_with_options_async(
        self,
        request: adb_20211201_models.GetSparkAppAttemptLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppAttemptLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.attempt_id):
            body['AttemptId'] = request.attempt_id
        if not UtilClient.is_unset(request.log_length):
            body['LogLength'] = request.log_length
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppAttemptLog',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppAttemptLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_attempt_log(
        self,
        request: adb_20211201_models.GetSparkAppAttemptLogRequest,
    ) -> adb_20211201_models.GetSparkAppAttemptLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_spark_app_attempt_log_with_options(request, runtime)

    async def get_spark_app_attempt_log_async(
        self,
        request: adb_20211201_models.GetSparkAppAttemptLogRequest,
    ) -> adb_20211201_models.GetSparkAppAttemptLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_app_attempt_log_with_options_async(request, runtime)

    def get_spark_app_info_with_options(
        self,
        request: adb_20211201_models.GetSparkAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppInfo',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_info_with_options_async(
        self,
        request: adb_20211201_models.GetSparkAppInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppInfoResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppInfo',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_info(
        self,
        request: adb_20211201_models.GetSparkAppInfoRequest,
    ) -> adb_20211201_models.GetSparkAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_spark_app_info_with_options(request, runtime)

    async def get_spark_app_info_async(
        self,
        request: adb_20211201_models.GetSparkAppInfoRequest,
    ) -> adb_20211201_models.GetSparkAppInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_app_info_with_options_async(request, runtime)

    def get_spark_app_log_with_options(
        self,
        request: adb_20211201_models.GetSparkAppLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.log_length):
            body['LogLength'] = request.log_length
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppLog',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_log_with_options_async(
        self,
        request: adb_20211201_models.GetSparkAppLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppLogResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.log_length):
            body['LogLength'] = request.log_length
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppLog',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_log(
        self,
        request: adb_20211201_models.GetSparkAppLogRequest,
    ) -> adb_20211201_models.GetSparkAppLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_spark_app_log_with_options(request, runtime)

    async def get_spark_app_log_async(
        self,
        request: adb_20211201_models.GetSparkAppLogRequest,
    ) -> adb_20211201_models.GetSparkAppLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_app_log_with_options_async(request, runtime)

    def get_spark_app_metrics_with_options(
        self,
        request: adb_20211201_models.GetSparkAppMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppMetricsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppMetrics',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_metrics_with_options_async(
        self,
        request: adb_20211201_models.GetSparkAppMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppMetricsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppMetrics',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_metrics(
        self,
        request: adb_20211201_models.GetSparkAppMetricsRequest,
    ) -> adb_20211201_models.GetSparkAppMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_spark_app_metrics_with_options(request, runtime)

    async def get_spark_app_metrics_async(
        self,
        request: adb_20211201_models.GetSparkAppMetricsRequest,
    ) -> adb_20211201_models.GetSparkAppMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_app_metrics_with_options_async(request, runtime)

    def get_spark_app_state_with_options(
        self,
        request: adb_20211201_models.GetSparkAppStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppStateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppState',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_state_with_options_async(
        self,
        request: adb_20211201_models.GetSparkAppStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppStateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppState',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_state(
        self,
        request: adb_20211201_models.GetSparkAppStateRequest,
    ) -> adb_20211201_models.GetSparkAppStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_spark_app_state_with_options(request, runtime)

    async def get_spark_app_state_async(
        self,
        request: adb_20211201_models.GetSparkAppStateRequest,
    ) -> adb_20211201_models.GetSparkAppStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_app_state_with_options_async(request, runtime)

    def get_spark_app_web_ui_address_with_options(
        self,
        request: adb_20211201_models.GetSparkAppWebUiAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppWebUiAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppWebUiAddress',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppWebUiAddressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_app_web_ui_address_with_options_async(
        self,
        request: adb_20211201_models.GetSparkAppWebUiAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkAppWebUiAddressResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkAppWebUiAddress',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkAppWebUiAddressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_app_web_ui_address(
        self,
        request: adb_20211201_models.GetSparkAppWebUiAddressRequest,
    ) -> adb_20211201_models.GetSparkAppWebUiAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_spark_app_web_ui_address_with_options(request, runtime)

    async def get_spark_app_web_ui_address_async(
        self,
        request: adb_20211201_models.GetSparkAppWebUiAddressRequest,
    ) -> adb_20211201_models.GetSparkAppWebUiAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_app_web_ui_address_with_options_async(request, runtime)

    def get_spark_config_log_path_with_options(
        self,
        request: adb_20211201_models.GetSparkConfigLogPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkConfigLogPathResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkConfigLogPath',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkConfigLogPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_config_log_path_with_options_async(
        self,
        request: adb_20211201_models.GetSparkConfigLogPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkConfigLogPathResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkConfigLogPath',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkConfigLogPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_config_log_path(
        self,
        request: adb_20211201_models.GetSparkConfigLogPathRequest,
    ) -> adb_20211201_models.GetSparkConfigLogPathResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_spark_config_log_path_with_options(request, runtime)

    async def get_spark_config_log_path_async(
        self,
        request: adb_20211201_models.GetSparkConfigLogPathRequest,
    ) -> adb_20211201_models.GetSparkConfigLogPathResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_config_log_path_with_options_async(request, runtime)

    def get_spark_log_analyze_task_with_options(
        self,
        request: adb_20211201_models.GetSparkLogAnalyzeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkLogAnalyzeTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkLogAnalyzeTask',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkLogAnalyzeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_log_analyze_task_with_options_async(
        self,
        request: adb_20211201_models.GetSparkLogAnalyzeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkLogAnalyzeTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkLogAnalyzeTask',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkLogAnalyzeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_log_analyze_task(
        self,
        request: adb_20211201_models.GetSparkLogAnalyzeTaskRequest,
    ) -> adb_20211201_models.GetSparkLogAnalyzeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_spark_log_analyze_task_with_options(request, runtime)

    async def get_spark_log_analyze_task_async(
        self,
        request: adb_20211201_models.GetSparkLogAnalyzeTaskRequest,
    ) -> adb_20211201_models.GetSparkLogAnalyzeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_log_analyze_task_with_options_async(request, runtime)

    def get_spark_sqlengine_state_with_options(
        self,
        request: adb_20211201_models.GetSparkSQLEngineStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkSQLEngineStateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkSQLEngineState',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkSQLEngineStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_sqlengine_state_with_options_async(
        self,
        request: adb_20211201_models.GetSparkSQLEngineStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkSQLEngineStateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkSQLEngineState',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkSQLEngineStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_sqlengine_state(
        self,
        request: adb_20211201_models.GetSparkSQLEngineStateRequest,
    ) -> adb_20211201_models.GetSparkSQLEngineStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_spark_sqlengine_state_with_options(request, runtime)

    async def get_spark_sqlengine_state_async(
        self,
        request: adb_20211201_models.GetSparkSQLEngineStateRequest,
    ) -> adb_20211201_models.GetSparkSQLEngineStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_sqlengine_state_with_options_async(request, runtime)

    def get_spark_template_file_content_with_options(
        self,
        request: adb_20211201_models.GetSparkTemplateFileContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkTemplateFileContentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkTemplateFileContent',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkTemplateFileContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_template_file_content_with_options_async(
        self,
        request: adb_20211201_models.GetSparkTemplateFileContentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkTemplateFileContentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkTemplateFileContent',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkTemplateFileContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_template_file_content(
        self,
        request: adb_20211201_models.GetSparkTemplateFileContentRequest,
    ) -> adb_20211201_models.GetSparkTemplateFileContentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_spark_template_file_content_with_options(request, runtime)

    async def get_spark_template_file_content_async(
        self,
        request: adb_20211201_models.GetSparkTemplateFileContentRequest,
    ) -> adb_20211201_models.GetSparkTemplateFileContentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_template_file_content_with_options_async(request, runtime)

    def get_spark_template_folder_tree_with_options(
        self,
        request: adb_20211201_models.GetSparkTemplateFolderTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkTemplateFolderTreeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkTemplateFolderTree',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkTemplateFolderTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_template_folder_tree_with_options_async(
        self,
        request: adb_20211201_models.GetSparkTemplateFolderTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkTemplateFolderTreeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkTemplateFolderTree',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkTemplateFolderTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_template_folder_tree(
        self,
        request: adb_20211201_models.GetSparkTemplateFolderTreeRequest,
    ) -> adb_20211201_models.GetSparkTemplateFolderTreeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_spark_template_folder_tree_with_options(request, runtime)

    async def get_spark_template_folder_tree_async(
        self,
        request: adb_20211201_models.GetSparkTemplateFolderTreeRequest,
    ) -> adb_20211201_models.GetSparkTemplateFolderTreeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_template_folder_tree_with_options_async(request, runtime)

    def get_spark_template_full_tree_with_options(
        self,
        request: adb_20211201_models.GetSparkTemplateFullTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkTemplateFullTreeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkTemplateFullTree',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkTemplateFullTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_spark_template_full_tree_with_options_async(
        self,
        request: adb_20211201_models.GetSparkTemplateFullTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetSparkTemplateFullTreeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSparkTemplateFullTree',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetSparkTemplateFullTreeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_spark_template_full_tree(
        self,
        request: adb_20211201_models.GetSparkTemplateFullTreeRequest,
    ) -> adb_20211201_models.GetSparkTemplateFullTreeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_spark_template_full_tree_with_options(request, runtime)

    async def get_spark_template_full_tree_async(
        self,
        request: adb_20211201_models.GetSparkTemplateFullTreeRequest,
    ) -> adb_20211201_models.GetSparkTemplateFullTreeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_spark_template_full_tree_with_options_async(request, runtime)

    def get_view_ddlwith_options(
        self,
        request: adb_20211201_models.GetViewDDLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetViewDDLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetViewDDL',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetViewDDLResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_view_ddlwith_options_async(
        self,
        request: adb_20211201_models.GetViewDDLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.GetViewDDLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.schema_name):
            query['SchemaName'] = request.schema_name
        if not UtilClient.is_unset(request.view_name):
            query['ViewName'] = request.view_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetViewDDL',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.GetViewDDLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_view_ddl(
        self,
        request: adb_20211201_models.GetViewDDLRequest,
    ) -> adb_20211201_models.GetViewDDLResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_view_ddlwith_options(request, runtime)

    async def get_view_ddl_async(
        self,
        request: adb_20211201_models.GetViewDDLRequest,
    ) -> adb_20211201_models.GetViewDDLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_view_ddlwith_options_async(request, runtime)

    def kill_spark_app_with_options(
        self,
        request: adb_20211201_models.KillSparkAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.KillSparkAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkApp',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.KillSparkAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_spark_app_with_options_async(
        self,
        request: adb_20211201_models.KillSparkAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.KillSparkAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkApp',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.KillSparkAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_spark_app(
        self,
        request: adb_20211201_models.KillSparkAppRequest,
    ) -> adb_20211201_models.KillSparkAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.kill_spark_app_with_options(request, runtime)

    async def kill_spark_app_async(
        self,
        request: adb_20211201_models.KillSparkAppRequest,
    ) -> adb_20211201_models.KillSparkAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kill_spark_app_with_options_async(request, runtime)

    def kill_spark_log_analyze_task_with_options(
        self,
        request: adb_20211201_models.KillSparkLogAnalyzeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.KillSparkLogAnalyzeTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkLogAnalyzeTask',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.KillSparkLogAnalyzeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_spark_log_analyze_task_with_options_async(
        self,
        request: adb_20211201_models.KillSparkLogAnalyzeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.KillSparkLogAnalyzeTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkLogAnalyzeTask',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.KillSparkLogAnalyzeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_spark_log_analyze_task(
        self,
        request: adb_20211201_models.KillSparkLogAnalyzeTaskRequest,
    ) -> adb_20211201_models.KillSparkLogAnalyzeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.kill_spark_log_analyze_task_with_options(request, runtime)

    async def kill_spark_log_analyze_task_async(
        self,
        request: adb_20211201_models.KillSparkLogAnalyzeTaskRequest,
    ) -> adb_20211201_models.KillSparkLogAnalyzeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kill_spark_log_analyze_task_with_options_async(request, runtime)

    def kill_spark_sqlengine_with_options(
        self,
        request: adb_20211201_models.KillSparkSQLEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.KillSparkSQLEngineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkSQLEngine',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.KillSparkSQLEngineResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_spark_sqlengine_with_options_async(
        self,
        request: adb_20211201_models.KillSparkSQLEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.KillSparkSQLEngineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='KillSparkSQLEngine',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.KillSparkSQLEngineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_spark_sqlengine(
        self,
        request: adb_20211201_models.KillSparkSQLEngineRequest,
    ) -> adb_20211201_models.KillSparkSQLEngineResponse:
        runtime = util_models.RuntimeOptions()
        return self.kill_spark_sqlengine_with_options(request, runtime)

    async def kill_spark_sqlengine_async(
        self,
        request: adb_20211201_models.KillSparkSQLEngineRequest,
    ) -> adb_20211201_models.KillSparkSQLEngineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kill_spark_sqlengine_with_options_async(request, runtime)

    def list_spark_app_attempts_with_options(
        self,
        request: adb_20211201_models.ListSparkAppAttemptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkAppAttemptsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSparkAppAttempts',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkAppAttemptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_app_attempts_with_options_async(
        self,
        request: adb_20211201_models.ListSparkAppAttemptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkAppAttemptsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSparkAppAttempts',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkAppAttemptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_app_attempts(
        self,
        request: adb_20211201_models.ListSparkAppAttemptsRequest,
    ) -> adb_20211201_models.ListSparkAppAttemptsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_spark_app_attempts_with_options(request, runtime)

    async def list_spark_app_attempts_async(
        self,
        request: adb_20211201_models.ListSparkAppAttemptsRequest,
    ) -> adb_20211201_models.ListSparkAppAttemptsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_spark_app_attempts_with_options_async(request, runtime)

    def list_spark_apps_with_options(
        self,
        request: adb_20211201_models.ListSparkAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSparkApps',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_apps_with_options_async(
        self,
        request: adb_20211201_models.ListSparkAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSparkApps',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_apps(
        self,
        request: adb_20211201_models.ListSparkAppsRequest,
    ) -> adb_20211201_models.ListSparkAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_spark_apps_with_options(request, runtime)

    async def list_spark_apps_async(
        self,
        request: adb_20211201_models.ListSparkAppsRequest,
    ) -> adb_20211201_models.ListSparkAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_spark_apps_with_options_async(request, runtime)

    def list_spark_log_analyze_tasks_with_options(
        self,
        request: adb_20211201_models.ListSparkLogAnalyzeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkLogAnalyzeTasksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSparkLogAnalyzeTasks',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkLogAnalyzeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_log_analyze_tasks_with_options_async(
        self,
        request: adb_20211201_models.ListSparkLogAnalyzeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkLogAnalyzeTasksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSparkLogAnalyzeTasks',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkLogAnalyzeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_log_analyze_tasks(
        self,
        request: adb_20211201_models.ListSparkLogAnalyzeTasksRequest,
    ) -> adb_20211201_models.ListSparkLogAnalyzeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_spark_log_analyze_tasks_with_options(request, runtime)

    async def list_spark_log_analyze_tasks_async(
        self,
        request: adb_20211201_models.ListSparkLogAnalyzeTasksRequest,
    ) -> adb_20211201_models.ListSparkLogAnalyzeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_spark_log_analyze_tasks_with_options_async(request, runtime)

    def list_spark_template_file_ids_with_options(
        self,
        request: adb_20211201_models.ListSparkTemplateFileIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkTemplateFileIdsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSparkTemplateFileIds',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkTemplateFileIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_spark_template_file_ids_with_options_async(
        self,
        request: adb_20211201_models.ListSparkTemplateFileIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ListSparkTemplateFileIdsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSparkTemplateFileIds',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ListSparkTemplateFileIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_spark_template_file_ids(
        self,
        request: adb_20211201_models.ListSparkTemplateFileIdsRequest,
    ) -> adb_20211201_models.ListSparkTemplateFileIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_spark_template_file_ids_with_options(request, runtime)

    async def list_spark_template_file_ids_async(
        self,
        request: adb_20211201_models.ListSparkTemplateFileIdsRequest,
    ) -> adb_20211201_models.ListSparkTemplateFileIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_spark_template_file_ids_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: adb_20211201_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: adb_20211201_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: adb_20211201_models.ModifyAccountDescriptionRequest,
    ) -> adb_20211201_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: adb_20211201_models.ModifyAccountDescriptionRequest,
    ) -> adb_20211201_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_audit_log_config_with_options(
        self,
        request: adb_20211201_models.ModifyAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyAuditLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_log_status):
            query['AuditLogStatus'] = request.audit_log_status
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAuditLogConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyAuditLogConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_audit_log_config_with_options_async(
        self,
        request: adb_20211201_models.ModifyAuditLogConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyAuditLogConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audit_log_status):
            query['AuditLogStatus'] = request.audit_log_status
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAuditLogConfig',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyAuditLogConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_audit_log_config(
        self,
        request: adb_20211201_models.ModifyAuditLogConfigRequest,
    ) -> adb_20211201_models.ModifyAuditLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_audit_log_config_with_options(request, runtime)

    async def modify_audit_log_config_async(
        self,
        request: adb_20211201_models.ModifyAuditLogConfigRequest,
    ) -> adb_20211201_models.ModifyAuditLogConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_audit_log_config_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: adb_20211201_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: adb_20211201_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: adb_20211201_models.ModifyBackupPolicyRequest,
    ) -> adb_20211201_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: adb_20211201_models.ModifyBackupPolicyRequest,
    ) -> adb_20211201_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_cluster_access_white_list_with_options(
        self,
        request: adb_20211201_models.ModifyClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyClusterAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_iparray_attribute):
            query['DBClusterIPArrayAttribute'] = request.dbcluster_iparray_attribute
        if not UtilClient.is_unset(request.dbcluster_iparray_name):
            query['DBClusterIPArrayName'] = request.dbcluster_iparray_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterAccessWhiteList',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_access_white_list_with_options_async(
        self,
        request: adb_20211201_models.ModifyClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyClusterAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_iparray_attribute):
            query['DBClusterIPArrayAttribute'] = request.dbcluster_iparray_attribute
        if not UtilClient.is_unset(request.dbcluster_iparray_name):
            query['DBClusterIPArrayName'] = request.dbcluster_iparray_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.security_ips):
            query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterAccessWhiteList',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_access_white_list(
        self,
        request: adb_20211201_models.ModifyClusterAccessWhiteListRequest,
    ) -> adb_20211201_models.ModifyClusterAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_access_white_list_with_options(request, runtime)

    async def modify_cluster_access_white_list_async(
        self,
        request: adb_20211201_models.ModifyClusterAccessWhiteListRequest,
    ) -> adb_20211201_models.ModifyClusterAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_access_white_list_with_options_async(request, runtime)

    def modify_cluster_connection_string_with_options(
        self,
        request: adb_20211201_models.ModifyClusterConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyClusterConnectionStringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterConnectionString',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyClusterConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_connection_string_with_options_async(
        self,
        request: adb_20211201_models.ModifyClusterConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyClusterConnectionStringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.current_connection_string):
            query['CurrentConnectionString'] = request.current_connection_string
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyClusterConnectionString',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyClusterConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_cluster_connection_string(
        self,
        request: adb_20211201_models.ModifyClusterConnectionStringRequest,
    ) -> adb_20211201_models.ModifyClusterConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_connection_string_with_options(request, runtime)

    async def modify_cluster_connection_string_async(
        self,
        request: adb_20211201_models.ModifyClusterConnectionStringRequest,
    ) -> adb_20211201_models.ModifyClusterConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_connection_string_with_options_async(request, runtime)

    def modify_dbcluster_with_options(
        self,
        request: adb_20211201_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_with_options_async(
        self,
        request: adb_20211201_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.compute_resource):
            query['ComputeResource'] = request.compute_resource
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.storage_resource):
            query['StorageResource'] = request.storage_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster(
        self,
        request: adb_20211201_models.ModifyDBClusterRequest,
    ) -> adb_20211201_models.ModifyDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_with_options(request, runtime)

    async def modify_dbcluster_async(
        self,
        request: adb_20211201_models.ModifyDBClusterRequest,
    ) -> adb_20211201_models.ModifyDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_with_options_async(request, runtime)

    def modify_dbcluster_description_with_options(
        self,
        request: adb_20211201_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBClusterDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBClusterDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_description_with_options_async(
        self,
        request: adb_20211201_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBClusterDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_description):
            query['DBClusterDescription'] = request.dbcluster_description
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterDescription',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBClusterDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_description(
        self,
        request: adb_20211201_models.ModifyDBClusterDescriptionRequest,
    ) -> adb_20211201_models.ModifyDBClusterDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_description_with_options(request, runtime)

    async def modify_dbcluster_description_async(
        self,
        request: adb_20211201_models.ModifyDBClusterDescriptionRequest,
    ) -> adb_20211201_models.ModifyDBClusterDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_description_with_options_async(request, runtime)

    def modify_dbcluster_maintain_time_with_options(
        self,
        request: adb_20211201_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBClusterMaintainTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMaintainTime',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBClusterMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_maintain_time_with_options_async(
        self,
        request: adb_20211201_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBClusterMaintainTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMaintainTime',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBClusterMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_maintain_time(
        self,
        request: adb_20211201_models.ModifyDBClusterMaintainTimeRequest,
    ) -> adb_20211201_models.ModifyDBClusterMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_maintain_time_with_options(request, runtime)

    async def modify_dbcluster_maintain_time_async(
        self,
        request: adb_20211201_models.ModifyDBClusterMaintainTimeRequest,
    ) -> adb_20211201_models.ModifyDBClusterMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_maintain_time_with_options_async(request, runtime)

    def modify_dbresource_group_with_options(
        self,
        request: adb_20211201_models.ModifyDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not UtilClient.is_unset(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbresource_group_with_options_async(
        self,
        request: adb_20211201_models.ModifyDBResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ModifyDBResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.max_compute_resource):
            query['MaxComputeResource'] = request.max_compute_resource
        if not UtilClient.is_unset(request.min_compute_resource):
            query['MinComputeResource'] = request.min_compute_resource
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBResourceGroup',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ModifyDBResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbresource_group(
        self,
        request: adb_20211201_models.ModifyDBResourceGroupRequest,
    ) -> adb_20211201_models.ModifyDBResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbresource_group_with_options(request, runtime)

    async def modify_dbresource_group_async(
        self,
        request: adb_20211201_models.ModifyDBResourceGroupRequest,
    ) -> adb_20211201_models.ModifyDBResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbresource_group_with_options_async(request, runtime)

    def preload_spark_app_metrics_with_options(
        self,
        request: adb_20211201_models.PreloadSparkAppMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.PreloadSparkAppMetricsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PreloadSparkAppMetrics',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.PreloadSparkAppMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def preload_spark_app_metrics_with_options_async(
        self,
        request: adb_20211201_models.PreloadSparkAppMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.PreloadSparkAppMetricsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PreloadSparkAppMetrics',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.PreloadSparkAppMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preload_spark_app_metrics(
        self,
        request: adb_20211201_models.PreloadSparkAppMetricsRequest,
    ) -> adb_20211201_models.PreloadSparkAppMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.preload_spark_app_metrics_with_options(request, runtime)

    async def preload_spark_app_metrics_async(
        self,
        request: adb_20211201_models.PreloadSparkAppMetricsRequest,
    ) -> adb_20211201_models.PreloadSparkAppMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.preload_spark_app_metrics_with_options_async(request, runtime)

    def release_cluster_public_connection_with_options(
        self,
        request: adb_20211201_models.ReleaseClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ReleaseClusterPublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseClusterPublicConnection',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ReleaseClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cluster_public_connection_with_options_async(
        self,
        request: adb_20211201_models.ReleaseClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ReleaseClusterPublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseClusterPublicConnection',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ReleaseClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_cluster_public_connection(
        self,
        request: adb_20211201_models.ReleaseClusterPublicConnectionRequest,
    ) -> adb_20211201_models.ReleaseClusterPublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_public_connection_with_options(request, runtime)

    async def release_cluster_public_connection_async(
        self,
        request: adb_20211201_models.ReleaseClusterPublicConnectionRequest,
    ) -> adb_20211201_models.ReleaseClusterPublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_cluster_public_connection_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: adb_20211201_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: adb_20211201_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_description):
            query['AccountDescription'] = request.account_description
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            query['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: adb_20211201_models.ResetAccountPasswordRequest,
    ) -> adb_20211201_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: adb_20211201_models.ResetAccountPasswordRequest,
    ) -> adb_20211201_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def set_spark_app_log_root_path_with_options(
        self,
        request: adb_20211201_models.SetSparkAppLogRootPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.SetSparkAppLogRootPathResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.oss_log_path):
            body['OssLogPath'] = request.oss_log_path
        if not UtilClient.is_unset(request.use_default_oss):
            body['UseDefaultOss'] = request.use_default_oss
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetSparkAppLogRootPath',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.SetSparkAppLogRootPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_spark_app_log_root_path_with_options_async(
        self,
        request: adb_20211201_models.SetSparkAppLogRootPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.SetSparkAppLogRootPathResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.oss_log_path):
            body['OssLogPath'] = request.oss_log_path
        if not UtilClient.is_unset(request.use_default_oss):
            body['UseDefaultOss'] = request.use_default_oss
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetSparkAppLogRootPath',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.SetSparkAppLogRootPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_spark_app_log_root_path(
        self,
        request: adb_20211201_models.SetSparkAppLogRootPathRequest,
    ) -> adb_20211201_models.SetSparkAppLogRootPathResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_spark_app_log_root_path_with_options(request, runtime)

    async def set_spark_app_log_root_path_async(
        self,
        request: adb_20211201_models.SetSparkAppLogRootPathRequest,
    ) -> adb_20211201_models.SetSparkAppLogRootPathResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_spark_app_log_root_path_with_options_async(request, runtime)

    def start_spark_sqlengine_with_options(
        self,
        request: adb_20211201_models.StartSparkSQLEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.StartSparkSQLEngineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.jars):
            body['Jars'] = request.jars
        if not UtilClient.is_unset(request.max_executor):
            body['MaxExecutor'] = request.max_executor
        if not UtilClient.is_unset(request.min_executor):
            body['MinExecutor'] = request.min_executor
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.slot_num):
            body['SlotNum'] = request.slot_num
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSparkSQLEngine',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.StartSparkSQLEngineResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_spark_sqlengine_with_options_async(
        self,
        request: adb_20211201_models.StartSparkSQLEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.StartSparkSQLEngineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.jars):
            body['Jars'] = request.jars
        if not UtilClient.is_unset(request.max_executor):
            body['MaxExecutor'] = request.max_executor
        if not UtilClient.is_unset(request.min_executor):
            body['MinExecutor'] = request.min_executor
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.slot_num):
            body['SlotNum'] = request.slot_num
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartSparkSQLEngine',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.StartSparkSQLEngineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_spark_sqlengine(
        self,
        request: adb_20211201_models.StartSparkSQLEngineRequest,
    ) -> adb_20211201_models.StartSparkSQLEngineResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_spark_sqlengine_with_options(request, runtime)

    async def start_spark_sqlengine_async(
        self,
        request: adb_20211201_models.StartSparkSQLEngineRequest,
    ) -> adb_20211201_models.StartSparkSQLEngineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_spark_sqlengine_with_options_async(request, runtime)

    def submit_spark_app_with_options(
        self,
        request: adb_20211201_models.SubmitSparkAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.SubmitSparkAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_source):
            body['AgentSource'] = request.agent_source
        if not UtilClient.is_unset(request.agent_version):
            body['AgentVersion'] = request.agent_version
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.template_file_id):
            body['TemplateFileId'] = request.template_file_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSparkApp',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.SubmitSparkAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_spark_app_with_options_async(
        self,
        request: adb_20211201_models.SubmitSparkAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.SubmitSparkAppResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.agent_source):
            body['AgentSource'] = request.agent_source
        if not UtilClient.is_unset(request.agent_version):
            body['AgentVersion'] = request.agent_version
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.app_type):
            body['AppType'] = request.app_type
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.template_file_id):
            body['TemplateFileId'] = request.template_file_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSparkApp',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.SubmitSparkAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_spark_app(
        self,
        request: adb_20211201_models.SubmitSparkAppRequest,
    ) -> adb_20211201_models.SubmitSparkAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_spark_app_with_options(request, runtime)

    async def submit_spark_app_async(
        self,
        request: adb_20211201_models.SubmitSparkAppRequest,
    ) -> adb_20211201_models.SubmitSparkAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_spark_app_with_options_async(request, runtime)

    def submit_spark_log_analyze_task_with_options(
        self,
        request: adb_20211201_models.SubmitSparkLogAnalyzeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.SubmitSparkLogAnalyzeTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSparkLogAnalyzeTask',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.SubmitSparkLogAnalyzeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_spark_log_analyze_task_with_options_async(
        self,
        request: adb_20211201_models.SubmitSparkLogAnalyzeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.SubmitSparkLogAnalyzeTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitSparkLogAnalyzeTask',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.SubmitSparkLogAnalyzeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_spark_log_analyze_task(
        self,
        request: adb_20211201_models.SubmitSparkLogAnalyzeTaskRequest,
    ) -> adb_20211201_models.SubmitSparkLogAnalyzeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_spark_log_analyze_task_with_options(request, runtime)

    async def submit_spark_log_analyze_task_async(
        self,
        request: adb_20211201_models.SubmitSparkLogAnalyzeTaskRequest,
    ) -> adb_20211201_models.SubmitSparkLogAnalyzeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_spark_log_analyze_task_with_options_async(request, runtime)

    def unbind_account_with_options(
        self,
        request: adb_20211201_models.UnbindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.UnbindAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.UnbindAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_account_with_options_async(
        self,
        request: adb_20211201_models.UnbindAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.UnbindAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name):
            query['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindAccount',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.UnbindAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_account(
        self,
        request: adb_20211201_models.UnbindAccountRequest,
    ) -> adb_20211201_models.UnbindAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_account_with_options(request, runtime)

    async def unbind_account_async(
        self,
        request: adb_20211201_models.UnbindAccountRequest,
    ) -> adb_20211201_models.UnbindAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_account_with_options_async(request, runtime)

    def update_spark_template_file_with_options(
        self,
        request: adb_20211201_models.UpdateSparkTemplateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.UpdateSparkTemplateFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSparkTemplateFile',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.UpdateSparkTemplateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_spark_template_file_with_options_async(
        self,
        request: adb_20211201_models.UpdateSparkTemplateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adb_20211201_models.UpdateSparkTemplateFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.dbcluster_id):
            body['DBClusterId'] = request.dbcluster_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.resource_group_name):
            body['ResourceGroupName'] = request.resource_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSparkTemplateFile',
            version='2021-12-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adb_20211201_models.UpdateSparkTemplateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_spark_template_file(
        self,
        request: adb_20211201_models.UpdateSparkTemplateFileRequest,
    ) -> adb_20211201_models.UpdateSparkTemplateFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_spark_template_file_with_options(request, runtime)

    async def update_spark_template_file_async(
        self,
        request: adb_20211201_models.UpdateSparkTemplateFileRequest,
    ) -> adb_20211201_models.UpdateSparkTemplateFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_spark_template_file_with_options_async(request, runtime)
