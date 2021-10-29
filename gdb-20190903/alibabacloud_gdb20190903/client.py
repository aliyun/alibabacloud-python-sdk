# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_gdb20190903 import models as gdb_20190903_models
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
            'ap-northeast-1': 'gdb-api.aliyuncs.com',
            'ap-northeast-2-pop': 'gdb-api.aliyuncs.com',
            'ap-south-1': 'gdb-api.ap-south-1.aliyuncs.com',
            'ap-southeast-1': 'gdb-api.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'gdb-api.aliyuncs.com',
            'ap-southeast-3': 'gdb-api.aliyuncs.com',
            'ap-southeast-5': 'gdb-api.ap-southeast-5.aliyuncs.com',
            'cn-beijing': 'gdb-api.aliyuncs.com',
            'cn-beijing-finance-1': 'gdb-api.aliyuncs.com',
            'cn-beijing-finance-pop': 'gdb-api.aliyuncs.com',
            'cn-beijing-gov-1': 'gdb-api.aliyuncs.com',
            'cn-beijing-nu16-b01': 'gdb-api.aliyuncs.com',
            'cn-chengdu': 'gdb-api.aliyuncs.com',
            'cn-edge-1': 'gdb-api.aliyuncs.com',
            'cn-fujian': 'gdb-api.aliyuncs.com',
            'cn-haidian-cm12-c01': 'gdb-api.aliyuncs.com',
            'cn-hangzhou': 'gdb-api.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'gdb-api.aliyuncs.com',
            'cn-hangzhou-finance': 'gdb-api.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'gdb-api.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'gdb-api.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'gdb-api.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'gdb-api.aliyuncs.com',
            'cn-hangzhou-test-306': 'gdb-api.aliyuncs.com',
            'cn-hongkong': 'gdb-api.aliyuncs.com',
            'cn-hongkong-finance-pop': 'gdb-api.aliyuncs.com',
            'cn-huhehaote': 'gdb-api.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'gdb-api.aliyuncs.com',
            'cn-north-2-gov-1': 'gdb-api.aliyuncs.com',
            'cn-qingdao': 'gdb-api.aliyuncs.com',
            'cn-qingdao-nebula': 'gdb-api.aliyuncs.com',
            'cn-shanghai': 'gdb-api.aliyuncs.com',
            'cn-shanghai-et15-b01': 'gdb-api.aliyuncs.com',
            'cn-shanghai-et2-b01': 'gdb-api.aliyuncs.com',
            'cn-shanghai-finance-1': 'gdb-api.aliyuncs.com',
            'cn-shanghai-inner': 'gdb-api.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'gdb-api.aliyuncs.com',
            'cn-shenzhen': 'gdb-api.aliyuncs.com',
            'cn-shenzhen-finance-1': 'gdb-api.aliyuncs.com',
            'cn-shenzhen-inner': 'gdb-api.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'gdb-api.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'gdb-api.aliyuncs.com',
            'cn-wuhan': 'gdb-api.aliyuncs.com',
            'cn-wulanchabu': 'gdb-api.aliyuncs.com',
            'cn-yushanfang': 'gdb-api.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'gdb-api.aliyuncs.com',
            'cn-zhangjiakou': 'gdb-api.cn-zhangjiakou.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'gdb-api.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'gdb-api.aliyuncs.com',
            'eu-central-1': 'gdb-api.aliyuncs.com',
            'eu-west-1': 'gdb-api.aliyuncs.com',
            'eu-west-1-oxs': 'gdb-api.aliyuncs.com',
            'me-east-1': 'gdb-api.aliyuncs.com',
            'rus-west-1-pop': 'gdb-api.aliyuncs.com',
            'us-east-1': 'gdb-api.aliyuncs.com',
            'us-west-1': 'gdb-api.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('gdb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def allocate_instance_public_connection_with_options(
        self,
        request: gdb_20190903_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.AllocateInstancePublicConnectionResponse(),
            self.do_rpcrequest('AllocateInstancePublicConnection', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_instance_public_connection_with_options_async(
        self,
        request: gdb_20190903_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.AllocateInstancePublicConnectionResponse(),
            await self.do_rpcrequest_async('AllocateInstancePublicConnection', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_instance_public_connection(
        self,
        request: gdb_20190903_models.AllocateInstancePublicConnectionRequest,
    ) -> gdb_20190903_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    async def allocate_instance_public_connection_async(
        self,
        request: gdb_20190903_models.AllocateInstancePublicConnectionRequest,
    ) -> gdb_20190903_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_instance_public_connection_with_options_async(request, runtime)

    def clone_dbinstance_with_options(
        self,
        request: gdb_20190903_models.CloneDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.CloneDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.CloneDBInstanceResponse(),
            self.do_rpcrequest('CloneDBInstance', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clone_dbinstance_with_options_async(
        self,
        request: gdb_20190903_models.CloneDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.CloneDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.CloneDBInstanceResponse(),
            await self.do_rpcrequest_async('CloneDBInstance', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_dbinstance(
        self,
        request: gdb_20190903_models.CloneDBInstanceRequest,
    ) -> gdb_20190903_models.CloneDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_dbinstance_with_options(request, runtime)

    async def clone_dbinstance_async(
        self,
        request: gdb_20190903_models.CloneDBInstanceRequest,
    ) -> gdb_20190903_models.CloneDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_dbinstance_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: gdb_20190903_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.CreateAccountResponse(),
            self.do_rpcrequest('CreateAccount', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: gdb_20190903_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.CreateAccountResponse(),
            await self.do_rpcrequest_async('CreateAccount', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_account(
        self,
        request: gdb_20190903_models.CreateAccountRequest,
    ) -> gdb_20190903_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: gdb_20190903_models.CreateAccountRequest,
    ) -> gdb_20190903_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: gdb_20190903_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.CreateDBInstanceResponse(),
            self.do_rpcrequest('CreateDBInstance', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        request: gdb_20190903_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.CreateDBInstanceResponse(),
            await self.do_rpcrequest_async('CreateDBInstance', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbinstance(
        self,
        request: gdb_20190903_models.CreateDBInstanceRequest,
    ) -> gdb_20190903_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: gdb_20190903_models.CreateDBInstanceRequest,
    ) -> gdb_20190903_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_read_dbinstance_with_options(
        self,
        request: gdb_20190903_models.CreateReadDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.CreateReadDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.CreateReadDBInstanceResponse(),
            self.do_rpcrequest('CreateReadDBInstance', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_read_dbinstance_with_options_async(
        self,
        request: gdb_20190903_models.CreateReadDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.CreateReadDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.CreateReadDBInstanceResponse(),
            await self.do_rpcrequest_async('CreateReadDBInstance', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_read_dbinstance(
        self,
        request: gdb_20190903_models.CreateReadDBInstanceRequest,
    ) -> gdb_20190903_models.CreateReadDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_read_dbinstance_with_options(request, runtime)

    async def create_read_dbinstance_async(
        self,
        request: gdb_20190903_models.CreateReadDBInstanceRequest,
    ) -> gdb_20190903_models.CreateReadDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_read_dbinstance_with_options_async(request, runtime)

    def create_service_linked_role_with_options(
        self,
        request: gdb_20190903_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.CreateServiceLinkedRoleResponse(),
            self.do_rpcrequest('CreateServiceLinkedRole', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_service_linked_role_with_options_async(
        self,
        request: gdb_20190903_models.CreateServiceLinkedRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.CreateServiceLinkedRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.CreateServiceLinkedRoleResponse(),
            await self.do_rpcrequest_async('CreateServiceLinkedRole', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_linked_role(
        self,
        request: gdb_20190903_models.CreateServiceLinkedRoleRequest,
    ) -> gdb_20190903_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    async def create_service_linked_role_async(
        self,
        request: gdb_20190903_models.CreateServiceLinkedRoleRequest,
    ) -> gdb_20190903_models.CreateServiceLinkedRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_linked_role_with_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: gdb_20190903_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DeleteDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DeleteDBInstanceResponse(),
            self.do_rpcrequest('DeleteDBInstance', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: gdb_20190903_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DeleteDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DeleteDBInstanceResponse(),
            await self.do_rpcrequest_async('DeleteDBInstance', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbinstance(
        self,
        request: gdb_20190903_models.DeleteDBInstanceRequest,
    ) -> gdb_20190903_models.DeleteDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: gdb_20190903_models.DeleteDBInstanceRequest,
    ) -> gdb_20190903_models.DeleteDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: gdb_20190903_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeAccountsResponse(),
            self.do_rpcrequest('DescribeAccounts', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: gdb_20190903_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeAccountsResponse(),
            await self.do_rpcrequest_async('DescribeAccounts', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accounts(
        self,
        request: gdb_20190903_models.DescribeAccountsRequest,
    ) -> gdb_20190903_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: gdb_20190903_models.DescribeAccountsRequest,
    ) -> gdb_20190903_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: gdb_20190903_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeAvailableResourceResponse(),
            self.do_rpcrequest('DescribeAvailableResource', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: gdb_20190903_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeAvailableResourceResponse(),
            await self.do_rpcrequest_async('DescribeAvailableResource', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(
        self,
        request: gdb_20190903_models.DescribeAvailableResourceRequest,
    ) -> gdb_20190903_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: gdb_20190903_models.DescribeAvailableResourceRequest,
    ) -> gdb_20190903_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: gdb_20190903_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeBackupPolicyResponse(),
            self.do_rpcrequest('DescribeBackupPolicy', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: gdb_20190903_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeBackupPolicyResponse(),
            await self.do_rpcrequest_async('DescribeBackupPolicy', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(
        self,
        request: gdb_20190903_models.DescribeBackupPolicyRequest,
    ) -> gdb_20190903_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: gdb_20190903_models.DescribeBackupPolicyRequest,
    ) -> gdb_20190903_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: gdb_20190903_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeBackupsResponse(),
            self.do_rpcrequest('DescribeBackups', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: gdb_20190903_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeBackupsResponse(),
            await self.do_rpcrequest_async('DescribeBackups', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backups(
        self,
        request: gdb_20190903_models.DescribeBackupsRequest,
    ) -> gdb_20190903_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: gdb_20190903_models.DescribeBackupsRequest,
    ) -> gdb_20190903_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_dbinstance_access_white_list_with_options(
        self,
        request: gdb_20190903_models.DescribeDBInstanceAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeDBInstanceAccessWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeDBInstanceAccessWhiteListResponse(),
            self.do_rpcrequest('DescribeDBInstanceAccessWhiteList', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_access_white_list_with_options_async(
        self,
        request: gdb_20190903_models.DescribeDBInstanceAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeDBInstanceAccessWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeDBInstanceAccessWhiteListResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceAccessWhiteList', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_access_white_list(
        self,
        request: gdb_20190903_models.DescribeDBInstanceAccessWhiteListRequest,
    ) -> gdb_20190903_models.DescribeDBInstanceAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_access_white_list_with_options(request, runtime)

    async def describe_dbinstance_access_white_list_async(
        self,
        request: gdb_20190903_models.DescribeDBInstanceAccessWhiteListRequest,
    ) -> gdb_20190903_models.DescribeDBInstanceAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_access_white_list_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: gdb_20190903_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeDBInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeDBInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeDBInstanceAttribute', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: gdb_20190903_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeDBInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeDBInstanceAttributeResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceAttribute', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: gdb_20190903_models.DescribeDBInstanceAttributeRequest,
    ) -> gdb_20190903_models.DescribeDBInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: gdb_20190903_models.DescribeDBInstanceAttributeRequest,
    ) -> gdb_20190903_models.DescribeDBInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_performance_with_options(
        self,
        request: gdb_20190903_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeDBInstancePerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeDBInstancePerformanceResponse(),
            self.do_rpcrequest('DescribeDBInstancePerformance', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_performance_with_options_async(
        self,
        request: gdb_20190903_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeDBInstancePerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeDBInstancePerformanceResponse(),
            await self.do_rpcrequest_async('DescribeDBInstancePerformance', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_performance(
        self,
        request: gdb_20190903_models.DescribeDBInstancePerformanceRequest,
    ) -> gdb_20190903_models.DescribeDBInstancePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    async def describe_dbinstance_performance_async(
        self,
        request: gdb_20190903_models.DescribeDBInstancePerformanceRequest,
    ) -> gdb_20190903_models.DescribeDBInstancePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_performance_with_options_async(request, runtime)

    def describe_dbinstance_status_with_options(
        self,
        request: gdb_20190903_models.DescribeDBInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeDBInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeDBInstanceStatusResponse(),
            self.do_rpcrequest('DescribeDBInstanceStatus', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_status_with_options_async(
        self,
        request: gdb_20190903_models.DescribeDBInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeDBInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeDBInstanceStatusResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceStatus', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_status(
        self,
        request: gdb_20190903_models.DescribeDBInstanceStatusRequest,
    ) -> gdb_20190903_models.DescribeDBInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_status_with_options(request, runtime)

    async def describe_dbinstance_status_async(
        self,
        request: gdb_20190903_models.DescribeDBInstanceStatusRequest,
    ) -> gdb_20190903_models.DescribeDBInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_status_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        request: gdb_20190903_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeDBInstancesResponse(),
            self.do_rpcrequest('DescribeDBInstances', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        request: gdb_20190903_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeDBInstancesResponse(),
            await self.do_rpcrequest_async('DescribeDBInstances', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances(
        self,
        request: gdb_20190903_models.DescribeDBInstancesRequest,
    ) -> gdb_20190903_models.DescribeDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: gdb_20190903_models.DescribeDBInstancesRequest,
    ) -> gdb_20190903_models.DescribeDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: gdb_20190903_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: gdb_20190903_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: gdb_20190903_models.DescribeRegionsRequest,
    ) -> gdb_20190903_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: gdb_20190903_models.DescribeRegionsRequest,
    ) -> gdb_20190903_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_resource_usage_with_options(
        self,
        request: gdb_20190903_models.DescribeResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeResourceUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeResourceUsageResponse(),
            self.do_rpcrequest('DescribeResourceUsage', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_resource_usage_with_options_async(
        self,
        request: gdb_20190903_models.DescribeResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeResourceUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeResourceUsageResponse(),
            await self.do_rpcrequest_async('DescribeResourceUsage', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_resource_usage(
        self,
        request: gdb_20190903_models.DescribeResourceUsageRequest,
    ) -> gdb_20190903_models.DescribeResourceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_usage_with_options(request, runtime)

    async def describe_resource_usage_async(
        self,
        request: gdb_20190903_models.DescribeResourceUsageRequest,
    ) -> gdb_20190903_models.DescribeResourceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_usage_with_options_async(request, runtime)

    def describe_security_group_configuration_with_options(
        self,
        request: gdb_20190903_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeSecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeSecurityGroupConfigurationResponse(),
            self.do_rpcrequest('DescribeSecurityGroupConfiguration', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_group_configuration_with_options_async(
        self,
        request: gdb_20190903_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeSecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeSecurityGroupConfigurationResponse(),
            await self.do_rpcrequest_async('DescribeSecurityGroupConfiguration', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_group_configuration(
        self,
        request: gdb_20190903_models.DescribeSecurityGroupConfigurationRequest,
    ) -> gdb_20190903_models.DescribeSecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    async def describe_security_group_configuration_async(
        self,
        request: gdb_20190903_models.DescribeSecurityGroupConfigurationRequest,
    ) -> gdb_20190903_models.DescribeSecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_group_configuration_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: gdb_20190903_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeTagsResponse(),
            self.do_rpcrequest('DescribeTags', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: gdb_20190903_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.DescribeTagsResponse(),
            await self.do_rpcrequest_async('DescribeTags', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tags(
        self,
        request: gdb_20190903_models.DescribeTagsRequest,
    ) -> gdb_20190903_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: gdb_20190903_models.DescribeTagsRequest,
    ) -> gdb_20190903_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: gdb_20190903_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: gdb_20190903_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: gdb_20190903_models.ListTagResourcesRequest,
    ) -> gdb_20190903_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: gdb_20190903_models.ListTagResourcesRequest,
    ) -> gdb_20190903_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: gdb_20190903_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ModifyBackupPolicyResponse(),
            self.do_rpcrequest('ModifyBackupPolicy', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: gdb_20190903_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ModifyBackupPolicyResponse(),
            await self.do_rpcrequest_async('ModifyBackupPolicy', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy(
        self,
        request: gdb_20190903_models.ModifyBackupPolicyRequest,
    ) -> gdb_20190903_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: gdb_20190903_models.ModifyBackupPolicyRequest,
    ) -> gdb_20190903_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_dbinstance_access_white_list_with_options(
        self,
        request: gdb_20190903_models.ModifyDBInstanceAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ModifyDBInstanceAccessWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ModifyDBInstanceAccessWhiteListResponse(),
            self.do_rpcrequest('ModifyDBInstanceAccessWhiteList', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_access_white_list_with_options_async(
        self,
        request: gdb_20190903_models.ModifyDBInstanceAccessWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ModifyDBInstanceAccessWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ModifyDBInstanceAccessWhiteListResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceAccessWhiteList', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_access_white_list(
        self,
        request: gdb_20190903_models.ModifyDBInstanceAccessWhiteListRequest,
    ) -> gdb_20190903_models.ModifyDBInstanceAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_access_white_list_with_options(request, runtime)

    async def modify_dbinstance_access_white_list_async(
        self,
        request: gdb_20190903_models.ModifyDBInstanceAccessWhiteListRequest,
    ) -> gdb_20190903_models.ModifyDBInstanceAccessWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_access_white_list_with_options_async(request, runtime)

    def modify_dbinstance_description_with_options(
        self,
        request: gdb_20190903_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ModifyDBInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ModifyDBInstanceDescriptionResponse(),
            self.do_rpcrequest('ModifyDBInstanceDescription', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_description_with_options_async(
        self,
        request: gdb_20190903_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ModifyDBInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ModifyDBInstanceDescriptionResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceDescription', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_description(
        self,
        request: gdb_20190903_models.ModifyDBInstanceDescriptionRequest,
    ) -> gdb_20190903_models.ModifyDBInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    async def modify_dbinstance_description_async(
        self,
        request: gdb_20190903_models.ModifyDBInstanceDescriptionRequest,
    ) -> gdb_20190903_models.ModifyDBInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_description_with_options_async(request, runtime)

    def modify_dbinstance_maintain_time_with_options(
        self,
        request: gdb_20190903_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ModifyDBInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ModifyDBInstanceMaintainTimeResponse(),
            self.do_rpcrequest('ModifyDBInstanceMaintainTime', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_maintain_time_with_options_async(
        self,
        request: gdb_20190903_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ModifyDBInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ModifyDBInstanceMaintainTimeResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceMaintainTime', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_maintain_time(
        self,
        request: gdb_20190903_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> gdb_20190903_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    async def modify_dbinstance_maintain_time_async(
        self,
        request: gdb_20190903_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> gdb_20190903_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_maintain_time_with_options_async(request, runtime)

    def modify_dbinstance_spec_with_options(
        self,
        request: gdb_20190903_models.ModifyDBInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ModifyDBInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ModifyDBInstanceSpecResponse(),
            self.do_rpcrequest('ModifyDBInstanceSpec', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_spec_with_options_async(
        self,
        request: gdb_20190903_models.ModifyDBInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ModifyDBInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ModifyDBInstanceSpecResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceSpec', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_spec(
        self,
        request: gdb_20190903_models.ModifyDBInstanceSpecRequest,
    ) -> gdb_20190903_models.ModifyDBInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_spec_with_options(request, runtime)

    async def modify_dbinstance_spec_async(
        self,
        request: gdb_20190903_models.ModifyDBInstanceSpecRequest,
    ) -> gdb_20190903_models.ModifyDBInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_spec_with_options_async(request, runtime)

    def modify_security_group_configuration_with_options(
        self,
        request: gdb_20190903_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ModifySecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ModifySecurityGroupConfigurationResponse(),
            self.do_rpcrequest('ModifySecurityGroupConfiguration', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_group_configuration_with_options_async(
        self,
        request: gdb_20190903_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ModifySecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ModifySecurityGroupConfigurationResponse(),
            await self.do_rpcrequest_async('ModifySecurityGroupConfiguration', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_configuration(
        self,
        request: gdb_20190903_models.ModifySecurityGroupConfigurationRequest,
    ) -> gdb_20190903_models.ModifySecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    async def modify_security_group_configuration_async(
        self,
        request: gdb_20190903_models.ModifySecurityGroupConfigurationRequest,
    ) -> gdb_20190903_models.ModifySecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_configuration_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: gdb_20190903_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ResetAccountPasswordResponse(),
            self.do_rpcrequest('ResetAccountPassword', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: gdb_20190903_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.ResetAccountPasswordResponse(),
            await self.do_rpcrequest_async('ResetAccountPassword', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account_password(
        self,
        request: gdb_20190903_models.ResetAccountPasswordRequest,
    ) -> gdb_20190903_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: gdb_20190903_models.ResetAccountPasswordRequest,
    ) -> gdb_20190903_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_dbinstance_with_options(
        self,
        request: gdb_20190903_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.RestartDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.RestartDBInstanceResponse(),
            self.do_rpcrequest('RestartDBInstance', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_dbinstance_with_options_async(
        self,
        request: gdb_20190903_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.RestartDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.RestartDBInstanceResponse(),
            await self.do_rpcrequest_async('RestartDBInstance', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_dbinstance(
        self,
        request: gdb_20190903_models.RestartDBInstanceRequest,
    ) -> gdb_20190903_models.RestartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: gdb_20190903_models.RestartDBInstanceRequest,
    ) -> gdb_20190903_models.RestartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: gdb_20190903_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: gdb_20190903_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: gdb_20190903_models.TagResourcesRequest,
    ) -> gdb_20190903_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: gdb_20190903_models.TagResourcesRequest,
    ) -> gdb_20190903_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: gdb_20190903_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: gdb_20190903_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.UntagResourcesResponse(),
            await self.do_rpcrequest_async('UntagResources', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: gdb_20190903_models.UntagResourcesRequest,
    ) -> gdb_20190903_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: gdb_20190903_models.UntagResourcesRequest,
    ) -> gdb_20190903_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(
        self,
        request: gdb_20190903_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.UpgradeDBInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.UpgradeDBInstanceKernelVersionResponse(),
            self.do_rpcrequest('UpgradeDBInstanceKernelVersion', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_dbinstance_kernel_version_with_options_async(
        self,
        request: gdb_20190903_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> gdb_20190903_models.UpgradeDBInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            gdb_20190903_models.UpgradeDBInstanceKernelVersionResponse(),
            await self.do_rpcrequest_async('UpgradeDBInstanceKernelVersion', '2019-09-03', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbinstance_kernel_version(
        self,
        request: gdb_20190903_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> gdb_20190903_models.UpgradeDBInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)

    async def upgrade_dbinstance_kernel_version_async(
        self,
        request: gdb_20190903_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> gdb_20190903_models.UpgradeDBInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_kernel_version_with_options_async(request, runtime)
