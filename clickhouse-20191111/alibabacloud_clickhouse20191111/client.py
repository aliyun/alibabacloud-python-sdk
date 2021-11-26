# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_clickhouse20191111 import models as clickhouse_20191111_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def allocate_cluster_public_connection_with_options(
        self,
        request: clickhouse_20191111_models.AllocateClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.AllocateClusterPublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AllocateClusterPublicConnection',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.AllocateClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_cluster_public_connection_with_options_async(
        self,
        request: clickhouse_20191111_models.AllocateClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.AllocateClusterPublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConnectionStringPrefix'] = request.connection_string_prefix
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AllocateClusterPublicConnection',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.AllocateClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_cluster_public_connection(
        self,
        request: clickhouse_20191111_models.AllocateClusterPublicConnectionRequest,
    ) -> clickhouse_20191111_models.AllocateClusterPublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_cluster_public_connection_with_options(request, runtime)

    async def allocate_cluster_public_connection_async(
        self,
        request: clickhouse_20191111_models.AllocateClusterPublicConnectionRequest,
    ) -> clickhouse_20191111_models.AllocateClusterPublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_cluster_public_connection_with_options_async(request, runtime)

    def check_clickhouse_to_rdswith_options(
        self,
        request: clickhouse_20191111_models.CheckClickhouseToRDSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckClickhouseToRDSResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CkPassword'] = request.ck_password
        query['CkUserName'] = request.ck_user_name
        query['ClickhousePort'] = request.clickhouse_port
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['RdsVpcId'] = request.rds_vpc_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckClickhouseToRDS',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckClickhouseToRDSResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_clickhouse_to_rdswith_options_async(
        self,
        request: clickhouse_20191111_models.CheckClickhouseToRDSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckClickhouseToRDSResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CkPassword'] = request.ck_password
        query['CkUserName'] = request.ck_user_name
        query['ClickhousePort'] = request.clickhouse_port
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['RdsVpcId'] = request.rds_vpc_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckClickhouseToRDS',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckClickhouseToRDSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_clickhouse_to_rds(
        self,
        request: clickhouse_20191111_models.CheckClickhouseToRDSRequest,
    ) -> clickhouse_20191111_models.CheckClickhouseToRDSResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_clickhouse_to_rdswith_options(request, runtime)

    async def check_clickhouse_to_rds_async(
        self,
        request: clickhouse_20191111_models.CheckClickhouseToRDSRequest,
    ) -> clickhouse_20191111_models.CheckClickhouseToRDSResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_clickhouse_to_rdswith_options_async(request, runtime)

    def check_scale_out_balanced_with_options(
        self,
        request: clickhouse_20191111_models.CheckScaleOutBalancedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckScaleOutBalancedResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckScaleOutBalanced',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckScaleOutBalancedResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_scale_out_balanced_with_options_async(
        self,
        request: clickhouse_20191111_models.CheckScaleOutBalancedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckScaleOutBalancedResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckScaleOutBalanced',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckScaleOutBalancedResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_scale_out_balanced(
        self,
        request: clickhouse_20191111_models.CheckScaleOutBalancedRequest,
    ) -> clickhouse_20191111_models.CheckScaleOutBalancedResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_scale_out_balanced_with_options(request, runtime)

    async def check_scale_out_balanced_async(
        self,
        request: clickhouse_20191111_models.CheckScaleOutBalancedRequest,
    ) -> clickhouse_20191111_models.CheckScaleOutBalancedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_scale_out_balanced_with_options_async(request, runtime)

    def check_service_linked_role_with_options(
        self,
        request: clickhouse_20191111_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRole',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_with_options_async(
        self,
        request: clickhouse_20191111_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRole',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role(
        self,
        request: clickhouse_20191111_models.CheckServiceLinkedRoleRequest,
    ) -> clickhouse_20191111_models.CheckServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    async def check_service_linked_role_async(
        self,
        request: clickhouse_20191111_models.CheckServiceLinkedRoleRequest,
    ) -> clickhouse_20191111_models.CheckServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_with_options_async(request, runtime)

    def check_version_transfer_with_options(
        self,
        request: clickhouse_20191111_models.CheckVersionTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckVersionTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CheckAccount'] = request.check_account
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SourceAccount'] = request.source_account
        query['SourcePassword'] = request.source_password
        query['TargetAccount'] = request.target_account
        query['TargetDbClusterId'] = request.target_db_cluster_id
        query['TargetPassword'] = request.target_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckVersionTransfer',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckVersionTransferResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_version_transfer_with_options_async(
        self,
        request: clickhouse_20191111_models.CheckVersionTransferRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CheckVersionTransferResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CheckAccount'] = request.check_account
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SourceAccount'] = request.source_account
        query['SourcePassword'] = request.source_password
        query['TargetAccount'] = request.target_account
        query['TargetDbClusterId'] = request.target_db_cluster_id
        query['TargetPassword'] = request.target_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CheckVersionTransfer',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CheckVersionTransferResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_version_transfer(
        self,
        request: clickhouse_20191111_models.CheckVersionTransferRequest,
    ) -> clickhouse_20191111_models.CheckVersionTransferResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_version_transfer_with_options(request, runtime)

    async def check_version_transfer_async(
        self,
        request: clickhouse_20191111_models.CheckVersionTransferRequest,
    ) -> clickhouse_20191111_models.CheckVersionTransferResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_version_transfer_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: clickhouse_20191111_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDescription'] = request.account_description
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDescription'] = request.account_description
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: clickhouse_20191111_models.CreateAccountRequest,
    ) -> clickhouse_20191111_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: clickhouse_20191111_models.CreateAccountRequest,
    ) -> clickhouse_20191111_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_account_and_authority_with_options(
        self,
        request: clickhouse_20191111_models.CreateAccountAndAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateAccountAndAuthorityResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDescription'] = request.account_description
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['AllowDatabases'] = request.allow_databases
        query['AllowDictionaries'] = request.allow_dictionaries
        query['DBClusterId'] = request.dbcluster_id
        query['DdlAuthority'] = request.ddl_authority
        query['DmlAuthority'] = request.dml_authority
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TotalDatabases'] = request.total_databases
        query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccountAndAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountAndAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_and_authority_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateAccountAndAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateAccountAndAuthorityResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDescription'] = request.account_description
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['AllowDatabases'] = request.allow_databases
        query['AllowDictionaries'] = request.allow_dictionaries
        query['DBClusterId'] = request.dbcluster_id
        query['DdlAuthority'] = request.ddl_authority
        query['DmlAuthority'] = request.dml_authority
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TotalDatabases'] = request.total_databases
        query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccountAndAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateAccountAndAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account_and_authority(
        self,
        request: clickhouse_20191111_models.CreateAccountAndAuthorityRequest,
    ) -> clickhouse_20191111_models.CreateAccountAndAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_and_authority_with_options(request, runtime)

    async def create_account_and_authority_async(
        self,
        request: clickhouse_20191111_models.CreateAccountAndAuthorityRequest,
    ) -> clickhouse_20191111_models.CreateAccountAndAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_and_authority_with_options_async(request, runtime)

    def create_backup_policy_with_options(
        self,
        request: clickhouse_20191111_models.CreateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BackupRetentionPeriod'] = request.backup_retention_period
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PreferredBackupPeriod'] = request.preferred_backup_period
        query['PreferredBackupTime'] = request.preferred_backup_time
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_policy_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BackupRetentionPeriod'] = request.backup_retention_period
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PreferredBackupPeriod'] = request.preferred_backup_period
        query['PreferredBackupTime'] = request.preferred_backup_time
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup_policy(
        self,
        request: clickhouse_20191111_models.CreateBackupPolicyRequest,
    ) -> clickhouse_20191111_models.CreateBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_policy_with_options(request, runtime)

    async def create_backup_policy_async(
        self,
        request: clickhouse_20191111_models.CreateBackupPolicyRequest,
    ) -> clickhouse_20191111_models.CreateBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_policy_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: clickhouse_20191111_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['DBClusterCategory'] = request.dbcluster_category
        query['DBClusterClass'] = request.dbcluster_class
        query['DBClusterDescription'] = request.dbcluster_description
        query['DBClusterNetworkType'] = request.dbcluster_network_type
        query['DBClusterVersion'] = request.dbcluster_version
        query['DBNodeGroupCount'] = request.dbnode_group_count
        query['DBNodeStorage'] = request.dbnode_storage
        query['DbNodeStorageType'] = request.db_node_storage_type
        query['EncryptionKey'] = request.encryption_key
        query['EncryptionType'] = request.encryption_type
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UsedTime'] = request.used_time
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['DBClusterCategory'] = request.dbcluster_category
        query['DBClusterClass'] = request.dbcluster_class
        query['DBClusterDescription'] = request.dbcluster_description
        query['DBClusterNetworkType'] = request.dbcluster_network_type
        query['DBClusterVersion'] = request.dbcluster_version
        query['DBNodeGroupCount'] = request.dbnode_group_count
        query['DBNodeStorage'] = request.dbnode_storage
        query['DbNodeStorageType'] = request.db_node_storage_type
        query['EncryptionKey'] = request.encryption_key
        query['EncryptionType'] = request.encryption_type
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PayType'] = request.pay_type
        query['Period'] = request.period
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UsedTime'] = request.used_time
        query['VPCId'] = request.vpcid
        query['VSwitchId'] = request.v_switch_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance(
        self,
        request: clickhouse_20191111_models.CreateDBInstanceRequest,
    ) -> clickhouse_20191111_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: clickhouse_20191111_models.CreateDBInstanceRequest,
    ) -> clickhouse_20191111_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_ossstorage_with_options(
        self,
        request: clickhouse_20191111_models.CreateOSSStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateOSSStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateOSSStorage',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateOSSStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ossstorage_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateOSSStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateOSSStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateOSSStorage',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateOSSStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ossstorage(
        self,
        request: clickhouse_20191111_models.CreateOSSStorageRequest,
    ) -> clickhouse_20191111_models.CreateOSSStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ossstorage_with_options(request, runtime)

    async def create_ossstorage_async(
        self,
        request: clickhouse_20191111_models.CreateOSSStorageRequest,
    ) -> clickhouse_20191111_models.CreateOSSStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ossstorage_with_options_async(request, runtime)

    def create_ports_for_click_house_with_options(
        self,
        request: clickhouse_20191111_models.CreatePortsForClickHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreatePortsForClickHouseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PortType'] = request.port_type
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePortsForClickHouse',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreatePortsForClickHouseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ports_for_click_house_with_options_async(
        self,
        request: clickhouse_20191111_models.CreatePortsForClickHouseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreatePortsForClickHouseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PortType'] = request.port_type
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePortsForClickHouse',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreatePortsForClickHouseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ports_for_click_house(
        self,
        request: clickhouse_20191111_models.CreatePortsForClickHouseRequest,
    ) -> clickhouse_20191111_models.CreatePortsForClickHouseResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ports_for_click_house_with_options(request, runtime)

    async def create_ports_for_click_house_async(
        self,
        request: clickhouse_20191111_models.CreatePortsForClickHouseRequest,
    ) -> clickhouse_20191111_models.CreatePortsForClickHouseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ports_for_click_house_with_options_async(request, runtime)

    def create_rdsto_clickhouse_db_with_options(
        self,
        request: clickhouse_20191111_models.CreateRDSToClickhouseDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateRDSToClickhouseDbResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CkPassword'] = request.ck_password
        query['CkUserName'] = request.ck_user_name
        query['ClickhousePort'] = request.clickhouse_port
        query['DbClusterId'] = request.db_cluster_id
        query['LimitUpper'] = request.limit_upper
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['RdsVpcId'] = request.rds_vpc_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SkipUnsupported'] = request.skip_unsupported
        query['SynDbTables'] = request.syn_db_tables
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRDSToClickhouseDb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateRDSToClickhouseDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rdsto_clickhouse_db_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateRDSToClickhouseDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateRDSToClickhouseDbResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CkPassword'] = request.ck_password
        query['CkUserName'] = request.ck_user_name
        query['ClickhousePort'] = request.clickhouse_port
        query['DbClusterId'] = request.db_cluster_id
        query['LimitUpper'] = request.limit_upper
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['RdsVpcId'] = request.rds_vpc_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SkipUnsupported'] = request.skip_unsupported
        query['SynDbTables'] = request.syn_db_tables
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateRDSToClickhouseDb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateRDSToClickhouseDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rdsto_clickhouse_db(
        self,
        request: clickhouse_20191111_models.CreateRDSToClickhouseDbRequest,
    ) -> clickhouse_20191111_models.CreateRDSToClickhouseDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rdsto_clickhouse_db_with_options(request, runtime)

    async def create_rdsto_clickhouse_db_async(
        self,
        request: clickhouse_20191111_models.CreateRDSToClickhouseDbRequest,
    ) -> clickhouse_20191111_models.CreateRDSToClickhouseDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rdsto_clickhouse_db_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: clickhouse_20191111_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: clickhouse_20191111_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.CreateServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_linked_role(
        self,
        request: clickhouse_20191111_models.CreateServiceLinkedRoleRequest,
    ) -> clickhouse_20191111_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: clickhouse_20191111_models.CreateServiceLinkedRoleRequest,
    ) -> clickhouse_20191111_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: clickhouse_20191111_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: clickhouse_20191111_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: clickhouse_20191111_models.DeleteAccountRequest,
    ) -> clickhouse_20191111_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: clickhouse_20191111_models.DeleteAccountRequest,
    ) -> clickhouse_20191111_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_dbcluster_with_options(
        self,
        request: clickhouse_20191111_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteDBClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbcluster_with_options_async(
        self,
        request: clickhouse_20191111_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteDBClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDBCluster',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbcluster(
        self,
        request: clickhouse_20191111_models.DeleteDBClusterRequest,
    ) -> clickhouse_20191111_models.DeleteDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    async def delete_dbcluster_async(
        self,
        request: clickhouse_20191111_models.DeleteDBClusterRequest,
    ) -> clickhouse_20191111_models.DeleteDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbcluster_with_options_async(request, runtime)

    def delete_lorne_task_with_options(
        self,
        request: clickhouse_20191111_models.DeleteLorneTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteLorneTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLorneTask',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteLorneTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_lorne_task_with_options_async(
        self,
        request: clickhouse_20191111_models.DeleteLorneTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteLorneTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLorneTask',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteLorneTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_lorne_task(
        self,
        request: clickhouse_20191111_models.DeleteLorneTaskRequest,
    ) -> clickhouse_20191111_models.DeleteLorneTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_lorne_task_with_options(request, runtime)

    async def delete_lorne_task_async(
        self,
        request: clickhouse_20191111_models.DeleteLorneTaskRequest,
    ) -> clickhouse_20191111_models.DeleteLorneTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_lorne_task_with_options_async(request, runtime)

    def delete_syndb_with_options(
        self,
        request: clickhouse_20191111_models.DeleteSyndbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteSyndbResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SynDb'] = request.syn_db
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSyndb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteSyndbResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_syndb_with_options_async(
        self,
        request: clickhouse_20191111_models.DeleteSyndbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DeleteSyndbResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SynDb'] = request.syn_db
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSyndb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DeleteSyndbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_syndb(
        self,
        request: clickhouse_20191111_models.DeleteSyndbRequest,
    ) -> clickhouse_20191111_models.DeleteSyndbResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_syndb_with_options(request, runtime)

    async def delete_syndb_async(
        self,
        request: clickhouse_20191111_models.DeleteSyndbRequest,
    ) -> clickhouse_20191111_models.DeleteSyndbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_syndb_with_options_async(request, runtime)

    def describe_account_authority_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAccountAuthorityResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccountAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_authority_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAccountAuthorityResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccountAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_authority(
        self,
        request: clickhouse_20191111_models.DescribeAccountAuthorityRequest,
    ) -> clickhouse_20191111_models.DescribeAccountAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_account_authority_with_options(request, runtime)

    async def describe_account_authority_async(
        self,
        request: clickhouse_20191111_models.DescribeAccountAuthorityRequest,
    ) -> clickhouse_20191111_models.DescribeAccountAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_authority_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: clickhouse_20191111_models.DescribeAccountsRequest,
    ) -> clickhouse_20191111_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: clickhouse_20191111_models.DescribeAccountsRequest,
    ) -> clickhouse_20191111_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_all_data_source_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAllDataSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSource',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_data_source_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAllDataSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSource',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_data_source(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourceRequest,
    ) -> clickhouse_20191111_models.DescribeAllDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_source_with_options(request, runtime)

    async def describe_all_data_source_async(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourceRequest,
    ) -> clickhouse_20191111_models.DescribeAllDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_data_source_with_options_async(request, runtime)

    def describe_all_data_sources_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAllDataSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSources',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_all_data_sources_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAllDataSourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAllDataSources',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAllDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_all_data_sources(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourcesRequest,
    ) -> clickhouse_20191111_models.DescribeAllDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_all_data_sources_with_options(request, runtime)

    async def describe_all_data_sources_async(
        self,
        request: clickhouse_20191111_models.DescribeAllDataSourcesRequest,
    ) -> clickhouse_20191111_models.DescribeAllDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_all_data_sources_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: clickhouse_20191111_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AcceptLanguage'] = request.accept_language
        query['ChargeType'] = request.charge_type
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AcceptLanguage'] = request.accept_language
        query['ChargeType'] = request.charge_type
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_available_resource(
        self,
        request: clickhouse_20191111_models.DescribeAvailableResourceRequest,
    ) -> clickhouse_20191111_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: clickhouse_20191111_models.DescribeAvailableResourceRequest,
    ) -> clickhouse_20191111_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: clickhouse_20191111_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: clickhouse_20191111_models.DescribeBackupPolicyRequest,
    ) -> clickhouse_20191111_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: clickhouse_20191111_models.DescribeBackupPolicyRequest,
    ) -> clickhouse_20191111_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: clickhouse_20191111_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BackupId'] = request.backup_id
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BackupId'] = request.backup_id
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: clickhouse_20191111_models.DescribeBackupsRequest,
    ) -> clickhouse_20191111_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: clickhouse_20191111_models.DescribeBackupsRequest,
    ) -> clickhouse_20191111_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_columns_with_options(
        self,
        request: clickhouse_20191111_models.DescribeColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeColumnsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeColumns',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_columns_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeColumnsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeColumnsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeColumns',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_columns(
        self,
        request: clickhouse_20191111_models.DescribeColumnsRequest,
    ) -> clickhouse_20191111_models.DescribeColumnsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_columns_with_options(request, runtime)

    async def describe_columns_async(
        self,
        request: clickhouse_20191111_models.DescribeColumnsRequest,
    ) -> clickhouse_20191111_models.DescribeColumnsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_columns_with_options_async(request, runtime)

    def describe_dbcluster_access_white_list_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAccessWhiteList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_access_white_list_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAccessWhiteList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_access_white_list(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAccessWhiteListRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_access_white_list_with_options(request, runtime)

    async def describe_dbcluster_access_white_list_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAccessWhiteListRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_access_white_list_with_options_async(request, runtime)

    def describe_dbcluster_attribute_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAttribute',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_attribute_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterAttribute',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_attribute(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAttributeRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_attribute_with_options(request, runtime)

    async def describe_dbcluster_attribute_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterAttributeRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_attribute_with_options_async(request, runtime)

    def describe_dbcluster_config_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_config_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_config(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_config_with_options(request, runtime)

    async def describe_dbcluster_config_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterConfigRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_config_with_options_async(request, runtime)

    def describe_dbcluster_net_info_items_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterNetInfoItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterNetInfoItems',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_net_info_items_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterNetInfoItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterNetInfoItems',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_net_info_items(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterNetInfoItemsRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_net_info_items_with_options(request, runtime)

    async def describe_dbcluster_net_info_items_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterNetInfoItemsRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterNetInfoItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_net_info_items_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['Key'] = request.key
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterPerformanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClusterPerformanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['Key'] = request.key
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusterPerformance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClusterPerformanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbcluster_performance(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterPerformanceRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClusterPerformanceRequest,
    ) -> clickhouse_20191111_models.DescribeDBClusterPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def describe_dbclusters_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterDescription'] = request.dbcluster_description
        query['DBClusterIds'] = request.dbcluster_ids
        query['DBClusterStatus'] = request.dbcluster_status
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusters',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbclusters_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterDescription'] = request.dbcluster_description
        query['DBClusterIds'] = request.dbcluster_ids
        query['DBClusterStatus'] = request.dbcluster_status
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBClusters',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbclusters(
        self,
        request: clickhouse_20191111_models.DescribeDBClustersRequest,
    ) -> clickhouse_20191111_models.DescribeDBClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbclusters_with_options(request, runtime)

    async def describe_dbclusters_async(
        self,
        request: clickhouse_20191111_models.DescribeDBClustersRequest,
    ) -> clickhouse_20191111_models.DescribeDBClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbclusters_with_options_async(request, runtime)

    def describe_dbconfig_with_options(
        self,
        request: clickhouse_20191111_models.DescribeDBConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbconfig_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeDBConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeDBConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDBConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeDBConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbconfig(
        self,
        request: clickhouse_20191111_models.DescribeDBConfigRequest,
    ) -> clickhouse_20191111_models.DescribeDBConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbconfig_with_options(request, runtime)

    async def describe_dbconfig_async(
        self,
        request: clickhouse_20191111_models.DescribeDBConfigRequest,
    ) -> clickhouse_20191111_models.DescribeDBConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbconfig_with_options_async(request, runtime)

    def describe_log_hub_attribute_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLogHubAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLogHubAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['DeliverName'] = request.deliver_name
        query['LogStoreName'] = request.log_store_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ProjectName'] = request.project_name
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogHubAttribute',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLogHubAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_hub_attribute_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLogHubAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLogHubAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['DeliverName'] = request.deliver_name
        query['LogStoreName'] = request.log_store_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ProjectName'] = request.project_name
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogHubAttribute',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLogHubAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_hub_attribute(
        self,
        request: clickhouse_20191111_models.DescribeLogHubAttributeRequest,
    ) -> clickhouse_20191111_models.DescribeLogHubAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_hub_attribute_with_options(request, runtime)

    async def describe_log_hub_attribute_async(
        self,
        request: clickhouse_20191111_models.DescribeLogHubAttributeRequest,
    ) -> clickhouse_20191111_models.DescribeLogHubAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_hub_attribute_with_options_async(request, runtime)

    def describe_log_store_keys_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLogStoreKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLogStoreKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        query['LogStoreName'] = request.log_store_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ProjectName'] = request.project_name
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogStoreKeys',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLogStoreKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_store_keys_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLogStoreKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLogStoreKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        query['LogStoreName'] = request.log_store_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ProjectName'] = request.project_name
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLogStoreKeys',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLogStoreKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_store_keys(
        self,
        request: clickhouse_20191111_models.DescribeLogStoreKeysRequest,
    ) -> clickhouse_20191111_models.DescribeLogStoreKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_store_keys_with_options(request, runtime)

    async def describe_log_store_keys_async(
        self,
        request: clickhouse_20191111_models.DescribeLogStoreKeysRequest,
    ) -> clickhouse_20191111_models.DescribeLogStoreKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_store_keys_with_options_async(request, runtime)

    def describe_loghub_detail_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLoghubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLoghubDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ExportName'] = request.export_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ProjectName'] = request.project_name
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLoghubDetail',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLoghubDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_loghub_detail_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLoghubDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLoghubDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ExportName'] = request.export_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ProjectName'] = request.project_name
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLoghubDetail',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLoghubDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_loghub_detail(
        self,
        request: clickhouse_20191111_models.DescribeLoghubDetailRequest,
    ) -> clickhouse_20191111_models.DescribeLoghubDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_loghub_detail_with_options(request, runtime)

    async def describe_loghub_detail_async(
        self,
        request: clickhouse_20191111_models.DescribeLoghubDetailRequest,
    ) -> clickhouse_20191111_models.DescribeLoghubDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_loghub_detail_with_options_async(request, runtime)

    def describe_lorne_log_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLorneLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLorneLog',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lorne_log_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLorneLog',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lorne_log(
        self,
        request: clickhouse_20191111_models.DescribeLorneLogRequest,
    ) -> clickhouse_20191111_models.DescribeLorneLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_log_with_options(request, runtime)

    async def describe_lorne_log_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneLogRequest,
    ) -> clickhouse_20191111_models.DescribeLorneLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_lorne_log_with_options_async(request, runtime)

    def describe_lorne_tasks_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLorneTasks',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lorne_tasks_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLorneTasks',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lorne_tasks(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksRequest,
    ) -> clickhouse_20191111_models.DescribeLorneTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_tasks_with_options(request, runtime)

    async def describe_lorne_tasks_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksRequest,
    ) -> clickhouse_20191111_models.DescribeLorneTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_lorne_tasks_with_options_async(request, runtime)

    def describe_lorne_tasks_mcount_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMCountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['MetricName'] = request.metric_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLorneTasksMCount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksMCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lorne_tasks_mcount_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMCountResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['MetricName'] = request.metric_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLorneTasksMCount',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksMCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lorne_tasks_mcount(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMCountRequest,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_tasks_mcount_with_options(request, runtime)

    async def describe_lorne_tasks_mcount_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMCountRequest,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_lorne_tasks_mcount_with_options_async(request, runtime)

    def describe_lorne_tasks_metrics_with_options(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['MetricName'] = request.metric_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLorneTasksMetrics',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lorne_tasks_metrics_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMetricsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['MetricName'] = request.metric_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLorneTasksMetrics',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeLorneTasksMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lorne_tasks_metrics(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMetricsRequest,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_lorne_tasks_metrics_with_options(request, runtime)

    async def describe_lorne_tasks_metrics_async(
        self,
        request: clickhouse_20191111_models.DescribeLorneTasksMetricsRequest,
    ) -> clickhouse_20191111_models.DescribeLorneTasksMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_lorne_tasks_metrics_with_options_async(request, runtime)

    def describe_ossstorage_with_options(
        self,
        request: clickhouse_20191111_models.DescribeOSSStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeOSSStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOSSStorage',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeOSSStorageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ossstorage_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeOSSStorageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeOSSStorageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeOSSStorage',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeOSSStorageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ossstorage(
        self,
        request: clickhouse_20191111_models.DescribeOSSStorageRequest,
    ) -> clickhouse_20191111_models.DescribeOSSStorageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ossstorage_with_options(request, runtime)

    async def describe_ossstorage_async(
        self,
        request: clickhouse_20191111_models.DescribeOSSStorageRequest,
    ) -> clickhouse_20191111_models.DescribeOSSStorageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ossstorage_with_options_async(request, runtime)

    def describe_process_list_with_options(
        self,
        request: clickhouse_20191111_models.DescribeProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeProcessListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['InitialQueryId'] = request.initial_query_id
        query['InitialUser'] = request.initial_user
        query['Keyword'] = request.keyword
        query['Order'] = request.order
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['QueryDurationMs'] = request.query_duration_ms
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeProcessList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeProcessListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_process_list_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeProcessListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['InitialQueryId'] = request.initial_query_id
        query['InitialUser'] = request.initial_user
        query['Keyword'] = request.keyword
        query['Order'] = request.order
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['QueryDurationMs'] = request.query_duration_ms
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeProcessList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeProcessListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_process_list(
        self,
        request: clickhouse_20191111_models.DescribeProcessListRequest,
    ) -> clickhouse_20191111_models.DescribeProcessListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_process_list_with_options(request, runtime)

    async def describe_process_list_async(
        self,
        request: clickhouse_20191111_models.DescribeProcessListRequest,
    ) -> clickhouse_20191111_models.DescribeProcessListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_process_list_with_options_async(request, runtime)

    def describe_rdstables_with_options(
        self,
        request: clickhouse_20191111_models.DescribeRDSTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeRDSTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRDSTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRDSTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rdstables_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeRDSTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeRDSTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Schema'] = request.schema
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRDSTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRDSTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rdstables(
        self,
        request: clickhouse_20191111_models.DescribeRDSTablesRequest,
    ) -> clickhouse_20191111_models.DescribeRDSTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rdstables_with_options(request, runtime)

    async def describe_rdstables_async(
        self,
        request: clickhouse_20191111_models.DescribeRDSTablesRequest,
    ) -> clickhouse_20191111_models.DescribeRDSTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rdstables_with_options_async(request, runtime)

    def describe_rdsvpc_with_options(
        self,
        request: clickhouse_20191111_models.DescribeRDSVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeRDSVpcResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRDSVpc',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRDSVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rdsvpc_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeRDSVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeRDSVpcResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRDSVpc',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRDSVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rdsvpc(
        self,
        request: clickhouse_20191111_models.DescribeRDSVpcRequest,
    ) -> clickhouse_20191111_models.DescribeRDSVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rdsvpc_with_options(request, runtime)

    async def describe_rdsvpc_async(
        self,
        request: clickhouse_20191111_models.DescribeRDSVpcRequest,
    ) -> clickhouse_20191111_models.DescribeRDSVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rdsvpc_with_options_async(request, runtime)

    def describe_rdsschemas_with_options(
        self,
        request: clickhouse_20191111_models.DescribeRDSschemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeRDSschemasResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRDSschemas',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRDSschemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rdsschemas_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeRDSschemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeRDSschemasResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRDSschemas',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRDSschemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rdsschemas(
        self,
        request: clickhouse_20191111_models.DescribeRDSschemasRequest,
    ) -> clickhouse_20191111_models.DescribeRDSschemasResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rdsschemas_with_options(request, runtime)

    async def describe_rdsschemas_async(
        self,
        request: clickhouse_20191111_models.DescribeRDSschemasRequest,
    ) -> clickhouse_20191111_models.DescribeRDSschemasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rdsschemas_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: clickhouse_20191111_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: clickhouse_20191111_models.DescribeRegionsRequest,
    ) -> clickhouse_20191111_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: clickhouse_20191111_models.DescribeRegionsRequest,
    ) -> clickhouse_20191111_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_schemas_with_options(
        self,
        request: clickhouse_20191111_models.DescribeSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSchemasResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSchemas',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSchemasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_schemas_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeSchemasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSchemasResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSchemas',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSchemasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_schemas(
        self,
        request: clickhouse_20191111_models.DescribeSchemasRequest,
    ) -> clickhouse_20191111_models.DescribeSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_schemas_with_options(request, runtime)

    async def describe_schemas_async(
        self,
        request: clickhouse_20191111_models.DescribeSchemasRequest,
    ) -> clickhouse_20191111_models.DescribeSchemasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_schemas_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['QueryDurationMs'] = request.query_duration_ms
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['QueryDurationMs'] = request.query_duration_ms
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogRecordsRequest,
    ) -> clickhouse_20191111_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogRecordsRequest,
    ) -> clickhouse_20191111_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_slow_log_trend_with_options(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSlowLogTrendResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['QueryDurationMs'] = request.query_duration_ms
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogTrend',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_trend_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSlowLogTrendResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['EndTime'] = request.end_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['QueryDurationMs'] = request.query_duration_ms
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogTrend',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSlowLogTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_trend(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogTrendRequest,
    ) -> clickhouse_20191111_models.DescribeSlowLogTrendResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_trend_with_options(request, runtime)

    async def describe_slow_log_trend_async(
        self,
        request: clickhouse_20191111_models.DescribeSlowLogTrendRequest,
    ) -> clickhouse_20191111_models.DescribeSlowLogTrendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_trend_with_options_async(request, runtime)

    def describe_syn_db_tables_with_options(
        self,
        request: clickhouse_20191111_models.DescribeSynDbTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSynDbTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SynDb'] = request.syn_db
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSynDbTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSynDbTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_syn_db_tables_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeSynDbTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSynDbTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SynDb'] = request.syn_db
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSynDbTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSynDbTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_syn_db_tables(
        self,
        request: clickhouse_20191111_models.DescribeSynDbTablesRequest,
    ) -> clickhouse_20191111_models.DescribeSynDbTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_syn_db_tables_with_options(request, runtime)

    async def describe_syn_db_tables_async(
        self,
        request: clickhouse_20191111_models.DescribeSynDbTablesRequest,
    ) -> clickhouse_20191111_models.DescribeSynDbTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_syn_db_tables_with_options_async(request, runtime)

    def describe_syn_dbs_with_options(
        self,
        request: clickhouse_20191111_models.DescribeSynDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSynDbsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSynDbs',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSynDbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_syn_dbs_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeSynDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeSynDbsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSynDbs',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeSynDbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_syn_dbs(
        self,
        request: clickhouse_20191111_models.DescribeSynDbsRequest,
    ) -> clickhouse_20191111_models.DescribeSynDbsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_syn_dbs_with_options(request, runtime)

    async def describe_syn_dbs_async(
        self,
        request: clickhouse_20191111_models.DescribeSynDbsRequest,
    ) -> clickhouse_20191111_models.DescribeSynDbsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_syn_dbs_with_options_async(request, runtime)

    def describe_tables_with_options(
        self,
        request: clickhouse_20191111_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tables_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tables(
        self,
        request: clickhouse_20191111_models.DescribeTablesRequest,
    ) -> clickhouse_20191111_models.DescribeTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    async def describe_tables_async(
        self,
        request: clickhouse_20191111_models.DescribeTablesRequest,
    ) -> clickhouse_20191111_models.DescribeTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tables_with_options_async(request, runtime)

    def describe_transfer_history_with_options(
        self,
        request: clickhouse_20191111_models.DescribeTransferHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeTransferHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTransferHistory',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeTransferHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_transfer_history_with_options_async(
        self,
        request: clickhouse_20191111_models.DescribeTransferHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.DescribeTransferHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeTransferHistory',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.DescribeTransferHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_transfer_history(
        self,
        request: clickhouse_20191111_models.DescribeTransferHistoryRequest,
    ) -> clickhouse_20191111_models.DescribeTransferHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_transfer_history_with_options(request, runtime)

    async def describe_transfer_history_async(
        self,
        request: clickhouse_20191111_models.DescribeTransferHistoryRequest,
    ) -> clickhouse_20191111_models.DescribeTransferHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_transfer_history_with_options_async(request, runtime)

    def kill_process_with_options(
        self,
        request: clickhouse_20191111_models.KillProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.KillProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['InitialQueryId'] = request.initial_query_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='KillProcess',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.KillProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_process_with_options_async(
        self,
        request: clickhouse_20191111_models.KillProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.KillProcessResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['InitialQueryId'] = request.initial_query_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='KillProcess',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.KillProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_process(
        self,
        request: clickhouse_20191111_models.KillProcessRequest,
    ) -> clickhouse_20191111_models.KillProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.kill_process_with_options(request, runtime)

    async def kill_process_async(
        self,
        request: clickhouse_20191111_models.KillProcessRequest,
    ) -> clickhouse_20191111_models.KillProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kill_process_with_options_async(request, runtime)

    def modify_account_authority_with_options(
        self,
        request: clickhouse_20191111_models.ModifyAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyAccountAuthorityResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['AllowDatabases'] = request.allow_databases
        query['AllowDictionaries'] = request.allow_dictionaries
        query['DBClusterId'] = request.dbcluster_id
        query['DdlAuthority'] = request.ddl_authority
        query['DmlAuthority'] = request.dml_authority
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TotalDatabases'] = request.total_databases
        query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccountAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_authority_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyAccountAuthorityResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['AllowDatabases'] = request.allow_databases
        query['AllowDictionaries'] = request.allow_dictionaries
        query['DBClusterId'] = request.dbcluster_id
        query['DdlAuthority'] = request.ddl_authority
        query['DmlAuthority'] = request.dml_authority
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TotalDatabases'] = request.total_databases
        query['TotalDictionaries'] = request.total_dictionaries
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccountAuthority',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_authority(
        self,
        request: clickhouse_20191111_models.ModifyAccountAuthorityRequest,
    ) -> clickhouse_20191111_models.ModifyAccountAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_authority_with_options(request, runtime)

    async def modify_account_authority_async(
        self,
        request: clickhouse_20191111_models.ModifyAccountAuthorityRequest,
    ) -> clickhouse_20191111_models.ModifyAccountAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_authority_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: clickhouse_20191111_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDescription'] = request.account_description
        query['AccountName'] = request.account_name
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountDescription'] = request.account_description
        query['AccountName'] = request.account_name
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: clickhouse_20191111_models.ModifyAccountDescriptionRequest,
    ) -> clickhouse_20191111_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: clickhouse_20191111_models.ModifyAccountDescriptionRequest,
    ) -> clickhouse_20191111_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: clickhouse_20191111_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BackupRetentionPeriod'] = request.backup_retention_period
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PreferredBackupPeriod'] = request.preferred_backup_period
        query['PreferredBackupTime'] = request.preferred_backup_time
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BackupRetentionPeriod'] = request.backup_retention_period
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PreferredBackupPeriod'] = request.preferred_backup_period
        query['PreferredBackupTime'] = request.preferred_backup_time
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: clickhouse_20191111_models.ModifyBackupPolicyRequest,
    ) -> clickhouse_20191111_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: clickhouse_20191111_models.ModifyBackupPolicyRequest,
    ) -> clickhouse_20191111_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_dbcluster_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterClass'] = request.dbcluster_class
        query['DBClusterId'] = request.dbcluster_id
        query['DBNodeGroupCount'] = request.dbnode_group_count
        query['DBNodeStorage'] = request.dbnode_storage
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterClass'] = request.dbcluster_class
        query['DBClusterId'] = request.dbcluster_id
        query['DBNodeGroupCount'] = request.dbnode_group_count
        query['DBNodeStorage'] = request.dbnode_storage
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBCluster',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_with_options(request, runtime)

    async def modify_dbcluster_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_with_options_async(request, runtime)

    def modify_dbcluster_access_white_list_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterIPArrayAttribute'] = request.dbcluster_iparray_attribute
        query['DBClusterIPArrayName'] = request.dbcluster_iparray_name
        query['DBClusterId'] = request.dbcluster_id
        query['ModifyMode'] = request.modify_mode
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterAccessWhiteList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_access_white_list_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterIPArrayAttribute'] = request.dbcluster_iparray_attribute
        query['DBClusterIPArrayName'] = request.dbcluster_iparray_name
        query['DBClusterId'] = request.dbcluster_id
        query['ModifyMode'] = request.modify_mode
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SecurityIps'] = request.security_ips
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterAccessWhiteList',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_access_white_list(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterAccessWhiteListRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_access_white_list_with_options(request, runtime)

    async def modify_dbcluster_access_white_list_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterAccessWhiteListRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_access_white_list_with_options_async(request, runtime)

    def modify_dbcluster_config_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_config_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_config(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_config_with_options(request, runtime)

    async def modify_dbcluster_config_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterConfigRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_config_with_options_async(request, runtime)

    def modify_dbcluster_description_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterDescription'] = request.dbcluster_description
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterDescription',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_description_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterDescriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterDescription'] = request.dbcluster_description
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterDescription',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_description(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterDescriptionRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_description_with_options(request, runtime)

    async def modify_dbcluster_description_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterDescriptionRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_description_with_options_async(request, runtime)

    def modify_dbcluster_maintain_time_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['MaintainTime'] = request.maintain_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMaintainTime',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbcluster_maintain_time_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['MaintainTime'] = request.maintain_time
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBClusterMaintainTime',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbcluster_maintain_time(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterMaintainTimeRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_maintain_time_with_options(request, runtime)

    async def modify_dbcluster_maintain_time_async(
        self,
        request: clickhouse_20191111_models.ModifyDBClusterMaintainTimeRequest,
    ) -> clickhouse_20191111_models.ModifyDBClusterMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_maintain_time_with_options_async(request, runtime)

    def modify_dbconfig_with_options(
        self,
        request: clickhouse_20191111_models.ModifyDBConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Config'] = request.config
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbconfig_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyDBConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyDBConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Config'] = request.config
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyDBConfig',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyDBConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbconfig(
        self,
        request: clickhouse_20191111_models.ModifyDBConfigRequest,
    ) -> clickhouse_20191111_models.ModifyDBConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbconfig_with_options(request, runtime)

    async def modify_dbconfig_async(
        self,
        request: clickhouse_20191111_models.ModifyDBConfigRequest,
    ) -> clickhouse_20191111_models.ModifyDBConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbconfig_with_options_async(request, runtime)

    def modify_rdsto_clickhouse_db_with_options(
        self,
        request: clickhouse_20191111_models.ModifyRDSToClickhouseDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyRDSToClickhouseDbResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CkPassword'] = request.ck_password
        query['CkUserName'] = request.ck_user_name
        query['ClickhousePort'] = request.clickhouse_port
        query['DbClusterId'] = request.db_cluster_id
        query['LimitUpper'] = request.limit_upper
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsSynDb'] = request.rds_syn_db
        query['RdsSynTables'] = request.rds_syn_tables
        query['RdsUserName'] = request.rds_user_name
        query['RdsVpcId'] = request.rds_vpc_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SkipUnsupported'] = request.skip_unsupported
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyRDSToClickhouseDb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyRDSToClickhouseDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_rdsto_clickhouse_db_with_options_async(
        self,
        request: clickhouse_20191111_models.ModifyRDSToClickhouseDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ModifyRDSToClickhouseDbResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CkPassword'] = request.ck_password
        query['CkUserName'] = request.ck_user_name
        query['ClickhousePort'] = request.clickhouse_port
        query['DbClusterId'] = request.db_cluster_id
        query['LimitUpper'] = request.limit_upper
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsSynDb'] = request.rds_syn_db
        query['RdsSynTables'] = request.rds_syn_tables
        query['RdsUserName'] = request.rds_user_name
        query['RdsVpcId'] = request.rds_vpc_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SkipUnsupported'] = request.skip_unsupported
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyRDSToClickhouseDb',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ModifyRDSToClickhouseDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_rdsto_clickhouse_db(
        self,
        request: clickhouse_20191111_models.ModifyRDSToClickhouseDbRequest,
    ) -> clickhouse_20191111_models.ModifyRDSToClickhouseDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_rdsto_clickhouse_db_with_options(request, runtime)

    async def modify_rdsto_clickhouse_db_async(
        self,
        request: clickhouse_20191111_models.ModifyRDSToClickhouseDbRequest,
    ) -> clickhouse_20191111_models.ModifyRDSToClickhouseDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_rdsto_clickhouse_db_with_options_async(request, runtime)

    def operate_log_hub_with_options(
        self,
        request: clickhouse_20191111_models.OperateLogHubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.OperateLogHubResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['AccessSecret'] = request.access_secret
        query['Create'] = request.create
        query['DBClusterId'] = request.dbcluster_id
        query['DeliverName'] = request.deliver_name
        query['DeliverTime'] = request.deliver_time
        query['Description'] = request.description
        query['DomainUrl'] = request.domain_url
        query['FilterDirtyData'] = request.filter_dirty_data
        query['LogHubStores'] = request.log_hub_stores
        query['LogStoreName'] = request.log_store_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Password'] = request.password
        query['ProjectName'] = request.project_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        query['TaskId'] = request.task_id
        query['UseLorne'] = request.use_lorne
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OperateLogHub',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.OperateLogHubResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_log_hub_with_options_async(
        self,
        request: clickhouse_20191111_models.OperateLogHubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.OperateLogHubResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessKey'] = request.access_key
        query['AccessSecret'] = request.access_secret
        query['Create'] = request.create
        query['DBClusterId'] = request.dbcluster_id
        query['DeliverName'] = request.deliver_name
        query['DeliverTime'] = request.deliver_time
        query['Description'] = request.description
        query['DomainUrl'] = request.domain_url
        query['FilterDirtyData'] = request.filter_dirty_data
        query['LogHubStores'] = request.log_hub_stores
        query['LogStoreName'] = request.log_store_name
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['Password'] = request.password
        query['ProjectName'] = request.project_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SchemaName'] = request.schema_name
        query['TableName'] = request.table_name
        query['TaskId'] = request.task_id
        query['UseLorne'] = request.use_lorne
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OperateLogHub',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.OperateLogHubResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_log_hub(
        self,
        request: clickhouse_20191111_models.OperateLogHubRequest,
    ) -> clickhouse_20191111_models.OperateLogHubResponse:
        runtime = util_models.RuntimeOptions()
        return self.operate_log_hub_with_options(request, runtime)

    async def operate_log_hub_async(
        self,
        request: clickhouse_20191111_models.OperateLogHubRequest,
    ) -> clickhouse_20191111_models.OperateLogHubResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_log_hub_with_options_async(request, runtime)

    def operate_lorne_task_status_with_options(
        self,
        request: clickhouse_20191111_models.OperateLorneTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.OperateLorneTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['LorneStatus'] = request.lorne_status
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OperateLorneTaskStatus',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.OperateLorneTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_lorne_task_status_with_options_async(
        self,
        request: clickhouse_20191111_models.OperateLorneTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.OperateLorneTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['LorneStatus'] = request.lorne_status
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OperateLorneTaskStatus',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.OperateLorneTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_lorne_task_status(
        self,
        request: clickhouse_20191111_models.OperateLorneTaskStatusRequest,
    ) -> clickhouse_20191111_models.OperateLorneTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.operate_lorne_task_status_with_options(request, runtime)

    async def operate_lorne_task_status_async(
        self,
        request: clickhouse_20191111_models.OperateLorneTaskStatusRequest,
    ) -> clickhouse_20191111_models.OperateLorneTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.operate_lorne_task_status_with_options_async(request, runtime)

    def release_cluster_public_connection_with_options(
        self,
        request: clickhouse_20191111_models.ReleaseClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseClusterPublicConnection',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cluster_public_connection_with_options_async(
        self,
        request: clickhouse_20191111_models.ReleaseClusterPublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseClusterPublicConnection',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_cluster_public_connection(
        self,
        request: clickhouse_20191111_models.ReleaseClusterPublicConnectionRequest,
    ) -> clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_public_connection_with_options(request, runtime)

    async def release_cluster_public_connection_async(
        self,
        request: clickhouse_20191111_models.ReleaseClusterPublicConnectionRequest,
    ) -> clickhouse_20191111_models.ReleaseClusterPublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_cluster_public_connection_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: clickhouse_20191111_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: clickhouse_20191111_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccountName'] = request.account_name
        query['AccountPassword'] = request.account_password
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: clickhouse_20191111_models.ResetAccountPasswordRequest,
    ) -> clickhouse_20191111_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: clickhouse_20191111_models.ResetAccountPasswordRequest,
    ) -> clickhouse_20191111_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_instance_with_options(
        self,
        request: clickhouse_20191111_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.RestartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: clickhouse_20191111_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartInstance',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.RestartInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_instance(
        self,
        request: clickhouse_20191111_models.RestartInstanceRequest,
    ) -> clickhouse_20191111_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    async def restart_instance_async(
        self,
        request: clickhouse_20191111_models.RestartInstanceRequest,
    ) -> clickhouse_20191111_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_instance_with_options_async(request, runtime)

    def search_rdstables_with_options(
        self,
        request: clickhouse_20191111_models.SearchRDSTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.SearchRDSTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchRDSTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.SearchRDSTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_rdstables_with_options_async(
        self,
        request: clickhouse_20191111_models.SearchRDSTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.SearchRDSTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DbClusterId'] = request.db_cluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['RdsId'] = request.rds_id
        query['RdsPassword'] = request.rds_password
        query['RdsPort'] = request.rds_port
        query['RdsUserName'] = request.rds_user_name
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchRDSTables',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.SearchRDSTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_rdstables(
        self,
        request: clickhouse_20191111_models.SearchRDSTablesRequest,
    ) -> clickhouse_20191111_models.SearchRDSTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_rdstables_with_options(request, runtime)

    async def search_rdstables_async(
        self,
        request: clickhouse_20191111_models.SearchRDSTablesRequest,
    ) -> clickhouse_20191111_models.SearchRDSTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_rdstables_with_options_async(request, runtime)

    def transfer_version_with_options(
        self,
        request: clickhouse_20191111_models.TransferVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.TransferVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SourceAccount'] = request.source_account
        query['SourcePassword'] = request.source_password
        query['TargetAccount'] = request.target_account
        query['TargetDbClusterId'] = request.target_db_cluster_id
        query['TargetPassword'] = request.target_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TransferVersion',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.TransferVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_version_with_options_async(
        self,
        request: clickhouse_20191111_models.TransferVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20191111_models.TransferVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DBClusterId'] = request.dbcluster_id
        query['OwnerAccount'] = request.owner_account
        query['OwnerId'] = request.owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SourceAccount'] = request.source_account
        query['SourcePassword'] = request.source_password
        query['TargetAccount'] = request.target_account
        query['TargetDbClusterId'] = request.target_db_cluster_id
        query['TargetPassword'] = request.target_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TransferVersion',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20191111_models.TransferVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_version(
        self,
        request: clickhouse_20191111_models.TransferVersionRequest,
    ) -> clickhouse_20191111_models.TransferVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.transfer_version_with_options(request, runtime)

    async def transfer_version_async(
        self,
        request: clickhouse_20191111_models.TransferVersionRequest,
    ) -> clickhouse_20191111_models.TransferVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_version_with_options_async(request, runtime)
