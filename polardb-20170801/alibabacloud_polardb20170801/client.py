# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_polardb20170801 import models as polardb_20170801_models
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
            'cn-qingdao': 'polardb.aliyuncs.com',
            'cn-beijing': 'polardb.aliyuncs.com',
            'cn-hangzhou': 'polardb.aliyuncs.com',
            'cn-shanghai': 'polardb.aliyuncs.com',
            'cn-shenzhen': 'polardb.aliyuncs.com',
            'cn-hongkong': 'polardb.aliyuncs.com',
            'ap-southeast-1': 'polardb.aliyuncs.com',
            'us-west-1': 'polardb.aliyuncs.com',
            'us-east-1': 'polardb.aliyuncs.com',
            'cn-hangzhou-finance': 'polardb.aliyuncs.com',
            'cn-shanghai-finance-1': 'polardb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'polardb.aliyuncs.com',
            'ap-northeast-2-pop': 'polardb.aliyuncs.com',
            'cn-beijing-finance-1': 'polardb.aliyuncs.com',
            'cn-beijing-finance-pop': 'polardb.aliyuncs.com',
            'cn-beijing-gov-1': 'polardb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'polardb.aliyuncs.com',
            'cn-edge-1': 'polardb.aliyuncs.com',
            'cn-fujian': 'polardb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'polardb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'polardb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'polardb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'polardb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'polardb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'polardb.aliyuncs.com',
            'cn-hangzhou-test-306': 'polardb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'polardb.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'polardb.aliyuncs.com',
            'cn-north-2-gov-1': 'polardb.aliyuncs.com',
            'cn-qingdao-nebula': 'polardb.aliyuncs.com',
            'cn-shanghai-et15-b01': 'polardb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'polardb.aliyuncs.com',
            'cn-shanghai-inner': 'polardb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'polardb.aliyuncs.com',
            'cn-shenzhen-inner': 'polardb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'polardb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'polardb.aliyuncs.com',
            'cn-wuhan': 'polardb.aliyuncs.com',
            'cn-wulanchabu': 'polardb.aliyuncs.com',
            'cn-yushanfang': 'polardb.aliyuncs.com',
            'cn-zhangbei': 'polardb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'polardb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'polardb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'polardb.aliyuncs.com',
            'eu-west-1-oxs': 'polardb.aliyuncs.com',
            'rus-west-1-pop': 'polardb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('polardb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_schedule_tasks_with_options(
        self,
        request: polardb_20170801_models.CancelScheduleTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CancelScheduleTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CancelScheduleTasksResponse().from_map(
            self.do_rpcrequest('CancelScheduleTasks', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_schedule_tasks_with_options_async(
        self,
        request: polardb_20170801_models.CancelScheduleTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CancelScheduleTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CancelScheduleTasksResponse().from_map(
            await self.do_rpcrequest_async('CancelScheduleTasks', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_schedule_tasks(
        self,
        request: polardb_20170801_models.CancelScheduleTasksRequest,
    ) -> polardb_20170801_models.CancelScheduleTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_schedule_tasks_with_options(request, runtime)

    async def cancel_schedule_tasks_async(
        self,
        request: polardb_20170801_models.CancelScheduleTasksRequest,
    ) -> polardb_20170801_models.CancelScheduleTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_schedule_tasks_with_options_async(request, runtime)

    def check_account_name_with_options(
        self,
        request: polardb_20170801_models.CheckAccountNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CheckAccountNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CheckAccountNameResponse().from_map(
            self.do_rpcrequest('CheckAccountName', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_account_name_with_options_async(
        self,
        request: polardb_20170801_models.CheckAccountNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CheckAccountNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CheckAccountNameResponse().from_map(
            await self.do_rpcrequest_async('CheckAccountName', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_account_name(
        self,
        request: polardb_20170801_models.CheckAccountNameRequest,
    ) -> polardb_20170801_models.CheckAccountNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_account_name_with_options(request, runtime)

    async def check_account_name_async(
        self,
        request: polardb_20170801_models.CheckAccountNameRequest,
    ) -> polardb_20170801_models.CheckAccountNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_account_name_with_options_async(request, runtime)

    def check_dbname_with_options(
        self,
        request: polardb_20170801_models.CheckDBNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CheckDBNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CheckDBNameResponse().from_map(
            self.do_rpcrequest('CheckDBName', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_dbname_with_options_async(
        self,
        request: polardb_20170801_models.CheckDBNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CheckDBNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CheckDBNameResponse().from_map(
            await self.do_rpcrequest_async('CheckDBName', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_dbname(
        self,
        request: polardb_20170801_models.CheckDBNameRequest,
    ) -> polardb_20170801_models.CheckDBNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_dbname_with_options(request, runtime)

    async def check_dbname_async(
        self,
        request: polardb_20170801_models.CheckDBNameRequest,
    ) -> polardb_20170801_models.CheckDBNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_dbname_with_options_async(request, runtime)

    def close_dbcluster_migration_with_options(
        self,
        request: polardb_20170801_models.CloseDBClusterMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CloseDBClusterMigrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CloseDBClusterMigrationResponse().from_map(
            self.do_rpcrequest('CloseDBClusterMigration', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def close_dbcluster_migration_with_options_async(
        self,
        request: polardb_20170801_models.CloseDBClusterMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CloseDBClusterMigrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CloseDBClusterMigrationResponse().from_map(
            await self.do_rpcrequest_async('CloseDBClusterMigration', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def close_dbcluster_migration(
        self,
        request: polardb_20170801_models.CloseDBClusterMigrationRequest,
    ) -> polardb_20170801_models.CloseDBClusterMigrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_dbcluster_migration_with_options(request, runtime)

    async def close_dbcluster_migration_async(
        self,
        request: polardb_20170801_models.CloseDBClusterMigrationRequest,
    ) -> polardb_20170801_models.CloseDBClusterMigrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_dbcluster_migration_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: polardb_20170801_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateAccountResponse().from_map(
            self.do_rpcrequest('CreateAccount', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: polardb_20170801_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateAccountResponse().from_map(
            await self.do_rpcrequest_async('CreateAccount', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_account(
        self,
        request: polardb_20170801_models.CreateAccountRequest,
    ) -> polardb_20170801_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: polardb_20170801_models.CreateAccountRequest,
    ) -> polardb_20170801_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: polardb_20170801_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateBackupResponse().from_map(
            self.do_rpcrequest('CreateBackup', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: polardb_20170801_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateBackupResponse().from_map(
            await self.do_rpcrequest_async('CreateBackup', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup(
        self,
        request: polardb_20170801_models.CreateBackupRequest,
    ) -> polardb_20170801_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: polardb_20170801_models.CreateBackupRequest,
    ) -> polardb_20170801_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_database_with_options(
        self,
        request: polardb_20170801_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateDatabaseResponse().from_map(
            self.do_rpcrequest('CreateDatabase', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_database_with_options_async(
        self,
        request: polardb_20170801_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateDatabaseResponse().from_map(
            await self.do_rpcrequest_async('CreateDatabase', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_database(
        self,
        request: polardb_20170801_models.CreateDatabaseRequest,
    ) -> polardb_20170801_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    async def create_database_async(
        self,
        request: polardb_20170801_models.CreateDatabaseRequest,
    ) -> polardb_20170801_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_database_with_options_async(request, runtime)

    def create_dbcluster_with_options(
        self,
        request: polardb_20170801_models.CreateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateDBClusterResponse().from_map(
            self.do_rpcrequest('CreateDBCluster', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbcluster_with_options_async(
        self,
        request: polardb_20170801_models.CreateDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateDBClusterResponse().from_map(
            await self.do_rpcrequest_async('CreateDBCluster', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbcluster(
        self,
        request: polardb_20170801_models.CreateDBClusterRequest,
    ) -> polardb_20170801_models.CreateDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbcluster_with_options(request, runtime)

    async def create_dbcluster_async(
        self,
        request: polardb_20170801_models.CreateDBClusterRequest,
    ) -> polardb_20170801_models.CreateDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbcluster_with_options_async(request, runtime)

    def create_dbcluster_endpoint_with_options(
        self,
        request: polardb_20170801_models.CreateDBClusterEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBClusterEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateDBClusterEndpointResponse().from_map(
            self.do_rpcrequest('CreateDBClusterEndpoint', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbcluster_endpoint_with_options_async(
        self,
        request: polardb_20170801_models.CreateDBClusterEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBClusterEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateDBClusterEndpointResponse().from_map(
            await self.do_rpcrequest_async('CreateDBClusterEndpoint', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbcluster_endpoint(
        self,
        request: polardb_20170801_models.CreateDBClusterEndpointRequest,
    ) -> polardb_20170801_models.CreateDBClusterEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbcluster_endpoint_with_options(request, runtime)

    async def create_dbcluster_endpoint_async(
        self,
        request: polardb_20170801_models.CreateDBClusterEndpointRequest,
    ) -> polardb_20170801_models.CreateDBClusterEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbcluster_endpoint_with_options_async(request, runtime)

    def create_dbendpoint_address_with_options(
        self,
        request: polardb_20170801_models.CreateDBEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBEndpointAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateDBEndpointAddressResponse().from_map(
            self.do_rpcrequest('CreateDBEndpointAddress', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbendpoint_address_with_options_async(
        self,
        request: polardb_20170801_models.CreateDBEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBEndpointAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateDBEndpointAddressResponse().from_map(
            await self.do_rpcrequest_async('CreateDBEndpointAddress', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbendpoint_address(
        self,
        request: polardb_20170801_models.CreateDBEndpointAddressRequest,
    ) -> polardb_20170801_models.CreateDBEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbendpoint_address_with_options(request, runtime)

    async def create_dbendpoint_address_async(
        self,
        request: polardb_20170801_models.CreateDBEndpointAddressRequest,
    ) -> polardb_20170801_models.CreateDBEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbendpoint_address_with_options_async(request, runtime)

    def create_dblink_with_options(
        self,
        request: polardb_20170801_models.CreateDBLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBLinkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateDBLinkResponse().from_map(
            self.do_rpcrequest('CreateDBLink', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dblink_with_options_async(
        self,
        request: polardb_20170801_models.CreateDBLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBLinkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateDBLinkResponse().from_map(
            await self.do_rpcrequest_async('CreateDBLink', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dblink(
        self,
        request: polardb_20170801_models.CreateDBLinkRequest,
    ) -> polardb_20170801_models.CreateDBLinkResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dblink_with_options(request, runtime)

    async def create_dblink_async(
        self,
        request: polardb_20170801_models.CreateDBLinkRequest,
    ) -> polardb_20170801_models.CreateDBLinkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dblink_with_options_async(request, runtime)

    def create_dbnodes_with_options(
        self,
        request: polardb_20170801_models.CreateDBNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateDBNodesResponse().from_map(
            self.do_rpcrequest('CreateDBNodes', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbnodes_with_options_async(
        self,
        request: polardb_20170801_models.CreateDBNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.CreateDBNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.CreateDBNodesResponse().from_map(
            await self.do_rpcrequest_async('CreateDBNodes', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbnodes(
        self,
        request: polardb_20170801_models.CreateDBNodesRequest,
    ) -> polardb_20170801_models.CreateDBNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbnodes_with_options(request, runtime)

    async def create_dbnodes_async(
        self,
        request: polardb_20170801_models.CreateDBNodesRequest,
    ) -> polardb_20170801_models.CreateDBNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbnodes_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: polardb_20170801_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteAccountResponse().from_map(
            self.do_rpcrequest('DeleteAccount', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: polardb_20170801_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteAccountResponse().from_map(
            await self.do_rpcrequest_async('DeleteAccount', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_account(
        self,
        request: polardb_20170801_models.DeleteAccountRequest,
    ) -> polardb_20170801_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: polardb_20170801_models.DeleteAccountRequest,
    ) -> polardb_20170801_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_backup_with_options(
        self,
        request: polardb_20170801_models.DeleteBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteBackupResponse().from_map(
            self.do_rpcrequest('DeleteBackup', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_backup_with_options_async(
        self,
        request: polardb_20170801_models.DeleteBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteBackupResponse().from_map(
            await self.do_rpcrequest_async('DeleteBackup', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_backup(
        self,
        request: polardb_20170801_models.DeleteBackupRequest,
    ) -> polardb_20170801_models.DeleteBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_with_options(request, runtime)

    async def delete_backup_async(
        self,
        request: polardb_20170801_models.DeleteBackupRequest,
    ) -> polardb_20170801_models.DeleteBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_backup_with_options_async(request, runtime)

    def delete_database_with_options(
        self,
        request: polardb_20170801_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteDatabaseResponse().from_map(
            self.do_rpcrequest('DeleteDatabase', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_database_with_options_async(
        self,
        request: polardb_20170801_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteDatabaseResponse().from_map(
            await self.do_rpcrequest_async('DeleteDatabase', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_database(
        self,
        request: polardb_20170801_models.DeleteDatabaseRequest,
    ) -> polardb_20170801_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    async def delete_database_async(
        self,
        request: polardb_20170801_models.DeleteDatabaseRequest,
    ) -> polardb_20170801_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_database_with_options_async(request, runtime)

    def delete_dbcluster_with_options(
        self,
        request: polardb_20170801_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteDBClusterResponse().from_map(
            self.do_rpcrequest('DeleteDBCluster', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbcluster_with_options_async(
        self,
        request: polardb_20170801_models.DeleteDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteDBClusterResponse().from_map(
            await self.do_rpcrequest_async('DeleteDBCluster', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbcluster(
        self,
        request: polardb_20170801_models.DeleteDBClusterRequest,
    ) -> polardb_20170801_models.DeleteDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_with_options(request, runtime)

    async def delete_dbcluster_async(
        self,
        request: polardb_20170801_models.DeleteDBClusterRequest,
    ) -> polardb_20170801_models.DeleteDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbcluster_with_options_async(request, runtime)

    def delete_dbcluster_endpoint_with_options(
        self,
        request: polardb_20170801_models.DeleteDBClusterEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBClusterEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteDBClusterEndpointResponse().from_map(
            self.do_rpcrequest('DeleteDBClusterEndpoint', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbcluster_endpoint_with_options_async(
        self,
        request: polardb_20170801_models.DeleteDBClusterEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBClusterEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteDBClusterEndpointResponse().from_map(
            await self.do_rpcrequest_async('DeleteDBClusterEndpoint', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbcluster_endpoint(
        self,
        request: polardb_20170801_models.DeleteDBClusterEndpointRequest,
    ) -> polardb_20170801_models.DeleteDBClusterEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbcluster_endpoint_with_options(request, runtime)

    async def delete_dbcluster_endpoint_async(
        self,
        request: polardb_20170801_models.DeleteDBClusterEndpointRequest,
    ) -> polardb_20170801_models.DeleteDBClusterEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbcluster_endpoint_with_options_async(request, runtime)

    def delete_dbendpoint_address_with_options(
        self,
        request: polardb_20170801_models.DeleteDBEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBEndpointAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteDBEndpointAddressResponse().from_map(
            self.do_rpcrequest('DeleteDBEndpointAddress', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbendpoint_address_with_options_async(
        self,
        request: polardb_20170801_models.DeleteDBEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBEndpointAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteDBEndpointAddressResponse().from_map(
            await self.do_rpcrequest_async('DeleteDBEndpointAddress', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbendpoint_address(
        self,
        request: polardb_20170801_models.DeleteDBEndpointAddressRequest,
    ) -> polardb_20170801_models.DeleteDBEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbendpoint_address_with_options(request, runtime)

    async def delete_dbendpoint_address_async(
        self,
        request: polardb_20170801_models.DeleteDBEndpointAddressRequest,
    ) -> polardb_20170801_models.DeleteDBEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbendpoint_address_with_options_async(request, runtime)

    def delete_dblink_with_options(
        self,
        request: polardb_20170801_models.DeleteDBLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBLinkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteDBLinkResponse().from_map(
            self.do_rpcrequest('DeleteDBLink', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dblink_with_options_async(
        self,
        request: polardb_20170801_models.DeleteDBLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBLinkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteDBLinkResponse().from_map(
            await self.do_rpcrequest_async('DeleteDBLink', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dblink(
        self,
        request: polardb_20170801_models.DeleteDBLinkRequest,
    ) -> polardb_20170801_models.DeleteDBLinkResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dblink_with_options(request, runtime)

    async def delete_dblink_async(
        self,
        request: polardb_20170801_models.DeleteDBLinkRequest,
    ) -> polardb_20170801_models.DeleteDBLinkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dblink_with_options_async(request, runtime)

    def delete_dbnodes_with_options(
        self,
        request: polardb_20170801_models.DeleteDBNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteDBNodesResponse().from_map(
            self.do_rpcrequest('DeleteDBNodes', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbnodes_with_options_async(
        self,
        request: polardb_20170801_models.DeleteDBNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DeleteDBNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DeleteDBNodesResponse().from_map(
            await self.do_rpcrequest_async('DeleteDBNodes', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbnodes(
        self,
        request: polardb_20170801_models.DeleteDBNodesRequest,
    ) -> polardb_20170801_models.DeleteDBNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbnodes_with_options(request, runtime)

    async def delete_dbnodes_async(
        self,
        request: polardb_20170801_models.DeleteDBNodesRequest,
    ) -> polardb_20170801_models.DeleteDBNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbnodes_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: polardb_20170801_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeAccountsResponse().from_map(
            self.do_rpcrequest('DescribeAccounts', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: polardb_20170801_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeAccountsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAccounts', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accounts(
        self,
        request: polardb_20170801_models.DescribeAccountsRequest,
    ) -> polardb_20170801_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: polardb_20170801_models.DescribeAccountsRequest,
    ) -> polardb_20170801_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_auto_renew_attribute_with_options(
        self,
        request: polardb_20170801_models.DescribeAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeAutoRenewAttributeResponse().from_map(
            self.do_rpcrequest('DescribeAutoRenewAttribute', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_auto_renew_attribute_with_options_async(
        self,
        request: polardb_20170801_models.DescribeAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeAutoRenewAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeAutoRenewAttribute', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_renew_attribute(
        self,
        request: polardb_20170801_models.DescribeAutoRenewAttributeRequest,
    ) -> polardb_20170801_models.DescribeAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_renew_attribute_with_options(request, runtime)

    async def describe_auto_renew_attribute_async(
        self,
        request: polardb_20170801_models.DescribeAutoRenewAttributeRequest,
    ) -> polardb_20170801_models.DescribeAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_renew_attribute_with_options_async(request, runtime)

    def describe_backup_logs_with_options(
        self,
        request: polardb_20170801_models.DescribeBackupLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeBackupLogsResponse().from_map(
            self.do_rpcrequest('DescribeBackupLogs', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_logs_with_options_async(
        self,
        request: polardb_20170801_models.DescribeBackupLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeBackupLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupLogs', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_logs(
        self,
        request: polardb_20170801_models.DescribeBackupLogsRequest,
    ) -> polardb_20170801_models.DescribeBackupLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_logs_with_options(request, runtime)

    async def describe_backup_logs_async(
        self,
        request: polardb_20170801_models.DescribeBackupLogsRequest,
    ) -> polardb_20170801_models.DescribeBackupLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_logs_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: polardb_20170801_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeBackupPolicyResponse().from_map(
            self.do_rpcrequest('DescribeBackupPolicy', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: polardb_20170801_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeBackupPolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupPolicy', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(
        self,
        request: polardb_20170801_models.DescribeBackupPolicyRequest,
    ) -> polardb_20170801_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: polardb_20170801_models.DescribeBackupPolicyRequest,
    ) -> polardb_20170801_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: polardb_20170801_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeBackupsResponse().from_map(
            self.do_rpcrequest('DescribeBackups', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: polardb_20170801_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeBackupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackups', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backups(
        self,
        request: polardb_20170801_models.DescribeBackupsRequest,
    ) -> polardb_20170801_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: polardb_20170801_models.DescribeBackupsRequest,
    ) -> polardb_20170801_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_backup_tasks_with_options(
        self,
        request: polardb_20170801_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeBackupTasksResponse().from_map(
            self.do_rpcrequest('DescribeBackupTasks', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_tasks_with_options_async(
        self,
        request: polardb_20170801_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeBackupTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeBackupTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupTasks', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_tasks(
        self,
        request: polardb_20170801_models.DescribeBackupTasksRequest,
    ) -> polardb_20170801_models.DescribeBackupTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    async def describe_backup_tasks_async(
        self,
        request: polardb_20170801_models.DescribeBackupTasksRequest,
    ) -> polardb_20170801_models.DescribeBackupTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_tasks_with_options_async(request, runtime)

    def describe_character_set_name_with_options(
        self,
        request: polardb_20170801_models.DescribeCharacterSetNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeCharacterSetNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeCharacterSetNameResponse().from_map(
            self.do_rpcrequest('DescribeCharacterSetName', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_character_set_name_with_options_async(
        self,
        request: polardb_20170801_models.DescribeCharacterSetNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeCharacterSetNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeCharacterSetNameResponse().from_map(
            await self.do_rpcrequest_async('DescribeCharacterSetName', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_character_set_name(
        self,
        request: polardb_20170801_models.DescribeCharacterSetNameRequest,
    ) -> polardb_20170801_models.DescribeCharacterSetNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_character_set_name_with_options(request, runtime)

    async def describe_character_set_name_async(
        self,
        request: polardb_20170801_models.DescribeCharacterSetNameRequest,
    ) -> polardb_20170801_models.DescribeCharacterSetNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_character_set_name_with_options_async(request, runtime)

    def describe_databases_with_options(
        self,
        request: polardb_20170801_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDatabasesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDatabasesResponse().from_map(
            self.do_rpcrequest('DescribeDatabases', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_databases_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDatabasesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDatabasesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDatabases', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_databases(
        self,
        request: polardb_20170801_models.DescribeDatabasesRequest,
    ) -> polardb_20170801_models.DescribeDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_databases_with_options(request, runtime)

    async def describe_databases_async(
        self,
        request: polardb_20170801_models.DescribeDatabasesRequest,
    ) -> polardb_20170801_models.DescribeDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_databases_with_options_async(request, runtime)

    def describe_dbcluster_access_whitelist_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterAccessWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAccessWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterAccessWhitelistResponse().from_map(
            self.do_rpcrequest('DescribeDBClusterAccessWhitelist', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_access_whitelist_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAccessWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAccessWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterAccessWhitelistResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClusterAccessWhitelist', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_access_whitelist(
        self,
        request: polardb_20170801_models.DescribeDBClusterAccessWhitelistRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAccessWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_access_whitelist_with_options(request, runtime)

    async def describe_dbcluster_access_whitelist_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAccessWhitelistRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAccessWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_access_whitelist_with_options_async(request, runtime)

    def describe_dbcluster_attribute_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterAttributeResponse().from_map(
            self.do_rpcrequest('DescribeDBClusterAttribute', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_attribute_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClusterAttribute', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_attribute(
        self,
        request: polardb_20170801_models.DescribeDBClusterAttributeRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_attribute_with_options(request, runtime)

    async def describe_dbcluster_attribute_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAttributeRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_attribute_with_options_async(request, runtime)

    def describe_dbcluster_audit_log_collector_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterAuditLogCollectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAuditLogCollectorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterAuditLogCollectorResponse().from_map(
            self.do_rpcrequest('DescribeDBClusterAuditLogCollector', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_audit_log_collector_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAuditLogCollectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAuditLogCollectorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterAuditLogCollectorResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClusterAuditLogCollector', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_audit_log_collector(
        self,
        request: polardb_20170801_models.DescribeDBClusterAuditLogCollectorRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAuditLogCollectorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_audit_log_collector_with_options(request, runtime)

    async def describe_dbcluster_audit_log_collector_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAuditLogCollectorRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAuditLogCollectorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_audit_log_collector_with_options_async(request, runtime)

    def describe_dbcluster_available_resources_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterAvailableResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAvailableResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterAvailableResourcesResponse().from_map(
            self.do_rpcrequest('DescribeDBClusterAvailableResources', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_available_resources_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAvailableResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterAvailableResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterAvailableResourcesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClusterAvailableResources', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_available_resources(
        self,
        request: polardb_20170801_models.DescribeDBClusterAvailableResourcesRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAvailableResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_available_resources_with_options(request, runtime)

    async def describe_dbcluster_available_resources_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterAvailableResourcesRequest,
    ) -> polardb_20170801_models.DescribeDBClusterAvailableResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_available_resources_with_options_async(request, runtime)

    def describe_dbcluster_endpoints_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterEndpointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterEndpointsResponse().from_map(
            self.do_rpcrequest('DescribeDBClusterEndpoints', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_endpoints_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterEndpointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterEndpointsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClusterEndpoints', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_endpoints(
        self,
        request: polardb_20170801_models.DescribeDBClusterEndpointsRequest,
    ) -> polardb_20170801_models.DescribeDBClusterEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_endpoints_with_options(request, runtime)

    async def describe_dbcluster_endpoints_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterEndpointsRequest,
    ) -> polardb_20170801_models.DescribeDBClusterEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_endpoints_with_options_async(request, runtime)

    def describe_dbcluster_migration_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterMigrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterMigrationResponse().from_map(
            self.do_rpcrequest('DescribeDBClusterMigration', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_migration_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterMigrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterMigrationResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClusterMigration', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_migration(
        self,
        request: polardb_20170801_models.DescribeDBClusterMigrationRequest,
    ) -> polardb_20170801_models.DescribeDBClusterMigrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_migration_with_options(request, runtime)

    async def describe_dbcluster_migration_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterMigrationRequest,
    ) -> polardb_20170801_models.DescribeDBClusterMigrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_migration_with_options_async(request, runtime)

    def describe_dbcluster_monitor_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterMonitorResponse().from_map(
            self.do_rpcrequest('DescribeDBClusterMonitor', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_monitor_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterMonitorResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClusterMonitor', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_monitor(
        self,
        request: polardb_20170801_models.DescribeDBClusterMonitorRequest,
    ) -> polardb_20170801_models.DescribeDBClusterMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_monitor_with_options(request, runtime)

    async def describe_dbcluster_monitor_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterMonitorRequest,
    ) -> polardb_20170801_models.DescribeDBClusterMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_monitor_with_options_async(request, runtime)

    def describe_dbcluster_parameters_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterParametersResponse().from_map(
            self.do_rpcrequest('DescribeDBClusterParameters', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_parameters_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterParametersResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClusterParameters', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_parameters(
        self,
        request: polardb_20170801_models.DescribeDBClusterParametersRequest,
    ) -> polardb_20170801_models.DescribeDBClusterParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_parameters_with_options(request, runtime)

    async def describe_dbcluster_parameters_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterParametersRequest,
    ) -> polardb_20170801_models.DescribeDBClusterParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_parameters_with_options_async(request, runtime)

    def describe_dbcluster_performance_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterPerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterPerformanceResponse().from_map(
            self.do_rpcrequest('DescribeDBClusterPerformance', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_performance_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterPerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterPerformanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClusterPerformance', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_performance(
        self,
        request: polardb_20170801_models.DescribeDBClusterPerformanceRequest,
    ) -> polardb_20170801_models.DescribeDBClusterPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_performance_with_options(request, runtime)

    async def describe_dbcluster_performance_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterPerformanceRequest,
    ) -> polardb_20170801_models.DescribeDBClusterPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_performance_with_options_async(request, runtime)

    def describe_dbclusters_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClustersResponse().from_map(
            self.do_rpcrequest('DescribeDBClusters', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbclusters_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClustersResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClusters', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbclusters(
        self,
        request: polardb_20170801_models.DescribeDBClustersRequest,
    ) -> polardb_20170801_models.DescribeDBClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbclusters_with_options(request, runtime)

    async def describe_dbclusters_async(
        self,
        request: polardb_20170801_models.DescribeDBClustersRequest,
    ) -> polardb_20170801_models.DescribeDBClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbclusters_with_options_async(request, runtime)

    def describe_dbcluster_sslwith_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterSSLResponse().from_map(
            self.do_rpcrequest('DescribeDBClusterSSL', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_sslwith_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterSSLResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClusterSSL', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_ssl(
        self,
        request: polardb_20170801_models.DescribeDBClusterSSLRequest,
    ) -> polardb_20170801_models.DescribeDBClusterSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_sslwith_options(request, runtime)

    async def describe_dbcluster_ssl_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterSSLRequest,
    ) -> polardb_20170801_models.DescribeDBClusterSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_sslwith_options_async(request, runtime)

    def describe_dbclusters_with_backups_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClustersWithBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClustersWithBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClustersWithBackupsResponse().from_map(
            self.do_rpcrequest('DescribeDBClustersWithBackups', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbclusters_with_backups_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClustersWithBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClustersWithBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClustersWithBackupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClustersWithBackups', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbclusters_with_backups(
        self,
        request: polardb_20170801_models.DescribeDBClustersWithBackupsRequest,
    ) -> polardb_20170801_models.DescribeDBClustersWithBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbclusters_with_backups_with_options(request, runtime)

    async def describe_dbclusters_with_backups_async(
        self,
        request: polardb_20170801_models.DescribeDBClustersWithBackupsRequest,
    ) -> polardb_20170801_models.DescribeDBClustersWithBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbclusters_with_backups_with_options_async(request, runtime)

    def describe_dbcluster_tdewith_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterTDEResponse().from_map(
            self.do_rpcrequest('DescribeDBClusterTDE', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_tdewith_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterTDEResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClusterTDE', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_tde(
        self,
        request: polardb_20170801_models.DescribeDBClusterTDERequest,
    ) -> polardb_20170801_models.DescribeDBClusterTDEResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_tdewith_options(request, runtime)

    async def describe_dbcluster_tde_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterTDERequest,
    ) -> polardb_20170801_models.DescribeDBClusterTDEResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_tdewith_options_async(request, runtime)

    def describe_dbcluster_version_with_options(
        self,
        request: polardb_20170801_models.DescribeDBClusterVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterVersionResponse().from_map(
            self.do_rpcrequest('DescribeDBClusterVersion', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbcluster_version_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBClusterVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBClusterVersionResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBClusterVersion', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbcluster_version(
        self,
        request: polardb_20170801_models.DescribeDBClusterVersionRequest,
    ) -> polardb_20170801_models.DescribeDBClusterVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbcluster_version_with_options(request, runtime)

    async def describe_dbcluster_version_async(
        self,
        request: polardb_20170801_models.DescribeDBClusterVersionRequest,
    ) -> polardb_20170801_models.DescribeDBClusterVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbcluster_version_with_options_async(request, runtime)

    def describe_dbinitialize_variable_with_options(
        self,
        request: polardb_20170801_models.DescribeDBInitializeVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBInitializeVariableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBInitializeVariableResponse().from_map(
            self.do_rpcrequest('DescribeDBInitializeVariable', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinitialize_variable_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBInitializeVariableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBInitializeVariableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBInitializeVariableResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInitializeVariable', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinitialize_variable(
        self,
        request: polardb_20170801_models.DescribeDBInitializeVariableRequest,
    ) -> polardb_20170801_models.DescribeDBInitializeVariableResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinitialize_variable_with_options(request, runtime)

    async def describe_dbinitialize_variable_async(
        self,
        request: polardb_20170801_models.DescribeDBInitializeVariableRequest,
    ) -> polardb_20170801_models.DescribeDBInitializeVariableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinitialize_variable_with_options_async(request, runtime)

    def describe_dblinks_with_options(
        self,
        request: polardb_20170801_models.DescribeDBLinksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBLinksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBLinksResponse().from_map(
            self.do_rpcrequest('DescribeDBLinks', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dblinks_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBLinksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBLinksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBLinksResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBLinks', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dblinks(
        self,
        request: polardb_20170801_models.DescribeDBLinksRequest,
    ) -> polardb_20170801_models.DescribeDBLinksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dblinks_with_options(request, runtime)

    async def describe_dblinks_async(
        self,
        request: polardb_20170801_models.DescribeDBLinksRequest,
    ) -> polardb_20170801_models.DescribeDBLinksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dblinks_with_options_async(request, runtime)

    def describe_dbnode_performance_with_options(
        self,
        request: polardb_20170801_models.DescribeDBNodePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBNodePerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBNodePerformanceResponse().from_map(
            self.do_rpcrequest('DescribeDBNodePerformance', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbnode_performance_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDBNodePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDBNodePerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDBNodePerformanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBNodePerformance', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbnode_performance(
        self,
        request: polardb_20170801_models.DescribeDBNodePerformanceRequest,
    ) -> polardb_20170801_models.DescribeDBNodePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbnode_performance_with_options(request, runtime)

    async def describe_dbnode_performance_async(
        self,
        request: polardb_20170801_models.DescribeDBNodePerformanceRequest,
    ) -> polardb_20170801_models.DescribeDBNodePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbnode_performance_with_options_async(request, runtime)

    def describe_detached_backups_with_options(
        self,
        request: polardb_20170801_models.DescribeDetachedBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDetachedBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDetachedBackupsResponse().from_map(
            self.do_rpcrequest('DescribeDetachedBackups', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_detached_backups_with_options_async(
        self,
        request: polardb_20170801_models.DescribeDetachedBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeDetachedBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeDetachedBackupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDetachedBackups', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_detached_backups(
        self,
        request: polardb_20170801_models.DescribeDetachedBackupsRequest,
    ) -> polardb_20170801_models.DescribeDetachedBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_detached_backups_with_options(request, runtime)

    async def describe_detached_backups_async(
        self,
        request: polardb_20170801_models.DescribeDetachedBackupsRequest,
    ) -> polardb_20170801_models.DescribeDetachedBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_detached_backups_with_options_async(request, runtime)

    def describe_global_database_networks_with_options(
        self,
        request: polardb_20170801_models.DescribeGlobalDatabaseNetworksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeGlobalDatabaseNetworksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeGlobalDatabaseNetworksResponse().from_map(
            self.do_rpcrequest('DescribeGlobalDatabaseNetworks', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_global_database_networks_with_options_async(
        self,
        request: polardb_20170801_models.DescribeGlobalDatabaseNetworksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeGlobalDatabaseNetworksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeGlobalDatabaseNetworksResponse().from_map(
            await self.do_rpcrequest_async('DescribeGlobalDatabaseNetworks', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_global_database_networks(
        self,
        request: polardb_20170801_models.DescribeGlobalDatabaseNetworksRequest,
    ) -> polardb_20170801_models.DescribeGlobalDatabaseNetworksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_global_database_networks_with_options(request, runtime)

    async def describe_global_database_networks_async(
        self,
        request: polardb_20170801_models.DescribeGlobalDatabaseNetworksRequest,
    ) -> polardb_20170801_models.DescribeGlobalDatabaseNetworksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_database_networks_with_options_async(request, runtime)

    def describe_log_backup_policy_with_options(
        self,
        request: polardb_20170801_models.DescribeLogBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeLogBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeLogBackupPolicyResponse().from_map(
            self.do_rpcrequest('DescribeLogBackupPolicy', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_log_backup_policy_with_options_async(
        self,
        request: polardb_20170801_models.DescribeLogBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeLogBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeLogBackupPolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeLogBackupPolicy', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_backup_policy(
        self,
        request: polardb_20170801_models.DescribeLogBackupPolicyRequest,
    ) -> polardb_20170801_models.DescribeLogBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_backup_policy_with_options(request, runtime)

    async def describe_log_backup_policy_async(
        self,
        request: polardb_20170801_models.DescribeLogBackupPolicyRequest,
    ) -> polardb_20170801_models.DescribeLogBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_backup_policy_with_options_async(request, runtime)

    def describe_meta_list_with_options(
        self,
        request: polardb_20170801_models.DescribeMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeMetaListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeMetaListResponse().from_map(
            self.do_rpcrequest('DescribeMetaList', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meta_list_with_options_async(
        self,
        request: polardb_20170801_models.DescribeMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeMetaListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeMetaListResponse().from_map(
            await self.do_rpcrequest_async('DescribeMetaList', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_meta_list(
        self,
        request: polardb_20170801_models.DescribeMetaListRequest,
    ) -> polardb_20170801_models.DescribeMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meta_list_with_options(request, runtime)

    async def describe_meta_list_async(
        self,
        request: polardb_20170801_models.DescribeMetaListRequest,
    ) -> polardb_20170801_models.DescribeMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meta_list_with_options_async(request, runtime)

    def describe_pending_maintenance_action_with_options(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribePendingMaintenanceActionResponse().from_map(
            self.do_rpcrequest('DescribePendingMaintenanceAction', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_pending_maintenance_action_with_options_async(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribePendingMaintenanceActionResponse().from_map(
            await self.do_rpcrequest_async('DescribePendingMaintenanceAction', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_pending_maintenance_action(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionRequest,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pending_maintenance_action_with_options(request, runtime)

    async def describe_pending_maintenance_action_async(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionRequest,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pending_maintenance_action_with_options_async(request, runtime)

    def describe_pending_maintenance_actions_with_options(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribePendingMaintenanceActionsResponse().from_map(
            self.do_rpcrequest('DescribePendingMaintenanceActions', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_pending_maintenance_actions_with_options_async(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribePendingMaintenanceActionsResponse().from_map(
            await self.do_rpcrequest_async('DescribePendingMaintenanceActions', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_pending_maintenance_actions(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionsRequest,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pending_maintenance_actions_with_options(request, runtime)

    async def describe_pending_maintenance_actions_async(
        self,
        request: polardb_20170801_models.DescribePendingMaintenanceActionsRequest,
    ) -> polardb_20170801_models.DescribePendingMaintenanceActionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pending_maintenance_actions_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: polardb_20170801_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: polardb_20170801_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: polardb_20170801_models.DescribeRegionsRequest,
    ) -> polardb_20170801_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: polardb_20170801_models.DescribeRegionsRequest,
    ) -> polardb_20170801_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_schedule_tasks_with_options(
        self,
        request: polardb_20170801_models.DescribeScheduleTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeScheduleTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeScheduleTasksResponse().from_map(
            self.do_rpcrequest('DescribeScheduleTasks', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_schedule_tasks_with_options_async(
        self,
        request: polardb_20170801_models.DescribeScheduleTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeScheduleTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeScheduleTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeScheduleTasks', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_schedule_tasks(
        self,
        request: polardb_20170801_models.DescribeScheduleTasksRequest,
    ) -> polardb_20170801_models.DescribeScheduleTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_schedule_tasks_with_options(request, runtime)

    async def describe_schedule_tasks_async(
        self,
        request: polardb_20170801_models.DescribeScheduleTasksRequest,
    ) -> polardb_20170801_models.DescribeScheduleTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_schedule_tasks_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: polardb_20170801_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSlowLogRecordsResponse().from_map(
            self.do_rpcrequest('DescribeSlowLogRecords', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: polardb_20170801_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSlowLogRecordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSlowLogRecords', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: polardb_20170801_models.DescribeSlowLogRecordsRequest,
    ) -> polardb_20170801_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: polardb_20170801_models.DescribeSlowLogRecordsRequest,
    ) -> polardb_20170801_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_sqlexplorer_policy_with_options(
        self,
        request: polardb_20170801_models.DescribeSQLExplorerPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSQLExplorerPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSQLExplorerPolicyResponse().from_map(
            self.do_rpcrequest('DescribeSQLExplorerPolicy', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqlexplorer_policy_with_options_async(
        self,
        request: polardb_20170801_models.DescribeSQLExplorerPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSQLExplorerPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSQLExplorerPolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeSQLExplorerPolicy', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqlexplorer_policy(
        self,
        request: polardb_20170801_models.DescribeSQLExplorerPolicyRequest,
    ) -> polardb_20170801_models.DescribeSQLExplorerPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlexplorer_policy_with_options(request, runtime)

    async def describe_sqlexplorer_policy_async(
        self,
        request: polardb_20170801_models.DescribeSQLExplorerPolicyRequest,
    ) -> polardb_20170801_models.DescribeSQLExplorerPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlexplorer_policy_with_options_async(request, runtime)

    def describe_sqlexplorer_retention_with_options(
        self,
        request: polardb_20170801_models.DescribeSQLExplorerRetentionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSQLExplorerRetentionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSQLExplorerRetentionResponse().from_map(
            self.do_rpcrequest('DescribeSQLExplorerRetention', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqlexplorer_retention_with_options_async(
        self,
        request: polardb_20170801_models.DescribeSQLExplorerRetentionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSQLExplorerRetentionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSQLExplorerRetentionResponse().from_map(
            await self.do_rpcrequest_async('DescribeSQLExplorerRetention', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqlexplorer_retention(
        self,
        request: polardb_20170801_models.DescribeSQLExplorerRetentionRequest,
    ) -> polardb_20170801_models.DescribeSQLExplorerRetentionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlexplorer_retention_with_options(request, runtime)

    async def describe_sqlexplorer_retention_async(
        self,
        request: polardb_20170801_models.DescribeSQLExplorerRetentionRequest,
    ) -> polardb_20170801_models.DescribeSQLExplorerRetentionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlexplorer_retention_with_options_async(request, runtime)

    def describe_sqlexplorer_version_with_options(
        self,
        request: polardb_20170801_models.DescribeSQLExplorerVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSQLExplorerVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSQLExplorerVersionResponse().from_map(
            self.do_rpcrequest('DescribeSQLExplorerVersion', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqlexplorer_version_with_options_async(
        self,
        request: polardb_20170801_models.DescribeSQLExplorerVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSQLExplorerVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSQLExplorerVersionResponse().from_map(
            await self.do_rpcrequest_async('DescribeSQLExplorerVersion', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqlexplorer_version(
        self,
        request: polardb_20170801_models.DescribeSQLExplorerVersionRequest,
    ) -> polardb_20170801_models.DescribeSQLExplorerVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlexplorer_version_with_options(request, runtime)

    async def describe_sqlexplorer_version_async(
        self,
        request: polardb_20170801_models.DescribeSQLExplorerVersionRequest,
    ) -> polardb_20170801_models.DescribeSQLExplorerVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlexplorer_version_with_options_async(request, runtime)

    def describe_sqllog_records_with_options(
        self,
        request: polardb_20170801_models.DescribeSQLLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSQLLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSQLLogRecordsResponse().from_map(
            self.do_rpcrequest('DescribeSQLLogRecords', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqllog_records_with_options_async(
        self,
        request: polardb_20170801_models.DescribeSQLLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSQLLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSQLLogRecordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSQLLogRecords', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_records(
        self,
        request: polardb_20170801_models.DescribeSQLLogRecordsRequest,
    ) -> polardb_20170801_models.DescribeSQLLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_records_with_options(request, runtime)

    async def describe_sqllog_records_async(
        self,
        request: polardb_20170801_models.DescribeSQLLogRecordsRequest,
    ) -> polardb_20170801_models.DescribeSQLLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_records_with_options_async(request, runtime)

    def describe_sqllog_templates_with_options(
        self,
        request: polardb_20170801_models.DescribeSQLLogTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSQLLogTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSQLLogTemplatesResponse().from_map(
            self.do_rpcrequest('DescribeSQLLogTemplates', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqllog_templates_with_options_async(
        self,
        request: polardb_20170801_models.DescribeSQLLogTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSQLLogTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSQLLogTemplatesResponse().from_map(
            await self.do_rpcrequest_async('DescribeSQLLogTemplates', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_templates(
        self,
        request: polardb_20170801_models.DescribeSQLLogTemplatesRequest,
    ) -> polardb_20170801_models.DescribeSQLLogTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_templates_with_options(request, runtime)

    async def describe_sqllog_templates_async(
        self,
        request: polardb_20170801_models.DescribeSQLLogTemplatesRequest,
    ) -> polardb_20170801_models.DescribeSQLLogTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_templates_with_options_async(request, runtime)

    def describe_sql_log_trial_status_with_options(
        self,
        request: polardb_20170801_models.DescribeSqlLogTrialStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSqlLogTrialStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSqlLogTrialStatusResponse().from_map(
            self.do_rpcrequest('DescribeSqlLogTrialStatus', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sql_log_trial_status_with_options_async(
        self,
        request: polardb_20170801_models.DescribeSqlLogTrialStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeSqlLogTrialStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeSqlLogTrialStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeSqlLogTrialStatus', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sql_log_trial_status(
        self,
        request: polardb_20170801_models.DescribeSqlLogTrialStatusRequest,
    ) -> polardb_20170801_models.DescribeSqlLogTrialStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_log_trial_status_with_options(request, runtime)

    async def describe_sql_log_trial_status_async(
        self,
        request: polardb_20170801_models.DescribeSqlLogTrialStatusRequest,
    ) -> polardb_20170801_models.DescribeSqlLogTrialStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sql_log_trial_status_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: polardb_20170801_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeTasksResponse().from_map(
            self.do_rpcrequest('DescribeTasks', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: polardb_20170801_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.DescribeTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeTasks', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tasks(
        self,
        request: polardb_20170801_models.DescribeTasksRequest,
    ) -> polardb_20170801_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: polardb_20170801_models.DescribeTasksRequest,
    ) -> polardb_20170801_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def failover_dbcluster_with_options(
        self,
        request: polardb_20170801_models.FailoverDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.FailoverDBClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.FailoverDBClusterResponse().from_map(
            self.do_rpcrequest('FailoverDBCluster', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def failover_dbcluster_with_options_async(
        self,
        request: polardb_20170801_models.FailoverDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.FailoverDBClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.FailoverDBClusterResponse().from_map(
            await self.do_rpcrequest_async('FailoverDBCluster', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def failover_dbcluster(
        self,
        request: polardb_20170801_models.FailoverDBClusterRequest,
    ) -> polardb_20170801_models.FailoverDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.failover_dbcluster_with_options(request, runtime)

    async def failover_dbcluster_async(
        self,
        request: polardb_20170801_models.FailoverDBClusterRequest,
    ) -> polardb_20170801_models.FailoverDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.failover_dbcluster_with_options_async(request, runtime)

    def grant_account_privilege_with_options(
        self,
        request: polardb_20170801_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.GrantAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.GrantAccountPrivilegeResponse().from_map(
            self.do_rpcrequest('GrantAccountPrivilege', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def grant_account_privilege_with_options_async(
        self,
        request: polardb_20170801_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.GrantAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.GrantAccountPrivilegeResponse().from_map(
            await self.do_rpcrequest_async('GrantAccountPrivilege', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_account_privilege(
        self,
        request: polardb_20170801_models.GrantAccountPrivilegeRequest,
    ) -> polardb_20170801_models.GrantAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_account_privilege_with_options(request, runtime)

    async def grant_account_privilege_async(
        self,
        request: polardb_20170801_models.GrantAccountPrivilegeRequest,
    ) -> polardb_20170801_models.GrantAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_account_privilege_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: polardb_20170801_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: polardb_20170801_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: polardb_20170801_models.ListTagResourcesRequest,
    ) -> polardb_20170801_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: polardb_20170801_models.ListTagResourcesRequest,
    ) -> polardb_20170801_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: polardb_20170801_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyAccountDescriptionResponse().from_map(
            self.do_rpcrequest('ModifyAccountDescription', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: polardb_20170801_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyAccountDescriptionResponse().from_map(
            await self.do_rpcrequest_async('ModifyAccountDescription', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(
        self,
        request: polardb_20170801_models.ModifyAccountDescriptionRequest,
    ) -> polardb_20170801_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: polardb_20170801_models.ModifyAccountDescriptionRequest,
    ) -> polardb_20170801_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_account_password_with_options(
        self,
        request: polardb_20170801_models.ModifyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyAccountPasswordResponse().from_map(
            self.do_rpcrequest('ModifyAccountPassword', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_password_with_options_async(
        self,
        request: polardb_20170801_models.ModifyAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyAccountPasswordResponse().from_map(
            await self.do_rpcrequest_async('ModifyAccountPassword', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_password(
        self,
        request: polardb_20170801_models.ModifyAccountPasswordRequest,
    ) -> polardb_20170801_models.ModifyAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_password_with_options(request, runtime)

    async def modify_account_password_async(
        self,
        request: polardb_20170801_models.ModifyAccountPasswordRequest,
    ) -> polardb_20170801_models.ModifyAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_password_with_options_async(request, runtime)

    def modify_auto_renew_attribute_with_options(
        self,
        request: polardb_20170801_models.ModifyAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyAutoRenewAttributeResponse().from_map(
            self.do_rpcrequest('ModifyAutoRenewAttribute', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_auto_renew_attribute_with_options_async(
        self,
        request: polardb_20170801_models.ModifyAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyAutoRenewAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyAutoRenewAttribute', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_auto_renew_attribute(
        self,
        request: polardb_20170801_models.ModifyAutoRenewAttributeRequest,
    ) -> polardb_20170801_models.ModifyAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_renew_attribute_with_options(request, runtime)

    async def modify_auto_renew_attribute_async(
        self,
        request: polardb_20170801_models.ModifyAutoRenewAttributeRequest,
    ) -> polardb_20170801_models.ModifyAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_renew_attribute_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: polardb_20170801_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyBackupPolicyResponse().from_map(
            self.do_rpcrequest('ModifyBackupPolicy', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: polardb_20170801_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyBackupPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifyBackupPolicy', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy(
        self,
        request: polardb_20170801_models.ModifyBackupPolicyRequest,
    ) -> polardb_20170801_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: polardb_20170801_models.ModifyBackupPolicyRequest,
    ) -> polardb_20170801_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_dbcluster_access_whitelist_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterAccessWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterAccessWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterAccessWhitelistResponse().from_map(
            self.do_rpcrequest('ModifyDBClusterAccessWhitelist', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_access_whitelist_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterAccessWhitelistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterAccessWhitelistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterAccessWhitelistResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBClusterAccessWhitelist', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_access_whitelist(
        self,
        request: polardb_20170801_models.ModifyDBClusterAccessWhitelistRequest,
    ) -> polardb_20170801_models.ModifyDBClusterAccessWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_access_whitelist_with_options(request, runtime)

    async def modify_dbcluster_access_whitelist_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterAccessWhitelistRequest,
    ) -> polardb_20170801_models.ModifyDBClusterAccessWhitelistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_access_whitelist_with_options_async(request, runtime)

    def modify_dbcluster_audit_log_collector_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterAuditLogCollectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterAuditLogCollectorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterAuditLogCollectorResponse().from_map(
            self.do_rpcrequest('ModifyDBClusterAuditLogCollector', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_audit_log_collector_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterAuditLogCollectorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterAuditLogCollectorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterAuditLogCollectorResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBClusterAuditLogCollector', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_audit_log_collector(
        self,
        request: polardb_20170801_models.ModifyDBClusterAuditLogCollectorRequest,
    ) -> polardb_20170801_models.ModifyDBClusterAuditLogCollectorResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_audit_log_collector_with_options(request, runtime)

    async def modify_dbcluster_audit_log_collector_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterAuditLogCollectorRequest,
    ) -> polardb_20170801_models.ModifyDBClusterAuditLogCollectorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_audit_log_collector_with_options_async(request, runtime)

    def modify_dbcluster_description_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterDescriptionResponse().from_map(
            self.do_rpcrequest('ModifyDBClusterDescription', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_description_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterDescriptionResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBClusterDescription', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_description(
        self,
        request: polardb_20170801_models.ModifyDBClusterDescriptionRequest,
    ) -> polardb_20170801_models.ModifyDBClusterDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_description_with_options(request, runtime)

    async def modify_dbcluster_description_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterDescriptionRequest,
    ) -> polardb_20170801_models.ModifyDBClusterDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_description_with_options_async(request, runtime)

    def modify_dbcluster_endpoint_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterEndpointResponse().from_map(
            self.do_rpcrequest('ModifyDBClusterEndpoint', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_endpoint_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterEndpointResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBClusterEndpoint', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_endpoint(
        self,
        request: polardb_20170801_models.ModifyDBClusterEndpointRequest,
    ) -> polardb_20170801_models.ModifyDBClusterEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_endpoint_with_options(request, runtime)

    async def modify_dbcluster_endpoint_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterEndpointRequest,
    ) -> polardb_20170801_models.ModifyDBClusterEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_endpoint_with_options_async(request, runtime)

    def modify_dbcluster_maintain_time_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterMaintainTimeResponse().from_map(
            self.do_rpcrequest('ModifyDBClusterMaintainTime', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_maintain_time_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterMaintainTimeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBClusterMaintainTime', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_maintain_time(
        self,
        request: polardb_20170801_models.ModifyDBClusterMaintainTimeRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_maintain_time_with_options(request, runtime)

    async def modify_dbcluster_maintain_time_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMaintainTimeRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_maintain_time_with_options_async(request, runtime)

    def modify_dbcluster_migration_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMigrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterMigrationResponse().from_map(
            self.do_rpcrequest('ModifyDBClusterMigration', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_migration_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMigrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterMigrationResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBClusterMigration', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_migration(
        self,
        request: polardb_20170801_models.ModifyDBClusterMigrationRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMigrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_migration_with_options(request, runtime)

    async def modify_dbcluster_migration_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMigrationRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMigrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_migration_with_options_async(request, runtime)

    def modify_dbcluster_monitor_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterMonitorResponse().from_map(
            self.do_rpcrequest('ModifyDBClusterMonitor', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_monitor_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterMonitorResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBClusterMonitor', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_monitor(
        self,
        request: polardb_20170801_models.ModifyDBClusterMonitorRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_monitor_with_options(request, runtime)

    async def modify_dbcluster_monitor_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterMonitorRequest,
    ) -> polardb_20170801_models.ModifyDBClusterMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_monitor_with_options_async(request, runtime)

    def modify_dbcluster_parameters_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterParametersResponse().from_map(
            self.do_rpcrequest('ModifyDBClusterParameters', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_parameters_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterParametersResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBClusterParameters', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_parameters(
        self,
        request: polardb_20170801_models.ModifyDBClusterParametersRequest,
    ) -> polardb_20170801_models.ModifyDBClusterParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_parameters_with_options(request, runtime)

    async def modify_dbcluster_parameters_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterParametersRequest,
    ) -> polardb_20170801_models.ModifyDBClusterParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_parameters_with_options_async(request, runtime)

    def modify_dbcluster_primary_zone_with_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterPrimaryZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterPrimaryZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterPrimaryZoneResponse().from_map(
            self.do_rpcrequest('ModifyDBClusterPrimaryZone', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_primary_zone_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterPrimaryZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterPrimaryZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterPrimaryZoneResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBClusterPrimaryZone', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_primary_zone(
        self,
        request: polardb_20170801_models.ModifyDBClusterPrimaryZoneRequest,
    ) -> polardb_20170801_models.ModifyDBClusterPrimaryZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_primary_zone_with_options(request, runtime)

    async def modify_dbcluster_primary_zone_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterPrimaryZoneRequest,
    ) -> polardb_20170801_models.ModifyDBClusterPrimaryZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_primary_zone_with_options_async(request, runtime)

    def modify_dbcluster_sslwith_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterSSLResponse().from_map(
            self.do_rpcrequest('ModifyDBClusterSSL', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_sslwith_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterSSLResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBClusterSSL', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_ssl(
        self,
        request: polardb_20170801_models.ModifyDBClusterSSLRequest,
    ) -> polardb_20170801_models.ModifyDBClusterSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_sslwith_options(request, runtime)

    async def modify_dbcluster_ssl_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterSSLRequest,
    ) -> polardb_20170801_models.ModifyDBClusterSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_sslwith_options_async(request, runtime)

    def modify_dbcluster_tdewith_options(
        self,
        request: polardb_20170801_models.ModifyDBClusterTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterTDEResponse().from_map(
            self.do_rpcrequest('ModifyDBClusterTDE', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbcluster_tdewith_options_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBClusterTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBClusterTDEResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBClusterTDE', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbcluster_tde(
        self,
        request: polardb_20170801_models.ModifyDBClusterTDERequest,
    ) -> polardb_20170801_models.ModifyDBClusterTDEResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbcluster_tdewith_options(request, runtime)

    async def modify_dbcluster_tde_async(
        self,
        request: polardb_20170801_models.ModifyDBClusterTDERequest,
    ) -> polardb_20170801_models.ModifyDBClusterTDEResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbcluster_tdewith_options_async(request, runtime)

    def modify_dbdescription_with_options(
        self,
        request: polardb_20170801_models.ModifyDBDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBDescriptionResponse().from_map(
            self.do_rpcrequest('ModifyDBDescription', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbdescription_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBDescriptionResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBDescription', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbdescription(
        self,
        request: polardb_20170801_models.ModifyDBDescriptionRequest,
    ) -> polardb_20170801_models.ModifyDBDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbdescription_with_options(request, runtime)

    async def modify_dbdescription_async(
        self,
        request: polardb_20170801_models.ModifyDBDescriptionRequest,
    ) -> polardb_20170801_models.ModifyDBDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbdescription_with_options_async(request, runtime)

    def modify_dbendpoint_address_with_options(
        self,
        request: polardb_20170801_models.ModifyDBEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBEndpointAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBEndpointAddressResponse().from_map(
            self.do_rpcrequest('ModifyDBEndpointAddress', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbendpoint_address_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBEndpointAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBEndpointAddressResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBEndpointAddress', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbendpoint_address(
        self,
        request: polardb_20170801_models.ModifyDBEndpointAddressRequest,
    ) -> polardb_20170801_models.ModifyDBEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbendpoint_address_with_options(request, runtime)

    async def modify_dbendpoint_address_async(
        self,
        request: polardb_20170801_models.ModifyDBEndpointAddressRequest,
    ) -> polardb_20170801_models.ModifyDBEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbendpoint_address_with_options_async(request, runtime)

    def modify_dbnode_class_with_options(
        self,
        request: polardb_20170801_models.ModifyDBNodeClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBNodeClassResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBNodeClassResponse().from_map(
            self.do_rpcrequest('ModifyDBNodeClass', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbnode_class_with_options_async(
        self,
        request: polardb_20170801_models.ModifyDBNodeClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyDBNodeClassResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyDBNodeClassResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBNodeClass', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbnode_class(
        self,
        request: polardb_20170801_models.ModifyDBNodeClassRequest,
    ) -> polardb_20170801_models.ModifyDBNodeClassResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbnode_class_with_options(request, runtime)

    async def modify_dbnode_class_async(
        self,
        request: polardb_20170801_models.ModifyDBNodeClassRequest,
    ) -> polardb_20170801_models.ModifyDBNodeClassResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbnode_class_with_options_async(request, runtime)

    def modify_log_backup_policy_with_options(
        self,
        request: polardb_20170801_models.ModifyLogBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyLogBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyLogBackupPolicyResponse().from_map(
            self.do_rpcrequest('ModifyLogBackupPolicy', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_log_backup_policy_with_options_async(
        self,
        request: polardb_20170801_models.ModifyLogBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyLogBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyLogBackupPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifyLogBackupPolicy', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_log_backup_policy(
        self,
        request: polardb_20170801_models.ModifyLogBackupPolicyRequest,
    ) -> polardb_20170801_models.ModifyLogBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_log_backup_policy_with_options(request, runtime)

    async def modify_log_backup_policy_async(
        self,
        request: polardb_20170801_models.ModifyLogBackupPolicyRequest,
    ) -> polardb_20170801_models.ModifyLogBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_log_backup_policy_with_options_async(request, runtime)

    def modify_pending_maintenance_action_with_options(
        self,
        request: polardb_20170801_models.ModifyPendingMaintenanceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyPendingMaintenanceActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyPendingMaintenanceActionResponse().from_map(
            self.do_rpcrequest('ModifyPendingMaintenanceAction', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_pending_maintenance_action_with_options_async(
        self,
        request: polardb_20170801_models.ModifyPendingMaintenanceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ModifyPendingMaintenanceActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ModifyPendingMaintenanceActionResponse().from_map(
            await self.do_rpcrequest_async('ModifyPendingMaintenanceAction', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_pending_maintenance_action(
        self,
        request: polardb_20170801_models.ModifyPendingMaintenanceActionRequest,
    ) -> polardb_20170801_models.ModifyPendingMaintenanceActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_pending_maintenance_action_with_options(request, runtime)

    async def modify_pending_maintenance_action_async(
        self,
        request: polardb_20170801_models.ModifyPendingMaintenanceActionRequest,
    ) -> polardb_20170801_models.ModifyPendingMaintenanceActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_pending_maintenance_action_with_options_async(request, runtime)

    def reset_account_with_options(
        self,
        request: polardb_20170801_models.ResetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ResetAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ResetAccountResponse().from_map(
            self.do_rpcrequest('ResetAccount', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_account_with_options_async(
        self,
        request: polardb_20170801_models.ResetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.ResetAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.ResetAccountResponse().from_map(
            await self.do_rpcrequest_async('ResetAccount', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account(
        self,
        request: polardb_20170801_models.ResetAccountRequest,
    ) -> polardb_20170801_models.ResetAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_with_options(request, runtime)

    async def reset_account_async(
        self,
        request: polardb_20170801_models.ResetAccountRequest,
    ) -> polardb_20170801_models.ResetAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_with_options_async(request, runtime)

    def restart_dbnode_with_options(
        self,
        request: polardb_20170801_models.RestartDBNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RestartDBNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.RestartDBNodeResponse().from_map(
            self.do_rpcrequest('RestartDBNode', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_dbnode_with_options_async(
        self,
        request: polardb_20170801_models.RestartDBNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RestartDBNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.RestartDBNodeResponse().from_map(
            await self.do_rpcrequest_async('RestartDBNode', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_dbnode(
        self,
        request: polardb_20170801_models.RestartDBNodeRequest,
    ) -> polardb_20170801_models.RestartDBNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_dbnode_with_options(request, runtime)

    async def restart_dbnode_async(
        self,
        request: polardb_20170801_models.RestartDBNodeRequest,
    ) -> polardb_20170801_models.RestartDBNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbnode_with_options_async(request, runtime)

    def restore_table_with_options(
        self,
        request: polardb_20170801_models.RestoreTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RestoreTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.RestoreTableResponse().from_map(
            self.do_rpcrequest('RestoreTable', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restore_table_with_options_async(
        self,
        request: polardb_20170801_models.RestoreTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RestoreTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.RestoreTableResponse().from_map(
            await self.do_rpcrequest_async('RestoreTable', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_table(
        self,
        request: polardb_20170801_models.RestoreTableRequest,
    ) -> polardb_20170801_models.RestoreTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_table_with_options(request, runtime)

    async def restore_table_async(
        self,
        request: polardb_20170801_models.RestoreTableRequest,
    ) -> polardb_20170801_models.RestoreTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_table_with_options_async(request, runtime)

    def revoke_account_privilege_with_options(
        self,
        request: polardb_20170801_models.RevokeAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RevokeAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.RevokeAccountPrivilegeResponse().from_map(
            self.do_rpcrequest('RevokeAccountPrivilege', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_account_privilege_with_options_async(
        self,
        request: polardb_20170801_models.RevokeAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.RevokeAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.RevokeAccountPrivilegeResponse().from_map(
            await self.do_rpcrequest_async('RevokeAccountPrivilege', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_account_privilege(
        self,
        request: polardb_20170801_models.RevokeAccountPrivilegeRequest,
    ) -> polardb_20170801_models.RevokeAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_account_privilege_with_options(request, runtime)

    async def revoke_account_privilege_async(
        self,
        request: polardb_20170801_models.RevokeAccountPrivilegeRequest,
    ) -> polardb_20170801_models.RevokeAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_account_privilege_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: polardb_20170801_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: polardb_20170801_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: polardb_20170801_models.TagResourcesRequest,
    ) -> polardb_20170801_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: polardb_20170801_models.TagResourcesRequest,
    ) -> polardb_20170801_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: polardb_20170801_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: polardb_20170801_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: polardb_20170801_models.UntagResourcesRequest,
    ) -> polardb_20170801_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: polardb_20170801_models.UntagResourcesRequest,
    ) -> polardb_20170801_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_dbcluster_minor_version_with_options(
        self,
        request: polardb_20170801_models.UpgradeDBClusterMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.UpgradeDBClusterMinorVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.UpgradeDBClusterMinorVersionResponse().from_map(
            self.do_rpcrequest('UpgradeDBClusterMinorVersion', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_dbcluster_minor_version_with_options_async(
        self,
        request: polardb_20170801_models.UpgradeDBClusterMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.UpgradeDBClusterMinorVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.UpgradeDBClusterMinorVersionResponse().from_map(
            await self.do_rpcrequest_async('UpgradeDBClusterMinorVersion', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbcluster_minor_version(
        self,
        request: polardb_20170801_models.UpgradeDBClusterMinorVersionRequest,
    ) -> polardb_20170801_models.UpgradeDBClusterMinorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbcluster_minor_version_with_options(request, runtime)

    async def upgrade_dbcluster_minor_version_async(
        self,
        request: polardb_20170801_models.UpgradeDBClusterMinorVersionRequest,
    ) -> polardb_20170801_models.UpgradeDBClusterMinorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbcluster_minor_version_with_options_async(request, runtime)

    def upgrade_dbcluster_version_with_options(
        self,
        request: polardb_20170801_models.UpgradeDBClusterVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.UpgradeDBClusterVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.UpgradeDBClusterVersionResponse().from_map(
            self.do_rpcrequest('UpgradeDBClusterVersion', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_dbcluster_version_with_options_async(
        self,
        request: polardb_20170801_models.UpgradeDBClusterVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardb_20170801_models.UpgradeDBClusterVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return polardb_20170801_models.UpgradeDBClusterVersionResponse().from_map(
            await self.do_rpcrequest_async('UpgradeDBClusterVersion', '2017-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbcluster_version(
        self,
        request: polardb_20170801_models.UpgradeDBClusterVersionRequest,
    ) -> polardb_20170801_models.UpgradeDBClusterVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbcluster_version_with_options(request, runtime)

    async def upgrade_dbcluster_version_async(
        self,
        request: polardb_20170801_models.UpgradeDBClusterVersionRequest,
    ) -> polardb_20170801_models.UpgradeDBClusterVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbcluster_version_with_options_async(request, runtime)
