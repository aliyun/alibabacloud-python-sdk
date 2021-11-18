# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_polardbx20200202 import models as polardbx_20200202_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def allocate_instance_public_connection_with_options(
        self,
        request: polardbx_20200202_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.AllocateInstancePublicConnectionResponse(),
            self.do_rpcrequest('AllocateInstancePublicConnection', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_instance_public_connection_with_options_async(
        self,
        request: polardbx_20200202_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.AllocateInstancePublicConnectionResponse(),
            await self.do_rpcrequest_async('AllocateInstancePublicConnection', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_instance_public_connection(
        self,
        request: polardbx_20200202_models.AllocateInstancePublicConnectionRequest,
    ) -> polardbx_20200202_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    async def allocate_instance_public_connection_async(
        self,
        request: polardbx_20200202_models.AllocateInstancePublicConnectionRequest,
    ) -> polardbx_20200202_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_instance_public_connection_with_options_async(request, runtime)

    def cancel_active_operation_tasks_with_options(
        self,
        request: polardbx_20200202_models.CancelActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CancelActiveOperationTasksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CancelActiveOperationTasksResponse(),
            self.do_rpcrequest('CancelActiveOperationTasks', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def cancel_active_operation_tasks_with_options_async(
        self,
        request: polardbx_20200202_models.CancelActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CancelActiveOperationTasksResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CancelActiveOperationTasksResponse(),
            await self.do_rpcrequest_async('CancelActiveOperationTasks', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def cancel_active_operation_tasks(
        self,
        request: polardbx_20200202_models.CancelActiveOperationTasksRequest,
    ) -> polardbx_20200202_models.CancelActiveOperationTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_active_operation_tasks_with_options(request, runtime)

    async def cancel_active_operation_tasks_async(
        self,
        request: polardbx_20200202_models.CancelActiveOperationTasksRequest,
    ) -> polardbx_20200202_models.CancelActiveOperationTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_active_operation_tasks_with_options_async(request, runtime)

    def cancel_polarx_order_with_options(
        self,
        request: polardbx_20200202_models.CancelPolarxOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CancelPolarxOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CancelPolarxOrderResponse(),
            self.do_rpcrequest('CancelPolarxOrder', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_polarx_order_with_options_async(
        self,
        request: polardbx_20200202_models.CancelPolarxOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CancelPolarxOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CancelPolarxOrderResponse(),
            await self.do_rpcrequest_async('CancelPolarxOrder', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_polarx_order(
        self,
        request: polardbx_20200202_models.CancelPolarxOrderRequest,
    ) -> polardbx_20200202_models.CancelPolarxOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_polarx_order_with_options(request, runtime)

    async def cancel_polarx_order_async(
        self,
        request: polardbx_20200202_models.CancelPolarxOrderRequest,
    ) -> polardbx_20200202_models.CancelPolarxOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_polarx_order_with_options_async(request, runtime)

    def check_cloud_resource_authorized_with_options(
        self,
        request: polardbx_20200202_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CheckCloudResourceAuthorizedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CheckCloudResourceAuthorizedResponse(),
            self.do_rpcrequest('CheckCloudResourceAuthorized', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_cloud_resource_authorized_with_options_async(
        self,
        request: polardbx_20200202_models.CheckCloudResourceAuthorizedRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CheckCloudResourceAuthorizedResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CheckCloudResourceAuthorizedResponse(),
            await self.do_rpcrequest_async('CheckCloudResourceAuthorized', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_cloud_resource_authorized(
        self,
        request: polardbx_20200202_models.CheckCloudResourceAuthorizedRequest,
    ) -> polardbx_20200202_models.CheckCloudResourceAuthorizedResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    async def check_cloud_resource_authorized_async(
        self,
        request: polardbx_20200202_models.CheckCloudResourceAuthorizedRequest,
    ) -> polardbx_20200202_models.CheckCloudResourceAuthorizedResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_cloud_resource_authorized_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: polardbx_20200202_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateAccountResponse(),
            self.do_rpcrequest('CreateAccount', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: polardbx_20200202_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateAccountResponse(),
            await self.do_rpcrequest_async('CreateAccount', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_account(
        self,
        request: polardbx_20200202_models.CreateAccountRequest,
    ) -> polardbx_20200202_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: polardbx_20200202_models.CreateAccountRequest,
    ) -> polardbx_20200202_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: polardbx_20200202_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateBackupResponse(),
            self.do_rpcrequest('CreateBackup', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: polardbx_20200202_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateBackupResponse(),
            await self.do_rpcrequest_async('CreateBackup', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup(
        self,
        request: polardbx_20200202_models.CreateBackupRequest,
    ) -> polardbx_20200202_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: polardbx_20200202_models.CreateBackupRequest,
    ) -> polardbx_20200202_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_dbwith_options(
        self,
        request: polardbx_20200202_models.CreateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateDBResponse(),
            self.do_rpcrequest('CreateDB', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbwith_options_async(
        self,
        request: polardbx_20200202_models.CreateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateDBResponse(),
            await self.do_rpcrequest_async('CreateDB', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_db(
        self,
        request: polardbx_20200202_models.CreateDBRequest,
    ) -> polardbx_20200202_models.CreateDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbwith_options(request, runtime)

    async def create_db_async(
        self,
        request: polardbx_20200202_models.CreateDBRequest,
    ) -> polardbx_20200202_models.CreateDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbwith_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: polardbx_20200202_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateDBInstanceResponse(),
            self.do_rpcrequest('CreateDBInstance', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        request: polardbx_20200202_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateDBInstanceResponse(),
            await self.do_rpcrequest_async('CreateDBInstance', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbinstance(
        self,
        request: polardbx_20200202_models.CreateDBInstanceRequest,
    ) -> polardbx_20200202_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: polardbx_20200202_models.CreateDBInstanceRequest,
    ) -> polardbx_20200202_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_polarx_order_with_options(
        self,
        request: polardbx_20200202_models.CreatePolarxOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreatePolarxOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreatePolarxOrderResponse(),
            self.do_rpcrequest('CreatePolarxOrder', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_polarx_order_with_options_async(
        self,
        request: polardbx_20200202_models.CreatePolarxOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreatePolarxOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreatePolarxOrderResponse(),
            await self.do_rpcrequest_async('CreatePolarxOrder', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_polarx_order(
        self,
        request: polardbx_20200202_models.CreatePolarxOrderRequest,
    ) -> polardbx_20200202_models.CreatePolarxOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_polarx_order_with_options(request, runtime)

    async def create_polarx_order_async(
        self,
        request: polardbx_20200202_models.CreatePolarxOrderRequest,
    ) -> polardbx_20200202_models.CreatePolarxOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_polarx_order_with_options_async(request, runtime)

    def create_super_account_with_options(
        self,
        request: polardbx_20200202_models.CreateSuperAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateSuperAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateSuperAccountResponse(),
            self.do_rpcrequest('CreateSuperAccount', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_super_account_with_options_async(
        self,
        request: polardbx_20200202_models.CreateSuperAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.CreateSuperAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.CreateSuperAccountResponse(),
            await self.do_rpcrequest_async('CreateSuperAccount', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_super_account(
        self,
        request: polardbx_20200202_models.CreateSuperAccountRequest,
    ) -> polardbx_20200202_models.CreateSuperAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_super_account_with_options(request, runtime)

    async def create_super_account_async(
        self,
        request: polardbx_20200202_models.CreateSuperAccountRequest,
    ) -> polardbx_20200202_models.CreateSuperAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_super_account_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: polardbx_20200202_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteAccountResponse(),
            self.do_rpcrequest('DeleteAccount', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: polardbx_20200202_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteAccountResponse(),
            await self.do_rpcrequest_async('DeleteAccount', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_account(
        self,
        request: polardbx_20200202_models.DeleteAccountRequest,
    ) -> polardbx_20200202_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: polardbx_20200202_models.DeleteAccountRequest,
    ) -> polardbx_20200202_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_dbwith_options(
        self,
        request: polardbx_20200202_models.DeleteDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteDBResponse(),
            self.do_rpcrequest('DeleteDB', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbwith_options_async(
        self,
        request: polardbx_20200202_models.DeleteDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteDBResponse(),
            await self.do_rpcrequest_async('DeleteDB', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_db(
        self,
        request: polardbx_20200202_models.DeleteDBRequest,
    ) -> polardbx_20200202_models.DeleteDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbwith_options(request, runtime)

    async def delete_db_async(
        self,
        request: polardbx_20200202_models.DeleteDBRequest,
    ) -> polardbx_20200202_models.DeleteDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbwith_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: polardbx_20200202_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteDBInstanceResponse(),
            self.do_rpcrequest('DeleteDBInstance', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: polardbx_20200202_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DeleteDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DeleteDBInstanceResponse(),
            await self.do_rpcrequest_async('DeleteDBInstance', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbinstance(
        self,
        request: polardbx_20200202_models.DeleteDBInstanceRequest,
    ) -> polardbx_20200202_models.DeleteDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: polardbx_20200202_models.DeleteDBInstanceRequest,
    ) -> polardbx_20200202_models.DeleteDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def describe_account_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeAccountListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeAccountListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeAccountListResponse(),
            self.do_rpcrequest('DescribeAccountList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_account_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeAccountListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeAccountListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeAccountListResponse(),
            await self.do_rpcrequest_async('DescribeAccountList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_account_list(
        self,
        request: polardbx_20200202_models.DescribeAccountListRequest,
    ) -> polardbx_20200202_models.DescribeAccountListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_account_list_with_options(request, runtime)

    async def describe_account_list_async(
        self,
        request: polardbx_20200202_models.DescribeAccountListRequest,
    ) -> polardbx_20200202_models.DescribeAccountListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_list_with_options_async(request, runtime)

    def describe_active_operation_maintain_conf_with_options(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationMaintainConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeActiveOperationMaintainConfResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeActiveOperationMaintainConfResponse(),
            self.do_rpcrequest('DescribeActiveOperationMaintainConf', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_active_operation_maintain_conf_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationMaintainConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeActiveOperationMaintainConfResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeActiveOperationMaintainConfResponse(),
            await self.do_rpcrequest_async('DescribeActiveOperationMaintainConf', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_active_operation_maintain_conf(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationMaintainConfRequest,
    ) -> polardbx_20200202_models.DescribeActiveOperationMaintainConfResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_maintain_conf_with_options(request, runtime)

    async def describe_active_operation_maintain_conf_async(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationMaintainConfRequest,
    ) -> polardbx_20200202_models.DescribeActiveOperationMaintainConfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_maintain_conf_with_options_async(request, runtime)

    def describe_active_operation_task_count_with_options(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationTaskCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeActiveOperationTaskCountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeActiveOperationTaskCountResponse(),
            self.do_rpcrequest('DescribeActiveOperationTaskCount', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_active_operation_task_count_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationTaskCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeActiveOperationTaskCountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeActiveOperationTaskCountResponse(),
            await self.do_rpcrequest_async('DescribeActiveOperationTaskCount', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_active_operation_task_count(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationTaskCountRequest,
    ) -> polardbx_20200202_models.DescribeActiveOperationTaskCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_active_operation_task_count_with_options(request, runtime)

    async def describe_active_operation_task_count_async(
        self,
        request: polardbx_20200202_models.DescribeActiveOperationTaskCountRequest,
    ) -> polardbx_20200202_models.DescribeActiveOperationTaskCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_active_operation_task_count_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: polardbx_20200202_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBackupPolicyResponse(),
            self.do_rpcrequest('DescribeBackupPolicy', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBackupPolicyResponse(),
            await self.do_rpcrequest_async('DescribeBackupPolicy', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(
        self,
        request: polardbx_20200202_models.DescribeBackupPolicyRequest,
    ) -> polardbx_20200202_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: polardbx_20200202_models.DescribeBackupPolicyRequest,
    ) -> polardbx_20200202_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backup_set_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeBackupSetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBackupSetListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBackupSetListResponse(),
            self.do_rpcrequest('DescribeBackupSetList', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_backup_set_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeBackupSetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBackupSetListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBackupSetListResponse(),
            await self.do_rpcrequest_async('DescribeBackupSetList', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_backup_set_list(
        self,
        request: polardbx_20200202_models.DescribeBackupSetListRequest,
    ) -> polardbx_20200202_models.DescribeBackupSetListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_set_list_with_options(request, runtime)

    async def describe_backup_set_list_async(
        self,
        request: polardbx_20200202_models.DescribeBackupSetListRequest,
    ) -> polardbx_20200202_models.DescribeBackupSetListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_set_list_with_options_async(request, runtime)

    def describe_binary_log_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeBinaryLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBinaryLogListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBinaryLogListResponse(),
            self.do_rpcrequest('DescribeBinaryLogList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_binary_log_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeBinaryLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeBinaryLogListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeBinaryLogListResponse(),
            await self.do_rpcrequest_async('DescribeBinaryLogList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_binary_log_list(
        self,
        request: polardbx_20200202_models.DescribeBinaryLogListRequest,
    ) -> polardbx_20200202_models.DescribeBinaryLogListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_binary_log_list_with_options(request, runtime)

    async def describe_binary_log_list_async(
        self,
        request: polardbx_20200202_models.DescribeBinaryLogListRequest,
    ) -> polardbx_20200202_models.DescribeBinaryLogListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_binary_log_list_with_options_async(request, runtime)

    def describe_character_set_with_options(
        self,
        request: polardbx_20200202_models.DescribeCharacterSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeCharacterSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeCharacterSetResponse(),
            self.do_rpcrequest('DescribeCharacterSet', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_character_set_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeCharacterSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeCharacterSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeCharacterSetResponse(),
            await self.do_rpcrequest_async('DescribeCharacterSet', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_character_set(
        self,
        request: polardbx_20200202_models.DescribeCharacterSetRequest,
    ) -> polardbx_20200202_models.DescribeCharacterSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_character_set_with_options(request, runtime)

    async def describe_character_set_async(
        self,
        request: polardbx_20200202_models.DescribeCharacterSetRequest,
    ) -> polardbx_20200202_models.DescribeCharacterSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_character_set_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeDBInstanceAttribute', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceAttributeResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceAttribute', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceAttributeRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceAttributeRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_config_with_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceConfigResponse(),
            self.do_rpcrequest('DescribeDBInstanceConfig', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_config_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceConfigResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceConfig', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_config(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceConfigRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_config_with_options(request, runtime)

    async def describe_dbinstance_config_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceConfigRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_config_with_options_async(request, runtime)

    def describe_dbinstance_sslwith_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceSSLResponse(),
            self.do_rpcrequest('DescribeDBInstanceSSL', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_sslwith_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceSSLResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceSSL', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_ssl(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceSSLRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    async def describe_dbinstance_ssl_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceSSLRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_sslwith_options_async(request, runtime)

    def describe_dbinstance_tdewith_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceTDEResponse(),
            self.do_rpcrequest('DescribeDBInstanceTDE', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_tdewith_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceTDEResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceTDE', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_tde(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTDERequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_tdewith_options(request, runtime)

    async def describe_dbinstance_tde_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTDERequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_tdewith_options_async(request, runtime)

    def describe_dbinstance_topology_with_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceTopologyResponse(),
            self.do_rpcrequest('DescribeDBInstanceTopology', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_topology_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstanceTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstanceTopologyResponse(),
            await self.do_rpcrequest_async('DescribeDBInstanceTopology', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_topology(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTopologyRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_topology_with_options(request, runtime)

    async def describe_dbinstance_topology_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstanceTopologyRequest,
    ) -> polardbx_20200202_models.DescribeDBInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_topology_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        request: polardbx_20200202_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstancesResponse(),
            self.do_rpcrequest('DescribeDBInstances', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBInstancesResponse(),
            await self.do_rpcrequest_async('DescribeDBInstances', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances(
        self,
        request: polardbx_20200202_models.DescribeDBInstancesRequest,
    ) -> polardbx_20200202_models.DescribeDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: polardbx_20200202_models.DescribeDBInstancesRequest,
    ) -> polardbx_20200202_models.DescribeDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_dbnode_performance_with_options(
        self,
        request: polardbx_20200202_models.DescribeDBNodePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBNodePerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBNodePerformanceResponse(),
            self.do_rpcrequest('DescribeDBNodePerformance', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbnode_performance_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDBNodePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDBNodePerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDBNodePerformanceResponse(),
            await self.do_rpcrequest_async('DescribeDBNodePerformance', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbnode_performance(
        self,
        request: polardbx_20200202_models.DescribeDBNodePerformanceRequest,
    ) -> polardbx_20200202_models.DescribeDBNodePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbnode_performance_with_options(request, runtime)

    async def describe_dbnode_performance_async(
        self,
        request: polardbx_20200202_models.DescribeDBNodePerformanceRequest,
    ) -> polardbx_20200202_models.DescribeDBNodePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbnode_performance_with_options_async(request, runtime)

    def describe_db_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeDbListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDbListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDbListResponse(),
            self.do_rpcrequest('DescribeDbList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_db_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDbListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDbListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDbListResponse(),
            await self.do_rpcrequest_async('DescribeDbList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_db_list(
        self,
        request: polardbx_20200202_models.DescribeDbListRequest,
    ) -> polardbx_20200202_models.DescribeDbListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_db_list_with_options(request, runtime)

    async def describe_db_list_async(
        self,
        request: polardbx_20200202_models.DescribeDbListRequest,
    ) -> polardbx_20200202_models.DescribeDbListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_db_list_with_options_async(request, runtime)

    def describe_distribute_table_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeDistributeTableListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDistributeTableListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDistributeTableListResponse(),
            self.do_rpcrequest('DescribeDistributeTableList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_distribute_table_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeDistributeTableListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeDistributeTableListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeDistributeTableListResponse(),
            await self.do_rpcrequest_async('DescribeDistributeTableList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_distribute_table_list(
        self,
        request: polardbx_20200202_models.DescribeDistributeTableListRequest,
    ) -> polardbx_20200202_models.DescribeDistributeTableListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_distribute_table_list_with_options(request, runtime)

    async def describe_distribute_table_list_async(
        self,
        request: polardbx_20200202_models.DescribeDistributeTableListRequest,
    ) -> polardbx_20200202_models.DescribeDistributeTableListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_distribute_table_list_with_options_async(request, runtime)

    def describe_events_with_options(
        self,
        request: polardbx_20200202_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeEventsResponse(),
            self.do_rpcrequest('DescribeEvents', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_events_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeEventsResponse(),
            await self.do_rpcrequest_async('DescribeEvents', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_events(
        self,
        request: polardbx_20200202_models.DescribeEventsRequest,
    ) -> polardbx_20200202_models.DescribeEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    async def describe_events_async(
        self,
        request: polardbx_20200202_models.DescribeEventsRequest,
    ) -> polardbx_20200202_models.DescribeEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_events_with_options_async(request, runtime)

    def describe_parameter_templates_with_options(
        self,
        request: polardbx_20200202_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeParameterTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeParameterTemplatesResponse(),
            self.do_rpcrequest('DescribeParameterTemplates', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameter_templates_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeParameterTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeParameterTemplatesResponse(),
            await self.do_rpcrequest_async('DescribeParameterTemplates', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_templates(
        self,
        request: polardbx_20200202_models.DescribeParameterTemplatesRequest,
    ) -> polardbx_20200202_models.DescribeParameterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    async def describe_parameter_templates_async(
        self,
        request: polardbx_20200202_models.DescribeParameterTemplatesRequest,
    ) -> polardbx_20200202_models.DescribeParameterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_templates_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: polardbx_20200202_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeParametersResponse(),
            self.do_rpcrequest('DescribeParameters', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeParametersResponse(),
            await self.do_rpcrequest_async('DescribeParameters', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameters(
        self,
        request: polardbx_20200202_models.DescribeParametersRequest,
    ) -> polardbx_20200202_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: polardbx_20200202_models.DescribeParametersRequest,
    ) -> polardbx_20200202_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_polarx_data_nodes_with_options(
        self,
        request: polardbx_20200202_models.DescribePolarxDataNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribePolarxDataNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribePolarxDataNodesResponse(),
            self.do_rpcrequest('DescribePolarxDataNodes', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_polarx_data_nodes_with_options_async(
        self,
        request: polardbx_20200202_models.DescribePolarxDataNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribePolarxDataNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribePolarxDataNodesResponse(),
            await self.do_rpcrequest_async('DescribePolarxDataNodes', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_polarx_data_nodes(
        self,
        request: polardbx_20200202_models.DescribePolarxDataNodesRequest,
    ) -> polardbx_20200202_models.DescribePolarxDataNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_polarx_data_nodes_with_options(request, runtime)

    async def describe_polarx_data_nodes_async(
        self,
        request: polardbx_20200202_models.DescribePolarxDataNodesRequest,
    ) -> polardbx_20200202_models.DescribePolarxDataNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_polarx_data_nodes_with_options_async(request, runtime)

    def describe_polarx_db_instances_with_options(
        self,
        request: polardbx_20200202_models.DescribePolarxDbInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribePolarxDbInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribePolarxDbInstancesResponse(),
            self.do_rpcrequest('DescribePolarxDbInstances', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_polarx_db_instances_with_options_async(
        self,
        request: polardbx_20200202_models.DescribePolarxDbInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribePolarxDbInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribePolarxDbInstancesResponse(),
            await self.do_rpcrequest_async('DescribePolarxDbInstances', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_polarx_db_instances(
        self,
        request: polardbx_20200202_models.DescribePolarxDbInstancesRequest,
    ) -> polardbx_20200202_models.DescribePolarxDbInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_polarx_db_instances_with_options(request, runtime)

    async def describe_polarx_db_instances_async(
        self,
        request: polardbx_20200202_models.DescribePolarxDbInstancesRequest,
    ) -> polardbx_20200202_models.DescribePolarxDbInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_polarx_db_instances_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self) -> polardbx_20200202_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> polardbx_20200202_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def describe_scale_out_migrate_task_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeScaleOutMigrateTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeScaleOutMigrateTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeScaleOutMigrateTaskListResponse(),
            self.do_rpcrequest('DescribeScaleOutMigrateTaskList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scale_out_migrate_task_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeScaleOutMigrateTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeScaleOutMigrateTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeScaleOutMigrateTaskListResponse(),
            await self.do_rpcrequest_async('DescribeScaleOutMigrateTaskList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scale_out_migrate_task_list(
        self,
        request: polardbx_20200202_models.DescribeScaleOutMigrateTaskListRequest,
    ) -> polardbx_20200202_models.DescribeScaleOutMigrateTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scale_out_migrate_task_list_with_options(request, runtime)

    async def describe_scale_out_migrate_task_list_async(
        self,
        request: polardbx_20200202_models.DescribeScaleOutMigrateTaskListRequest,
    ) -> polardbx_20200202_models.DescribeScaleOutMigrateTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scale_out_migrate_task_list_with_options_async(request, runtime)

    def describe_security_ips_with_options(
        self,
        request: polardbx_20200202_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeSecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeSecurityIpsResponse(),
            self.do_rpcrequest('DescribeSecurityIps', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_ips_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeSecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeSecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeSecurityIpsResponse(),
            await self.do_rpcrequest_async('DescribeSecurityIps', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_ips(
        self,
        request: polardbx_20200202_models.DescribeSecurityIpsRequest,
    ) -> polardbx_20200202_models.DescribeSecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_ips_with_options(request, runtime)

    async def describe_security_ips_async(
        self,
        request: polardbx_20200202_models.DescribeSecurityIpsRequest,
    ) -> polardbx_20200202_models.DescribeSecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_ips_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: polardbx_20200202_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeTasksResponse(),
            self.do_rpcrequest('DescribeTasks', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeTasksResponse(),
            await self.do_rpcrequest_async('DescribeTasks', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tasks(
        self,
        request: polardbx_20200202_models.DescribeTasksRequest,
    ) -> polardbx_20200202_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: polardbx_20200202_models.DescribeTasksRequest,
    ) -> polardbx_20200202_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def describe_user_encryption_key_list_with_options(
        self,
        request: polardbx_20200202_models.DescribeUserEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeUserEncryptionKeyListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeUserEncryptionKeyListResponse(),
            self.do_rpcrequest('DescribeUserEncryptionKeyList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_encryption_key_list_with_options_async(
        self,
        request: polardbx_20200202_models.DescribeUserEncryptionKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.DescribeUserEncryptionKeyListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.DescribeUserEncryptionKeyListResponse(),
            await self.do_rpcrequest_async('DescribeUserEncryptionKeyList', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_encryption_key_list(
        self,
        request: polardbx_20200202_models.DescribeUserEncryptionKeyListRequest,
    ) -> polardbx_20200202_models.DescribeUserEncryptionKeyListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_encryption_key_list_with_options(request, runtime)

    async def describe_user_encryption_key_list_async(
        self,
        request: polardbx_20200202_models.DescribeUserEncryptionKeyListRequest,
    ) -> polardbx_20200202_models.DescribeUserEncryptionKeyListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_encryption_key_list_with_options_async(request, runtime)

    def get_polarx_commodity_with_options(
        self,
        request: polardbx_20200202_models.GetPolarxCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.GetPolarxCommodityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.GetPolarxCommodityResponse(),
            self.do_rpcrequest('GetPolarxCommodity', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_polarx_commodity_with_options_async(
        self,
        request: polardbx_20200202_models.GetPolarxCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.GetPolarxCommodityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.GetPolarxCommodityResponse(),
            await self.do_rpcrequest_async('GetPolarxCommodity', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_polarx_commodity(
        self,
        request: polardbx_20200202_models.GetPolarxCommodityRequest,
    ) -> polardbx_20200202_models.GetPolarxCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_polarx_commodity_with_options(request, runtime)

    async def get_polarx_commodity_async(
        self,
        request: polardbx_20200202_models.GetPolarxCommodityRequest,
    ) -> polardbx_20200202_models.GetPolarxCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_polarx_commodity_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: polardbx_20200202_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyAccountDescriptionResponse(),
            self.do_rpcrequest('ModifyAccountDescription', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyAccountDescriptionResponse(),
            await self.do_rpcrequest_async('ModifyAccountDescription', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(
        self,
        request: polardbx_20200202_models.ModifyAccountDescriptionRequest,
    ) -> polardbx_20200202_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: polardbx_20200202_models.ModifyAccountDescriptionRequest,
    ) -> polardbx_20200202_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_active_operation_maintain_conf_with_options(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationMaintainConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyActiveOperationMaintainConfResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyActiveOperationMaintainConfResponse(),
            self.do_rpcrequest('ModifyActiveOperationMaintainConf', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def modify_active_operation_maintain_conf_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationMaintainConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyActiveOperationMaintainConfResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyActiveOperationMaintainConfResponse(),
            await self.do_rpcrequest_async('ModifyActiveOperationMaintainConf', '2020-02-02', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def modify_active_operation_maintain_conf(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationMaintainConfRequest,
    ) -> polardbx_20200202_models.ModifyActiveOperationMaintainConfResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_maintain_conf_with_options(request, runtime)

    async def modify_active_operation_maintain_conf_async(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationMaintainConfRequest,
    ) -> polardbx_20200202_models.ModifyActiveOperationMaintainConfResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_active_operation_maintain_conf_with_options_async(request, runtime)

    def modify_active_operation_tasks_with_options(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyActiveOperationTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyActiveOperationTasksResponse(),
            self.do_rpcrequest('ModifyActiveOperationTasks', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_active_operation_tasks_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyActiveOperationTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyActiveOperationTasksResponse(),
            await self.do_rpcrequest_async('ModifyActiveOperationTasks', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_active_operation_tasks(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationTasksRequest,
    ) -> polardbx_20200202_models.ModifyActiveOperationTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_active_operation_tasks_with_options(request, runtime)

    async def modify_active_operation_tasks_async(
        self,
        request: polardbx_20200202_models.ModifyActiveOperationTasksRequest,
    ) -> polardbx_20200202_models.ModifyActiveOperationTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_active_operation_tasks_with_options_async(request, runtime)

    def modify_dbinstance_class_with_options(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceClassResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceClassResponse(),
            self.do_rpcrequest('ModifyDBInstanceClass', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_class_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceClassResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceClassResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceClass', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_class(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceClassRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceClassResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_class_with_options(request, runtime)

    async def modify_dbinstance_class_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceClassRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceClassResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_class_with_options_async(request, runtime)

    def modify_dbinstance_config_with_options(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceConfigResponse(),
            self.do_rpcrequest('ModifyDBInstanceConfig', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_config_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceConfigResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceConfig', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_config(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceConfigRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_config_with_options(request, runtime)

    async def modify_dbinstance_config_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceConfigRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_config_with_options_async(request, runtime)

    def modify_dbinstance_description_with_options(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceDescriptionResponse(),
            self.do_rpcrequest('ModifyDBInstanceDescription', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_description_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDBInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDBInstanceDescriptionResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceDescription', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_description(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceDescriptionRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    async def modify_dbinstance_description_async(
        self,
        request: polardbx_20200202_models.ModifyDBInstanceDescriptionRequest,
    ) -> polardbx_20200202_models.ModifyDBInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_description_with_options_async(request, runtime)

    def modify_database_description_with_options(
        self,
        request: polardbx_20200202_models.ModifyDatabaseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDatabaseDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDatabaseDescriptionResponse(),
            self.do_rpcrequest('ModifyDatabaseDescription', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_database_description_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyDatabaseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyDatabaseDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyDatabaseDescriptionResponse(),
            await self.do_rpcrequest_async('ModifyDatabaseDescription', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_database_description(
        self,
        request: polardbx_20200202_models.ModifyDatabaseDescriptionRequest,
    ) -> polardbx_20200202_models.ModifyDatabaseDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_database_description_with_options(request, runtime)

    async def modify_database_description_async(
        self,
        request: polardbx_20200202_models.ModifyDatabaseDescriptionRequest,
    ) -> polardbx_20200202_models.ModifyDatabaseDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_database_description_with_options_async(request, runtime)

    def modify_parameter_with_options(
        self,
        request: polardbx_20200202_models.ModifyParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyParameterResponse(),
            self.do_rpcrequest('ModifyParameter', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_parameter_with_options_async(
        self,
        request: polardbx_20200202_models.ModifyParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifyParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifyParameterResponse(),
            await self.do_rpcrequest_async('ModifyParameter', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_parameter(
        self,
        request: polardbx_20200202_models.ModifyParameterRequest,
    ) -> polardbx_20200202_models.ModifyParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_with_options(request, runtime)

    async def modify_parameter_async(
        self,
        request: polardbx_20200202_models.ModifyParameterRequest,
    ) -> polardbx_20200202_models.ModifyParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameter_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: polardbx_20200202_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifySecurityIpsResponse(),
            self.do_rpcrequest('ModifySecurityIps', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: polardbx_20200202_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ModifySecurityIpsResponse(),
            await self.do_rpcrequest_async('ModifySecurityIps', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_ips(
        self,
        request: polardbx_20200202_models.ModifySecurityIpsRequest,
    ) -> polardbx_20200202_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: polardbx_20200202_models.ModifySecurityIpsRequest,
    ) -> polardbx_20200202_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def release_instance_public_connection_with_options(
        self,
        request: polardbx_20200202_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ReleaseInstancePublicConnectionResponse(),
            self.do_rpcrequest('ReleaseInstancePublicConnection', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_instance_public_connection_with_options_async(
        self,
        request: polardbx_20200202_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.ReleaseInstancePublicConnectionResponse(),
            await self.do_rpcrequest_async('ReleaseInstancePublicConnection', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance_public_connection(
        self,
        request: polardbx_20200202_models.ReleaseInstancePublicConnectionRequest,
    ) -> polardbx_20200202_models.ReleaseInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    async def release_instance_public_connection_async(
        self,
        request: polardbx_20200202_models.ReleaseInstancePublicConnectionRequest,
    ) -> polardbx_20200202_models.ReleaseInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_public_connection_with_options_async(request, runtime)

    def restart_dbinstance_with_options(
        self,
        request: polardbx_20200202_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.RestartDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.RestartDBInstanceResponse(),
            self.do_rpcrequest('RestartDBInstance', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_dbinstance_with_options_async(
        self,
        request: polardbx_20200202_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.RestartDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.RestartDBInstanceResponse(),
            await self.do_rpcrequest_async('RestartDBInstance', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_dbinstance(
        self,
        request: polardbx_20200202_models.RestartDBInstanceRequest,
    ) -> polardbx_20200202_models.RestartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: polardbx_20200202_models.RestartDBInstanceRequest,
    ) -> polardbx_20200202_models.RestartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def update_backup_policy_with_options(
        self,
        request: polardbx_20200202_models.UpdateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdateBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateBackupPolicyResponse(),
            self.do_rpcrequest('UpdateBackupPolicy', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_backup_policy_with_options_async(
        self,
        request: polardbx_20200202_models.UpdateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdateBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateBackupPolicyResponse(),
            await self.do_rpcrequest_async('UpdateBackupPolicy', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_backup_policy(
        self,
        request: polardbx_20200202_models.UpdateBackupPolicyRequest,
    ) -> polardbx_20200202_models.UpdateBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_backup_policy_with_options(request, runtime)

    async def update_backup_policy_async(
        self,
        request: polardbx_20200202_models.UpdateBackupPolicyRequest,
    ) -> polardbx_20200202_models.UpdateBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_backup_policy_with_options_async(request, runtime)

    def update_dbinstance_sslwith_options(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdateDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateDBInstanceSSLResponse(),
            self.do_rpcrequest('UpdateDBInstanceSSL', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dbinstance_sslwith_options_async(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdateDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateDBInstanceSSLResponse(),
            await self.do_rpcrequest_async('UpdateDBInstanceSSL', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dbinstance_ssl(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceSSLRequest,
    ) -> polardbx_20200202_models.UpdateDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dbinstance_sslwith_options(request, runtime)

    async def update_dbinstance_ssl_async(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceSSLRequest,
    ) -> polardbx_20200202_models.UpdateDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dbinstance_sslwith_options_async(request, runtime)

    def update_dbinstance_tdewith_options(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdateDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateDBInstanceTDEResponse(),
            self.do_rpcrequest('UpdateDBInstanceTDE', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dbinstance_tdewith_options_async(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdateDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdateDBInstanceTDEResponse(),
            await self.do_rpcrequest_async('UpdateDBInstanceTDE', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dbinstance_tde(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceTDERequest,
    ) -> polardbx_20200202_models.UpdateDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dbinstance_tdewith_options(request, runtime)

    async def update_dbinstance_tde_async(
        self,
        request: polardbx_20200202_models.UpdateDBInstanceTDERequest,
    ) -> polardbx_20200202_models.UpdateDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dbinstance_tdewith_options_async(request, runtime)

    def update_polar_dbxinstance_node_with_options(
        self,
        request: polardbx_20200202_models.UpdatePolarDBXInstanceNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdatePolarDBXInstanceNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdatePolarDBXInstanceNodeResponse(),
            self.do_rpcrequest('UpdatePolarDBXInstanceNode', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_polar_dbxinstance_node_with_options_async(
        self,
        request: polardbx_20200202_models.UpdatePolarDBXInstanceNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpdatePolarDBXInstanceNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpdatePolarDBXInstanceNodeResponse(),
            await self.do_rpcrequest_async('UpdatePolarDBXInstanceNode', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_polar_dbxinstance_node(
        self,
        request: polardbx_20200202_models.UpdatePolarDBXInstanceNodeRequest,
    ) -> polardbx_20200202_models.UpdatePolarDBXInstanceNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_polar_dbxinstance_node_with_options(request, runtime)

    async def update_polar_dbxinstance_node_async(
        self,
        request: polardbx_20200202_models.UpdatePolarDBXInstanceNodeRequest,
    ) -> polardbx_20200202_models.UpdatePolarDBXInstanceNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_polar_dbxinstance_node_with_options_async(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(
        self,
        request: polardbx_20200202_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpgradeDBInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpgradeDBInstanceKernelVersionResponse(),
            self.do_rpcrequest('UpgradeDBInstanceKernelVersion', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_dbinstance_kernel_version_with_options_async(
        self,
        request: polardbx_20200202_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> polardbx_20200202_models.UpgradeDBInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            polardbx_20200202_models.UpgradeDBInstanceKernelVersionResponse(),
            await self.do_rpcrequest_async('UpgradeDBInstanceKernelVersion', '2020-02-02', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbinstance_kernel_version(
        self,
        request: polardbx_20200202_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> polardbx_20200202_models.UpgradeDBInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)

    async def upgrade_dbinstance_kernel_version_async(
        self,
        request: polardbx_20200202_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> polardbx_20200202_models.UpgradeDBInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_kernel_version_with_options_async(request, runtime)
