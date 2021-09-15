# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_gpdb20160503 import models as gpdb_20160503_models
from alibabacloud_tea_util import models as util_models


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
            'cn-beijing': 'gpdb.aliyuncs.com',
            'cn-hangzhou': 'gpdb.aliyuncs.com',
            'cn-shanghai': 'gpdb.aliyuncs.com',
            'cn-shenzhen': 'gpdb.aliyuncs.com',
            'cn-hongkong': 'gpdb.aliyuncs.com',
            'ap-southeast-1': 'gpdb.aliyuncs.com',
            'us-west-1': 'gpdb.aliyuncs.com',
            'us-east-1': 'gpdb.aliyuncs.com',
            'cn-hangzhou-finance': 'gpdb.aliyuncs.com',
            'cn-shanghai-finance-1': 'gpdb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'gpdb.aliyuncs.com',
            'cn-qingdao': 'gpdb.aliyuncs.com',
            'cn-north-2-gov-1': 'gpdb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('gpdb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_bu_dbinstance_relation_with_options(
        self,
        request: gpdb_20160503_models.AddBuDBInstanceRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.AddBuDBInstanceRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.AddBuDBInstanceRelationResponse(),
            self.do_rpcrequest('AddBuDBInstanceRelation', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_bu_dbinstance_relation_with_options_async(
        self,
        request: gpdb_20160503_models.AddBuDBInstanceRelationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.AddBuDBInstanceRelationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.AddBuDBInstanceRelationResponse(),
            await self.do_rpcrequest_async('AddBuDBInstanceRelation', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_bu_dbinstance_relation(
        self,
        request: gpdb_20160503_models.AddBuDBInstanceRelationRequest,
    ) -> gpdb_20160503_models.AddBuDBInstanceRelationResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_bu_dbinstance_relation_with_options(request, runtime)

    async def add_bu_dbinstance_relation_async(
        self,
        request: gpdb_20160503_models.AddBuDBInstanceRelationRequest,
    ) -> gpdb_20160503_models.AddBuDBInstanceRelationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_bu_dbinstance_relation_with_options_async(request, runtime)

    def allocate_instance_public_connection_with_options(
        self,
        request: gpdb_20160503_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.AllocateInstancePublicConnectionResponse(),
            self.do_rpcrequest('AllocateInstancePublicConnection', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_instance_public_connection_with_options_async(
        self,
        request: gpdb_20160503_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.AllocateInstancePublicConnectionResponse(),
            await self.do_rpcrequest_async('AllocateInstancePublicConnection', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_instance_public_connection(
        self,
        request: gpdb_20160503_models.AllocateInstancePublicConnectionRequest,
    ) -> gpdb_20160503_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    async def allocate_instance_public_connection_async(
        self,
        request: gpdb_20160503_models.AllocateInstancePublicConnectionRequest,
    ) -> gpdb_20160503_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_instance_public_connection_with_options_async(request, runtime)

    def check_service_linked_role_with_options(
        self,
        request: gpdb_20160503_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CheckServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CheckServiceLinkedRoleResponse(),
            self.do_rpcrequest('CheckServiceLinkedRole', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_service_linked_role_with_options_async(
        self,
        request: gpdb_20160503_models.CheckServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CheckServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CheckServiceLinkedRoleResponse(),
            await self.do_rpcrequest_async('CheckServiceLinkedRole', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_service_linked_role(
        self,
        request: gpdb_20160503_models.CheckServiceLinkedRoleRequest,
    ) -> gpdb_20160503_models.CheckServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_with_options(request, runtime)

    async def check_service_linked_role_async(
        self,
        request: gpdb_20160503_models.CheckServiceLinkedRoleRequest,
    ) -> gpdb_20160503_models.CheckServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: gpdb_20160503_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateAccountResponse(),
            self.do_rpcrequest('CreateAccount', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: gpdb_20160503_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateAccountResponse(),
            await self.do_rpcrequest_async('CreateAccount', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_account(
        self,
        request: gpdb_20160503_models.CreateAccountRequest,
    ) -> gpdb_20160503_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: gpdb_20160503_models.CreateAccountRequest,
    ) -> gpdb_20160503_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: gpdb_20160503_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateDBInstanceResponse(),
            self.do_rpcrequest('CreateDBInstance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        request: gpdb_20160503_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateDBInstanceResponse(),
            await self.do_rpcrequest_async('CreateDBInstance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbinstance(
        self,
        request: gpdb_20160503_models.CreateDBInstanceRequest,
    ) -> gpdb_20160503_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: gpdb_20160503_models.CreateDBInstanceRequest,
    ) -> gpdb_20160503_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_ecsdbinstance_with_options(
        self,
        request: gpdb_20160503_models.CreateECSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateECSDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateECSDBInstanceResponse(),
            self.do_rpcrequest('CreateECSDBInstance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ecsdbinstance_with_options_async(
        self,
        request: gpdb_20160503_models.CreateECSDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateECSDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateECSDBInstanceResponse(),
            await self.do_rpcrequest_async('CreateECSDBInstance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ecsdbinstance(
        self,
        request: gpdb_20160503_models.CreateECSDBInstanceRequest,
    ) -> gpdb_20160503_models.CreateECSDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ecsdbinstance_with_options(request, runtime)

    async def create_ecsdbinstance_async(
        self,
        request: gpdb_20160503_models.CreateECSDBInstanceRequest,
    ) -> gpdb_20160503_models.CreateECSDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ecsdbinstance_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: gpdb_20160503_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateServiceLinkedRoleResponse(),
            self.do_rpcrequest('CreateServiceLinkedRole', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: gpdb_20160503_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.CreateServiceLinkedRoleResponse(),
            await self.do_rpcrequest_async('CreateServiceLinkedRole', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_linked_role(
        self,
        request: gpdb_20160503_models.CreateServiceLinkedRoleRequest,
    ) -> gpdb_20160503_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: gpdb_20160503_models.CreateServiceLinkedRoleRequest,
    ) -> gpdb_20160503_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def delete_database_with_options(
        self,
        request: gpdb_20160503_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDatabaseResponse(),
            self.do_rpcrequest('DeleteDatabase', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_database_with_options_async(
        self,
        request: gpdb_20160503_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDatabaseResponse(),
            await self.do_rpcrequest_async('DeleteDatabase', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_database(
        self,
        request: gpdb_20160503_models.DeleteDatabaseRequest,
    ) -> gpdb_20160503_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    async def delete_database_async(
        self,
        request: gpdb_20160503_models.DeleteDatabaseRequest,
    ) -> gpdb_20160503_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_database_with_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: gpdb_20160503_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDBInstanceResponse(),
            self.do_rpcrequest('DeleteDBInstance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: gpdb_20160503_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DeleteDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DeleteDBInstanceResponse(),
            await self.do_rpcrequest_async('DeleteDBInstance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbinstance(
        self,
        request: gpdb_20160503_models.DeleteDBInstanceRequest,
    ) -> gpdb_20160503_models.DeleteDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: gpdb_20160503_models.DeleteDBInstanceRequest,
    ) -> gpdb_20160503_models.DeleteDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: gpdb_20160503_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeAccountsResponse(),
            self.do_rpcrequest('DescribeAccounts', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeAccountsResponse(),
            await self.do_rpcrequest_async('DescribeAccounts', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accounts(
        self,
        request: gpdb_20160503_models.DescribeAccountsRequest,
    ) -> gpdb_20160503_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: gpdb_20160503_models.DescribeAccountsRequest,
    ) -> gpdb_20160503_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_available_resources_with_options(
        self,
        request: gpdb_20160503_models.DescribeAvailableResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeAvailableResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeAvailableResourcesResponse(),
            self.do_rpcrequest('DescribeAvailableResources', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_resources_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeAvailableResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeAvailableResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeAvailableResourcesResponse(),
            await self.do_rpcrequest_async('DescribeAvailableResources', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resources(
        self,
        request: gpdb_20160503_models.DescribeAvailableResourcesRequest,
    ) -> gpdb_20160503_models.DescribeAvailableResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resources_with_options(request, runtime)

    async def describe_available_resources_async(
        self,
        request: gpdb_20160503_models.DescribeAvailableResourcesRequest,
    ) -> gpdb_20160503_models.DescribeAvailableResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resources_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: gpdb_20160503_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeBackupPolicyResponse(),
            self.do_rpcrequest('DescribeBackupPolicy', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeBackupPolicyResponse(),
            await self.do_rpcrequest_async('DescribeBackupPolicy', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(
        self,
        request: gpdb_20160503_models.DescribeBackupPolicyRequest,
    ) -> gpdb_20160503_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: gpdb_20160503_models.DescribeBackupPolicyRequest,
    ) -> gpdb_20160503_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_data_backups_with_options(
        self,
        request: gpdb_20160503_models.DescribeDataBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDataBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataBackupsResponse(),
            self.do_rpcrequest('DescribeDataBackups', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_backups_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDataBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDataBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDataBackupsResponse(),
            await self.do_rpcrequest_async('DescribeDataBackups', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_backups(
        self,
        request: gpdb_20160503_models.DescribeDataBackupsRequest,
    ) -> gpdb_20160503_models.DescribeDataBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_backups_with_options(request, runtime)

    async def describe_data_backups_async(
        self,
        request: gpdb_20160503_models.DescribeDataBackupsRequest,
    ) -> gpdb_20160503_models.DescribeDataBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_backups_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBClusterPerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBClusterPerformanceResponse(),
            self.do_rpcrequest('DescribeDBClusterPerformance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBClusterPerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBClusterPerformanceResponse(),
            await self.do_rpcrequest_async('DescribeDBClusterPerformance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_performance(
        self,
        request: gpdb_20160503_models.DescribeDBClusterPerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDBClusterPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: gpdb_20160503_models.DescribeDBClusterPerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDBClusterPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeDBInstanceAttribute', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceAttributeResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceAttribute', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceAttributeRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceAttributeRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_iparray_list_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIPArrayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse(),
            self.do_rpcrequest('DescribeDBInstanceIPArrayList', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_iparray_list_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIPArrayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceIPArrayList', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_iparray_list(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIPArrayListRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_iparray_list_with_options(request, runtime)

    async def describe_dbinstance_iparray_list_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceIPArrayListRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceIPArrayListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_iparray_list_with_options_async(request, runtime)

    def describe_dbinstance_net_info_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceNetInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceNetInfoResponse(),
            self.do_rpcrequest('DescribeDBInstanceNetInfo', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_net_info_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceNetInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceNetInfoResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceNetInfo', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_net_info(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceNetInfoRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceNetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    async def describe_dbinstance_net_info_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceNetInfoRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceNetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_net_info_with_options_async(request, runtime)

    def describe_dbinstance_on_ecsattribute_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceOnECSAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceOnECSAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceOnECSAttributeResponse(),
            self.do_rpcrequest('DescribeDBInstanceOnECSAttribute', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_on_ecsattribute_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceOnECSAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceOnECSAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceOnECSAttributeResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceOnECSAttribute', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_on_ecsattribute(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceOnECSAttributeRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceOnECSAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_on_ecsattribute_with_options(request, runtime)

    async def describe_dbinstance_on_ecsattribute_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceOnECSAttributeRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceOnECSAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_on_ecsattribute_with_options_async(request, runtime)

    def describe_dbinstance_performance_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstancePerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstancePerformanceResponse(),
            self.do_rpcrequest('DescribeDBInstancePerformance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_performance_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstancePerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstancePerformanceResponse(),
            await self.do_rpcrequest_async('DescribeDBInstancePerformance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_performance(
        self,
        request: gpdb_20160503_models.DescribeDBInstancePerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDBInstancePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    async def describe_dbinstance_performance_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstancePerformanceRequest,
    ) -> gpdb_20160503_models.DescribeDBInstancePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_performance_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstancesResponse(),
            self.do_rpcrequest('DescribeDBInstances', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstancesResponse(),
            await self.do_rpcrequest_async('DescribeDBInstances', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances(
        self,
        request: gpdb_20160503_models.DescribeDBInstancesRequest,
    ) -> gpdb_20160503_models.DescribeDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstancesRequest,
    ) -> gpdb_20160503_models.DescribeDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_dbinstance_sqlpatterns_with_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSQLPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceSQLPatternsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceSQLPatternsResponse(),
            self.do_rpcrequest('DescribeDBInstanceSQLPatterns', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_sqlpatterns_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSQLPatternsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceSQLPatternsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceSQLPatternsResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceSQLPatterns', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_sqlpatterns(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSQLPatternsRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceSQLPatternsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sqlpatterns_with_options(request, runtime)

    async def describe_dbinstance_sqlpatterns_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSQLPatternsRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceSQLPatternsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_sqlpatterns_with_options_async(request, runtime)

    def describe_dbinstance_sslwith_options(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceSSLResponse(),
            self.do_rpcrequest('DescribeDBInstanceSSL', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_sslwith_options_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeDBInstanceSSLResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceSSL', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_ssl(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSSLRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    async def describe_dbinstance_ssl_async(
        self,
        request: gpdb_20160503_models.DescribeDBInstanceSSLRequest,
    ) -> gpdb_20160503_models.DescribeDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_sslwith_options_async(request, runtime)

    def describe_log_backups_with_options(
        self,
        request: gpdb_20160503_models.DescribeLogBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeLogBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeLogBackupsResponse(),
            self.do_rpcrequest('DescribeLogBackups', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_log_backups_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeLogBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeLogBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeLogBackupsResponse(),
            await self.do_rpcrequest_async('DescribeLogBackups', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_backups(
        self,
        request: gpdb_20160503_models.DescribeLogBackupsRequest,
    ) -> gpdb_20160503_models.DescribeLogBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_backups_with_options(request, runtime)

    async def describe_log_backups_async(
        self,
        request: gpdb_20160503_models.DescribeLogBackupsRequest,
    ) -> gpdb_20160503_models.DescribeLogBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_backups_with_options_async(request, runtime)

    def describe_modify_parameter_log_with_options(
        self,
        request: gpdb_20160503_models.DescribeModifyParameterLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeModifyParameterLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeModifyParameterLogResponse(),
            self.do_rpcrequest('DescribeModifyParameterLog', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_modify_parameter_log_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeModifyParameterLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeModifyParameterLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeModifyParameterLogResponse(),
            await self.do_rpcrequest_async('DescribeModifyParameterLog', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_modify_parameter_log(
        self,
        request: gpdb_20160503_models.DescribeModifyParameterLogRequest,
    ) -> gpdb_20160503_models.DescribeModifyParameterLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_modify_parameter_log_with_options(request, runtime)

    async def describe_modify_parameter_log_async(
        self,
        request: gpdb_20160503_models.DescribeModifyParameterLogRequest,
    ) -> gpdb_20160503_models.DescribeModifyParameterLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_modify_parameter_log_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: gpdb_20160503_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeParametersResponse(),
            self.do_rpcrequest('DescribeParameters', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeParametersResponse(),
            await self.do_rpcrequest_async('DescribeParameters', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameters(
        self,
        request: gpdb_20160503_models.DescribeParametersRequest,
    ) -> gpdb_20160503_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: gpdb_20160503_models.DescribeParametersRequest,
    ) -> gpdb_20160503_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_rds_vpcs_with_options(
        self,
        request: gpdb_20160503_models.DescribeRdsVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRdsVpcsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRdsVpcsResponse(),
            self.do_rpcrequest('DescribeRdsVpcs', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rds_vpcs_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeRdsVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRdsVpcsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRdsVpcsResponse(),
            await self.do_rpcrequest_async('DescribeRdsVpcs', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_vpcs(
        self,
        request: gpdb_20160503_models.DescribeRdsVpcsRequest,
    ) -> gpdb_20160503_models.DescribeRdsVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vpcs_with_options(request, runtime)

    async def describe_rds_vpcs_async(
        self,
        request: gpdb_20160503_models.DescribeRdsVpcsRequest,
    ) -> gpdb_20160503_models.DescribeRdsVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_vpcs_with_options_async(request, runtime)

    def describe_rds_vswitchs_with_options(
        self,
        request: gpdb_20160503_models.DescribeRdsVSwitchsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRdsVSwitchsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRdsVSwitchsResponse(),
            self.do_rpcrequest('DescribeRdsVSwitchs', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rds_vswitchs_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeRdsVSwitchsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRdsVSwitchsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRdsVSwitchsResponse(),
            await self.do_rpcrequest_async('DescribeRdsVSwitchs', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_vswitchs(
        self,
        request: gpdb_20160503_models.DescribeRdsVSwitchsRequest,
    ) -> gpdb_20160503_models.DescribeRdsVSwitchsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vswitchs_with_options(request, runtime)

    async def describe_rds_vswitchs_async(
        self,
        request: gpdb_20160503_models.DescribeRdsVSwitchsRequest,
    ) -> gpdb_20160503_models.DescribeRdsVSwitchsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_vswitchs_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: gpdb_20160503_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: gpdb_20160503_models.DescribeRegionsRequest,
    ) -> gpdb_20160503_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: gpdb_20160503_models.DescribeRegionsRequest,
    ) -> gpdb_20160503_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_resource_usage_with_options(
        self,
        request: gpdb_20160503_models.DescribeResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeResourceUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeResourceUsageResponse(),
            self.do_rpcrequest('DescribeResourceUsage', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_resource_usage_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeResourceUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeResourceUsageResponse(),
            await self.do_rpcrequest_async('DescribeResourceUsage', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_resource_usage(
        self,
        request: gpdb_20160503_models.DescribeResourceUsageRequest,
    ) -> gpdb_20160503_models.DescribeResourceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_usage_with_options(request, runtime)

    async def describe_resource_usage_async(
        self,
        request: gpdb_20160503_models.DescribeResourceUsageRequest,
    ) -> gpdb_20160503_models.DescribeResourceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_usage_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: gpdb_20160503_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSlowLogRecordsResponse(),
            self.do_rpcrequest('DescribeSlowLogRecords', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSlowLogRecordsResponse(),
            await self.do_rpcrequest_async('DescribeSlowLogRecords', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: gpdb_20160503_models.DescribeSlowLogRecordsRequest,
    ) -> gpdb_20160503_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: gpdb_20160503_models.DescribeSlowLogRecordsRequest,
    ) -> gpdb_20160503_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_slow_sqllogs_with_options(
        self,
        request: gpdb_20160503_models.DescribeSlowSQLLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSlowSQLLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSlowSQLLogsResponse(),
            self.do_rpcrequest('DescribeSlowSQLLogs', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_slow_sqllogs_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSlowSQLLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSlowSQLLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSlowSQLLogsResponse(),
            await self.do_rpcrequest_async('DescribeSlowSQLLogs', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_sqllogs(
        self,
        request: gpdb_20160503_models.DescribeSlowSQLLogsRequest,
    ) -> gpdb_20160503_models.DescribeSlowSQLLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_sqllogs_with_options(request, runtime)

    async def describe_slow_sqllogs_async(
        self,
        request: gpdb_20160503_models.DescribeSlowSQLLogsRequest,
    ) -> gpdb_20160503_models.DescribeSlowSQLLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_sqllogs_with_options_async(request, runtime)

    def describe_specification_with_options(
        self,
        request: gpdb_20160503_models.DescribeSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSpecificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSpecificationResponse(),
            self.do_rpcrequest('DescribeSpecification', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_specification_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSpecificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSpecificationResponse(),
            await self.do_rpcrequest_async('DescribeSpecification', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_specification(
        self,
        request: gpdb_20160503_models.DescribeSpecificationRequest,
    ) -> gpdb_20160503_models.DescribeSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_specification_with_options(request, runtime)

    async def describe_specification_async(
        self,
        request: gpdb_20160503_models.DescribeSpecificationRequest,
    ) -> gpdb_20160503_models.DescribeSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_specification_with_options_async(request, runtime)

    def describe_sqlcollector_policy_with_options(
        self,
        request: gpdb_20160503_models.DescribeSQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLCollectorPolicyResponse(),
            self.do_rpcrequest('DescribeSQLCollectorPolicy', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqlcollector_policy_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLCollectorPolicyResponse(),
            await self.do_rpcrequest_async('DescribeSQLCollectorPolicy', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqlcollector_policy(
        self,
        request: gpdb_20160503_models.DescribeSQLCollectorPolicyRequest,
    ) -> gpdb_20160503_models.DescribeSQLCollectorPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlcollector_policy_with_options(request, runtime)

    async def describe_sqlcollector_policy_async(
        self,
        request: gpdb_20160503_models.DescribeSQLCollectorPolicyRequest,
    ) -> gpdb_20160503_models.DescribeSQLCollectorPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlcollector_policy_with_options_async(request, runtime)

    def describe_sqllog_by_query_id_with_options(
        self,
        request: gpdb_20160503_models.DescribeSQLLogByQueryIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogByQueryIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogByQueryIdResponse(),
            self.do_rpcrequest('DescribeSQLLogByQueryId', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqllog_by_query_id_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogByQueryIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogByQueryIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogByQueryIdResponse(),
            await self.do_rpcrequest_async('DescribeSQLLogByQueryId', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_by_query_id(
        self,
        request: gpdb_20160503_models.DescribeSQLLogByQueryIdRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogByQueryIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_by_query_id_with_options(request, runtime)

    async def describe_sqllog_by_query_id_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogByQueryIdRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogByQueryIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_by_query_id_with_options_async(request, runtime)

    def describe_sqllog_count_with_options(
        self,
        request: gpdb_20160503_models.DescribeSQLLogCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogCountResponse(),
            self.do_rpcrequest('DescribeSQLLogCount', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqllog_count_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogCountResponse(),
            await self.do_rpcrequest_async('DescribeSQLLogCount', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_count(
        self,
        request: gpdb_20160503_models.DescribeSQLLogCountRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_count_with_options(request, runtime)

    async def describe_sqllog_count_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogCountRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_count_with_options_async(request, runtime)

    def describe_sqllog_files_with_options(
        self,
        request: gpdb_20160503_models.DescribeSQLLogFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogFilesResponse(),
            self.do_rpcrequest('DescribeSQLLogFiles', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqllog_files_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogFilesResponse(),
            await self.do_rpcrequest_async('DescribeSQLLogFiles', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_files(
        self,
        request: gpdb_20160503_models.DescribeSQLLogFilesRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_files_with_options(request, runtime)

    async def describe_sqllog_files_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogFilesRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_files_with_options_async(request, runtime)

    def describe_sqllog_records_with_options(
        self,
        request: gpdb_20160503_models.DescribeSQLLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogRecordsResponse(),
            self.do_rpcrequest('DescribeSQLLogRecords', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqllog_records_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogRecordsResponse(),
            await self.do_rpcrequest_async('DescribeSQLLogRecords', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_records(
        self,
        request: gpdb_20160503_models.DescribeSQLLogRecordsRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_records_with_options(request, runtime)

    async def describe_sqllog_records_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogRecordsRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_records_with_options_async(request, runtime)

    def describe_sqllogs_with_options(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogsResponse(),
            self.do_rpcrequest('DescribeSQLLogs', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqllogs_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogsResponse(),
            await self.do_rpcrequest_async('DescribeSQLLogs', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllogs(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllogs_with_options(request, runtime)

    async def describe_sqllogs_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllogs_with_options_async(request, runtime)

    def describe_sqllogs_on_slice_with_options(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsOnSliceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogsOnSliceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogsOnSliceResponse(),
            self.do_rpcrequest('DescribeSQLLogsOnSlice', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqllogs_on_slice_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsOnSliceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeSQLLogsOnSliceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeSQLLogsOnSliceResponse(),
            await self.do_rpcrequest_async('DescribeSQLLogsOnSlice', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllogs_on_slice(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsOnSliceRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogsOnSliceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllogs_on_slice_with_options(request, runtime)

    async def describe_sqllogs_on_slice_async(
        self,
        request: gpdb_20160503_models.DescribeSQLLogsOnSliceRequest,
    ) -> gpdb_20160503_models.DescribeSQLLogsOnSliceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllogs_on_slice_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: gpdb_20160503_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeTagsResponse(),
            self.do_rpcrequest('DescribeTags', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeTagsResponse(),
            await self.do_rpcrequest_async('DescribeTags', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tags(
        self,
        request: gpdb_20160503_models.DescribeTagsRequest,
    ) -> gpdb_20160503_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: gpdb_20160503_models.DescribeTagsRequest,
    ) -> gpdb_20160503_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_user_encryption_key_list_with_options(
        self,
        request: gpdb_20160503_models.DescribeUserEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeUserEncryptionKeyListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeUserEncryptionKeyListResponse(),
            self.do_rpcrequest('DescribeUserEncryptionKeyList', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_encryption_key_list_with_options_async(
        self,
        request: gpdb_20160503_models.DescribeUserEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.DescribeUserEncryptionKeyListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.DescribeUserEncryptionKeyListResponse(),
            await self.do_rpcrequest_async('DescribeUserEncryptionKeyList', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_encryption_key_list(
        self,
        request: gpdb_20160503_models.DescribeUserEncryptionKeyListRequest,
    ) -> gpdb_20160503_models.DescribeUserEncryptionKeyListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_encryption_key_list_with_options(request, runtime)

    async def describe_user_encryption_key_list_async(
        self,
        request: gpdb_20160503_models.DescribeUserEncryptionKeyListRequest,
    ) -> gpdb_20160503_models.DescribeUserEncryptionKeyListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_encryption_key_list_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: gpdb_20160503_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: gpdb_20160503_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: gpdb_20160503_models.ListTagResourcesRequest,
    ) -> gpdb_20160503_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: gpdb_20160503_models.ListTagResourcesRequest,
    ) -> gpdb_20160503_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: gpdb_20160503_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyAccountDescriptionResponse(),
            self.do_rpcrequest('ModifyAccountDescription', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyAccountDescriptionResponse(),
            await self.do_rpcrequest_async('ModifyAccountDescription', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(
        self,
        request: gpdb_20160503_models.ModifyAccountDescriptionRequest,
    ) -> gpdb_20160503_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: gpdb_20160503_models.ModifyAccountDescriptionRequest,
    ) -> gpdb_20160503_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: gpdb_20160503_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyBackupPolicyResponse(),
            self.do_rpcrequest('ModifyBackupPolicy', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyBackupPolicyResponse(),
            await self.do_rpcrequest_async('ModifyBackupPolicy', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy(
        self,
        request: gpdb_20160503_models.ModifyBackupPolicyRequest,
    ) -> gpdb_20160503_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: gpdb_20160503_models.ModifyBackupPolicyRequest,
    ) -> gpdb_20160503_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_dbinstance_connection_mode_with_options(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConnectionModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceConnectionModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceConnectionModeResponse(),
            self.do_rpcrequest('ModifyDBInstanceConnectionMode', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_connection_mode_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConnectionModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceConnectionModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceConnectionModeResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceConnectionMode', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_connection_mode(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConnectionModeRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceConnectionModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_mode_with_options(request, runtime)

    async def modify_dbinstance_connection_mode_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConnectionModeRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceConnectionModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_connection_mode_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceConnectionStringResponse(),
            self.do_rpcrequest('ModifyDBInstanceConnectionString', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceConnectionStringResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceConnectionString', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_connection_string(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConnectionStringRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    async def modify_dbinstance_connection_string_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceConnectionStringRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_connection_string_with_options_async(request, runtime)

    def modify_dbinstance_description_with_options(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceDescriptionResponse(),
            self.do_rpcrequest('ModifyDBInstanceDescription', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_description_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceDescriptionResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceDescription', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_description(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceDescriptionRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    async def modify_dbinstance_description_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceDescriptionRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_description_with_options_async(request, runtime)

    def modify_dbinstance_maintain_time_with_options(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceMaintainTimeResponse(),
            self.do_rpcrequest('ModifyDBInstanceMaintainTime', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_maintain_time_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceMaintainTimeResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceMaintainTime', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_maintain_time(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    async def modify_dbinstance_maintain_time_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_maintain_time_with_options_async(request, runtime)

    def modify_dbinstance_network_type_with_options(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceNetworkTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceNetworkTypeResponse(),
            self.do_rpcrequest('ModifyDBInstanceNetworkType', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_network_type_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceNetworkTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceNetworkTypeResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceNetworkType', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_network_type(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceNetworkTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_type_with_options(request, runtime)

    async def modify_dbinstance_network_type_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceNetworkTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_network_type_with_options_async(request, runtime)

    def modify_dbinstance_sslwith_options(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceSSLResponse(),
            self.do_rpcrequest('ModifyDBInstanceSSL', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_sslwith_options_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyDBInstanceSSLResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceSSL', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_ssl(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceSSLRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_sslwith_options(request, runtime)

    async def modify_dbinstance_ssl_async(
        self,
        request: gpdb_20160503_models.ModifyDBInstanceSSLRequest,
    ) -> gpdb_20160503_models.ModifyDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_sslwith_options_async(request, runtime)

    def modify_parameters_with_options(
        self,
        request: gpdb_20160503_models.ModifyParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyParametersResponse(),
            self.do_rpcrequest('ModifyParameters', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_parameters_with_options_async(
        self,
        request: gpdb_20160503_models.ModifyParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifyParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifyParametersResponse(),
            await self.do_rpcrequest_async('ModifyParameters', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_parameters(
        self,
        request: gpdb_20160503_models.ModifyParametersRequest,
    ) -> gpdb_20160503_models.ModifyParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_parameters_with_options(request, runtime)

    async def modify_parameters_async(
        self,
        request: gpdb_20160503_models.ModifyParametersRequest,
    ) -> gpdb_20160503_models.ModifyParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameters_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: gpdb_20160503_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifySecurityIpsResponse(),
            self.do_rpcrequest('ModifySecurityIps', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: gpdb_20160503_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifySecurityIpsResponse(),
            await self.do_rpcrequest_async('ModifySecurityIps', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_ips(
        self,
        request: gpdb_20160503_models.ModifySecurityIpsRequest,
    ) -> gpdb_20160503_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: gpdb_20160503_models.ModifySecurityIpsRequest,
    ) -> gpdb_20160503_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def modify_sqlcollector_policy_with_options(
        self,
        request: gpdb_20160503_models.ModifySQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifySQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifySQLCollectorPolicyResponse(),
            self.do_rpcrequest('ModifySQLCollectorPolicy', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sqlcollector_policy_with_options_async(
        self,
        request: gpdb_20160503_models.ModifySQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ModifySQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ModifySQLCollectorPolicyResponse(),
            await self.do_rpcrequest_async('ModifySQLCollectorPolicy', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sqlcollector_policy(
        self,
        request: gpdb_20160503_models.ModifySQLCollectorPolicyRequest,
    ) -> gpdb_20160503_models.ModifySQLCollectorPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_policy_with_options(request, runtime)

    async def modify_sqlcollector_policy_async(
        self,
        request: gpdb_20160503_models.ModifySQLCollectorPolicyRequest,
    ) -> gpdb_20160503_models.ModifySQLCollectorPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sqlcollector_policy_with_options_async(request, runtime)

    def release_instance_public_connection_with_options(
        self,
        request: gpdb_20160503_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ReleaseInstancePublicConnectionResponse(),
            self.do_rpcrequest('ReleaseInstancePublicConnection', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_instance_public_connection_with_options_async(
        self,
        request: gpdb_20160503_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ReleaseInstancePublicConnectionResponse(),
            await self.do_rpcrequest_async('ReleaseInstancePublicConnection', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance_public_connection(
        self,
        request: gpdb_20160503_models.ReleaseInstancePublicConnectionRequest,
    ) -> gpdb_20160503_models.ReleaseInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    async def release_instance_public_connection_async(
        self,
        request: gpdb_20160503_models.ReleaseInstancePublicConnectionRequest,
    ) -> gpdb_20160503_models.ReleaseInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_public_connection_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: gpdb_20160503_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ResetAccountPasswordResponse(),
            self.do_rpcrequest('ResetAccountPassword', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: gpdb_20160503_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.ResetAccountPasswordResponse(),
            await self.do_rpcrequest_async('ResetAccountPassword', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account_password(
        self,
        request: gpdb_20160503_models.ResetAccountPasswordRequest,
    ) -> gpdb_20160503_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: gpdb_20160503_models.ResetAccountPasswordRequest,
    ) -> gpdb_20160503_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_dbinstance_with_options(
        self,
        request: gpdb_20160503_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.RestartDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.RestartDBInstanceResponse(),
            self.do_rpcrequest('RestartDBInstance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_dbinstance_with_options_async(
        self,
        request: gpdb_20160503_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.RestartDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.RestartDBInstanceResponse(),
            await self.do_rpcrequest_async('RestartDBInstance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_dbinstance(
        self,
        request: gpdb_20160503_models.RestartDBInstanceRequest,
    ) -> gpdb_20160503_models.RestartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: gpdb_20160503_models.RestartDBInstanceRequest,
    ) -> gpdb_20160503_models.RestartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def switch_dbinstance_net_type_with_options(
        self,
        request: gpdb_20160503_models.SwitchDBInstanceNetTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.SwitchDBInstanceNetTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.SwitchDBInstanceNetTypeResponse(),
            self.do_rpcrequest('SwitchDBInstanceNetType', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def switch_dbinstance_net_type_with_options_async(
        self,
        request: gpdb_20160503_models.SwitchDBInstanceNetTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.SwitchDBInstanceNetTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.SwitchDBInstanceNetTypeResponse(),
            await self.do_rpcrequest_async('SwitchDBInstanceNetType', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_dbinstance_net_type(
        self,
        request: gpdb_20160503_models.SwitchDBInstanceNetTypeRequest,
    ) -> gpdb_20160503_models.SwitchDBInstanceNetTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_net_type_with_options(request, runtime)

    async def switch_dbinstance_net_type_async(
        self,
        request: gpdb_20160503_models.SwitchDBInstanceNetTypeRequest,
    ) -> gpdb_20160503_models.SwitchDBInstanceNetTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_dbinstance_net_type_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: gpdb_20160503_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: gpdb_20160503_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: gpdb_20160503_models.TagResourcesRequest,
    ) -> gpdb_20160503_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: gpdb_20160503_models.TagResourcesRequest,
    ) -> gpdb_20160503_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: gpdb_20160503_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: gpdb_20160503_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UntagResourcesResponse(),
            await self.do_rpcrequest_async('UntagResources', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: gpdb_20160503_models.UntagResourcesRequest,
    ) -> gpdb_20160503_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: gpdb_20160503_models.UntagResourcesRequest,
    ) -> gpdb_20160503_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_dbinstance_with_options(
        self,
        request: gpdb_20160503_models.UpgradeDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpgradeDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpgradeDBInstanceResponse(),
            self.do_rpcrequest('UpgradeDBInstance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_dbinstance_with_options_async(
        self,
        request: gpdb_20160503_models.UpgradeDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpgradeDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpgradeDBInstanceResponse(),
            await self.do_rpcrequest_async('UpgradeDBInstance', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbinstance(
        self,
        request: gpdb_20160503_models.UpgradeDBInstanceRequest,
    ) -> gpdb_20160503_models.UpgradeDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_with_options(request, runtime)

    async def upgrade_dbinstance_async(
        self,
        request: gpdb_20160503_models.UpgradeDBInstanceRequest,
    ) -> gpdb_20160503_models.UpgradeDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_with_options_async(request, runtime)

    def upgrade_dbversion_with_options(
        self,
        request: gpdb_20160503_models.UpgradeDBVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpgradeDBVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpgradeDBVersionResponse(),
            self.do_rpcrequest('UpgradeDBVersion', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_dbversion_with_options_async(
        self,
        request: gpdb_20160503_models.UpgradeDBVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gpdb_20160503_models.UpgradeDBVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gpdb_20160503_models.UpgradeDBVersionResponse(),
            await self.do_rpcrequest_async('UpgradeDBVersion', '2016-05-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbversion(
        self,
        request: gpdb_20160503_models.UpgradeDBVersionRequest,
    ) -> gpdb_20160503_models.UpgradeDBVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbversion_with_options(request, runtime)

    async def upgrade_dbversion_async(
        self,
        request: gpdb_20160503_models.UpgradeDBVersionRequest,
    ) -> gpdb_20160503_models.UpgradeDBVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbversion_with_options_async(request, runtime)
